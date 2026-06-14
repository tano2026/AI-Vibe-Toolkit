# Kế Toán Tự Động Hóa — Skill Dùng Ngay Với Claude Code

**Nguồn:** Workflow từ infographic "AI Thay Đổi Cách Kế Toán Vận Hành"
**Stack:** Claude Code + Python + Google Workspace MCP + Google Drive/Sheets
**Cập nhật:** tháng 6/2026

---

## 2 Workflows Chính

### Workflow 1: Phân Loại Sao Kê Ngân Hàng (20 giây)
```
CSV sao kê thô → AI phân loại → Bảng chi phí chuẩn thuế + ITC
```

### Workflow 2: Chuỗi Tác Vụ Tự Động
```
Xuất PDF hóa đơn → Upload Drive → Sync Google Sheets
```

---

## PROMPT 1 — Phân Loại Sao Kê Ngân Hàng

Copy paste vào Claude Code khi có file CSV sao kê:

```
Tôi có file sao kê ngân hàng [tên file]. Hãy:

1. Đọc file CSV, parse các cột: Ngày, Nội dung, Số tiền

2. Phân loại từng giao dịch theo danh mục chi phí chuẩn:
   - Chi phí điện nước
   - Chi phí dịch vụ
   - Chi phí ngân hàng
   - Mua hàng hóa
   - Chi phí quảng cáo
   - Chi phí nhân sự
   - Khác (nếu không xác định được)

3. Xác định khấu trừ thuế GTGT:
   - "Được khấu trừ": có hóa đơn GTGT, phục vụ hoạt động kinh doanh
   - "Không khấu trừ": không có hóa đơn, chi phí cá nhân, không hợp lệ

4. Tính ITC (Input Tax Credit):
   - Tỷ lệ khấu trừ: 100% (kinh doanh thuần), 70%, 50% tùy trường hợp
   - ITC = Số tiền × Tỷ lệ × 10% (thuế GTGT)

5. Output bảng kết quả:
   | Ngày | Nội dung | Danh mục | Khấu trừ | Tỷ lệ | ITC (VAT) |

6. Tổng hợp cuối:
   - Tổng chi phí: X,XXX,XXX
   - Tổng ITC được khấu trừ: X,XXX,XXX
   - Điều kiện hoàn thuế GTGT: Đủ/Chưa đủ điều kiện

QUAN TRỌNG:
- Đối chiếu quy định Cục Thuế Việt Nam (Thông tư 219/2013/TT-BTC)
- Không tự ý xác định nếu không chắc → đánh dấu "Cần xem lại"
- Giao dịch nghi ngờ → flag để kế toán review
```

---

## PROMPT 2 — Chuỗi Tác Vụ: Hóa Đơn → Drive → Sheets

```
Tôi cần tự động hóa quy trình hóa đơn. Hãy viết Python script:

INPUT: Danh sách hóa đơn (số HĐ, khách hàng, ngày, tổng tiền, thuế)

BƯỚC 1 — Xuất PDF:
- Dùng reportlab hoặc weasyprint
- Template: Logo công ty, thông tin hóa đơn, bảng sản phẩm/dịch vụ
- Tên file: HĐ_{số_hóa_đơn}_{ngày}_{khách_hàng}.pdf
- Lưu vào folder /invoices/

BƯỚC 2 — Upload Google Drive:
- Dùng Google Drive API (credentials.json)
- Upload vào folder: "Hóa đơn xuất/{năm}/{tháng}/"
- Tạo folder nếu chưa có
- Lấy shareable link sau khi upload

BƯỚC 3 — Update Google Sheets:
- Sheet: "Theo dõi hóa đơn 2026"
- Append row: Số HĐ | Ngày | Khách hàng | Tổng tiền | Thuế | Link PDF | Status
- Status: "Đã xuất - chờ thanh toán"

BƯỚC 4 — Gửi email thông báo (optional):
- Gửi cho khách hàng: PDF đính kèm + link Drive
- CC: ke-toan@company.com

Yêu cầu:
- Error handling: log lỗi, không crash toàn bộ nếu 1 HĐ fail
- Dry-run mode: --dry-run để test không gửi thật
- Config file: config.yaml cho credentials và settings
```

