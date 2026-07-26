---
name: fable-prompter
description: >
  - "Polish prompt này cho Claude Fable" - "Tối ưu prompt cho model sáng tạo"
---

# Fable Prompter — Skill

## TL;DR
Bước 05 trong chuỗi 9 skill (xem `stacks/chuoi-9-buoc-viet-prompt.md`) — giống bước 04
`prompt-optimizer` nhưng chỉnh riêng cho các model thiên về sáng tạo/reasoning dài (Claude
Fable 5, Claude Mythos-tier) thay vì model chuẩn task-execution.

## Khi nào dùng
- Prompt sẽ chạy trên model thiên sáng tạo (viết truyện, brainstorm, content GMSP) thay vì
  task kỹ thuật thuần
- Cần prompt giữ được "chất" sáng tạo, không bị optimizer chuẩn làm cứng nhắc/khô khan

## Nội dung skill / prompt
```
Nhận 1 prompt đã được optimize theo chuẩn task-execution (rõ ràng, ngắn gọn, ít mơ hồ).
Polish lại cho phù hợp model sáng tạo — KHÁC bước 04 ở chỗ: không tối giản tối đa, mà giữ lại
đủ "không gian" cho model tự diễn giải sáng tạo.

QUY TRÌNH:
1. Giữ nguyên phần constraint cứng (độ dài, format bắt buộc, thông tin không được sai)
2. Nới lỏng phần mô tả tông giọng/phong cách — dùng ví dụ và ẩn dụ thay vì liệt kê rule cứng
3. Thêm 1-2 câu "không gian tưởng tượng" — gợi mở hướng đi thay vì chỉ định chính xác
4. Loại bỏ ngôn ngữ máy móc kiểu "Bước 1... Bước 2..." nếu task là sáng tạo tự do

OUTPUT: prompt đã polish, kèm 1 dòng giải thích khác biệt so với bản optimize chuẩn.
```

## Ví dụ thực tế
Prompt gốc "Viết 3 đoạn giới thiệu ngắn, mỗi đoạn 50 từ" (task-execution rõ) → bản Fable thêm:
"Viết như đang kể chuyện cho một người bạn nghe lần đầu, được phép lạc đề nhẹ nếu ý hay" — giữ
constraint 50 từ nhưng mở không gian giọng văn.

## Đánh giá cá nhân
- Có nên dùng không: 6/10 — chỉ cần khi thật sự chạy trên model/task thiên sáng tạo, không cần
  cho hầu hết prompt kỹ thuật (dùng thẳng bước 04 `prompt-optimizer` là đủ).

## Link
- Thuộc chuỗi: `stacks/chuoi-9-buoc-viet-prompt.md` — bước 05/09
