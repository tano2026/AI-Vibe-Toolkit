# Chatwoot — GitHub Repo

## TL;DR
Platform cham soc khach hang mo nguon mo — thay the Intercom, Zendesk, Freshdesk. 33.7K stars, MIT license. Gop tat ca kenh (live chat, email, WhatsApp, Facebook, Instagram, Telegram, Zalo) vao 1 inbox duy nhat. Co AI agent "Captain" tu tra loi tu dong. Self-host tren VPS, data hoan toan cua may.

## Repo nay dung de lam gi
ABTRIP dang xu ly khach qua nhieu kenh rieng le: web chat rieng, Zalo rieng, Facebook rieng, email rieng. Nhan vien phai mo nhieu tab, de sot tin nhan, khong co lich su hoi thoai day du.

Chatwoot giai quyet:
- **1 inbox tap trung:** Tat ca kenh do vao 1 dashboard
- **Team collaboration:** Nhieu nhan vien cung xu ly, assign conversation, private note noi bo
- **AI Captain:** Tu dong tra loi cau hoi thuong gap (gio ngoai gio lam viec)
- **Canned responses:** Mau cau tra loi nhanh cho agent
- **CSAT:** Do satisfaction score sau moi cuoc tro chuyen
- **Help Center:** FAQ public — khach tu tim truoc khi hoi

**Kenh ho tro:**
Website live chat, Email, WhatsApp, Facebook Messenger, Instagram DM, Twitter/X, Telegram, Line, SMS, API channel (Zalo via webhook)

## Architecture

```
Khach nhan tin (bat ky kenh)
    ↓
Chatwoot Inbox (1 dashboard)
    ↓
Captain AI → tu tra loi neu biet
    ↓ (neu kho hoac ngoai scope)
Agent ABTRIP (nhan vien that) → tra loi
    ↓
Lich su luu tru day du, CSAT, bao cao
```

## Setup cho ABTRIP tren VPS

### Yeu cau
- VPS: Ubuntu 20.04+, toi thieu 4GB RAM, 20GB storage
- Docker + Docker Compose
- Domain: chat.abtrip.vn (hoac subdomain)
- SSL: Let's Encrypt (tu dong)
- SMTP: SendGrid hoac Gmail SMTP (gui email thong bao)

### Buoc 1 — Cai Docker

```bash
# Nhờ Antigravity chay:
curl -fsSL https://get.docker.com | sh
sudo systemctl enable docker
sudo systemctl start docker
```

### Buoc 2 — Cai Chatwoot

```bash
mkdir -p /opt/chatwoot
cd /opt/chatwoot

# Tai file config
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml

# Generate secret keys
SECRET_KEY=$(openssl rand -hex 64)
RAILS_KEY=$(openssl rand -hex 32)

# Edit .env — cac bien quan trong:
nano .env
```

**Cac bien .env can dien:**
```bash
# Keys (paste tu lenh openssl tren)
SECRET_KEY_BASE=<SECRET_KEY>
RAILS_MASTER_KEY=<RAILS_KEY>

# Domain
FRONTEND_URL=https://chat.abtrip.vn

# Database (Docker tu tao, khong can thay)
POSTGRES_HOST=postgres
POSTGRES_DATABASE=chatwoot_production
POSTGRES_USERNAME=chatwoot
POSTGRES_PASSWORD=<random_password>

# Redis
REDIS_URL=redis://redis:6379

# Email (dung SendGrid)
MAILER_SENDER_EMAIL=support@abtrip.vn
SMTP_ADDRESS=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USERNAME=apikey
SMTP_PASSWORD=<SENDGRID_API_KEY>

# Storage (dung S3 hoac Cloudflare R2)
STORAGE_SERVICE=s3
S3_BUCKET_NAME=abtrip-chatwoot
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>
AWS_REGION=ap-southeast-1
```

### Buoc 3 — Chay Chatwoot

```bash
cd /opt/chatwoot

# Khoi tao database
docker compose run --rm rails bundle exec rails db:chatwoot_prepare

# Chay tat ca services
docker compose up -d

# Kiem tra
docker compose ps
# → rails, sidekiq, postgres, redis deu "running"
```

### Buoc 4 — Tao admin account

```bash
docker compose exec rails bundle exec rails console

# Trong Rails console:
SuperAdmin.create!(
  email: 'admin@abtrip.vn',
  password: 'YourSecurePassword123!'
)
exit
```

### Buoc 5 — Config Nginx + SSL

```nginx
# /etc/nginx/sites-available/chatwoot
server {
    listen 80;
    server_name chat.abtrip.vn;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name chat.abtrip.vn;

    ssl_certificate /etc/letsencrypt/live/chat.abtrip.vn/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/chat.abtrip.vn/privkey.pem;

    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

```bash
# Cai SSL
certbot --nginx -d chat.abtrip.vn

