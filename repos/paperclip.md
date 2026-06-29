# Paperclip — GitHub Repo

## TL;DR
Platform quan ly doi AI agent cho doanh nghiep — mo nguon mo, 72K stars. Neu OpenClaw la "nhan vien AI", Paperclip la "cong ty" quan ly nhung nhan vien do. Dat muc tieu kinh doanh → thue doi agent → duyet ngan sach → agent tu chay. OpenClaw integration chinh thuc.

## Repo nay dung de lam gi
Cac AI agent tool hien tai (Claude Code, OpenClaw, Cursor) cho phep mot agent lam viec. Nhung khi can ca doi agent phoi hop — ai giao viec, ai theo doi tien do, ai kiem soat chi phi? Paperclip giai quyet:

**Mo hinh:**
```
Muc tieu: "Build #1 AI note-taking app len $1M MRR"
    ↓
Paperclip tao doi:
- CEO agent: chien luoc, quyet dinh
- CTO agent: kien truc, technical decisions
- Engineer agents: code
- Designer agent: UI/UX
- Marketing agent: content, growth
    ↓
Mày duyet ke hoach + ngan sach → Hit Go
    ↓
Dashboard: xem tung agent dang lam gi, chi phi bao nhieu
```

**Tinh nang chinh:**
- **Org chart:** Ve so do to chuc cho doi agent nhu cong ty that
- **Goal alignment:** Muc tieu lon → breakdown thanh task cho tung agent
- **Budget control:** Dat ngan sach tung agent, khong bi chay qua
- **Governance:** Duyet quyet dinh truoc khi agent lam — tranh sai sot lon
- **Dashboard:** Theo doi toan bo doi real-time
- **Multi-provider:** Moi agent co the dung LLM khac nhau (Claude, GPT, Gemini)

**Trong ảnh thấy:**
- 505 branches, 655 tags — development rat active
- Folder structure: agents/skills, claude/skills, cli, doc, docker, evals, packages, scripts, server
- OpenClaw duoc list dau tien trong danh sach "Works with"

## Setup tung buoc

```bash
# Yeu cau: Node.js 22+, Docker

# Clone
git clone https://github.com/paperclipai/paperclip
cd paperclip

# Cai dependencies
npm install

# Config
cp .env.example .env
# Edit .env: them API keys (Anthropic, OpenAI, Gemini...)

# Chay voi Docker (khuyen nghi)
docker compose up -d

# Hoac chay thu cong
npm run dev

# Truy cap: http://localhost:3000
```

**Ket noi OpenClaw:**
```bash
# Trong Paperclip dashboard:
# Settings → Agents → Add Agent → chon OpenClaw
# Nhap OpenClaw endpoint cua may
# → Paperclip giao viec cho OpenClaw tu dong
```

**Tao cong ty AI dau tien:**
```
1. Dashboard → New Company
2. Dat muc tieu: "Xay dung content factory AI cho ABTRIP"
3. Hire agents: CEO (Claude), Marketing Lead (GPT-4o), Content Writer (Gemini)
4. Set budget: $50/thang tong the
5. Review ke hoach → Approve → chay
6. Theo doi tung agent tren dashboard
```

## Vi du thuc te

**Dung Paperclip quan ly ABTRIP AI company:**

```
Company: ABTRIP Digital
Goal: "Tang 300% booking online trong 6 thang"

Doi agent:
- CEO (Claude Sonnet): Quyet dinh chien luoc, duyet ngan sach
- Marketing Director (GPT-4o): Campaign planning, KPI tracking
- Content Creator (Gemini Flash): Viet bai, script TikTok
- SEO Specialist (DeepSeek): Keyword research, on-page
- Ads Manager (Claude Haiku): Google/Meta ads optimization

Budget: $100/thang cho LLM API
Governance: Duyet truoc moi campaign > $500

→ Mày ngoi quan sat tren dashboard
→ Agent tu chay, bao cao hang ngay
→ Chi can duyet quyet dinh lon
```

## So sanh voi agency-agents

| | Paperclip | agency-agents |
|---|---|---|
| **La gi** | Platform quan ly doi agent | Bo skill files cho 1 agent |
| **Scope** | Nhieu agent phoi hop | 1 agent chuyen mon |
| **UI** | Co dashboard dep | CLI/file-based |
| **Budget control** | Co built-in | Khong |
| **Self-host** | Co (Docker) | Co (file copy) |
| **OpenClaw** | Integration chinh thuc | Installation script |
| **Dung khi** | Quan ly ca cong ty AI | Nang cap 1 agent cu the |

**Ket hop tot nhat:** agency-agents cung cap skill cho tung agent → Paperclip quan ly toan bo doi → OpenClaw/Hermes thuc thi task.

## Luu y / Loi thuong gap
- Can Node.js 22+ — check truoc khi cai
- Docker khuyen nghi cho production — khong nen chay thu cong tren VPS
- Budget control quan trong — dat gioi han truoc khi cho agent tu chay
- Governance layer can thiet — mot so quyet dinh agent co the sai, can duyet thu cong
- Con moi (72K stars trong thoi gian ngan) — mot so tinh nang con beta
- Multi-agent tieu ton nhieu token hon single agent — can tinh ngan sach ky

## Danh gia ca nhan
- Diem manh: Concept dung — quan ly doi agent nhu cong ty that; OpenClaw integration chinh thuc; dashboard dep; budget control built-in; MIT license; TypeScript clean
- Diem yeu: Con moi, ecosystem chua on dinh; setup phuc tap hon agency-agents; can Docker; chi phi LLM tang nhanh khi nhieu agent chay cung luc
- Co nen dung khong: **8.5/10** — Day la buoc tiep theo sau khi may da co Hermes + OpenClaw chay on. Paperclip la lop quan ly phia tren — giao muc tieu lon, de doi agent tu xu ly. Deploy khi san sang scale.

## Vi tri trong he sinh thai cua tao

```
Nobitano (muc tieu kinh doanh)
    ↓
Paperclip (quan ly doi, ngan sach, governance)
    ↓
OpenClaw (orchestrator, nhan task tu Paperclip)
    ↓
Hermes (thuc thi Python task)
    ↓
agency-agents skills (chuyen mon hoa tung task)
    ↓
OmniRoute (1.6B token mien phi)
```

Day la full stack AI company cua mày.

## Link
- Repo: https://github.com/paperclipai/paperclip
- Website: https://paperclip.ing
- Docs: https://paperclip.ing/docs
- Discord: discord.gg/m4HZY7xNG3
- License: MIT
- Language: TypeScript, Node.js 22+
