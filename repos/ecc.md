# ECC (affaan-m) — Agent Harness OS Cho Claude Code/Codex (215k⭐)

**GitHub:** https://github.com/affaan-m/ECC
**Stars:** 215k⭐ | **Forks:** 30.2k | **License:** MIT
**#4 GitHub Trending Tuần 23** | +10,351 stars tuần này
**Tagline:** "The agent harness performance optimization system"
**Tương thích:** Claude Code, Codex, Opencode, Cursor, và beyond

---

## Đây Là Gì

**ECC = Everything Claude Code** — hệ vận hành cho AI coding agents. Gồm: Skills + Instincts + Memory + Security + Research-first development.

Không phải plugin đơn lẻ — là **operating system** cho toàn bộ AI coding workflow.

---

## 3 Thành Phần Chính

### Skills
Reusable behaviors cho agent:
```bash
# Cài skills từ ECC marketplace
/skill install code-review
/skill install test-generator
/skill install security-audit
/skill install documentation
```

### Instincts
Behaviors built-in chạy tự động:
- Detect patterns và apply best practices
- Self-correct khi detect lỗi
- Research trước khi implement

### Memory
Cross-session context:
- Nhớ preferences của mày
- Nhớ codebase conventions
- Nhớ decisions đã làm và lý do

---

## Cài Đặt

```bash
# Claude Code
/plugin marketplace add affaan-m/ECC
/plugin install ecc@affaan-m-ecc

# Codex
codex plugin install affaan-m/ECC

# Opencode
opencode plugin install affaan-m/ECC

# Cursor
# Xem docs/cursor/README.md
```

---

## Folder Structure Trong ECC Repo

```
affaan-m/ECC/
├── agents/          # Pre-built agent configs
├── claude/          # Claude Code specific
├── codex/           # Codex specific  
├── claude-plugin/   # Plugin definitions
├── codex-plugin/    # Codex plugin
├── cursor/          # Cursor rules
├── gemini/          # Gemini CLI
├── github/          # GitHub Actions
├── kiro/            # Kiro IDE
├── opencode/        # Opencode
└── raven/           # Raven agent
```

---

## Khác Với agent-skills (Addy Osmani)

| | ECC | agent-skills |
|--|-----|-------------|
| Scope | OS layer (skills+memory+security) | Skills only |
| Tools | 289 (Jaz-style) qua integrations | 24 skills |
| Memory | ✅ Cross-session | ❌ |
| Multi-tool | Claude+Codex+Cursor+Opencode | Claude Code chủ yếu |
| Stars | 215k | 59k |

**Dùng cả 2:** ECC cho OS layer, agent-skills cho dev lifecycle skills.

---

## Đánh Giá Cá Nhân

215k stars — số cao nhất trong repo AI coding tools hiện tại. Community cực lớn.

Điểm tao thấy hay nhất: **multi-tool support** — cùng 1 config chạy được trên Claude Code, Codex, Cursor, Opencode. Không bị lock-in vào 1 tool.

**Rating: 9/10** — Cài ngay nếu dùng nhiều AI coding tools.

---
*Nguồn: github.com/affaan-m/ECC | 215k⭐ | MIT | tháng 6/2026*
