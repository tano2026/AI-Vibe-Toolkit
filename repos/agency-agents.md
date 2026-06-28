# agency-agents — GitHub Repo

## TL;DR
232 AI agent chuyen biet to chuc thanh 16 phong ban — Engineering, Marketing, Sales, Design, Paid Media, QA, Customer Support... Cai 1 lenh vao Claude Code, Cursor, OpenClaw, Antigravity. 117K stars, 19K forks, dang tang cuc nhanh. Repo trending nong nhat 2 tuan qua.

## Repo nay dung de lam gi
Thay vi dung 1 AI lam tat ca (viet code cung Claude, marketing cung Claude, SEO cung Claude) — agency-agents cung cap doi ngu AI chuyen mon hoa nhu mot cong ty that:

**12+ phong ban, 232 agents (va dang tang):**
- Engineering: Frontend Dev, Backend Architect, AI Engineer, DevOps, Mobile Builder, Rapid Prototyper
- Marketing: TikTok Strategist, Content Creator, Growth Hacker, Xiaohongshu Specialist, Twitter Engager
- Sales: Outbound Strategist, Deal Strategist, Pipeline Analyst, Sales Coach
- Paid Media: PPC Campaign Strategist, Ad Creative Strategist, Tracking Specialist
- Design: UI Designer, Brand Guardian, Image Prompt Engineer, Whimsy Injector
- QA, Customer Support, Product, Legal, Finance, Spatial Computing, Game Dev...

Moi agent co: vai tro rieng, quy trinh lam viec rieng, tieu chi danh gia rieng, biet phoi hop voi agent khac.

## Setup tung buoc

**Claude Code (cach nhanh nhat):**
```bash
# Clone repo
git clone https://github.com/msitarzewski/agency-agents
cd agency-agents

# Cai tat ca agents
./scripts/install.sh --tool claude-code
# -> Copy het vao ~/.claude/agents/

# Hoac chi cai 1 phong ban
cp marketing/*.md ~/.claude/agents/

# Dung trong Claude Code session
# "Activate TikTok Strategist and help me plan content for next week"
# "Use Growth Hacker to analyze our acquisition funnel"
```

**OpenClaw (Hermes ecosystem):**
```bash
# Script rieng cho OpenClaw
./scripts/install.sh --tool openclaw
# -> Moi agent tro thanh workspace voi SOUL.md, AGENTS.md, IDENTITY.md
# -> Tu dong register neu openclaw CLI co san
```

**Cursor:**
```bash
./scripts/install.sh --tool cursor
# -> Agent compile thanh .cursorrules
# Dung: "@tiktok-strategist review this content calendar"
```

**Antigravity / Gemini CLI / OpenCode / Aider / Windsurf:**
```bash
./scripts/convert.sh --tool [ten-tool]
./scripts/install.sh --tool [ten-tool]
```

## Agents hay dung nhat cho moi nguoi (chon nhanh)

**Content Creator (Tano/AI Vibe Toolkit):**
- TikTok Strategist: Viral content, algorithm optimization
- Content Creator: Multi-platform content, editorial calendars
- Growth Hacker: User acquisition, viral loops
- Instagram Curator: Visual storytelling, community building

**ABTRIP (Travel brand):**
- Social Media Strategist: Cross-platform campaigns
- Xiaohongshu Specialist: Lifestyle content, trend-driven (theo doi XHS truoc TikTok VN)
- Offer & Lead Gen Strategist: Tour package offers, lead magnets

**Wonder Mart (E-commerce):**
- PPC Campaign Strategist: Google/Facebook Ads optimization
- App Store Optimizer: ASO, discoverability
- Paid Social Strategist: Meta, TikTok ads

**Hermes/OpenClaw agent ecosystem:**
- AI Engineer: ML models, AI integration
- Backend Architect: API design, scalability
- DevOps Automator: CI/CD, cloud ops
- Autonomous Optimization Architect: LLM routing, cost optimization

## Vi du thuc te
**Build content calendar cho ABTRIP bang 3 agents phoi hop:**

```
# Session 1 - Research
"Activate Xiaohongshu Specialist. Analyze top travel content trends on XHS this week."

# Session 2 - Strategy
"Activate TikTok Strategist. Based on these XHS trends, create a 2-week TikTok content calendar for ABTRIP targeting Gen Z travelers."

# Session 3 - Copy
"Activate Content Creator. Write 5 TikTok scripts from this calendar, hook-first format, ElevenLabs-ready."
```

3 agent, 3 session, ra noi dung chuan chuyen gia. Khac voi nhoi tat ca vao 1 prompt dai.

## Luu y / Loi thuong gap
- 232 agents = overwhelming neu cai het — chon 10-15 agent relevant nhat, khong cai ca bo
- Agent md file chi la system prompt — chat luong output van phu thuoc vao model dang dung
- Community dang contribute them lien tuc — pull moi tuan de co agent moi
- Mot so agent chuyen cho startup US (Reddit Builder, App Store Optimizer) — can adapt cho thi truong VN
- OpenClaw integration la cai dac biet trong repo nay — hiem repo nao ho tro OpenClaw officially

## Danh gia ca nhan
- Diem manh: 117K stars = community lon, nhieu nguoi dang dung va contribute; setup 1 lenh; ho tro moi tool coding; MIT license; OpenClaw integration chinh thuc
- Diem yeu: 232 agents co the qua nhieu, gay confusion khi chon; chat luong agent khong dong deu (community contribute); mot so agent qua specific cho context US/global
- Co nen dung khong: **9.5/10** — Must-install ngay cho bat ky ai dung Claude Code. Day la setup nhanh nhat de co doi ngu AI chuyen mon. Chon 10-15 agent phu hop, bo sung vao Claude Code/OpenClaw, dung ngay.

## Agent dac biet cho he sinh thai cua tao
Repo nay co **OpenClaw integration chinh thuc** — hiem gap. Script tu dong tao workspace cho tung agent trong OpenClaw. Khi Hermes nhan task, OpenClaw co the route sang dung agent chuyen mon thay vi dung 1 general LLM.

## Link
- Repo: https://github.com/msitarzewski/agency-agents
- Stars: 117,465 (tinh den 29/6/2026)
- License: MIT
- Topics: claude-code, cursor, ai-agents, multi-agent, openclaw
