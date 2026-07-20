---
name: org-v2
description: Org design v2 — công ty 1 người kiểu TQ, CEO Nobitano + 8 nhân viên AI, mỗi role có JD/KPI/SOP/escalation
version: 2.0
replaces: agents/company/ORG.md
updated: 2026-07-19
---

# ORG v2 — Công ty 1 người vận hành bằng Agent

> Thay thế `ORG.md` (v1). Entry point cho toàn bộ mô hình One-Person Company.
> Đọc kèm: `COORDINATION-v2.md` (state + handoff), `OPERATING-RHYTHM.md` (nhịp chạy),
> `DECISION-MATRIX.md` (ai quyết gì).
> Nguyên tắc không đổi: **domain-agnostic core + Domain Pack cắm thêm + 3 runtime thật.**

---

## TL;DR

Công ty = **AI Agency cung cấp dịch vụ đầy đủ phòng ban**. Mỗi business domain
(ABTRIP/An Bình, Trùm Sân Bay, Tano Cafe, Airfare Decoded, GMSP, kênh AI review) = 1 **client
đặt dịch vụ**, chạy trên cùng bộ máy qua Domain Pack. CEO (Nobitano, con người duy nhất)
ra quyết định qua Telegram; 8 nhân viên AI làm toàn bộ chuyên môn số hoá 24/7, cộng thêm
1 role ⑨ quản lý con người thật (nhân sự có hợp đồng, ca trực) — 9 vị trí tổng cộng.

Chuẩn "nhân viên AI" kiểu TQ (mỗi role BẮT BUỘC đủ 4 thứ, thiếu 1 = chưa được nhận việc):
1. **JD** — job-to-be-done + ranh giới (không làm gì)
2. **KPI** — 1-2 số đo được, review hàng tuần
3. **SOP** — quy trình chuẩn cho việc lặp lại (lưu bảng `sops` trong Airtable)
4. **Escalation rule** — khi nào dừng và gọi CEO

---

## Rà soát 7 role v1 → kết luận v2

| Role v1 | Phán quyết | Lý do |
|---------|-----------|-------|
| ① Research & Analytics | ✅ Giữ nguyên | Đầu vào cho mọi role, đã proven (RIO) |
| ② Marketing | ✅ Giữ nguyên | Ranh giới rõ: chiến lược + kênh + tiền ads |
| ③ Sales | ✅ Giữ, mở rộng JD | Nhận thêm CSKH TRƯỚC bán (tư vấn, báo giá). CSKH SAU bán → Ops |
| ④ Content Creator | ✅ Giữ nguyên | Chồng chéo với Designer/Media chỉ là bề mặt — pack đã chia ranh giới chữ / hình / đăng rất rõ. Gộp lại sẽ mất separation of duties (người tạo ≠ người đăng = guardrail chống đăng bậy) |
| ⑤ Dev & Automation | ✅ Giữ nguyên | Xương sống, charter 4 mảng đã chuẩn |
| ⑥ Designer | ✅ Giữ nguyên | Như ④ |
| ⑦ Media | ✅ Giữ nguyên | Là role duy nhất cầm quyền "bấm đăng" — phải đứng riêng |
| **⑧ Ops & Finance** | 🆕 **THÊM MỚI** | Lỗ hổng lớn nhất v1: không ai fulfillment đơn (Fast Track booking, đơn Tano Cafe), không ai đếm tiền. Công ty không có sổ thu chi theo domain = không biết job nào lãi job nào lỗ = không bền vững. Pack: `roles/ops-finance.md` |
| **⑨ HR & Admin** | 🆕 **THÊM v2.1 — 20/07/2026** | Job-to-be-done KHÁC HẲN 8 role trên: 8 role kia đều là AI phối hợp AI xử lý việc số; ⑨ quản lý CON NGƯỜI THẬT — nhân viên ca trực Fast Track, nhân viên Tano Cafe, cộng tác viên thuê ngoài. Có hợp đồng thật, tranh chấp lao động thật, nghĩa vụ pháp lý thật — không role nào trong 8 role kia đảm nhiệm được. Đây là lý do duy nhất được phép phá vỡ kết luận "8 role, không option" ở trên: khác job-to-be-done, không phải mở rộng phạm vi 1 role cũ. Pack: `roles/hr-admin.md` |

**Kết luận v2.1: 9 role — 8 role AI-coordination (không gộp, không bỏ) + 1 role quản lý người
thật (HR & Admin).** Nếu sau này có đề xuất thêm role AI-coordination thứ 10 trở lên → mặc định
từ chối trừ khi chứng minh được job-to-be-done không trùng bất kỳ role nào trong 9 role hiện có
VÀ không thể gộp vào role sẵn có.

---

## Sơ đồ tổ chức v2

