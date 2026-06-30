---
name: tuvi-dau-so-expert
description: >
  Hệ thống luận giải Tử Vi Đẩu Số chuyên sâu. Dùng khi người dùng hỏi về
  tử vi, lá số, vận trình, sự nghiệp, tài chính, hôn nhân, sức khỏe, hoặc
  bất kỳ câu hỏi liên quan đến Tử Vi Đẩu Số phương Đông. Bao gồm đầy đủ:
  an sao, Tứ Hóa, Phi Hóa, 12 cung, đại hạn, tiểu hạn, lưu niên, cách cục,
  và framework luận giải theo từng người cụ thể.
version: "1.0"
author: "Built for Hermes Agent"
requires:
  - reference/AN_SAO.md
  - reference/PHI_HOA.md
  - reference/CACH_CUC.md
  - reference/VAN_HANH.md
  - data/BANG_TRA.md
---

# TỬ VI ĐẨU SỐ — SKILL LUẬN GIẢI CHUYÊN SÂU

## 🏛️ KIẾN TRÚC HỆ THỐNG TỬ VI

Skill này là **MASTER ENTRY POINT** cho toàn bộ hệ thống luận giải Tử Vi. Quy tắc routing:

```
User hỏi về Tử Vi / lá số / vận hạn
    │
    ▼
┌──────────────────────────────────────────────────────┐
│         🏛️ tuvi-dau-so-expert (MASTER)               │
│  Thu thập info → Lập lá số → Luận giải tổng thể       │
│  Dispatch tới subsystem khi cần chuyên sâu             │
└─────────────┬──────────────────────┬─────────────────┘
              │                      │
              ▼                      ▼
┌──────────────────────┐  ┌──────────────────────────┐
│ 🔄 Vận hạn chi tiết   │  │ 📜 Tứ Trụ / Bát Tự       │
│ tuvi-luu-nguyet-nhat │  │ tuvi-tu-tru-expert        │
│ (Python engine,       │  │ (BaZi, Dụng Thần,        │
│  chạy độc lập)        │  │  Đại Vận, Cách Cục)      │
└──────────────────────┘  └──────────────────────────┘
              │
     ┌────────┼────────┐
     ▼        ▼        ▼
┌────────┐┌────────┐┌──────────┐
│ ☯ Kinh  ││ 🏠 Phong││ ⚙️ MCP  │
│ Dịch    ││ Thủy   ││ Server  │
│ kinh-   ││ phong- ││ (iztro) │
│ dich-   ││ thuy-  ││ tuvi-   │
│ expert  ││ expert ││ mcp-    │
│         ││        ││ server  │
└────────┘└────────┘└──────────┘
```

### Routing rules (tự động dispatch)

| User hỏi về | Load skill | Ghi chú |
|---|---|---|
| Lá số tổng thể, 12 cung, sao, cách cục | `tuvi-dau-so-expert` (skill này) | Entry point mặc định |
| Tháng này thế nào, ngày mai sao, tuần tới | + `tuvi-luu-nguyet-nhat` | Dùng Python engine chạy Lưu Nguyệt/Nhật |
| Bát Tự, Tứ Trụ, Dụng Thần, Đại Vận | + `tuvi-tu-tru-expert` | Tử Bình Lạc Việt, 10 bước luận |
| Gieo quẻ, luận quẻ, 64 quẻ dịch | + `tuvi-kinh-dich-expert` | Chuyên đề Kinh Dịch |
| Hướng nhà, màu sắc, vật phẩm | + `tuvi-phong-thuy-expert` | Phong Thủy theo Dụng Thần |
| Cần tính toán tự động (an sao, đại hạn) | + `tuvi-mcp-server` | MCP iztro, ưu tiên khi có sẵn |

### Skill hierarchy (dành cho người quản trị)

- **Level 1 — Master:** `tuvi-dau-so-expert` ← bạn đang đọc
- **Level 2 — Chuyên ngành:** `tuvi-tu-tru-expert`, `tuvi-kinh-dich-expert`, `tuvi-phong-thuy-expert`
- **Level 3 — Engine:** `tuvi-luu-nguyet-nhat` (Python), `tuvi-mcp-server` (MCP iztro)
- **Đã absorb/delete:** `tuvi-bat-tu-expert` → merged vào `tuvi-tu-tru-expert`, `tuvi-expert` (cũ) → redirect

