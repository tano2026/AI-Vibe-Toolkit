# openclaw — Skill Chạy AI Agent 24/7 Trên Máy Mày (210k⭐)

**Repo:** github.com/openclaw/openclaw | MIT
**Stars:** 210k — fastest growing AI agent repo lịch sử GitHub

---

## Cài Nhanh

```bash
curl -fsSL https://get.openclaw.dev | bash
openclaw setup
```

## Kết Nối Messaging

```bash
# Telegram
openclaw connect telegram --token BOT_TOKEN

# Discord
openclaw connect discord --token BOT_TOKEN

# WhatsApp (qua Baileys)
openclaw connect whatsapp
```

## 4 Workflow Hay Nhất

```bash
# 1. Research agent chạy schedule
openclaw schedule "mỗi sáng 8h: research GitHub trending AI repos, tóm tắt 5 cái hay nhất, gửi Telegram"

# 2. Monitor & alert
openclaw watch "khi GitHub repo X có commit mới → gửi summary qua Discord"

# 3. Content pipeline
openclaw run "lấy trending Twitter AI → viết thread → draft post → chờ approve → đăng"

# 4. Code review agent
openclaw hook "khi có PR mới trên repo → review code → comment trực tiếp lên GitHub"
```

## Kết Hợp Với Hermes Agent

```
OpenClaw (gateway/interface)
    ↓
Hermes Agent (brain — 8 loops, memory, skills)
    ↓
Sub-agents (parallel tasks)
```

OpenClaw = cổng tiếp nhận lệnh từ messaging apps
Hermes = xử lý thông minh, học theo thời gian

## Tips Token

- Dùng `openclaw model set gemini-flash` cho tasks đơn giản
- Reserve Claude/GPT-4 cho tasks cần reasoning
- Enable caching để tránh re-process same content

---
*skills/openclaw-skill.md | AI Vibe Toolkit | tháng 6/2026*
