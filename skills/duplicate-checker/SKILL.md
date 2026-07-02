---
name: duplicate-checker
description: Hướng dẫn kiểm tra trùng lặp repo/tool trước khi viết file và script mới để tránh trùng lặp tài nguyên trong kho.
---
# 🔍 Duplicate Checker Skill — Tránh Trùng Lặp Repo & Tools

> Quy trình rà soát nhanh 3 bước trước khi thêm bất cứ tool hoặc repo nào vào kho, đảm bảo không có tài nguyên nào bị trùng lặp.

---

## 🛠️ Quy Trình Rà Soát

### Bước 1: Quét Tên & Đường Dẫn
- Khi nhận được yêu cầu thêm một tool (ví dụ: `firecrawl` hoặc `browser-use`), hãy tìm kiếm trong file `TRACKER.md` bằng cách quét cột **Tên** và kiểm tra xem tool đó đã tồn tại ở bất kỳ mục nào chưa.
- Kiểm tra chéo cả các tên thay thế (alias) hoặc tên viết thường/viết hoa (ví dụ: `Crawl4AI` và `crawl4ai`).

### Bước 2: Kiểm Tra Repo Cũ Qua URL
- Thực hiện tìm kiếm URL của GitHub repo trong toàn bộ thư mục `repos/` của kho.
- Nếu repo đã tồn tại dưới một tên file khác, tuyệt đối không tạo file mới.

### Bước 3: Phân Loại Và Xử Lý
- **Trường hợp đã có:** Báo cáo lại cho người dùng vị trí file cũ và cập nhật thêm thông tin mới vào file cũ (nếu có) thay vì tạo mới.
- **Trường hợp chưa có:** Xác nhận với người dùng là tool mới hoàn toàn, sau đó tiến hành tạo file `.md` trong thư mục tương ứng và thêm vào `TRACKER.md`.
