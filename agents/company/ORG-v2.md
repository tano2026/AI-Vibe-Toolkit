---
name: org-v2
description: Org design v3 — công ty 1 người kiểu TQ, CEO Nobitano + 9 agent AI THẬT (khớp agents/__init__.py), mỗi role có JD/KPI/SOP/escalation
version: 3.0
replaces: agents/company/ORG.md, ORG-v2.md v2.2 (bảng 10-role lý thuyết)
supersedes_reason: >
  v2.2 (10 role) là thiết kế lý thuyết, chưa từng khớp code thật đang chạy. Audit Claude Code
  25/07/2026 xác nhận agent-core (Local Windows) chỉ có 9 agent thật, cấu trúc khác v2.2 ở 4
  điểm. Xem UNIFIED-ARCHITECTURE.md (nguồn audit) + CHANGELOG-DECISIONS.md (quyết định
  28/07/2026: theo audit thật, không theo lý thuyết).
updated: 2026-07-28
---

# ORG v3 — Công ty 1 người vận hành bằng Agent (khớp code thật)

> Thay thế `ORG.md` (v1) và bảng 10-role của `ORG-v2.md` v2.2. Entry point cho toàn bộ mô hình
> One-Person Company. Đọc kèm: `UNIFIED-ARCHITECTURE.md` (nguồn audit — đọc TRƯỚC file này nếu
> có xung đột), `COORDINATION-v2.md`, `OPERATING-RHYTHM.md`, `DECISION-MATRIX.md`.
> Nguyên tắc không đổi: **domain-agnostic core + Domain Pack cắm thêm + 3 runtime thật.**

---

## TL;DR

Công ty = **AI Agency cung cấp dịch vụ đầy đủ phòng ban**. Mỗi business domain (ABTRIP/An Bình,
Trùm Sân Bay, Tano Cafe, Airfare Decoded, GMSP, kênh AI review) = 1 **client đặt dịch vụ**, chạy
trên cùng bộ máy qua Domain Pack. CEO (Nobitano, con người duy nhất) ra quyết định qua Telegram;
**9 agent thật** (đúng agents/__init__.py, agent-core) làm toàn bộ chuyên môn 24/7.

Chuẩn "nhân viên AI" kiểu TQ (mỗi agent BẮT BUỘC đủ 4 thứ, thiếu 1 = chưa được nhận việc):
1. **JD** — job-to-be-done + ranh giới (không làm gì)
2. **KPI** — 1-2 số đo được, review hàng tuần
3. **SOP** — quy trình chuẩn cho việc lặp lại (lưu bảng sops trong Airtable)
4. **Escalation rule** — khi nào dừng và gọi CEO

---

## 9 agent thật — nguồn chân lý (copy từ UNIFIED-ARCHITECTURE.md, gốc agents/__init__.py)

| # | Agent | JD (job-to-be-done) | Task types |
|---|---|---|---|
| 0 | ceo 🧠 | Nhận lệnh, phân tích, giao việc, theo dõi tiến độ, báo cáo — đây là tầng "Hermes" vận hành, không ngang hàng 8 agent dưới | plan, delegate, status, daily-briefing |
| 1 | research 🔬 | Nghiên cứu thị trường, phân tích ngách, fact-check, đối thủ, xu hướng | research, deep-dive, fact-check, niche, video, trend-analysis |
| 2 | dev 🔧 | Code/deploy, fix bug, hạ tầng + healthcheck/monitor/backup, review | build, review, scan, deploy, fix |
| 3 | sales 💰 | Lead-gen, CSKH TRƯỚC bán, outreach, proposal, pipeline | lead-gen, outreach, proposal, market-intel |
| 4 | marketing 📢 | Content đa kênh (viết + chiến lược, gộp Content Creator), SEO, campaign, calendar, trend | content, seo, campaign, social |
| 5 | media 🎬 | Thiết kế, hình ảnh, video, storyboard, format check, brand asset, ĐĂNG (guardrail người-tạo≠người-đăng qua approval gate, không tách agent) | render, footage-search, format-check, storyboard |
| 6 | operations ⚙️ | Healthcheck hạ tầng KHÔNG còn ở đây (chuyển sang dev) — giờ CHỈ: đơn/booking/lịch (Fast Track, Tano Cafe) + ca trực/nhân sự cơ bản (extension pack HR&Admin, xem dưới) + tự động hoá | fulfillment, scheduling, hr-basic |
| 7 | support 🎫 | CSKH 24/7 SAU bán, KB/FAQ, ticket, escalate | ticket, kb-search, kb-ingest, faq-gen, escalate |
| 8 | analytics 📊 | Doanh thu, KPI, dashboard, trend/anomaly, forecast, SWOT — nơi nạp 3 skill tư duy tài chính (ops-finance.md, tu-duy-tai-chinh-vi-mo.md, tu-duy-tai-chinh-phat-trien-ban-than.md) | sql-query, report, dashboard, data-audit, swot, sentiment, forecast, kpi |

