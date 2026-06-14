# accounting-skills (cynco) — 8 Phases Kế Toán Chuyên Nghiệp (10⭐)

**GitHub:** https://github.com/cynco-labs/skills
**Stars:** 10⭐ | **License:** MIT
**Install:** `npx @cynco/accounting-skills`
**Compliance:** MPERS / MFRS / ITA 1967 | Sole prop, Partnership, Sdn Bhd, NGO

---

## Cài Nhanh

```bash
npx @cynco/accounting-skills
```

Hoặc trong Claude Code:
```bash
/plugin marketplace add cynco-labs/skills
```

---

## 8 Phases — Pipeline Kế Toán Hoàn Chỉnh

```
PHASE 0: Engagement Setup
  → Scan folder, detect entity type & FY
  → Inventory documents available

PHASE 1: Document Extraction
  → OCR bank statements
  → Parse invoices
  → Extract payslips & bills

PHASE 2: Reconciliation & Classification
  → Classify transactions theo Chart of Accounts
  → Match bank ↔ invoices (accrual basis)

PHASE 3: Journal Entries
  → Opening balances
  → Bank transactions
  → Payroll, depreciation, accruals, adjustments

PHASE 4: Financial Statements
  → GL → Trial Balance → P&L → Balance Sheet

PHASE 5: Tax Computation
  → Form C / Form B / Form P
  → S44(6) exempt income

PHASE 6: Quality Control
  → Mandatory checklist: math, data, compliance, completeness

PHASE 7: Output
  → Excel working papers (openpyxl)
  → PDF financial statements (reportlab)
```

---

## Dùng Ngay

```bash
# Drop documents vào folder, Claude tự xử lý
"Chạy accounting pipeline cho tháng 5:
 Folder: ./thang-05/
 Có: bank_statement_t5.csv, invoices/, payroll.xlsx"

# Phase cụ thể
"Chạy Phase 2: reconcile bank statement với invoices tháng 5"
"Chạy Phase 4: tạo P&L và Balance Sheet từ GL đã có"
"Chạy Phase 6: QC check toàn bộ working papers"
```

---

## Adapt Cho Việt Nam

Cynco viết cho Malaysia (MPERS/ITA 1967) — adapt cho Việt Nam:

```
Thay đổi:
- Tax form: Form C → Tờ khai thuế TNDN (mẫu 03/TNDN)
- VAT: GST Malaysia → GTGT Việt Nam (10%/5%/0%)
- Compliance: ITA 1967 → Luật Thuế TNDN 2008 + sửa đổi
- Standards: MPERS → VAS (Chuẩn mực kế toán Việt Nam)

Prompt thêm vào đầu:
"Áp dụng quy định kế toán và thuế Việt Nam:
 - VAS (Vietnamese Accounting Standards)
 - Thuế TNDN: 20% (SME), 25% (lớn)
 - GTGT: 10%/5%/0%
 - Tờ khai theo mẫu Tổng cục Thuế"
```

---

## Tích Hợp Với Jaz AI

```bash
# Dùng cynco skills để xử lý documents
# → Dùng Jaz AI để push dữ liệu vào hệ thống

Phase 0-3: cynco-skills (document processing)
Phase 4-7: Jaz AI tools (financial statements + tax)
```

---

*Nguồn: github.com/cynco-labs/skills | 10⭐ | MIT | tháng 6/2026*
