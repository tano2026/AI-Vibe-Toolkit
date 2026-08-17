---
name: healthchecks
description: >
  Cron job / dead man's switch monitoring self-host, viet bang Python/Django.
  Agent tu ping 1 URL sau khi chay xong; qua gio ma khong thay ping -> canh
  bao ngay qua Telegram/email/Slack. Va dung van de OPC Mission Control
  dashboard offline ca tuan khong ai biet, port 3100 khong co gi listen.
---

# Healthchecks — GitHub Repo

## TL;DR
Cron/dead-man-switch monitoring self-host — mỗi agent (Hermes, OpenClaw, cron job trên Antigravity) sau khi chạy xong "ping" 1 URL. Quá giờ mà không thấy ping → Healthchecks tự bắn cảnh báo. Vá đúng lỗ hổng đang ghi trong kho: "OPC TANO AGENCY dashboard đang offline, port 3100 không có gì listen" — không ai biết cho tới khi tự vào check.

## Repo này dùng để làm gì
Nguyên lý ngược với monitoring thông thường: không phải Healthchecks đi kiểm tra agent còn sống hay không, mà agent phải tự báo cáo ("tao vừa chạy xong") bằng cách gọi 1 URL ping duy nhất sau mỗi lần chạy. Nếu quá "period" (chu kỳ dự kiến) + "grace" (khoảng trễ cho phép) mà không có ping mới → tự động coi là "chết" và gửi cảnh báo. Cực hợp cho:
- Cron job trên Antigravity (PM2/systemd) — biết ngay job nào silent-fail.
- Hermes/OpenClaw sau mỗi task lớn — báo "tao vẫn sống" định kỳ.
- Zalo OA bot / RIO Bot — phát hiện ngay khi bot offline thay vì đợi Nobitano hỏi kho mới biết.

## Setup từng bước
1. Chạy container (SQLite đủ dùng cho scale nhỏ, không cần Postgres riêng):
```bash
docker run -d --name healthchecks --restart unless-stopped \
  -p 8000:8000 \
  -e SITE_ROOT=http://your-vps-ip:8000 \
  -e DEFAULT_FROM_EMAIL=noreply@tano.agency \
  -v /opt/healthchecks_data:/data \
  healthchecks/healthchecks
```
2. Vào UI (`:8000`), tạo tài khoản admin, tạo 1 "Check" mới cho từng job cần theo dõi (vd "Hermes daily research", "RIO Bot heartbeat", "OpenClaw pm2 restart cron").
3. Set Period (vd 1 giờ) + Grace (vd 15 phút) — quá 1h15p không ping là bắn cảnh báo.
4. Copy URL ping riêng (dạng `https://your-vps:8000/ping/<uuid>/`), gắn vào cuối script/cronjob.
5. Kết nối kênh cảnh báo: Settings → Integrations → thêm Telegram bot (dùng chung bot RIO_Tano_bot cũng được) hoặc Email/Slack.

## Ví dụ thực tế
Thêm dòng cuối vào cron job PM2 restart OpenClaw trên Antigravity:
```bash
# crontab hiện tại
0 * * * * pm2 restart openclaw --update-env && curl -fsS --retry 3 https://vps:8000/ping/abc-123-uuid/
```
Nếu 1 tiếng trôi qua mà VPS không gửi ping (script lỗi, PM2 chết, VPS down) → Healthchecks tự nhắn Telegram "OpenClaw restart job đã 1h15p không báo cáo" — biết ngay thay vì đợi tự phát hiện port 3100 chết như tình trạng hiện tại.

## Lưu ý / Lỗi thường gặp
- SITE_ROOT phải khớp đúng domain/IP thật, nếu không link ping trong email cảnh báo sẽ sai.
- Ping endpoint public — không có gì bí mật ngoài UUID, nhưng vẫn nên để Healthchecks chạy nội bộ qua Tailscale (100.64.173.75) thay vì expose thẳng ra internet.
- Cron thiếu `--retry` dễ miss ping do mạng chập chờn 1 lần rồi báo động giả — nên thêm `curl --retry 3` như ví dụ trên.
- Không thay thế được error tracking (Healthchecks chỉ biết "có chạy hay không", không biết "chạy đúng hay sai") — nếu cần bắt lỗi logic bên trong thì phải kèm GlitchTip hoặc log riêng.

## Đánh giá cá nhân
- Điểm mạnh: cực nhẹ, setup 5 phút, giải quyết đúng 1 vấn đề cụ thể (biết cái gì chết) mà không cần dựng cả dashboard.
- Điểm yếu: chỉ là "có ping hay không", không phải full observability — không thay được việc xem log thật khi debug.
- Có nên dùng không: **9/10** — chi phí implement gần như bằng 0, giải quyết trực tiếp pain point "OPC dashboard offline không ai biết" đang ghi trong kho.

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes chỉ dùng urllib, gọi ping cuối mỗi task lớn
import urllib.request

PING_URL = "https://vps:8000/ping/[HEALTHCHECKS_UUID]/"

def report_alive(success=True):
    url = PING_URL if success else PING_URL + "fail"
    try:
        urllib.request.urlopen(url, timeout=10)
    except Exception:
        pass  # không để lỗi ping làm crash task chính

# Gọi sau khi task Hermes hoàn thành:
report_alive(success=True)
```

### OpenClaw
```bash
# Thêm vào cuối script wrapper PM2 cron, hoặc trực tiếp trong crontab của VPS
curl -fsS --retry 3 https://vps:8000/ping/[HEALTHCHECKS_UUID]/
```

### Antigravity
```bash
# Deploy Healthchecks như 1 service riêng cạnh OpenClaw trên Tencent Cloud VPS
docker run -d --name healthchecks --restart unless-stopped \
  -p 8000:8000 \
  -e SITE_ROOT=http://100.64.173.75:8000 \
  -v /opt/healthchecks_data:/data \
  healthchecks/healthchecks

# Thêm ping vào MỌI cron job hiện có trên Antigravity (ecosystem.config.js pm2)
# để lần đầu tiên có cảnh báo chủ động thay vì bị động phát hiện port chết
```
> ⚠️ Ưu tiên set check đầu tiên cho chính OPC TANO AGENCY dashboard (port 3100) — đây là ca đang chết mà không ai biết, đúng use case sinh ra Healthchecks.

## Link
- Repo: https://github.com/healthchecks/healthchecks
- Docs: https://healthchecks.io/docs/self_hosted/
- License: BSD-3-Clause
