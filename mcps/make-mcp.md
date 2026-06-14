# makemcp — Build Make.com Scenarios Từ Claude (3,260 Apps)

**GitHub:** https://github.com/tommyevening/makemcp
**License:** MIT | **Language:** TypeScript | **Apps:** 3,260+
**Cập nhật:** 6/6/2026

---

## Đây Là Gì

MCP server để Claude **discover, assemble, validate và deploy** Make.com scenarios — 3,260 apps, làm offline discovery, deploy trực tiếp vào account của mày.

---

## Cài Đặt

```bash
git clone https://github.com/tommyevening/makemcp.git
cd makemcp
npm install && npm run build
```

**Lấy Make API token:** Make → Profile → API/SDK → Add token

```json
{
  "mcpServers": {
    "make": {
      "command": "node",
      "args": ["/path/to/makemcp/dist/index.js"],
      "env": {
        "MAKE_API_TOKEN": "your-token",
        "MAKE_TEAM_ID": "your-team-id",
        "MAKE_REGION": "eu1"
      }
    }
  }
}
```

---

## 17 Tools

```bash
# Discovery (offline — không cần credentials)
"Tìm Make modules cho Gmail"
"List tất cả apps liên quan đến social media"
"Get schema cho Slack module 'Send Message'"

# Build
"Tạo scenario: khi Gmail nhận email → parse → add vào Google Sheets"
"Build scenario: Webhook → filter → Slack notify → update Airtable"

# Validate & Deploy
"Validate scenario trước khi deploy"
"Deploy scenario X vào Make account"
"List tất cả scenarios trong team"
"Get execution history của scenario Y"
```

---

## Scenario Hay Nhất Cho Marketing

```bash
# Social listening + alert
"Tạo scenario: monitor Twitter mentions của 'AI Vibe Toolkit' → 
 filter negative sentiment → notify Slack #alerts → 
 log vào Google Sheets"

# Content scheduler
"Scenario: mỗi ngày 7h → fetch từ Google Sheets content calendar → 
 post lên Buffer → update status trong sheet"

# Lead enrichment
"Scenario: HubSpot new contact webhook → 
 enrich với Clearbit → 
 update HubSpot properties → 
 add vào right Mailchimp audience"

# Video production notify
"Scenario: khi file .mp4 mới trong Google Drive /finished/ → 
 upload lên YouTube (scheduled) → 
 post caption lên TikTok → 
 notify Telegram khi done"
```

---

## So Sánh n8n MCP vs Make MCP

| | n8n MCP | Make MCP |
|--|---------|---------|
| Self-hosted | ✅ | ❌ Cloud |
| Apps | 400+ native | 3,260 |
| Free | ✅ (self-host) | Limited free tier |
| Offline build | ❌ | ✅ (discovery) |
| Deploy | ✅ | ✅ |
| Best for | Tech users | Non-tech users, many SaaS |

---

*Nguồn: github.com/tommyevening/makemcp | MIT | 3,260 apps | tháng 6/2026*
