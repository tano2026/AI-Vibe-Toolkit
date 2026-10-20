# Thủ Kho — Agent tra kho và gợi ý cài đặt

> Trạng thái: **bản thiết kế + công cụ chạy được, chưa chạy với dự án thật.** Mọi nhãn trong kho là nhãn đọc, không phải nhãn dùng (xem `catalog/AGENT-ROUTER.md` mục 5).

## Spec
- **Domain:** Quản trị kho công cụ AI (916 mục: repo, MCP, skill, stack) của Tano Agency
- **Job-to-be-done:** Nhận một việc cần làm, tra `catalog/catalog.json` đúng quy trình AGENT-ROUTER, đề xuất 1 mục chính + 1 dự phòng cho từng khả năng cần, lập **kế hoạch cài** (không thực thi), và ghi sổ `GAP-LOG.md` / `USAGE-LOG.md` để kho học từ việc dùng thật
- **Người dùng:** Nobitano (duyệt), các agent trong công ty (research, dev, marketing, media...) khi cần chọn công cụ, và nhân viên dự án
- **Input điển hình:**
  - "Cào web đối thủ khách sạn A, không có GPU"
  - "Dự án Fanpage cho khách B: đăng bài có lịch + video ngắn + báo cáo tuần — gợi ý bộ đồ nghề"
  - "Cài giúp mcps/crawl4ai" (chỉ ra kế hoạch, chờ duyệt)
  - "Dự án X xong, dùng buffer-mcp được, tiết kiệm 2 giờ" (ghi USAGE-LOG)
- **Output điển hình:** Danh sách ứng viên (id, vì sao khớp, mức tin cậy của nhãn, điều kiện cần, cờ rủi ro) / kế hoạch cài đánh số, có mức duyệt L0-L3 và cờ đỏ / dòng Markdown để dán vào GAP-LOG hoặc USAGE-LOG
- **Mức tự chủ:** **Chỉ đọc + đề xuất + ghi sổ.** Tra, so sánh, lập kế hoạch: tự chạy (L0/L1). Cài, chạy lệnh từ entry, đặt khoá, chi tiền: **không bao giờ tự làm** — luôn chờ người duyệt
- **Rủi ro cao nhất:** Khuyên cài một thứ chạy lệnh nguy hiểm hoặc tốn tiền/lộ khoá vì tin nhãn quá mức. Chặn bằng: luôn đọc entry gốc trước khi khuyên, cờ đỏ tự động cho `curl|sh`/`sudo`/`rm -rf`/ghi ngoài dự án, nói rõ độ tin cậy của nhãn, và công cụ không có đường code nào chạy lệnh lấy từ entry

## Capability Map
**Não:** quy trình tra 4 bước của AGENT-ROUTER · đọc `skip_if` + mục Lưu ý của entry gốc · phân biệt độ tin cậy nhãn (`da-doc-entry-goc` > `da-doc-dau-entry` > `chua-gan-nhan`; khi xếp hạng, `confidence` cao được xét trước curation_status) · chọn 1 chính + 1 dự phòng khác `dup_group` · nhận ra HỔNG và ghi sổ thay vì bịa · map hành động sang mức L0-L3 của DECISION-MATRIX

**Tay:** `tools/thu_kho.py` (CLI + import): `tim`, `chi-tiet`, `ke-hoach-cai`, `goi-y`, `ghi-gap`, `ghi-usage`, `may` · đọc `catalog/catalog.json`, `catalog/audit.json` (nếu có) · đọc entry gốc trong repo · nối dòng vào `catalog/GAP-LOG.md` và `catalog/USAGE-LOG.md` (chỉ nối cuối bảng, khi người dùng đồng ý)

**Cơ:** Python stdlib (không cần mạng, không cần API) · git (đồng bộ kho bằng `git pull`) · chạy được trong Hermes (Python), OpenClaw, hoặc Claude Code (Bash)

## Kiến trúc
```
Yêu cầu (người / agent khác)
        ↓
Thủ Kho (system-prompt.md)
  ├─ skill tra-kho          → thu_kho.py tim / chi-tiet     → ứng viên + độ tin cậy nhãn
  ├─ skill goi-y-cai-dat    → thu_kho.py goi-y / ke-hoach-cai → bộ gợi ý + kế hoạch CHƯA CHẠY
  │                              ↓ (mức L2/L3 → approvals chờ "OK <job-id>")
  └─ skill ghi-so           → thu_kho.py ghi-gap / ghi-usage → GAP-LOG.md, USAGE-LOG.md
        ↓
Người duyệt (Nobitano) ──► người/agent dev mới cài (ngoài phạm vi Thủ Kho)
```
Thủ Kho là **nhân viên tra cứu**, không phải người cài. Vai "cài" thuộc agent `dev` sau khi có duyệt.

## Cách bung
1. Đồng bộ kho: `git pull` trong thư mục repo (xem `deploy-checklist.md`)
2. Kiểm công cụ: `python tools/thu_kho.py may` rồi `python -m unittest discover -s tools/tests`
3. Dán `system-prompt.md` làm instruction cho Hermes / OpenClaw / Claude Code subagent
4. Nạp 3 skill trong `skills/` (tra-kho, goi-y-cai-dat, ghi-so)
5. Điền `MACHINE-PROFILE.md` cho từng máy/VPS (mẫu có sẵn; chạy `thu_kho.py may` để lấy số liệu thật)
6. Chạy thử các truy vấn trong `EXAMPLES.md` và so kết quả

## File trong package
| File | Nội dung |
|---|---|
| `system-prompt.md` | Vai, quy trình 5 bước, luật cứng |
| `skills/tra-kho/SKILL.md` | Tra kho theo AGENT-ROUTER |
| `skills/goi-y-cai-dat/SKILL.md` | Gợi ý bộ đồ nghề + kế hoạch cài (không chạy) |
| `skills/ghi-so/SKILL.md` | Ghi GAP-LOG và USAGE-LOG |
| `JD-KPI-SOP-ESCALATION.md` | Đủ 4 thứ theo chuẩn ORG-v3 |
| `deploy-checklist.md` | Nạp vào Hermes/OpenClaw/Claude Code, đồng bộ kho |
| `MACHINE-PROFILE.md` | Mẫu hồ sơ máy |
| `EXAMPLES.md` | Đầu ra thật của 8 truy vấn tự kiểm |
| `../../tools/thu_kho.py` | Công cụ (import được) |
| `../../tools/tests/test_thu_kho.py` | Test |

## Giới hạn trung thực
- Xếp hạng dựa trên nhãn do model gắn; **chưa mục nào có dòng USAGE-LOG** nên chưa ai biết mục nào "dùng được" thật
- 460 skill nhập hàng loạt chưa gắn nhãn: mặc định bị ẩn khỏi kết quả chính, chỉ hiện ở phần "Thêm (chưa gắn nhãn)"
- Bộ khớp từ là heuristic (đồng nghĩa + khớp theo đầu từ + trọng số IDF), không phải tìm kiếm ngữ nghĩa; truy vấn dùng từ lạ có thể trượt (khi đó ghi GAP-LOG, đừng ép)
- Trích lệnh cài là regex trên khối mã của entry; có thể sót hoặc nhận nhầm lệnh. Kế hoạch luôn kèm "đọc entry gốc"
