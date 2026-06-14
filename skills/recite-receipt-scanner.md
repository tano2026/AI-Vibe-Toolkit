# Recite — AI Scan Hóa Đơn, Chứng Từ → Bookkeeping Tự Động (2⭐)

**GitHub:** https://github.com/rivradev/recite-agent-skill
**Stars:** 2⭐ | **License:** MIT
**Dùng với:** OpenClaw, Claude Code, Claude Cowork, Codex, Antigravity
**API:** Recite Vision API (recite.ai)

---

## Đây Là Gì

AI agent skill scan ảnh/PDF hóa đơn, chứng từ → extract data → đặt tên file logic → lưu vào CSV ledger tự động.

Thay vì nhập tay từng hóa đơn → chụp ảnh → Recite tự xử lý.

---

## Cài Nhanh

```bash
# OpenClaw
openclaw skill install rivradev/recite-agent-skill

# Claude Code
claude plugin install rivradev/recite-agent-skill

# Lấy Recite Vision API key: recite.ai → Sign up
export RECITE_API_KEY="your-key"
```

---

## Dùng Ngay

```bash
# Scan 1 hóa đơn
"Scan hóa đơn này: invoice_may.jpg
 → Extract: vendor, date, items, total, VAT
 → Đặt tên: 2026-05-15_CtyABC_1500000.jpg
 → Append vào ledger.csv"

# Batch scan cả folder
"Scan tất cả files trong /chung-tu/thang-05/:
 → Extract data từng cái
 → Rename logic
 → Tổng hợp vào ledger_t5.csv
 → Summary: tổng chi phí, tổng VAT"

# Scan với camera (mobile)
"Chụp biên lai này → extract → lưu vào sổ chi tiêu"
```

---

## Output CSV Ledger

```csv
Date,Vendor,Category,Total,Tax,Tip,Currency,File
2026-05-01,Công ty Điện lực,Điện nước,2300000,230000,0,VND,2026-05-01_Dien-luc_2300000.jpg
2026-05-03,Grab,Vận chuyển,150000,0,0,VND,2026-05-03_Grab_150000.pdf
2026-05-05,VPBank,Phí NH,55000,0,0,VND,2026-05-05_VPBank_55000.jpg
```

---

## Tích Hợp Với Workflow Kế Toán

```bash
# Step 1: Chụp/scan chứng từ → Recite extract
# Step 2: CSV ledger → import vào Google Sheets (Google Workspace MCP)
# Step 3: Jaz AI classify + journal entries
# Step 4: cynco-skills generate financial statements

# Cả pipeline:
"Scan tất cả chứng từ tháng 5 → 
 Import vào Google Sheets → 
 Run classification với Jaz AI → 
 Generate P&L báo cáo"
```

---

## Khi Nào Dùng Recite

✅ Nhiều hóa đơn giấy cần nhập liệu
✅ Chứng từ scan/chụp ảnh chưa có data
✅ Muốn tự động đặt tên file chuẩn
✅ Build ledger từ đầu

❌ Hóa đơn điện tử có sẵn XML/JSON → parse trực tiếp
❌ Bank statement CSV → dùng cynco-skills hoặc ke-toan-automation.md

---

*Nguồn: github.com/rivradev/recite-agent-skill | 2⭐ | MIT | tháng 6/2026*
