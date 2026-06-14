# Accounting Stack Guide — Kế Toán AI Đầy Đủ

**Tổng hợp:** Jaz AI + cynco-skills + Worker K + Recite + Invoice Extractor + Cloud MCPs
**Cập nhật:** tháng 6/2026

---

## Chọn Stack Theo Tình Huống

```
SMB đang dùng Xero/Wave/FreshBooks
→ Cloud Accounting MCP tương ứng + Jaz AI

Kế toán độc lập, file-based
→ cynco-skills (8 phases) + Worker K (Excel/PDF)

Nhiều hóa đơn giấy cần nhập
→ Recite scanner + Invoice Extractor

Chứng từ thô từ ngân hàng (CSV)
→ skills/ke-toan-automation.md (đã có trong kho)

Full stack chuyên nghiệp
→ Tất cả kết hợp (xem workflow dưới)
```

---

## Decision Tree — Tool Nào Cho Việc Gì

```
CÓ CHỨNG TỪ GIẤY/ẢNH?
├── Có → Recite scanner + Invoice Extractor → JSON/CSV
└── Không ↓

CÓ FILE CSV SAO KÊ NGÂN HÀNG?
├── Có → ke-toan-automation.md (Claude phân loại)
└── Không ↓

ĐANG DÙNG PHẦN MỀM KẾ TOÁN?
├── Xero → xero-mcp
├── Wave → waveapps-mcp  
├── FreshBooks → freshbooks-mcp
├── Jaz → jaz-ai-mcp (289 tools!)
└── Không dùng gì ↓

CẦN FULL PIPELINE KẾ TOÁN?
└── cynco-skills (8 phases) + Worker K (Excel/PDF output)
```

---

## Full Stack Workflow — Cuối Tháng

```bash
# TUẦN 1-4: Thu thập
Recite: scan chứng từ phát sinh → CSV ledger
Invoice Extractor: extract hóa đơn → JSON validate

# CUỐI THÁNG: Xử lý
Week 4, ngày 28-30:

# Step 1: Tổng hợp data
"Merge: Recite ledger + Bank CSV + Invoice JSON
 → Google Sheets tổng hợp tháng 5"

# Step 2: Phân loại + tính thuế
Ke-toan-automation.md:
"Phân loại 150 transactions, tính ITC, check hoàn thuế"

# Step 3: Jaz AI — financial statements
"Post journal entries tháng 5
 Generate P&L, Balance Sheet
 Tính VAT phải nộp"

# Step 4: Worker K — working papers
"Tạo Excel working papers professional
 Convert → PDF
 Upload Google Drive"

# Step 5: Reports + Archive
Google Workspace MCP:
"Tạo Google Doc báo cáo tổng hợp
 Upload Drive/Kế toán/2026/Tháng-05/
 Gửi email cho kế toán trưởng"

# Claude Routine ngày 18:
"Nhắc: Deadline nộp VAT ngày 20
 Summary: phải nộp X đồng"
```

---

## Setup Nhanh (Chạy Lần Đầu)

```bash
# 1. Jaz AI — best all-in-one
/plugin marketplace add teamtinvio/jaz-ai

# 2. cynco skills — full pipeline
npx @cynco/accounting-skills

# 3. Worker K — Excel/PDF/Word
claude plugin install WeiKhjan/worker-k
pip install openpyxl pandas python-docx pdfplumber reportlab

# 4. Recite — scan chứng từ
claude plugin install rivradev/recite-agent-skill

# 5. Invoice Extractor
claude plugin install Viprasol-Tech/invoice-extractor

# 6. Google Workspace MCP (đã có trong kho)
# Xem: mcps/google-workspace-mcp.md

# 7. Cloud accounting (chọn 1)
# Xero: github.com/wyre-technology/xero-mcp
# Wave: github.com/LunaParker/waveapps-mcp
# FreshBooks: github.com/devolasvegas/freshbooks-mcp
```

---

## Prompts Copy-Paste

### Bank Reconciliation Nhanh
```
Reconcile bank statement tháng 5:
- Bank file: [upload bank_t5.csv]
- Sổ sách: [upload cash_book_t5.xlsx]
→ Match tự động theo date + amount (±1 ngày, ±1000đ tolerance)
→ Flag: unmatched bank entries + unmatched book entries
→ Output: Excel reconciliation với 3 tabs:
  Tab 1: Matched items
  Tab 2: Unmatched bank
  Tab 3: Unmatched book
→ Summary: số items match/không match, tổng chênh lệch
```

### Extract Batch Hóa Đơn
```
Process tất cả files trong folder /hoa-don-thang-05/:
- PDF và ảnh JPG/PNG
- Extract: vendor, date, invoice#, items, total, VAT
- Validate: total = subtotal + VAT
- Rename: YYYY-MM-DD_TenCongTy_SoTien.pdf
- Export: hoa-don-t5.xlsx với tất cả data
- Flag: files có validation errors
```

### Tính Thuế VAT Tháng
```
Tính VAT tháng 5:
GTGT đầu vào (từ ke-toan-automation output):
- Tổng ITC được khấu trừ: [X] đ

GTGT đầu ra (từ hóa đơn bán hàng):
- Tổng doanh thu có VAT: [Y] đ
- Thuế GTGT đầu ra: Y × 10%

Kết quả:
- VAT phải nộp = Đầu ra - Đầu vào
- Hoặc: VAT được hoàn nếu đầu vào > đầu ra liên tục 3 tháng

Tạo tờ khai 01/GTGT dạng bảng số liệu
```

---

*AI Vibe Toolkit | Accounting Stack Guide | tháng 6/2026*
