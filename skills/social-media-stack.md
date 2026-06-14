# Social Media Stack — Facebook/YouTube/TikTok Guide Dùng Ngay

**Tổng hợp:** claude-ads + affiliate-skills + viral-hooks + youtube-skills + meta-mcp + buffer-mcp + poppify
**Cập nhật:** tháng 6/2026

---

## Stack Theo Mục Tiêu

```
Muốn grow YouTube organic        → youtube-marketing-skills + viral-hooks
Muốn chạy paid ads               → claude-ads + meta-mcp-server
Muốn làm affiliate content       → affiliate-skills + viral-hooks
Muốn auto-schedule social posts  → buffer-mcp + meta-mcp-server
Muốn tạo video nhanh từ ảnh      → poppify
Muốn full stack marketing        → tất cả kết hợp
```

---

## Quick Commands Theo Platform

### YOUTUBE
```bash
/yt keyword-research "topic"          # Tìm keyword có traffic
/yt script-outline "hook + topic"     # Outline video
/yt title-optimize "draft title"      # SEO title
/yt description-write "topic"         # Description + timestamps
/yt thumbnail-brief "concept"         # Brief cho thumbnail

# + viral-hooks cho hook:
"Tạo 3 hook variants cho video YouTube về [topic]"
```

### TIKTOK
```bash
# Tạo video từ ảnh
"Make a 30s TikTok from these screenshots" → Poppify

# Viral hooks
"Tạo TikTok hook kiểu CURIOSITY GAP cho [topic]"

# Script ngắn
/marketing video-script "[topic]" --duration 60s --platform tiktok
```

### FACEBOOK & INSTAGRAM
```bash
# Post content
"Đăng Facebook post: [nội dung]" → meta-mcp-server
"Schedule Instagram photo 7pm: [caption + hashtags]"

# Audit ads
/ads meta audit
/ads creative audit

# Analytics
"Get Facebook page insights tuần này"
"Instagram: top 5 posts engagement rate tháng này"
```

### CROSS-PLATFORM SCHEDULING
```bash
# Buffer MCP — 1 lần, đăng mọi nơi
"Schedule announcement video mới cho tất cả platforms:
 - X 9:00am: thread 3 tweets
 - Facebook 9:15am: caption 200 words
 - Instagram 9:30am: caption + 20 hashtags
 - LinkedIn 10:00am: professional angle"
```

---

## Workflow Hoàn Chỉnh — Từ Tool Mới Đến Published

```bash
# Step 1: Research (5 phút)
/yt keyword-research "tool name"
/last30days "tool name community sentiment"

# Step 2: Hook (2 phút)
"Tạo 5 hook variants cho [tool] với viral-hooks-skill"
→ Chọn hook tốt nhất

# Step 3: Script (10 phút)
/yt script-outline "[hook] + [tool overview]"
# hoặc content-creator.md skill

# Step 4: Voiceover (5 phút)
supertonic --file script.txt --lang vi --out voice.wav

# Step 5: Visual (10 phút)
/image "thumbnail: [hook text], dark bg, neon accent" → fal-mcp
# hoặc poppify từ screenshots

# Step 6: SEO (5 phút)
/yt title-optimize "draft title"
/yt description-write "topic" --include-timestamps
/yt tag-generator "topic"

# Step 7: Publish & Schedule (5 phút)
# Upload YouTube manually (API upload phức tạp)
# Buffer MCP → schedule social posts
"Schedule announcement cho Facebook, Instagram, X, LinkedIn"

# Step 8: Track (weekly)
/yt top-videos --period 7d
"Get meta insights tuần này"
```

---

## Ads Budget Decision Tree

```
Có budget quảng cáo?
├── < $100/tháng → Tập trung organic (YouTube SEO + TikTok)
├── $100-500/tháng → Meta Ads retargeting only
└── > $500/tháng → Full funnel: Meta Top + Google Middle + Retargeting Bottom

Audit trước khi tăng budget:
/ads audit --platform [platform]
→ Score < 60: fix issues trước khi scale
→ Score > 80: safe to scale
```

---

## Prompt Templates Social Media

### TikTok/Reels Hook (15 giây)
```
"Tạo TikTok hook 15 giây cho [TOOL]:
Hook type: [curiosity gap / contrarian / social proof]
Key stat: [X]k stars / [Y]% faster / [Z] minutes saved
Audience: vibe coders, non-technical builders
Tiếng Việt, casual, punchy"
```

### YouTube Description Template
```
"Viết YouTube description cho video [TITLE]:
- Hook paragraph (2-3 câu)
- What you'll learn (bullet points)
- Timestamps: [list chapters]
- Links section: GitHub + related videos
- Hashtags: #vibecoding #claudecode #aitools
- CTA: subscribe + notification bell
SEO optimize cho keyword: [keyword]"
```

### Facebook Post (Educational)
```
"Viết Facebook post educational về [TOOL]:
- Hook: stat hoặc surprising fact
- Problem nó giải quyết
- Key features (3 bullet points)
- Cách dùng nhanh
- CTA: comment 'LINK' để nhận link
Tone: casual, tiếng Việt, 200-300 words"
```

---
*skills/social-media-stack.md | AI Vibe Toolkit | tháng 6/2026*
