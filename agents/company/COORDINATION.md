# COORDINATION — Giao thức phối hợp giữa 7 vị trí

> Đọc kèm `agents/company/ORG.md`. File này định nghĩa: workspace chung, format handoff,
> approval loop với CEO, và sync định kỳ. Mọi role pack đều tuân theo file này.

---

## 1. Shared workspace: 2 tầng, không thêm tool mới

| Tầng | Công cụ | Chứa gì | Vì sao chọn |
|------|---------|---------|-------------|
| **Artifacts** | Repo `tano2026/AI-Vibe-Toolkit` | Deliverable cuối: report, script, plan, file design spec | Đã là source of truth, versioned, agents đã biết fetch, append-only quen thuộc |
| **State** | Airtable base `company-hq` | Task queue, trạng thái, approvals, activity log | Airtable vốn đã là kế hoạch memory layer cho Hermes — dùng luôn, 1 công đôi việc. REST API đơn giản, Hermes gọi được bằng `urllib.request` |

Không dùng Notion/tool thứ 3 cho state — thêm tool = thêm điểm hỏng cho công ty 1 người.

---

## 2. Schema Airtable base `company-hq` (3 tables)

### Table `tasks`
| Field | Type | Ghi chú |
|-------|------|---------|
| `task_id` | Autonumber/formula | ID duy nhất, dùng trong mọi giao tiếp |
| `pack` | Single line | Slug Domain Pack (`abtrip`, `wonder-mart`...) |
| `role` | Single select | research / marketing / sales / content / designer / media / dev |
| `brief` | Long text | Context + yêu cầu + định nghĩa "xong" (format mục 3) |
| `status` | Single select | `queued` → `doing` → `review` → `done` / `blocked` / `awaiting_approval` |
| `output_url` | URL | Link file trong repo hoặc artifact |
| `depends_on` | Link to tasks | Task phải xong trước |
| `requested_by` | Single line | `ceo` hoặc tên role khởi tạo (phối hợp ngang hàng) |
| `created`, `updated` | Datetime | |

### Table `approvals`
| Field | Type | Ghi chú |
|-------|------|---------|
| `task_id` | Link to tasks | |
| `action` | Long text | Mô tả CHÍNH XÁC hành động sắp thực thi (gửi cho ai, nội dung gì, tiền bao nhiêu) |
| `risk_type` | Single select | send_external / spend_money / publish / production / credential |
| `status` | Single select | `pending` → `approved` / `rejected` / `expired` |
| `decided_at` | Datetime | |

### Table `activity_log` (append-only)
| Field | Type |
|-------|------|
| `ts` | Datetime |
| `role` | Single select |
| `task_id` | Link |
| `event` | Long text — 1 dòng: làm gì, kết quả gì |

**Code mẫu Hermes (urllib, không dùng requests):**
```python
import urllib.request, json, os

AT_TOKEN = os.environ["AIRTABLE_TOKEN"]   # env var, không hardcode
BASE = os.environ["AIRTABLE_BASE_HQ"]     # app... của base company-hq

def at(table, method="GET", record=None, payload=None):
    url = f"https://api.airtable.com/v0/{BASE}/{table}"
    if record: url += f"/{record}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {AT_TOKEN}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

# Nhận task: lấy task queued của role mình
tasks = at("tasks?filterByFormula=" + urllib.parse.quote("AND({role}='content',{status}='queued')"))

# Ghi log 1 dòng sau mỗi bước đáng kể
at("activity_log", "POST", payload={"records":[{"fields":{
    "role":"content","event":"Draft xong script video cho [Sản phẩm X], chờ review chéo"}}]})
```

---

## 3. Handoff protocol — format chuẩn cho MỌI lần giao việc

Dù CEO giao hay role giao chéo cho nhau, message/brief PHẢI đủ 5 phần:

