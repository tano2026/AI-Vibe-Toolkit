# Claude Routines — Prompt Templates Dùng Ngay

**URL:** claude.ai/code/routines
**Feature:** Anthropic official | Release 15/4/2026
**Cập nhật:** tháng 6/2026

---

## Cách Dùng File Này

1. Vào `claude.ai/code/routines`
2. Click **New Routine**
3. Copy prompt template bên dưới
4. Chỉnh `<placeholders>` theo situation của mày
5. Set schedule + connectors → Save

---

## TEMPLATE 1 — Morning Business Brief

**Schedule:** Mỗi ngày 07:30
**Connectors:** Gmail / Telegram / Slack

```markdown
## Context
Tôi cần bản tóm tắt buổi sáng trước khi bắt đầu ngày làm việc.

## Task
Tổng hợp những thứ quan trọng nhất cần biết và làm hôm nay.

## Steps
Step 1: Đọc emails quan trọng chưa đọc từ tối hôm qua (filter: starred hoặc từ domain ưu tiên)
Step 2: Check lịch hôm nay — meetings nào cần prep?
Step 3: Với mỗi meeting: tóm tắt context, ai tham dự, cần chuẩn bị gì
Step 4: List 3 task ưu tiên cao nhất hôm nay từ emails + lịch

## Hard Rules
- KHÔNG reply email tự động
- KHÔNG thay đổi lịch
- CHỈ read và tóm tắt

## Output Format
# ☀️ Morning Brief — {ngày}

## 📧 Emails Cần Xử Lý ({số})
- [From] Subject — action cần làm

## 📅 Meetings Hôm Nay
- HH:MM — Tên meeting — prep note ngắn

## 🎯 Top 3 Việc Cần Làm
1. ...
2. ...
3. ...

## Delivery
Telegram: <your_telegram_chat_id>
```

---

## TEMPLATE 2 — GitHub PR Auto Review

**Schedule:** Webhook — trigger khi có PR mới
**Connectors:** GitHub

```markdown
## Context
Repository: <github_org/repo>
Tôi muốn first-pass review tự động mọi PR mới.

## Task
Review PR #{pr_number} theo checklist engineering standard.

## Steps
Step 1: Fetch PR diff + description + linked issues
Step 2: Check: có test không? Test cover happy path + edge cases không?
Step 3: Check: có breaking changes không? Docs được update không?
Step 4: Check: security — SQL injection, XSS, hardcoded credentials không?
Step 5: Check: performance — N+1 queries, blocking operations không?
Step 6: Draft review comment với: summary, issues found (severity), suggestions

## Hard Rules
- KHÔNG tự approve PR
- KHÔNG tự merge
- KHÔNG request changes nếu chỉ là style issues nhỏ
- Chỉ comment, để author và reviewer quyết định

## Output Format
Post GitHub comment với:
## 🤖 Auto Review

**Summary:** [1-2 câu tóm tắt PR làm gì]

**Issues Found:**
- 🔴 Critical: [nếu có]
- 🟡 Warning: [nếu có]
- 🟢 Suggestions: [nếu có]

**Checklist:**
- [ ] Tests: ...
- [ ] Docs: ...
- [ ] Security: ...
- [ ] Performance: ...
```

---

## TEMPLATE 3 — Weekly Metrics Report

**Schedule:** Thứ Hai 08:00 hàng tuần
**Connectors:** Google Analytics / HubSpot / Slack

```markdown
## Context
Tôi cần weekly metrics report để gửi cho team mỗi sáng thứ Hai.

## Task
Tổng hợp metrics tuần trước và so sánh với tuần trước đó.

## Steps
Step 1: Fetch GA4 data — sessions, users, conversion rate, top pages
Step 2: Fetch HubSpot — new leads, deals created, deals closed, revenue
Step 3: Calculate WoW change (%) cho từng metric
Step 4: Identify: metric nào tăng đáng kể? Metric nào cần chú ý?
Step 5: 1-2 câu nhận xét cho mỗi metric quan trọng

## Hard Rules
- KHÔNG invent numbers nếu API không trả data
- KHÔNG đưa ra recommendation nếu không có đủ data
- Chỉ report facts

## Output Format
# 📊 Weekly Report — Tuần {W} ({date range})

| Metric | Tuần này | Tuần trước | Change |
|--------|---------|-----------|--------|
| Sessions | ... | ... | ±X% |
| New Leads | ... | ... | ±X% |
| Revenue | ... | ... | ±X% |

**🔺 Highlights:** ...
**🔻 Cần chú ý:** ...

## Delivery
Slack: #team-metrics
```

