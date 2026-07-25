---
name: coordination-v2
description: Coordination layer v2 — schema Airtable company-hq 7 bảng, job lifecycle, approval loop, review chéo
version: 2.0
replaces: agents/company/COORDINATION.md
updated: 2026-07-19
---

# COORDINATION v2 — Airtable `company-hq` + giao thức phối hợp

> Thay thế `COORDINATION.md` (v1: 3 bảng). V2 = 7 bảng, đủ cho chuẩn nhân viên AI
> (JD/KPI/SOP/escalation) mà vẫn tạo tay được trong ~30 phút.
> Đọc kèm: `ORG-v2.md`, `OPERATING-RHYTHM.md`, `DECISION-MATRIX.md`.

---

## 1. Nguyên tắc

- **Artifacts** = repo `tano2026/AI-Vibe-Toolkit` (deliverable, versioned).
- **State** = Airtable `company-hq` (queue, trạng thái, duyệt, log). Không thêm tool thứ 3.
- CEO chỉ nhìn **1 view duy nhất mỗi sáng** (`CEO Cockpit`, mục 3) — mọi thứ khác tự chạy.
- Token Airtable nằm trong env var trên VPS (`AIRTABLE_TOKEN`, `AIRTABLE_BASE_HQ`) — không bao giờ trong file .md.

---

## 2. Schema 7 bảng (tạo theo đúng thứ tự này, bảng sau link bảng trước)

### 2.1 `agents` — sổ nhân sự AI (tạo TRƯỚC, bảng khác link vào)
| Field | Type | Ghi chú |
|-------|------|---------|
| `role` | Single line | research / marketing / sales / content / designer / media / ops-finance / hr-admin / legal-compliance / dev |
| `runtime` | Multiple select | hermes / openclaw / antigravity |
| `model_tier` | Single select | cheap / balanced / reasoning / creative |
| `role_pack_url` | URL | Link raw GitHub tới role pack |
| `status` | Single select | active / paused |
| `kpi_chinh` | Single line | 1 câu, khớp bảng ORG-v2 |
| `escalation_rule` | Long text | Khi nào dừng gọi CEO (copy từ role pack) |

Seed: 10 record = 10 role theo ORG-v2 (v2.2, đã thêm HR & Admin ⑨ và Legal & Compliance ⑩).

### 2.2 `jobs` — trái tim hệ thống
| Field | Type | Ghi chú |
|-------|------|---------|
| `job_id` | Autonumber | Dùng trong MỌI giao tiếp, kể cả lệnh duyệt |
| `pack` | Single select | abtrip / an-binh / trum-san-bay / tano-cafe / airfare-decoded / gmsp / ai-review / noi-bo |
| `role` | Link to `agents` | Ai nhận việc |
| `brief` | Long text | Format handoff 5 phần (mục 4) |
| `status` | Single select | `queued` → `doing` → `review` → `awaiting_approval` → `done` · nhánh: `blocked` |
| `priority` | Single select | P0 (hôm nay) / P1 (tuần này) / P2 (khi rảnh) |
| `output_url` | URL | Link deliverable trong repo |
| `depends_on` | Link to `jobs` | Job phải xong trước |
| `requested_by` | Single line | `ceo` hoặc tên role (phối hợp ngang hàng) |
| `sop` | Link to `sops` | SOP áp dụng (nếu việc lặp lại) |
| `due` | Date | |
| `created`, `updated` | Created/Last modified time | Tự động |

### 2.3 `sops` — thư viện quy trình
| Field | Type | Ghi chú |
|-------|------|---------|
| `sop_id` | Autonumber | |
| `name` | Single line | Vd "Sản xuất 1 video TikTok Trùm Sân Bay" |
| `role` | Link to `agents` | Role sở hữu |
| `trigger` | Single line | Khi nào dùng ("job dạng X", "mỗi thứ 2"...) |
| `steps` | Long text | Đánh số từng bước + định nghĩa xong của mỗi bước |
| `version` | Number | Tăng khi sửa; sửa SOP = job dạng `noi-bo` cần CEO duyệt |
| `updated` | Last modified time | |

