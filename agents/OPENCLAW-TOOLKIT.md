# OPENCLAW-TOOLKIT
> File này dành riêng cho OpenClaw. Đọc 1 lần, không cần fetch từng file .md riêng.
> Tổng hợp toàn bộ npm/ClawHub tools trong kho — nhóm theo category, kèm lệnh cài ngay.

---

## Cách dùng file này

1. Đọc category phù hợp với task
2. `/skill install [tên]` hoặc `npx -y [package]`
3. Nếu task cần Python → delegate Hermes, không cài ở đây

---

## 📹 VIDEO PRODUCTION

Tools để tạo video tự động — content factory của Nobitano.

### HyperFrames — HTML → Video MP4
```bash
# Claude Code skill
npx -y @heygen/hyperframes
# Hoặc ClawHub:
/skill install hyperframes
```
- Viết HTML animation → render thành MP4
- 200k downloads/tháng, không cần biết edit video
- **File kho:** `repos/hyperframes.md` | `skills/hyperframes-skill.md`

### Remotion — Video bằng React/code
```bash
npm create video@latest
# Hoặc trong project:
npm install remotion @remotion/cli
npx remotion studio
```
- Code video như code UI component
- 49.9k stars, 900k installs/tháng
- **File kho:** `repos/remotion.md` | `skills/remotion-skill.md`

### HTML Video — Animate HTML → video
```bash
/skill install html-video
# Hoặc:
npx -y @nexu/html-video
```
- Biến HTML/CSS animation thành video file
- Không cần FFmpeg hay editor
- **File kho:** `repos/html-video.md` | `skills/html-video-skill.md`

### HTML Anything — Render HTML → mọi format
```bash
/skill install html-anything
npx -y @nexu/html-anything
```
- Export HTML → PNG, PDF, MP4, GIF
- **File kho:** `repos/html-anything.md` | `skills/html-anything-skill.md`

### ToonFlow — Script → Animated video
```bash
# Desktop app — download từ GitHub releases
# https://github.com/toonflow/toonflow
```
- 10K+ stars, biến script thành animated short drama
- **File kho:** `repos/toonflow.md`

### AI Shorts Generator Pipeline
```bash
# Stack: Claude Code + Playwright + FFmpeg
# Xem workflow tại:
# repos/ai-shorts-generator-pipeline.md
```
- Pipeline tự động tạo Shorts từ text
- **File kho:** `repos/ai-shorts-generator-pipeline.md`

### MoneyPrinterTurbo Config
```bash
pip install moneyprinterturbo
# Config file tại: skills/moneyprinterturbo-config.md
```
- Auto tạo video kiếm tiền từ keywords
- **File kho:** `skills/moneyprinterturbo-config.md`

---

## 🎨 DESIGN & UI

### Taste Skill — Design taste cho AI
```bash
/skill install taste
npx -y @leonxlnx/taste-skill
```
- Cải thiện aesthetic sense của AI khi design
- 43.3k stars
- **File kho:** `repos/taste-skill.md` | `skills/taste-skill-frontend.md`

### UI/UX Pro Max — Design Director skill
```bash
/skill install ui-ux-pro-max
```
- Biến Claude thành design director
- 94K+ stars reference
- **File kho:** `skills/ui-ux-pro-max.md`

### SC-DataV — 3D Dashboard
```bash
npm install sc-datav
```
- Three.js + Vue3, dashboard màn hình lớn 3D
- **File kho:** `repos/sc-datav.md` | `skills/sc-datav-skill.md`

---

## 🔧 DEVELOPER TOOLS

### Superpowers — Claude Code supercharger
```bash
/skill install superpowers
# Hoặc:
npx -y @obra/superpowers
```
- 150k stars, #1 GitHub Trending
- Bộ skill tổng hợp cho Claude Code
- **File kho:** `repos/superpowers.md` | `skills/superpowers-skill.md`

