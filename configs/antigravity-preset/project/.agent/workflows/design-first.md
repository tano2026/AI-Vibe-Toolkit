---
description: Khoá design system (DESIGN.md) trước khi dựng UI. Dùng khi bắt đầu giao diện mới hoặc project chưa có DESIGN.md.
---
# /design-first

1. Hỏi 1 câu: brand nào (ABTRIP / An Bình / khác) và có ảnh tham chiếu không?
2. Chưa có `DESIGN.md` ở gốc project:
   - ABTRIP hoặc An Bình: copy từ `.agent/design-templates/` ra gốc project, đổi tên thành `DESIGN.md`.
   - Brand khác: chạy `kho-navigator` lấy `repos/awesome-design-md.md`, tìm brand có phong cách gần nhất làm nền, đề xuất token.
3. Các mục ghi "(đề xuất)" trong DESIGN.md là chưa chốt: liệt kê cho tao xác nhận.
4. Đọc `skills/nobitano-ui-ux-guidelines` (qua kho hoặc skill đã cài) và áp dụng, cùng rule `30-design`.
5. Dựng từng màn một. Mỗi màn xong chạy `/ui-check` rồi mới sang màn tiếp.
6. Cuối: đề xuất đóng gói `DESIGN.md` thành skill dùng lại (skill `write-a-skill`).
