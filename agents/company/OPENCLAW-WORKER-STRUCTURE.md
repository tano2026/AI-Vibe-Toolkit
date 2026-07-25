---
name: openclaw-worker-structure
description: Cấu trúc thư mục agent worker trên OpenClaw VPS — bản sửa, khớp 9 role trong ORG-v2.md. Thay thế đề xuất 8-folder ban đầu (gộp sai role, thiếu Ops&Finance thật và HR&Admin).
version: 1.0
updated: 2026-07-25
supersedes: đề xuất "3 bước" ban đầu của OpenClaw (2026-07-25, gộp marketing/content, media/designer, ops/support sai)
---

# OpenClaw Worker Structure — Bản sửa khớp ORG-v2

> Đọc kèm: `agents/company/ORG-v2.md` (nguồn chân lý duy nhất về 9 role),
> `agents/company/DECISION-MATRIX.md`, `agents/company/SENIOR-ADVISOR.md`.
> File này thay bản đề xuất gốc — giữ nguyên Bước 1 (dọn workspace, không liên quan cấu trúc
> role), sửa Bước 2 (worker folder) và Bước 3 (Claude không phải worker).

---

## Bước 1 — Dọn workspace VPS (giữ nguyên như đề xuất gốc)

Giữ lại: MCP servers, TANO-AGENCY, AI-Vibe-Toolkit, flight-booking-webapp.
Xóa: screenshot, test file v1-v9, abtrip_dump*, debug scripts.
Gom: project phụ vào `archive/`.

**Trước khi xoá gì:** `git pull origin main` trong thư mục AI-Vibe-Toolkit trên VPS để đảm bảo
đang đọc bản kho mới nhất (đã có ORG-v2.md, SENIOR-ADVISOR.md, FOCUS-MODE.md, local-gap-finder).

## Bước 2 — Build agent workers: ĐÚNG 9 folder, không gộp

```
/opt/openclaw/agents/
├── research/        ← ① Research & Analytics — insight, không phải KPI report
├── marketing/        ← ② Marketing — chiến lược kênh + tiền ads
├── sales/             ← ③ Sales — deal + CSKH TRƯỚC bán (đã mở rộng JD trong ORG-v2)
├── content/           ← ④ Content Creator — TÁCH RIÊNG khỏi marketing
├── dev/               ← ⑤ Dev & Automation — code, deploy, healthcheck, schedule (Antigravity job nằm ở đây, không phải "ops")
├── designer/          ← ⑥ Designer — TÁCH RIÊNG khỏi media
├── media/             ← ⑦ Media — CHỈ role được quyền bấm đăng thật (guardrail: người tạo ≠ người đăng)
├── ops-finance/       ← ⑧ Ops & Finance — fulfillment đơn (Fast Track, Tano Cafe) + CSKH SAU bán + sổ thu chi
└── hr-admin/          ← ⑨ HR & Admin — nhân viên ca trực Fast Track, nhân viên Tano Cafe (THIẾU trong đề xuất gốc)
```

**3 điểm sửa quan trọng so với đề xuất gốc:**
1. `marketing/` và `content/` là 2 folder riêng — không gộp. Lý do: ORG-v2 tách có chủ đích.
2. `media/` và `designer/` là 2 folder riêng — không gộp. Lý do: guardrail "người tạo ≠ người
   đăng" — gộp lại nghĩa là 1 worker vừa tạo vừa tự đăng, mất lớp kiểm soát trước khi lên public.
3. `ops-finance/` = đơn hàng + tiền (đúng JD role ⑧), KHÔNG phải healthcheck/schedule — cái đó
   thuộc `dev/` (Antigravity). "support/" không tồn tại độc lập — CSKH trước bán nằm trong
   `sales/`, CSKH sau bán nằm trong `ops-finance/`.

Mỗi worker Python nhận task từ Hermes theo đúng pattern đã có: fetch role pack
(`agents/company/roles/<role>.md`) + section trong `EXPERT-CORE.md` + Domain Pack → chạy.

## Bước 3 — Senior Advisor: KHÔNG phải worker thứ 10

Không tạo `claude/` trong `/opt/openclaw/agents/`. Senior Advisor không nhận task qua hàng đợi
như 9 worker trên — chi tiết đầy đủ: `agents/company/SENIOR-ADVISOR.md`.

**Đúng cách wire (giai đoạn 2, chưa build):**
```
Hermes phát hiện điều kiện escalate (SENIOR-ADVISOR.md mục "Khi nào escalate")
    → gọi Claude API qua agents/senior-advisor/invoke.py (chưa tồn tại, cần build riêng)
    → KHÔNG polling liên tục, KHÔNG watcher chạy nền
    → nhận response → Hermes tự push file kết quả lên repo
```

**Về "theo dõi ECC repo → sync skill":** chưa rõ "ECC" là repo/nguồn gì — không tìm thấy định
nghĩa trong AI-Vibe-Toolkit. Trước khi build cơ chế sync tự động, cần Nobitano xác nhận: ECC là
gì, có phải nguồn ngoài kho chính hay không. Nếu đúng là nguồn ngoài — việc "tự động sync skill
mới vào Hermes" là hành động ghi hệ thống, nên xếp mức L1 (log) theo `DECISION-MATRIX.md`, không
phải tự chạy nền vô hạn.

---

## Việc cần làm ngay (theo thứ tự)

1. `git pull` kho trên VPS
2. Dọn workspace theo Bước 1
3. Tạo đúng 9 folder Bước 2 (không phải 8)
4. KHÔNG tạo `claude/` — xoá khỏi kế hoạch nếu đã tạo
5. Hỏi lại Nobitano về "ECC" trước khi build sync skill tự động
