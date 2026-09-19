# Script Video 316 — TypeSafe Jev

## Thông tin
- Tool/Repo/Skill liên quan: /repos/typesafe-jev.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
"Đừng dùng cả một con LLM to chỉ để trả lời có hay không."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề/pain point]
Trong vòng lặp của một agent, rất nhiều lúc chỉ cần quyết định nhỏ như chọn công cụ nào, chấm điểm mức độ khẩn cấp, hay kiểm tra đúng sai, nhưng lại phải gọi cả một LLM đầy đủ, tốn token cho một câu trả lời rất ngắn.

[Đoạn 2 — giới thiệu giải pháp]
TypeSafe vừa ra một loại model khác hẳn, gọi là System One Model, tên là Jev. Nó không sinh văn bản, mà nhận dữ liệu và một câu hỏi đã định kiểu sẵn, trả về đúng một lựa chọn, một điểm số, hoặc một xác suất đúng sai.

[Đoạn 3 — demo/cách làm]
Theo công bố của chính họ, nhanh hơn LLM thường gần hai trăm lần và rẻ hơn tới bốn trăm lần cho loại quyết định nhỏ này. Gọi được qua thư viện chính chủ, hoặc thử ngay không cần chờ danh sách chờ qua cổng AI Gateway của Vercel.

[Đoạn 4 — kết + CTA]
Đây là model rất mới, số liệu là do chính họ công bố, chưa có ai kiểm chứng độc lập, nên chỉ nên dùng cho quyết định phụ trợ, chưa nên giao việc quan trọng. Link thử nghiệm tao để trong kho, comment "jev" là gửi.

## Ghi chú quay (OBS)
- Cảnh 1: Icon LLM to bị dùng chỉ để trả lời "có/không" — lúc hook/pain point
- Cảnh 2: Sơ đồ state + câu hỏi có kiểu → Choice/Score/Boolean — lúc giới thiệu
- Cảnh 3: Code mẫu evaluate() trả về xác suất, không phải văn bản — lúc demo
- Cảnh 4: Chữ cảnh báo "số liệu tự công bố, chưa kiểm chứng" nổi bật màu cam — lúc kết

## Caption/Sub note (CapCut)
Highlight: "không sinh văn bản", "một lựa chọn, một điểm số, một xác suất", "chưa có ai kiểm chứng độc lập". Giữ đúng sắc thái khách quan, đừng thổi phồng số liệu của chính hãng.

## Thumbnail idea (Canva)
Cân thăng bằng, một bên là icon LLM nặng chậm, một bên là icon Jev nhẹ nhanh, text to: "MODEL MỚI: KHÔNG NÓI CHUYỆN, CHỈ RA QUYẾT ĐỊNH — NHANH HƠN GẦN 200 LẦN".

## CTA cuối video
Comment "jev" nhận link thử nghiệm qua Vercel AI Gateway không cần chờ waitlist, follow để xem thêm model mới đáng theo dõi.
