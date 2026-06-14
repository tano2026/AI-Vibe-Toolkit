# 🗂️ AI VIBE TOOLKIT — MASTER SKILL INDEX

**Kho:** github.com/tano2026/AI-Vibe-Toolkit
**Cập nhật:** tháng 6/2026
**Tổng:** 13 MCPs | 30 Repos | 12 Skills | 1 Stack | 41 Scripts

> File này là bản đồ toàn bộ kho — dùng để tra cứu nhanh,
> tìm đúng tool/skill/MCP cho từng situation.

---

## 🧭 TRA CỨU NHANH THEO SITUATION

| Mày muốn làm gì | Dùng cái nào | File |
|-----------------|-------------|------|
| Claude hết bịa code/API | Context7 MCP | `mcps/context7.md` |
| Claude tự search web | Brave Search MCP | `mcps/brave-search.md` |
| Claude đọc website/link | Firecrawl MCP | `mcps/firecrawl.md` |
| Claude cào web free | Crawl4AI MCP | `mcps/crawl4ai.md` |
| Claude test web tự động | Playwright MCP | `mcps/playwright.md` |
| Claude đọc file local | Filesystem MCP | `mcps/filesystem.md` |
| Claude commit/push GitHub | GitHub MCP | `mcps/github-mcp.md` |
| Claude nghĩ kỹ trước khi làm | Sequential Thinking MCP | `mcps/sequential-thinking.md` |
| AI nhớ mày qua nhiều phiên | Mem0 / Hermes Agent | `repos/mem0.md`, `repos/hermes-agent.md` |
| AI agent tự vận hành 24/7 | Hermes Agent | `repos/hermes-agent.md` |
| Audit SEO toàn site | claude-seo plugin | `skills/claude-seo-commands.md` |
| UI AI trông đẹp, có gu | taste-skill | `skills/taste-skill/` |
| Coding AI theo đúng rules | ai-coding-rules | `skills/ai-coding-rules-from-continue.md` |
| Research nhanh bất kỳ chủ đề | Research Agent skill | `skills/research-agent.md` |
| 1 idea → 10 loại content | Content Creator skill | `skills/content-creator.md` |
| Code nhưng không chuyên | Vibe Coder Assistant | `skills/vibe-coder-assistant.md` |
| Claude hiểu giọng văn của mày | Voice Profile Builder | `skills/voice-profile-builder.md` |
| Browser tự điền form, click | browser-use | `repos/browser-use.md` |
| Video từ React code | Remotion | `repos/remotion.md` |
| NotebookLM + Claude Code | NotebookLM MCP | `mcps/notebooklm-mcp-*.md` |
| Làm slide từ NotebookLM | NotebookLM Slide Commands | `skills/notebooklm-slide-commands.md` |
| TTS local $0 thay ElevenLabs | Supertonic | `repos/supertonic.md` |
| RAG nặng → nhẹ hơn 8x | TurboVec | `repos/turbovec.md` |
| 500+ AI agent use cases có code | 500-AI-Agents-Projects | `repos/500-ai-agents-projects.md` |
| AI agent framework tốt nhất | Hermes Agent | `repos/hermes-agent.md` |

---

## 🔌 MCPs — 13 Cái (Cài Vào Claude Code / Cursor)

### Setup chung:
```json
// Thêm vào claude_desktop_config.json hoặc .cursor/mcp.json
{
  "mcpServers": {
    "context7": { ... },
    "brave-search": { ... },
    "firecrawl": { ... }
  }
}
```

### Danh sách đầy đủ:

| MCP | Dùng cho | Install |
|-----|---------|---------|
| **Context7** | Docs up-to-date, hết bịa API | `npx -y @upstash/context7-mcp` |
| **Brave Search** | Claude tự search web real-time | `npx -y @modelcontextprotocol/server-brave-search` |
| **Firecrawl** | Paste link → Claude đọc website | `npx -y firecrawl-mcp` |
| **Crawl4AI** | Cào web free, 63k⭐ | `uvx crawl4ai-mcp` |
| **Playwright** | Claude tự test/thao tác web | `npx -y @playwright/mcp` |
| **Filesystem** | Đọc file local không copy paste | `npx -y @modelcontextprotocol/server-filesystem` |
| **GitHub MCP** | Tự commit, tạo PR, đọc repo | `npx -y @modelcontextprotocol/server-github` |
| **Sequential Thinking** | Bắt AI nghĩ trước khi làm | `npx -y @modelcontextprotocol/server-sequential-thinking` |
| **NotebookLM (PleasePrompto)** | NotebookLM API, 2.7k⭐ | Xem `mcps/notebooklm-mcp-pleaseprompto.md` |
| **NotebookLM (roomi-fields)** | REST + Docker variant | Xem `mcps/notebooklm-mcp-roomifields.md` |
| **NotebookLM Secure (Pantheon)** | Bảo mật hơn | Xem `mcps/notebooklm-mcp-secure.md` |
| **NotebookLM 2026 (Python)** | Python-based, mới nhất | Xem `mcps/notebooklm-mcp-2026.md` |
| **NotebookLM Server** | Auto-update | Xem `mcps/notebooklm-mcp-server.md` |

