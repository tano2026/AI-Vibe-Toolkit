---
description: Cổng tiếp nhận → brainstorm → plan có verify từng bước → DỪNG chờ duyệt. Dùng cho feature hoặc thay đổi nhiều file.
---
# /plan-feature

1. Đọc `AGENTS.md`, `DESIGN.md` (nếu có) và các rule trong `.agent/rules/`.
2. **Cổng tiếp nhận** (im lặng nếu qua cả 4):
   - Đúng việc, đúng phạm vi project chưa?
   - Đủ thông tin chưa? Thiếu thì hỏi TỪNG câu một. Câu đầu tiên luôn là hình thức giao (file / báo cáo / hành động thật).
   - Có đụng lằn ranh đỏ hoặc mức L2/L3 không? Có thì hỏi tao trước, chưa làm gì.
   - Khẩn hay xếp hàng?
3. Nếu chưa rõ giải pháp: nêu tối đa 2 hướng, chọn MỘT, lý do 1 dòng.
4. Nếu thiếu công cụ hay pattern: chạy `kho-navigator` đúng 1 lần.
5. Viết plan: mỗi bước có `→ verify: cách kiểm`, liệt kê file sẽ đụng, kèm rollback.
6. **DỪNG.** Chờ tao duyệt. Không code trước khi có "OK".
7. Sau khi duyệt: làm từng bước, test trước, báo bằng output lệnh thật. Không tự commit.
