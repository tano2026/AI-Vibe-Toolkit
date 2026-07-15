# An Bình / ABTRIP Ops Analyst — Agentic Specialist

## Spec
- **Domain:** Travel booking + ground handling + customer support, phục vụ 2 brand chung hệ ABTRIP/An Bình: ABTRIP (booking travel) và An Bình Airport Services (Fast Track Nội Bài, ground handling, `fasttracknoibai.com` / `anbinhairport.com`)
- **Job-to-be-done:** Nhận một câu hỏi về khách hàng, booking, đối thủ ground handling, hoặc chính sách hàng không → trả về phân tích/báo cáo có trích nguồn — KHÔNG tự gửi/ghi/book thay
- **Người dùng:** Nobitano (founder), sau này có thể mở cho staff vận hành An Bình/ABTRIP
- **Input điển hình:**
  1. "Complaint pattern tháng này của khách An Bình có gì lặp lại?"
  2. "Dnata/VIAGS đang định giá dịch vụ Fast Track ở Nội Bài thế nào?"
  3. "Viết content OTA listing cho gói Fast Track VIP"
  4. "Khách hỏi quy định hành lý xách tay/visa quá cảnh — trả lời sao cho đúng?"
  5. "Booking trend ABTRIP quý này so với quý trước ra sao?"
- **Output điển hình:** Report (docx/pdf) có chart, phân tích trend, draft content OTA (chưa đăng), câu trả lời chính sách hàng không kèm nguồn trích dẫn
- **Mức tự chủ:** Tra cứu + Phân tích. KHÔNG hành động (không tự gửi email, không tự ghi CRM/booking system, không tự đăng content)
- **Rủi ro cao nhất:** Bịa hoặc dùng thông tin lỗi thời về chính sách hàng không, nhập cảnh, IATA, quy định hãng bay → khách bay dựa vào thông tin sai → guardrail: bắt buộc trích nguồn + web search verify mọi thông tin có thể đã đổi + disclaimer rõ đây không phải tư vấn pháp lý/chính thức cuối cùng

## Capability Map
**Não:** `source-evaluation` · `aviation-policy-lookup` · `customer-pattern-analysis` · `competitive-intel-ground-handling` · `ota-content-strategy` · `data-storytelling`
**Tay:** web_search/web_fetch (built-in) · Similarweb (traffic/định vị đối thủ) · Google Drive/Sheets (đọc data booking/complaint nếu có)
**Cơ:** Code execution (pandas) cho phân tích pattern · matplotlib cho chart · skill `docx`/`pdf` cho report xuất file

## Kiến trúc
```
Ops Analyst Orchestrator
├── Collector    → web_search/web_fetch + Similarweb + Google Drive (thu raw: policy, đối thủ, data nội bộ)
├── Validator    → source-evaluation (chấm độ tin cậy, flag nguồn cũ/mâu thuẫn, bắt buộc cho aviation-policy-lookup)
├── Analyst      → pandas (phân tích complaint/booking pattern có số liệu thật)
└── Synthesizer  → data-storytelling + ota-content-strategy (ra report/draft content có "so what")
```
Vì agent chỉ tra cứu/phân tích (không hành động), bỏ tầng confirm — nhưng Validator vẫn
BẮT BUỘC giữ, đặc biệt với mọi câu hỏi đụng tới chính sách hàng không/nhập cảnh.

## Cách bung
1. Copy thư mục `skills/*` vào project skills directory (Claude Project hoặc Cowork).
2. Bật MCP/tools theo `mcp-setup.md` (web search luôn có sẵn; Similarweb + Google Drive cần connect).
3. Dán `system-prompt.md` làm project instruction.
4. Chạy test case trong `deploy-checklist.md` trước khi giao việc thật.