---

## CÁCH SỬ DỤNG SKILL NÀY

Khi người dùng hỏi về tử vi, thực hiện theo trình tự:

### BƯỚC 1 — THU THẬP THÔNG TIN
Hỏi đủ 5 yếu tố bắt buộc:
1. **Ngày sinh** (dương lịch)
2. **Tháng sinh** (dương lịch)
3. **Năm sinh** (dương lịch)
4. **Giờ sinh** (giờ địa phương — hỏi kỹ nếu không chắc)
5. **Giới tính** (ảnh hưởng hướng đại hạn)

Hỏi thêm nếu cần:
- Câu hỏi cụ thể (sự nghiệp? tài chính? tình duyên? sức khỏe?)
- Năm/giai đoạn quan tâm
- Bối cảnh hiện tại (đang làm gì, vấn đề đang gặp)

### BƯỚC 2 — LẬP LÁ SỐ

**Lưu ý về công cụ:** Do hạn chế về quyền truy cập hoặc credits của các MCP tools, khi các lệnh MCP không hoạt động hoặc không có sẵn, cần chủ động yêu cầu người dùng cung cấp đường link tới trang web tính lá số Tử Vi Đẩu Số uy tín hoặc cung cấp trực tiếp dữ liệu lá số để tiếp tục phân tích. Sử dụng `browser_navigate` để truy cập các trang web được cung cấp.

Đọc `reference/AN_SAO.md` để an sao chính xác:
- Tính Can Chi năm → Cục
- An Cung Mệnh, Cung Thân
- An 14 Chính tinh
- An các sao phụ quan trọng (Lộc Tồn, Kình/Đà, Khôi/Việt, Xương/Khúc, Không/Kiếp...)
- Đặt Tứ Hóa theo Can năm sinh

### BƯỚC 3 — ĐỌC TỔNG THỂ TRƯỚC
Không đọc từng sao riêng lẻ. Đọc theo thứ tự:
1. **Cung Mệnh + Thân** — Bản chất, khí chất, xu hướng tổng thể
2. **Tam Phương Tứ Chính** — Mệnh/Tài/Quan/Di hoặc theo câu hỏi
3. **Cách Cục** — Nhận diện pattern tổng thể (xem `reference/CACH_CUC.md`)
4. **Tứ Hóa vị trí** — Lộc/Quyền/Khoa/Kỵ đang kích thích cung nào

### BƯỚC 4 — ĐI VÀO VẤN ĐỀ CỤ THỂ
Tùy câu hỏi, focus vào cung liên quan:
- Sự nghiệp → Quan Lộc + Nô Bộc + Thiên Di
- Tài chính → Tài Bạch + Điền Trạch + Phúc Đức
- Tình duyên → Phu Thê + Huynh Đệ + Phúc Đức
- Sức khỏe → Tật Ách + Phụ Mẫu
- Con cái → Tử Tức

### Bước 5 — Luận vận hạn
Đọc `reference/VAN_HANH.md`:
- Xác định Đại hạn hiện tại
- Lưu niên năm hỏi
- Tương tác đa lớp
- Dự báo cụ thể
- Ưu tiên giải pháp thực tế (kinh doanh, nghề nghiệp)
- Luôn kết hợp phong thủy màu sắc/hướng theo hành của mệnh chủ

### BƯỚC 6 — PHI HÓA NÂNG CAO (nếu cần sâu hơn)
Đọc `reference/PHI_HOA.md` khi:
- Cần giải thích tại sao tiền đến/đi qua đâu
- Mối quan hệ giữa các cung tương tác thế nào
- Tình huống phức tạp cần phân tích nhiều lớp

---

## NGUYÊN TẮC LUẬN GIẢI

**Nguyên tắc 1 — Không đọc sao đơn lẻ**
Tham Lang một mình không nói lên gì. Tham Lang Miếu + Hóa Lộc + tại Mệnh = cách hoàn toàn khác.

