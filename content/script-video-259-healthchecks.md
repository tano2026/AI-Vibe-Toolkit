# Script Video 259 — Healthchecks

## Thông tin
- Tool/Repo/Skill liên quan: [/repos/healthchecks.md](../repos/healthchecks.md)
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~45 giây

## Hook (3 giây đầu)
Dashboard quản lý agent của tao chết cả tuần mà không ai biết.

## Script voiceover (ElevenLabs-ready)
Tao có 1 con dashboard theo dõi mấy con AI agent chạy trên VPS. Nó chết từ bao giờ tao cũng không rõ, chỉ tự phát hiện khi vô tình mở lên kiểm tra.

Vấn đề là không có ai báo khi có thứ gì đó ngừng chạy.

Cách fix cực đơn giản, gọi là Healthchecks. Nguyên lý ngược lại bình thường. Mỗi job sau khi chạy xong tự gọi 1 đường link báo cáo còn sống.

Nếu quá giờ mà không thấy báo cáo, hệ thống tự nhắn Telegram ngay lập tức.

Setup 5 phút, chạy Docker 1 dòng, gắn vào cuối mỗi cron job đang có.

Giờ agent nào chết là biết liền, không phải đợi tự phát hiện như trước nữa.

## Ghi chú quay (OBS)
- Cảnh 1: Dashboard Healthchecks UI hiện danh sách check, có cái màu đỏ báo "down"
- Cảnh 2: Điện thoại nhận tin Telegram cảnh báo real-time
- Cảnh 3: Terminal show dòng curl ping thêm vào cuối cron job

## Caption/Sub note (CapCut)
Highlight: "dead man's switch", "Healthchecks", "cron job" — nhấn mạnh lúc điện thoại nhận cảnh báo.

## Thumbnail idea (Canva)
Chữ to: "AGENT CHẾT LÀ BIẾT LIỀN" + icon chuông cảnh báo đỏ, nền dashboard.

## CTA cuối video
Save lại nếu VPS mày cũng đang chạy cron job mù không biết sống chết, link kho trong bio.
