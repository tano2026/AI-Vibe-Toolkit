# OpenVoice (myshell-ai) — GitHub Repo

## TL;DR
Voice cloning miễn phí, mã nguồn mở, MIT license — chỉ cần 1 đoạn audio ngắn để clone giọng, sinh giọng nói đa ngôn ngữ. 36.6K stars, đã chạy hàng chục triệu lượt trên myshell.ai. Có thể thay thế ElevenLabs cho 1 số use case để tiết kiệm chi phí, nhưng cần kiểm tra kỹ hỗ trợ tiếng Việt trước khi thay hẳn.

## Repo này dùng để làm gì
Cho 1 đoạn audio giọng mẫu (chỉ cần ngắn), OpenVoice clone lại tông giọng (tone color) và cho phép chỉnh: cảm xúc, ngữ điệu, nhịp điệu, khoảng ngắt, accent — đồng thời làm được **zero-shot cross-lingual** (clone giọng 1 người rồi cho nói ngôn ngữ khác họ chưa từng nói trong data huấn luyện).

## Setup từng bước
1. Cài môi trường:
```bash
conda create -n openvoice python=3.9
conda activate openvoice
git clone https://github.com/myshell-ai/OpenVoice.git
cd OpenVoice
pip install -e .
```
2. Tải checkpoint từ link chính thức trong docs, giải nén vào thư mục `checkpoints`.
3. Có cả V1 và V2 — cài đặt giống nhau, dùng bản V2 (mới hơn, chất lượng tốt hơn).
4. Muốn thử nhanh không cần cài local: có sẵn demo online (link trong docs), phù hợp để test trước khi quyết định tự host.

## Ví dụ thực tế
Cân nhắc cho content daily/batch (Trùm Sân Bay, video ngắn Wonder Mart) — thay vì trả phí ElevenLabs cho mọi voiceover, dùng OpenVoice tự host cho content khối lượng lớn/không cần chất lượng cao nhất, giữ ElevenLabs cho content chỉn chu (GMSP, Airfare Decoded) nơi chất lượng giọng đọc quan trọng hơn.

## Lưu ý / Lỗi thường gặp
- **Chưa xác nhận hỗ trợ tiếng Việt** — docs liệt kê rõ tiếng Anh, Tây Ban Nha, Pháp, Trung, Nhật, Hàn cho phần TTS gốc (MeloTTS đi kèm); phần zero-shot cross-lingual có thể mở rộng hơn nhưng CẦN TỰ TEST chất lượng tiếng Việt trước khi dùng sản xuất thật, không giả định hoạt động tốt.
- Cần GPU để chạy tốc độ hợp lý — CPU vẫn chạy được nhưng chậm hơn nhiều, không hợp cho batch lớn.
- MIT License từ tháng 4/2024 — dùng thương mại tự do, không cần xin phép, khác nhiều model AI khác trong danh sách hôm nay cần đọc kỹ license.
- Chất lượng clone phụ thuộc nhiều vào chất lượng audio mẫu đầu vào — audio mẫu nhiễu/ngắn quá sẽ ra kết quả kém.

## Đánh giá cá nhân
- Điểm mạnh: miễn phí hoàn toàn, MIT license rõ ràng, đã được kiểm chứng ở quy mô lớn (hàng chục triệu lượt dùng qua myshell.ai); công thức tính "tốn tiền tệ hơn API thương mại hàng chục lần" (theo research paper) hấp dẫn cho content khối lượng lớn.
- Điểm yếu: chưa xác nhận chất lượng tiếng Việt — đây là rủi ro lớn nhất trước khi dùng thay ElevenLabs; cần GPU để hiệu quả; setup phức tạp hơn hẳn so với gọi API ElevenLabs (chỉ cần request HTTP).
- Có nên dùng không: 6.5/10 cho tới khi test tiếng Việt xong — tiềm năng tiết kiệm chi phí lớn cho content khối lượng cao, nhưng KHÔNG nên thay ElevenLabs ngay mà chưa verify chất lượng giọng Việt thật.

## Link
- Repo: https://github.com/myshell-ai/OpenVoice
- Docs: https://research.myshell.ai/open-voice