**Nguyên tắc 2 — Tam Phương là đơn vị cơ bản**
Luôn đọc cung trong bối cảnh tam hợp của nó. Cung Quan Lộc cần đọc cùng Mệnh và Tài Bạch.

**Nguyên tắc 3 — Vận hạn phải khớp với bản mệnh**
Đại hạn tốt mà Mệnh yếu = vẫn khó. Đại hạn xấu mà Mệnh mạnh = chịu được.

**Nguyên tắc 4 — Luận theo ngữ cảnh người thực**
Cùng lá số nhưng người 25t và 50t đọc khác. Người kinh doanh và người làm công đọc khác. Hỏi bối cảnh trước khi luận.

**Nguyên tắc 5 — Không phán định mệnh số tuyệt đối**
Tử vi cho thấy xu hướng và thời điểm, không phải định mệnh cứng. Luôn nhấn mạnh yếu tố con người có thể điều chỉnh.

---

## VÍ DỤ LUẬN GIẢI MẪU

### Câu hỏi: "Sự nghiệp năm nay thế nào?"

**Thu thập:** Đủ 5 thông tin cơ bản + năm hỏi

**Lập lá số → Focus Quan Lộc:**
- Sao chính tại Quan Lộc là gì? Miếu/Hãm?
- Tứ Hóa nào đang nhập Quan Lộc (bản mệnh + đại hạn + lưu niên)?
- Cung Nô Bộc (nhân sự/đối tác) và Thiên Di (cơ hội bên ngoài) ra sao?

**Đọc Vận hạn:**
- Đại hạn hiện tại tốt/xấu với Quan Lộc?
- Lưu niên năm đó Thái Tuế đứng cung nào?
- Lưu nguyệt tháng nào thuận nhất để hành động?
- Chi tiết Lưu Nguyệt/Lưu Nhật → dùng skill `tuvi-luu-nguyet-nhat` (module Python chuyên dụng, chạy độc lập không cần MCP)

**Output:** Xu hướng tổng thể + tháng nên hành động + tháng cẩn thận + lời khuyên cụ thể

---

## CÁC FILE THAM KHẢO

| File | Nội dung | Khi nào dùng |
|------|----------|--------------|
| `reference/AN_SAO.md` | Thuật toán an sao đầy đủ | Mỗi lần lập lá số |
| `reference/PHI_HOA.md` | Kỹ thuật Phi Hóa | Phân tích sâu |
| `reference/CACH_CUC.md` | 51+ cách cục | Nhận diện pattern |
| `reference/VAN_HANH.md` | Framework vận hạn | Luận vận trình |
| `data/BANG_TRA.md` | Bảng tra nhanh | Tra cứu trong lúc an sao |
| `tuvi-luu-nguyet-nhat` | Skill con — Lưu Nguyệt/Nhật | Khi cần xem tháng/ngày chi tiết (có script Python riêng) |

---

## MCP TOOLS — TÍCH HỢP TÍNH TOÁN TỰ ĐỘNG

Đọc `data/MCP_TOOLS.md` để biết MCP nào đang available và cách dùng.

**Ưu tiên dùng MCP khi:**
- Cần an sao chính xác (tránh tính tay sai)
- Cross-validate giữa Tử Vi và Bát Tự
- Tính Đại hạn / Lưu niên / Lưu nguyệt tự động

**Thứ tự ưu tiên:**
1. `wuunicorn/MCPIztro` → Tử Vi chính
2. `cantian-ai/bazi-mcp` → Bát Tự verify
3. `spyfree/mingli-mcp` → Cả hai cùng lúc

---

## OUTPUT — TRÌNH BÀY TRÊN TELEGRAM

Tham khảo `tuvi-tu-tru-expert/references/TELEGRAM_FORMAT.md` cho quy tắc format chung.

> **Tóm tắt:** Chia 3-4 tin ngắn. Emoji nhất quán (📜=Tứ Trụ, 🏛️=Tử Vi, 🎯=Hành động). Bold keyword chính. Spoiler cho chi tiết. Luôn kết thúc = hành động.