Luật: việc gì lặp ≥3 lần mà chưa có SOP → role tự draft SOP, CEO duyệt 1 lần, từ đó chạy theo SOP.

### 2.4 `kpis` — bảng điểm
| Field | Type | Ghi chú |
|-------|------|---------|
| `metric` | Single line | Vd "Bài đăng đúng lịch", "Booking Fast Track" |
| `pack` | Single select | Cùng option với `jobs.pack` |
| `role` | Link to `agents` | |
| `target` | Number | Theo tuần |
| `actual` | Number | Role tự cập nhật tối CN (rhythm) |
| `week` | Single line | Vd `2026-W30` |
| `note` | Long text | Giải thích lệch target — bắt buộc nếu actual < 70% |

### 2.5 `approvals` — cổng duyệt (giữ nguyên v1 + risk_level)
| Field | Type | Ghi chú |
|-------|------|---------|
| `job_id` | Link to `jobs` | |
| `action` | Long text | Mô tả CHÍNH XÁC bản CUỐI (gửi ai, nội dung gì, bao nhiêu tiền) |
| `risk_type` | Single select | spend_money / publish / send_external / commit_customer / production / credential |
| `risk_level` | Single select | L2 / L3 (theo DECISION-MATRIX.md) |
| `status` | Single select | `pending` → `approved` / `rejected` / `expired` |
| `decided_at` | Date | |

### 2.6 `escalations` — nhật ký sự cố & vượt cấp
| Field | Type | Ghi chú |
|-------|------|---------|
| `ts` | Created time | |
| `job_id` | Link to `jobs` | |
| `role` | Link to `agents` | Ai kêu |
| `reason` | Long text | Vì sao dừng (blocked >24h, dữ liệu mâu thuẫn, ticket tồn >7 ngày, khách phàn nàn...) |
| `resolution` | Long text | CEO quyết gì |
| `resolved` | Checkbox | |

### 2.7 `activity_log` — append-only (giữ nguyên v1)
| Field | Type |
|-------|------|
| `ts` | Created time |
| `role` | Link to `agents` |
| `job_id` | Link to `jobs` |
| `event` | Long text — 1 dòng |
| `tokens` | Number — ước lượng token của bước (Dev dùng tính P&L) |

---

## 3. Views bắt buộc

| View | Bảng | Filter/Group | Ai dùng |
|------|------|--------------|---------|
| **CEO Cockpit** | `jobs` | `status ∈ {awaiting_approval, blocked}` + `done` trong 24h; group by status | CEO — view DUY NHẤT mỗi sáng |
| Queue theo role | `jobs` | `status=queued`, group by role | OpenClaw dispatch |
| Theo client | `jobs` | group by pack | CEO khi họp với khách/tự review domain |
| KPI tuần này | `kpis` | `week = tuần hiện tại` | Weekly review |
| Chờ duyệt | `approvals` | `status=pending` | OpenClaw nhắc Telegram |

---

## 4. Job lifecycle — ai làm gì ở mỗi bước

```
① CEO nhắn Telegram: "/job [PACK: trum-san-bay] role=content P1 due=T5 — <brief 5 phần>"
     └→ OpenClaw parse → tạo row `jobs` status=queued
② OpenClaw dispatch tick (rhythm): lấy queued theo priority
     └→ fetch role pack + EXPERT-CORE section + Domain Pack → delegate xuống runtime
     └→ set status=doing, log activity
③ Runtime chạy xong → push artifact lên repo → điền output_url → status=review
④ Review chéo (bảng mục 5) → reviewer note vào job
     └→ đạt: hành động không rủi ro → status=done
     └→ đạt + hành động rủi ro (đăng/gửi/chi tiền) → tạo `approvals` → status=awaiting_approval
     └→ không đạt: về doing kèm note — tối đa 1 vòng sửa, còn cấn đẩy escalations
⑤ OpenClaw gửi Telegram: "⚠️ [job-12] media xin duyệt: đăng TikTok <link preview>. OK 12 / NO 12"
     └→ "OK 12" → approved → thực thi thật → log → done
     └→ "NO 12" → rejected → về doing kèm note
     └→ im lặng 24h → expired → KHÔNG thực thi, nhắc đúng 1 lần
⑥ Blocked >24h hoặc lặp lỗi 3 lần → role tự tạo `escalations` → lên Morning Brief hôm sau
```