**MCP Stack tối thiểu (cài 3 cái này trước):**
```
Context7 + Brave Search + Firecrawl = 80% use cases
```

---

## 📦 REPOS — 30 Cái (Theo Category)

### 🤖 AI Agents & Frameworks
| Repo | Stars | Dùng cho |
|------|-------|---------|
| **Hermes Agent** | 188k⭐ | AI agent self-learning, 8 loops, memory xuyên phiên |
| **500-AI-Agents-Projects** | 32.4k⭐ | 500+ use case có code thật theo ngành |
| **browser-use** | 95k⭐ | Browser tự thao tác bằng ngôn ngữ tự nhiên |
| **OpenClaw** | 210k⭐ | AI agent framework fastest growing |
| **n8n-claw** | - | N8N + AI agent tự vận hành |
| **Mem0** | - | Memory layer cho AI agent |
| **Bumblebee** | - | Scan MCP packages an toàn |

### 🎨 Frontend & UI
| Repo | Stars | Dùng cho |
|------|-------|---------|
| **taste-skill** | 43.3k⭐ | Anti-slop frontend — UI có gu |
| **html-anything** | 6.2k⭐ | Canva $0 — HTML thay design tool |
| **sc-datav** | - | Dashboard 3D đẹp |
| **HyperFrames** | - | Video edit bằng HTML |
| **Remotion** | 49.9k⭐ | React → Video MP4 |
| **html-video** | ~346⭐ | Paste link → nhận MP4 |

### 🔊 Audio & Media
| Repo | Stars | Dùng cho |
|------|-------|---------|
| **Supertonic** | 5.3k⭐ | TTS local $0, thay ElevenLabs |
| **DiffusionGemma** | - | LLM architecture mới của Google |

### 🧠 AI Tools & Skills
| Repo | Stars | Dùng cho |
|------|-------|---------|
| **Superpowers** | 150k⭐ | Plugin pack 150k stars |
| **Agent Skills** | 109k⭐ | Skills cho AI agents (mattpocock) |
| **System Prompts Leaked** | - | Bộ sưu tập system prompts |
| **claude-seo** | 8.8k⭐ | SEO audit plugin cho Claude Code |
| **continue** | 33.7k⭐ | Coding agent (discontinued, học concept) |
| **marketingskills** | 31.9k⭐ | 43 AI marketing skills |

### 📊 Data & Performance
| Repo | Stars | Dùng cho |
|------|-------|---------|
| **TurboVec** | ~6k⭐ | RAG 31GB→4GB, 8x nhẹ hơn |
| **LMCache** | - | Cache LLM responses, giảm latency |
| **magika** | 15.2k⭐ | Google file type detection |

### 📚 Learning & Reference
| Repo | Stars | Dùng cho |
|------|-------|---------|
| **Vibe Coding Roadmap** | - | Lộ trình vibe coding từ đầu |
| **last30days** | - | GitHub trending 30 ngày, không bị index |
| **nanochat** | - | Train AI với $15 (Karpathy) |
| **AiToEarn** | - | Kiếm tiền với AI |
| **Plannotator** | ~6k⭐ | Review plan AI trước khi approve |

---

## 🧠 SKILLS — 12 Cái (Dùng Ngay)

### Category: Prompt Templates (copy-paste dùng ngay)

**1. Research Agent** — `skills/research-agent.md`
- Dùng: Nhờ Claude research bất kỳ chủ đề nào
- Best with: Brave Search + Firecrawl MCP
- Output: Báo cáo có nguồn, có phân tích

**2. Content Creator** — `skills/content-creator.md`
- Dùng: 1 idea → script TikTok + caption + hook + thumbnail + tweet + email
- Level: Beginner
- Output: 7 loại content format từ 1 input

**3. Vibe Coder Assistant** — `skills/vibe-coder-assistant.md`
- Dùng: System prompt — Claude giải thích code kiểu người thường
- Best for: Người mới code, không muốn bị làm phức tạp

**4. Voice Profile Builder** — `skills/voice-profile-builder.md`
- Dùng: 2-stage workflow — Claude học giọng văn của mày
- Output: Profile file → paste 1 lần, Claude hiểu mày mãi mãi

**5. Auto Research Trending** — `skills/auto-research-trending.md`
- Dùng: Tự động research GitHub trending, tổng hợp báo cáo

**6. AI Content Writing (6 prompts)** — `skills/ai-content-writing.md`
- Dùng: 6 prompt templates cho content marketing

**7. ML Concepts Explainer** — `skills/ml-concepts-explainer.md`
- Dùng: Giải thích ML/AI concepts theo kiểu dễ hiểu

