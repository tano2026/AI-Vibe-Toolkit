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

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** marketing YouTube channel

```python
import urllib.request, json, base64

def fetch_skill(skill_file, token="[GITHUB_TOKEN]"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/skills/{skill_file}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode()

# Bước 1: Fetch skill này về
skill_prompt = fetch_skill("youtube-marketing-skills.md")

# Bước 2: Extract phần "Prompt Template" hoặc "Nội dung skill"
# (tìm block code đầu tiên sau header ## Prompt)
import re
match = re.search(r'```\n([\s\S]+?)\n```', skill_prompt)
prompt = match.group(1) if match else skill_prompt

# Bước 3: Nhúng vào LLM call
def call_with_skill(user_input, system_prompt):
    # Gọi Claude/DeepSeek với skill làm system prompt
    payload = json.dumps({
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 2000,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_input}]
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=payload,
        headers={"x-api-key": "[ANTHROPIC_KEY]",
                 "anthropic-version": "2023-06-01",
                 "Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["content"][0]["text"]

# Dùng:
# result = call_with_skill("Phân tích thị trường AI tools VN 2026", prompt)
```

> Skills không cần cài gì — fetch về, nhúng làm system prompt, gọi LLM.
