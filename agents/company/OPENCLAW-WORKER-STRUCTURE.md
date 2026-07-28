---
name: openclaw-worker-structure
description: Cấu trúc thư mục agent worker trên OpenClaw VPS — khớp 9 agent THẬT trong ORG-v2.md v3.0 (agent-core audit), không phải 9-role lý thuyết cũ.
version: 2.0
updated: 2026-07-28
supersedes: v1.0 (25/07/2026) mô tả 9 folder theo ORG-v2.md v2.2 lý thuyết (research/marketing/sales/content/dev/designer/media/ops-finance/hr-admin) — SAI, không khớp agent-core thật. Xem CHANGELOG-DECISIONS.md entry 28/07/2026.
---

# OpenClaw Worker Structure — Bản v2, khớp ORG-v2 v3.0 (9 agent thật)

> Đọc kèm: `agents/company/ORG-v2.md` v3.0 (nguồn chân lý duy nhất, dựa trên audit
> `agents/__init__.py`), `agents/company/UNIFIED-ARCHITECTURE.md`, `agents/company/DECISION-MATRIX.md`.
> File này thay bản v1.0 — bản đó dùng 9-role LÝ THUYẾT (ORG-v2 v2.2), không khớp code thật
> đang chạy. Giữ nguyên Bước 1 (dọn workspace), sửa lại Bước 2 (worker folder) cho đúng.

---

## Bước 1 — Dọn workspace VPS (giữ nguyên như đề xuất gốc)

Giữ lại: MCP servers, TANO-AGENCY, AI-Vibe-Toolkit, flight-booking-webapp.
Xóa: screenshot, test file v1-v9, abtrip_dump*, debug scripts.
Gom: project phụ vào `archive/`.

**Trước khi xoá gì:** `git pull origin main` trong thư mục AI-Vibe-Toolkit trên VPS để đảm bảo
đang đọc bản kho mới nhất (đã có ORG-v2.md v3.0, SENIOR-ADVISOR.md, CHANGELOG-DECISIONS.md).

## Bước 2 — Build agent workers: ĐÚNG 8 folder (không tính `ceo` — đó là Hermes/bộ não, không phải worker OpenClaw thực thi)

```
/opt/openclaw/agents/
├── research/          ← nghiên cứu thị trường, fact-check, đối thủ, xu hướng
├── dev/                ← code/deploy, fix bug, hạ tầng + healthcheck/monitor/backup
├── sales/              ← lead-gen, CSKH trước bán, proposal + ext. legal-compliance khi chạm hợp đồng B2B
├── marketing/          ← content đa kênh (gộp Content Creator) + SEO + campaign
├── media/              ← thiết kế + hình ảnh + video + ĐĂNG (approval gate, không tách agent designer riêng)
├── operations/         ← đơn/booking/lịch (Fast Track, Tano Cafe) + ext. hr-admin khi chạm ca trực/nhân sự
├── support/            ← CSKH 24/7 SAU bán, ticket, KB/FAQ
└── analytics/          ← doanh thu, KPI, dashboard, forecast, SWOT — nạp 3 skill tài chính đã có
```

**Điểm khác biệt quan trọng so với bản v1.0 (SAI, đã supersede):**
1. **KHÔNG có folder `content/` riêng** — gộp vào `marketing/` (code thật đã gộp, không tách).
2. **KHÔNG có folder `designer/` riêng** — chỉ có `media/`, guardrail "người tạo ≠ người đăng"
   xử lý qua approval gate (`DECISION-MATRIX.md`), không phải tách agent.
3. **KHÔNG có folder `ops-finance/` và `hr-admin/` riêng** — gộp thành `operations/`, HR&Admin
   là **extension pack nạp thêm** khi cần (không phải worker riêng, xem `roles/hr-admin.md`).
4. **KHÔNG có folder `hr-admin/` hay `legal-compliance/` độc lập** — Legal&Compliance là
   **extension pack nạp vào `sales/`** khi task chạm hợp đồng B2B/NDA.
5. **Có thêm folder `support/`** — không có trong bản v1.0, nhưng code thật xác nhận đây là
   agent riêng, hoạt động tốt hơn ép vào Sales/Ops.
6. **Có thêm folder `analytics/`** tách riêng khỏi `research/` — code thật xác nhận 2 agent
   riêng, không gộp.

Mỗi worker Python nhận task từ Hermes theo đúng pattern đã có: fetch package tham chiếu
(`agents/company/roles/<role>.md` hoặc file tương ứng trong bảng ORG-v2.md) + section trong
`EXPERT-CORE.md` + Domain Pack → chạy. Extension pack (`hr-admin.md`, `legal-compliance.md`)
chỉ nạp thêm khi task khớp điều kiện, không nạp mặc định.

## Bước 3 — Senior Advisor: KHÔNG phải worker thứ 9/10

Không tạo `claude/` trong `/opt/openclaw/agents/`. Senior Advisor không nhận task qua hàng đợi
như 9 worker trên — chi tiết đầy đủ: `agents/company/SENIOR-ADVISOR.md`.

**Đúng cách wire (giai đoạn 2, chưa build):**
```
Hermes phát hiện điều kiện escalate (SENIOR-ADVISOR.md mục "Khi nào escalate")
    → gọi Claude API qua agents/senior-advisor/invoke.py (chưa tồn tại, cần build riêng)
    → KHÔNG polling liên tục, KHÔNG watcher chạy nền
    → nhận response → Hermes tự push file kết quả lên repo
```

**Về "theo dõi ECC repo → sync skill" — ĐÃ XÁC ĐỊNH (25/07/2026):** "ECC" = kho skill plugin
chính thức (Anthropic maintain, ~360-459 plugin tuỳ thời điểm snapshot) — KHÔNG phải nguồn của
Nobitano, không kiểm soát được nội dung, cập nhật theo lịch riêng của Anthropic.

**Quan trọng:** trong đó có ~66/407 skill có khả năng HÀNH ĐỘNG THẬT (Twilio gửi tin, Gmail gửi
mail, Airtable/Vercel/Slack ghi dữ liệu). Đây không phải tài liệu tham khảo thuần — sync 1 skill
loại này vào Hermes = cấp thêm quyền hành động cho hệ thống.

**Quy tắc xử lý (không đổi so với DECISION-MATRIX.md):**
- Claude Advisor CHỈ **báo cáo** skill mới/đổi trong ECC (report-only), KHÔNG tự sync
- Skill loại tham khảo/đọc (docx, pdf, research, analysis...) → Nobitano duyệt 1 lần, sau đó Hermes tự import — mức L1
- Skill loại hành động thật (gửi/ghi/tiền — nhận diện qua tên plugin: twilio*, gmail, airtable
  write action, vercel deploy, slack send...) → BẮT BUỘC qua CEO duyệt trước khi wire vào bất kỳ
  role nào — mức L2 theo DECISION-MATRIX.md, không có ngoại lệ dù chỉ là "thêm 1 tool mới"
- Claude Advisor không tự động chạy nền theo dõi liên tục (giữ đúng thiết kế SENIOR-ADVISOR.md:
  không watcher, chỉ trả lời khi được hỏi hoặc escalate qua invoke.py giai đoạn 2)

---

## Việc cần làm ngay (theo thứ tự)

1. `git pull` kho trên VPS
2. Dọn workspace theo Bước 1
3. Tạo đúng 9 folder Bước 2 (không phải 8)
4. KHÔNG tạo `claude/` — xoá khỏi kế hoạch nếu đã tạo
5. Hỏi lại Nobitano về "ECC" trước khi build sync skill tự động
