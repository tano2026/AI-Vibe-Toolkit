# Bộ Tứ AI Ecosystem — Hướng Dẫn Phối Hợp

**4 tools:** Claude + Hermes + OpenClaw + Antigravity
**Mục đích:** Content creator + Vibe coder + Digital marketer
**Cập nhật:** tháng 6/2026

---

## Vai Trò Từng Tool

```
┌─────────────────────────────────────────────┐
│                  MÀY                        │
│  (quyết định, review, approve)              │
└──────────┬──────────────────────────────────┘
           │
    ┌──────▼──────┐
    │   CLAUDE    │ ← Brainstorm, spec, writing, quick chat
    └──────┬──────┘
           │ tasks phức tạp
    ┌──────▼──────┐
    │   HERMES    │ ← Execute, research, tích lũy skills
    └──────┬──────┘
           │ gateway
    ┌──────▼──────┐
    │  OPENCLAW   │ ← Telegram/WhatsApp interface, 24/7
    └─────────────┘

    ┌─────────────┐
    │ ANTIGRAVITY │ ← Cài đặt + Deploy + Maintain tất cả
    └─────────────┘
```

---

## Workflow Theo Tình Huống

### Tình Huống 1: Thấy Tool Hay Trên TikTok

```
Mày chụp ảnh/copy link
→ Gửi Telegram: "thêm repo github.com/..."
→ OpenClaw nhận
→ Giao Hermes: research + push kho
→ Hermes làm xong
→ OpenClaw báo Telegram: "Script #52 ready, repo #42 added"
→ Mày quay video khi rảnh

Thời gian mày bỏ ra: 30 giây
```

### Tình Huống 2: Build App Mới

```
Mày có idea
→ Claude (web): brainstorm → spec trong 10 phút
→ Mở Claude Code
→ Antigravity đã cài sẵn: agent-skills + superpowers + taste-skill
→ /spec → /plan → approve → /build auto
→ Hermes track progress
→ Antigravity deploy lên Vercel
→ App live

Mày chỉ cần: idea + review + approve
```

### Tình Huống 3: Sáng Dậy Check Business

```
07:00 — OpenClaw đã gửi Telegram:
  📊 ROAS hôm qua: Campaign A 3.2x ✅, Campaign B 1.4x ⚠️
  🔍 GitHub trending: 3 repos AI mới đáng xem
  📅 Lịch hôm nay: 2 meetings, cần prep

Mày review → reply:
  "pause Campaign B"
  "thêm repo X"
  → OpenClaw + Hermes tự xử

Thời gian: 5 phút
```

### Tình Huống 4: Làm Content Hàng Loạt

```
Mày có 3 tools muốn làm video
→ Hermes: delegate_task x3 song song
  - Task 1: research tool A + viết script
  - Task 2: research tool B + viết script
  - Task 3: research tool C + viết script
→ 3 scripts xong cùng lúc
→ Mày quay 3 video

Thời gian research + viết: 15 phút (thay vì 45 phút tuần tự)
```

---

## Daily Routine Với Bộ Tứ

### Sáng (5 phút)
```
07:00 — Telegram: Morning brief từ OpenClaw
        - ROAS check
        - Trending repos
        - Lịch hôm nay
07:05 — Mày review, reply lệnh nếu cần
```

### Ban ngày
```
Khi thấy tool hay → Telegram OpenClaw → tự động vào kho
Khi cần code → Claude Code với skills đã cài
Khi cần research sâu → Hermes /goal
```

### Tối (10 phút)
```
Review những gì Hermes đã làm trong ngày
Check kho có script mới nào ready để quay
Plan content tuần tới nếu cần
```

### Tự Động (không cần làm gì)
```
02:00 — Claude Routines: SEO audit
07:00 — OpenClaw: Morning brief
08:00 — OpenClaw: ROAS check
16:00 thứ 6 — OpenClaw: Content calendar tuần tới
```

---

## Setup Checklist — Làm 1 Lần

```bash
# Bước 1: Cài Antigravity
npm install -g antigravity

# Bước 2: Cài ecosystem
agy install hermes-agent
agy install openclaw

# Bước 3: Config Hermes
cp configs/hermes-USER.md ~/.hermes/USER.md
cp configs/hermes-MEMORY.md ~/.hermes/MEMORY.md
# Chỉnh [PLACEHOLDER] trong USER.md

# Bước 4: Config OpenClaw
# Tạo Telegram bot (@BotFather)
openclaw connect telegram --token BOT_TOKEN
# Copy workflows từ configs/openclaw-config.md
# Paste vào terminal từng workflow

# Bước 5: Cài plugins Claude Code
agy plugin install addyosmani/agent-skills
agy plugin install obra/superpowers
agy plugin install Leonxlnx/taste-skill
agy plugin install coreyhaines31/marketingskills
agy plugin install AgriciDaniel/claude-seo
agy plugin install AgriciDaniel/claude-ads

# Bước 6: Setup Claude Routines
# Vào claude.ai/code/routines
# Copy templates từ skills/claude-routines-templates.md
# Setup 3 routines: morning brief, ROAS check, SEO audit

# Bước 7: Setup CLAUDE.md cho projects
# Copy configs/CLAUDE-md-vibe-coder.md vào mỗi project mới

# Verify
agy status
openclaw status
hermes status
```

---

## Files Trong /configs/ Folder

| File | Dùng cho |
|------|---------|
| `hermes-USER.md` | Copy → `~/.hermes/USER.md` |
| `hermes-MEMORY.md` | Copy → `~/.hermes/MEMORY.md` |
| `openclaw-config.md` | Reference khi setup workflows |
| `antigravity-setup.md` | Guide cài ecosystem đầy đủ |
| `CLAUDE-md-vibe-coder.md` | Copy → `CLAUDE.md` mỗi project mới |
| `ecosystem-guide.md` | File này — bản đồ phối hợp |

---

## Nguyên Tắc Cốt Lõi

**Claude = Think** — Brainstorm, spec, review chất lượng
**Hermes = Do** — Execute, research, tích lũy skills theo thời gian
**OpenClaw = Connect** — Interface với thế giới bên ngoài (Telegram, apps)
**Antigravity = Maintain** — Cài đặt, update, deploy

Mày chỉ cần:
1. **Quyết định** — Claude giúp think
2. **Giao lệnh** — Telegram hoặc terminal
3. **Review kết quả** — approve hoặc reject
4. **Enjoy** — bộ tứ tự xử phần còn lại