---

## PROMPT 3 — Logic Thuế Tự Động Khi Tạo Hóa Đơn

```
Tôi đang tạo hóa đơn cho khách hàng. Dựa vào thông tin:
- Khách hàng: [tên/địa chỉ/mã số thuế]
- Loại dịch vụ/hàng hóa: [...]
- Khu vực: Việt Nam / EU / Mỹ / Khác

Hãy xác định:

1. Thuế suất áp dụng:
   - Việt Nam: GTGT 10% (hàng hóa thông thường) / 5% (thiết yếu) / 0% (xuất khẩu)
   - EU: VAT theo từng nước (DE 19%, FR 20%, IT 22%...)
   - Mỹ: Sales tax theo state (CA 7.25%, TX 8.25%...)
   - Xuất khẩu: 0% GTGT

2. Thông tin trên hóa đơn:
   - Ghi đúng mã số thuế người mua/người bán
   - Đơn vị tiền tệ
   - Phương thức thanh toán
   - Điều khoản thanh toán

3. Yêu cầu pháp lý:
   - Việt Nam: Hóa đơn điện tử theo Nghị định 123/2020/NĐ-CP
   - EU: Invoice phải có VAT ID của buyer (B2B)
   - Mỹ: Không cần VAT, nhưng cần Sales Tax Certificate nếu có

Output: Thông tin hóa đơn đầy đủ, sẵn sàng để tạo PDF
```

---

## PROMPT 4 — Báo Cáo Tổng Hợp Thuế Tháng

```
Từ dữ liệu sao kê đã phân loại, tạo báo cáo tổng hợp thuế:

INPUT: Google Sheets "Sổ kế toán 2026" - Tab "Tháng {X}"

OUTPUT — Báo cáo tổng hợp:

1. BẢNG CHI PHÍ THEO DANH MỤC:
   | Danh mục | Số giao dịch | Tổng chi phí | ITC |
   
2. TỔNG KẾT:
   - Tổng chi phí tháng: X,XXX,XXX đ
   - Tổng ITC được khấu trừ: X,XXX,XXX đ
   - Thuế GTGT đầu ra: X,XXX,XXX đ (từ hóa đơn bán hàng)
   - Thuế GTGT đầu vào: X,XXX,XXX đ (ITC)
   - Thuế GTGT phải nộp / được hoàn: X,XXX,XXX đ

3. ĐIỀU KIỆN HOÀN THUẾ:
   - Đầu vào > Đầu ra liên tục 3 tháng → Đủ điều kiện hoàn
   - Xuất khẩu → Hoàn ngay

4. CHECKLIST CUỐI THÁNG:
   □ Đã đối chiếu số dư ngân hàng với sổ sách
   □ Đã kiểm tra hóa đơn đầu vào hợp lệ
   □ Đã nộp báo cáo VAT (deadline: ngày 20 tháng sau)
   □ Đã archive hóa đơn lên Drive

Lưu báo cáo:
- Google Doc: "Báo cáo thuế tháng {X}/2026"
- Upload PDF lên Drive/Báo cáo thuế/2026/
- Update Google Sheets "Dashboard kế toán"
```

---

## Python Script Mẫu — Phân Loại CSV

