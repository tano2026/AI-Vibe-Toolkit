---
name: personal-voice
description: >
  - "Chỉnh prompt này nghe giống giọng tao" - "Đừng để AI viết, để nó nghe như tao viết"
---

# Personal Voice — Skill

## TL;DR
Bước 06 trong chuỗi 9 skill — chỉnh prompt để output nghe đúng giọng văn của người dùng cụ
thể, không phải giọng AI trung tính. Với Nobitano: giọng casual, tiếng Việt, "tao/mày", đi
thẳng vấn đề, đưa recommendation rõ ràng thay vì liệt kê option trung lập.

## Khi nào dùng
- Prompt sẽ tạo ra content xuất bản trực tiếp (không qua biên tập) — cần đúng giọng ngay
- Sau bước optimize (04) hoặc fable (05), trước khi strip AI-tells (07)

## Nội dung skill / prompt
```
Nhận 1 prompt đã tối ưu về nội dung/cấu trúc. Chèn thêm chỉ dẫn giọng văn cụ thể của người
dùng vào cuối prompt — KHÔNG viết chung chung "giọng thân thiện", mà mô tả đặc điểm cụ thể:

1. Xưng hô: tao/mày hay tôi/bạn hay Anh/Chị — chốt đúng 1 kiểu, không trộn
2. Độ dài câu: ngắn gọn đi thẳng vấn đề, hay dài có văn phong bay bổng
3. Có/không dùng emoji, có/không dùng thuật ngữ kỹ thuật không giải nghĩa
4. Thái độ: đưa 1 khuyến nghị rõ ràng, hay liệt kê nhiều option trung lập để người đọc tự chọn
5. Câu cấm: liệt kê 2-3 cụm từ/kiểu câu người dùng ghét nghe AI nói (vd "trong thế giới ngày
   nay", "không thể phủ nhận rằng")

OUTPUT: prompt gốc + đoạn "Voice Guide" chèn thêm, ngắn gọn 4-6 dòng.
```

## Ví dụ thực tế
Prompt gốc: "Viết báo cáo tóm tắt research." → thêm Voice Guide: "Giọng tao/mày, tiếng Việt,
casual. Đi thẳng vào kết luận trước, không mở bài dài dòng. Đưa 1 khuyến nghị rõ ràng thay vì
liệt kê nhiều lựa chọn. Cấm dùng 'trong thế giới ngày nay', 'không thể phủ nhận'."

## Đánh giá cá nhân
- Có nên dùng không: 8/10 — quan trọng cho content xuất bản trực tiếp; ít cần cho task nội bộ
  chỉ CEO đọc 1 lần.

## Link
- Thuộc chuỗi: `stacks/chuoi-9-buoc-viet-prompt.md` — bước 06/09
