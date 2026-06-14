# agency-agents — 220 AI Agents Theo 17 Phòng Ban, Cài 1 Lệnh (113k⭐)

**GitHub:** https://github.com/msitarzewski/agency-agents
**Stars:** 113k⭐ | **Forks:** 18.4k | **License:** MIT
**Tác giả:** msitarzewski + 87 contributors | **Tạo:** 10/2025
**Active:** update hàng ngày, commit 5 ngày trước

---

## Đây Là Gì

"Văn phòng AI hoàn chỉnh trong 1 cú click" — 220 AI agents được thiết kế như nhân viên chuyên nghiệp thật: có personality, workflow riêng, deliverables cụ thể.

**Không phải generic prompt.** Mỗi agent:
- Personality riêng (voice, communication style)
- Workflow cụ thể (processes, steps)
- Deliverables đo được (real code, reports, outcomes)
- Battle-tested qua community 87 contributors

---

## 17 Phòng Ban — 220 Agents

| Division | Agents | Highlights |
|----------|--------|-----------|
| **Engineering** | 33 | Frontend Dev, Backend Architect, AI Engineer, DevOps, Code Reviewer, SRE, Prompt Engineer... |
| **Marketing** | 36 | Content Strategist, SEO Specialist, Social Media Manager, Email Marketer, Reddit Ninja... |
| **Specialized** | 53 | Whimsy Injector, Reality Checker, và nhiều role cực kỳ niche |
| **GIS** | 13 | Spatial Data Analyst, Map Design Specialist, GIS Developer... |
| **Security** | 10 | Penetration Tester, Security Auditor, Threat Modeler... |
| **Sales** | 9 | Lead Gen Specialist, SDR, Account Executive, Closer... |
| **Design** | 9 | UI/UX Designer, Brand Identity, Persona Specialist... |
| **Testing** | 8 | QA Engineer, Performance Tester, Accessibility Auditor... |
| **Project Mgmt** | 7 | Scrum Master, Meeting Notes Specialist, Risk Manager... |
| **Paid Media** | 7 | Google Ads, Meta Ads, Performance Marketer... |
| **Support** | 6 | Customer Success, Technical Support, Escalation Manager... |
| **Spatial Computing** | 6 | AR/VR Developer, Spatial UI Designer... |
| **Finance** | 5 | Financial Analyst, Budget Planner, CFO Assistant... |
| **Product** | 5 | Product Manager, User Researcher, Roadmap Planner... |
| **Game Development** | 5 | Game Designer, Level Designer, Narrative Writer... |
| **Academic** | 5 | Research Assistant, Literature Reviewer, Thesis Writer... |
| **Strategy** | 3 | Business Strategist, Competitive Analyst, OKR Coach |

---

## Cài Đặt

```bash
git clone https://github.com/msitarzewski/agency-agents
cd agency-agents

# Option 1: Claude Code (recommended)
./scripts/install.sh --tool claude-code

# Option 2: Chọn division cụ thể
./scripts/install.sh --tool claude-code --division engineering,security

# Option 3: Chọn agent cụ thể
./scripts/install.sh --tool cursor --agent frontend-developer,ui-designer

# Option 4: Tool khác
./scripts/install.sh --tool cursor
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool windsurf
./scripts/install.sh --tool codex

# Xem danh sách teams
./scripts/install.sh --list teams

# Dry run trước
./scripts/install.sh --tool claude-code --division engineering --dry-run
```

---

## Cách Activate Agent

```bash
# Trong Claude Code sau khi cài
"Activate Frontend Developer mode và help me build a React dashboard"
"Switch to Security Auditor và review this authentication code"
"Activate Content Strategist và create a content plan for my SaaS"
"Use Reddit Community Ninja và draft a post about this tool"
```

---

## Agents Hay Nhất Theo Use Case

### Cho Vibe Coders
- 🎨 **Frontend Developer** — React/Vue, pixel-perfect UI
- ⚡ **Rapid Prototyper** — POC nhanh, MVP trong 1 ngày
- 🔧 **Minimal Change Engineer** — Fix exactly what's asked, no scope creep
- 🧭 **Codebase Onboarding Engineer** — Hiểu repo mới nhanh
- 🧬 **Prompt Engineer** — Tối ưu prompts cho AI tasks

### Cho Content & Marketing
- 📝 **Content Strategist** — Full content strategy
- 🎯 **SEO Specialist** — Technical + on-page SEO
- 🎭 **Reddit Community Ninja** — Reddit posts không bị spam
- 💌 **Email Marketer** — Email sequence, nurture flows
- ✨ **Whimsy Injector** — Add personality vào content khô khan

### Cho Business
- 💰 **Lead Generation Specialist** — Outbound prospecting
- 📊 **Financial Analyst** — P&L, forecasting, unit economics
- 🎯 **Product Manager** — PRD, roadmap, prioritization
- 🛡️ **Security Auditor** — Code + infra security review
- 📋 **Meeting Notes Specialist** — Transform raw notes → action items

---

## Format Agent File

Mỗi agent là 1 file `.md` với structure:
```yaml
---
name: Agent Name
description: What this agent does
color: cyan
emoji: 🎯
vibe: One-line personality
---

# Agent Personality
[Identity, expertise, communication style]

# Core Mission
[What this agent delivers]

# Workflow
[Step-by-step process]

# Deliverables
[Concrete outputs with examples]

# Success Metrics
[How to know if it worked]
```

---

## Đánh Giá Cá Nhân

113k stars, 18.4k forks, 87 contributors, active đến hôm nay — đây là community project lớn nhất trong category AI agents-as-personas.

Điểm tao thấy thực dụng nhất: **Minimal Change Engineer** ("fix only what's asked") và **Whimsy Injector** ("add personality"). Hai cái này giải quyết 2 vấn đề phổ biến nhất với AI coding/content.

Điểm đặc biệt: **220 agents** nhưng mỗi cái đều có personality thật, không phải template copy-paste. Marketing division có 36 agents — từ Google Ads đến Reddit Ninja — đủ cover mọi channel.

**Rating: 9/10** — Install engineering + marketing + security là cover 80% daily tasks.

---
*Nguồn: github.com/msitarzewski/agency-agents*
*Stars: 113k⭐ (tháng 6/2026) | MIT | 220 agents | 17 divisions*
*Cập nhật: tháng 6/2026*
