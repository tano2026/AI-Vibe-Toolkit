# Bộ Cài Đặt — Trùm Sân Bay Agent

Toàn bộ những gì cần cài/config để pipeline chạy được. Làm theo thứ tự.

---

## 0. Yêu cầu hệ thống VPS

```
OS:      Ubuntu 22.04 (đang có)
Node.js: 22+ (cho HyperFrames, OpenClaw)
Python:  3.10+ (cho Hermes)
RAM:     tối thiểu 4GB (video render không cần GPU)
ffmpeg:  bắt buộc
```

```bash
# Check version hiện tại
node -v
python3 --version
ffmpeg -version

# Cài ffmpeg nếu chưa có
apt update && apt install ffmpeg -y
```

---

## 1. HyperFrames — Render video (thay SceneWorks)

```bash
npm install -g hyperframes
npx skills add heygen-com/hyperframes

# Test thử
mkdir -p /opt/trum-san-bay/video-workspace
cd /opt/trum-san-bay/video-workspace
npx hyperframes init tsb-template
npx hyperframes render --input test.html --output test.mp4 --width 1080 --height 1920
```

**Không cần token/API key** — chạy local hoàn toàn.

---

## 2. Apify — Research Agent crawler

```
Đăng ký free: https://apify.com
Free tier: 5 USD credit/tháng (đủ ~50 lần crawl)

Lấy token tại: Settings → Integrations → API tokens
```

```bash
# Set env
APIFY_TOKEN=apify_api_xxxxxxxxxxxx
```

---

## 3. Meta Graph API — Facebook + Instagram + Reels

**Cần chuẩn bị:**
1. Tạo Facebook App tại developers.facebook.com
2. Có sẵn 1 Facebook Page (Trùm Sân Bay)
3. Instagram Business Account, link với Page trên

**Permissions cần request khi review app:**
```
pages_manage_posts
pages_read_engagement
instagram_basic
instagram_content_publish
instagram_manage_comments
```

**Lấy Page Access Token (long-lived):**
```bash
# Bước 1: lấy short-lived token từ Graph API Explorer
# Bước 2: đổi sang long-lived (60 ngày)
curl -X GET "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={SHORT_TOKEN}"
```

```bash
# Set env
FB_PAGE_ID=xxxxxxxxxxxxx
FB_ACCESS_TOKEN=EAAxxxxxxxxxxxxx
IG_USER_ID=17xxxxxxxxxxxxx
```

> ⚠️ Token này hết hạn sau 60 ngày — api-error-handler skill sẽ cảnh báo trước 3 ngày qua Telegram.

---

## 4. TikTok Content Posting API

**Cần chuẩn bị:**
1. Đăng ký TikTok Developer: developers.tiktok.com
2. Tạo App, request quyền Content Posting API
3. OAuth2 flow lấy access token

```bash
# Set env
TIKTOK_CLIENT_KEY=xxxxxxxxxxxxx
TIKTOK_CLIENT_SECRET=xxxxxxxxxxxxx
TIKTOK_ACCESS_TOKEN=xxxxxxxxxxxxx
```

> ⚠️ Access token TikTok thường hết hạn sau 24h — cần refresh token riêng, lưu ý setup refresh flow.

---

## 5. YouTube Data API v3

**Cần chuẩn bị:**
1. Tạo project tại console.cloud.google.com
2. Enable YouTube Data API v3
3. Tạo OAuth2 credentials → download credentials.json
4. Chạy OAuth flow lần đầu để lấy refresh token

```bash
# Set env
YOUTUBE_CLIENT_ID=xxxxxxxxxxxxx.apps.googleusercontent.com
YOUTUBE_CLIENT_SECRET=xxxxxxxxxxxxx
YOUTUBE_CHANNEL_ID=UCxxxxxxxxxxxxx
```

> ⚠️ Quota mặc định 10,000 units/ngày — mỗi lần upload video tốn ~1600 units, nên tối đa ~6 video/ngày.

