# Markdown Converter — Convert PDF/docx/xlsx/audio sang Markdown an toàn

## TL;DR
Wrapper Python quanh thư viện MarkItDown (Microsoft), convert local file (PDF, Word, Excel, HTML, ảnh, audio) sang Markdown — có sẵn guardrail: chặn URL input, chặn overwrite file nhầm, tắt hết plugin ngoài. Hữu ích khi Bước 2 (Research) của Quy trình kho gặp nguồn là file thay vì link.

## Skill này dùng để làm gì
MarkItDown là công cụ chuẩn để trích text có cấu trúc (heading, list, table, link) từ file phức tạp ra markdown sạch, dễ cho AI đọc tiếp. Bản wrapper này (`markitdown_local.py`) thêm lớp an toàn:
- Chỉ nhận file local, từ chối thẳng input dạng URL (tránh agent tự ý fetch web ngoài ý muốn)
- Ghi ra file tạm trước, validate UTF-8, rồi mới thay thế file đích — tránh ghi đè hỏng file gốc
- Không bật plugin lạ, không dính credential cloud

## Setup từng bước
1. Cài MarkItDown: `pip install markitdown --break-system-packages` (hoặc dùng `uvx markitdown` nếu không muốn cài global)
2. Check runtime: `python scripts/markitdown_local.py doctor`
3. Convert 1 file: `python scripts/markitdown_local.py convert input.pdf output.md`
4. Convert cả thư mục: `python scripts/markitdown_local.py batch source_dir output_dir --recursive --include pdf --include docx`
5. Luôn kiểm tra lại output: heading/list/table/link có đúng thứ tự không, số liệu quan trọng có khớp bản gốc không

## Ví dụ thực tế
**Case:** Nobitano gửi Claude 1 file PDF hợp đồng NDC aggregator (Duffel) để research cho B2B Travel Platform ABTRIP → thay vì Claude đọc PDF trực tiếp trong context (tốn token, đôi khi mất cấu trúc bảng), convert trước qua markdown-converter:
```bash
python scripts/markitdown_local.py convert duffel-nda-contract.pdf duffel-nda.md
```
→ Ra file markdown sạch, bảng điều khoản giữ đúng cấu trúc, dễ research/trích dẫn hơn nhiều so với đọc PDF thô.

## Lưu ý / Lỗi thường gặp
- Không phải công cụ "giữ layout" — nếu cần giữ đúng bố cục trình bày (VD: brochure thiết kế phức tạp) thì không hợp, chỉ hợp cho trích xuất nội dung/text/bảng
- File scan ảnh (không có lớp text) → MarkItDown không OCR tốt, cần công cụ OCR riêng
- Lỗi thường gặp: quên `--overwrite` khi thật sự muốn ghi đè file .md đã tồn tại → script sẽ báo lỗi thay vì âm thầm ghi đè (đây là tính năng an toàn, không phải bug)

## Đánh giá cá nhân
- Điểm mạnh: có guardrail thật (chặn URL, chặn overwrite nhầm), dùng thư viện MarkItDown uy tín (Microsoft maintain), setup nhanh, không cần API key
- Điểm yếu: chỉ là 1 CLI wrapper mỏng — giá trị gia tăng so với gọi MarkItDown trực tiếp không nhiều, chủ yếu là lớp an toàn; không OCR scan tốt
- Có nên dùng không: 6/10 — hữu ích như 1 utility phụ trợ cho Bước 2 Research khi nguồn là file, không phải core capability mới

## Link
- MarkItDown gốc: https://github.com/microsoft/markitdown
- Wrapper: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes không được cài pip package ngoài (theo nguyên tắc urllib.request thuần)
# Nên KHÔNG cài markitdown trực tiếp vào Hermes runtime.
# Thay vào đó: Claude (trong session research) chạy converter trong sandbox riêng,
# rồi đưa nội dung .md đã convert cho Hermes xử lý tiếp qua Telegram/OmniRoute nếu cần.
```

### OpenClaw
```bash
# Nếu OpenClaw (Node.js, chạy VPS qua PM2) cần convert file trong workflow research:
pip install markitdown --break-system-packages
python markitdown_local.py convert /path/to/file.pdf /path/to/output.md
# Gọi qua child_process từ OpenClaw nếu cần tự động hóa
```

### Antigravity
```bash
# Cài markitdown trên VPS nếu OpenClaw cần dùng thường xuyên
pip install markitdown --break-system-packages
```
> ⚠️ Không cài vào Hermes runtime — vi phạm nguyên tắc "không pip ngoài" của Hermes. Chỉ dùng ở tầng Claude session hoặc OpenClaw.
