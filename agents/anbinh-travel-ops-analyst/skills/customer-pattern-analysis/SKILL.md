---
name: customer-pattern-analysis
description: >
  Phân tích pattern trong complaint, feedback, hoặc dữ liệu booking của khách hàng ABTRIP/
  An Bình để tìm vấn đề lặp lại và cơ hội cải thiện dịch vụ. Dùng khi user hỏi "khách phàn
  nàn gì nhiều nhất", "booking trend thế nào", "vấn đề nào lặp lại tháng này", hoặc paste/
  upload data complaint, review, booking export.
---

# Customer Pattern Analysis

## Khi nào dùng
- Có data thật (CSV export, Google Sheets, text paste) về complaint/booking/review
- Câu hỏi dạng trend/pattern theo thời gian ("tháng này so với tháng trước")
- Cần tìm top vấn đề để ưu tiên cải thiện dịch vụ

## Quy trình
1. Nếu có file data → dùng code execution (pandas) đọc và làm sạch, KHÔNG suy diễn số liệu
   khi chưa có data thật.
2. Nếu chưa có data → hỏi rõ nguồn (export QuickBooks/CRM, Google Sheet link, hay paste tay)
   thay vì tự bịa số liệu minh hoạ.
3. Nhóm complaint/feedback theo chủ đề (vd: chậm trễ, thái độ nhân viên, giá, thủ tục giấy tờ)
   — đếm tần suất, không chỉ liệt kê ví dụ đơn lẻ.
4. So sánh theo thời gian nếu có đủ dữ liệu (tháng này vs tháng trước) — dùng chart
   (matplotlib) để trực quan hoá.
5. Ra "so what": không chỉ liệt kê số liệu, mà chỉ rõ 2-3 vấn đề cần ưu tiên xử lý và vì sao.
6. KHÔNG tự động soạn phản hồi gửi khách hoặc ghi log CRM — chỉ ra insight, để Nobitano
   quyết định bước tiếp theo.

## Ví dụ thực tế
**Input:** User paste 20 dòng feedback khách Fast Track tháng 6-7/2026.
**Xử lý:** Đọc qua pandas → nhóm theo chủ đề (thời gian chờ, giao tiếp nhân viên, giá) →
đếm tần suất mỗi nhóm → vẽ bar chart → kết luận: "60% complaint liên quan thời gian chờ tại
kiosk — đây là vấn đề ưu tiên số 1, không phải giá dịch vụ như giả định ban đầu."

## Lưu ý
- Không đủ data (dưới ~10 điểm) → nói rõ mẫu quá nhỏ để kết luận chắc chắn, tránh phóng đại.
