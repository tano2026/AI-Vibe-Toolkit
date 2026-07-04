---
name: ceo-decision-lens
description: >
  Khung ra quyết định cấp CEO cho bài toán kinh doanh mơ hồ — đánh giá theo 3 trục:
  risk (rủi ro), return (lợi ích), reversibility (có đảo ngược được không). Dùng khi
  user hỏi "có nên làm X không", "quyết định này có ổn không", trước khi cam kết resource
  lớn, pricing, pháp lý, hoặc mở rộng sang hướng mới.
---

# CEO Decision Lens

## TL;DR
Trước khi ra bất kỳ quyết định kinh doanh nào có rủi ro, chạy qua 3 trục:
**Risk / Return / Reversibility**. Quyết định dễ đảo ngược thì làm nhanh không cần
phân tích nhiều; quyết định khó đảo ngược thì phải chậm, kỹ, và thường nên qua `council`.

## Khi nào dùng
- Trước khi cam kết giá dài hạn cho khách
- Trước khi mở rộng/đóng 1 dòng sản phẩm/dịch vụ
- Trước khi ký hợp đồng có điều khoản ràng buộc lâu dài
- Trước khi thay đổi pricing tier ảnh hưởng toàn bộ khách hàng

## Khung 3 trục

### 1. Risk — rủi ro nếu quyết định này sai
- Tài chính: mất bao nhiêu tiền nếu sai? (số cụ thể, không mập mờ)
- Pháp lý: có ràng buộc hợp đồng/quy định nào bị vi phạm không?
- Thương hiệu/quan hệ: ảnh hưởng tới khách hàng khác/thị trường thế nào?

### 2. Return — lợi ích nếu đúng
- Định lượng được không? (doanh thu tăng thêm, thời gian tiết kiệm, quan hệ mở ra)
- Nếu không định lượng được → nghi ngờ, có thể đang quyết định theo cảm tính.

### 3. Reversibility — có rút lại được không
- **Dễ đảo ngược** (VD: thử 1 chiến dịch outbound nhỏ, giảm giá 1 đơn) → quyết nhanh,
  không cần phân tích sâu, coi như thử nghiệm.
- **Khó đảo ngược** (VD: ký hợp đồng 2 năm, đổi pricing tier toàn công ty, sa thải người) →
  BẮT BUỘC chậm lại, chạy qua `council` để có tranh luận đối lập trước khi chốt.

## Ma trận quyết định

| Reversibility | Risk thấp | Risk cao |
|---|---|---|
| **Dễ đảo ngược** | Làm ngay, không cần hỏi | Làm thử quy mô nhỏ, review sau |
| **Khó đảo ngược** | Cân nhắc kỹ, có data rõ mới làm | Chạy `council` trước, không tự chốt |

## Output format bắt buộc
```
Trục Risk:          [cụ thể, có số]
Trục Return:        [cụ thể, có số hoặc nói rõ "chưa định lượng được"]
Trục Reversibility: [dễ/khó đảo ngược, vì sao]
→ Khuyến nghị:      [1 hướng rõ]
→ Rủi ro:           [downside cụ thể]
```

## Ví dụ thực tế
User: "Có nên đổi toàn bộ pricing tier của Wonder Mart sang subscription không?"
→ Risk: khách hiện tại quen mua lẻ, có thể churn ngắn hạn (khó đo % chính xác, cần A/B
test trước) | Return: LTV tăng nếu retention tốt, nhưng chưa có data retention thật |
Reversibility: khó đảo ngược (đổi lại tốn công truyền thông 2 lần, mất niềm tin khách)
→ Khuyến nghị: KHÔNG đổi toàn bộ ngay, chạy thử subscription cho 1 nhóm sản phẩm nhỏ
3 tháng trước → Rủi ro: nếu không thử trước, đổi sai hướng thì thiệt hại thương hiệu lớn.

## Lưu ý / Lỗi thường gặp
- Đừng nhảy thẳng vào khuyến nghị mà bỏ qua bước liệt kê 3 trục — dễ quyết định theo
  cảm tính rồi hợp lý hóa ngược.
- "Chưa định lượng được Return" không có nghĩa là bỏ qua — nói thẳng ra để Nobitano biết
  đang quyết định dựa trên thiếu data.

## Đánh giá cá nhân
- Điểm mạnh: ép phải tách rõ rủi ro/lợi ích/khả năng đảo ngược, tránh quyết định cảm tính.
- Điểm yếu: không có công thức tính điểm tự động — vẫn cần con người/agent đánh giá định
  tính ở 1 số chỗ (đặc biệt trục Return khi chưa có data).
- Có nên dùng không: 9/10 — nên là bước bắt buộc trước mọi quyết định khó đảo ngược.
