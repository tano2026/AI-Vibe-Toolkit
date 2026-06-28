# KHO-INDEX — AI Vibe Toolkit
> Cập nhật: tháng 6/2026 | Version: 2.1
> **Entry point duy nhất cho mọi agent. Fetch file này đầu tiên.**

---

## Kho là gì

- **Repo:** https://github.com/tano2026/AI-Vibe-Toolkit
- **Chủ:** Nobitano — vibe coder, content creator, digital marketer VN
- **Mục đích kép:**
  1. Knowledge base để agents thực thi task
  2. Content factory — mỗi entry = 1 video TikTok/YouTube Shorts

---

## Số liệu thực tế (tháng 6/2026)

| Folder | Số files | Ghi chú |
|--------|----------|---------|
| /mcps/ | 37 | MCP servers |
| /repos/ | 92 | GitHub repos |
| /skills/ | 85 | Prompt templates |
| /stacks/ | 3 | Combo workflows |
| /agents/ | 7 | Playbook agents |
| /content/ | 126 | Script video |

---

## Agent nào đọc file nào tiếp theo

| Agent | Fetch ngay sau file này |
|-------|------------------------|
| **Hermes** | `agents/HERMES-PLAYBOOK.md` |
| **OpenClaw** | `agents/OPENCLAW-PLAYBOOK.md` |
| **Antigravity** | `agents/ANTIGRAVITY-PLAYBOOK.md` |
| **Claude** | Không cần — gọi GitHub API trực tiếp trong session |

---

## Trạng thái patch Agent Integration (tháng 6/2026)

**49 files đã có section `## 🤖 Agent Integration`** — Hermes đọc block Python, chạy được ngay.

### Tier 1 — MCPs có REST API (11 files) ✅ ĐÃ PATCH HẾT

| File | API Endpoint | Key cần |
|------|-------------|---------|
| mcps/firecrawl.md | api.firecrawl.dev/v1/scrape | FIRECRAWL_API_KEY |
| mcps/brave-search.md | api.search.brave.com/res/v1/web/search | BRAVE_API_KEY |
| mcps/github-mcp.md | api.github.com | GITHUB_TOKEN |
| mcps/markitdown-mcp.md | local pip | không cần |
| mcps/pollinations-mcp.md | image.pollinations.ai | không cần (free) |
| mcps/mcp-youtube.md | googleapis.com/youtube/v3 | YOUTUBE_API_KEY |
| mcps/fal-mcp.md | fal.run/fal-ai/ | FAL_KEY |
| mcps/minimax-mcp.md | api.minimax.chat/v1 | MINIMAX_API_KEY |
| mcps/meta-mcp-server.md | graph.facebook.com/v19.0 | META_ACCESS_TOKEN |
| mcps/n8n-workflow-builder-mcp.md | localhost:5678/api/v1 | N8N_API_KEY |
| mcps/crawl4ai.md | localhost:11235/crawl | self-hosted |

### Tier 2 — Repos self-hostable (25 files) ✅ ĐÃ PATCH HẾT

Antigravity deploy 1 lần → Hermes gọi endpoint mãi mãi.

| File | Port | Deploy bằng |
|------|------|------------|
| repos/mem0.md | cloud/8000 | pip / Docker |
| repos/supabase.md | cloud/5432 | Docker |
| repos/dify.md | 80 | Docker |
| repos/langflow.md | 7860 | pip / Docker |
| repos/open-webui.md | 3000 | Docker |
| repos/coolify.md | 8000 | script |
| repos/stirling-pdf.md | 8080 | Docker |
| repos/markitdown.md | local | pip |
| repos/browser-use.md | - | pip |
| repos/maxun.md | 8080 | Docker |
| repos/openhands.md | 3000 | Docker |
| repos/tiktokautouploader.md | - | pip |
| repos/magika.md | - | pip |
| repos/billionmail.md | 8080 | Docker |
| repos/chattts.md | 9966 | pip |
| repos/f5-tts.md | 7860 | pip |
| repos/kokoro-82m.md | 8880 | pip |
| repos/vimax.md | 8000 | pip |
| repos/vectcutapi.md | 8000 | pip |
| repos/turbovec.md | 6333 | Docker |
| repos/mediacrawler.md | - | pip |
| repos/n8n-claw.md | 5678 | Docker |
| repos/headroom.md | 8000 | pip |
| repos/lmcache.md | 8000 | pip |
| repos/narratoai.md | 7860 | pip |

### Tier 3 — Skills/Prompts (13 files) ✅ ĐÃ PATCH HẾT

Fetch về → dùng làm system prompt cho LLM call. Không cài gì.

