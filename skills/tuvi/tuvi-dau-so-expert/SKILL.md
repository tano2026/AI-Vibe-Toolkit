---
name: tuvi-dau-so-expert
description: >
  Hệ thống luận giải Tử Vi Đẩu Số chuyên sâu. Dùng khi người dùng hỏi về
  tử vi, lá số, vận trình, sự nghiệp, tài chính, hôn nhân, sức khỏe, hoặc
  bất kỳ câu hỏi liên quan đến Tử Vi Đẩu Số phương Đông. Bao gồm đầy đủ:
  an sao, Tứ Hóa, Phi Hóa, 12 cung, đại hạn, tiểu hạn, lưu niên, cách cục,
  và framework luận giải theo từng người cụ thể.
version: "1.1"
author: "Built for Hermes Agent"
updated: "2026-09-23 — đồng bộ với engine tuvi_calc.py (Tiểu Hạn, Quốc Ấn, Tứ Hóa Phi Tinh hội tụ, câu hỏi đương số)"
requires:
  - references/AN_SAO.md
  - references/PHI_HOA.md
  - references/CACH_CUC.md
  - references/VAN_HANH.md
  - references/BANG_TRA.md
---

# TỬ VI ĐẨU SỐ — SKILL LUẬN GIẢI CHUYÊN SÂU

## 🏛️ VỊ TRÍ TRONG HỆ THỐNG

Skill này là **CORE ENGINE TỬ VI** (subsystem cấp 2) trong hệ thống `tuvi-agent`, cung cấp dữ liệu nền tảng và luận giải cơ bản. 
**MASTER ENTRY POINT** duy nhất là `tuvi-agent` để tích hợp các bridge layer nâng cao (Tâm lý học hành vi, Định luật vũ trụ, Cổ nhân thuật, Nhân tính học, Khắc kỷ). Quy tắc routing:

