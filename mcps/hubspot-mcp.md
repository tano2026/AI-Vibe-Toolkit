# hubspot-mcp — HubSpot CRM & Marketing Từ Claude (33 Tools)

**GitHub:** https://github.com/ZLeventer/hubspot-mcp
**Tools:** 33 tools | **License:** MIT | **Language:** TypeScript
**Cover:** Contacts, Companies, Deals, Pipelines, Lists, Marketing Emails, Forms, Workflows

---

## Đây Là Gì

MCP server cho HubSpot — Claude đọc, tạo, update toàn bộ CRM data và marketing workflows mà không cần mở HubSpot UI.

---

## Cài Đặt

```bash
git clone https://github.com/ZLeventer/hubspot-mcp
cd hubspot-mcp
npm install && npm run build
```

**Lấy API key:** HubSpot → Settings → Integrations → Private Apps → Create

```json
{
  "mcpServers": {
    "hubspot": {
      "command": "node",
      "args": ["/path/to/hubspot-mcp/build/index.js"],
      "env": { "HUBSPOT_ACCESS_TOKEN": "pat-xxx" }
    }
  }
}
```

---

## 33 Tools — Theo Category

### Contacts (6 tools)
```bash
"Tìm contact theo email john@example.com"
"Tạo contact mới: name, email, phone, company"
"Update lifecycle stage của contact X thành Customer"
"Lấy 50 contacts mới nhất trong pipeline"
```

### Companies (3 tools)
```bash
"Search companies trong industry Tech có > 100 employees"
"Tạo company record mới"
"Get company với tất cả associated contacts"
```

### Deals (4 tools)
```bash
"List tất cả deals trong stage Proposal Sent"
"Tạo deal mới: $5000, close date next month, assign to rep"
"Update deal amount và stage"
"Get deals closing this week"
```

### Marketing Emails (4 tools)
```bash
"List tất cả email campaigns"
"Get stats của campaign 'April Newsletter': opens, clicks, unsubscribes"
"Tạo draft marketing email"
"Schedule email campaign cho ngày mai 9am"
```

### Lists & Workflows (6 tools)
```bash
"Create list: contacts opened email nhưng chưa mua trong 30 ngày"
"List tất cả active workflows"
"Enroll contact X vào workflow Lead Nurture"
"Get workflow execution history"
```

### Forms & Properties (6 tools)
```bash
"List tất cả forms trên website"
"Get form submissions từ hôm qua"
"Create custom property: 'AI Tool Used'"
"Get tất cả custom properties của Contact object"
```

---

## Workflow Marketing Dùng Claude + HubSpot MCP

```bash
# Morning marketing review
"Lấy tất cả leads mới từ hôm qua, group theo source, tóm tắt"

# Follow-up automation
"Tìm contacts đã open email nhưng không click CTA trong 7 ngày → 
 tạo list → enroll vào workflow re-engagement"

# Pipeline health check
"List deals không có activity trong 14 ngày → 
 tổng hợp theo owner → highlight deals có giá trị cao nhất"

# Campaign performance
"Get stats tất cả emails trong tháng này → 
 so sánh open rate, click rate → identify top performer"
```

---

*Nguồn: github.com/ZLeventer/hubspot-mcp | 33 tools | MIT | tháng 6/2026*
