---
name: churn-risk-escalation-discipline
description: >
  Vận hành hoá ngưỡng số EXPERT-CORE.md section 8 (Customer Satisfaction) —
  SLA phản hồi theo kênh, FCR, và luật quan trọng nhất: 1 lần phục vụ tệ
  đã đủ rủi ro rời bỏ, không đợi lặp lại. Dùng khi quét inbox/comment/ticket
  hỗ trợ khách hàng cho bất kỳ brand nào (ABTRIP/Tano Cafe/Wonder Mart...).
---

# Churn Risk & Escalation Discipline

## TL;DR
1 khách phàn nàn nặng = xử lý như khẩn cấp ngay từ lần đầu, không đợi "xem có lặp lại không" — khác hẳn luật comment thường (escalate ở lần thứ 3). Đây là điểm phân biệt quan trọng nhất: khiếu nại nhỏ khác bản chất với tín hiệu rời bỏ.

## Khi nào dùng
- Quét inbox/ticket/comment hỗ trợ khách hàng
- Phân loại độ khẩn cấp trước khi trả lời
- Báo cáo hiệu suất CSKH định kỳ

## Nội dung skill / prompt

### Bước 1 — Phân loại NGAY khi đọc, trước khi soạn trả lời

```
Tín hiệu RỜI BỎ THẬT (escalate ngay lần đầu, không đợi lặp lại):
  - Nói thẳng ý định huỷ/chuyển đối thủ ("chắc lần sau không dùng nữa")
  - Thất vọng nặng có bằng chứng cụ thể (số tiền, thời gian mất, hậu quả)
  - Yêu cầu hoàn tiền/bồi thường

Phàn nàn NHỎ (áp luật thường — escalate khi lặp lại >=3 lần):
  - Câu hỏi lặp lại về cùng 1 tính năng/chính sách
  - Nhầm lẫn không có thiệt hại thật
```

### Bước 2 — Áp đúng SLA theo kênh (từ EXPERT-CORE 8)

```
Chat: <=40 giây | Email thường: <=4h | Email ưu tiên: <=1-2h | Social: <=60 phút
```

### Bước 3 — Soạn câu trả lời khó TRƯỚC (đúng thứ tự ưu tiên)

```
Xếp hàng đợi theo độ khó GIẢM DẦN — trả lời câu khó/rủi ro cao trước,
câu dễ để sau. Ngược lại thói quen thường (trả câu dễ trước cho nhanh
xong việc) — nhưng câu khó càng để lâu càng tăng rủi ro rời bỏ.
```

### Bước 4 — Gắn cờ kèm bằng chứng, không chỉ gắn cờ suông

```
Mỗi case gắn cờ "rủi ro rời bỏ" PHẢI kèm:
  - Trích nguyên văn câu khách nói (không diễn giải lại)
  - Thời gian đã trôi qua từ lúc nhận được
  - Giá trị/lịch sử khách (nếu có data) — khách VIP rủi ro cao hơn khách mới
```

### Báo cáo định kỳ — dùng median/P90, không dùng trung bình

```
Đúng luật EXPERT-CORE 8: "X% ticket trả lời trong Y giờ" — KHÔNG báo
"thời gian phản hồi trung bình Z giờ" (dễ bị outlier làm sai lệch)
```

## Setup từng bước
1. Quét inbox/comment mới → chạy Bước 1 phân loại ngay
2. Tín hiệu rời bỏ thật → escalate ngay, không đợi
3. Còn lại → xếp hàng theo SLA kênh + độ khó giảm dần
4. Soạn trả lời, gắn cờ kèm bằng chứng nếu là case rủi ro
5. Báo cáo cuối kỳ theo median/P90

## Ví dụ thực tế
Khách Wonder Mart nhắn "đặt hàng 3 ngày chưa thấy, định huỷ luôn không mua nữa" — dù đây là LẦN ĐẦU khách phàn nàn, câu "định huỷ" là tín hiệu rời bỏ thật → escalate ngay, không đợi xem có phàn nàn lần 2 không. Ngược lại, khách hỏi "shop có ship COD không" 3 lần liên tiếp (không phải dấu hiệu rời bỏ) → áp luật thường, escalate ở lần thứ 3 để xem lại vì sao câu trả lời cũ không rõ.

## Lưu ý / Lỗi thường gặp
- Áp nhầm luật ">=3 lần mới escalate" (dùng cho comment thường) vào tín hiệu rời bỏ thật — sai, tín hiệu rời bỏ escalate ngay từ lần đầu
- Trả lời câu dễ trước để "xong việc nhanh" — sai thứ tự, câu khó/rủi ro cao phải ưu tiên
- Báo cáo bằng số trung bình — dễ che giấu vấn đề thật (vài ca outlier kéo trung bình lệch, ẩn đi phần lớn case đang chậm)

## Đánh giá cá nhân
- Điểm mạnh: ngưỡng số có nguồn thật (SQM Group, HubSpot, Zendesk 2026), không suy đoán; phân biệt rõ 2 loại escalate (thường vs rủi ro rời bỏ) — tránh cả 2 lỗi (escalate quá tay lẫn phản ứng quá chậm)
- Điểm yếu: cần data lịch sử khách (VIP/mới) để gắn cờ chính xác — nếu chưa có CRM đủ tốt, phần "giá trị khách" trong Bước 4 khó áp dụng đầy đủ
- Có nên dùng: 9/10 — đây là mảng duy nhất trong 8 Pro Agent trực tiếp gắn với rủi ro mất doanh thu định lượng được (94% vs 78% tái ký hợp đồng chỉ từ tốc độ phản hồi)

## Link
- Nguồn số liệu: SQM Group FCR 2025, SuperOffice/GreetNow response-time study, HubSpot State of Service 2025, Zendesk CX Trends 2026
- Nguồn gốc luật: agents/company/EXPERT-CORE.md section 8