```python
# ke_toan_classifier.py
# Chạy: python ke_toan_classifier.py --input sao_ke_t5.csv --output ket_qua_t5.csv

import pandas as pd
import anthropic
import sys, argparse

# Danh mục chi phí chuẩn
CATEGORIES = {
    "điện nước": {"name": "Chi phí điện nước", "deductible": True, "rate": 100},
    "dịch vụ": {"name": "Chi phí dịch vụ", "deductible": True, "rate": 100},
    "ngân hàng": {"name": "Chi phí ngân hàng", "deductible": True, "rate": 100},
    "mua hàng": {"name": "Mua hàng hóa", "deductible": True, "rate": 100},
    "quảng cáo": {"name": "Chi phí quảng cáo", "deductible": True, "rate": 80},
    "nhân sự": {"name": "Chi phí nhân sự", "deductible": False, "rate": 0},
}

def classify_transaction(client, description, amount):
    prompt = f"""
Phân loại giao dịch kế toán:
Nội dung: {description}
Số tiền: {amount:,} VNĐ

Trả về JSON:
{{
  "category": "tên danh mục",
  "deductible": true/false,
  "rate": 0-100,
  "itc": số tiền ITC,
  "note": "ghi chú nếu cần"
}}
"""
    response = client.messages.create(
        model="claude-haiku-4-5",  # rẻ nhất, đủ dùng
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )
    import json
    return json.loads(response.content[0].text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    client = anthropic.Anthropic()
    df = pd.read_csv(args.input, encoding='utf-8-sig')

    results = []
    for _, row in df.iterrows():
        result = classify_transaction(client, row['Nội dung'], row['Số tiền'])
        results.append({
            'Ngày': row['Ngày'],
            'Nội dung': row['Nội dung'],
            'Số tiền': row['Số tiền'],
            'Danh mục': result['category'],
            'Khấu trừ': 'Được khấu trừ' if result['deductible'] else 'Không khấu trừ',
            'Tỷ lệ': f"{result['rate']}%",
            'ITC (VAT)': result['itc'],
            'Ghi chú': result.get('note', '')
        })
        print(f"✅ {row['Nội dung'][:40]} → {result['category']}")

    if not args.dry_run:
        pd.DataFrame(results).to_csv(args.output, index=False, encoding='utf-8-sig')
        print(f"\n✅ Saved: {args.output}")

    # Tổng hợp
    df_result = pd.DataFrame(results)
    total = df_result['Số tiền'].sum()
    itc = df_result['ITC (VAT)'].sum()
    print(f"\n📊 TỔNG KẾT:")
    print(f"Tổng chi phí: {total:,.0f} đ")
    print(f"Tổng ITC: {itc:,.0f} đ")

if __name__ == "__main__":
    main()
```

---

## Setup Nhanh

```bash
# Cài dependencies
pip install pandas anthropic gspread google-auth reportlab

# Cài Google Workspace MCP
git clone https://github.com/evolsb/claude-code-google-workspace
cd claude-code-google-workspace && npm install
gws auth login

# Chạy phân loại
python ke_toan_classifier.py \
  --input sao_ke_thang5.csv \
  --output ket_qua_thang5.csv

# Chạy với dry-run trước
python ke_toan_classifier.py \
  --input sao_ke_thang5.csv \
  --output test.csv \
  --dry-run
```

---

## Claude Routine Cho Kế Toán

Vào `claude.ai/code/routines`, tạo routine:

```markdown
## Task: Nhắc Nhở Kế Toán Cuối Tháng

## Schedule: Ngày 18 mỗi tháng, 09:00

## Steps
Step 1: Check Google Sheets "Sổ kế toán 2026" tháng hiện tại
Step 2: Tính: tổng ITC, tổng thuế đầu ra, số thuế phải nộp
Step 3: List các hóa đơn đầu vào chưa có trong hệ thống

## Hard Rules
- KHÔNG tự nộp báo cáo thuế
- KHÔNG tự điền mẫu
- CHỈ tóm tắt và nhắc việc cần làm

## Output
Gửi email ke-toan@company.com:
Subject: [Nhắc] Deadline báo cáo VAT tháng {X} — ngày 20
Body: Tóm tắt số liệu + checklist việc cần làm
```

---

*Skill từ infographic "AI Thay Đổi Cách Kế Toán" | AI Vibe Toolkit | tháng 6/2026*
