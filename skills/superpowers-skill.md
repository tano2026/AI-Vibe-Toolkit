# superpowers — Skill Biến Claude Code Thành Senior Dev (150k⭐)

**Repo:** github.com/obra/superpowers | MIT | Jesse Vincent
**Dùng với:** Claude Code

---

## Cài 1 Lệnh

```bash
/plugin marketplace add obra/superpowers
/plugin install superpowers@obra-superpowers
```

Hoặc manual:
```bash
git clone https://github.com/obra/superpowers ~/.claude/plugins/superpowers
```

## Superpowers Làm Gì

Thêm behaviors vào Claude Code — AI sẽ:
- **Think trước khi code** — không nhảy vào làm bừa
- **Test-driven** — viết test trước, code sau
- **Self-review** — tự review code trước khi output
- **Incremental** — từng step nhỏ, verify từng bước

## Core Commands

```bash
/plan    # Lên kế hoạch trước khi code
/spec    # Viết spec từ requirements
/build   # Code có test, incremental
/review  # Self-review code quality
/ship    # Pre-deploy checklist
```

## Kết Hợp Với agent-skills (Addy Osmani)

```bash
# Cài cả 2 — synergy effect
/plugin marketplace add obra/superpowers
/plugin marketplace add addyosmani/agent-skills

# Workflow hoàn chỉnh:
/spec → /plan → /build → /review → /ship
```

## Tips

- Dùng `/plan` cho mọi task > 30 phút
- Dùng `/spec` trước khi bắt đầu feature mới
- Kết hợp với `CLAUDE.md` để persist behaviors

---
*skills/superpowers-skill.md | AI Vibe Toolkit | tháng 6/2026*