### Last30Days — Slash commands cho Claude Code
```bash
/skill install last30days
npx -y last30days
```
- 34k stars, `/last30days` command
- **File kho:** `repos/last30days.md` | `skills/last30days-skill.md`

### Continue — AI coding trong VS Code/JetBrains
```bash
# VS Code extension:
code --install-extension Continue.continue
# Config: repos/continue.md
```
- 33.7k stars, alternative Copilot open-source
- **File kho:** `repos/continue.md`

### GStack — Garry Tan's Claude Code setup
```bash
# 25 skills bundle từ CEO Y Combinator
/skill install gstack
```
- Setup Claude Code đã proven của Garry Tan
- **File kho:** `repos/gstack.md` | `skills/gstack.md`

### Matt Pocock Skills — TypeScript mastery
```bash
/skill install mattpocock
npx -y @mattpocock/skills
```
- Cha đẻ Total TypeScript
- **File kho:** `repos/mattpocock-skills.md` | `skills/mattpocock-skills-skill.md`

### Claude Code Skills List — Top 20 skills
```bash
# Reference list — không cài package
# Đọc: skills/claude-code-skills-list-skill.md
```
- Tổng hợp 20 skills tốt nhất cho Claude Code
- **File kho:** `skills/claude-code-skills-list-skill.md`

### Agent Research Skills (Academic)
```bash
npx -y @lingzhi/agent-research-skills
/skill install agent-research
```
- Research skills chuyên academic
- **File kho:** `repos/agent-research-skills-academic.md`

### Plannotator — Plan trước khi code
```bash
/skill install plannotator
npx -y @backnotprop/plannotator
```
- Bắt AI lên plan chi tiết trước khi implement
- **File kho:** `skills/plannotator-skill.md`

### Caveman — Trả lời đơn giản nhất có thể
```bash
/skill install caveman
```
- Bắt AI giải thích như người hang động
- Dùng để simplify complex output
- **File kho:** `skills/caveman.md`

---

## 📊 MARKETING & BUSINESS

### Marketing Skills — 43 marketing skills
```bash
/skill install marketingskills
npx -y @coreyhaines/marketingskills
```
- 31.9k stars, 43 marketing automation skills
- **File kho:** `repos/marketingskills.md` | `skills/marketingskills-skill.md`

### Open SEO — Alternative Semrush/Ahrefs
```bash
npm install open-seo
npx -y open-seo
```
- Open-source SEO tool, Claude integration
- **File kho:** `repos/open-seo.md`

### HubSpot MCP
```bash
npx -y hubspot-mcp
```
- Kết nối Claude với HubSpot CRM
- **File kho:** `mcps/hubspot-mcp.md`

### Make.com MCP
```bash
npx -y makemcp
```
- Trigger Make.com scenarios từ Claude
- **File kho:** `mcps/make-mcp.md`

### AiToEarn — Auto content kiếm tiền
```bash
/skill install aitoearn
# Xem: skills/aitoearn-skill.md
```
- Tự tạo content, tự đăng social, tự kiếm tiền
- **File kho:** `repos/aitoearn.md` | `skills/aitoearn-skill.md`

### Cloud Accounting MCPs
```bash
npx -y cloud-accounting-mcp
```
- Kết nối Claude với phần mềm kế toán cloud VN
- **File kho:** `mcps/cloud-accounting-mcps.md`

### Accounting Skills (Cynco)
```bash
/skill install accounting
npx -y @cynco/skills
```
- Skills kế toán tự động
- **File kho:** `skills/accounting-skills-cynco.md`

### Invoice Extractor
```bash
/skill install invoice-extractor
npx -y @viprasol/invoice-extractor
```
- Extract data từ hóa đơn tự động
- **File kho:** `skills/invoice-extractor.md`

---

## 🤖 AI & AGENTS

### UI-TARS Desktop — Agent TARS (ByteDance)
```bash
# Download desktop app:
# github.com/bytedance/UI-TARS-desktop/releases
```
- Agent duyệt web + computer control
- **File kho:** `repos/ui-tars-desktop.md`

