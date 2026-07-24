# Script Video 188 — LightRAG

## Thông tin
- Tool/Repo/Skill liên quan: /repos/lightrag.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
Kho tri thức của mày càng lớn, AI càng trả lời tệ hơn. Đây là lý do tại sao.

## Script voiceover (ElevenLabs-ready)
Cách làm RAG thông thường là cắt tài liệu thành từng đoạn nhỏ, biến thành vector, rồi tìm đoạn giống câu hỏi nhất. Nhưng cách này mất hết mối quan hệ giữa các thông tin với nhau.

LightRAG làm khác. Nó vừa dựng một đồ thị tri thức, ghi rõ cái gì liên quan tới cái gì, vừa giữ song song vector embedding như bình thường. Khi mày hỏi một câu phức tạp kiểu, cái này liên quan gì tới cái kia qua một thứ ba, nó tra được qua đồ thị thay vì chỉ dò chữ giống nhau.

Điểm mạnh nhất là cập nhật tăng dần. Có tài liệu mới, nó không cần dựng lại toàn bộ chỉ mục từ đầu như các framework khác. Nó tự gộp phần đồ thị mới vào phần đang có.

Ba mươi tám nghìn sao trên GitHub, đã được công bố chính thức tại hội nghị EMNLP hai không hai lăm, gần như là chuẩn mực mới cho RAG có đồ thị.

## Ghi chú quay (OBS)
- Cảnh 1: Vẽ nhanh sơ đồ vector search vs graph search (trước/sau) trên bảng trắng hoặc Figma
- Cảnh 2: Quay terminal chạy lightrag-server
- Cảnh 3: Quay Web UI LightRAG hiển thị đồ thị tri thức

## Caption/Sub note (CapCut)
Highlight: "mất hết mối quan hệ", "đồ thị tri thức", "cập nhật tăng dần", "ba mươi tám nghìn sao". Zoom nhẹ vào số liệu sao.

## Thumbnail idea (Canva)
Nền xanh cyan-tím gradient (theo màu brand LightRAG), chữ lớn "RAG THẾ HỆ MỚI: KHÔNG CHỈ TÌM CHỮ GIỐNG NHAU", hình đồ thị node đơn giản.

## CTA cuối video
Follow để cập nhật thêm công cụ AI cho content factory và research pipeline.
