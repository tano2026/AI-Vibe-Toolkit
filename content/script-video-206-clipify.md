# Script Video 206 — Clipify

## Thông tin
- Tool/Repo/Skill liên quan: /repos/clipify.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~48 giây

## Hook (3 giây đầu)
1 video dài 1 tiếng, quẳng vào đây, ra liền 10 clip ngắn viral-ready.

## Script voiceover (ElevenLabs-ready)
Clipify là một toolkit Python, chuyên biến video dài thành nhiều clip ngắn, tự động hoàn toàn.

Đưa một video dài vào, kiểu podcast hay livestream, nó tự transcribe, tự phân tích ngữ nghĩa để chọn ra đoạn nào đáng xem nhất, không phải cắt máy móc theo thời gian.

Rồi tự convert luôn qua tỷ lệ dọc cho TikTok, Reels, Shorts, kèm caption, kèm cả gợi ý tiêu đề và hashtag.

Có bản chạy giao diện Gradio để test nhanh, có thư viện Python để tự động hoá, và có cả bản mở rộng, gọi là Clipify Hub, với REST API để scale cho nhiều video cùng lúc.

Điều cần lưu ý, phần chọn đoạn hay nhất phụ thuộc vào AI provider ngoài, kiểu Gemini hoặc OpenAI. Không có key thì nó chọn kiểu máy móc, chất lượng thấp hơn hẳn.

Đúng công cụ để tái sử dụng nội dung dài đã có sẵn, thành nhiều clip ngắn quảng bá.

Chi tiết trong mô tả.

## Ghi chú quay (OBS)
- Cảnh 1: Timeline video dài 1 tiếng → chia nhỏ thành 10 clip ngắn (graphic overlay minh họa)
- Cảnh 2: Giao diện Gradio, upload video, bấm "Generate clips"
- Cảnh 3: Kết quả ra — grid 5-10 clip ngắn dọc, mỗi clip có caption
- Cảnh 4: Text overlay "Cần API key Gemini/OpenAI để chọn đoạn hay nhất"

## Caption/Sub note (CapCut)
Highlight: "tự động hoàn toàn", "10 clip", "cần API key ngoài" (giữ khách quan, không PR quá đà). Cắt cảnh nhanh mỗi khi nhắc 1 tính năng mới (transcribe/chọn đoạn/convert/caption) để giữ nhịp.

## Thumbnail idea (Canva)
1 video dài (icon file lớn) ở giữa, mũi tên tỏa ra nhiều hướng thành nhiều clip nhỏ dọc xung quanh, chữ "CLIPIFY — 1 THÀNH 10".

## CTA cuối video
Có video dài nào đang bỏ xó không tận dụng? Thử Clipify rồi kể tao kết quả sao.