**8. NotebookLM Slide Commands** — `skills/notebooklm-slide-commands.md`
- Dùng: 8 prompts tạo slide từ NotebookLM

### Category: AI Coding Rules

**9. AI Coding Rules (from Continue)** — `skills/ai-coding-rules-from-continue.md`
- Dùng: Copy vào CLAUDE.md / .cursorrules
- Content: 7 sections — Personality, TypeScript, Testing, CSS, Docs, PR Agents, Template

**10. taste-skill Frontend** — `skills/taste-skill/` (10 files)
- Dùng: Anti-slop UI cho AI coding
- Files: taste-skill.md, redesign-skill.md, soft-skill.md, minimalist-skill.md, brutalist-skill.md...
- INDEX.md để biết dùng file nào

**11. claude-seo Commands** — `skills/claude-seo-commands.md`
- Dùng: Cheat sheet 25 lệnh /seo đầy đủ + quick decision guide

**12. continue .continue/ Folder** — `skills/continue-dot-continue-folder.md`
- Dùng: 15 rules + 5 agents + 3 prompts gốc từ Continue repo
- Copy vào .continue/ hoặc CLAUDE.md

---

## 🏗️ STACK — 1 Cái

**AI Content Stack Việt** — `stacks/ai-content-stack-viet.md`
- Workflow viết content hoàn chỉnh: Idea → Draft → Polish → Publish
- Chi phí: $0 đến $20/tháng
- Tools: Claude + Brave Search + Firecrawl + Canva/html-anything

---

## 🎬 SCRIPTS — 41 Video Sẵn Sàng Quay

### Theo Priority (Hook mạnh nhất):
| # | Video | Hook |
|---|-------|------|
| 12 | Vibe Coding Roadmap | Hook rộng nhất |
| 08 | OpenClaw 210k stars | Số stars gây sốc |
| 20 | browser-use | Demo ấn tượng nhất |
| 37 | Hermes Agent | Compound learning loop |
| 41 | taste-skill | Before/after UI rõ nhất |
| 39 | claude-seo | 18 agents chạy song song |
| 29 | NotebookLM MCP | Zero hallucination angle |
| 01 | Context7 | MCP cơ bản dễ demo |

### Tất cả scripts: `content/script-video-01` đến `content/script-video-41`

---

## 🚀 QUICK START — Bắt Đầu Từ Đây

### Nếu mày mới setup Claude Code:
1. Cài Context7 + Brave Search + Firecrawl MCP
2. Copy `skills/vibe-coder-assistant.md` vào CLAUDE.md
3. Copy `skills/taste-skill/taste-skill.md` vào project frontend
4. Dùng `skills/research-agent.md` cho research task đầu tiên

### Nếu mày làm content:
1. Dùng `skills/voice-profile-builder.md` để Claude học giọng văn
2. Dùng `skills/content-creator.md` hàng ngày
3. Xem `stacks/ai-content-stack-viet.md` cho full workflow

### Nếu mày làm SEO:
1. Cài claude-seo plugin
2. Mở `skills/claude-seo-commands.md`
3. Bắt đầu với `/seo audit https://your-site.com`

### Nếu mày muốn build AI agent:
1. Đọc `repos/hermes-agent.md`
2. Tham khảo `repos/500-ai-agents-projects.md` cho use case
3. Thêm memory với `repos/mem0.md`

---

*AI Vibe Toolkit | Master Skill Index*
*github.com/tano2026/AI-Vibe-Toolkit*
*Cập nhật: tháng 6/2026*

---

## 🤖 HERMES AGENT — WORKFLOW CHO AI VIBE TOOLKIT

> Xem chi tiết: `skills/hermes-agent-deep-dive.md`

### Setup 1 lần (15 phút):
```bash
# Cài Hermes
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup --portal

# Điền USER.md — context về kho
# ~/.hermes/USER.md:
# - Kho: github.com/tano2026/AI-Vibe-Toolkit
# - Workflow: link → research → .md → script → push → TRACKER
# - Style: tiếng Việt, casual, có ví dụ thực tế
# - Format: xem _template.md trong kho
```

### Dùng hàng ngày:
```bash
# Thay chat thường → dùng /goal
/goal "research [repo/tool mới], viết .md và script video, push lên kho"

# Batch 3 repos cùng lúc
delegate_task("research repo A") &
delegate_task("research repo B") &
delegate_task("research repo C") &
```

### Lịch trình compound:
- **Ngày 1-7:** Setup, L1+L5 chạy
- **Ngày 8-30:** /goal cho mọi entry → L3 build skills về kho
- **Ngày 31-60:** 15-20 skills tích lũy → dùng delegate_task
- **Ngày 90+:** Agent biết kho như chính mày, nhanh hơn 40%

---
*MASTER-INDEX cập nhật: tháng 6/2026*
