# Claude Code Routines — Automation Không Cần Máy Bật, Không Cần VPS

**Feature chính thức:** claude.ai/code/routines
**Release:** 15/4/2026 — Anthropic
**Requires:** Claude Pro ($20/tháng) trở lên
**URL:** https://claude.ai/code/routines

---

## Đây Là Gì

Feature chính thức của Anthropic — Claude Code chạy **scheduled automation trên cloud của Anthropic**. Không cần máy tính bật, không cần VPS, không cần kéo node n8n.

```
Viết 1 lần → Chạy mãi mãi
```

3 bước:
1. **Prompt** — mô tả việc cần làm bằng lời
2. **Trigger** — lịch chạy (cron) hoặc webhook
3. **Cloud** — Anthropic tự chạy, tự lo

---

## Free Tier Theo Plan

| Plan | Routine runs/ngày | Giá |
|------|------------------|-----|
| Pro | 5 runs/ngày | $20/tháng |
| Max | 15 runs/ngày | $100/tháng |
| Team | 25 runs/ngày | $25/user/tháng |
| Enterprise | 25 runs/ngày | Custom |

**First run free** trên mọi paid plan.

---

## Cách Setup Routine

```
1. Vào claude.ai/code/routines
2. Click "New Routine"
3. Điền:
   - Prompt: mô tả việc cần làm
   - Connectors: GitHub, Slack, Gmail, HubSpot...
   - Schedule: mỗi ngày 8h / mỗi tuần / webhook
4. Save → chạy tự động trên cloud Anthropic
```

---

## Trigger Types

```bash
# Scheduled (cron-style)
"Every day at 08:00"
"Every Monday at 09:00"
"Every hour"
"Every 15 minutes"

# API trigger
POST https://api.anthropic.com/routines/{id}/trigger
Authorization: Bearer sk-...

# GitHub event
On: pull_request.opened
On: push to main
On: issue.created
```

---

## 15 Routine Hay Nhất (Từ Community)

### 🔧 Engineering
```
PR Review — Auto first-pass review mọi PR
On-call Digest — Hourly summary alerts đang cháy
Deploy Verification — Check health sau mỗi deploy
Flaky Test Quarantine — Detect và isolate flaky tests
i18n Drift — Detect missing translations
```

### 💰 Business & Sales
```
Meeting Brief — Prep trước mọi external meeting
Pipeline Hygiene — Daily CRM cleanup
Weekly Metrics Email — KPI email tự viết
Runway Watch — Monthly cash+burn alert
Churn Save — Detect churn signals, alert sales
```

### 📊 Marketing & Ops
```
Daily Reading Triage — Sort + summarize reading queue
Morning Brief — News + priorities digest mỗi sáng
Weekly Vault Harvest — Compile best content of week
Social Mentions Monitor — Track brand mentions
Content Calendar — Weekly content planning
```

### 🎯 Cho AI Vibe Toolkit Cụ Thể
```
Check sale Shopify mỗi sáng, báo ROAS về Telegram
Quét trend POD: Google Trends đối chiếu TikTok
SEO audit mỗi đêm, tự generate schema JSON-LD
Form khách điền, tự soạn proposal trong Google Docs
GitHub trending scan → tóm tắt → push vào kho
```

---

## Connectors Hỗ Trợ

Routines dùng cùng MCP connectors như Claude Code:

```
GitHub, GitLab, Jira, Linear (Engineering)
Slack, Gmail, Outlook, Notion, Confluence (Communication)
HubSpot, Salesforce, Pipedrive (CRM/Sales)
Google Analytics, Search Console (SEO/Analytics)
Shopify, Stripe (E-commerce)
Google Docs, Sheets, Drive (Productivity)
Telegram, Discord (Notifications)
```

---

## Template Prompt Chuẩn

Structure prompt hiệu quả cho Routines:

```markdown
## Context
[Mày làm gì, dùng tool nào, output đi đâu]

## Task
[1 việc cụ thể, đo được]

## Steps
Step 1: [action cụ thể]
Step 2: [action cụ thể]
Step 3: [action cụ thể]

## Hard Rules
- KHÔNG tự xóa bất cứ thứ gì
- KHÔNG tự merge PR
- KHÔNG gửi email nếu không có data mới
- CHỈ report, không tự fix

## Output Format
[Định dạng output cụ thể]

## Delivery
Send to: [Slack channel / Email / Telegram]
```

---

## Ví Dụ Routine Thực Tế

### Routine: GitHub Trending AI Scan

```markdown
## Context
Tôi quản lý kho AI Vibe Toolkit tại github.com/tano2026/AI-Vibe-Toolkit.
Mỗi sáng cần biết repos AI mới trending để thêm vào kho.

## Task
Scan GitHub trending hàng ngày, tìm repos AI/ML/LLM mới đáng chú ý.

## Steps
Step 1: Fetch github.com/trending?since=daily, lọc repos liên quan AI/Claude/LLM
Step 2: Với mỗi repo > 100 stars mới: fetch README, lấy description + key features
Step 3: Filter: loại bỏ repo đã có trong kho
Step 4: Format thành markdown list với: tên, stars, mô tả ngắn, lý do đáng xem

## Hard Rules
- KHÔNG tự push lên GitHub
- KHÔNG add vào kho nếu không có human review
- Chỉ báo cáo, để tôi quyết định

## Output Format
## AI Repos Trending Hôm Nay ({date})
| Repo | Stars | Mô tả | Angle video |
|------|-------|-------|-------------|
| ... | ... | ... | ... |

## Delivery
Send to Telegram: @AI_Vibe_Channel
```

### Routine: SEO Audit Hàng Đêm

```markdown
## Context
Website [URL]. Cần audit SEO mỗi đêm, detect regressions sớm.

## Steps
Step 1: Run /seo drift compare [url] via claude-seo plugin
Step 2: Check Core Web Vitals via PageSpeed API
Step 3: Compare với baseline từ tuần trước
Step 4: If có regression > 10%: alert ngay

## Hard Rules
- KHÔNG tự sửa code
- CHỈ alert khi có regression thực sự
- Attach diff để tôi biết gì thay đổi

## Delivery
If regression: Slack #seo-alerts
Else: log vào Google Sheets silently
```

---

## Repos Community Liên Quan

| Repo | Stars | Nội dung |
|------|-------|---------|
| fabiootempesta/claude-routines | 2⭐ | Local dashboard cho scheduled Claude CLI routines |
| Fisher521/routine-templates | 1⭐ | 5 production templates: PR triage, morning brief... |
| vigneshbarani24/awesome-claude-routines | - | 200 copy-paste routines: engineering, sales, ops... |
| charlie-morrison/claude-code-cron-cookbook | - | Production patterns, no silent failures |

---

## Lưu Ý Quan Trọng

⚠️ **Routines là cloud feature** — data của mày đi qua Anthropic servers. Không dùng cho sensitive data.

⚠️ **Pro plan ($20) chỉ có 5 runs/ngày** — plan kỹ trước khi setup nhiều routines.

⚠️ **Không có file format** — prompt lưu trong claude.ai UI, không thể export dễ dàng → backup prompt ra file local.

---
*Feature chính thức Anthropic | Release 15/4/2026 | claude.ai/code/routines*
*AI Vibe Toolkit | tháng 6/2026*
