# Postiz Self-Host — Deploy qua Antigravity

## Vì sao self-host thay vì Postiz Cloud
Postiz Cloud không có bản free, thấp nhất $29/tháng. Postiz mã nguồn mở (AGPL) — self-host
trên VPS Tencent Cloud sẵn có = free hoàn toàn, giao diện/tính năng giống hệt bản trả phí,
vẫn bấm "Connect Facebook Page" y hệt (Postiz tự lo OAuth qua app đã đăng ký sẵn của họ,
không phải Nobitano tự làm Facebook App Review).

## ⚠️ Yêu cầu bắt buộc trước khi deploy
Postiz dùng secure cookie — **cần HTTPS thật + 1 domain/subdomain trỏ vào VPS**, không chạy
được qua IP trần một cách ổn định lâu dài. Đề xuất dùng subdomain có sẵn, ví dụ
`postiz.anbinhairport.com` — trỏ DNS record A về IP VPS trước khi deploy.

## Việc của Antigravity (không phải Nobitano tự làm)

### 1. Cài Docker + Docker Compose (nếu VPS chưa có)
```bash
curl -fsSL https://get.docker.com | sh
apt install docker-compose-plugin -y
docker --version && docker compose version
```

### 2. Tạo thư mục + file cấu hình
```bash
mkdir -p /opt/postiz && cd /opt/postiz
# copy nội dung postiz-docker-compose.yml vào đây, đặt tên docker-compose.yml
```

### 3. Set biến môi trường (file `.env` cùng thư mục)
```bash
cat > .env << 'EOF'
POSTIZ_DOMAIN=postiz.anbinhairport.com
DB_PASSWORD=<tạo password mạnh ngẫu nhiên>
JWT_SECRET=<tạo chuỗi random 64 ký tự>
EOF

# Tạo JWT_SECRET ngẫu nhiên:
openssl rand -hex 32
```

### 4. Setup reverse proxy + HTTPS (Caddy — tự động lấy SSL, đơn giản nhất)
```bash
apt install caddy -y
cat > /etc/caddy/Caddyfile << 'EOF'
postiz.anbinhairport.com {
    reverse_proxy localhost:5000
}
EOF
systemctl restart caddy
```

### 5. Chạy Postiz
```bash
cd /opt/postiz
docker compose up -d
docker compose logs -f postiz   # theo dõi tới khi thấy "ready"
```

### 6. Khóa đăng ký công khai — bắt buộc ngay sau khi tạo tài khoản admin đầu tiên
Truy cập `https://postiz.anbinhairport.com`, tạo tài khoản admin (Nobitano), sau đó:
```bash
# Sửa docker-compose.yml: DISABLE_REGISTRATION: "true"
docker compose up -d   # apply lại
```
Bỏ qua bước này = ai cũng tạo được tài khoản trên Postiz của mày — lỗ hổng bảo mật thật.

## Việc của Nobitano (chỉ 1 bước, giống hệt bản Cloud)
1. Vào `https://postiz.anbinhairport.com`, đăng nhập
2. Connect → Facebook → chọn Page "Trùm Sân Bay" → xác nhận OAuth
3. Vào Settings lấy API key + integration ID → gửi cho Claude để nối vào `agent.py`

## Rủi ro thật cần biết khi self-host (khác Cloud)
- Server down = Postiz down — không có ai vận hành thay, Antigravity cần set uptime alert
- Backup Postgres định kỳ — mất volume = mất toàn bộ lịch sử kết nối/lịch đăng
- Update Postiz version về sau phải tự `docker compose pull && up -d`, không tự động
