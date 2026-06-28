# KHO-INDEX — AI Vibe Toolkit
> Cập nhật: tháng 6/2026 | Version: 2.0 — Agent-Ready
> **Entry point duy nhất cho mọi agent. Đọc file này trước tiên.**

---

## Kho này là gì

- **Repo:** https://github.com/tano2026/AI-Vibe-Toolkit
- **Chủ:** Nobitano — vibe coder, content creator, digital marketer (VN)
- **Mục đích kép:**
  1. Knowledge base để agents (Hermes/OpenClaw/Antigravity) thực thi task
  2. Content factory — mỗi entry = 1 video TikTok/YouTube Shorts

---

## Cấu trúc kho

```
/mcps/          37 files   MCP servers
/repos/         92 files   GitHub repos
/skills/        84 files   Prompt templates + system prompts
/stacks/         5 files   Combo tools theo use case
/agents/         8 files   Playbook riêng cho từng agent  ← ĐỌC TIẾP Ở ĐÂY
/content/      127 files   Script video TikTok/YouTube
TRACKER.md               Danh sách toàn bộ entries
KHO-INDEX.md             File này — entry point
```

---

## Mày là agent nào → đọc file nào ngay sau đây

| Agent | File cần đọc tiếp | Lệnh fetch |
|-------|------------------|-----------|
| **Hermes** | `/agents/HERMES-PLAYBOOK.md` | `fetch("agents/HERMES-PLAYBOOK.md")` |
| **OpenClaw** | `/agents/OPENCLAW-PLAYBOOK.md` | `fetchKho("agents/OPENCLAW-PLAYBOOK.md")` |
| **Antigravity** | `/agents/ANTIGRAVITY-PLAYBOOK.md` | `fetch_kho "agents/ANTIGRAVITY-PLAYBOOK.md"` |
| **Claude** | Không cần — gọi thẳng GitHub API trong session | - |

---

## Hệ thống Agent Integration — cách kho được tổ chức

**50 files trong kho đã được patch** với section `## 🤖 Agent Integration` ở cuối mỗi file.
Các file này chia làm 3 tier theo mức độ ưu tiên:

### Tier 1 — MCPs có REST API (11 files) — Hermes gọi thẳng
Không cần cài MCP. Gọi HTTP API trực tiếp bằng Python.

| File | API Endpoint | Key cần |
|------|-------------|---------|
| `mcps/firecrawl.md` | api.firecrawl.dev/v1/scrape | FIRECRAWL_API_KEY |
| `mcps/brave-search.md` | api.search.brave.com/res/v1/web/search | BRAVE_API_KEY |
| `mcps/github-mcp.md` | api.github.com | GITHUB_TOKEN |
| `mcps/markitdown-mcp.md` | pip install markitdown (local) | không cần |
| `mcps/pollinations-mcp.md` | image.pollinations.ai (free) | không cần |
| `mcps/mcp-youtube.md` | googleapis.com/youtube/v3 | YOUTUBE_API_KEY |
| `mcps/fal-mcp.md` | fal.run/fal-ai/ | FAL_KEY |
| `mcps/minimax-mcp.md` | api.minimax.chat/v1 | MINIMAX_API_KEY |
| `mcps/meta-mcp-server.md` | graph.facebook.com/v19.0 | META_ACCESS_TOKEN |
| `mcps/n8n-workflow-builder-mcp.md` | localhost:5678/api/v1 | N8N_API_KEY |
| `mcps/crawl4ai.md` | localhost:11235/crawl | self-hosted |

### Tier 2 — Repos self-hostable (25 files) — Antigravity deploy, Hermes gọi
Antigravity deploy 1 lần → Hermes gọi endpoint mãi mãi.

