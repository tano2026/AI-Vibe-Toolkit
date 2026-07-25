---
name: write-a-skill
description: >
  - "Đóng gói cái prompt này thành skill dùng lại được" - "Biến quy trình này thành SKILL.md"
---

# Write a Skill — Skill

## TL;DR
Bước 08 trong chuỗi 9 skill — biến 1 prompt/quy trình đã chứng minh dùng tốt thành file
`SKILL.md` đóng gói chuẩn, dùng lại được nhiều lần thay vì gõ lại từ đầu mỗi lần.

## Khi nào dùng
- 1 prompt đã dùng thành công ≥2-3 lần cho cùng loại task
- Muốn Hermes/OpenClaw/agent khác dùng lại được quy trình này mà không cần hỏi lại CEO

## Nội dung skill / prompt
```
Nhận 1 prompt/quy trình đã verify hoạt động tốt. Đóng gói thành SKILL.md chuẩn:

CẤU TRÚC BẮT BUỘC:
1. Frontmatter YAML: name (snake-case), description (liệt kê 2-4 câu trigger phổ biến,
   dạng "- \"câu nói X\" - \"câu nói Y\"")
2. TL;DR: 1-2 câu skill làm gì
3. Khi nào dùng: liệt kê tình huống trigger cụ thể
4. Nội dung skill/prompt: đúng nội dung prompt gốc, đặt trong code block, copy-paste được
5. Ví dụ thực tế: input cụ thể → output cụ thể (không mô tả chung chung)
6. Đánh giá cá nhân: có nên dùng không, X/10, vì sao

QUY TẮC ĐẶT TÊN: tên skill mô tả HÀNH ĐỘNG (vd "phan-tich-unit-economics"), không mô tả công cụ
("dung-excel-de-tinh-toan") — skill là về việc làm gì, không phải công cụ nào.

Kiểm tra trùng tên trước khi tạo file mới (search kho `skills/` theo slug variant).
```

## Ví dụ thực tế
Đã dùng 1 prompt tay để "soạn JD tuyển nhân viên ca trực" 3 lần cho Fast Track → đóng gói thành
skill mới trong `agents/company/roles/hr-admin.md` thay vì gõ lại prompt mỗi lần cần tuyển.

## Đánh giá cá nhân
- Có nên dùng không: 9/10 — đây chính là engine của toàn bộ kho AI-Vibe-Toolkit, biến kinh
  nghiệm rời rạc thành tài sản tái sử dụng.

## Link
- Thuộc chuỗi: `stacks/chuoi-9-buoc-viet-prompt.md` — bước 08/09