```
User hỏi về Tử Vi / lá số / vận hạn
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│        🏛️ tuvi-agent (MASTER — entry point duy nhất)    │
│  5 tầng: Input → Core → Bridge → Domain → Output        │
│  Tích hợp Bridge (tâm lý, định luật, cổ nhân) + Domain   │
└───────────────────────┬──────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────┐
│    ⚙️ tuvi-dau-so-expert (skill này — Core Tử Vi)    │
│  Thu thập info → Lập lá số → Luận giải 12 cung        │
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

### Routing rules (tự động dispatch từ master `tuvi-agent`)

| User hỏi về | Load subsystem | Ghi chú |
|---|---|---|
| Lá số tổng thể, 12 cung, sao, cách cục → dispatch | `tuvi-dau-so-expert` (skill này) | Core Tử Vi engine |
| Tháng này thế nào, ngày mai sao, tuần tới | + `tuvi-luu-nguyet-nhat` | **Chạy Python engine qua `execute_code()`** — gọi `xem_luu_nguyet()` hoặc `xem_luu_nhat()` trực tiếp. Không chỉ load skill. |
| Bát Tự, Tứ Trụ, Dụng Thần, Đại Vận | + `tuvi-tu-tru-expert` | Tử Bình Lạc Việt, 10 bước luận |
| Gieo quẻ, luận quẻ, 64 quẻ dịch | + `tuvi-kinh-dich-expert` | Chuyên đề Kinh Dịch |
| Hướng nhà, màu sắc, vật phẩm | + `tuvi-phong-thuy-expert` | Phong Thủy theo Dụng Thần |
| Cần bridge (tâm lý / định luật / cổ nhân) | + `tuvi-agent` (bridge layers) | Overconfidence, Murphy, cổ nhân thuật |
| Cần domain (công sở / đầu tư / quan hệ) | + `tuvi-agent` (domain modules) | Áp dụng vào đời thực |
| Cần tính toán tự động (an sao, đại hạn) | + `tuvi-mcp-server` | MCP iztro, ưu tiên khi có sẵn |

### Skill hierarchy

- **Level 1 — Master:** `tuvi-agent` ← entry point duy nhất (5 tầng, bridge, domain)
- **Level 2 — Core Engine:** `tuvi-dau-so-expert` ← skill này (Tử Vi Đẩu Số)
- **Level 2 — Chuyên ngành:** `tuvi-tu-tru-expert`, `tuvi-kinh-dich-expert`, `tuvi-phong-thuy-expert`
- **Level 3 — Engine:** `tuvi-luu-nguyet-nhat` (Python), `tuvi-mcp-server` (MCP iztro)
- **Đã absorb/delete:** `tuvi-bat-tu-expert` → merged vào `tuvi-tu-tru-expert`, `tuvi-holistic-analysis` → absorb vào `tuvi-agent`, `tuvi-expert` (cũ) → redirect

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

⚠️ Xác nhận lại ngày sinh **bằng chữ** ("ngày X tháng Y năm Z dương lịch") — không suy diễn từ "1/5/1984":
với ngày ≤ 12, đọc ngày/tháng kiểu Việt hay Mỹ đều ra số hợp lệ nhưng ra lá số sai người; và phải phân biệt dương/âm lịch.

Hỏi thêm (nên hỏi — đây là phần khách quan tâm nhất):
- **Câu hỏi/mối bận tâm chính hiện tại** (sự nghiệp? tài chính? tình duyên? sức khỏe? có nên chuyển việc không?) → lưu vào trường `cau_hoi` để bài luận trả lời trực tiếp
- Năm/giai đoạn quan tâm
- Bối cảnh hiện tại (đang làm gì, vấn đề đang gặp)

### BƯỚC 2 — LẬP LÁ SỐ

**Engine ưu tiên số 1 (2026-09-23):** `D:\tano-tuvi-platform\skills\tuvi-master\scripts\tuvi_calc.py`
(`python tuvi_calc.py <Y> <M> <D> <H> <phút> "Tên" "Nơi sinh" nam|nu [năm_xem] out.json`, rồi
`generate_reading.py` / `render_chart.py`). Đã verify bằng 2 phương pháp + case thật; có giờ mặt trời thật
(`solar_time.py`, chỉ tham khảo, KHÔNG tự đổi giờ Chi), Tiểu Hạn, tạp diệu (gồm Quốc Ấn). MCP iztro chỉ để đối chiếu.

**Lưu ý về công cụ:** Do hạn chế về quyền truy cập hoặc credits của các MCP tools, khi các lệnh MCP không hoạt động hoặc không có sẵn, cần chủ động yêu cầu người dùng cung cấp đường link tới trang web tính lá số Tử Vi Đẩu Số uy tín hoặc cung cấp trực tiếp dữ liệu lá số để tiếp tục phân tích. Sử dụng `browser_navigate` để truy cập các trang web được cung cấp.

Đọc `references/AN_SAO.md` để an sao chính xác:
- Tính Can Chi năm → Cục
- An Cung Mệnh, Cung Thân
- An 14 Chính tinh
- An các sao phụ quan trọng (Lộc Tồn, Kình/Đà, Khôi/Việt, Xương/Khúc, Không/Kiếp...)
- Đặt Tứ Hóa theo Can năm sinh

### BƯỚC 3 — ĐỌC TỔNG THỂ TRƯỚC
Không đọc từng sao riêng lẻ. Đọc theo thứ tự:
1. **Cung Mệnh + Thân** — Bản chất, khí chất, xu hướng tổng thể
2. **Tam Phương Tứ Chính** — Mệnh/Tài/Quan/Di hoặc theo câu hỏi. Đây là cơ chế "chiếu": đánh giá Mệnh
   mạnh/yếu phải nhìn cả khối 4 cung, không chỉ riêng cung Mệnh. **Mệnh vô chính diệu → mượn sao từ khối
   Tam Phương Tứ Chính** (không được bỏ trống phần luận).
   Kèm **Giáp Cung** (2 cung kẹp hai bên Mệnh: Huynh Đệ + Phụ Mẫu) — môi trường sát cạnh đỡ hay kéo.
3. **Cách Cục** — Nhận diện pattern tổng thể (xem `references/CACH_CUC.md`)
4. **Tứ Hóa vị trí** — Lộc/Quyền/Khoa/Kỵ đang kích thích cung nào

### BƯỚC 4 — ĐI VÀO VẤN ĐỀ CỤ THỂ
Tùy câu hỏi, focus vào cung liên quan:
- Sự nghiệp → Quan Lộc + Nô Bộc + Thiên Di
- Tài chính → Tài Bạch + Điền Trạch + Phúc Đức
- Tình duyên → Phu Thê + Huynh Đệ + Phúc Đức
- Sức khỏe → Tật Ách + Phụ Mẫu
- Con cái → Tử Tức

### Bước 5 — Luận vận hạn
Đọc `references/VAN_HANH.md`. **3 lớp hạn, đừng gộp nhầm:**
- **Đại Hạn** (10 năm): chiều thuận/nghịch theo **Can năm sinh (âm/dương) + giới tính**
- **Tiểu Hạn** (từng năm tuổi): chiều thuận/nghịch theo **CHỈ giới tính** (không phụ thuộc Can), điểm khởi theo
  tam hợp của Chi năm sinh — công thức trong `get_tieu_han_branch()` của `tuvi_calc.py` (đã khớp case thật:
  cưới 2012 lúc 24 tuổi → Tiểu Hạn cung Thân). Đây là lớp trước đây bị thiếu giữa Đại Hạn và Lưu Niên.
- **Lưu Niên / Thái Tuế** (sao lưu theo năm dương lịch đang xem)
- Khi Tiểu Hạn trùng cung Đại Hạn = 2 lớp cùng dồn 1 chỗ, năm bản lề; trùng cung Mệnh = năm nhìn lại chính mình
- Trả lời "có nên làm X BÂY GIỜ không": xem cung liên quan tới X có đúng là cung Đại Hạn/Tiểu Hạn hiện tại không

Các bước:
- Xác định Đại hạn hiện tại
- Lưu niên năm hỏi
- Tương tác đa lớp
- Dự báo cụ thể
- Ưu tiên giải pháp thực tế (kinh doanh, nghề nghiệp)
- Luôn kết hợp phong thủy màu sắc/hướng theo hành của mệnh chủ

### BƯỚC 6 — PHI HÓA NÂNG CAO (nếu cần sâu hơn)
Đọc `references/PHI_HOA.md` khi:
- Cần giải thích tại sao tiền đến/đi qua đâu
- Mối quan hệ giữa các cung tương tác thế nào
- Tình huống phức tạp cần phân tích nhiều lớp

**Tứ Hóa Phi Tinh (engine đã có):** mỗi cung có Can riêng → sinh Tứ Hóa riêng "bay" sang cung khác.
- **Hội tụ:** ≥2 cung cùng bay 1 loại Hóa vào 1 cung = điểm hội tụ thật (Kỵ = rủi ro cần xử lý chủ động;
  Lộc/Quyền/Khoa = tiếp sức, nên tận dụng). Đây mới là "ai đang kéo/đẩy ai", không nhìn từng cung tách rời.
- **Tự Hóa Kỵ** tại 1 cung = vướng mắc do chính mình tạo ra, không phải hoàn cảnh → giải thích vì sao
  cùng 1 kiểu chuyện lặp lại dù đã đổi việc/đổi người.
- Lưu Tứ Hóa trùng cung với Hóa gốc của cùng sao = vừa cơ hội vừa rủi ro, cần chú ý đặc biệt.

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

**Nguyên tắc 6 — Cụ thể, không Barnum**
Mỗi nhận định phải gắn 1 tình huống quan sát được và 1 hành động "Nếu X thì Y". Câu đúng với mọi người là câu vô giá trị.

**Nguyên tắc 7 — Kỷ luật verify (từ bug thật của dự án)**
Không tin 1 nguồn duy nhất; không tin báo cáo "đã verify" khi chưa tự kiểm tra; công thức mới cần ≥2 nguồn/phương pháp
độc lập + test case thật; không bịa/đoán khi thiếu dữ liệu (báo rõ "không xác định"). Ví dụ đã xảy ra: Quốc Ấn
thiếu ở cả iztro lẫn ziwei-doushu → chỉ thêm sau khi đối chiếu 2 nguồn tiếng Việt độc lập + kiểm tra nội bộ
(luôn = Lộc Tồn + 8 cung ở cả 10 Can). Nếu lá số chưa có case thật đối chiếu, ghi rõ mức tin cậy.

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
- Chi tiết Lưu Nguyệt/Lưu Nhật → gọi `execute_code()` chạy `tuvi_luu_engine.py` (skill `tuvi-luu-nguyet-nhat`, module Python chạy độc lập không cần MCP)

**Output:** Xu hướng tổng thể + tháng nên hành động + tháng cẩn thận + lời khuyên cụ thể

---

## CÁC FILE THAM KHẢO

| File | Nội dung | Khi nào dùng |
|------|----------|--------------|
| `references/AN_SAO.md` | Thuật toán an sao đầy đủ | Mỗi lần lập lá số |
| `references/PHI_HOA.md` | Kỹ thuật Phi Hóa | Phân tích sâu |
| `references/CACH_CUC.md` | 51+ cách cục | Nhận diện pattern |
| `references/VAN_HANH.md` | Framework vận hạn | Luận vận trình |
| `references/BANG_TRA.md` | Bảng tra nhanh | Tra cứu trong lúc an sao |
| `tuvi-luu-nguyet-nhat` | Skill con — Lưu Nguyệt/Nhật | Khi cần xem tháng/ngày chi tiết (có script Python riêng) |

---

## MCP TOOLS — TÍCH HỢP TÍNH TOÁN TỰ ĐỘNG

(File `data/MCP_TOOLS.md` không tồn tại — tra `tuvi-mcp-server/SKILL.md` để biết tool MCP hiện có.)

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