| File | Service | Port | Deploy bằng |
|------|---------|------|------------|
| `repos/mem0.md` | Memory layer | cloud/8000 | pip / Docker |
| `repos/supabase.md` | Database + Auth + Storage | cloud/5432 | Docker |
| `repos/dify.md` | LLM platform + workflows | 80 | Docker |
| `repos/langflow.md` | Agent builder UI | 7860 | pip / Docker |
| `repos/open-webui.md` | LLM UI + API | 3000 | Docker |
| `repos/coolify.md` | Deploy platform | 8000 | script |
| `repos/stirling-pdf.md` | PDF processing | 8080 | Docker |
| `repos/markitdown.md` | File reader local | local | pip |
| `repos/browser-use.md` | Browser automation | - | pip |
| `repos/maxun.md` | No-code scraper | 8080 | Docker |
| `repos/openhands.md` | Coding agent | 3000 | Docker |
| `repos/tiktokautouploader.md` | TikTok auto-upload | - | pip |
| `repos/magika.md` | File type detection | - | pip |
| `repos/billionmail.md` | Email marketing | 8080 | Docker |
| `repos/chattts.md` | TTS Vietnamese | 9966 | pip |
| `repos/f5-tts.md` | TTS high quality | 7860 | pip |
| `repos/kokoro-82m.md` | TTS lightweight | 8880 | pip |
| `repos/vimax.md` | Video processing | 8000 | pip |
| `repos/vectcutapi.md` | Video processing | 8000 | pip |
| `repos/turbovec.md` | Vector search | 6333 | Docker |
| `repos/mediacrawler.md` | Social media crawl | - | pip |
| `repos/n8n-claw.md` | Workflow + agent | 5678 | Docker |
| `repos/headroom.md` | Audio/video | 8000 | pip |
| `repos/lmcache.md` | LLM cache layer | 8000 | pip |
| `repos/narratoai.md` | AI narration | 7860 | pip |

### Tier 3 — Skills/Prompts (14 files) — Hermes fetch + nhúng vào LLM call
Không cài gì. Fetch về → dùng làm system prompt.

| File | Dùng khi |
|------|---------|
| `skills/research-agent.md` | Research thị trường, phân tích tool |
| `skills/content-creator.md` | Viết script video, social post |
| `skills/token-efficient-research.md` | Research nhiều source, tiết kiệm token |
| `skills/fact-checker.md` | Verify thông tin trước khi báo chủ |
| `skills/auto-research-trending.md` | Tự động research trending |
| `skills/mem0-skill.md` | Lưu/retrieve memory preferences |
| `skills/hermes-agent-deep-dive.md` | Reference nội bộ Hermes architecture |
| `skills/viral-hooks-skill.md` | Viết hook cho video content |
| `skills/personal-branding-creator.md` | Content personal brand |
| `skills/social-media-stack.md` | Chọn tool cho từng platform |
| `skills/youtube-marketing-skills.md` | Marketing YouTube |
| `skills/vibe-coder-assistant.md` | Assist coding tasks |
| `skills/marketing-automation-mcp-guide.md` | Automation marketing |
| `skills/hermes-agent-deep-dive.md` | Hermes architecture ref |

### Còn lại — ~175 files — KHÔNG dùng trực tiếp
Frontend tools (remotion, hyperframes, shadcn...), video-only tools, reference docs.
Hermes đọc để biết tool làm gì — không thực thi được trong Python runtime.

---

## Fetch function chuẩn — copy paste chạy ngay

### Python (Hermes dùng)
```python
import urllib.request, json, base64

GITHUB_TOKEN = "[GITHUB_TOKEN]"
REPO = "tano2026/AI-Vibe-Toolkit"

def fetch(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode("utf-8")

def list_folder(folder):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{folder}",
        headers={"Authorization": f"token {GITHUB_TOKEN}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    return [f["name"] for f in json.loads(urllib.request.urlopen(req).read())]

# Bắt đầu bằng:
playbook = fetch("agents/HERMES-PLAYBOOK.md")
# Sau đó đọc section nào cần
```

