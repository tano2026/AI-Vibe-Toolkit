---
name: aviation-policy-lookup
description: >
  Tra cứu quy định hàng không, nhập cảnh, hành lý, an ninh sân bay để trả lời câu hỏi
  của khách hoặc staff An Bình/ABTRIP. CHỈ tra cứu và trình bày thông tin — không tự
  quyết định thay khách, không tự xác nhận chính sách cuối cùng thay hãng bay. Dùng khi
  có câu hỏi kiểu "quy định về X là gì", "hành lý xách tay được mang gì", "visa quá cảnh
  cần gì", "thủ tục Fast Track/ground handling ở Nội Bài ra sao".
---

# Aviation Policy Lookup

## Khi nào dùng
- Khách hàng hoặc staff hỏi về quy định hành lý, an ninh, nhập cảnh, quá cảnh
- Câu hỏi về quy trình Fast Track/ground handling cụ thể tại Nội Bài
- Bất kỳ câu hỏi nào cần trích dẫn tiêu chuẩn IATA hoặc quy định hãng bay cụ thể

## Quy trình
1. Xác định phạm vi câu hỏi: quy định chung (IATA/ICAO) hay quy định riêng của 1 hãng bay/
   1 sân bay cụ thể — 2 loại này có thể khác nhau, không gộp chung.
2. **Luôn chạy `source-evaluation` trước** — không trả lời trực tiếp từ trí nhớ vì quy định
   hay đổi.
3. Trình bày câu trả lời theo cấu trúc:
   - Quy định chung áp dụng (nếu có)
   - Ngoại lệ/khác biệt theo hãng bay hoặc tuyến cụ thể (nếu biết)
   - Nguồn trích dẫn
   - Disclaimer: khuyến nghị khách xác nhận lại trực tiếp với hãng bay trước ngày bay,
     vì quy định có thể thay đổi không báo trước
4. KHÔNG tự đưa ra cam kết thay An Bình/ABTRIP về việc "chắc chắn được phép" — chỉ nói
   "theo quy định hiện tại (nguồn X), thường được phép, nhưng nên xác nhận lại".

## Ví dụ thực tế
**Input:** "Khách quá cảnh ở Nội Bài đi tiếp quốc tế cần visa quá cảnh không?"
**Xử lý:** Web search quy định quá cảnh mới nhất áp dụng cho quốc tịch khách (nếu biết) →
nếu không biết quốc tịch, hỏi lại 1 câu trước khi trả lời chung chung → trả lời có nguồn
+ khuyến nghị xác nhận lại với hãng bay/Đại sứ quán.

## Lưu ý / giới hạn
- Đây KHÔNG phải công cụ Timatic chính thức — chỉ là tra cứu hỗ trợ, không thay thế hệ
  thống nhập cảnh chuẩn mà đại lý vé dùng.
- Không tự động hoá quyết định check-in/từ chối khách dựa trên skill này.
