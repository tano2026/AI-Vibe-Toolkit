---
name: humanizer
description: Rewrite AI-generated content to sound natural, human, with personality and emotion. Strip AI-isms.
category: content
---

# Humanizer — Skill

## TL;DR
Viết lại nội dung AI-generated thành văn bản nghe tự nhiên như người thật — có cá tính, có cảm xúc, không bị AI detector bắt.

## Khi nào dùng
- "Bài này nghe như AI quá, viết lại cho tự nhiên hơn"
- "Humanize bài này cho tao"
- Muốn bypass AI content detector (Originality.ai, GPTZero...)
- Muốn thêm giọng văn cá nhân vào nội dung AI tạo ra

## Nội dung skill / prompt
```
Bạn là chuyên gia viết content tự nhiên như con người. Nhiệm vụ: viết lại đoạn text sau để không còn nghe như AI.

NGUYÊN TẮC:
1. Vary độ dài câu mạnh tay — xen câu rất ngắn với câu dài hơn
2. Bắt đầu câu bằng "Và", "Nhưng", "À mà" khi tự nhiên
3. Xóa bỏ: "Furthermore", "Moreover", "In conclusion", "It is important to note", "Delve", "Comprehensive"
4. Thêm quan điểm cá nhân — "Tao nghĩ", "Theo kinh nghiệm", "Thật ra thì"
5. Dùng ví dụ cụ thể và unexpected thay vì generic
6. Đừng balance mọi thứ — có lập trường rõ ràng
7. [Tiếng Việt] Xen từ lóng tự nhiên: "kiểu như", "đại loại", "thôi thì"

OUTPUT:
- Phần 1: Bản đã humanize
- Phần 2: 3-5 bullet ghi chú những gì đã thay đổi và tại sao

Level mặc định: Medium (viết lại câu + thêm cá tính, giữ nguyên ý)

Text cần humanize:
[DÁN VÀO ĐÂY]
```

## Setup từng bước
1. Copy prompt trên
2. Paste vào system prompt của Claude/ChatGPT
3. Dán text cần humanize vào cuối
4. Nếu muốn giọng văn cụ thể hơn, thêm: "Viết theo tone [casual/professional/sarcastic]"

## Ví dụ thực tế

**Trước (AI-generated):**
> "It is important to note that artificial intelligence has become increasingly prevalent in modern society. Furthermore, this technology offers numerous benefits while also presenting significant challenges that must be carefully considered."

**Sau (Humanized):**
> "AI đang ở khắp nơi rồi. Không phải "ngày càng phổ biến" theo kiểu báo cáo — mà kiểu như mày mở điện thoại lên là đã dùng AI mà không biết. Tao thấy vừa thú vị vừa hơi lo. Không phải lo kiểu phim khoa học viễn tưởng — mà lo thiết thực hơn, kiểu như mình có còn biết tự suy nghĩ không."

## Lưu ý / Lỗi thường gặp
- Đừng humanize quá mức → mất thông tin quan trọng
- Với content SEO: balance giữa "tự nhiên" và "vẫn có keyword"
- Thuật ngữ chuyên ngành: giữ lại, chỉ humanize phần xung quanh

## Đánh giá cá nhân
- Điểm mạnh: Hiệu quả với cả tiếng Việt lẫn tiếng Anh, output nghe thật sự tự nhiên
- Điểm yếu: Cần review output — đôi khi thay đổi sắc thái ý nghĩa
- Có nên dùng không: **9/10** — Essential cho ai làm content bằng AI

## Link
- Nguồn gốc: Build bởi AI Vibe Toolkit
- File skill: /skills/humanizer.md

