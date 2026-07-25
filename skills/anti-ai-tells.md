---
name: anti-ai-tells
description: >
  - "Bản draft này đọc rõ là AI viết, fix giúp" - "Strip AI tells khỏi đoạn này"
---

# Anti-AI (chống dấu vết AI) — Skill

## TL;DR
Bước 07 trong chuỗi 9 skill — quét và loại bỏ "dấu vết AI" điển hình khỏi bản draft: cụm từ
sáo rỗng, cấu trúc lặp máy móc, giọng văn quá cân bằng/trung tính không tự nhiên.

## Khi nào dùng
- Sau khi đã có draft nội dung (từ bước 04/05/06), trước khi giao xuất bản
- Đọc lại thấy "nghe rõ là AI viết" dù nội dung đúng

## Nội dung skill / prompt
```
Quét đoạn text, tìm và sửa các dấu hiệu "AI tells" phổ biến:

1. CỤM SÁO RỖNG: "trong thế giới ngày nay", "không thể phủ nhận rằng", "đóng vai trò quan
   trọng trong việc", "delve into", "game-changer", "revolutionize" → xoá hoặc viết lại cụ thể
2. CẤU TRÚC LẶP MÁY MÓC: mọi đoạn đều bắt đầu bằng "Đầu tiên/Thứ hai/Cuối cùng", mọi câu đều
   dài tương đương nhau → phá nhịp, trộn câu ngắn-dài tự nhiên
3. GIỌNG QUÁ CÂN BẰNG: luôn đưa "mặt tốt và mặt xấu" cho mọi thứ kể cả khi không cần → cắt bớt,
   chỉ giữ khi thật sự có tranh cãi 2 chiều
4. THỪA TỪ ĐỆM: "Điều quan trọng cần lưu ý là", "Cần phải nói rằng" → xoá thẳng, vào thẳng ý
5. KẾT LUẬN THỪA: đoạn cuối tóm tắt lại y hệt những gì đã nói → xoá nếu không thêm giá trị mới

OUTPUT: bản đã sửa + liệt kê ngắn gọn đã sửa những dấu hiệu nào (để người dùng học được pattern,
không chỉ nhận bản sửa mà không biết vì sao).
```

## Ví dụ thực tế
Trước: "Trong thế giới ngày nay, việc tối ưu hoá quy trình đóng vai trò quan trọng trong việc
nâng cao hiệu suất." → Sau: "Tối ưu quy trình giúp tăng hiệu suất rõ rệt."

## Đánh giá cá nhân
- Có nên dùng không: 8/10 — nên chạy qua bước này cho MỌI content xuất bản, không tốn nhiều
  công nhưng cải thiện chất lượng đọc rõ rệt.

## Link
- Thuộc chuỗi: `stacks/chuoi-9-buoc-viet-prompt.md` — bước 07/09
