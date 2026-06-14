# agent-skills (Addy Osmani) — Index & Hướng Dẫn Dùng Nhanh

**Nguồn:** github.com/addyosmani/agent-skills (59k⭐) | MIT
**Tác giả:** Addy Osmani — Google Chrome Engineering Lead
**Cập nhật:** tháng 6/2026

---

## Cài Nhanh

```bash
# Claude Code
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# Cursor
# Copy SKILL.md bất kỳ vào .cursor/rules/

# Antigravity CLI
agy plugin install https://github.com/addyosmani/agent-skills.git

# Gemini CLI
gemini skills install https://github.com/addyosmani/agent-skills.git --path skills
```

---

## 7 Slash Commands — Development Lifecycle

```
DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
 /spec   /plan  /build   /test   /review  /ship
                         + /code-simplify
```

| Command | Dùng khi | Skill kích hoạt |
|---------|---------|----------------|
| `/spec` | Có idea, chưa có spec | spec-driven-development |
| `/plan` | Có spec, cần breakdown tasks | planning-and-task-breakdown |
| `/build` | Ready to code | incremental-implementation + TDD |
| `/build auto` | Approve plan 1 lần, AI tự chạy hết | tất cả build skills |
| `/test` | Cần prove it works | test-driven-development |
| `/review` | Trước khi merge | code-review-and-quality |
| `/code-simplify` | Code quá phức tạp | code-simplification |
| `/ship` | Deploy lên production | shipping-and-launch |

---

## 24 Skills — Theo Development Phase

### 🎯 DEFINE (Xác Định)
| File | Dùng khi |
|------|---------|
| `idea-refine.md` | Có idea mơ hồ, cần làm rõ trước khi làm gì |
| `interview-me.md` | AI phỏng vấn mày để extract requirements |
| `spec-driven-development.md` | Viết spec trước khi code — bắt buộc |

### 📋 PLAN (Lên Kế Hoạch)
| File | Dùng khi |
|------|---------|
| `planning-and-task-breakdown.md` | Breakdown task thành steps nhỏ, verifiable |

### 🔨 BUILD (Code)
| File | Dùng khi |
|------|---------|
| `incremental-implementation.md` | Code từng slice nhỏ, không dump cả feature |
| `test-driven-development.md` | Test trước, code sau |
| `context-engineering.md` | Manage context window hiệu quả |
| `source-driven-development.md` | Code từ nguồn chính thống, không hallucinate |
| `doubt-driven-development.md` | Dừng lại, verify assumptions trước khi tiếp |
| `frontend-ui-engineering.md` | Build UI components chuẩn production |
| `api-and-interface-design.md` | Design API trước khi implement |

### ✅ VERIFY (Kiểm Tra)
| File | Dùng khi |
|------|---------|
| `browser-testing-with-devtools.md` | Test web app với DevTools |
| `debugging-and-error-recovery.md` | Debug có hệ thống — không đoán mò |

### 🔍 REVIEW (Review)
| File | Dùng khi |
|------|---------|
| `code-review-and-quality.md` | Review 5 axes: correctness, readability, arch, security, perf |
| `code-simplification.md` | Simplify code phức tạp |
| `security-and-hardening.md` | Harden code trước khi ship |
| `performance-optimization.md` | Optimize performance có data |

### 🚀 SHIP (Deploy)
| File | Dùng khi |
|------|---------|
| `git-workflow-and-versioning.md` | Git workflow chuẩn |
| `ci-cd-and-automation.md` | Setup CI/CD pipeline |
| `deprecation-and-migration.md` | Migrate/deprecate safely |
| `documentation-and-adrs.md` | Viết docs + Architecture Decision Records |
| `observability-and-instrumentation.md` | Monitoring, logging, alerting |
| `shipping-and-launch.md` | Pre-launch checklist, rollback plan |

### 📖 META
| File | Dùng khi |
|------|---------|
| `using-agent-skills.md` | Hiểu cách dùng skills system này |

---

## Top 5 Skills Dùng Nhiều Nhất

**1. `spec-driven-development.md`** — Luôn dùng trước khi code bất cứ thứ gì
**2. `planning-and-task-breakdown.md`** — Có spec rồi thì breakdown tasks
**3. `incremental-implementation.md`** — Code từng slice, không dump cả feature
**4. `code-review-and-quality.md`** — Review mọi change trước merge
**5. `debugging-and-error-recovery.md`** — Khi có bug: follow process, đừng đoán mò

---

## Cách Dùng Thủ Công (Không Cần Cài Plugin)

1. Mở file `.md` tương ứng
2. Copy toàn bộ content
3. Paste vào đầu conversation Claude / Cursor
4. Bắt đầu task

---

*Nguồn gốc: addyosmani/agent-skills | MIT*
*AI Vibe Toolkit | tháng 6/2026*
