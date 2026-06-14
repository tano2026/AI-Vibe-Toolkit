# Invoice Extractor — Hóa Đơn/Chứng Từ → JSON Sạch, Tự Kiểm Tra

**GitHub:** https://github.com/Viprasol-Tech/invoice-extractor
**License:** MIT | **Output:** Validated JSON
**Dùng với:** Claude Code, OpenClaw, Antigravity

---

## Đây Là Gì

Agent skill extract data từ hóa đơn, biên lai, bills → JSON sạch với:
- Vendor, line items, totals, tax, payment terms
- **Math được check tự động** — flag discrepancies
- Validation built-in

---

## Cài

```bash
claude plugin install Viprasol-Tech/invoice-extractor
# hoặc
npx skills add Viprasol-Tech/invoice-extractor
```

---

## Dùng Ngay

```bash
# Extract 1 hóa đơn
"Extract data từ invoice này" + [attach file]

# Batch extract
"Extract tất cả hóa đơn trong folder /hoa-don-t5/"

# Với validation
"Extract và validate: check tổng tiền = sum(line items)"
```

---

## Output JSON

```json
{
  "invoice_number": "INV-2026-001",
  "date": "2026-05-15",
  "due_date": "2026-06-15",
  "vendor": {
    "name": "Công ty ABC",
    "tax_id": "0123456789",
    "address": "123 Nguyễn Huệ, TP.HCM"
  },
  "line_items": [
    {
      "description": "Dịch vụ thiết kế website",
      "quantity": 1,
      "unit_price": 10000000,
      "amount": 10000000
    }
  ],
  "subtotal": 10000000,
  "tax_rate": 0.10,
  "tax_amount": 1000000,
  "total": 11000000,
  "payment_terms": "Net 30",
  "validation": {
    "math_check": "PASS",
    "discrepancies": []
  }
}
```

---

## Tích Hợp Workflow

```bash
# Extract → Validate → Import vào Jaz AI / Xero
"Extract hóa đơn → validate → 
 nếu PASS: tạo bill entry trong Xero
 nếu FAIL: flag để review thủ công"

# Batch processing
"Process 50 hóa đơn tháng 5:
 → Extract JSON từng cái
 → Validate math
 → Import vào Google Sheets
 → Report: X pass, Y cần review"
```

---

*Nguồn: github.com/Viprasol-Tech/invoice-extractor | MIT | tháng 6/2026*
