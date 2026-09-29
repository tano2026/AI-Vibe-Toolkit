---
trigger: always_on
alwaysApply: true
description: Kỷ luật design — DESIGN.md trước code, dùng đúng token, đọc được, verify bằng browser
---
# Kỷ luật design
(Nguồn: kho `agents/company/EXPERT-CORE.md` mục Designer, `skills/nobitano-ui-ux-guidelines`, `repos/taste-skill.md`.)

1. **Thiết kế trước, code sau.** Chưa có `DESIGN.md` ở gốc project mà được giao làm UI thì dừng, chạy `/design-first`. Không vừa nghĩ design vừa code.
2. **Chỉ dùng token trong `DESIGN.md`** (màu, font, spacing, radius). Cần màu mới thì đề xuất bổ sung vào `DESIGN.md`, không tự chế mỗi màn một màu.
3. **Đọc được:** chữ thường tương phản ≥ 4.5:1 với nền (chữ lớn ≥ 3:1). Tối đa 2 font và 3 cấp hierarchy mỗi màn. Focus bàn phím nhìn thấy được, ảnh có alt.
4. **Phong cách của tao:** hiện đại, đơn giản, dễ thao tác, thông tin trực quan. Palette hài hoà, không "đập vào mắt". Chữ phân cấp rõ, spacing thoáng, đổ bóng nhẹ theo Material Design 3. Không màu mè rườm rà.
5. **Chống UI "AI slop":** không mặc định xanh dương + Inter + gradient hero + card đổ bóng dày. Đọc brief rồi mới chọn hướng.
6. **Ảnh chỉ 3 nguồn hợp lệ:** ảnh gốc trong project, ảnh AI tự tạo, hoặc ảnh có license ghi link. Cấm ảnh lấy tạm từ Google, kể cả làm nháp.
7. **Visual/social:** nội dung quan trọng cách mép ≥10%. Thiết kế khung 4:5 trước rồi mở ra 1:1, 9:16, 16:9.
8. **Verify bằng browser:** mở app, chụp ở 1440px và 390px, so với `DESIGN.md`, liệt kê chỗ lệch. Chưa qua bước này thì chưa gọi là xong.
9. **Brand:** ABTRIP không dùng vàng, giọng ấm B2C. An Bình không dùng cam, giọng trang trọng B2B/B2G.