| File | Dùng khi |
|------|---------|
| skills/research-agent.md | Research thị trường, phân tích tool |
| skills/content-creator.md | Viết script video, social post |
| skills/token-efficient-research.md | Research nhiều source, tiết kiệm token |
| skills/fact-checker.md | Verify thông tin trước khi báo chủ |
| skills/auto-research-trending.md | Tự động research trending |
| skills/mem0-skill.md | Lưu/retrieve memory preferences |
| skills/hermes-agent-deep-dive.md | Reference Hermes architecture |
| skills/viral-hooks-skill.md | Viết hook cho video content |
| skills/personal-branding-creator.md | Content personal brand |
| skills/social-media-stack.md | Chọn tool cho từng platform |
| skills/youtube-marketing-skills.md | Marketing YouTube |
| skills/vibe-coder-assistant.md | Assist coding tasks |
| skills/marketing-automation-mcp-guide.md | Automation marketing |

### Còn lại — ~170 files — KHÔNG có Agent Integration

Frontend tools, video-only tools, reference docs.
Hermes đọc TL;DR để biết tool làm gì, không thực thi trực tiếp được.

---

## Fetch function chuẩn

### Python (Hermes)
```python
import urllib.request, json, base64, os

def fetch(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode()

# Workflow chuẩn khi nhận task:
# 1. fetch("KHO-INDEX.md")           → map toàn bộ kho
# 2. fetch("agents/HERMES-PLAYBOOK.md") → instruction của mày
# 3. fetch("mcps/[tool].md")         → đọc Agent Integration block
# 4. Chạy code Python trong block đó
```

### Node.js (OpenClaw)
```javascript
const https = require("https");
async function fetchKho(path) {
  return new Promise((resolve, reject) => {
    https.get({
      hostname: "api.github.com",
      path: `/repos/tano2026/AI-Vibe-Toolkit/contents/${path}`,
      headers: { "Authorization": `token ${process.env.GITHUB_TOKEN}`,
                 "User-Agent": "openclaw",
                 "Accept": "application/vnd.github.v3+json" }
    }, res => {
      let d = ""; res.on("data", c => d += c);
      res.on("end", () => resolve(Buffer.from(JSON.parse(d).content, "base64").toString()));
    }).on("error", reject);
  });
}
```

### Bash (Antigravity)
```bash
fetch_kho() {
  curl -sf     -H "Authorization: token $GITHUB_TOKEN"     -H "Accept: application/vnd.github.v3+json"     "https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/$1"     | python3 -c "import sys,json,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"
}
```

---

## Quy tắc đọc file .md trong kho

| Section trong file | Hermes đọc? | OpenClaw? | Antigravity? |
|--------------------|-------------|-----------|--------------|
| TL;DR | ✅ | ✅ | ✅ |
| Dùng để làm gì | ✅ | ✅ | ✅ |
| Setup Claude Desktop / npx | ❌ skip | ✅ | ❌ |
| `## 🤖 Agent Integration` | ✅ **ĐỌC NGAY** | ✅ | ✅ |
| → Hermes (Python) block | ✅ | - | - |
| → OpenClaw block | - | ✅ | - |
| → Antigravity block | - | - | ✅ |
| Đánh giá cá nhân | tham khảo | tham khảo | - |

---

## Phân công 3 agent

```
Nobitano nhắn Telegram
        ↓
OpenClaw nhận, phân loại
        ├── Browser / UI / WhatsApp  → OpenClaw tự làm
        ├── Python / API / data      → Hermes
        ├── Deploy / install / VPS   → Antigravity
        └── Thêm entry kho / .md mới → Báo chủ → Claude làm
                ↓
          Hermes thực thi
                ├── Fetch file .md → đọc "Hermes (Python)" block → chạy
                ├── Tier 1: gọi REST API trực tiếp (11 MCPs)
                ├── Tier 2: gọi localhost endpoint (25 repos, Antigravity đã deploy)
                └── Tier 3: fetch skill → nhúng system prompt → gọi LLM
                        ↓
                  Antigravity (khi được yêu cầu)
                        ├── pip install packages
                        ├── Docker deploy services
                        └── Báo endpoint về cho Hermes
```

---

## Env vars toàn hệ thống

```bash
# GitHub
GITHUB_TOKEN=[GITHUB_TOKEN]

# Search/Scrape (free tier đủ dùng hàng ngày)
BRAVE_API_KEY=          # brave.com/search/api — 2000 req/month free
TAVILY_API_KEY=         # tavily.com — 1000 req/month free  
FIRECRAWL_API_KEY=      # firecrawl.dev — 500 req/month free

# LLM
ANTHROPIC_API_KEY=

# Media
FAL_KEY=                # fal.ai — pay per use, rất rẻ
MINIMAX_API_KEY=        # TTS tiếng Việt
MINIMAX_GROUP_ID=
YOUTUBE_API_KEY=        # free 10k units/ngày

# Database
SUPABASE_URL=
SUPABASE_KEY=

# Email
RESEND_API_KEY=         # free 3000/month

# Social
META_ACCESS_TOKEN=
TIKTOK_SESSION=         # cookies từ browser

# Memory
MEM0_API_KEY=           # cloud hoặc self-host port 8000
```
