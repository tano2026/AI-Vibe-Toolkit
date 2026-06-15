# OpenClaw — Đưa Toàn Bộ Kho AI Vibe Toolkit Vào

**Mục tiêu:** Nhắn Telegram → OpenClaw dùng được mọi skill, MCP, config trong kho
**Cập nhật:** tháng 6/2026

---

## Bước 1: Cài OpenClaw

```bash
# Cài OpenClaw
npm install -g openclaw
# hoặc
pnpm add -g openclaw
# hoặc
bun add -g openclaw

# Setup guided
openclaw onboard
```

---

## Bước 2: Kết Nối Kênh (Telegram recommended)

```bash
# Telegram
openclaw channels add telegram
# → Làm theo hướng dẫn: tạo bot @BotFather → paste token

# WhatsApp (alternative)
openclaw channels add whatsapp

# Kiểm tra
openclaw channels list
```

---

## Bước 3: Cài ClawHub CLI (skill manager)

```bash
npm install -g clawhub
clawhub login  # đăng ký tại clawhub.com
clawhub whoami
```

---

## Bước 4: Cài Skills Từ ClawHub

```bash
# Skills chính từ community
clawhub install coding-agent      # delegate coding tasks
clawhub install github            # GitHub operations
clawhub install clawhub           # manage skills
clawhub install canvas            # visual canvas
clawhub install diagram-maker     # tạo diagrams

# Update tất cả
clawhub update --all
clawhub list
```

---

## Bước 5: Load Skills Từ Kho AI Vibe Toolkit

**Cách 1: Clone kho vào thư mục skills OpenClaw**

```bash
# Tìm skills directory của OpenClaw
openclaw config get skills.dir
# Thường là: ~/.openclaw/skills/ hoặc ~/Library/Application Support/OpenClaw/skills/

# Clone kho vào đó
cd ~/.openclaw/skills/
git clone https://github.com/tano2026/AI-Vibe-Toolkit ./ai-vibe-toolkit
# → Tất cả skills trong kho được load

# Sync khi có update
cd ~/.openclaw/skills/ai-vibe-toolkit
git pull
```

**Cách 2: Symlink từng folder skills**

```bash
OPENCLAW_SKILLS=$(openclaw config get skills.dir)

# Link toàn bộ skills ECC (262 files)
ln -s ~/AI-Vibe-Toolkit/skills/ecc $OPENCLAW_SKILLS/ecc

# Link agent-skills (Addy Osmani)
ln -s ~/AI-Vibe-Toolkit/skills/agent-skills $OPENCLAW_SKILLS/agent-skills

# Link taste-skill
ln -s ~/AI-Vibe-Toolkit/skills/taste-skill $OPENCLAW_SKILLS/taste-skill

# Link affiliate skills
ln -s ~/AI-Vibe-Toolkit/skills/affiliate-skills $OPENCLAW_SKILLS/affiliate-skills

# Link viral hooks
ln -s ~/AI-Vibe-Toolkit/skills/viral-hooks $OPENCLAW_SKILLS/viral-hooks

# Verify
openclaw skills list
```

**Cách 3: Copy skills cần dùng**

```bash
OPENCLAW_SKILLS=$(openclaw config get skills.dir)

# Copy skills quan trọng nhất
cp -r ~/AI-Vibe-Toolkit/skills/ecc/content-engine.md $OPENCLAW_SKILLS/
cp -r ~/AI-Vibe-Toolkit/skills/ecc/deep-research.md $OPENCLAW_SKILLS/
cp -r ~/AI-Vibe-Toolkit/skills/ecc/social-publisher.md $OPENCLAW_SKILLS/
cp -r ~/AI-Vibe-Toolkit/skills/viral-hooks/SKILL.md $OPENCLAW_SKILLS/viral-hooks.md
```

---

## Bước 6: Config MCP Servers

```bash
# Xem MCP config template từ ECC
cat ~/.openclaw/skills/ai-vibe-toolkit/skills/ecc/mcp-servers.json

# Copy vào OpenClaw MCP config
openclaw mcp add --config ~/.openclaw/skills/ai-vibe-toolkit/skills/ecc/mcp-servers.json

# Hoặc add từng MCP
openclaw mcp add context7 --url https://mcp.context7.com
openclaw mcp add brave-search --command "npx @anthropic-ai/mcp-server-brave-search"
openclaw mcp add firecrawl --command "npx @mendable/firecrawl-mcp-server"

# Verify
openclaw mcp list
```

---

## Bước 7: Setup USER Context (Hermes-style)

```bash
# Tạo workspace context cho OpenClaw
cat > ~/.openclaw/context.md << 'EOF'
## Identity
Tôi làm content creator AI + vibe coder + digital marketer. Tiếng Việt, casual.

## Kho AI Vibe Toolkit
- GitHub: https://github.com/tano2026/AI-Vibe-Toolkit
- 49 repos, 34 MCPs, 406 skills, 59 scripts

## Workflow khi nhận tool mới
1. Fetch GitHub API + README
2. Viết /repos/tên.md
3. Viết /content/script-video-XX.md
4. Push lên kho + update TRACKER.md

## Content: TikTok + YouTube Shorts, tiếng Việt, vibe coders
EOF

openclaw context set --file ~/.openclaw/context.md
```

---

## Bước 8: Tạo Workflows Qua Telegram

Sau khi setup xong, nhắn bot Telegram:

```
"thêm repo github.com/owner/tool"
→ OpenClaw fetch + research + push kho tự động

"viết script video về hermes-agent"
→ Dùng viral-hooks skill + content từ kho

"check ROAS ads hôm nay"
→ OpenClaw query Meta Ads MCP + báo kết quả

"kho có gì mới tuần này"
→ Fetch TRACKER.md + tóm tắt
```

---

## Bước 9: Scheduled Tasks

```bash
# Morning brief 7h
openclaw schedule add "morning-brief" \
  --cron "0 7 * * *" \
  --prompt "Fetch GitHub trending AI repos hôm nay, filter chưa có trong kho tano2026/AI-Vibe-Toolkit, gửi list về Telegram"

# ROAS check 8h
openclaw schedule add "roas-check" \
  --cron "0 8 * * *" \
  --prompt "Check ROAS Meta Ads hôm qua, flag campaigns < 2x ROAS, send Telegram"

# Content calendar thứ 6
openclaw schedule add "content-calendar" \
  --cron "0 16 * * 5" \
  --prompt "List scripts chưa quay từ kho, tạo content calendar tuần tới, send Telegram"
```

---

## Verify Toàn Bộ

```bash
openclaw status          # overall health
openclaw skills list     # skills đã load
openclaw mcp list        # MCPs đã connect
openclaw channels list   # kênh đang dùng
openclaw schedule list   # scheduled tasks
```

---

*AI Vibe Toolkit | OpenClaw Full Setup | tháng 6/2026*
