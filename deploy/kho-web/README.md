# Trang tra cứu kho trên VPS

Một trang tĩnh (`index.html`) có ô tìm, bộ lọc theo việc cần làm, độ tin cậy nhãn và nút mở entry gốc. Không cần token Claude, không gọi server nào, nên dùng được khi Claude hết hạn mức.

## Cài lần đầu
1. Domain (ví dụ `kho.<domain-của-bạn>`) trỏ A record về IP VPS. Mở cổng 80 và 443.
2. Kho đã clone trên VPS bằng deploy key (xem `deploy/PRIVATE-REPO.md`).
3. Chạy:
   ```bash
   sudo DOMAIN=kho.example.com EMAIL=ban@example.com bash deploy/kho-web/setup-kho-web.sh
   ```
   Script hỏi mật khẩu cho tài khoản `tano` ngay trên terminal. Mật khẩu không nằm trong kho.

## Cập nhật
`deploy/auto-sync.sh` pull kho mỗi 6 giờ. Cron của script này dựng lại trang mỗi giờ từ bản đã pull. Dựng tay: `python3 tools/build_kho_web.py --out /var/www/kho`.

## Lưu ý
- Trang chứa toàn bộ danh mục kho (mô tả, điều kiện dùng, đường dẫn). Repo đã private nên trang này phải có mật khẩu và HTTPS, đừng bỏ.
- Link "Mở entry gốc trên GitHub" chỉ mở được với tài khoản có quyền vào repo.
- Đã kiểm: dựng trang từ catalog, cú pháp script. Chưa chạy trên VPS thật.
