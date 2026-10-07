# Hướng dẫn triển khai Twenty CRM cho ABTRIP (nội bộ)

> Quyết định (Nobitano chốt 07/10/2026): **chuyển sang Twenty**, ABTrip CRM tự xây đóng băng (không xoá).
> Trạng thái: script đã kiểm cú pháp và kiểm `docker compose config` hợp lệ trên bản compose chính thức, **chưa chạy trên VPS thật**. Chưa PASS bước 5 thì chưa nhập dữ liệu thật.
> Bối cảnh bảo mật + license: `repos/twenty-crm.md`. Thiết kế dữ liệu: `stacks/twenty-crm-abtrip-internal.md`.

## Gồm gì
| File | Việc |
|---|---|
| `install-twenty.sh` | Cài Twenty (ghim v2.45.0), sinh khoá ngẫu nhiên, khoá cổng vào localhost |
| `backup-twenty.sh` | Backup Postgres + file, giữ 14 ngày |
| `test-twenty-api.py` | Test PASS/FAIL: tạo → đọc → xoá 1 Company qua API |

## Cần có
- VPS Linux có Docker + Docker Compose v2 + openssl + curl. RAM tối thiểu khoảng 2GB, nên 4GB (số ước lượng, chưa đo).
- Tài khoản Tailscale (miễn phí) cài trên VPS và trên điện thoại/máy tính của nhân viên. Đây là cách giữ Twenty KHÔNG lộ ra internet.
- Làm được từ điện thoại: đưa mục "Prompt giao Antigravity" ở cuối cho Antigravity trên VPS.

## Bước 1 — Tailscale trên VPS
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
# Lấy tên máy trong mạng riêng (dùng làm SERVER_URL):
tailscale status --json | python3 -c "import sys,json;print(json.load(sys.stdin)['Self']['DNSName'].rstrip('.'))"
```
Trong trang quản trị Tailscale: bật **MagicDNS** và **HTTPS Certificates** (cần cho địa chỉ https).
Kết quả mong đợi: tên dạng `ten-may.ten-tailnet.ts.net`.

## Bước 2 — Cài Twenty
```bash
SERVER_URL="https://ten-may.ten-tailnet.ts.net" bash install-twenty.sh
```
`SERVER_URL` phải đúng là địa chỉ nhân viên gõ vào trình duyệt. Sai là đăng nhập lỗi/lặp.
Script tự dừng nếu `.env` đã tồn tại (không ghi đè). Khoá bí mật nằm trong `~/twenty-abtrip/.env` (quyền 600). Không copy file này vào kho hay chat.

## Bước 3 — Mở cho mạng riêng
```bash
sudo tailscale serve --bg 3000
tailscale serve status        # kiểm tra đã proxy 3000
```
(Cú pháp lệnh `serve` đổi theo phiên bản Tailscale — nếu lỗi, xem `tailscale serve --help`.)

## Bước 4 — Tạo admin
Mở `https://ten-may.ten-tailnet.ts.net` từ thiết bị đã vào Tailscale, tạo tài khoản + workspace đầu tiên. Dùng mật khẩu mạnh, riêng cho Twenty.

## Bước 5 — TEST PASS/FAIL (bắt buộc)
1. Trong Twenty: Settings → APIs & Webhooks → tạo API key (tên mục có thể khác chút theo bản).
2. Trên VPS:
```bash
TWENTY_URL="http://127.0.0.1:3000" TWENTY_API_KEY="dán-key" python3 test-twenty-api.py
```
- **PASS** = in `PASS: tạo -> đọc lại -> xoá thành công`. Đi tiếp.
- **FAIL** = in rõ bước hỏng. Gửi nguyên dòng FAIL cho Claude, đừng tự đoán. Nếu endpoint khác (`/rest/...`), sửa trong script theo docs bản đang chạy.

## Bước 6 — Backup (làm TRƯỚC khi có dữ liệu thật)
```bash
bash backup-twenty.sh                       # chạy thử 1 lần
crontab -e   # thêm:  30 2 * * *  bash $HOME/twenty-abtrip/backup-twenty.sh >> $HOME/twenty-backup.log 2>&1
```
- Chép backup sang nơi khác (Google Drive/máy khác). Backup cùng VPS không cứu được khi VPS hỏng.
- **Thử khôi phục 1 lần** trên máy/instance trống rồi mới tin backup:
```bash
gunzip -c twenty-db-XXXX.sql.gz | docker compose exec -T db psql -U postgres -d default
```

