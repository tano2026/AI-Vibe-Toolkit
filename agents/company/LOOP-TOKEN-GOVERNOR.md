---
name: loop-token-governor
description: >
  Wire skill agentic-loop-optimizer (đã có sẵn, không viết lại) vào đúng kiến trúc thật của
  Tano Agency — map với OmniRoute tier, gắn exit condition theo DECISION-MATRIX risk level, và
  quy tắc cụ thể cho 9 agent thật. Đọc kèm skills/agentic-loop-optimizer/SKILL.md (lý thuyết đầy
  đủ nằm ở đó) — file này chỉ là lớp áp dụng cụ thể, không lặp lại nội dung.
version: 1.0
updated: 2026-07-25
---

# Loop & Token Governor — áp dụng cho 9 agent thật

## Vấn đề cụ thể cần giải — không phải lý thuyết suông

9 job P0 (dev, marketing) đang kẹt status "doing" 5 ngày liền không tiến triển — 1 trong các khả
năng (chưa loại trừ) là loop không có exit condition rõ, agent cứ gọi tool lặp lại không ra kết
quả, hoặc đơn giản là cron dừng (đã xác nhận nguyên nhân chính). Dù nguyên nhân chính đã rõ, đây
vẫn là lỗ hổng cần vá: **không có cơ chế nào tự phát hiện "job đứng loop bất thường" và báo động**
— nếu cron chạy lại mà 1 job thật sự bị stuck-loop, sẽ không ai biết cho tới khi hết ngân sách.

## Map Model Routing vào đúng OmniRoute đã có — không dùng ví dụ generic của skill gốc

Skill gốc dùng ví dụ `claude-haiku`/`claude-sonnet` — Tano Agency đã có OmniRoute với 4 tier
riêng, dùng đúng cái đã build:

```python
TIER = {
    "cheap":     "deepseek-v3",      # lookup, format, classify, task đơn giản lặp lại
    "balanced":  "gemini-flash",     # research vừa, tổng hợp không cần suy luận sâu
    "reasoning": "deepseek-r1",      # phân tích phức tạp, debug, kiến trúc
    "creative":  "claude-sonnet",    # content chất lượng cao, factcheck quan trọng
}

def pick_tier(task_type, risk_level):
    # Risk level càng cao, càng nên dùng tier tốt hơn — sai sót ở L2/L3 tốn kém hơn nhiều
    # so với phí chênh lệch giữa các tier
    if risk_level in ("L2", "L3"):
        return TIER["reasoning"] if task_type == "analysis" else TIER["creative"]
    if task_type in ("lookup", "format", "classify", "healthcheck"):
        return TIER["cheap"]
    return TIER["balanced"]
```

**Quy tắc cứng:** task L2/L3 (theo `DECISION-MATRIX.md`) KHÔNG được route xuống tier `cheap` dù
task_type nghe đơn giản — vì hậu quả sai ở mức rủi ro cao vượt xa phần tiết kiệm được.

## Exit condition gắn theo risk_level — không dùng số chung cho mọi task

```python
LOOP_LIMITS = {
    "L0": {"max_iterations": 10, "cost_cap_tokens": 15000},   # tự chạy, rẻ, cho phép thử nhiều
    "L1": {"max_iterations": 8,  "cost_cap_tokens": 12000},   # tự chạy + log, vẫn cho phép thử
    "L2": {"max_iterations": 3,  "cost_cap_tokens": 6000},    # sắp cần duyệt — đừng đốt token
                                                                 # trước khi biết CEO có approve không
    "L3": {"max_iterations": 1,  "cost_cap_tokens": 2000},    # dừng ngay để hỏi, KHÔNG được tự
                                                                 # loop thử nhiều phương án trước
}
```

**Lý do L2/L3 giới hạn chặt hơn L0/L1** (ngược trực giác nếu nghĩ "việc quan trọng nên đầu tư
nhiều hơn"): task L2/L3 CHƯA CHẮC được duyệt — nếu CEO từ chối, mọi token đã đốt để "thử nhiều
phương án" trước khi hỏi đều lãng phí. Tối ưu đúng là: **soạn 1 bản nháp gọn, hỏi sớm, không tự
lặp tìm phương án tối ưu trước khi biết có được làm hay không.**

## Circuit breaker — tự phát hiện stuck-loop, không đợi hết ngân sách mới biết

```python
def check_circuit_breaker(job):
    if job.iterations >= LOOP_LIMITS[job.risk_level]["max_iterations"]:
        escalate(job, reason="max_iterations_hit")
        return "STOP"
    if job.tokens_used >= LOOP_LIMITS[job.risk_level]["cost_cap_tokens"]:
        escalate(job, reason="cost_cap_hit")
        return "STOP"
    if job.output_similarity(prev_iteration) > 0.9:  # diminishing returns
        escalate(job, reason="no_improvement")
        return "STOP"
    if job.status == "doing" and (now() - job.last_activity) > timedelta(hours=2):
        escalate(job, reason="stalled_no_activity")  # chính là case 9 job đang kẹt
        return "STOP"
    return "CONTINUE"
```

**Field mới cần thêm vào bảng `jobs`** (Airtable, theo `COORDINATION-v2.md`): `iterations`,
`tokens_used`, `last_activity`, `circuit_breaker_reason`. Khi `bridge.py` (đang build) ghi job,
cần init các field này = 0/null, và mỗi lần OpenClaw/Hermes chạy 1 vòng phải cập nhật lại.

## Maker-Checker — áp đúng pattern đã có, gắn với review chéo COORDINATION-v2.md

Skill gốc đã có "Maker vs Checker" — khớp thẳng với cơ chế review chéo đã thiết kế trong
`COORDINATION-v2.md`. Không cần thêm gì, chỉ cần đảm bảo `bridge.py` khi dispatch job action
(qua OpenClaw) tách rõ: agent tạo output (Maker) ≠ agent/gate duyệt trước khi publish (Checker,
chính là `_publish_approval_gate()` đã có).

## Việc cần làm — thêm vào plan build OpenClaw/Hermes đang chạy

```
Paste cho Claude Code:

Thêm cơ chế Loop & Token Governor vào core/bridge.py + core/harness.py:
1. Thêm 4 field vào job record: iterations, tokens_used, last_activity,
   circuit_breaker_reason
2. Trước mỗi vòng lặp — check LOOP_LIMITS theo risk_level (bảng trong
   agents/company/LOOP-TOKEN-GOVERNOR.md), map model routing theo
   pick_tier() — dùng đúng OmniRoute 4 tier, không phải claude-haiku/sonnet
3. Cron riêng (10 phút/lần): quét job status="doing" mà last_activity >
   2 giờ → tự đánh circuit_breaker_reason="stalled_no_activity", báo
   Telegram. Đây chính là cơ chế đáng lẽ đã báo sớm việc 9 job kẹt 5 ngày.
```
