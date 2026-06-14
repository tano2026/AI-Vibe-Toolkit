# agency-agents — Skill Dùng Ngay (113k⭐)

**Repo:** github.com/msitarzewski/agency-agents | MIT
**220 agents | 17 divisions | 87 contributors**

---

## Cài Nhanh

```bash
git clone https://github.com/msitarzewski/agency-agents
cd agency-agents

# Cài cho Claude Code
./scripts/install.sh --tool claude-code

# Hoặc chỉ những division mày cần
./scripts/install.sh --tool claude-code --division engineering,marketing,security
```

---

## Activate Agents — Syntax

```bash
# Trong Claude Code sau khi cài
"Activate [Agent Name] và [task]"

# Ví dụ:
"Activate Frontend Developer và build a dashboard component with dark mode"
"Activate Content Strategist và create 30-day content plan for AI tool"
"Activate Security Auditor và review this login code for vulnerabilities"
"Activate Rapid Prototyper và build MVP for this feature in 2 hours"
"Activate Reddit Community Ninja và write a post about agency-agents"
"Activate Minimal Change Engineer và fix only the bug on line 47"
"Activate Prompt Engineer và optimize this system prompt"
```

---

## Quick Reference — Agent Theo Situation

### 🔨 Đang Code
| Situation | Agent |
|-----------|-------|
| Build UI component | Frontend Developer |
| Design API | Backend Architect |
| Fix bug nhanh | Minimal Change Engineer |
| Review PR | Code Reviewer |
| Tìm hiểu repo mới | Codebase Onboarding Engineer |
| Build MVP nhanh | Rapid Prototyper |
| Deploy / CI-CD | DevOps Automator |
| Security review | Security Auditor |
| Optimize prompts | Prompt Engineer |
| Multi-agent system | Multi-Agent Systems Architect |

### 📣 Đang Làm Marketing/Content
| Situation | Agent |
|-----------|-------|
| Content strategy | Content Strategist |
| SEO audit | SEO Specialist |
| Email sequence | Email Marketer |
| Social media | Social Media Manager |
| Reddit post | Reddit Community Ninja |
| Google Ads | Google Ads Specialist |
| Thêm personality vào content | Whimsy Injector |
| Fact-check content | Reality Checker |

### 💼 Đang Làm Business
| Situation | Agent |
|-----------|-------|
| Tìm leads | Lead Generation Specialist |
| Financial model | Financial Analyst |
| Product roadmap | Product Manager |
| Meeting summary | Meeting Notes Specialist |
| Business strategy | Business Strategist |
| Competitive analysis | Competitive Analyst |

### 🎮 Đặc Biệt
| Situation | Agent |
|-----------|-------|
| Build game | Game Designer |
| AR/VR feature | Spatial Computing Developer |
| Map/GIS data | GIS Developer |
| Academic research | Research Assistant |
| Smart contract | Solidity Engineer |

---

## Copy Agent Thủ Công (Không Cài Script)

```bash
# Clone repo
git clone https://github.com/msitarzewski/agency-agents

# Copy agent cụ thể vào Claude Code
cp agency-agents/engineering/engineering-frontend-developer.md    ~/.claude/agents/

cp agency-agents/marketing/marketing-content-strategist.md    ~/.claude/agents/

# Hoặc paste content vào đầu conversation
cat agency-agents/engineering/engineering-minimal-change-engineer.md
# → copy toàn bộ → paste vào Claude
```

---

## Top 10 Agents Cho AI Vibe Toolkit

```bash
# 1. Content Strategist — lên kế hoạch content 30 ngày
"Activate Content Strategist và create monthly content calendar for AI tools channel"

# 2. Frontend Developer — build components cho demo
"Activate Frontend Developer và create a dark-theme dashboard for AI metrics"

# 3. Reddit Community Ninja — promote tools lên Reddit
"Activate Reddit Community Ninja và write authentic post about hermes-agent for r/MachineLearning"

# 4. SEO Specialist — optimize channel/site
"Activate SEO Specialist và audit my YouTube channel for SEO improvements"

# 5. Rapid Prototyper — build demo nhanh
"Activate Rapid Prototyper và build a 2-hour MVP: web app showing GitHub trending AI repos"

# 6. Minimal Change Engineer — fix bugs chính xác
"Activate Minimal Change Engineer và fix only the TRACKER.md update bug, nothing else"

# 7. Prompt Engineer — optimize skills trong kho
"Activate Prompt Engineer và optimize the research-agent.md skill for better outputs"

# 8. Whimsy Injector — thêm personality vào script video
"Activate Whimsy Injector và make this dry script more engaging without losing information"

# 9. Meeting Notes Specialist — tóm tắt session làm việc
"Activate Meeting Notes Specialist và summarize this conversation into action items"

# 10. Reality Checker — verify claims trong .md files
"Activate Reality Checker và fact-check the statistics in this hermes-agent.md"
```

---

## Kết Hợp Với Workflow Kho

```
Quẳng link tool mới
→ "Activate Codebase Onboarding Engineer và summarize this repo in 5 bullets"
→ "Activate Content Strategist và turn this into a TikTok script"
→ "Activate Whimsy Injector và make the hook more punchy"
→ Push lên kho
```

---
*skills/agency-agents-skill.md | AI Vibe Toolkit | tháng 6/2026*
