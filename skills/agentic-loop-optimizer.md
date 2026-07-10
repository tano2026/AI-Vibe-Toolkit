# Agentic Loop Optimizer — Skill

## TL;DR
Thiết kế vòng lặp agent chạy hiệu quả: không bị stuck, không tốn token vô ích, biết khi nào dừng. Tổng hợp từ SAMS framework, Loop Engineering (Addy Osmani), cost-aware pipeline và continuous-agent-loop patterns.

## Khi nào dùng
- Agent đang chạy loop nhưng tốn token nhiều, output không cải thiện sau vài vòng
- Muốn thiết kế loop từ đầu, cần chọn đúng pattern (sequential / reactive / autonomous)
- Cần thêm exit condition, cost cap, hoặc human gate vào loop hiện tại
- Agent "spin" — cứ gọi tool rồi gọi lại, không ra kết quả

---

## Core Concept

```
Manual prompting (cũ):
Mày → nhắc → AI → làm → báo → mày nhắc tiếp (mày là bottleneck)

Loop engineering (mới):
Mày define Goal → Agent discover → Act → Check → Remember → Repeat
(mày chỉ review kết quả)
```

Vòng lặp chuẩn:
```
Perceive → Think → Act → Observe → [Exit Check] → Repeat hoặc Done
```

---

## 3 Pattern Loop Theo Mức Độ

### Level 1 — Sequential (Tuần tự)
```
Trigger → Step 1 → Step 2 → Step 3 → Output → Done
```
Dùng khi: task có thứ tự cố định, ít nhánh điều kiện.
Ví dụ: Hermes nhận link → research → format .md → push GitHub → notify.

### Level 2 — Reactive Loop
```
Event → Agent acts → Verify → Done (hoặc retry 1 lần)
```
Dùng khi: trigger từ bên ngoài (Telegram message, webhook, cron job).
Ví dụ: Nobitano forward link Telegram → OpenClaw nhận → Hermes xử lý → báo lại.

### Level 3 — Autonomous Loop (SAMS-style)
```
Goal → Discover → Act → Check → Remember → Repeat (liên tục)
```
Dùng khi: agent cần tự cải thiện theo thời gian, không cần trigger thủ công.
Bắt buộc: cost cap + human gate + memory file.

---

## 6 Thành Phần Thiết Kế Loop (SAMS)

### 1. Goal — Recursive Target
```
Formula: Purpose + Cadence + Tools + Checks + Memory + Hard Rules
Ví dụ: "Mỗi ngày 9AM, scan kho GitHub → tìm entry thiếu script → tạo draft → notify Telegram"
```

### 2. Cadence — Nhịp Tim
```
Scheduled:  cron 0 9 * * * → morning brief
Reactive:   on webhook/event → xử lý ngay
Continuous: vòng lặp không dừng (cẩn thận cost)
```

### 3. Skills — Context Library (nạp 1 lần, loop đọc mỗi run)
```
TRACKER.md        → danh sách entries đã có (tránh duplicate)
KHO-INDEX.md      → entry point cho agent
agent-playbook.md → rules + tools available
```

### 4. Maker vs Checker (Sub-agent Pattern)
```
MAKER:   Explore → Build → Output
CHECKER: Test → Review → Approve (độc lập, không để maker tự chấm)

Rule: "Don't let the writer grade itself."
Áp dụng ngay: Research Pro v4.3 Drafter-Reviewer Loop = Maker vs Checker pattern.
```

### 5. Memory — File-based Vault
```
Không lưu trong chat (mất sau session). Lưu ra file:
triage.md    → quyết định phân loại
status.md    → trạng thái hiện tại
done-log.md  → đã làm gì, kết quả gì
next-up.md   → việc tiếp theo
```

### 6. Exit Condition — Quan Trọng Nhất
```
Thiếu exit condition = agent chạy mãi = tốn tiền

4 loại exit condition:
├── Max iterations:     if iterations >= N → stop
├── Confidence gate:    if confidence >= 0.85 → output và stop
├── Diminishing check:  if output[i] ≈ output[i-1] → stop (không cải thiện)
└── Cost cap:           if total_tokens >= budget → stop và báo user
```

---

## Token Optimization Patterns

### Model Routing theo Task Complexity
```python
# Đừng dùng Sonnet cho mọi thứ
CHEAP  = "claude-haiku-4-5"      # simple lookup, format, classify
SMART  = "claude-sonnet-4-6"     # complex reasoning, synthesis

def pick_model(task_type, text_length):
    if task_type in ["lookup", "format", "classify"] and text_length < 5000:
        return CHEAP   # 3-4x rẻ hơn
    return SMART
```

