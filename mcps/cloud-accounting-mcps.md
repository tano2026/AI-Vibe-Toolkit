# Cloud Accounting MCPs — Xero + Wave + FreshBooks + Stripe

**Dùng cho:** Kết nối Claude với phần mềm kế toán cloud
**Cập nhật:** tháng 6/2026

---

## 1. XERO MCP

**GitHub:** https://github.com/wyre-technology/xero-mcp (1⭐)
**Also:** doublebash/xero-mcp (Cloudflare Workers)
**Cover:** Contacts, Invoices, Payments, Bank transactions, P&L, Balance Sheet

### Cài
```bash
# Option A: Deploy to Cloudflare Workers (recommended)
# Fork doublebash/xero-mcp → Deploy → Point Claude tới worker URL

# Option B: Local
git clone https://github.com/wyre-technology/xero-mcp
cd xero-mcp && npm install
# Setup Xero OAuth: developer.xero.com → Create App
export XERO_CLIENT_ID="..."
export XERO_CLIENT_SECRET="..."
```

### Tools
```bash
# Contacts
"List tất cả customers active trong Xero"
"Tạo contact mới: Công ty ABC, MST 123456789"
"Get contact details cho Công ty XYZ"

# Invoices
"Tạo invoice cho [client]: 3 items, due 30 ngày"
"List invoices overdue > 30 ngày"
"Apply payment $5000 vào invoice INV-2026-050"
"Void invoice INV-2026-040 với note 'Duplicate'"

# Bank transactions
"Get tất cả bank transactions tháng 5"
"Reconcile: match bank transactions với invoices"
"Get unreconciled transactions"

# Reports
"Get P&L tháng 5"
"Get Balance Sheet ngày 31/5/2026"
"Get Aged Receivables report"
```

---

## 2. WAVE ACCOUNTING MCP (FREE)

**GitHub:** https://github.com/LunaParker/waveapps-mcp
**Wave Accounting:** waveapps.com — FREE cho invoicing + accounting cơ bản

### Cài
```bash
git clone https://github.com/LunaParker/waveapps-mcp
cd waveapps-mcp && npm install

# Wave API key: waveapps.com → Settings → Developers → API tokens
export WAVE_API_KEY="..."
```

### Khi Nào Dùng Wave
✅ SMB cần kế toán cơ bản FREE
✅ Freelancer, sole prop
✅ Invoicing đơn giản
❌ Cần inventory management → dùng Xero/QuickBooks

### Tools
```bash
"List tất cả invoices tháng 5 trong Wave"
"Tạo invoice mới cho client A: design service $500"
"Get tổng revenue tháng này từ Wave"
"List expenses chưa categorize"
"Get P&L report Q2 2026"
```

---

## 3. FRESHBOOKS MCP

**GitHub:** https://github.com/devolasvegas/freshbooks-mcp (1⭐)
**FreshBooks:** freshbooks.com — phổ biến cho freelancer/agency

### Cài
```bash
git clone https://github.com/devolasvegas/freshbooks-mcp
cd freshbooks-mcp && npm install
cp .env.example .env
# Điền FreshBooks OAuth credentials
# developer.freshbooks.com → Create App
```

### Tools
```bash
"List tất cả clients trong FreshBooks"
"Tạo invoice cho client X: 10 giờ thiết kế × $50/h"
"Get outstanding invoices > 30 ngày"
"Record payment received từ client Y"
"Generate expense report tháng 5"
```

---

## 4. STRIPE MCP (Payments + Invoicing)

**GitHub:** https://github.com/friendlygeorge/stripe-mcp-server
**Cover:** Customers, Charges, Payments, Subscriptions, Invoices, Products, Refunds

### Cài
```bash
git clone https://github.com/friendlygeorge/stripe-mcp-server
cd stripe-mcp-server && npm install
export STRIPE_SECRET_KEY="sk_live_..."
```

### Tools
```bash
"List tất cả customers trong Stripe"
"Tạo payment link $500 cho client X"
"Get revenue tháng 5 từ Stripe"
"List subscriptions sắp renewal trong 7 ngày"
"Process refund $200 cho charge ch_xxx"
"Get tất cả failed payments tháng này"
"Export invoices tháng 5 → CSV"
```

---

## Chọn Tool Nào?

| Tình huống | Tool |
|-----------|------|
| Đang dùng Xero | Xero MCP |
| Muốn FREE, đơn giản | Wave MCP |
| Freelancer/Agency | FreshBooks MCP |
| Thu tiền online | Stripe MCP |
| Kế toán chuyên nghiệp | Jaz AI MCP |
| Xử lý chứng từ thô | cynco-skills + Worker K |

---

*AI Vibe Toolkit | Cloud Accounting MCPs | tháng 6/2026*