### Node.js (OpenClaw dùng)
```javascript
const https = require("https");
async function fetchKho(path) {
  return new Promise((resolve, reject) => {
    https.get({
      hostname: "api.github.com",
      path: `/repos/tano2026/AI-Vibe-Toolkit/contents/${path}`,
      headers: { "Authorization": `token ${process.env.GITHUB_TOKEN}`,
                 "User-Agent": "openclaw", "Accept": "application/vnd.github.v3+json" }
    }, res => {
      let d = ""; res.on("data", c => d += c);
      res.on("end", () => resolve(Buffer.from(JSON.parse(d).content, "base64").toString()));
    }).on("error", reject);
  });
}
// Bắt đầu: const pb = await fetchKho("agents/OPENCLAW-PLAYBOOK.md");
```

### Bash/curl (Antigravity dùng)
```bash
GITHUB_TOKEN="[GITHUB_TOKEN]"
fetch_kho() {
  curl -sf     -H "Authorization: token $GITHUB_TOKEN"     -H "Accept: application/vnd.github.v3+json"     "https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/$1"     | python3 -c "import sys,json,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"
}
# Bắt đầu: fetch_kho "agents/ANTIGRAVITY-PLAYBOOK.md"
```

---

## Quy tắc đọc file .md trong kho

Mỗi file trong kho có structure chuẩn. Agent đọc đúng section:

| Section | Claude | Hermes | OpenClaw | Antigravity |
|---------|--------|--------|----------|-------------|
| TL;DR | ✅ | ✅ | ✅ | ✅ |
| Dùng để làm gì | ✅ | ✅ | ✅ | ✅ |
| Setup Claude Desktop / npx | ✅ | ❌ skip | ✅ | ❌ |
| `## 🤖 Agent Integration` | - | ✅ **ĐỌC** | ✅ | ✅ |
| → Hermes (Python) block | - | ✅ | - | - |
| → OpenClaw block | - | - | ✅ | - |
| → Antigravity block | - | - | - | ✅ |
| Đánh giá cá nhân | ✅ | tham khảo | tham khảo | - |

**Quy tắc vàng:** Thấy file có `## 🤖 Agent Integration` → đọc đúng block của mình, bỏ qua phần còn lại.

---

## Phân công 3 agent

```
Nhận lệnh từ chủ qua Telegram
        ↓
   OpenClaw (điều phối)
        ├── Browser/UI task → OpenClaw tự xử
        ├── Python/API/data → Hermes
        ├── Deploy/install → Antigravity
        └── Thêm entry kho / viết .md → báo chủ để Claude xử lý
                ↓
           Hermes (thực thi Python)
                ├── Fetch kho → đọc Agent Integration block
                ├── Gọi REST API trực tiếp (Tier 1)
                ├── Gọi local endpoint sau khi Antigravity deploy (Tier 2)
                └── Fetch skill → nhúng vào LLM call (Tier 3)
                        ↓
                  Antigravity (deploy on demand)
                        ├── pip install packages cho Hermes
                        ├── Docker deploy services
                        └── Maintain + restart services
```

---

## Env vars toàn hệ thống — set 1 lần, dùng mãi

```bash
# GitHub
GITHUB_TOKEN=[GITHUB_TOKEN]

# Search
BRAVE_API_KEY=BSA-xxx           # brave.com/search/api — free 2000/month
TAVILY_API_KEY=tvly-xxx         # tavily.com — free 1000/month
FIRECRAWL_API_KEY=fc-xxx        # firecrawl.dev — free 500/month

# AI/Media
FAL_KEY=xxx                     # fal.ai — pay per use
MINIMAX_API_KEY=xxx             # platform.minimax.io
MINIMAX_GROUP_ID=xxx
YOUTUBE_API_KEY=xxx             # console.cloud.google.com

# Database/Storage
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=xxx

# Email
RESEND_API_KEY=re_xxx           # resend.com — free 3000/month

# Social
META_ACCESS_TOKEN=xxx           # developers.facebook.com
TIKTOK_SESSION=xxx              # cookies từ browser

# Memory
MEM0_API_KEY=xxx                # mem0.ai — hoặc self-host

# LLM
ANTHROPIC_API_KEY=xxx
```
