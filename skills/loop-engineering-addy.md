# Loop Engineering — Xu Hướng Mới Của Vibe Coding (Addy Osmani)

**Nguồn:** Addy Osmani — Google Chrome Lead | @bachtambui (Bách làm Tech)
**Liên quan:** skills/sams-loop-engineering.md (framework chi tiết hơn)
**Cập nhật:** tháng 6/2026

---

## Core Quote

> "Thiết kế vòng lặp thay vì tự prompt agent"
> — Addy Osmani

---

## Vấn Đề Với Cách Làm Hiện Tại

```
Mày đang làm:
Mày → prompt → AI → output → mày review → prompt lại → ...

Vấn đề:
- Mày là bottleneck
- Mỗi lần cần mày ngồi đó
- Không scale
- Repetitive, error-prone
```

---

## Loop Engineering Là Gì

```
Thay vì: mày prompt từng bước
→ Mày DESIGN hệ thống tự prompt

Loop = recursive goal:
Define purpose
→ System discovers
→ System acts
→ System checks
→ System remembers
→ System repeats
→ Mày chỉ review kết quả
```

---

## 3 Levels Của Loop

### Level 1: Scheduled Automation
```
Cron job → trigger Claude → run task → output
(mày không cần làm gì, chỉ nhận kết quả)

Ví dụ: Morning brief lúc 7h tự động
```

### Level 2: Reactive Loop
```
Event → trigger → agent acts → verify → done

Ví dụ: PR mới → auto review → comment
```

### Level 3: Autonomous Loop (SAMS-style)
```
Goal defined → agent discovers → acts → checks → remembers → repeats
(chạy liên tục, tự cải thiện)
```

---

## Apply Ngay Cho AI Vibe Toolkit

```
Trước (manual prompting):
Mày thấy tool mới → nhắn Claude → Claude research → copy paste → push GitHub

Sau (loop engineering):
Mày thấy tool mới → nhắn Telegram "thêm [tool]"
→ OpenClaw nhận → Hermes research → push GitHub → notify Telegram

Mày chỉ làm: thấy → forward link
AI làm: research → format → push → notify

= Level 2 Loop: Reactive
```

---

## Checklist Thiết Kế Loop

```
□ Define Goal rõ ràng (1 câu)
□ Set cadence (cron hoặc event trigger)
□ Define tools/connectors
□ Hard Rules: KHÔNG làm gì
□ Output format cụ thể
□ Delivery destination
□ Human gate: khi nào cần review
□ Cost cap: max spend per run
```

---

## Liên Quan Trong Kho

- `skills/sams-loop-engineering.md` — framework SAMS chi tiết
- `VAULT/status.md` — system health
- `configs/openclaw-workflows.md` — 6 loop templates
- `skills/claude-routines-templates.md` — 6 prompt templates

---
*AI Vibe Toolkit | Loop Engineering Insight | tháng 6/2026*
