# Trùm Sân Bay — Architecture

## Luồng dữ liệu tổng quan

```
[Nobitano] ──Telegram──► [OpenClaw]
                              │
                    ┌─────────▼──────────┐
                    │  Content            │
                    │  Orchestrator       │
                    │  (Hermes)           │
                    └──┬──────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    [Ideation]    [Writer]     [Visual]
    Agent         Agent        Agent
          │            │            │
          └────────────┼────────────┘
                       ▼
                 [Adapter Agent]
                 (fork theo platform)
                 │    │    │    │    │
                 ▼    ▼    ▼    ▼    ▼
                FB   IG  TikTok YT  Reels
                       │
                       ▼
               [Airtable Queue]
               (status: PENDING)
                       │
               [Telegram notify]
               → Nobitano review
                       │
              ┌────────┴────────┐
              ▼                 ▼
           APPROVE           REJECT/EDIT
              │                 │
              ▼                 ▼
      [Publisher Agent]    Back to Writer
      post qua API         Agent
```

## Sub-agents chi tiết

### 1. Ideation Agent
- **Trigger:** Lệnh "tạo content tuần này" hoặc cron hàng tuần
- **Input:** Content pillar, lịch content, ngày lễ/sự kiện hàng không sắp tới
- **Output:** List 7-10 idea với pillar tag (TOFU/MOFU/BOFU), platform target
- **Tool:** web_search (tin tức hàng không), aviation-knowledge skill

### 2. Writer Agent
- **Trigger:** Idea được approve từ Ideation
- **Input:** Idea + pillar + platform target
- **Output:** Caption đầy đủ cho từng platform (đã check caption limit)
- **Tool:** copywriting skill + brand-voice skill + aviation-knowledge (fact-check)
- **Guardrail:** Mọi tip/quy định phải có nguồn hoặc được flag "cần verify"

### 3. Visual Agent
- **Trigger:** Caption xong
- **Input:** Caption + platform + content type (ảnh/video/carousel)
- **Output:** File ảnh/video raw (1:1 hoặc 9:16 hoặc 16:9)
- **Tool:** image-prompt-engineer skill (viết prompt ảnh) → HyperFrames (video) → ffmpeg

### 3b. Brand Design System Agent
- **Trigger:** Ngay sau Visual Agent, trước Adapter Agent
- **Input:** Asset raw (ảnh/video) từ Visual Agent
- **Output:** Asset đã validate/chuẩn hóa theo brand — hoặc reject kèm issues
- **Tool:** brand-design-system skill — check màu, font, logo, layout, contrast
- **Guardrail:** Asset KHÔNG được qua Adapter nếu chưa pass checklist

### 4. Adapter Agent
- **Trigger:** Visual asset xong
- **Input:** Caption + asset
- **Output:** Package riêng từng platform với đúng format

| Platform | Format ảnh | Format video | Caption limit | Hashtag |
|----------|-----------|--------------|---------------|---------|
| Facebook | 1200x630 | 16:9, max 20p | 63,206 chars | 3-5 |
| Instagram Feed | 1080x1080 | 1:1, max 60s | 2,200 chars | 5-10 |
| Reels | 1080x1920 | 9:16, max 90s | 2,200 chars | 3-5 |
| TikTok | 1080x1920 | 9:16, 15-60s | 2,200 chars | 3-5 |
| YouTube Shorts | 1080x1920 | 9:16, max 60s | title 100 chars | - |

### 5. Review Queue (Airtable)
- **Schema:** xem `airtable-schema.json`
- **Status flow:** DRAFT → PENDING_REVIEW → APPROVED / REJECTED → POSTED
- **Notify:** Telegram message kèm preview khi có bài mới vào queue

### 5b. API Error Handler (bọc quanh Publisher)
- **Trigger:** Mọi lần Publisher Agent gọi API đăng bài
- **Input:** API call function + platform
- **Output:** Retry tự động nếu lỗi tạm thời, escalate Telegram nếu lỗi cần người xử lý
- **Tool:** api-error-handler skill — bảng lỗi theo platform, backoff strategy
- **Guardrail:** 1 platform fail không chặn platform khác; token hết hạn luôn alert ngay

### 6. Publisher Agent
- **Trigger:** Status = APPROVED trong Airtable
- **Input:** Package từng platform + scheduled_time
- **Output:** Post ID trả về từ API, update status → POSTED
- **Tools:**
  - Facebook/Instagram/Reels: Meta Graph API v18+
  - TikTok: TikTok Content Posting API
  - YouTube Shorts: YouTube Data API v3

### 6b. Sentiment Classifier (ngay sau Comment Monitor)
- **Trigger:** Comment mới fetch về, trước khi vào comment_queue
- **Input:** Comment text + post context
- **Output:** Label (URGENT_COMPLAINT/QUESTION/PURCHASE_INTENT/POSITIVE/NEGATIVE_MILD/SPAM/IRRELEVANT) + priority
- **Tool:** sentiment-classifier skill
- **Guardrail:** Confidence thấp luôn route thủ công, không tự động reply

### 7. Comment Monitor
- **Trigger:** Cron mỗi 2 giờ
- **Input:** Post IDs đã đăng
- **Output:** Draft reply cho comment mới, đưa vào queue riêng
- **Mode semi-auto:** Draft → Nobitano approve → reply
- **Mode auto (tương lai):** Auto reply comment thông thường, chỉ queue comment phức tạp

## n8n Workflow Nodes

```
Cron (8h sáng T2) → Trigger Ideation
Webhook (Telegram) → Parse lệnh → Route đến đúng agent
Airtable watch → Khi record APPROVED → trigger Publisher
Cron (2h/lần) → Comment Monitor
```

## Tech Stack

```
Orchestrator:  Hermes (Python, urllib)
Gateway:       OpenClaw (Node.js, Telegram bot)
Workflow:      n8n (port 5678, đang chạy trên VPS)
Queue/CMS:     Airtable
Visual gen:    HyperFrames (Node.js, không cần GPU)
Video render:  ffmpeg
Storage:       Local VPS /opt/trum-san-bay/assets/
```
