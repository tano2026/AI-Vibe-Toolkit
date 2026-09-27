---
name: visual-template-formula-core
description: >
  Khung kích thước + quy trình gác cổng visual THUẦN, không gắn brand
  nào — quy tắc khung kích thước theo định dạng (poster/thumbnail/
  infographic) và vị trí trong pipeline. Brand tự cung cấp token màu/
  phong cách qua file brand-context riêng, không sửa file này.
---

# Visual Template Formula (Core — không gắn brand)

## TL;DR
Khung kích thước theo ĐỊNH DẠNG (poster/thumbnail/infographic) không đổi dù brand nào — chỉ TOKEN MÀU/PHONG CÁCH mới khác nhau theo brand. Tách rõ 2 phần này.

## Khi nào dùng
- Xác định đúng khung kích thước trước khi tạo ảnh cho bất kỳ định dạng nào
- Làm nền tảng để đóng gói dùng cho nhiều brand/khách hàng khác nhau

## Nội dung skill / prompt

### Khung kích thước theo định dạng — universal, không đổi theo brand

```
POSTER
  Dọc: 1080x1350 (feed Instagram/Facebook) hoặc 1080x1920 (Story/Reels)
  Yêu cầu: chữ lớn, đọc được khi thu nhỏ, 1 thông điệp chính duy nhất

THUMBNAIL
  YouTube: 1280x720 (16:9) — chữ PHẢI đọc được ở kích thước ~120x67px
  (thumbnail hiện rất nhỏ trong feed)
  TikTok/Shorts cover: 1080x1920 (9:16)

INFOGRAPHIC
  Dọc dài: 1080x2000+ (linh hoạt theo lượng thông tin)
  Yêu cầu: hệ thống phân cấp rõ (tiêu đề > mục > chi tiết) — không
  phải khung cố định như poster
```

### Quy trình gác cổng — vị trí cố định trong pipeline, không đổi

```
Visual Agent (gen ảnh thô qua tool text-to-image)
        ↓
Visual Template Formula (skill này — xác định đúng khung kích thước
theo định dạng + tra token brand từ file riêng)
        ↓
Quality Gate (kiểm tra contrast/safe-zone/thumbnail-test/license —
xem skill design-quality-gate)
        ↓
Kênh phân phối (đăng theo platform)
```

### Cách brand cung cấp token — KHÔNG sửa file này

```
File này CHỈ có khung kích thước (universal) — không có màu/font cụ
thể. Mỗi brand tự có 1 file brand-context riêng chứa:

  - Bảng màu (hex code cụ thể)
  - Font chính/phụ
  - Logo, vị trí đặt logo chuẩn
  - Mood/phong cách hình ảnh tổng thể

Khi làm ảnh cho brand cụ thể: lấy khung kích thước từ FILE NÀY (theo
định dạng cần) + token từ file brand-context riêng → áp cả 2 vào ảnh
```

### Nếu brand CHƯA có file token — quy trình xác lập lần đầu

```
1. Đọc mô tả brand có sẵn (playbook/brief nếu có)
2. Tự đề xuất bảng màu/phong cách dựa trên mô tả đó
3. Xin xác nhận 1 lần từ người phụ trách brand
4. Sau khi xác nhận → LƯU THÀNH file brand-context cố định, dùng lại
   cho mọi lần sau, không hỏi lại
```

## Setup từng bước
1. Xác định định dạng cần làm (poster/thumbnail/infographic) → lấy đúng khung kích thước từ đây
2. Brand đã có file token → dùng luôn
3. Brand chưa có → chạy quy trình xác lập lần đầu (đề xuất → xác nhận → lưu cố định)
4. Áp khung + token vào ảnh → chuyển qua Quality Gate

## Ví dụ thực tế
2 dự án khác nhau (1 quán ăn, 1 cửa hàng thời trang) đều dùng chung khung kích thước "Thumbnail YouTube 1280x720" khi cần làm thumbnail — chỉ khác nhau ở token màu riêng từng file brand-context. File core này không đổi.

## Lưu ý / Lỗi thường gặp
- Dùng chung 1 khung kích thước cho cả poster/thumbnail/infographic — 3 định dạng có mục đích/ràng buộc đọc khác hẳn nhau, không thay thế được nhau
- Hardcode màu/token vào file core này — làm mất tính dùng chung, phải sửa lại mỗi lần thêm brand mới
- Bỏ qua bước xác nhận 1 lần khi brand chưa có token — dẫn tới không nhất quán giữa các lần tạo ảnh cùng 1 brand

## Đánh giá cá nhân
- Điểm mạnh: tách bạch khung kích thước (universal) khỏi token (brand-specific) — dùng được ngay cho brand/khách hàng mới không cần sửa gì
- Điểm yếu: cần ít nhất 1 vòng xác nhận thủ công khi gặp brand hoàn toàn mới chưa có token — không tự động 100% ngay từ đầu
- Có nên dùng: 9/10 — đúng nền tảng cần có để dùng lại cho nhiều brand/khách hàng, không phải viết riêng mỗi lần

## Link
- Nguồn gốc: agents/trum-san-bay/skills/brand-design-system, agents/designer-pro/skills/brand-visual-template-system (bản có brand cụ thể)
- Dùng cùng: design-quality-gate (bước sau), image-prompt-formula-core (bước trước)
