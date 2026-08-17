# Script Video 258 — Qdrant

## Thông tin
- Tool/Repo/Skill liên quan: [/repos/qdrant.md](../repos/qdrant.md)
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
Con bot AI của tao trả lời ngu vì nó không hiểu ý, chỉ biết match đúng từng chữ.

## Script voiceover (ElevenLabs-ready)
Con RIO Bot của tao chạy 24 tiếng nhưng có 1 vấn đề. Nó chỉ nhớ theo kiểu tìm đúng chữ, không hiểu ngữ nghĩa. Khách hỏi khác đi 1 chút là nó coi như chưa từng gặp câu đó bao giờ.

Cách fix là thêm 1 lớp gọi là vector database. Nó biến câu chữ thành dãy số thể hiện ý nghĩa, rồi so sánh độ giống nhau giữa các câu.

Tool tao dùng là Qdrant. Mã nguồn mở, tự host trên VPS, chạy bằng 1 dòng lệnh Docker.

Giờ RIO Bot hỏi câu gì na ná câu cũ, nó tự tìm ra ngữ cảnh liên quan, trả lời chính xác hơn hẳn.

Nếu con bot của mày cũng đang chỉ biết trả lời máy móc, thử thêm Qdrant vào xem.

## Ghi chú quay (OBS)
- Cảnh 1: Terminal chạy lệnh docker run qdrant, log container start
- Cảnh 2: Trước/sau — RIO Bot trả lời sai (chỉ match keyword) vs trả lời đúng (semantic search)
- Cảnh 3: Dashboard Qdrant UI hiện collection rio-memory với số điểm dữ liệu

## Caption/Sub note (CapCut)
Highlight: "vector database", "semantic search", "Qdrant" — cắt cảnh đúng lúc đọc tên tool.

## Thumbnail idea (Canva)
Chữ to: "BOT AI HẾT NGU CHỮ" + icon não/vector, nền tối kiểu terminal.

## CTA cuối video
Follow để xem full setup Qdrant cho RIO Bot, link kho trong bio.