### Context Pruning (Tỉa Context)
```
Đừng giữ nguyên raw tool output qua các vòng lặp.
Sau mỗi tool call → summarize kết quả → drop raw → giữ summary.

Trước: [raw search result 2000 tokens] → vòng 2 vẫn carry nguyên
Sau:   [summary 200 tokens: "tìm thấy 3 tool liên quan: A, B, C"] → vòng 2 dùng summary
```

### Token Budget Per Iteration
```python
BUDGET_PER_LOOP = 2000  # tokens tối đa mỗi vòng

# Trước khi gọi tool:
if estimated_tokens > BUDGET_PER_LOOP:
    # Rút gọn input hoặc break task nhỏ hơn
    input = summarize(input)
```

### Reflection Trigger (Khi nào nên tự review)
```
Không cần review mọi vòng → tốn token.
Chỉ trigger reflection khi:
├── Output sẽ giao cho user (lần cuối)
├── Confidence < 0.7
├── Tool call failed lần 2
└── Vòng lặp thứ N (ví dụ: mỗi 3 vòng review 1 lần)
```

---

## Checklist Thiết Kế Loop

```
□ Define Goal rõ ràng (1 câu, có cadence)
□ Chọn pattern: Sequential / Reactive / Autonomous
□ List tools/connectors cần thiết
□ Hard Rules: KHÔNG làm gì (guardrail)
□ Exit condition (ít nhất 2 loại)
□ Cost cap (max token hoặc max spend)
□ Human gate: khi nào cần review thủ công
□ Memory: lưu state ra file gì
□ Maker vs Checker: ai verify output
□ Model routing: task nào dùng cheap model
```

---

## Ví dụ thực tế — AI Vibe Toolkit Loop

**Goal:** Tự động thêm tool mới vào kho khi Nobitano forward link Telegram.

```
Trigger: Nobitano gửi link qua Telegram
     ↓
OpenClaw nhận (Level 2 Reactive)
     ↓
[Check] TRACKER.md → đã có chưa? (exit nếu duplicate)
     ↓
Hermes research (MAKER): fetch GitHub + web search
     ↓
Hermes viết .md + script (MAKER output)
     ↓
[Checker]: validate đủ section? rating có điểm yếu không?
     ↓
Push GitHub (Act)
     ↓
Update TRACKER.md (Remember)
     ↓
Notify Telegram: "✅ Đã thêm [tên tool] — xem tại [link]"

Exit conditions:
- Duplicate → stop ngay sau Check
- Research fail 2 lần → notify "❌ Không tìm thấy nguồn"
- Token > 8000 trong 1 run → summarize và continue
```

---

## Lưu ý / Lỗi thường gặp

- **Loop không có exit condition** → agent chạy mãi, bill tăng không kiểm soát. Fix: luôn set max_iterations + cost_cap.
- **Tin tool output quá dễ** → không verify → sai vẫn tự tin output. Fix: Maker-Checker pattern, không để agent tự chấm.
- **Context blow up** → giữ nguyên raw output qua nhiều vòng. Fix: summarize sau mỗi tool call, drop raw.
- **Dùng Sonnet cho mọi task** → tốn 3-4x so với cần thiết. Fix: model routing theo complexity.
- **Memory trong chat** → mất sau session, agent quên sạch. Fix: file-based vault (triage.md, status.md).
- **Reflection quá nhiều** → mỗi vòng đều tự review → ngốn token. Fix: chỉ trigger reflection khi có điều kiện cụ thể.

---

## Đánh giá cá nhân

- **Điểm mạnh:** Tổng hợp được cả góc thiết kế (SAMS/Addy) lẫn góc kỹ thuật (cost-aware, context pruning) — không phải chọn 1 trong 2.
- **Điểm yếu:** Autonomous Loop (Level 3) cần infra thật (cron, persistent storage) — không chạy được chỉ bằng chat. Hermes hiện tại chưa có file-based vault → phải build thêm.
- **Có nên dùng không:** 9/10 — bất kỳ ai đang build agent system đều cần cái này. Thiếu nó thì loop sẽ tốn tiền hoặc stuck.

---

## Nguồn tổng hợp từ

- `skills/sams-loop-engineering.md` — SAMS framework (Axial Studio)
- `skills/loop-engineering-addy.md` — Loop Engineering (Addy Osmani)
- `skills/continuous-agent-loop/SKILL.md` — ECC canonical loop patterns
- `skills/autonomous-loops/SKILL.md` — autonomous loop architectures
- `skills/cost-aware-llm-pipeline/SKILL.md` — model routing + cost tracking
- `skills/context-budget/SKILL.md` — context window optimization
- `skills/token-budget-advisor/SKILL.md` — token budget management
- `skills/verification-loop/SKILL.md` — Maker-Checker verification
