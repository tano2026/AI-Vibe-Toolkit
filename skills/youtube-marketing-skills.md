# youtube-marketing-skills — 21 Commands Grow YouTube Channel (14⭐)

**GitHub:** https://github.com/adityaarsharma/youtube-marketing-skills
**Stars:** 14⭐ | **npm:** youtube-channel-mcp | **License:** MIT

---

## Cài Đặt

```bash
git clone https://github.com/adityaarsharma/youtube-marketing-skills
cd youtube-marketing-skills && npm install

# Cần: Google Cloud project + YouTube Data API v3 + Analytics API
# OAuth credentials.json → copy vào folder
```

```json
{
  "mcpServers": {
    "youtube": {
      "command": "node",
      "args": ["/path/to/youtube-marketing-skills/mcp/index.js"],
      "env": { "CHANNEL_ID": "UCxxx" }
    }
  }
}
```

---

## 21 Commands

### 📊 ANALYTICS
```bash
/yt analyze-channel            # Overview: subs, views, revenue trend
/yt top-videos --period 30d    # Top 10 videos last 30 days
/yt audience-report            # Demographics, watch time, retention
/yt traffic-sources            # Where viewers come from
/yt revenue-report             # RPM, CPM, estimated revenue
```

### 🔍 SEO & RESEARCH
```bash
/yt keyword-research "ai coding tools"    # Volume, competition, CPC
/yt title-optimize "current title"        # SEO-optimized title variants
/yt tag-generator "video topic"           # Relevant tags list
/yt competitor-analysis @channel          # Competitor gaps
/yt trending-topics "AI niche"            # What's trending now
```

### 📝 CONTENT
```bash
/yt script-outline "viral hook + topic"   # Full video script outline
/yt description-write "video topic"       # SEO description + timestamps
/yt thumbnail-brief "video concept"       # Thumbnail design brief
/yt shorts-repurpose "long video URL"     # Cut into Shorts strategy
/yt content-calendar --weeks 4            # 4-week content plan
```

### 🚀 GROWTH
```bash
/yt cta-optimize "current CTA"            # Better call-to-action
/yt community-post "content idea"         # Draft community post
/yt collab-outreach @channel              # Collab pitch template
/yt ab-test-setup "thumbnail A vs B"      # A/B test strategy
/yt retention-audit "video URL"           # Where viewers drop off
/yt monetization-audit                    # Revenue optimization
```

---

## Workflow Cho AI Vibe Toolkit Channel

```bash
# Weekly planning
/yt trending-topics "AI tools vibe coding"
/yt keyword-research "claude code skills"
→ Chọn topic có search volume cao + low competition

# Pre-production
/yt script-outline "hook + topic từ viral-hooks-skill"
/yt thumbnail-brief "concept video"
/yt title-optimize "draft title"

# Post-upload
/yt description-write "video topic" --include-timestamps
/yt tag-generator "video topic"

# Monthly review
/yt top-videos --period 30d
/yt audience-report
/yt revenue-report
```

---
*Nguồn: github.com/adityaarsharma/youtube-marketing-skills | 14⭐ | MIT | tháng 6/2026*
