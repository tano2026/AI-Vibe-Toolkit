---
name: video-pipeline-checklist
description: Quy trình 5 bước sản xuất video demo AI không cần lộ mặt từ Script -> ElevenLabs -> OBS -> CapCut -> Đăng bài.
---
# 🎬 Quy Trình Sản Xuất Video AI (Video Pipeline Checklist)

> Checklist chạy bằng cơm giúp biến mọi script trong thư mục `/content/` thành video ngắn (TikTok/Reels/Shorts) chất lượng cao trong 30 phút.

---

## 📋 Checklist 5 Bước Thực Thi

### Bước 1: Tạo Giọng Nói AI (ElevenLabs)
- [ ] Mở file script trong thư mục `content/` lấy lời thoại ở phần **[SCRIPT VOICE]**.
- [ ] Truy cập [ElevenLabs.io](https://elevenlabs.io/).
- [ ] Chọn voice profile của riêng bạn (ví dụ: giọng nam miền Nam hoặc miền Bắc trầm ấm).
- [ ] Dán lời thoại vào và nhấn **Generate**.
- [ ] Tải file audio `.mp3` về máy.

### Bước 2: Quay Demo Màn Hình (OBS Studio)
- [ ] Mở phần mềm cần demo hoặc mở terminal/browser chạy tool AI.
- [ ] Mở **OBS Studio**, chọn độ phân giải dọc **1080x1920** (hoặc quay ngang rồi crop sau).
- [ ] Bật chế độ quay màn hình (Display Capture) hoặc cửa sổ (Window Capture).
- [ ] Bật audio vừa tải từ ElevenLabs lên nghe và thực hiện thao tác trên màn hình khớp theo lời thoại (nhấn nút, gõ lệnh, chạy code).
- [ ] Quay dư khoảng 5-10 giây để dễ cắt ghép.

### Bước 3: Dựng Video & Auto Caption (CapCut)
- [ ] Mở **CapCut** (bản PC hoặc Mobile).
- [ ] Import file audio ElevenLabs và file video quay màn hình OBS.
- [ ] Cắt ghép các đoạn thừa, đẩy tốc độ video màn hình (speed up 1.5x - 2.5x) ở những đoạn gõ code hoặc load dữ liệu để khớp hoàn hảo với giọng đọc.
- [ ] Nhấn **Text** -> **Auto Captions** (Chọn ngôn ngữ tiếng Việt).
- [ ] Chỉnh sửa font chữ Caption:
  * Khuyên dùng font: **Montserrat Extra Bold** hoặc **Geist**.
  * Style: Chữ vàng viền đen, hoặc chữ trắng nền đen bo góc nhẹ để tăng tỉ lệ giữ chân người xem.
- [ ] Thêm nhạc nền nhẹ nhàng (Volume nhạc nền chỉnh nhỏ xuống khoảng -25dB để không đè giọng đọc).

### Bước 4: Thiết Kế Thumbnail (Canva)
- [ ] Mở **Canva**, chọn template **TikTok Cover** hoặc **YouTube Shorts Thumbnail**.
- [ ] Chụp 1 ảnh đẹp nhất trong video (ảnh kết quả chạy code hoặc giao diện dashboard).
- [ ] Thêm tiêu đề giật gân (Hook mạnh, cỡ chữ lớn, tối đa 5-7 từ).
- [ ] Sử dụng tông màu tương phản (Vàng - Đen hoặc Đỏ - Trắng).

### Bước 5: Đăng Bài & Tối Ưu SEO
- [ ] Lấy phần **[METADATA CAPTION & HASHTAGS]** từ file script.
- [ ] Đăng đồng thời lên 3 nền tảng: **TikTok**, **YouTube Shorts**, và **Facebook Reels**.
- [ ] Đặt tiêu đề thu hút và gán đúng bộ Hashtags xu hướng.
