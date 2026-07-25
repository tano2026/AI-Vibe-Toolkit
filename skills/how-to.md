---
name: how-to
description: >
  - "Tao chưa biết làm cái này thế nào" - "Vạch ra các bước cần làm cho X"
  - "Task này phức tạp, chia nhỏ giúp tao"
---

# How-To — Skill

## TL;DR
Bước 03 trong chuỗi 9 skill "prompt chain" (xem `stacks/chuoi-9-buoc-viet-prompt.md`) — nhận 1 mục tiêu chưa rõ cách làm, vạch ra các bước cụ thể để đạt tới, dùng sau `grill-me` (khi câu hỏi đã đủ rõ nhưng chưa biết quy trình).

## Khi nào dùng
- Biết muốn gì nhưng chưa biết làm sao tới đó
- Task phức tạp cần chia nhỏ thành các bước verify được
- Sau khi `grill-me` đã làm rõ yêu cầu, giờ cần lộ trình thực hiện

## Nội dung skill / prompt
```
Bạn nhận 1 mục tiêu đã rõ ràng (không còn mơ hồ) nhưng người dùng chưa biết quy trình để đạt
tới. Nhiệm vụ: vạch ra các bước cụ thể, mỗi bước có tiêu chí "xong" đo lường được.

QUY TRÌNH:
1. Xác nhận lại mục tiêu cuối cùng bằng 1 câu
2. Liệt kê các bước theo thứ tự phụ thuộc (bước nào cần bước nào trước)
3. Mỗi bước ghi: [Hành động] → verify: [cách biết đã xong đúng]
4. Đánh dấu bước nào rủi ro cao nhất / dễ sai nhất
5. Không đưa quá 7 bước — nếu nhiều hơn, gộp thành giai đoạn lớn rồi breakdown riêng từng giai đoạn khi cần

OUTPUT:
- Lộ trình dạng số thứ tự, mỗi bước 1-2 dòng
- Ghi rõ bước nào có thể làm song song, bước nào bắt buộc tuần tự
```

## Ví dụ thực tế
Input: "Tao muốn RIO Bot chạy được thật trên VPS" → Output: 5 bước (test local trước → set env vars → wire OMNIROUTE nếu cần → chạy pm2 → verify 1 research request thật), mỗi bước có cách verify riêng, đánh dấu bước "wire OMNIROUTE" là optional không bắt buộc.

## Đánh giá cá nhân
- Có nên dùng không: 7/10 — hữu ích khi task mới, chưa có quy trình sẵn; không cần cho task đã quen tay.

## Link
- Thuộc chuỗi: `stacks/chuoi-9-buoc-viet-prompt.md` — bước 03/09