---

## TEMPLATE 4 — Shopify ROAS Morning Check

**Schedule:** Mỗi ngày 08:00
**Connectors:** Shopify + (Meta Ads hoặc Google Ads)

```markdown
## Context
Shopify store: <store_url>
Tôi chạy ads Facebook/Google và cần check ROAS mỗi sáng.

## Task
Check doanh số hôm qua và ROAS của từng campaign.

## Steps
Step 1: Fetch Shopify orders hôm qua — total revenue, số orders, AOV
Step 2: Fetch Meta Ads spend hôm qua theo campaign
Step 3: Calculate ROAS = revenue / spend cho từng campaign
Step 4: Flag campaigns có ROAS < <target_roas> để xem xét
Step 5: Flag campaigns có spend > <budget_threshold> mà ROAS thấp

## Hard Rules
- KHÔNG tự pause campaign
- KHÔNG tự điều chỉnh budget
- CHỈ alert, để tôi quyết định

## Output Format
# 🛒 Daily ROAS Check — {date}

**Tổng hôm qua:** {revenue} | {orders} orders | AOV: {aov}

| Campaign | Spend | Revenue | ROAS | Status |
|----------|-------|---------|------|--------|
| ... | ... | ... | ...x | 🟢/🔴 |

**⚠️ Cần xem xét:**
- [Campaign X]: ROAS {X} < target {Y}

## Delivery
Telegram: <chat_id>
```

---

## TEMPLATE 5 — Content Idea Generator

**Schedule:** Thứ Sáu 16:00
**Connectors:** last30days skill hoặc Brave Search

```markdown
## Context
Tôi làm content về AI tools cho audience Việt Nam (vibe coders, dev không chuyên).
Channel: TikTok + YouTube.

## Task
Tìm 5 AI tool/topic nổi bật trong tuần để làm content tuần tới.

## Steps
Step 1: Scan GitHub trending tuần này — repos AI/LLM có > 500 stars mới
Step 2: Check Reddit r/MachineLearning, r/LocalLLaMA — threads hot nhất
Step 3: Check HackerNews — AI stories > 100 points
Step 4: Filter: cái nào phù hợp với audience Việt Nam? Cái nào có visual demo tốt?
Step 5: Với mỗi topic: đề xuất hook video + angle độc đáo

## Hard Rules
- KHÔNG tự đăng content
- KHÔNG đề xuất topic quá kỹ thuật (audience là non-expert)
- Ưu tiên tools free và có visual demo

## Output Format
# 🎬 Content Ideas Tuần Tới

| # | Tool/Topic | Hook | Angle | Difficulty |
|---|-----------|------|-------|-----------|
| 1 | ... | ... | ... | Easy/Med |

## Delivery
Notion page: <page_id> hoặc Google Doc: <doc_id>
```

---

## TEMPLATE 6 — SEO Audit + Schema Auto-generate

**Schedule:** Hàng đêm 02:00
**Connectors:** claude-seo plugin

```markdown
## Context
Website: <your_url>
Tôi muốn SEO audit tự động mỗi đêm và auto-generate schema nếu thiếu.

## Steps
Step 1: /seo drift compare <url> — detect regressions
Step 2: /seo schema <url> — check schema hiện tại
Step 3: Nếu schema thiếu loại nào (Article, Product, FAQ): generate JSON-LD
Step 4: Save generated schema vào file schema.json
Step 5: Nếu có regression > 5%: alert ngay

## Hard Rules
- KHÔNG tự edit website code
- KHÔNG tự deploy schema
- Chỉ generate file và alert

## Output Format
File: schema-{date}.json (nếu có schema mới)

Report: Alert nếu có issue, silent nếu không.

## Delivery
If issues: Slack #seo-alerts + attach schema file
If OK: log vào Google Sheets
```

---

## Tips Viết Routine Hiệu Quả

**DO:**
- ✅ 1 routine = 1 việc cụ thể, đo được
- ✅ Hard Rules: nói rõ KHÔNG làm gì
- ✅ Output format cụ thể
- ✅ Delivery channel rõ ràng
- ✅ Backup prompt ra file local (UI không có export)

**DON'T:**
- ❌ 1 routine quá nhiều việc → split ra
- ❌ Không có Hard Rules → AI sẽ "improvise"
- ❌ Dùng routine cho sensitive data
- ❌ Quên giới hạn 5 runs/ngày (Pro plan)

---
*AI Vibe Toolkit | Claude Routines Templates | tháng 6/2026*
