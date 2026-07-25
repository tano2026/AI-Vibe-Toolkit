# Claude for Legal (anthropics) + claude-legal-skill (evolsb) — GitHub Repo

## TL;DR
2 nguồn cho năng lực pháp lý: bản chính thức của Anthropic (60+ plugin, đủ mảng từ hợp đồng thương mại tới M&A) và bản nhẹ portable (1 skill duy nhất, dùng CUAD dataset để chấm rủi ro điều khoản). **Cảnh báo quan trọng nhất: cả 2 đều thiên US law**, cần review lại bởi luật sư VN thật cho hợp đồng thật của ABTRIP.

## Repo này dùng để làm gì
**`anthropics/claude-for-legal`** — bộ plugin chính thức, chia theo mảng hành nghề: hợp đồng
thương mại (review vendor/NDA/SaaS theo playbook, theo dõi renewal), M&A diligence, privacy
(PIA/DPIA/DPA), marketing claims check, employment (hire/termination review theo jurisdiction).
Mỗi agent có "cold-start interview" học playbook riêng của tổ chức trước khi làm việc.

**`evolsb/claude-legal-skill`** — nhẹ hơn nhiều, 1 skill duy nhất, dựa trên CUAD dataset (41
loại rủi ro điều khoản) + benchmark ContractEval + LegalBench. Đọc hợp đồng, gắn cờ điều khoản
bất lợi, so sánh với chuẩn thị trường, đề xuất redline. F1 ~0.62 trên clause extraction theo
benchmark — tốt cho review lần đầu/gắn cờ vấn đề, KHÔNG thay thế luật sư cho deal quan trọng.

## Setup từng bước
1. Bản nhẹ (khuyên dùng trước, dễ tích hợp Hermes/OpenClaw hơn):
```bash
git clone https://github.com/evolsb/claude-legal-skill ~/Developer/claude-legal-skill
ln -s ~/Developer/claude-legal-skill ~/.claude/skills/contract-review
```
2. Bản đầy đủ Anthropic (nếu cần nhiều mảng hơn — M&A, privacy, employment):
```bash
git clone https://github.com/anthropics/claude-for-legal.git
```
Xem docs cài từng plugin riêng theo mảng cần (commercial, privacy, employment...).
3. Trigger tự nhiên: "Review hợp đồng ground handling này, tao là bên nhận dịch vụ" — skill tự
đọc file PDF/DOCX hợp đồng, phân tích theo vai trò (bên mua/bên bán/bên nhận).

## Ví dụ thực tế
ABTRIP ký hợp đồng ground handling B2B mới với 1 đối tác — trước khi CEO ký, chạy qua
`claude-legal-skill` để có bản review lần đầu: gắn cờ điều khoản indemnification bất lợi, điều
khoản chấm dứt hợp đồng mập mờ, so sánh với chuẩn thị trường — CEO có bản tóm tắt rủi ro trước
khi đưa cho luật sư thật review sâu, tiết kiệm thời gian luật sư chỉ tập trung vào điểm đã gắn cờ.

## Lưu ý / Lỗi thường gặp
- **US law focus** — phân tích mặc định theo luật Mỹ, điều khoản/rủi ro có thể khác hẳn khung
  pháp lý Việt Nam (Bộ luật Dân sự, Luật Thương mại VN). CHỈ dùng như bước sàng lọc sơ bộ, KHÔNG
  bao giờ thay thế luật sư VN thật cho hợp đồng có giá trị/rủi ro cao.
- Hợp đồng dài cần review theo từng phần (context window giới hạn), không nhồi cả hợp đồng dài
  vào 1 lần.
- F1 ~0.62 nghĩa là còn khoảng 38% điều khoản có thể bị bỏ sót hoặc gắn nhầm — luôn tự đọc lại
  toàn bộ, không tin tuyệt đối vào output.
- Không phải lời khuyên pháp lý chính thức (skill tự ghi rõ "Not legal advice").

## Đánh giá cá nhân
- Điểm mạnh: miễn phí, mở nguồn, tích hợp trực tiếp vào Claude Code — tiết kiệm bước review sơ
  bộ trước khi đưa luật sư; bản Anthropic chính thức đủ mảng nếu sau này ABTRIP mở rộng cần
  review privacy/employment.
- Điểm yếu: US law bias là rủi ro lớn nhất — dùng sai ngữ cảnh dễ gây hiểu nhầm về nghĩa vụ
  pháp lý thật tại VN; độ chính xác F1 0.62 chưa đủ tin tưởng hoàn toàn.
- Có nên dùng không: 6.5/10 — hữu ích làm bước sàng lọc sơ bộ, giảm tải cho luật sư, nhưng
  TUYỆT ĐỐI không thay thế tư vấn pháp lý thật cho hợp đồng quan trọng tại VN.

## Link
- Bản chính thức Anthropic: https://github.com/anthropics/claude-for-legal
- Bản nhẹ portable: https://github.com/evolsb/claude-legal-skill
