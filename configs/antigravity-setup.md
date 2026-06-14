# Antigravity — Setup Guide Cho AI Vibe Toolkit Ecosystem

**Install:** antigravity.dev hoặc `npm install -g antigravity`
**Docs:** docs.antigravity.dev

---

## Vai Trò Trong Ecosystem

```
Antigravity = Package manager + Deploy tool cho AI ecosystem

Dùng để:
✅ Cài skills/plugins cho Claude Code
✅ Cài Hermes Agent
✅ Cài OpenClaw
✅ Deploy apps lên cloud
✅ Update tất cả tools 1 lệnh
```

---

## Cài Toàn Bộ Ecosystem — Chạy 1 Lần

```bash
# Cài Antigravity trước
npm install -g antigravity

# Xác nhận
agy --version

# Cài Hermes Agent
agy install hermes-agent
hermes setup --portal

# Cài OpenClaw
agy install openclaw
openclaw setup

# Cài skills cho Claude Code
agy plugin install addyosmani/agent-skills     # 24 dev skills
agy plugin install obra/superpowers            # Think before code
agy plugin install Leonxlnx/taste-skill        # Anti-slop UI
agy plugin install coreyhaines31/marketingskills # 43 marketing commands
agy plugin install AgriciDaniel/claude-seo     # SEO audit 18 agents
agy plugin install AgriciDaniel/claude-ads     # Paid ads 250+ checks
agy plugin install backnotprop/plannotator     # Review plan trước khi approve
agy plugin install Affitor/affiliate-skills    # 52 affiliate skills

# Verify tất cả đã cài
agy list --installed
```

---

## Deploy Apps

```bash
# Deploy web app lên Vercel
agy deploy --platform vercel ./my-app

# Deploy API lên Railway
agy deploy --platform railway ./my-api

# Deploy với env variables
agy deploy --platform vercel   --env ANTHROPIC_API_KEY=sk-ant-...   --env GITHUB_TOKEN=ghp_...   ./my-app

# Auto-deploy khi có commit mới
agy deploy --watch --branch main ./my-app
```

---

## Update Tất Cả Tools

```bash
# Update ecosystem
agy update --all

# Update 1 tool cụ thể
agy update hermes-agent
agy update openclaw

# Update tất cả plugins Claude Code
agy plugin update --all
```

---

## Backup & Restore

```bash
# Export config hiện tại
agy export > ~/.agy-backup-$(date +%Y%m%d).json

# Restore trên máy mới
agy import ~/.agy-backup-20260615.json

# Sync config qua GitHub (private repo)
agy sync --repo github.com/YOUR/private-config
```

---

## Useful Commands

```bash
agy status              # Xem tất cả tools đang chạy
agy logs hermes         # Logs của Hermes
agy logs openclaw       # Logs của OpenClaw
agy restart hermes      # Restart service
agy stop openclaw       # Stop service
agy plugin list         # List Claude Code plugins
agy doctor              # Diagnose issues
```
