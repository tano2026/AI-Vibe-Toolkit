# Content Analysis — Phân tích sâu thay vì chỉ tóm tắt

## TL;DR
Khung phân tích bài viết/video/podcast theo 6 "lens" khác nhau (argument, editorial, research, practical, comparative, media) để trả lời "nội dung này nói gì, chứng minh bằng gì, và có đáng tin không" — thay vì chỉ tóm tắt lại nội dung.

## Skill này dùng để làm gì
Khác summarization ở chỗ: đây là phân tích, không phải tóm tắt. 6 lens để chọn theo nhu cầu:
- **Argument**: claim → lý do → bằng chứng → kết luận, có đứng vững không
- **Editorial**: cấu trúc, nhịp độ, framing, có hợp với audience không
- **Research**: phương pháp, chất lượng bằng chứng, giới hạn, giải thích thay thế
- **Practical**: quyết định/thói quen/quy trình có áp dụng được không
- **Comparative**: đồng thuận/mâu thuẫn/khác biệt giả định giữa nhiều nguồn
- **Media**: vai trò người nói, thứ tự, độ tin cậy transcript

Quy trình: xác định nguồn → check độ đầy đủ (transcript có thiếu đoạn nào không) → map nội dung thành claim/theme → đánh giá bằng chứng có thật sự support kết luận không → rút insight mạnh nhất → verify lại trích dẫn.

## Setup từng bước
1. Chọn lens phù hợp với mục đích (đừng dùng cả 6 lens cùng lúc — chỉ chọn cái phục vụ câu hỏi thật)
2. Với video/podcast — xác nhận transcript đã đầy đủ trước khi phân tích, note rõ đoạn nào thiếu
3. Tách rõ "source nói gì" và "mình suy luận thêm gì" trong output — không lẫn lộn 2 cái

## Ví dụ thực tế
**Case:** Phân tích 1 video đối thủ trong mảng Fast Track/dịch vụ sân bay để tìm insight cho ABTRIP, dùng lens **Comparative + Practical**:
- Comparative: đối thủ nhấn mạnh "giá rẻ nhất", ABTRIP hiện định vị "physical presence tại Nội Bài" — 2 hướng khác nhau, không mâu thuẫn trực tiếp
- Practical: đối thủ dùng CTA "đặt ngay trong app", ABTRIP hiện broadcast qua Zalo OA thủ công — có thể học cách rút ngắn friction đặt chỗ

## Lưu ý / Lỗi thường gặp
- Dễ lạm dụng phân tích quá sâu cho content đơn giản — chỉ nên dùng khi thực sự cần insight/critique, không phải cho mọi video research thông thường
- "Media lens" đòi hỏi transcript chất lượng tốt — với video tự quay có tiếng ồn/giọng khó nghe, độ tin cậy phân tích giảm mạnh

## Đánh giá cá nhân
- Điểm mạnh: phân biệt rõ ràng giữa "tóm tắt" và "phân tích", 6 lens giúp không bị lan man khi phân tích nội dung phức tạp
- Điểm yếu: overlap khá nhiều với content-research-writer và summarization ở phần quy trình verify nguồn — dùng cả 3 skill cùng lúc hơi dư thừa
- Có nên dùng không: 5/10 — hữu ích khi cần phân tích đối thủ/nội dung sâu, không cần cho việc nghiên cứu tool thông thường của kho

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Prompt-only — dùng khi Hermes research đối thủ (VD: phân tích video/content
# đối thủ ABTRIP trên TikTok) rồi cần insight có cấu trúc, không chỉ liệt kê fact
```

### OpenClaw
> Có thể dùng cho research-agent khi task là "phân tích đối thủ" thay vì "tóm tắt tin tức".

### Antigravity
> Không cần deploy.
