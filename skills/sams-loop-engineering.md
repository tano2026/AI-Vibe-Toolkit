# SAMS — Loop Engineering Framework (Axial Studio)

**Nguồn:** Axial Studio | Carousel 10 slides
**Concept:** "Stop prompting agents. Start designing loops."
**Cập nhật:** tháng 6/2026

---

## Core Concept

```
Manual prompting (cũ):
Mày → nhắc → AI → làm → báo → mày nhắc tiếp

Loop engineering (mới):
Mày define Goal → System tự discover → act → check → remember → repeat
```

---

## 6 Thành Phần SAMS

### 1. Goal — Recursive Target
```
Define purpose → System discovers, acts, checks, remembers, repeats
Formula: Purpose + Cadence + Tools + Checks + Memory
```

### 2. Automations — Heartbeat
```
Scheduled runs tạo nhịp tim:
- Daily triage 9AM: scan inbox → triage → start tasks
- CI summary every commit: collect → summarize → report
- Bug hunt every 4h: find anomalies → correlate → create tasks
```

### 3. Skills — Project Context Library
```
Viết 1 lần, loop đọc mỗi run:
01-build-steps.md    → install deps, run tests, commit rules
02-architecture.md   → system overview, service boundaries, data flow
03-team-rules.md     → code style, PR checklist, review flow
04-dont-do-this.md   → anti-patterns, blocked libraries, known issues
```

### 4. Connectors — MCP Integration
```
GitHub (Code & PRs) + Linear (Issues) + Slack (Notify)
Docs (Knowledge Base) + Database (PostgreSQL) + API (External)

Flow: Issue → Code → PR → Notify (tự động hoàn toàn)
```

### 5. Sub-agents — Maker vs Checker
```
MAKER (Builds):
  Explore: analyze request, find context, create plan
  Build: write code, add tests, update docs

CHECKER (Verifies, độc lập):
  Test: run tests, check edge cases, verify quality
  Review: evaluate objectively, assess clarity, spot issues
  Approve: meets standards, ready to ship, approve & merge

Rule: "Don't let the writer grade itself."
```

### 6. Memory — Vault (File-based)
```
Memory sống ngoài chat, trong repo:
triage.md    → triage decisions & assignments
status.md    → current system health snapshot
done-log.md  → completed work and outcomes
next-up.md   → planned actions and priorities
board.view   → kanban board (live view)

Impact: 98.6% success WITH memory vs 22.1% stateless
```

---

## Mapping Với AI Vibe Toolkit

| SAMS Component | AI Vibe Toolkit |
|---------------|----------------|
| Goal | /configs/hermes-USER.md — define purpose |
| Automations | OpenClaw scheduled tasks |
| Skills | /skills/ folder (400+ files) |
| Connectors | /mcps/ (34 MCPs) |
| Memory/Vault | /VAULT/ folder (cần tạo) |
| Maker | Hermes Agent |
| Checker | Claude (human review gate) |

---

## Loop Templates Cho AI Vibe Toolkit

### Loop 1: Kho Research Loop
```
Cadence: Mỗi sáng 7h
Goal: Tìm repos AI mới đáng thêm vào kho
Automate: OpenClaw → scan GitHub trending
Check: Filter repos đã có trong kho
Memory: VAULT/trending-log.md
Human gate: Mày approve qua Telegram trước khi push
```

### Loop 2: Content Production Loop
```
Cadence: Thứ 6 16h
Goal: Tạo content calendar tuần tới
Automate: Hermes → scan scripts chưa quay
Check: viral-hooks skill review hook quality
Memory: VAULT/content-status.md
Human gate: Review calendar trước khi confirm
```

### Loop 3: ROAS Monitor Loop
```
Cadence: Mỗi sáng 8h
Goal: Check ROAS, flag underperformers
Automate: OpenClaw → Meta Ads MCP
Check: ROAS < 2x threshold
Memory: VAULT/ads-log.md
Human gate: CHỈ flag, không tự pause campaign
```

---

## Cost Control (Quan Trọng!)

Từ ảnh SAMS: 24 runs × $0.42 = ~$10/ngày nếu không kiểm soát.

```
Best practices:
- Dùng Claude Haiku cho routine checks (10x rẻ hơn Sonnet)
- Set max_tokens per loop run
- Human gate trước khi loop thực hiện actions tốn kém
- Log cost mỗi run vào VAULT/cost-log.md
- Daily budget cap trong OpenClaw config
```

---

## Guardrails (Không Được Bỏ)

```
✅ Cost Control: $X/ngày hard limit
✅ Quality Gate: Checker agent độc lập
✅ Approval Step: Human review trước production actions
✅ Risk Monitor: Slop risk + comprehension debt tracking
✅ "Build the loop. Stay the engineer." — mày vẫn maintain
```

---

*Phân tích từ Axial Studio SAMS carousel | AI Vibe Toolkit | tháng 6/2026*
