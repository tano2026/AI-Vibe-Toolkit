# Worker K — Office Automation Cho Kế Toán (Excel/Word/PDF/Bank Rec)

**GitHub:** https://github.com/WeiKhjan/worker-k
**Stars:** 1⭐ | **License:** MIT
**Install:** `claude plugin install WeiKhjan/worker-k`
**Built for:** Malaysian accounting & audit firms → useful everywhere

---

## Cài Nhanh

```bash
claude plugin install WeiKhjan/worker-k

# Python dependencies cần thiết
pip install openpyxl xlrd pandas xlsxwriter python-docx docx2txt pdfplumber PyPDF2 reportlab pikepdf playwright
playwright install chromium
```

---

## Skills Chính

### 📊 Excel
```bash
"Đọc file Excel sao kê ngân hàng.xlsx, parse tất cả transactions"
"Tạo Excel working papers với professional formatting"
"Reconcile: match bank statement với cash book, highlight differences"
"Tạo pivot table: chi phí theo danh mục và tháng"
"Convert CSV → Excel với formatting chuẩn"
"Tạo Excel báo cáo với charts: bar chart doanh thu 6 tháng"
```

### 📝 Word
```bash
"Tạo Word document báo cáo kiểm toán từ template"
"Mail merge: điền thông tin khách hàng vào template hợp đồng"
"Convert Word → PDF"
"Tạo management representation letter cho audit"
```

### 📄 PDF
```bash
"Extract text và tables từ PDF hóa đơn"
"Merge 12 file PDF báo cáo tháng thành 1 file báo cáo năm"
"Split PDF: tách từng hóa đơn thành file riêng"
"Watermark PDF: thêm 'CONFIDENTIAL' vào mỗi trang"
"Fill PDF form: điền tờ khai thuế PDF"
"Generate PDF báo cáo từ data"
```

### 🏦 Bank Reconciliation
```bash
"Reconcile bank statement với cash book:
 Input: bank_statement.csv + cash_book.xlsx
 → Match tự động theo amount + date
 → Flag unmatched items
 → Generate Excel reconciliation report professional"
```

### 🔍 Research
```bash
"Research quy định thuế GTGT cho dịch vụ xuất khẩu phần mềm"
"Research: khấu hao tài sản cố định theo VAS 03"
"Research: điều kiện hoàn thuế GTGT đầu vào"
```

### 🌐 Web Automation
```bash
"Lên Cục Thuế website, tải mẫu tờ khai 01/GTGT mới nhất"
"Scrape bảng tỷ giá từ Vietcombank về Excel"
"Download danh sách hóa đơn từ portal hóa đơn điện tử"
```

---

## Workflow Kiểm Toán Nhanh

```bash
# Bank reconciliation hàng tháng
"Reconcile bank statement tháng 5:
 - File ngân hàng: bank_t5.csv
 - Sổ quỹ: so_quy_t5.xlsx
 - Output: reconciliation_t5.xlsx với professional format"

# Extract data từ hóa đơn PDF
"Extract tất cả hóa đơn trong folder /hoa-don/:
 - Vendor name, invoice number, date, amount, VAT
 - Export ra hoa-don-t5.xlsx"

# Tạo báo cáo
"Merge tất cả working papers tháng 5 thành 1 PDF
 Add watermark: DRAFT
 Email cho partner review"
```

---

*Nguồn: github.com/WeiKhjan/worker-k | 1⭐ | MIT | tháng 6/2026*