4 điểm lệch với thiết kế lý thuyết cũ (v2.2), đã quyết — xem chi tiết CHANGELOG-DECISIONS.md
entry 28/07/2026:

| Điểm lệch | Lý thuyết cũ (v2.2) | Thật (v3, giữ) |
|---|---|---|
| Research vs Analytics | Gộp 1 role | Tách 2 agent — code đã tách sẵn |
| Marketing vs Content | Tách 2 role | Gộp vào marketing — code đã gộp |
| Designer vs Media | Tách 2 role | Chỉ media, guardrail qua approval gate không qua tách agent |
| Ops&Finance vs Dev-healthcheck | Tách 2 role | Healthcheck → dev; đơn hàng/ca trực → operations (đổi tên/phạm vi) |

## Gap thật — không phải agent riêng, là extension pack nạp vào agent có sẵn

HR & Admin — KHÔNG phải agent thứ 10. Nạp vào operations khi task chạm ca trực/nhân sự
(package: roles/hr-admin.md, đổi vai trò từ "role pack độc lập" thành "extension pack"). Lý
do: khối lượng HR hiện tại (ca trực Fast Track, nhân viên Tano Cafe) chưa đủ lớn để cần agent
riêng — build/maintain 1 agent mới tốn hơn lợi ích lúc này. Tách thành agent riêng khi khối
lượng tăng (nhiều ca trực/tuyển dụng thường xuyên).

Legal & Compliance — KHÔNG phải agent thứ 10. Nạp vào sales khi task chạm hợp đồng B2B/NDA
(package: roles/legal-compliance.md, đổi vai trò tương tự) — lý do: hợp đồng B2B (ground
handling ABTRIP) thường phát sinh cùng lúc với deal, sales là agent tiếp xúc đối tác đầu tiên,
hợp lý hơn tạo agent riêng cho khối lượng còn nhỏ.

---

## Sơ đồ tổ chức v3

```
              CEO — Nobitano (con người, quyết định cuối)
                          |  ra lệnh qua Telegram (CEO Bot)
                          v
                  agent "ceo" (Hermes — bộ não, quyết định + dispatch)
                          |  giao task đã duyệt mức (DECISION-MATRIX.md)
                          v
   research  dev  sales  marketing  media  operations(+HR ext.)  support  analytics
                          |
                          v
             OpenClaw = TAY CHÂN thực thi (KHÔNG tự quyết, không kênh nhận lệnh riêng)
             Antigravity = hạ tầng VPS
                          |
                          v
   Shared workspace:
   - Repo AI-Vibe-Toolkit = artifacts
   - Airtable company-hq = state (jobs / agents / sops / kpis / approvals / escalations / log)
```

---

## Bảng phân công v3 — agent × runtime × LLM tier × domain

Tier OmniRoute: cheap (DeepSeek V3) · balanced (Gemini Flash) · reasoning (DeepSeek R1)
· creative (Claude Sonnet — CHỈ khi chất lượng chữ quyết định kết quả). Xem
LOOP-TOKEN-GOVERNOR.md cho pick_tier() đầy đủ theo risk_level.

