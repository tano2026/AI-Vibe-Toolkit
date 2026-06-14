# OpenClaw — Workflows Config

**Cài:** `curl -fsSL https://get.openclaw.dev | bash`

---

## Setup

```bash
openclaw connect telegram --token [YOUR_BOT_TOKEN]

# Tìm chat ID: nhắn /start cho bot
# Vào https://api.telegram.org/bot[TOKEN]/getUpdates
# Lấy "id" trong "chat" object

export GITHUB_REPO=tano2026/AI-Vibe-Toolkit
export GITHUB_TOKEN=[YOUR_GITHUB_TOKEN]
export TELEGRAM_CHAT_ID=[YOUR_CHAT_ID]
```

---

## Workflow 1: Morning Trending (07:00 hàng ngày)

```bash
openclaw schedule --name "morning-trending" \
  --cron "0 7 * * *" \
  --task "
    Fetch GitHub trending AI repos 2 ngày qua
    Filter repos chưa có trong $GITHUB_REPO/repos/
    Format: tên, stars, mô tả, angle video hay
    Send Telegram: $TELEGRAM_CHAT_ID
  "
```

## Workflow 2: Nhận Lệnh Thêm Repo

```bash
openclaw on-message --pattern "thêm repo (.+)" --name "add-repo" --task "
  1. Fetch GitHub API {match}
  2. Fetch README.md
  3. Viết /repos/{tên}.md
  4. Viết /content/script-video-{XX}-{tên}.md
  5. Push lên GitHub, update TRACKER.md
  6. Reply Telegram: Xong! Script #{XX} ready
"
```

## Workflow 3: Viết Script

```bash
openclaw on-message --pattern "viết script (.+)" --name "write-script" --task "
  Fetch /repos/{match}.md từ kho
  Fetch /skills/viral-hooks/hooks-database.md
  Viết script 60-90s, hook mạnh đầu tiên
  Push /content/script-video-{XX}-{match}.md
  Reply: preview script
"
```

## Workflow 4: ROAS Morning Check (08:00)

```bash
openclaw schedule --name "roas-check" \
  --cron "0 8 * * *" \
  --mcp meta-ads \
  --task "
    Fetch Meta Ads performance hôm qua theo campaign
    ROAS = revenue / spend
    Flag: ROAS < 2x → cần review
    Send Telegram: report ngắn
  "
```

## Workflow 5: SEO Monitor (02:00 hàng đêm)

```bash
openclaw schedule --name "seo-monitor" \
  --cron "0 2 * * *" \
  --plugin claude-seo \
  --task "
    /seo drift compare https://your-site.com
    Nếu regression > 10%: alert Telegram ngay
    Nếu OK: log Google Sheets, không nhắn
  "
```

## Workflow 6: Content Calendar (thứ 6, 16:00)

```bash
openclaw schedule --name "content-calendar" \
  --cron "0 16 * * 5" \
  --task "
    Fetch scripts chưa quay từ /content/
    Generate lịch 7 ngày tới
    Send Telegram: lịch format rõ ràng
  "
```

---

## On-Message Nhanh

```bash
# Check kho
openclaw on-message --pattern "kho có gì" \
  --task "Fetch TRACKER.md, tóm tắt số liệu, send Telegram"

# Check đã có chưa
openclaw on-message --pattern "đã có (.+) chưa" \
  --task "Search /repos/ cho {match}, reply có/chưa"

# Research nhanh
openclaw on-message --pattern "research (.+)" \
  --task "Research {match}, tóm tắt 200 words, send Telegram"

# Kết hợp Hermes
openclaw set-brain hermes
# → Hermes xử lý tasks phức tạp, tích lũy skills
```
