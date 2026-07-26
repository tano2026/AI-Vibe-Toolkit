# Script Video 205 — PyCaps

## Thông tin
- Tool/Repo/Skill liên quan: /repos/pycaps.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~40 giây

## Hook (3 giây đầu)
Phụ đề động kiểu highlight từng từ như mấy kênh triệu view — 1 dòng lệnh Python.

## Script voiceover (ElevenLabs-ready)
PyCaps là thư viện Python, chuyên làm phụ đề động cho video, style bằng CSS thuần.

Cách dùng đơn giản nhất, chỉ một dòng lệnh, với video đầu vào và một template có sẵn, là ra ngay video có phụ đề động, hiệu ứng theo từng từ.

Nó tự động transcribe bằng Whisper chạy local, không cần gọi API ngoài. Nếu mày đã có sẵn transcript rồi, từ Whisper hay từ FunASR, cũng đưa thẳng vào được, khỏi transcribe lại từ đầu.

Muốn style theo đúng màu thương hiệu của mình, chỉ cần viết file CSS riêng, không phải học một ngôn ngữ định dạng nào khác.

Có một điều cần lưu ý, dự án này còn đang ở giai đoạn rất sớm, chưa lên kho PyPI chính thức, nên cứ chuẩn bị tinh thần đôi khi cập nhật sẽ đổi API.

Nhưng để lấp khoảng trống phụ đề động trong pipeline làm video ngắn, đây là lựa chọn đáng thử ngay lúc này.

Link cài đặt để trong mô tả.

## Ghi chú quay (OBS)
- Cảnh 1: Video gốc không phụ đề → chạy lệnh pycaps render → video có phụ đề động chạy theo từng từ
- Cảnh 2: Terminal chạy `pycaps render --input video.mp4 --template minimalist`
- Cảnh 3: Đoạn code Python ngắn dùng CapsPipelineBuilder với add_css custom
- Cảnh 4: Text overlay "Còn ALPHA — pin đúng version khi dùng thật"

## Caption/Sub note (CapCut)
Highlight: "1 dòng lệnh", "CSS thuần", "còn alpha" (đặt gần cuối). Vì đây là video về công cụ làm phụ đề, cân nhắc chính video này cũng dùng luôn hiệu ứng phụ đề động kiểu PyCaps để minh họa trực quan (meta nhưng hiệu quả).

## Thumbnail idea (Canva)
Màn hình điện thoại với phụ đề động highlight từng chữ nổi bật, chữ lớn "PYCAPS" + icon Python + CSS logo nhỏ góc dưới.

## CTA cuối video
Xài thử rồi khoe video có phụ đề đẹp cho tao coi nhé, follow để không bỏ lỡ tool tiếp theo.
