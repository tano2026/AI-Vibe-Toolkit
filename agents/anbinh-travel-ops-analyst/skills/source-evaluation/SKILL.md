---
name: source-evaluation
description: >
  Chấm độ tin cậy nguồn trước khi dùng bất kỳ thông tin nào để trả lời. BẮT BUỘC chạy
  trước khi output bất kỳ câu trả lời nào liên quan chính sách hàng không, nhập cảnh,
  giá dịch vụ đối thủ, hoặc số liệu thị trường. Dùng skill này mỗi khi agent chuẩn bị
  trích dẫn một nguồn, đặc biệt khi thông tin có thể đã thay đổi (giá vé, quy định visa,
  chính sách hành lý, giá dịch vụ ground handling).
---

# Source Evaluation

## Khi nào dùng
- Mọi câu trả lời có nhắc tới quy định/chính sách hàng không (IATA, hãng bay, nhập cảnh)
- Mọi số liệu về đối thủ (giá, thị phần, đánh giá dịch vụ)
- Bất kỳ thông tin nào có khả năng đã lỗi thời (giá, chính sách thay đổi theo thời gian)

## Quy trình
1. **Web search trước, không trả lời từ training data** với mọi câu hỏi loại trên — chính sách
   hàng không/visa thay đổi thường xuyên, không được giả định vẫn còn đúng.
2. Với mỗi nguồn tìm được, chấm theo 3 tiêu chí:
   - **Độ mới**: có ngày publish rõ ràng không? Có phải bản cập nhật gần nhất không?
   - **Thẩm quyền**: nguồn chính thức (hãng bay, IATA, cơ quan quản lý) hay bên thứ ba
     (blog, forum, aggregator)?
   - **Nhất quán**: có mâu thuẫn với nguồn khác không? Nếu có, flag rõ ràng, không tự chọn 1 bên.
3. Nếu không tìm được nguồn đủ tin cậy → nói rõ "không tìm được nguồn xác nhận, cần
   double-check trực tiếp với hãng bay/cơ quan liên quan" — KHÔNG bịa để có câu trả lời.
4. Luôn đính kèm disclaimer khi trả lời về chính sách nhập cảnh/hàng không: đây là thông tin
   tham khảo, không thay thế xác nhận chính thức từ hãng bay hoặc cơ quan quản lý.

## Ví dụ thực tế
**Input:** "Khách hỏi mang bao nhiêu ml chất lỏng lên máy bay quốc tế được?"
**Xử lý:** Web search quy định an ninh hàng không mới nhất (không dùng số liệu cũ từ
training) → tìm nguồn chính thức (TSA/ICAO hoặc quy định sân bay cụ thể) → nếu 2 nguồn
lệch nhau (vd sân bay nội địa vs quốc tế khác quy định) → flag rõ, hỏi lại tuyến bay cụ thể
nếu cần → trả lời kèm nguồn + disclaimer.

## Lưu ý
- Đây là skill NỀN, mọi skill khác trong agent này đều phải qua bước chấm nguồn này trước
  khi Synthesizer ra output cuối.
