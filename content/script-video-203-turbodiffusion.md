# Script Video 203 — TurboDiffusion

## Thông tin
- Tool/Repo/Skill liên quan: /repos/turbodiffusion.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~45 giây

## Hook (3 giây đầu)
Video AI-gen mà chờ cả buổi cà phê mới ra? Cái này rút xuống vài giây.

## Script voiceover (ElevenLabs-ready)
Mấy model tạo video bằng AI, kiểu Wan2.1, thường chạy rất chậm, vì phải lặp qua rất nhiều bước để khử nhiễu từng khung hình.

TurboDiffusion, của nhóm nghiên cứu Tsinghua, giải quyết đúng vấn đề đó. Nó ghép ba kỹ thuật lại với nhau để nén quy trình xuống, kết quả là nhanh hơn gốc từ một trăm đến hai trăm lần, trên cùng một chiếc GPU.

Video năm giây mà trước đây phải chờ vài phút, giờ chỉ còn vài giây. Chất lượng gần như không đổi.

Nhưng có một điều kiện quan trọng. Nó đòi hỏi GPU đời cao, thử nghiệm chính là trên RTX năm không chín mươi. Không có GPU mạnh thì tool này không chạy được.

Nên đây là công cụ dành cho ai có sẵn máy có GPU rời, dùng để render nhanh các đoạn video ngắn, thay vì ngồi chờ.

Link cài đặt để trong mô tả.

## Ghi chú quay (OBS)
- Cảnh 1: Đồng hồ đếm ngược mô phỏng "chờ render" kiểu cũ (vài phút) — làm graphic overlay, không cần quay thật
- Cảnh 2: Terminal chạy lệnh generate, timer chạy chỉ vài giây — quay màn hình thật nếu có máy test
- Cảnh 3: So sánh side-by-side 2 video output (gốc vs TurboDiffusion) — nếu không có sẵn, dùng demo video từ repo GitHub
- Cảnh 4: Zoom vào dòng "Star 3.5k" trên GitHub repo

## Caption/Sub note (CapCut)
Highlight: "100-200 lần", "RTX 5090" (nhấn mạnh yêu cầu phần cứng ngay khi nhắc tới, tránh để người xem hiểu lầm chạy được máy yếu). Chữ to lúc nói số liệu tốc độ.

## Thumbnail idea (Canva)
Đồng hồ bấm giờ gạch chéo bên trái ghi "5 PHÚT", mũi tên chỉ sang phải ghi "5 GIÂY", nền tối, chữ "TURBODIFFUSION" nổi bật.

## CTA cuối video
Có máy GPU rời không? Thử xong quay lại kể tao nghe tốc độ thế nào.