| # | Agent | Package tham chiếu | Runtime | LLM tier mặc định | Domain phục vụ | KPI chính (weekly) |
|---|---|---|---|---|---|---|
| 1 | research | agents/research-pro.md + research-analytics-pro/ | ceo (Hermes) | reasoning | TẤT CẢ | Số insight report được agent khác dùng (cited) |
| 2 | dev | HERMES-PLAYBOOK.md + OPENCLAW-PLAYBOOK.md + ANTIGRAVITY-PLAYBOOK.md + infra-ops-agent/ | Cả 3 runtime | balanced | Hạ tầng + tool + healthcheck cho 8 agent | Uptime 3 runtime + ticket tồn <7 ngày |
| 3 | sales | agents/sales-ceo/system-prompt.md (+ ext. roles/legal-compliance.md) | ceo + OpenClaw | balanced (reasoning khi chạm hợp đồng) | ABTRIP/An Bình, dịch vụ Tano Agency | Số deal chốt + pipeline value + 100% hợp đồng sàng lọc trước ký |
| 4 | marketing | roles/marketing.md + roles/content-creator.md (gộp) | ceo + OpenClaw | creative (content) / balanced (SEO/ads) | Trùm Sân Bay, Airfare Decoded, GMSP, kênh AI review | Lead/traffic vs target + content ready-to-publish đúng hạn |
| 5 | media | roles/media.md + roles/designer.md (gộp) | OpenClaw | creative (design) / cheap (đăng) | Mọi kênh social/YouTube | Số visual đúng spec + số bài đăng đúng lịch |
| 6 | operations | roles/ops-finance.md (fulfillment) + ext. roles/hr-admin.md | ceo | cheap→balanced (reasoning khi tranh chấp lao động) | ABTRIP/An Bình, Tano Cafe, Fast Track (ca trực) | Đơn xử lý <SLA + % ca trực đủ người |
| 7 | support | (chưa có role pack riêng — viết khi cần) | OpenClaw | cheap | Mọi domain có khách hàng sau bán | Ticket resolve <SLA |
| 8 | analytics | 3 skill tài chính: ops-finance.md (DCF) + tu-duy-tai-chinh-vi-mo.md + tu-duy-tai-chinh-phat-trien-ban-than.md | ceo | reasoning | TẤT CẢ | Báo cáo KPI/forecast đúng hạn tuần |

Luật routing tier (tiết kiệm là P&L trực tiếp): mặc định theo bảng trên; nâng tier chỉ khi
task ghi rõ lý do trong brief; log token theo job (bảng activity_log). Mục tiêu giữ nguyên:
>80% khối lượng chạy free tier qua OmniRoute.

---

## Cách nạp agent (pattern proven, không đổi)

ceo (Hermes) fetch 3 file: package tham chiếu + section agent trong EXPERT-CORE.md +
Domain Pack → embed vào delegation message → agent hành xử theo JD trong phiên đó. Không
process mới, không deploy thêm. Extension pack (HR&Admin, Legal&Compliance) nạp THÊM vào
operations/sales khi task khớp — không phải nạp mặc định mọi lần.

## Nhân bản cho client mới (quy trình 30 phút)

1. Copy domain-packs/_TEMPLATE.md → domain-packs/<client-slug>/PACK.md, điền brand context
   + constraints + glossary + design tokens.
2. Tạo view lọc pack = <client-slug> trong Airtable jobs + thêm dòng KPI target vào kpis.
3. Job đầu tiên luôn là: [PACK: <slug>] agent=research — scan thị trường + đối thủ + kênh.
   Không agent nào được chạy trước khi Research nộp báo cáo nền.

Lõi 9 agent KHÔNG sửa khi thêm client. Sửa lõi = thay đổi công ty, phải qua CEO.

## Ma trận tự chủ

Chuyển toàn bộ sang DECISION-MATRIX.md (4 mức L0-L3 theo trục rủi ro). Ba lằn ranh đỏ
không bao giờ đổi: AI không tự chi tiền, không tự publish public, không tự cam kết với khách.

---

## Addendum — Tier cố vấn ngoài 9 agent (giữ nguyên từ v2.2)

9 agent ở trên là runtime-embedded, chạy qua Airtable jobs queue. Bên cạnh đó có 1 tier riêng
Senior Advisor (Claude, Project Chat) — không phải agent thứ 10, không chạy runtime, chỉ tư
duy thiết kế + viết file khi cần quyết định kiến trúc hoặc skill mới. Chi tiết:
agents/company/SENIOR-ADVISOR.md.

## Lịch sử phiên bản

- v1 (ORG.md) — 7 role lý thuyết ban đầu.
- v2.0-v2.2 — thêm Ops&Finance, HR&Admin, Legal&Compliance — toàn bộ lý
  thuyết, chưa đối chiếu code thật.
- v3.0 (file này) — viết lại theo audit thật agents/__init__.py (25/07/2026), quyết định
  chốt 28/07/2026 (xem CHANGELOG-DECISIONS.md): giữ 9 agent thật, HR&Admin/Legal&Compliance
  chuyển từ "role độc lập" thành "extension pack" nạp vào operations/sales.
