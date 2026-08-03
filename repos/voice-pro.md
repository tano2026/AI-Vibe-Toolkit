# Voice-Pro (abus-aikorea) — GitHub Repo

## TL;DR
WebUI Gradio "tất cả trong 1" cho xử lý giọng nói — transcribe (Whisper), tách vocal (Demucs), dịch 100+ ngôn ngữ, TTS đa giọng, và **voice cloning zero-shot** (F5-TTS/E2-TTS/CosyVoice) — tự định vị là "robust alternative to ElevenLabs". 12K sao, đã mã nguồn mở hoàn toàn, miễn phí. **License GPL-3.0** — khác OpenVoice (MIT) đã có trong kho, cần đọc kỹ trước khi dùng thương mại.

## Repo này dùng để làm gì
Khác OpenVoice (chỉ làm 1 việc: clone giọng), Voice-Pro là **cả pipeline sản xuất giọng nói end-to-end** trong 1 giao diện web:
1. **Tải + tách vocal từ YouTube** (yt-dlp + Demucs) — lấy giọng gốc từ video tham khảo
2. **Transcribe** (Whisper/Faster-Whisper/WhisperX) — ra transcript có timestamp
3. **Dịch** 100+ ngôn ngữ (Deep-Translator, có tuỳ chọn Azure Translator riêng)
4. **TTS đa giọng** (Edge-TTS miễn phí, kokoro) hoặc **clone giọng zero-shot** (F5-TTS/E2-TTS/CosyVoice — chỉ cần mẫu ngắn, không cần train)
5. Ghép lại thành video/audio đã lồng tiếng ngôn ngữ khác

Đây chính là quy trình **dubbing đa ngôn ngữ tự động** — lấy 1 video, ra bản lồng tiếng ngôn ngữ khác giữ đúng giọng gốc.

## Setup từng bước
```bash
git clone https://github.com/abus-aikorea/voice-pro.git
cd voice-pro
# Theo README: tạo virtual env qua Miniconda (khuyến nghị, cô lập hoàn toàn khỏi hệ thống)
./configure.bat   # hoặc script tương ứng theo OS
./start.bat
```
Cần GPU để chạy nhanh (voice cloning + Whisper nặng) — có báo cáo chạy tốt trên RTX 3080. CPU
vẫn chạy được nhưng chậm hơn nhiều.

## Ví dụ thực tế
Video "Airfare Decoded" quay bằng tiếng Anh — dùng Voice-Pro để: tách vocal gốc, transcribe,
dịch sang tiếng Việt, rồi TTS lại bằng chính giọng người dẫn (voice cloning từ mẫu gốc) — ra
bản lồng tiếng Việt giữ nguyên "chất giọng" gốc thay vì đổi hẳn sang giọng đọc khác, hợp việc mở
rộng kênh sang khán giả Việt mà không cần quay lại từ đầu.

## Lưu ý / Lỗi thường gặp
- **GPL-3.0 — khác hẳn MIT của OpenVoice đã có trong kho.** GPL là copyleft mạnh: nếu sửa code
  rồi phân phối lại (kể cả chỉ chạy như 1 service người khác dùng qua mạng tuỳ theo cách hiểu
  AGPL vs GPL), có nghĩa vụ công bố source theo điều khoản GPL. Dùng nội bộ (không phân phối lại
  phần mềm) thì an toàn, nhưng cần hiểu rõ trước khi tích hợp vào sản phẩm thương mại đóng.
- Có bản fork `ai-anchorite/Voice-Pro` đóng gói sẵn cho Pinokio (Windows+Nvidia, cài 1 click) —
  tiện hơn nếu máy Windows local không muốn tự cấu hình môi trường Python/CUDA tay.
- Nặng tài nguyên hơn nhiều so với chỉ dùng OpenVoice hay ElevenLabs API thuần — đây là cả 1
  pipeline (Whisper + Demucs + TTS + voice cloning) chạy cùng lúc, không phải 1 model đơn lẻ.
- Chưa xác nhận riêng chất lượng tiếng Việt (giống lưu ý đã ghi với OpenVoice) — cần tự test.

## Đánh giá cá nhân
- Điểm mạnh: pipeline đầy đủ nhất trong nhóm voice tool đã có trong kho — không chỉ clone
  giọng mà cả transcribe+dịch+dubbing trong 1 chỗ; miễn phí hoàn toàn, cộng đồng lớn (12K sao).
- Điểm yếu: GPL-3.0 cần cẩn trọng hơn OpenVoice (MIT) khi tính đường thương mại hoá; nặng tài
  nguyên, cần GPU để dùng thực tế; setup phức tạp hơn gọi API thuần.
- Có nên dùng không: 8/10 cho nhu cầu dubbing đa ngôn ngữ nội bộ (không phân phối lại code) —
  đáng thử nghiệm cho hướng mở rộng kênh Airfare Decoded/GMSP sang khán giả ngôn ngữ khác.

## Link
- Repo gốc: https://github.com/abus-aikorea/voice-pro
- Bản đóng gói Pinokio (Windows+Nvidia): https://github.com/ai-anchorite/Voice-Pro
