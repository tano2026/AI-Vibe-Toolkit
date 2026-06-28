# meta-mcp-server — 200+ Tools Facebook/Instagram/Threads/Ads (15⭐)

**GitHub:** https://github.com/oliverames/meta-mcp-server
**Stars:** 15⭐ | **License:** MIT | **npm:** @oliverames/meta-mcp-server
**Platforms:** Facebook Pages · Instagram · Threads · Ads Manager · Commerce · Insights

---

## Cài Đặt

```bash
# Download bundle (recommended)
# GitHub Releases → meta-mcp-server-2.0.2.mcpb

# Hoặc npm
npm install -g @oliverames/meta-mcp-server
```

```json
{
  "mcpServers": {
    "meta": {
      "command": "npx",
      "args": ["-y", "@oliverames/meta-mcp-server"],
      "env": {
        "META_ACCESS_TOKEN": "your-token",
        "META_PAGE_ID": "your-page-id"
      }
    }
  }
}
```

**Lấy token:** Meta Business Suite → Settings → Business Integrations → Create App

---

## 200+ Tools — 7 Platforms

### Facebook Pages
```bash
# Posts
"Đăng post lên Facebook Page: [nội dung]"
"Schedule post ngày mai 9am: [nội dung]"
"Get tất cả posts tháng này, sort theo engagement"
"List comments cần reply trên bài hôm nay"

# Analytics
"Get page insights: reach, engagement, fan growth tuần này"
"Which post type performs best? Photo vs video vs link?"
"Best time to post dựa trên audience activity"
```

### Instagram
```bash
"Post Instagram photo với caption và hashtags"
"Schedule Instagram Reel cho 7pm tối nay"
"Get story insights: views, exits, replies"
"List DMs cần respond"
"Get hashtag performance cho tháng này"
```

### Threads
```bash
"Post Threads update về tool mới"
"Get replies và mentions"
"Schedule thread series"
```

### Ads Manager
```bash
"Create Facebook ad campaign: objective, budget, audience"
"Get ad performance: CTR, CPC, ROAS last 7 days"
"Pause ads với CPR > $X"
"Duplicate best performing ad set với new audience"
"Get breakdown: age, gender, placement performance"
```

### Instagram Shopping
```bash
"List product catalog"
"Tag products trong Instagram post"
"Get shopping insights"
```

### Conversions API
```bash
"Send conversion event: purchase, lead, add to cart"
"Setup server-side tracking"
```

---

## Workflow Social Media Daily

```bash
# Morning: Review performance
"Get Facebook + Instagram insights từ hôm qua: 
 top performing content, comments cần reply, 
 ad spend vs conversions"

# Content posting
"Post video mới lên Facebook Page với description [X], 
 cross-post lên Instagram, schedule Threads announcement"

# Engagement
"List tất cả comments chưa reply trong 24h → 
 draft replies theo brand voice"

# Weekly ads review
"Get all active campaigns performance → 
 pause underperformers (CTR < 1%) → 
 increase budget cho winners (ROAS > 3x)"
```

---
*Nguồn: github.com/oliverames/meta-mcp-server | 15⭐ | MIT | 200+ tools | tháng 6/2026*

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
import urllib.request, json, urllib.parse

def meta_get_insights(page_id, metric, access_token, period="day"):
    url = (f"https://graph.facebook.com/v19.0/{page_id}/insights"
           f"?metric={metric}&period={period}&access_token={access_token}")
    req = urllib.request.Request(url)
    return json.loads(urllib.request.urlopen(req).read())["data"]

def meta_create_post(page_id, message, access_token):
    payload = urllib.parse.urlencode({
        "message": message, "access_token": access_token
    }).encode()
    req = urllib.request.Request(
        f"https://graph.facebook.com/v19.0/{page_id}/feed",
        data=payload, method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

def meta_get_ad_insights(ad_account_id, access_token, fields="spend,impressions,clicks,ctr"):
    url = (f"https://graph.facebook.com/v19.0/act_{ad_account_id}/insights"
           f"?fields={fields}&date_preset=last_7d&access_token={access_token}")
    req = urllib.request.Request(url)
    return json.loads(urllib.request.urlopen(req).read())["data"]

# Dùng: insights = meta_get_insights("PAGE_ID", "page_views_total",
#            os.environ["META_ACCESS_TOKEN"])
```

### OpenClaw
```bash
npx -y meta-mcp-server
# Set META_ACCESS_TOKEN + META_AD_ACCOUNT_ID
```

### Antigravity
```bash
# Không cần deploy
# Lấy token: developers.facebook.com → Graph API Explorer
```
> ⚠️ Cần Facebook App + Page Access Token. Dùng cho ABTRIP page insights.
