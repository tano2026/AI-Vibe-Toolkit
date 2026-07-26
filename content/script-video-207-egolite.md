# Script Video 207 — Egolite (ego lite)

## Thông tin
- Tool/Repo/Skill liên quan: /repos/egolite.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~45 giây

## Hook (3 giây đầu)
Trình duyệt mà mày và AI agent dùng chung, không giành tab của nhau.

## Script voiceover (ElevenLabs-ready)
Ego lite là một trình duyệt Chromium, nhưng thiết kế khác hẳn mấy tool automation cũ.

Mấy framework kiểu Browser-Use, agent phải điều khiển một trình duyệt tách riêng, đăng nhập không mang theo được, mỗi lần chạy phải login lại từ đầu.

Ego lite thì khác. Nó là một trình duyệt thật, dùng hàng ngày, agent chạy song song trong một không gian riêng gọi là Space, không đụng tới tab của mày, mà vẫn kế thừa thẳng cookie, đăng nhập có sẵn.

Claude Code, Codex, Cursor, kết nối qua một lớp gọi là ego browser, gọi thẳng function javascript thay vì gọi từng lệnh CLI riêng lẻ, nên xử lý việc nhiều bước nhanh hơn hẳn, ít tốn token hơn.

Nhưng có một điều quan trọng phải nói ngay. Hiện tại chỉ chạy được trên macOS. Windows và Linux còn nằm trong lộ trình, chưa có ngày ra mắt.

Nên nếu máy mày không phải Mac, phải chờ thêm.

Chi tiết để trong mô tả.

## Ghi chú quay (OBS)
- Cảnh 1: Split-screen — bên trái người dùng browse bình thường, bên phải agent chạy task trong Space riêng cùng lúc
- Cảnh 2: Terminal Claude Code gõ lệnh /ego-browser với yêu cầu bằng ngôn ngữ tự nhiên
- Cảnh 3: Bảng so sánh (từ README) ego lite vs Browser-Use vs agent-browser — tốc độ 2.5x
- Cảnh 4: Text overlay to rõ "CHỈ macOS — Windows/Linux đang chờ"

## Caption/Sub note (CapCut)
Highlight: "dùng chung", "kế thừa login", "chỉ macOS" (bắt buộc hiện rõ, không giấu giới hạn này vì đây là lý do nhiều người xem sẽ chưa dùng được ngay).

## Thumbnail idea (Canva)
2 icon (người + robot) cùng ngồi 1 khung trình duyệt, chia đôi màn hình, chữ "EGO LITE" ở giữa, nhỏ góc dưới "macOS only".

## CTA cuối video
Ai xài Mac thử trước đi, kể tao nghe agent chạy mượt cỡ nào.