# Bat Nginx
nginx -t && systemctl reload nginx
```

### Buoc 6 — Config kenh cho ABTRIP

**Website Live Chat:**
```
Dashboard → Settings → Inboxes → Add Inbox
→ Website → Ten: "ABTRIP Web Chat"
→ Copy widget code → Paste vao website abtrip.vn truoc </body>
```

**Facebook Messenger:**
```
→ Add Inbox → Facebook
→ Connect Facebook Page ABTRIP
→ Chon page → Done
```

**WhatsApp (dung WAHA - mien phi):**
```bash
# Cai WAHA (WhatsApp HTTP API)
docker run -d   -p 3001:3000   -e WHATSAPP_DEFAULT_ENGINE=WEBJS   -e WAHA_DASHBOARD_ENABLED=true   devlikeapro/waha-plus:latest

# Trong Chatwoot:
# Settings → Inboxes → Add Inbox → API Channel
# Webhook URL: http://localhost:3001/chatwoot
# Sau do config WAHA tro webhook ve Chatwoot
```

**Email:**
```
→ Add Inbox → Email
→ Email: support@abtrip.vn
→ Config IMAP/SMTP → Done
```

### Buoc 7 — Setup Captain AI (tu dong tra loi)

```
Super Admin Console (chat.abtrip.vn/super_admin)
→ Settings → Captain
→ OpenAI API Key: <key hoac OmniRoute endpoint>
→ Custom endpoint: http://localhost:20128/v1 (neu dung OmniRoute)
```

**Tao knowledge base cho Captain:**
```
Dashboard → Help Center → New Article
→ Them cac bai FAQ: "Tour Ha Giang gia bao nhieu?",
  "Chinh sach huy tour?", "Dat coc bao nhieu?"
→ Captain hoc tu day, tu tra loi khach
```

## Stack day du cho ABTRIP

```
Khach nhan tin WhatsApp
    ↓
WAHA (nhan + forward)
    ↓
Chatwoot (inbox)
    ↓
Captain AI (OmniRoute) → tu tra loi FAQ
    ↓ (neu kho)
Agent ABTRIP nhan notification → tra loi
    ↓
Lich su luu day du, CSAT gui tu dong
```

## Automation voi n8n (optional nhung manh)

```
Khach hoi gia tour → Captain khong biet
    ↓
Webhook → n8n
    ↓
n8n query database gia tour ABTRIP
    ↓
n8n gui ket qua vao Chatwoot
    ↓
Khach nhan duoc gia chinh xac, tu dong
```

## Chi phi

| Loai | Chi phi |
|------|---------|
| Self-host (Community) | $0 (chi tieu VPS) |
| Chatwoot Cloud Starter | $19/agent/thang |
| Intercom (thay the) | $74+/thang |
| Zendesk (thay the) | $55+/agent/thang |

**Self-host tren VPS $10/thang = tiet kiem $50-200/thang so voi SaaS.**

## Luu y / Loi thuong gap
- RAM: Can toi thieu 4GB — Rails + Sidekiq + Postgres + Redis an nhieu RAM
- WhatsApp chinh thuc (Meta) can dang ky WhatsApp Business API — WAHA la giai phap khong chinh thuc, dung cho scale nho
- Captain AI can Enterprise plan cua Chatwoot OR dung OpenAI-compatible endpoint (OmniRoute duoc)
- Backup: Setup cronjob backup Postgres hang ngay
- Update: `docker compose pull && docker compose up -d` de update version moi

## Danh gia ca nhan
- Diem manh: Omnichannel that su (tat ca kenh vao 1 inbox); Captain AI linh hoat (dung OpenAI-compatible = OmniRoute duoc); Help Center built-in; CSAT baked-in; community lon (15K+ businesses dang dung); MIT license
- Diem yeu: Nang (can 4GB RAM); WhatsApp chinh thuc phuc tap; Captain AI day du can plan tra phi; setup ban dau mat 1-2 gio
- Co nen dung khong: **9.5/10** — Bat buoc cho ABTRIP. Thay the Intercom/Zendesk hoan toan, tu chu data, tich hop AI qua OmniRoute mien phi. Deploy 1 lan, dung mai.

## Link
- Repo: https://github.com/chatwoot/chatwoot
- Docs: https://chatwoot.com/docs
- Deploy guide: https://developers.chatwoot.com/self-hosted/deployment/docker
- Discord: discord.gg/cJXdrwS
- License: MIT
- Language: Ruby on Rails + Vue.js