## Bước 7 — Dựng dữ liệu theo spec
Làm trong giao diện (Settings → Data model), theo `stacks/twenty-crm-abtrip-internal.md`:
1. Đổi stage Opportunities thành: Tiếp cận → Báo giá → Đàm phán hợp đồng → Ký/Gia hạn → Đang phục vụ
2. Thêm object `Bookings` (PNR, hãng bay, hành trình, ngày bay, ngày xuất vé, giá vé, hạng vé, trạng thái; liên kết Company/People)
3. Thêm object `Fast Track & Meet Assist` (loại dịch vụ, sân bay, ngày dùng, số người, trạng thái duyệt; liên kết Company)
4. Chỉ lưu MÃ PNR. Không lưu số hộ chiếu/thẻ thanh toán.
5. Mời nhân viên, phân quyền: phân quyền chi tiết theo vai trò có thể thuộc tính năng Enterprise — kiểm tra bản Community có đủ không trước khi hứa với team.

## Bước 8 — Chuyển từ ABTrip CRM cũ
1. Xuất CSV Companies/People từ CRM cũ
2. Nhập vào Twenty bằng chức năng Import (thử 10 dòng trước, kiểm tra tiếng Việt có dấu không lỗi)
3. CRM cũ: **đóng băng, KHÔNG xoá** — giữ chế độ chỉ-đọc ít nhất 30 ngày làm dự phòng. Xoá chỉ khi Nobitano xác nhận.
4. Từ ngày chuyển: ghi dữ liệu mới CHỈ vào Twenty.

## Cập nhật phiên bản
1. Đọc https://github.com/twentyhq/twenty/security/advisories và ghi chú release
2. Chạy `backup-twenty.sh`
3. Sửa `TAG=` trong `~/twenty-abtrip/.env` sang bản mới (dạng `vX.Y.Z`), rồi `docker compose pull && docker compose up -d`
4. Kiểm tra `curl http://127.0.0.1:3000/healthz` và mở giao diện

Bản mới nhất khi viết: v2.45.0 (05/10/2026). 2026 Twenty có nhiều lỗ hổng nặng (xem `repos/twenty-crm.md`) → đừng để bản cũ chạy lâu.

## Lỗi thường gặp
- Đăng nhập xong quay lại trang login → `SERVER_URL` trong `.env` khác địa chỉ đang gõ. Sửa `.env`, `docker compose up -d`.
- `healthz` không lên → `cd ~/twenty-abtrip && docker compose logs --tail=100 server`
- Cổng 3000 bị chiếm → đổi cả `docker-compose.yml` (phần ports) và `SERVER_URL`, hoặc dừng dịch vụ đang dùng cổng đó
- Mất khoá `ENCRYPTION_KEY` = không giải mã được dữ liệu mã hoá. Lưu bản `.env` ở chỗ an toàn riêng.

## Checklist bảo mật (đọc lại trước khi cho nhân viên dùng)
- [ ] Cổng 3000 chỉ nghe 127.0.0.1 (kiểm: `ss -ltnp | grep 3000` thấy 127.0.0.1)
- [ ] Chỉ truy cập qua Tailscale, không mở cổng trên firewall VPS/nhà cung cấp
- [ ] `.env` quyền 600, không nằm trong git
- [ ] Backup chạy + đã thử khôi phục + có bản ngoài VPS
- [ ] API key riêng từng agent, đặt qua biến môi trường, không ghi vào file
- [ ] Đang chạy bản mới nhất, đã đọc Security Advisories

## Prompt giao Antigravity (copy nguyên)
```
Trên VPS này, cài Twenty CRM theo hướng dẫn trong kho tano2026/AI-Vibe-Toolkit,
thư mục deploy/twenty-abtrip/ (đọc HUONG-DAN-TRIEN-KHAI.md trước).
Làm tuần tự Bước 1 đến Bước 3. DỪNG sau mỗi bước, báo kết quả thật (đầu ra lệnh).
Không tự ý đổi phiên bản, không mở cổng ra internet, không in nội dung file .env.
Nếu lệnh lỗi: gửi nguyên văn lỗi, không tự sửa theo cách khác.
```
