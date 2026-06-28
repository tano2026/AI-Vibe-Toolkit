# Marketing Automation — MCP Stack Guide

**Tổng hợp:** HubSpot MCP + n8n MCP + Make MCP
**Cập nhật:** tháng 6/2026

---

## Stack Theo Budget & Tech Level

```
Beginner, nhiều SaaS → Make MCP (3,260 apps, drag-drop familiar)
Intermediate, self-host ok → n8n MCP (free, powerful)
Marketing team → HubSpot MCP (CRM-first)
Full power → n8n + HubSpot MCP kết hợp
```

---

## HUBSPOT MCP — Marketing CRM

```bash
# Cài
git clone https://github.com/ZLeventer/hubspot-mcp
cd hubspot-mcp && npm install && npm run build
# API key: HubSpot → Settings → Integrations → Private Apps

# Daily marketing commands
"Lấy tất cả leads mới hôm nay, group theo source"
"Campaign nào có open rate cao nhất tháng này?"
"List contacts trong lifecycle stage Lead chưa được contact trong 14 ngày"
"Tạo list: opened email nhưng không click → enroll workflow re-engage"
"Get deals closing này tháng, sort theo value, assign follow-up tasks"
```

---

## N8N MCP — Automation Workflows

```bash
# Cài
npm install -g @kernel.salacoste/n8n-workflow-builder
# Config: N8N_HOST + N8N_API_KEY

# Build workflows bằng tiếng thường
"Tạo workflow: 6h sáng mỗi ngày → fetch GitHub trending AI repos → 
 tóm tắt top 5 → gửi Telegram @AI_Vibe_Toolkit_channel"

"Workflow: form submission → Claude analyze sentiment → 
 nếu positive: add vào testimonials sheet → 
 nếu negative: alert Slack #support"

"Monitor workflow: check video upload folder mỗi giờ → 
 khi có .mp4 mới → upload YouTube → post TikTok → notify Telegram"

# Manage
"List workflows failed trong 24h"
"Restart workflow 'Daily Content' sau khi fix"
"Get execution stats tuần này"
```

---

## MAKE MCP — 3,260 Apps

```bash
# Cài
git clone https://github.com/tommyevening/makemcp
cd makemcp && npm install && npm run build
# API token: Make → Profile → API/SDK

# Content & Social
"Tạo scenario: Airtable content calendar → Buffer schedule posts → 
 track performance → update sheet với metrics"

"Scenario: RSS feed AI news → Claude summarize → 
 post LinkedIn → post X/Twitter → log vào Notion"

# Lead Gen pipeline
"Scenario: Facebook Lead Ad form → HubSpot contact → 
 Clearbit enrich → Gmail welcome email → Slack alert sales"

# Video publishing
"Scenario: Google Drive /finished/ new file → 
 YouTube upload → TikTok upload → Instagram Reels → 
 notify Telegram khi tất cả done"
```

---

## Full Marketing Stack Kết Hợp

```
Content Creation:
claude-seo → /seo content-brief
marketingskills → /marketing blog-post
taste-skill → HTML/visual

Automation:
n8n MCP → workflow publish + distribute
Make MCP → cross-platform posting

CRM & Analytics:
HubSpot MCP → track leads + performance
last30days → monitor community sentiment

Image/Video:
fal-mcp → thumbnails, visuals
html-video → intros, transitions
supertonic → voiceover
```

---

## Prompt Templates Marketing

### Weekly Report
```
"Dùng HubSpot MCP lấy data tuần này:
- New leads (vs tuần trước)
- Deal pipeline movement  
- Email campaign performance
- Tóm tắt thành weekly report markdown"
```

### Content Ideation
```
"/last30days 'AI tools frustrations 2026'
→ Lấy top pain points từ Reddit/X
→ marketingskills content-brief cho từng pain point
→ Tạo content calendar 2 tuần"
```

### A/B Test Setup
```
"/marketing headline-test [landing-page-url]
→ Generate 5 headline variants
→ Create tracking UTMs cho từng variant
→ Setup n8n workflow track conversions"
```

---
*skills/marketing-automation-mcp-guide.md | AI Vibe Toolkit | tháng 6/2026*

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** automation marketing workflow

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
skill_prompt = fetch_skill("marketing-automation-mcp-guide.md")

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
