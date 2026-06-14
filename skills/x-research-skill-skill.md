# x-research-skill — X/Twitter Research Agent (1146⭐)

**Repo:** github.com/rohunvora/x-research-skill | TypeScript
**Dùng với:** Claude Code, OpenClaw

---

## Cài

```bash
mkdir -p .claude/skills
cd .claude/skills
git clone https://github.com/rohunvora/x-research-skill.git x-research
export X_BEARER_TOKEN="..."  # X Developer Portal
```

## Commands

```bash
# Search với filters
/x-research search "AI agent 2026" --sort engagement --days 7

# Pull thread
/x-research thread "https://x.com/user/status/123"

# Monitor account
/x-research watch "@addyosmani" --keywords "claude,skills,agent"

# Quick mode (cheap)
/x-research quick "hermes agent review"

# Research brief
/x-research brief "taste-skill github"  # comprehensive sourced report
```

## Use Cases Cho AI Vibe Toolkit

```bash
# Tìm reactions về tool mới
/x-research search "hermes agent" --days 30 --sort engagement
→ Lấy top opinions → feed vào video script hook

# Monitor trending repos
/x-research watch "@github" --keywords "trending,stars,agent"
→ Phát hiện repos hot sớm

# Research trước khi viết .md
/x-research brief "tool X" 
→ Community sentiment + real use cases
→ Supplement README info

# Tìm video hook ideas
/x-research search "claude code problems" --sort engagement
→ Pain points cao nhất = hook video mạnh nhất
```

## Cost Transparency

```bash
# Mỗi search show cost
Search "AI agent 2026" (7 days, top 20): $0.003
Thread pull: $0.001
Monitor check: $0.001/check

# Cache tránh duplicate charges
# Same query trong session → từ cache
```

## Cần X API Access

- **Free tier:** 1,500 reads/tháng — đủ cho light use
- **Basic tier:** $100/tháng — cho heavy research
- **Developer portal:** developer.twitter.com

---
*skills/x-research-skill-skill.md | AI Vibe Toolkit | tháng 6/2026*