```
              CEO — Nobitano (con người, quyết định cuối)
                          │ duyệt qua Telegram: "OK <job-id>"
                          ▼
             ┌──────────────────────────┐
             │  OpenClaw = Điều phối     │ Telegram/WhatsApp gateway
             │  (dispatcher + gateway)   │ route job → role → runtime
             └────────────┬─────────────┘
   ┌─────┬─────┬─────┬────┼────┬─────┬─────┬─────┐
   ▼     ▼     ▼     ▼    ▼    ▼     ▼     ▼     ▼
Research Mkt Sales Content Designer Media Ops&Fin HR&Admin  (9 nhân viên AI)
   └─────┴─────┴─────┴────┬────┴─────┴─────┴─────┘
                          ▼
             Dev & Automation (tầng nền, phục vụ 7 role kia)
             = Hermes + OpenClaw + Antigravity
                          │
                          ▼
   ┌────────────────────────────────────────┐
   │ Shared workspace:                       │
   │ • Repo AI-Vibe-Toolkit = artifacts      │
   │ • Airtable `company-hq` = state         │
   │   (jobs / agents / sops / kpis /        │
   │    approvals / escalations / log)       │
   └────────────────────────────────────────┘
```

---

## Bảng phân công v2 — role × runtime × LLM tier × domain

Tier OmniRoute: `cheap` (Gemini Flash) · `balanced` (DeepSeek V3) · `reasoning` (DeepSeek R1)
· `creative` (Claude Sonnet — CHỈ khi chất lượng chữ quyết định kết quả).

| # | Role | Role Pack | Runtime | LLM tier mặc định | Domain phục vụ | KPI chính (weekly) |
|---|------|-----------|---------|-------------------|----------------|--------------------|
| ① | Research & Analytics | `agents/research-pro.md` + `agents/research-analytics-pro/` | Hermes | reasoning | TẤT CẢ | Số insight report được role khác dùng (cited) |
| ② | Marketing | `roles/marketing.md` | Hermes + OpenClaw | balanced | TẤT CẢ | Lead/traffic theo domain vs target |
| ③ | Sales | `agents/sales-ceo/system-prompt.md` | Hermes + OpenClaw | balanced | ABTRIP/An Bình, dịch vụ Tano Agency | Số deal chốt + pipeline value |
| ④ | Content Creator | `roles/content-creator.md` | Hermes | creative | Trùm Sân Bay, Airfare Decoded, GMSP, kênh AI review | Số content ready-to-publish đúng hạn |
| ⑤ | Dev & Automation | `HERMES-PLAYBOOK.md` + `OPENCLAW-PLAYBOOK.md` + `ANTIGRAVITY-PLAYBOOK.md` + `infra-ops-agent/` | Cả 3 | balanced (coding) | Hạ tầng + tool cho 7 role | Uptime 3 runtime + ticket tồn <7 ngày |
| ⑥ | Designer | `roles/designer.md` | Hermes + OpenClaw | creative | TẤT CẢ | Số visual đúng spec, số template tái dùng |
| ⑦ | Media | `roles/media.md` | OpenClaw | cheap | Mọi kênh social/YouTube | Số bài đăng đúng lịch + engagement delta |
| ⑧ | Ops & Finance | `roles/ops-finance.md` 🆕 | Hermes | cheap→balanced | ABTRIP/An Bình, Tano Cafe (+ mọi domain có tiền vào) | Đơn xử lý <SLA + sổ thu chi cập nhật 100% |
| ⑨ | HR & Admin | `roles/hr-admin.md` 🆕 v2.1 | Hermes | balanced→reasoning (case quan hệ lao động) | Fast Track (ca trực), Tano Cafe (nhân viên) | % ca trực đủ người + hồ sơ nhân sự cập nhật 100% |

**Luật routing tier (tiết kiệm là P&L trực tiếp):** mặc định theo bảng trên; nâng tier chỉ khi
task ghi rõ lý do trong brief; log token theo job (bảng `activity_log`). Mục tiêu giữ nguyên:
>80% khối lượng chạy free tier qua OmniRoute.

---

## Cách nạp role (pattern proven, không đổi)

OpenClaw fetch 3 file: **role pack + section role trong `EXPERT-CORE.md` + Domain Pack** → embed
vào delegation message → runtime hành xử theo role trong phiên đó. Không process mới, không
deploy thêm. Mọi delegation mở đầu `[PACK: <slug>]` — thiếu là không chạy.

## Nhân bản cho client mới (quy trình 30 phút)

1. Copy `domain-packs/_TEMPLATE.md` → `domain-packs/<client-slug>/PACK.md`, điền brand context
   + constraints + glossary + design tokens.
2. Tạo view lọc `pack = <client-slug>` trong Airtable `jobs` + thêm dòng KPI target vào `kpis`.
3. Job đầu tiên luôn là: `[PACK: <slug>] role=research — scan thị trường + đối thủ + kênh`.
   Không role nào được chạy trước khi Research nộp báo cáo nền.

Lõi 8 role KHÔNG sửa khi thêm client. Sửa lõi = thay đổi công ty, phải qua CEO.

## Ma trận tự chủ

Chuyển toàn bộ sang `DECISION-MATRIX.md` (4 mức L0-L3 theo trục rủi ro). Ba lằn ranh đỏ
không bao giờ đổi: **AI không tự chi tiền, không tự publish public, không tự cam kết với khách.**
