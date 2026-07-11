---
name: google-workspace-mcp
description: >
  GitHub: https://github.com/evolsb/claude-code-google-workspace Stars: 25⭐
  License: MIT Multi-account support
---

# google-workspace-mcp — Gmail + Drive + Sheets + Docs Cho Claude Code (25⭐)

**GitHub:** https://github.com/evolsb/claude-code-google-workspace
**Stars:** 25⭐ | **License:** MIT | Multi-account support
**Cover:** Gmail · Google Drive · Calendar · Sheets · Docs · Slack

---

## Đây Là Gì

MCP server cho Claude Code để access toàn bộ Google Workspace — đọc/ghi Gmail, Drive, Sheets, Docs, Calendar. **Multi-account** (personal + work).

**Dùng cho kế toán:**
- Đọc file CSV sao kê ngân hàng từ Drive
- Xử lý → ghi kết quả vào Google Sheets
- Tạo Google Docs báo cáo thuế
- Gửi Gmail báo cáo định kỳ

---

## Cài Đặt

```bash
git clone https://github.com/evolsb/claude-code-google-workspace
cd claude-code-google-workspace
npm install

# Cài gws CLI
npm install -g @trypear/gws

# Setup OAuth2 (1 lần)
gws auth login
# → Mở browser → chọn Google account → authorize
```

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "node",
      "args": ["/path/to/claude-code-google-workspace/index.js"],
      "env": {
        "GWS_ACCOUNT": "your@gmail.com"
      }
    }
  }
}
```

---

## Tools Available

### Gmail
```bash
"Đọc emails chưa đọc hôm nay, filter hóa đơn nhà cung cấp"
"Search emails từ domain supplier.com trong tháng 5"
"Gửi email báo cáo thuế tháng cho kế toán trưởng"
"Draft email xác nhận thanh toán cho vendor X"
```

### Google Drive
```bash
"Upload file báo cáo thuế tháng 5 lên Drive/Kế toán/2026/"
"Tạo thư mục Drive theo cấu trúc: Kế toán/2026/Tháng-05/"
"Tìm file CSV sao kê ngân hàng tháng 5 trong Drive"
"Chia sẻ file với kế toán@company.com quyền view only"
```

### Google Sheets
```bash
"Đọc Sheet 'Sao kê tháng 5', lấy tất cả transactions"
"Ghi kết quả phân loại chi phí vào Sheet 'Báo cáo thuế'"
"Update cột ITC (Khấu trừ thuế) với giá trị tính toán"
"Tạo sheet mới 'Tổng hợp tháng 5' với báo cáo cuối"
"Append row mới vào Sheet tracking hóa đơn"
```

### Google Docs
```bash
"Tạo Google Doc báo cáo thuế tháng từ template"
"Điền số liệu vào template báo cáo kế toán"
"Export Doc thành PDF"
```

### Calendar
```bash
"Tạo reminder 'Nộp báo cáo VAT' ngày 20 mỗi tháng"
"Check lịch deadline thuế tháng này"
```

---

## Workflow Kế Toán Với Google Workspace MCP

```bash
# Step 1: Đọc sao kê từ Drive
"Tìm file CSV sao kê ngân hàng tháng 5 trong Drive/Sao kê/"

# Step 2: Xử lý phân loại (Python script)
# → Xem skills/ke-toan-automation.md

# Step 3: Ghi kết quả vào Sheets
"Ghi kết quả phân loại vào Google Sheets 'Sổ kế toán 2026'
 - Tab: Tháng 5
 - Columns: Ngày, Nội dung, Danh mục, Khấu trừ, Tỷ lệ, ITC"

# Step 4: Tạo báo cáo
"Tạo Google Doc 'Báo cáo thuế tháng 5' từ dữ liệu Sheets
 Include: Tổng chi phí, Tổng ITC, Điều kiện hoàn thuế"

# Step 5: Upload PDF lên Drive
"Export Doc thành PDF, upload vào Drive/Báo cáo thuế/2026/"

# Step 6: Gửi email
"Gửi email cho ke-toan@company.com với attachment PDF vừa tạo"
```

---

*Nguồn: github.com/evolsb/claude-code-google-workspace | 25⭐ | MIT | tháng 6/2026*


---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

def gmail_send(access_token, raw_message_base64):
    payload = json.dumps({"raw": raw_message_base64}).encode()
    req = urllib.request.Request(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
        data=payload,
        headers={"Authorization": f"Bearer {access_token}",
                 "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
git clone https://github.com/evolsb/claude-code-google-workspace
# Setup OAuth2 (1 lần) qua Google Cloud Console
```

### Antigravity
```bash
echo 'GOOGLE_CLIENT_ID=your_id' >> /home/ubuntu/.hermes/.env
echo 'GOOGLE_CLIENT_SECRET=your_secret' >> /home/ubuntu/.hermes/.env
echo 'GOOGLE_REFRESH_TOKEN=your_refresh_token' >> /home/ubuntu/.hermes/.env
```
> ⚠️ access_token hết hạn 1 giờ — Hermes cần logic tự refresh bằng refresh_token, phức tạp hơn API key tĩnh nhiều.
