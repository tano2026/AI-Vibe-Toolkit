# Script Video 204 — InfiniteTalk

## Thông tin
- Tool/Repo/Skill liên quan: /repos/infinitetalk.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~48 giây

## Hook (3 giây đầu)
1 tấm ảnh, 1 file âm thanh, ra 1 video người đang nói. Không giới hạn độ dài.

## Script voiceover (ElevenLabs-ready)
InfiniteTalk là model của MeiGen-AI, cho phép biến một tấm ảnh, cộng với một file âm thanh, thành video người trong ảnh đang nói đúng theo giọng đó.

Điểm khác biệt so với mấy tool lip-sync cũ, nó không chỉ khớp môi. Đầu, thân người, biểu cảm khuôn mặt cũng chuyển động theo giọng nói luôn.

Và tên nó không phải để câu view đâu. Infinite Talk nghĩa là không giới hạn độ dài video thật. Nhờ cơ chế xử lý theo từng đoạn nối tiếp, mà vẫn giữ đúng nhận diện nhân vật xuyên suốt.

Repo mã nguồn mở, giấy phép Apache hai chấm không, dùng thoải mái kể cả cho mục đích thương mại.

Tất nhiên, cũng cần GPU đủ mạnh để chạy, vì model gốc là Wan hai chấm một, mười bốn tỷ tham số.

Đây là hướng để làm host ảo nói phần mở đầu video, mà không cần quay mặt thật.

Chi tiết cài đặt để trong mô tả.

## Ghi chú quay (OBS)
- Cảnh 1: 1 tấm ảnh chân dung tĩnh → transition sang video "đang nói" (dùng demo có sẵn từ repo nếu chưa test được)
- Cảnh 2: Split-screen so sánh lip-sync cũ (chỉ môi động) vs InfiniteTalk (đầu+thân+biểu cảm cùng động) — làm graphic overlay minh họa
- Cảnh 3: Terminal chạy lệnh generate_infinitetalk.py
- Cảnh 4: Text overlay "Apache 2.0 — dùng thương mại OK"

## Caption/Sub note (CapCut)
Highlight: "không giới hạn độ dài", "Apache 2.0", "cần GPU mạnh" (đặt ngay gần cuối để không PR quá đà, giữ tính khách quan).

## Thumbnail idea (Canva)
1 khuôn mặt AI-gen (không dùng người thật/celeb) với soundwave phát ra từ miệng, chữ "InfiniteTalk" bên dưới, tag nhỏ góc "Ảnh + Âm thanh = Video".

## CTA cuối video
Follow nếu mày cũng đang tìm cách làm host ảo cho kênh, tao còn nhiều tool kiểu này nữa.
