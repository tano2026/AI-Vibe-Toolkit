---
name: digital-product-factory
description: Digital Product Factory — web app tự động tạo sản phẩm số bán Gumroad (PDF guide, ảnh bìa, mô tả sales). Dùng cho MMO hướng ngoại.
---

## Quick Start
```bash
cd D:\AI Store\Hermes Agent\digital-product-factory
python -m http.server 8081
```
Mở `http://127.0.0.1:8081`

## Cấu trúc
- `index.html` + `style.css` + `app.js` — frontend Content Factory + Media Studio + Copy Writer
- `products/` — thư mục chứa PDF và ảnh đã tạo

## 4 Tab
1. **Content Factory** — chọn ngách → AI generate nội dung → preview PDF → tải về
2. **Media Studio** — tạo ảnh bìa (1280×540), Pinterest Pin (1000×1500), Social Card (1200×630), Thumbnail (640×360) — 4 style, tuỳ chỉnh màu/cỡ chữ
3. **Copy Writer** — auto sinh mô tả Gumroad sales page (viết bằng tiếng Anh)
4. **Settings** — cấu hình tên brand, màu sắc, giá mặc định

## Backend Services
- **Content Brain API** — chạy tại `http://127.0.0.1:8082` — nhận `GET /api/generate?topic=...&chapters=5`, trả về JSON array chapters với nội dung markdown
- Nguồn data: sử dụng ABTRIP B2B API + web search làm context khi generate

## Lưu ý
- PDF export dùng html2canvas + jspdf qua CDN
- Canvas rendering cho cover images (không cần backend)
- Content brain dùng mỗi lần gọi là tốn token AI — dùng sparingly