### Page Agent — In-page GUI agent (Alibaba)
```bash
npm install @alibaba/page-agent
```
- Control web interface bằng JS
- **File kho:** `repos/page-agent.md`

### OpenClaw — AI agent platform
```bash
npm install -g openclaw
```
- 210k stars, orchestrator chính của hệ thống
- **File kho:** `repos/openclaw.md`

### Agent Research Skills (Academic)
```bash
/skill install agent-research-academic
```
- Research skills chuyên sâu cho agent
- **File kho:** `repos/agent-research-skills-academic.md` | `skills/agent-research-skills-academic-skill.md`

---

## 🖼️ IMAGE & CREATIVE AI

### ComfyUI MCP
```bash
npx -y comfyui-mcp
```
- Kết nối Claude với ComfyUI (Stable Diffusion)
- Cần ComfyUI đang chạy local port 8188
- **File kho:** `mcps/comfyui-mcp.md`

### Image/Video Gen MCP Guide
```bash
# Stack guide: ComfyUI + Fal + Pollinations
# Đọc: skills/image-video-gen-mcp-guide.md
```
- Hướng dẫn chọn tool gen image/video phù hợp
- **File kho:** `skills/image-video-gen-mcp-guide.md`

---

## 🗓️ PRODUCTIVITY & WORKSPACE

### Google Workspace MCP
```bash
npx -y @evolsb/claude-code-google-workspace
```
- Claude đọc/ghi Google Docs, Sheets, Drive
- **File kho:** `mcps/google-workspace-mcp.md`

### NotebookLM MCP (PleasePrompto)
```bash
npx -y notebooklm-mcp
```
- Kết nối Claude với NotebookLM
- 2.7k stars
- **File kho:** `mcps/notebooklm-mcp-pleaseprompto.md`

### NotebookLM MCP Server (auto-update)
```bash
npx -y notebooklm-mcp-server
```
- Version tự cập nhật của NotebookLM MCP
- **File kho:** `mcps/notebooklm-mcp-server.md`

### Motrix Next — Download manager
```bash
npm install motrix-next
```
- Download manager với AI integration
- **File kho:** `repos/motrix-next.md`

---

## 🔮 NICHE & SPECIAL

### Iztro — Tử Vi Đẩu Số (JS/TS)
```bash
npm install iztro
```
- Thư viện tính lá số Tử Vi, output JSON
- **File kho:** `repos/iztro.md`

### Bazi/Ziwei Skill
```bash
/skill install bazi-ziwei
```
- Luận Bát Tự + Tử Vi cho Claude
- **File kho:** `skills/bazi-ziwei-skill.md`

### RuView — WiFi sensing
```bash
npm install ruview
```
- Detect người qua WiFi signal
- **File kho:** `repos/ruview.md`

---

## 📋 Quick Reference — Cài nhiều tools cùng lúc

### Content Factory Stack (video production)
```bash
npx -y @heygen/hyperframes
npm create video@latest        # Remotion
npx -y @nexu/html-video
npx -y @nexu/html-anything
```

### Developer Productivity Stack
```bash
npx -y @obra/superpowers
npx -y last30days
/skill install mattpocock
/skill install gstack
```

### Marketing Stack
```bash
npx -y @coreyhaines/marketingskills
npx -y open-seo
npx -y hubspot-mcp
npx -y makemcp
```

### AI Agent Stack
```bash
npm install -g openclaw
npm install @alibaba/page-agent
npx -y @lingzhi/agent-research-skills
```

---

## Lưu ý quan trọng

- **npm-only tools = mày (OpenClaw) cài và dùng** — không delegate Hermes
- **Nếu tool cần Python sau khi cài** → delegate Hermes xử lý logic
- **Nếu tool cần Docker/VPS** → báo Antigravity deploy trước
- **File .md đầy đủ** của từng tool ở đường dẫn ghi trong "File kho:" — fetch khi cần chi tiết
