---
name: operating-rhythm
description: Nhịp vận hành công ty 1 người — daily/weekly rhythm, cron schedule cho Antigravity, report format
version: 1.0
updated: 2026-07-19
---

# OPERATING RHYTHM — Nhịp vận hành công ty

> Đọc kèm: `ORG-v2.md`, `COORDINATION-v2.md`, `DECISION-MATRIX.md`.
> Nguyên tắc: **CEO nhìn 1 dashboard + nhận ~3 message Telegram/ngày. Còn lại tự chạy.**
> Giờ trong file = giờ VN (UTC+7). Cron trên VPS chỉnh theo timezone máy.

---

## 1. Daily rhythm

| Giờ | Việc | Ai chạy | Output về đâu |
|-----|------|---------|---------------|
| 06:45 | Healthcheck 3 runtime (pm2 status, disk, RAM) | Antigravity | CHỈ nhắn Telegram khi có fail — khỏe thì im lặng |
| 07:00 | **Morning Brief** — quét Airtable, tổng hợp | OpenClaw | Telegram CEO (format mục 3) |
| 08:00 | Research daily scan: trend/đối thủ của domain active (xoay vòng theo thứ) | Hermes (research) | Report .md → repo, insight đáng chú ý → thêm vào brief mai |
| 09:00 | Dispatch tick #1 — phát job queued theo priority | OpenClaw | activity_log |
| 14:00 | Dispatch tick #2 + nhắc approvals pending sắp expired | OpenClaw | Telegram nếu có pending |
| 18:00 | Media pull số engagement các kênh (TikTok/YT) | Hermes (media) | Cập nhật `kpis.actual` |
| 20:00 | Dispatch tick #3 (job P2, việc nền) | OpenClaw | activity_log |
| 21:00 | **EOD Report** — chốt ngày | OpenClaw | Telegram CEO: `Hôm nay: X done / Y doing / Z blocked / N chờ duyệt (list id)` — ≤10 dòng |

Lịch xoay vòng Research scan: T2 abtrip+an-binh · T3 trum-san-bay · T4 airfare-decoded ·
T5 gmsp · T6 ai-review · T7 tổng hợp đối thủ · CN nghỉ scan (chạy weekly report).

## 2. Weekly rhythm

| Thời điểm | Việc | Ai | Output |
|-----------|------|-----|--------|
| T2 08:00 | **KPI Review** — bảng `kpis` tuần trước: actual vs target từng role, từng pack | OpenClaw tổng hợp | Telegram: bảng ≤8 dòng + role nào <70% target kèm note |
| T2 08:00 | Đề xuất priority tuần: 3 job quan trọng nhất | OpenClaw đề xuất, CEO chốt | CEO reply chốt trong Telegram |
| T6 16:00 | Content calendar tuần sau (mọi kênh) → chờ CEO duyệt 1 lần cả lô | Content + Media | 1 approval duy nhất dạng batch |
| CN 20:00 | Weekly report .md theo pack + theo role, kèm tổng token usage (P&L) | Hermes | Push `/reports/` trong repo — CEO đọc khi cần |
| CN 20:30 | Ops & Finance chốt sổ tuần: thu/chi theo domain | Hermes (ops-finance) | Dòng chốt vào Morning Brief T2 |

**Số PHẢI có trên bàn CEO sáng T2 (5 con số, không hơn):**
1. Tiền vào tuần trước theo domain (Ops & Finance)
2. Số job done / tổng job (throughput)
3. KPI role nào đỏ (<70% target)
4. Token usage & % chạy free tier (Dev)
5. 3 job đề xuất ưu tiên tuần này

## 3. Format Morning Brief (07:00 — 1 message duy nhất)

```
☀️ 19/07 — TANO HQ
💰 Chờ duyệt (N): [12] media đăng TikTok TSB · [15] sales gửi báo giá An Bình
🔴 Blocked (N): [9] dev — VPS thiếu RAM (escalated)
✅ Done hôm qua: 4 job (chi tiết trong Cockpit)
📊 Nhịp: 6 doing / 3 queued
👉 Cần mày: OK/NO 12, 15 · quyết escalation [9]
```

Luật: ≤12 dòng. Không có gì cần duyệt + không blocked → brief 3 dòng. Link Cockpit ở cuối.

## 4. Cron schedule cho Antigravity (paste-ready)

Antigravity deploy các dòng sau (crontab user chạy pm2; script nằm `/opt/tano/cron/`):

```cron
# ── TANO HQ operating rhythm (giờ VN) ──
45 6 * * *  /opt/tano/cron/healthcheck.sh
0  7 * * *  node /opt/tano/openclaw/jobs/morning-brief.js
0  8 * * *  python3 /opt/tano/hermes/jobs/research_daily_scan.py
0  9 * * *  node /opt/tano/openclaw/jobs/dispatch-tick.js --slot=1
0 14 * * *  node /opt/tano/openclaw/jobs/dispatch-tick.js --slot=2
0 18 * * *  python3 /opt/tano/hermes/jobs/media_pull_metrics.py
0 20 * * *  node /opt/tano/openclaw/jobs/dispatch-tick.js --slot=3
0 21 * * *  node /opt/tano/openclaw/jobs/eod-report.js
# ── weekly ──
0  8 * * 1  node /opt/tano/openclaw/jobs/kpi-review.js
0 16 * * 5  node /opt/tano/openclaw/jobs/content-calendar-reminder.js
0 20 * * 0  python3 /opt/tano/hermes/jobs/weekly_report.py
30 20 * * 0 python3 /opt/tano/hermes/jobs/ops_finance_close_week.py
```

Yêu cầu cho từng script: đọc env var (`AIRTABLE_TOKEN`, `AIRTABLE_BASE_HQ`, `TELEGRAM_*`),
log ra file riêng `/opt/tano/logs/<tên>.log`, fail thì exit code ≠0 để healthcheck bắt được.
Mỗi cron mới = 1 automation theo luật Dev charter: có owner, có log, có cách tắt khẩn cấp
(comment dòng cron là đủ).

## 5. Quy tắc ra quyết định

Toàn bộ chuyển sang `DECISION-MATRIX.md` — 4 mức L0-L3 theo trục rủi ro
(tiền / public content / cam kết khách / hạ tầng / dữ liệu). Rhythm chỉ cần nhớ:
**mọi thứ cần CEO đều phải xuất hiện trong Morning Brief hoặc message duyệt — CEO không bao giờ
phải tự mở Airtable để phát hiện việc cần quyết.**
