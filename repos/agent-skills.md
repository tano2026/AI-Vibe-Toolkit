# agent-skills — 24 Engineering Skills Của Senior Engineer Thành AI Agent

**GitHub:** https://github.com/addyosmani/agent-skills
**Stars:** 59k⭐ | **Forks:** 6.4k | **License:** MIT
**Tác giả:** Addy Osmani — Google Chrome Engineering Lead
**Tạo:** 02/2026 | **Đang trending GitHub hôm nay**

---

## Đây Là Gì

Bộ 24 skills mã hóa **workflow, quality gates, và best practices** mà senior engineers dùng khi build software — packaged để AI agents follow nhất quán qua mọi phase development.

**Vấn đề:** AI coding agent thường skip steps quan trọng — code không có spec, không có tests, không có review, ship mà không có monitoring. Kết quả: tech debt chồng chất.

**agent-skills fix cái đó.** Install 1 lần → AI tự kích hoạt đúng skill đúng lúc.

---

## 7 Slash Commands — Toàn Bộ Dev Lifecycle

```
DEFINE → PLAN  → BUILD → VERIFY → REVIEW → SHIP
 /spec   /plan   /build   /test   /review  /ship
                          + /code-simplify
```

| Command | Nguyên tắc cốt lõi |
|---------|-------------------|
| `/spec` | Spec trước khi code |
| `/plan` | Tasks nhỏ, atomic |
| `/build` | Từng slice một |
| `/build auto` | Approve plan 1 lần → AI tự chạy hết |
| `/test` | Tests = proof it works |
| `/review` | Improve code health trước merge |
| `/code-simplify` | Clarity over cleverness |
| `/ship` | Faster is safer |

---

## 24 Skills — Theo Phase

**Define:** idea-refine, interview-me, spec-driven-development
**Plan:** planning-and-task-breakdown
**Build:** incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design
**Verify:** browser-testing-with-devtools, debugging-and-error-recovery
**Review:** code-review-and-quality, code-simplification, security-and-hardening, performance-optimization
**Ship:** git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, observability-and-instrumentation, shipping-and-launch
**Meta:** using-agent-skills

---

## Cài Đặt

```bash
# Claude Code (recommended)
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# Cursor — copy SKILL.md vào .cursor/rules/
# Antigravity CLI
agy plugin install https://github.com/addyosmani/agent-skills.git
# Gemini CLI
gemini skills install https://github.com/addyosmani/agent-skills.git --path skills
```

---

## Tại Sao Khác Các Skills Khác

**Skills thông thường:** List rules → AI đọc → đôi khi follow.

**agent-skills:** Skills **tự kích hoạt** theo context:
- Đang design API → `api-and-interface-design` bật lên
- Đang build UI → `frontend-ui-engineering` bật lên
- Code có lỗi → `debugging-and-error-recovery` bật lên

Không cần nhớ dùng skill nào — AI tự biết.

---

## Addy Osmani Là Ai

Google Chrome Engineering Lead. Tác giả cuốn "Learning JavaScript Design Patterns". Viết về web performance, engineering practices. Khi ông ta viết 24 skills về engineering workflow — đây là distilled knowledge từ 15+ năm làm ở Google.

---

## Đánh Giá Cá Nhân

59k stars, đang trending ngày hôm nay — repo này đang bùng nổ.

Điểm tao thích nhất: **`/build auto`** — approve plan 1 lần, AI tự implement từng task, tự test, tự commit. Mày chỉ cần review kết quả cuối. Đây là level automation mà vibe coders cần.

Điểm khác biệt với taste-skill hay continue rules: agent-skills cover **toàn bộ dev lifecycle** từ idea đến ship — không chỉ code style hay UI. Đây là "senior engineer workflow as code."

**Rating: 9.5/10** — Cài ngay nếu dùng Claude Code hoặc Cursor.

---

*Nguồn: github.com/addyosmani/agent-skills*
*Stars: 59k⭐ (tháng 6/2026) | MIT | Đang trending*
*24 SKILL.md files đã lưu vào: skills/agent-skills/*
*Cập nhật: tháng 6/2026*
