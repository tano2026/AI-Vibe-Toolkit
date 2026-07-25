# Script Video 194 — FunASR

## Thông tin
- Tool/Repo/Skill liên quan: /repos/funasr.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
Mày còn ngồi gõ tay transcript podcast à? 1 dòng lệnh là xong.

## Script voiceover (ElevenLabs-ready)
Whisper thì ai cũng biết rồi. Nhưng có 1 bộ công cụ nhận diện giọng nói còn xịn hơn, tên là FunASR, của Alibaba, mã nguồn mở, mười chín ngàn sao trên GitHub.

Khác Whisper chỉ có một model, FunASR là cả một bộ công cụ. Chọn đúng model theo việc cần làm. Cần nhanh nhất thì dùng Fun-ASR-Nano. Cần chạy trên CPU không có GPU thì dùng SenseVoice. Cần xử lý giọng nói theo thời gian thực thì dùng Paraformer.

Điểm hay nhất là chỉ cần gọi một lần, ra luôn đầy đủ. Có chữ, có ai đang nói, có thời gian từng câu, có dấu câu đàng hoàng. Whisper thì phải ghép thêm thư viện khác mới làm được mấy việc này.

Tao đã test với một đoạn ghi âm ba phút, tiếng Việt xen tiếng Anh. Phần tiếng Anh nhận gần như hoàn hảo. Phần tiếng Việt thì còn sai chính tả dấu ở một vài câu, đủ để làm bản nháp, chưa đủ để đăng thẳng.

Nên dùng nó đúng chỗ: tạo bản nháp transcript cho podcast, cho video, để đỡ phải ngồi gõ tay từ đầu. Sau đó vẫn cần người kiểm lại trước khi đăng.

Link và hướng dẫn cài đặt để trong mô tả.

## Ghi chú quay (OBS)
- Cảnh 1: Màn hình terminal, gõ lệnh cài đặt `pip install funasr` — quay lúc lệnh chạy xong, hiện dòng "Successfully installed"
- Cảnh 2: Chạy lệnh CLI `funasr audio.wav --spk --timestamps -f json` — quay màn hình JSON output hiện ra với timestamp + speaker rõ ràng
- Cảnh 3: Split-screen so sánh Whisper (chỉ ra text suông) vs FunASR (ra text + speaker + timestamp) — không cần quay thật, làm graphic overlay
- Cảnh 4: Quay lại 1 đoạn transcript thật của GMSP đã chạy qua FunASR, highlight chỗ tiếng Anh đúng và chỗ tiếng Việt cần sửa tay

## Caption/Sub note (CapCut)
Highlight từ khóa: "FunASR", "mười chín ngàn sao", "một lần gọi", "bản nháp" (nhấn mạnh đây KHÔNG phải publish thẳng được). Cắt cảnh ngay lúc chuyển từ ưu điểm sang giới hạn (đoạn "Phần tiếng Việt thì còn sai chính tả dấu") để giữ tính khách quan, không PR quá đà.

## Thumbnail idea (Canva)
Chữ lớn "WHISPER 2.0?" gạch chéo, bên dưới "FUNASR — 19K SAO". Nền chia đôi: 1 bên icon microphone + soundwave, 1 bên đoạn JSON code có highlight "speaker" + "timestamp".

## CTA cuối video
Follow để coi thêm tool AI hay, xài thử xong quay lại kể mày thấy sao nhé.