```
[PACK: <slug>]                      ← bắt buộc, xác định project
[FROM: <role|ceo>] [TO: <role>] [TASK: <task_id>]
1. CONTEXT   — vì sao cần, dùng vào việc gì tiếp theo
2. YÊU CẦU   — cụ thể, đo được (không "làm cho đẹp")
3. INPUT KÈM — link data/file/insight sẵn có (đừng bắt bên nhận research lại)
4. DEADLINE  — hoặc "khi rảnh" nói rõ
5. DONE =    — định nghĩa "xong" kiểm tra được (vd: "file .md trong /content/, có 3 hook option")
```

Thiếu phần nào → bên nhận trả lại hỏi đúng 1 câu, không đoán bừa.

**Phối hợp chủ động (không chờ CEO làm cầu nối):** role tự tạo row `tasks` mới với
`requested_by = <role mình>` khi cần input từ role khác. Ví dụ chuẩn:
- Content cần số liệu cho claim → tạo task `role=research`, brief nêu rõ claim cần verify.
- Marketing chạy campaign → tạo SONG SONG 2 task cho Designer + Content, link `depends_on` về task campaign gốc.

---

## 4. Approval loop — 1 cơ chế duy nhất cho mọi hành động rủi ro

```
Agent chuẩn bị hành động rủi ro (theo ma trận tự chủ trong ORG.md)
   → tạo row `approvals` (status=pending, action mô tả CHÍNH XÁC)
   → set task status = awaiting_approval
   → OpenClaw gửi Telegram cho CEO:
     "⚠️ [<task_id>] <role> xin duyệt: <action tóm tắt>. Reply: OK <task_id> / NO <task_id>"
CEO reply "OK <task_id>"  → OpenClaw set approved → executor thực thi → log
CEO reply "NO <task_id>"  → rejected → task về doing kèm note
Không reply sau 24h       → expired → KHÔNG thực thi, nhắc lại 1 lần duy nhất
```

Quy tắc sắt:
- **Không có approved record = không thực thi.** Kể cả CEO đã nói miệng ở chỗ khác.
- Action mô tả trong approval phải là bản CUỐI — duyệt xong không được sửa nội dung rồi gửi.
- Mọi lần thực thi thật đều ghi `activity_log` ngay sau đó.

---

## 5. Review chéo trước khi "chạm CEO / chạm khách"

| Output từ | Reviewer mặc định | Check gì |
|-----------|-------------------|----------|
| Content | Research | Mọi claim/số liệu có nguồn không |
| Designer | Content | Đúng thông điệp, đúng brand voice theo PACK |
| Media (lịch đăng) | Marketing | Đúng kênh, đúng tần suất, đúng project |
| Sales (outreach) | Marketing | Đúng định vị, đúng giá theo PACK constraints |
| Marketing (plan chi tiền) | Research | Số liệu nền có thật không |
| Dev (thay đổi hạ tầng) | — | Theo checklist riêng trong infra-ops-agent |

Review chéo = 1 task nhỏ `status=review`, reviewer note thẳng vào task. Không họp, không round-trip nhiều lần: tối đa 1 vòng sửa, còn cấn thì đẩy lên CEO quyết.

---

## 6. Sync định kỳ

- **Daily (tối):** OpenClaw quét Airtable → tổng hợp 1 message Telegram cho CEO:
  `Hôm nay: X done / Y doing / Z blocked / N chờ duyệt (list task_id)`. Không quá 10 dòng.
- **Weekly:** Hermes xuất report .md ngắn (theo pack, theo role) → push `/reports/` trong repo — CEO đọc khi cần, không bắt đọc.

---

## 7. Domain Pack switching — chống lẫn project

1. Mọi message/task đều có `[PACK: <slug>]` — không có thì không chạy.
2. Agent đổi pack giữa phiên → dòng đầu output phải xác nhận: `Đang làm việc trên PACK: <slug>`.
3. File output đặt tên có slug: `report-<slug>-<topic>.md` — nhìn tên biết ngay của project nào.
4. Không bao giờ copy nguyên đoạn context từ pack này sang output của pack khác.
