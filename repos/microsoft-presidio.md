# Microsoft Presidio — GitHub Repo

## TL;DR
Phát hiện + ẩn danh PII (thông tin định danh cá nhân) trong text trước khi gửi cho model hoặc lưu log — vá đúng lỗ hổng đã phát hiện trước đó (rule Antigravity cho phép đọc `GEMINI_API_KEY` ra terminal) nhưng ở quy mô rộng hơn: số điện thoại khách hàng, số tài khoản ngân hàng, CCCD.

## Vì sao cần — rủi ro thật, không phải lý thuyết

Hệ thống đang xử lý data nhạy cảm thật: thông tin khách hàng ABTRIP, chi tiết hợp đồng PVN, số tài khoản ngân hàng ABTRIP. `destructive-command-guardrail` hiện chỉ chặn LỆNH nguy hiểm (rm -rf, DROP TABLE) — chưa có gì chặn NỘI DUNG nhạy cảm vô tình lọt vào log/context gửi cho model.

## Repo này dùng để làm gì
Quét text, nhận diện entity PII (tên, SĐT, email, số thẻ, địa chỉ, CCCD...) → tuỳ chọn ẩn danh (thay bằng placeholder) hoặc chặn hẳn trước khi gửi tiếp. Dùng được làm bước lọc TRƯỚC khi nội dung vào Claude/log, hoặc SAU khi model trả lời (chặn rò rỉ ra ngoài).

## Setup từng bước
```bash
pip install presidio-analyzer presidio-anonymizer
python -m spacy download en_core_web_lg
```
```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

text = "Khách hàng Nguyễn Văn A, SĐT 0912345678, số tài khoản 1903xxxxxxx"
results = analyzer.analyze(text=text, language="en")  # tiếng Việt cần config riêng
anonymized = anonymizer.anonymize(text=text, analyzer_results=results)
print(anonymized.text)  # "Khách hàng <PERSON>, SĐT <PHONE_NUMBER>, số tài khoản <NUMBER>"
```

⚠️ **Hỗ trợ tiếng Việt chưa chuẩn sẵn** — Presidio mặc định tối ưu tiếng Anh, cần tự thêm recognizer riêng cho định dạng CCCD/SĐT Việt Nam, chưa có sẵn, cần test kỹ trước khi tin dùng production.

## Vị trí trong hệ thống (đề xuất, chưa triển khai)

```
Nội dung vào (tin nhắn Zalo/log/data khách hàng)
        ↓
Presidio quét PII → ẩn danh nếu phát hiện
        ↓
Gửi tiếp cho model/lưu log (đã an toàn)
```

Áp được cho: log Hermes/OpenClaw trước khi lưu, nội dung gửi qua Langfuse (tránh PII thật xuất hiện trong dashboard quan sát), draft trả lời Customer Satisfaction Pro trước khi hiển thị.

## Ví dụ thực tế
`churn-risk-escalation-discipline` yêu cầu gắn cờ "kèm nguyên văn câu khách nói" — nếu câu đó chứa SĐT/thông tin tài khoản, Presidio ẩn danh trước khi đưa vào báo cáo/log, tránh rò rỉ qua Langfuse hay bất kỳ nơi lưu trữ nào.

## Lưu ý / Lỗi thường gặp
- Dùng model tiếng Anh mặc định cho text tiếng Việt — độ chính xác nhận diện PII sẽ thấp, cần test/tinh chỉnh riêng
- Chỉ chạy 1 chiều (đầu vào) mà quên chạy cả đầu ra (output model có thể vô tình lặp lại PII đã đọc trong context)

## Đánh giá cá nhân
- Điểm mạnh: MIT, từ Microsoft (đáng tin), giải đúng rủi ro thật đã xác nhận (PII trong data khách hàng/tài chính thật)
- Điểm yếu: cần tự làm thêm việc hỗ trợ tiếng Việt, chưa có sẵn — đáng kể công sức tích hợp thật, không phải cắm là chạy
- Có nên dùng: 7/10 — đáng làm, nhưng ưu tiên sau khi giải quyết các điểm nghẽn cấp thiết hơn (Claude Code, DeepSeek Harness)

## Link
- Repo: https://github.com/microsoft/presidio
- Docs: microsoft.github.io/presidio
- Dùng cùng: agents/company/skills/ (đề xuất thêm vào nhóm Đầu Não), repos/langfuse.md (tránh PII lọt vào dashboard quan sát)

---

## Ghi chú — NeMo Guardrails (bổ sung, không viết riêng file)

Nếu cần chặn ở TẦNG HÀNH ĐỘNG (không chỉ PII trong text) — `NeMo Guardrails` (NVIDIA, Apache 2.0) là lựa chọn phù hợp, bổ sung cho `destructive-command-guardrail` đã có, không thay thế. Để dành nghiên cứu sâu khi cần.

⚠️ **LLM Guard (Protect AI) — đã bị khai tử tháng 7/2026, không còn cập nhật** — loại khỏi danh sách cân nhắc dù vẫn xuất hiện trong nhiều bài so sánh cũ.
