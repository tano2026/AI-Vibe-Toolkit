---
name: data-storytelling
description: >
  Biến số liệu/phân tích thô thành report có "so what" rõ ràng — insight, không chỉ dump
  bảng số. Dùng làm bước cuối (Synthesizer) cho mọi phân tích trong agent này trước khi
  xuất báo cáo docx/pdf cho Nobitano.
---

# Data Storytelling

## Khi nào dùng
- Sau khi Analyst đã có số liệu/chart từ `customer-pattern-analysis` hoặc
  `competitive-intel-ground-handling`
- Trước khi xuất file report cuối cùng (docx/pdf)

## Quy trình
1. Không mở đầu bằng bảng số — mở đầu bằng kết luận chính (insight quan trọng nhất) trước,
   số liệu đi sau để chứng minh.
2. Mỗi insight phải trả lời được câu "vậy thì sao" — nếu chỉ là quan sát ("30% complaint về
   giá") mà không kèm hành động gợi ý ("nên xem lại minh bạch giá trước khi khách đặt") thì
   chưa đủ.
3. Giới hạn tối đa 3 insight chính mỗi report — nhiều hơn thì loãng, không ai nhớ được.
4. Dùng chart tối giản (matplotlib), không làm dashboard rối mắt cho 1 báo cáo ngắn.
5. Kết thúc bằng 2-3 khuyến nghị hành động cụ thể (nhưng KHÔNG tự thực hiện — để Nobitano
   quyết định và giao việc tiếp).

## Ví dụ thực tế
**Input:** Số liệu thô: 60% complaint về thời gian chờ, 25% về giá, 15% về thái độ nhân viên.
**Output:** "Insight chính: thời gian chờ là vấn đề số 1, gấp đôi vấn đề giá — ngược với giả
định ban đầu là giá đắt khiến khách phàn nàn. Khuyến nghị: ưu tiên tối ưu quy trình kiosk
trước khi điều chỉnh giá."

## Lưu ý
- Nếu data không đủ mạnh để rút insight chắc chắn, nói rõ giới hạn thay vì cố kết luận
  quá tay.
