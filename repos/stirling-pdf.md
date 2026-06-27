# Stirling PDF — GitHub Repo

## TL;DR
#1 PDF tool trên GitHub — 84.5K stars. Self-hosted web app xử lý mọi thứ liên quan đến PDF: merge, split, compress, convert, OCR, sign, watermark, edit — không upload file lên server người khác.

## Repo này dùng để làm gì
Thay vì dùng ILovePDF, SmallPDF (upload file lên server họ, tốn tiền, có giới hạn) — Stirling PDF chạy hoàn toàn local hoặc trên VPS của mày:
- Merge nhiều PDF thành một
- Split PDF theo trang
- Compress PDF giảm dung lượng
- Convert: PDF↔Word, PDF↔Excel, PDF↔PowerPoint, PDF↔Image
- OCR: scan PDF không có text → searchable PDF
- Sign: thêm chữ ký điện tử
- Watermark: thêm watermark hàng loạt
- Edit metadata, rotate, reorder pages
- Protect/unlock PDF bằng password

50+ tính năng, tất cả miễn phí, data không rời khỏi máy.

## Setup từng bước
```bash
# Docker (cách nhanh nhất)
docker run -d   -p 8080:8080   -v ./trainingData:/usr/share/tessdata   -v ./configs:/configs   --name stirling-pdf   frooodle/s-pdf:latest

# Truy cập: http://localhost:8080

# Docker Compose (có OCR tiếng Việt)
version: '3'
services:
  stirling-pdf:
    image: frooodle/s-pdf:latest
    ports:
      - '8080:8080'
    volumes:
      - ./trainingData:/usr/share/tessdata
    environment:
      - TESSERACT_LANGS=vie+eng  # OCR tiếng Việt
```

## Ví dụ thực tế
**Workflow agency du lịch:**
- Hàng tuần nhận 50 file PDF từ partner (hotel voucher, flight ticket)
- Stirling PDF: merge tất cả → split theo booking → watermark logo ABTRIP → compress → gửi khách
- Trước: 2 tiếng manual. Sau: script Python gọi Stirling PDF API → 5 phút.

**API automation:**
```python
import requests

# Merge PDFs via API
files = [open('doc1.pdf', 'rb'), open('doc2.pdf', 'rb')]
response = requests.post(
    'http://localhost:8080/api/v1/general/merge-pdfs',
    files=[('fileInput', f) for f in files]
)
with open('merged.pdf', 'wb') as out:
    out.write(response.content)
```

## Lưu ý / Lỗi thường gặp
- OCR tiếng Việt cần thêm Tesseract language pack `vie` — thêm vào TESSERACT_LANGS
- File lớn (>100MB) cần tăng Java heap: `-e JAVA_TOOL_OPTIONS="-Xmx2g"`
- Chạy trên ARM (Mac M1/M2): dùng tag `frooodle/s-pdf:latest-arm`
- Một số convert feature cần LibreOffice — image `frooodle/s-pdf:latest-fat` có sẵn

## Đánh giá cá nhân
- Điểm mạnh: 50+ tính năng miễn phí; data private 100%; có API để automation; OCR tiếng Việt; active development
- Điểm yếu: Cần Docker để self-host; UI không đẹp bằng ILovePDF; OCR chậm với file lớn
- Có nên dùng không: **9/10** — Deploy một lần dùng mãi. Không cần trả tiền ILovePDF Pro hay SmallPDF nữa.

## Link
- Repo: https://github.com/Stirling-Tools/Stirling-PDF
- Docs: https://stirlingtools.com/docs
