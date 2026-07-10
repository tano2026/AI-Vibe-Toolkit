# Script Video 153 — DramaClaw

## Thông tin
- Tool/Repo liên quan: [repos/dramaclaw.md](../repos/dramaclaw.md)
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

---

## Hook (3 giây đầu)

"Không studio, không diễn viên, không hậu kỳ thủ công — tao vừa tìm ra cái này."

---

## Script voiceover (ElevenLabs-ready)

[Đoạn 1 — pain point]
Làm video promo travel mà thuê quay phim, diễn viên, editor — tốn cả chục triệu một clip. Còn nếu dùng AI thì phải chắp vá 5, 6 tool khác nhau: ChatGPT viết kịch bản, Midjourney vẽ ảnh, ElevenLabs lồng tiếng, CapCut ghép video. Vừa mất thời gian vừa không nhất quán.

[Đoạn 2 — giới thiệu]
DramaClaw là pipeline sản xuất phim AI mã nguồn mở, chạy được ngay trên laptop hoặc VPS nhỏ. Mày đưa vào một file kịch bản, nó tự làm hết: phân tích nhân vật, vẽ storyboard, lồng tiếng, ghép video, export ra file hoàn chỉnh.

[Đoạn 3 — cách setup]
Setup chỉ 3 lệnh Docker. Clone repo, copy file env, docker compose up. Mở localhost 8080 là xong. Không cần GPU, không cần database phức tạp, không cần cài thêm gì. Toàn bộ inference chạy qua gateway remote, VPS 4GB RAM là đủ.

[Đoạn 4 — kết + CTA]
924 stars trên GitHub, v1.0.5, vừa ra mắt tháng 3 năm ngoái. Tao đã thêm vào kho AI Vibe Toolkit với full hướng dẫn tích hợp agent. Link trong bio. Follow để xem tao build thử workflow ABTRIP travel video bằng cái này.

---

## Ghi chú quay (OBS)

- Cảnh 1 (0-5s): Màn hình DramaClaw web UI tại localhost:8080 — zoom vào trang chủ
- Cảnh 2 (5-18s): Terminal — chạy 3 lệnh Docker setup, real-time
- Cảnh 3 (18-32s): Screen record — upload manuscript → pipeline chạy tự động → thấy storyboard frame sinh ra
- Cảnh 4 (32-42s): Split screen — bên trái pipeline DramaClaw, bên phải video output mẫu từ repo
- Cảnh 5 (42-50s): GitHub repo page — highlight 924 stars, link trong bio

---

## Caption/Sub note (CapCut)

- "KHÔNG CẦN STUDIO" → chữ đỏ đậm, 0-3s
- "3 LỆNH DOCKER" → highlight xanh, timing khi demo terminal
- "924 STARS" → highlight vàng, cuối video
- "ABTRIP USE CASE" → sub nhỏ khi nói về travel video
- Nhịp cắt nhanh 3-4 giây để giữ attention, nhất là cảnh pipeline chạy

---

## Thumbnail idea (Canva)

- Nền tối + gradient tím/xanh (AI aesthetic)
- Text lớn: **"Xưởng phim AI chạy trên laptop"**
- Sub text nhỏ: "Không studio • Không diễn viên • Mã nguồn mở"
- Logo DramaClaw góc trên phải
- Góc dưới trái: badge "AI Vibe Toolkit #153"

---

## CTA cuối video

"Follow để xem tao build thử travel promo cho ABTRIP bằng DramaClaw — không quay một giây nào."