Quy tắc sắt (không đổi từ v1):
- **Không có approved record = không thực thi.** Kể cả CEO nói miệng ở chỗ khác.
- Action trong approval là bản CUỐI — duyệt xong không sửa nội dung rồi mới gửi.
- Mọi thực thi thật → ghi `activity_log` ngay.

---

## 5. Handoff 5 phần + review chéo (giữ nguyên v1)

Format brief bắt buộc: `[PACK]` `[FROM/TO/TASK]` + CONTEXT / YÊU CẦU / INPUT KÈM / DEADLINE / DONE=.
Thiếu → bên nhận hỏi đúng 1 câu.

| Output từ | Reviewer | Check |
|-----------|----------|-------|
| Content | Research | Claim có nguồn |
| Designer | Content | Đúng thông điệp + brand voice theo PACK |
| Media (lịch đăng) | Marketing | Đúng kênh, tần suất, project |
| Sales (outreach) | Marketing | Đúng định vị, giá theo PACK |
| Marketing (plan chi tiền) | Research | Số liệu nền có thật |
| Ops & Finance (sổ tuần) | Research | Số khớp activity_log + nguồn thu |
| Dev (hạ tầng) | — | Checklist infra-ops-agent |

---

## 6. Code mẫu Hermes (urllib — giữ pattern v1, đổi tên bảng)

```python
import urllib.request, urllib.parse, json, os

AT_TOKEN = os.environ["AIRTABLE_TOKEN"]   # env var, không hardcode
BASE = os.environ["AIRTABLE_BASE_HQ"]

def at(table, method="GET", record=None, payload=None):
    url = f"https://api.airtable.com/v0/{BASE}/{table}"
    if record: url += f"/{record}"
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {AT_TOKEN}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

# Lấy job queued của role mình theo priority
q = urllib.parse.quote("AND({role}='content',{status}='queued')")
jobs = at(f"jobs?filterByFormula={q}&sort%5B0%5D%5Bfield%5D=priority")

# Ghi log sau mỗi bước đáng kể
at("activity_log", "POST", payload={"records":[{"fields":{
    "event":"Draft xong script video Fast Track, chờ review Research"}}]})
```

**Chống prompt injection (guardrail bắt buộc):** job nào có scraped content đầu vào (web, comment,
email khách) → flow do CODE quyết (state machine trong Hermes script), LLM chỉ xử lý từng bước
đóng khung — không bao giờ để nội dung scrape điều khiển bước tiếp theo hoặc sinh lệnh gọi tool.

---

## 7. Domain Pack switching — chống lẫn client (giữ nguyên v1)

1. Mọi message/job có `[PACK: <slug>]` — không có thì không chạy.
2. Đổi pack giữa phiên → dòng đầu output xác nhận `Đang làm việc trên PACK: <slug>`.
3. Tên file output có slug: `report-<slug>-<topic>.md`.
4. Không copy context pack này sang output pack khác.


---

## Addendum — Resolution path cho escalation kiến trúc (thêm 25/07/2026)

Với `escalations` mang tính kiến trúc/thiết kế (không phải blocked job thường) — CEO có thể
đưa qua **Senior Advisor** (`agents/company/SENIOR-ADVISOR.md`) trước khi tự quyết, lấy phương
án rồi mới approve. Giai đoạn 2 (chưa build): Hermes tự động route các escalation loại này qua
Claude API thay vì đợi CEO paste thủ công.
