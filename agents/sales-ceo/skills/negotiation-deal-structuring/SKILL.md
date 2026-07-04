---
name: negotiation-deal-structuring
description: >
  Cấu trúc và đàm phán deal B2B — tính BATNA, xây concession ladder, phát hiện điểm
  neo giá, thiết kế deal terms (thanh toán, cam kết, exit clause). Dùng khi user hỏi
  "deal này có nên giảm giá không", "khách đòi X, phản ứng sao", "cấu trúc gói giá
  cho hợp đồng lớn", "thương lượng payment terms".
---

# Negotiation & Deal Structuring

## TL;DR
Skill này giúp KHÔNG bước vào đàm phán với tay không — luôn có BATNA rõ, biết mình
nhường được tới đâu, và cấu trúc deal sao cho không lỗ dù khách ép giá.

## Khi nào dùng
- Khách đòi giảm giá/thêm ưu đãi
- Cần thiết kế payment terms cho hợp đồng lớn (trả trước/trả sau, milestone)
- Deal có rủi ro pháp lý (exit clause, penalty, SLA)
- Chuẩn bị trước 1 buổi đàm phán quan trọng

## Quy trình

### 1. Xác định BATNA (Best Alternative To Negotiated Agreement)
- Nếu deal này không xảy ra, phương án B là gì? (khách khác, giữ giá, bỏ qua)
- BATNA yếu → thế đàm phán yếu, cần biết trước để không hoảng khi bị ép.

### 2. Tính điểm hòa vốn (walk-away point)
- Giá/điều khoản thấp nhất mà vẫn còn lời — tính rõ bằng số, không cảm tính.
- Dùng `finance-billing-ops` để lấy data chi phí thật, không đoán.

### 3. Xây concession ladder
- Liệt kê 3-4 nhượng bộ có thể cho, xếp theo thứ tự chi phí thấp → cao với mình:
  1. Nhượng bộ rẻ (VD: thêm support, kéo dài trial) — cho trước
  2. Nhượng bộ vừa (VD: giảm giá 5-10% có điều kiện volume/cam kết dài hạn)
  3. Nhượng bộ đắt (VD: giảm giá sâu >15%) — chỉ cho nếu đổi lại được gì tương xứng
  4. Never (điều khoản không bao giờ nhượng — VD: điều khoản pháp lý bảo vệ mình)

### 4. Đề xuất deal terms cụ thể
- Thanh toán: trả trước bao %, milestone nào, penalty trễ hạn
- Cam kết: thời hạn hợp đồng, điều khoản gia hạn
- Exit clause: điều kiện hủy hợp đồng, ai chịu phí gì

### 5. Output khuyến nghị
Luôn kết thúc bằng:
```
Khuyến nghị: [1 hướng rõ ràng]
Rủi ro: [downside cụ thể nếu làm theo khuyến nghị này]
Điểm dừng: [walk-away point — dưới mức này thì không nên đồng ý]
```

## Ví dụ thực tế
User: "Khách ABTRIP đòi giảm 30% cho gói tour doanh nghiệp, có nên đồng ý không?"
→ Agent: tính chi phí thật của gói → walk-away point là giảm tối đa 12% mới còn lời →
đề xuất: giảm 10% + đổi lại cam kết đặt tối thiểu 20 tour/năm (concession ladder bậc 2,
không nhảy thẳng lên bậc 3) → Rủi ro: nếu khách không cam kết volume, margin âm.

## Lưu ý / Lỗi thường gặp
- Đừng nhượng bộ ngay ở request đầu tiên — luôn có ít nhất 1 câu hỏi ngược lại trước
  khi cho concession.
- Đừng gộp nhiều nhượng bộ cùng lúc — cho từng bậc, giữ đòn bẩy cho lần sau.
- Agent KHÔNG tự chốt deal — chỉ đưa khuyến nghị, người thật xác nhận trước khi gửi khách.

## Đánh giá cá nhân
- Điểm mạnh: buộc phải có số liệu walk-away point trước khi đàm phán, tránh cảm tính.
- Điểm yếu: không thay được kinh nghiệm đọc tâm lý khách trực tiếp — đây là khung tư duy,
  không phải script cứng.
- Có nên dùng không: 8/10 — bắt buộc trước mọi deal >10% giá trị hợp đồng trung bình.
