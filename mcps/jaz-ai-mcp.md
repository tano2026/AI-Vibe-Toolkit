# Jaz AI — 289 Tools Kế Toán, IFRS, 13 Calculators (4⭐)

**GitHub:** https://github.com/teamtinvio/jaz-ai
**MCP Remote:** https://mcp.jaz.ai/mcp (cloud, không cần cài)
**npm:** jaz-clio | **License:** MIT
**Tools:** 289 | **Skills:** 6 | **IFRS Recipes:** 16 | **Calculators:** 13 | **Close Playbooks:** 12
**Tương thích:** Claude, GPT, Gemini, Copilot, Cursor + Juan Accounting

---

## Đây Là Gì

Bộ agent tools đầy đủ nhất cho kế toán — 289 tools cover từ journal entries đến IFRS compliance, từ bank reconciliation đến financial statements. Token-lean, one-shot tool selection.

---

## Cài Đặt — 30 Giây

```bash
# Claude Code (recommended)
/plugin marketplace add teamtinvio/jaz-ai

# Claude Desktop / Claude.ai (cloud, không cài gì)
# Settings → Connectors → Add custom MCP
# URL: https://mcp.jaz.ai/mcp → Sign in với Jaz account

# Cursor / Windsurf
# Add MCP server: https://mcp.jaz.ai/mcp

# Microsoft 365 Copilot
# Add MCP tool: https://mcp.jaz.ai/mcp → OAuth
```

---

## 289 Tools — Theo Category

### 📊 Accounting Core
```bash
"Tạo journal entry: Dr Cash 10M / Cr Revenue 10M"
"Post tất cả transactions tháng 5 vào General Ledger"
"Generate Trial Balance từ GL tháng này"
"Tạo P&L statement Q2 2026"
"Tạo Balance Sheet tại ngày 30/6/2026"
"Phân loại chi phí theo Chart of Accounts"
```

### 🔄 Bank Reconciliation
```bash
"Reconcile bank statement với sổ sách tháng 5
 - Match transactions tự động
 - Flag unmatched items
 - Generate reconciliation report Excel"
```

### 📄 Invoicing
```bash
"Tạo invoice #INV-2026-001 cho [client]"
"List tất cả invoices outstanding > 30 ngày"
"Apply payment $5000 vào invoice INV-2025-089"
"Tạo credit note cho invoice bị sai"
```

### 🧮 13 Calculators
```bash
"Tính depreciation: Cost $50M, useful life 5 năm, SLM"
"Tính loan amortization: $1B, 12%, 60 months"
"Tính working capital ratio"
"Tính break-even point: Fixed cost 100M, margin 40%"
"Tính VAT: Revenue 500M, thuế suất 10%"
"Tính deferred tax liability"
"Tính goodwill từ acquisition"
```

### 📋 16 IFRS Recipes
```bash
"Apply IFRS 15 revenue recognition cho contract dài hạn"
"Apply IFRS 16 lease accounting: PV of lease payments"
"Apply IFRS 9 financial instruments classification"
"Prepare IFRS disclosures cho financial statements"
```

### 📅 12 Close Playbooks
```bash
"Run month-end close checklist tháng 5"
"Identify accruals cần book trước closing"
"Verify inter-company eliminations"
"Sign off close: all items checked"
```

### 📊 Financial Analysis
```bash
"Phân tích trend revenue 6 tháng gần nhất"
"So sánh actual vs budget tháng này"
"Tính KPIs: ROE, ROA, Current Ratio, Quick Ratio"
"Tạo CFO dashboard với key metrics"
```

---

## Workflow Kế Toán Cuối Tháng

```bash
# 1. Close check
"Run month-end close checklist tháng 5"

# 2. Bank reconciliation
"Reconcile bank statement file CSV với GL tháng 5"

# 3. Journal entries
"Post accruals: lương, khấu hao, prepaid"

# 4. Financial statements
"Generate P&L, Balance Sheet, Cash Flow tháng 5"

# 5. Tax
"Tính VAT phải nộp tháng 5: đầu ra - đầu vào"

# 6. Archive
"Export tất cả working papers Excel + PDF"
```

---

## Juan Accounting (Alternative)

Jaz AI tương thích với **Juan Accounting** (juan.ac) — cùng API surface. Nếu dùng Juan thay Jaz → vẫn dùng được toàn bộ 289 tools.

---

*Nguồn: github.com/teamtinvio/jaz-ai | 4⭐ | MIT | 289 tools | tháng 6/2026*
