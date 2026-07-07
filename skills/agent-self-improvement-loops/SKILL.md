---
name: agent-self-improvement-loops
description: >
  Framework 5 nhóm vòng lặp tự cải thiện (Chất lượng, Trí nhớ, Kế hoạch, Khám phá, Tự tối ưu)
  cho mọi agent trong hệ sinh thái — Claude, Hermes, OpenClaw, Antigravity. Dùng khi thiết kế
  agent mới, audit agent cũ chạy tệ, hoặc quyết định agent thiếu tầng nào trước khi thêm tool mới.
  Trigger khi user nói: "agent này không học được gì", "sao Hermes cứ lặp lại lỗi cũ", "audit loop
  cho agent X", "agent thiếu tầng nào", "tự tối ưu agent", "agent tự cải thiện".
---

# Agent Self-Improvement Loops — 5 Tầng Vòng Lặp

## TL;DR
Framework chấm điểm + nâng cấp agent theo 5 tầng loop: Chất lượng (tự kiểm output), Trí nhớ (học
từ lần trước), Kế hoạch (thích nghi khi thực tế đổi), Khám phá (thử song song nhiều hướng), Tự tối
ưu (loop chỉnh chính loop). Nguồn gốc: tổng hợp thực chiến (X @sairahul1) + khớp với research area
"self-improving agents" (Reflexion, ReasoningBank, Self-Refine, dual-loop planning).

## Khi nào dùng
- Build agent mới bằng `agentic-factory` → dùng skill này để audit xem 5 tầng đã đủ chưa trước khi
  generate package.
- Agent cũ (Hermes, Sales CEO...) chạy sai lặp lại → chẩn đoán đang thiếu tầng nào (thường là Trí nhớ).
- Quyết định nên thêm tool/MCP gì tiếp theo → map vào đúng tầng cần bù, không thêm bừa.

## Nội dung skill

### 5 tầng, chấm điểm 1-5 mỗi tầng

| Tầng | Câu hỏi chẩn đoán | Cơ chế literature tương ứng |
|---|---|---|
| **1. Chất lượng** | Agent có tự kiểm output trước khi trả không? | Self-Refine / Reflection critic loop |
| **2. Trí nhớ** | Agent có nhớ lần trước đã sai/đúng gì không? | Reflexion / ReasoningBank — lưu *reflection* dạng text, không phải raw log |
| **3. Kế hoạch** | Agent có tự điều chỉnh hướng khi thực tế lệch kế hoạch không? | Dual-loop planning (outer loop giữ mục tiêu, inner loop làm chi tiết) |
| **4. Khám phá** | Agent có thử song song nhiều hướng thay vì đâm đầu 1 đường không? | Parallel exploration, tránh local minimum |
| **5. Tự tối ưu** | Agent có tự chỉnh CƠ CHẾ HỌC của chính nó không? | Metacognitive learning — bài toán mở, hiếm khi cần build thật |

### Nguyên tắc áp dụng
1. **Không chase đủ 5 tầng cùng lúc.** Ưu tiên: tầng 2 (Trí nhớ) luôn là nền — thiếu nó thì tầng 3,
   4 vô nghĩa vì agent không học được gì giữa các lần chạy.
2. **Tầng 5 gần như luôn bỏ qua** trừ khi 4 tầng dưới đã vững — đây là bài toán research còn mở,
   build sớm chỉ tốn effort không ra giá trị.
3. **Reflection ≠ raw log.** Lưu "rút ra được gì" (1-3 câu, ngôn ngữ tự nhiên), không lưu toàn bộ
   transcript — tránh corrupt memory với noise.
4. **Validation gate cho tầng Trí nhớ**: memory update chỉ được promote nếu cải thiện outcome đo
   được; nếu làm agent tệ đi → tự động revert. Không để agent tự ghi đè memory không kiểm soát.

### Cách chấm 1 agent hiện có (workflow chẩn đoán)
1. Hỏi: agent có bước nào tự review output trước khi trả không? → chấm tầng 1.
2. Hỏi: agent có state storage nào giữa các lần chạy không (không phải chat history)? → chấm tầng 2.
3. Hỏi: khi có lỗi giữa chừng, agent có đổi hướng hay cắm đầu chạy tiếp? → chấm tầng 3.
4. Hỏi: agent có chạy song song hướng khác để so sánh không, hay luôn 1 đường? → chấm tầng 4.
5. Tầng 5: mặc định điểm thấp là bình thường, không phải lỗi thiết kế.