---

## 6. Airtable — Content Queue

```
Đăng ký free: https://airtable.com
Tạo base mới: "trum-san-bay-queue"
```

**3 table cần tạo:**
- content_queue — bài chờ duyệt/đã đăng
- comment_queue — comment chờ reply
- ideation_queue — chủ đề từ Research Agent

Schema chi tiết từng field → xem deploy-checklist.md Phase 3.

```bash
# Lấy API key: airtable.com/create/tokens
# Set env
AIRTABLE_API_KEY=patxxxxxxxxxxxxx
AIRTABLE_BASE_ID=appxxxxxxxxxxxxx
```

---

## 7. Anthropic API — Claude cho Writer/Research/Classifier

```bash
# Lấy tại console.anthropic.com
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

---

## 8. n8n — Orchestrate workflow (đã chạy sẵn port 5678)

```
Không cần cài mới — đã có trên VPS
Chỉ cần import workflow + set credentials trong n8n UI
```

---

## Tổng hợp — pm2 ecosystem.config.js

```javascript
module.exports = {
  apps: [{
    name: 'trum-san-bay',
    script: '/opt/trum-san-bay/agent.py',
    interpreter: 'python3',
    env: {
      // Meta
      FB_PAGE_ID: '[FB_PAGE_ID]',
      FB_ACCESS_TOKEN: '[FB_ACCESS_TOKEN]',
      IG_USER_ID: '[IG_USER_ID]',

      // TikTok
      TIKTOK_CLIENT_KEY: '[TIKTOK_CLIENT_KEY]',
      TIKTOK_CLIENT_SECRET: '[TIKTOK_CLIENT_SECRET]',
      TIKTOK_ACCESS_TOKEN: '[TIKTOK_ACCESS_TOKEN]',

      // YouTube
      YOUTUBE_CLIENT_ID: '[YOUTUBE_CLIENT_ID]',
      YOUTUBE_CLIENT_SECRET: '[YOUTUBE_CLIENT_SECRET]',
      YOUTUBE_CHANNEL_ID: '[YOUTUBE_CHANNEL_ID]',

      // Airtable
      AIRTABLE_API_KEY: '[AIRTABLE_API_KEY]',
      AIRTABLE_BASE_ID: '[AIRTABLE_BASE_ID]',

      // Research
      APIFY_TOKEN: '[APIFY_TOKEN]',

      // Content gen
      ANTHROPIC_API_KEY: '[ANTHROPIC_API_KEY]'
    }
  }]
}
```

```bash
pm2 start ecosystem.config.js
pm2 set trum-san-bay:FB_ACCESS_TOKEN "your_real_token"
pm2 restart trum-san-bay --update-env
pm2 save
```

> ⚠️ Không bao giờ commit token thật lên GitHub — file ecosystem.config.js với token thật KHÔNG được push, chỉ giữ local trên VPS. Dùng .gitignore.

---

## Checklist nhanh — cần bao nhiêu account/key

| # | Dịch vụ | Loại | Free? | Bắt buộc |
|---|---------|------|-------|----------|
| 1 | HyperFrames | npm package | Free | Có |
| 2 | Apify | API token | Free tier | Có |
| 3 | Facebook App + Page Token | OAuth | Free | Có |
| 4 | Instagram Business | Link qua FB | Free | Có |
| 5 | TikTok Developer | OAuth | Free | Có |
| 6 | YouTube/Google Cloud | OAuth | Free (quota giới hạn) | Có |
| 7 | Airtable | API key | Free tier | Có |
| 8 | Anthropic API | API key | Trả theo usage | Có |
| 9 | n8n | Đã có sẵn | — | — |

**Tổng chi phí cố định: $0/tháng** (trừ Anthropic API tính theo lượng dùng thực tế — content 1 fanpage/tháng thường chỉ vài USD).
