# BillionMail — GitHub Repo

## TL;DR
Platform email marketing self-hosted hoàn chỉnh: mail server + newsletter + campaign — không tốn phí subscription hàng tháng. 15K+ sao, đang tăng mạnh.

## Repo này dùng để làm gì
Thay thế Mailchimp, Brevo, hay các dịch vụ email marketing SaaS tốn tiền. Mày tự host trên VPS của mình, có toàn quyền kiểm soát data, không bị giới hạn số subscriber hay email gửi đi.

Bộ ba tính năng chính:
- **Mail Server** (dùng Postfix + Dovecot + Rspamd): tự vận hành SMTP server, không cần thuê SendGrid hay AWS SES
- **Newsletter**: quản lý danh sách, segmentation, gửi bulk email
- **Email Marketing**: campaign, tracking open/click, automation cơ bản

Phù hợp cho: indie hacker, agency, startup không muốn trả $50-200/tháng cho Mailchimp.

## Setup từng bước

### Yêu cầu
- VPS Linux (Ubuntu 22.04+), tối thiểu 2GB RAM
- Domain đã trỏ MX record
- Docker + Docker Compose

### Cài đặt
```bash
# Clone repo
git clone https://github.com/Billionmail/BillionMail.git
cd BillionMail

# Copy config
cp .env.example .env
# Sửa .env: domain, admin email, password

# Chạy
docker compose up -d
```

### Config DNS (bắt buộc để email không vào spam)
```
MX record: mail.yourdomain.com
SPF: v=spf1 ip4:YOUR_IP ~all
DKIM: lấy từ admin panel sau khi setup
DMARC: v=DMARC1; p=none; rua=mailto:admin@yourdomain.com
```

Xong vào `http://YOUR_IP:3000` để access admin panel.

## Ví dụ thực tế
Một indie hacker đang trả $89/tháng cho Mailchimp (15k subscribers). Chuyển sang BillionMail: chi phí còn lại chỉ là VPS $10-20/tháng. Setup mất khoảng 2-3 tiếng lần đầu, sau đó chạy tự động.

Gửi được 50k-100k email/ngày tùy cấu hình VPS và reputation của IP.

## Lưu ý / Lỗi thường gặp
- **IP reputation**: VPS mới thường bị blacklist → dùng IP warm-up, hoặc relay qua SES/Mailgun lúc đầu
- **DNS config sai** → email vào spam 100%. Phải setup đầy đủ SPF, DKIM, DMARC
- **Port 25 bị block**: nhiều cloud provider (AWS, GCP, Azure) chặn port 25 mặc định → cần request mở hoặc dùng provider khác (Hetzner, Vultr thường ok)
- Không có AI features, automation còn basic so với Mailchimp

## Đánh giá cá nhân
- Điểm mạnh: Miễn phí hoàn toàn, full control data, không giới hạn subscriber/email, Go-based nên nhẹ và nhanh
- Điểm yếu: Setup phức tạp hơn SaaS, cần biết sơ về DNS và server, deliverability phụ thuộc nhiều vào IP reputation của mày
- Có nên dùng không: **8/10** — Nếu mày đang trả tiền cho email marketing SaaS và có chút kiến thức server, đây là no-brainer. Không phù hợp cho người hoàn toàn không biết về server.

## Link
- Repo: https://github.com/Billionmail/BillionMail
- Website: https://billionmail.com
- Discord: https://discord.gg/asfXzBUhZr

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

BMAIL_URL = "http://localhost:8080"
BMAIL_KEY = "[BILLIONMAIL_API_KEY]"

def send_campaign_email(to_list, subject, html_content, from_name="Nobitano"):
    payload = json.dumps({
        "recipients": to_list,
        "subject": subject,
        "html": html_content,
        "from_name": from_name
    }).encode()
    req = urllib.request.Request(
        f"{BMAIL_URL}/api/v1/campaigns/send", data=payload,
        headers={"Authorization": f"Bearer {BMAIL_KEY}", "Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

def get_campaign_stats(campaign_id):
    req = urllib.request.Request(
        f"{BMAIL_URL}/api/v1/campaigns/{campaign_id}/stats",
        headers={"Authorization": f"Bearer {BMAIL_KEY}"}
    )
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Web UI — không cần npm
```

### Antigravity
```bash
git clone https://github.com/nicholasgasior/billionmail
cd billionmail && cp .env.example .env
docker compose up -d
# Mở: http://localhost:8080
```
> ⚠️ Self-hosted email marketing. Hermes gửi bulk email campaign tự động.