## Ví dụ thực tế
Áp cho Hermes (agent thực thi task Python trong hệ sinh thái Nobitano):
- Tầng 1 (Chất lượng): 3/5 — có validate output cơ bản nhưng chưa có critic loop rõ ràng.
- Tầng 2 (Trí nhớ): 1/5 — mỗi lần chạy là tabula rasa, không có state storage layer → đây là gap
  lớn nhất, fix trước tiên (Google Sheets/Airtable cho reflection log, không phải raw transcript).
- Tầng 3 (Kế hoạch): 2/5 — OpenClaw router có outer loop nhưng chưa tự redirect khi Hermes fail lặp.
- Tầng 4 (Khám phá): 1/5 — Collector trong Research Pro chạy tuần tự, chưa parallel query angles.
- Tầng 5 (Tự tối ưu): bỏ qua, chưa cần.
→ Khuyến nghị: fix tầng 2 trước (thêm state storage), rồi mới lên tầng 3 và 4.

## Lưu ý / Lỗi thường gặp
- Nhầm "lưu nhiều log" với "có trí nhớ" → log không phải memory nếu agent không retrieve và dùng
  lại được lần sau.
- Build tầng 5 (tự tối ưu) khi tầng 2 (trí nhớ) còn chưa có → lãng phí effort, tầng trên phụ thuộc
  tầng dưới.
- Không có validation gate cho memory → 1 reflection sai lan ra làm hỏng mọi quyết định sau đó
  (memory corruption pattern).

## Đánh giá cá nhân
- Điểm mạnh: framework đơn giản, chấm điểm nhanh, map thẳng vào literature thật (không phải hype),
  áp được cho bất kỳ agent nào không riêng gì code.
- Điểm yếu: tầng 5 mơ hồ nhất, dễ bị hiểu nhầm thành "AI tự học vô hạn" trong khi thực chất chỉ là
  agent chỉnh sửa cơ chế học của chính nó — hiếm agent thực tế cần tới.
- Có nên dùng không: 8/10 — dùng làm checklist audit định kỳ cho mọi agent trong hệ sinh thái, không
  dùng làm blueprint xây agent từ đầu (đó là việc của `agentic-factory`).

## Link
- Nguồn tổng hợp: X @sairahul1 (01/07/2026)
- Liên quan trong kho: `agentic-factory` (build agent mới), `continuous-learning-v2` (instinct-based
  learning cho Claude Code sessions — khác phạm vi, chỉ áp cho dev loop), `autonomous-loops` /
  `continuous-agent-loop` (pipeline kỹ thuật, không phải framework chẩn đoán 5 tầng này).

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Reflection logging pattern — dùng cho tầng 2 (Trí nhớ)
# Lưu vào Google Sheets/Airtable, KHÔNG lưu raw transcript, chỉ lưu rút gọn
import json, time

def log_reflection(task_type: str, outcome: str, lesson: str, store_fn):
    """
    task_type: loại task (vd 'fetch_github', 'skill_lookup')
    outcome: 'success' | 'fail'
    lesson: 1-3 câu rút ra được — KHÔNG phải raw log
    store_fn: hàm ghi vào state storage layer (Sheets/Airtable/DB)
    """
    entry = {
        "ts": time.time(),
        "task_type": task_type,
        "outcome": outcome,
        "lesson": lesson,
    }
    store_fn(entry)

def retrieve_lessons(task_type: str, fetch_fn, limit=5):
    """Kéo lại lesson liên quan trước khi chạy task cùng loại — đây là bước hay bị bỏ quên."""
    all_entries = fetch_fn(task_type)
    return sorted(all_entries, key=lambda e: e["ts"], reverse=True)[:limit]
```
> ⚠️ Đây mới là pattern — Hermes hiện chưa có state storage layer thật (ticket đã nằm trong
> `agents/ANTIGRAVITY-PLAYBOOK.md`). Code trên chỉ chạy được sau khi có backend lưu trữ (Sheets/Airtable).

### OpenClaw
```bash
# Outer-loop redirect: OpenClaw router nên check fail-count trước khi route lại domain cũ
# Nguyên tắc: nếu Hermes fail cùng 1 task_type >= 3 lần liên tiếp → OpenClaw đổi hướng
# (thử domain khác, hoặc escalate lên Telegram cho Nobitano) thay vì lặp lại route cũ
```
> ⚠️ Đây là tầng 3 (Kế hoạch) — chưa implement, cần thêm fail-counter vào Domain Agent Router.

### Antigravity
```bash
# Việc của Antigravity: dựng backend state storage (tầng Trí nhớ) trước tiên
# Ưu tiên deploy: Google Sheets API hoặc Airtable, gắn vào Hermes qua default_api
# Đây là blocker lớn nhất trong toàn bộ framework 5 tầng — không có tầng 2 thì tầng 3,4 vô dụng
```
