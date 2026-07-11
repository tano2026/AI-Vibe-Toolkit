# MCP & API Setup — Trùm Sân Bay

## Danh sách cần bật

### 1. ~~SceneWorks~~ — thay bằng HyperFrames

### 1b. HyperFrames (Render video — thay SceneWorks)
```bash
# Cài trên VPS (Node.js 22+ required)
npm install -g hyperframes
npx skills add heygen-com/hyperframes
apt install ffmpeg -y

# Test render
npx hyperframes render --input test.html --output test.mp4 --width 1080 --height 1920
```

### 1c. Apify (Research Agent crawler)
```
Free tier: 5 USD credit/tháng — đủ dùng

Set env:
APIFY_TOKEN=your_apify_token
```
Đăng ký: https://apify.com (free)


### 2. Meta Graph API (Facebook + Instagram + Reels)
```bash
# Chạy local hoặc GPU VPS
cd /opt/sceneworks
python app.py --host 0.0.0.0 --port 7860 --mcp-server

# MCP endpoint
SCENEWORKS_URL=http://localhost:7860
```

### 2. Meta Graph API (Facebook + Instagram + Reels)
```
Cần:
- Facebook App (developers.facebook.com)
- Page Access Token (long-lived)
- Instagram Business Account linked to Facebook Page

Permissions cần request:
- pages_manage_posts
- pages_read_engagement
- instagram_basic
- instagram_content_publish
- instagram_manage_comments

Set env:
FB_PAGE_ID=your_page_id
FB_ACCESS_TOKEN=your_long_lived_token
IG_USER_ID=your_ig_business_id
```

### 3. TikTok Content Posting API
```
Cần:
- TikTok Developer Account
- App với Content Posting API enabled
- OAuth2 access token

Set env:
TIKTOK_CLIENT_KEY=your_client_key
TIKTOK_CLIENT_SECRET=your_client_secret
TIKTOK_ACCESS_TOKEN=your_access_token
```

### 4. YouTube Data API v3
```
Cần:
- Google Cloud Project
- YouTube Data API v3 enabled
- OAuth2 credentials (credentials.json)

Set env:
YOUTUBE_CLIENT_ID=your_client_id
YOUTUBE_CLIENT_SECRET=your_client_secret
YOUTUBE_CHANNEL_ID=your_channel_id
```

### 5. Airtable (Content Queue)
```
Base: trum-san-bay-queue
Tables: content_queue, comment_queue, analytics

Set env:
AIRTABLE_API_KEY=your_api_key
AIRTABLE_BASE_ID=your_base_id
```

### 6. n8n (đã chạy trên VPS port 5678)
```
Import file: n8n-workflow.json
Set credentials cho từng service trong n8n UI
```

## pm2 ecosystem config

```javascript
// ecosystem.config.js — thêm vào file hiện tại
{
  name: 'trum-san-bay',
  script: '/opt/trum-san-bay/agent.py',
  interpreter: 'python3',
  env: {
    FB_PAGE_ID: 'your_page_id',
    FB_ACCESS_TOKEN: '[FB_TOKEN]',
    IG_USER_ID: 'your_ig_id',
    TIKTOK_ACCESS_TOKEN: '[TIKTOK_TOKEN]',
    YOUTUBE_CHANNEL_ID: 'your_channel_id',
    AIRTABLE_API_KEY: '[AIRTABLE_KEY]',
    AIRTABLE_BASE_ID: 'your_base_id',
    SCENEWORKS_URL: 'http://localhost:7860'
  }
}
```

> ⚠️ Không bao giờ paste token thật vào file config — dùng pm2 set hoặc .env file ngoài repo
