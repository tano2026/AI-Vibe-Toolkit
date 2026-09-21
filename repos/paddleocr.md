# PaddleOCR — GitHub Repo

## TL;DR
Toolkit OCR/document-parsing trưởng thành nhất trong mọi tool đã research phiên này — 6 năm phát triển, 89.761 sao, 22,67 triệu lượt tải PyPI, vẫn cập nhật đều (v3.7.0 tháng 6/2026). Từ Baidu (PaddlePaddle). Đây không phải fork hỗn loạn vài tuần tuổi như nhiều tool trước — là hạ tầng OCR nền cho hàng loạt project nổi tiếng khác (Umi-OCR, OmniParser, MinerU, RAGFlow đều dùng làm engine bên dưới).

## Repo này dùng để làm gì
Nhận diện chữ trong ảnh/PDF (OCR) + phân tích layout tài liệu (bảng, công thức, con dấu, ảnh) → xuất ra text/Markdown/DOCX có cấu trúc. PP-OCRv6 (mới nhất) hợp nhất 50 ngôn ngữ trong 1 model, 3 tier kích thước (tiny 1.5M/small 7.7M/medium 34.5M tham số) cho edge/mobile/server. PaddleOCR-VL-1.6 đạt 96,3% chính xác trên benchmark OmniDocBench — vượt cả model VLM tổng quát lớn (Qwen3-VL-235B, GPT-5.5) dù nhỏ hơn nhiều.

## Setup từng bước
1. Cài: `pip install paddleocr`
2. Dùng ngay:
```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")  # hoặc "ch", "vi" nếu hỗ trợ tiếng Việt riêng — cần verify
result = ocr.predict("duong-dan-anh.jpg")
for line in result:
    print(line)
```
3. Có SDK chính thức Python/Go/TypeScript, và PaddleOCR.js chạy thẳng trên trình duyệt (không cần server riêng)
4. Document parsing nâng cao (bảng/công thức/con dấu) dùng pipeline PP-StructureV3 hoặc PaddleOCR-VL

## Ví dụ thực tế
Zalo Mini App bán vé ABTRIP đang có màn hình "Nhập số giấy tờ" (CCCD/Hộ chiếu) yêu cầu khách gõ tay — có thể thay bằng chụp ảnh giấy tờ, PaddleOCR tự đọc số, khách chỉ cần xác nhận lại thay vì gõ toàn bộ. Giảm ma sát đúng tinh thần đã áp cho phần tên/SĐT (lấy tự động từ Zalo).

## Lưu ý / Lỗi thường gặp
- Model tải về khá nặng lần đầu (từ HuggingFace/ModelScope hoặc BOS của Baidu) — cần mạng ổn định lúc setup
- Cần xác nhận riêng mức hỗ trợ tiếng Việt — docs liệt kê "50 ngôn ngữ hợp nhất" gồm Latin-script nhưng chưa thấy xác nhận rõ tiếng Việt có dấu chạy tốt tới đâu, nên test thật trước khi tin dùng production cho CCCD/hộ chiếu VN
- Model 3 tier (tiny/small/medium) — chọn đúng tier theo môi trường chạy (mobile app nên dùng tiny/small, server có thể dùng medium để chính xác hơn)

## Đánh giá cá nhân
- Điểm mạnh: cực kỳ trưởng thành, được nhiều project lớn khác tin dùng làm engine nền, đa ngôn ngữ, nhiều tier kích thước phù hợp mobile lẫn server, license Apache 2.0 rõ ràng
- Điểm yếu: chưa xác nhận độ chính xác riêng với tiếng Việt có dấu — cần tự test trước khi dùng cho giấy tờ VN
- Có nên dùng: 9/10 — độ rủi ro thấp nhất trong các tool research gần đây (không phải fork hỗn loạn), đáng tích hợp thật cho bất kỳ luồng nào cần đọc giấy tờ/tài liệu

## Link
- Repo: https://github.com/PaddlePaddle/PaddleOCR
- Docs: https://paddlepaddle.github.io/PaddleOCR/main/en/index.html

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# PaddleOCR cần pip install — vi phạm luật urllib-only của Hermes.
# Đúng cách: Antigravity cài sẵn 1 lần trên VPS (đã có tiền lệ cài
# markitdown/tavily-python/playwright cho Hermes), Hermes chỉ import
# và gọi, không tự pip install trong runtime.
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang="en")
result = ocr.predict(image_path)
```
> Lưu ý: cần Antigravity chạy `pip install paddleocr` 1 lần trên môi trường Hermes trước, giống pattern các package khác đã cài sẵn.

### OpenClaw / Claude Code
```bash
pip install paddleocr
# Dùng trực tiếp trong code Python bất kỳ project nào Claude Code đang làm
```

### Antigravity
```bash
pip install paddleocr
# Nếu deploy cho Zalo Mini App backend-proxy — cân nhắc PaddleOCR.js
# (chạy trên browser, không cần server riêng) nếu muốn xử lý client-side
```
