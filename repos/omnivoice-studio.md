# OmniVoice Studio — GitHub Repo

## TL;DR
Ứng dụng desktop mã nguồn mở thay thế ElevenLabs chạy hoàn toàn offline: clone giọng, thiết kế giọng nói, lồng tiếng và đọc chính tả — không cần trả phí tháng, không cần internet.

## Repo này dùng để làm gì
OmniVoice Studio là ứng dụng desktop all-in-one cho TTS (text-to-speech) và voice cloning chạy 100% local trên máy. Mày có thể:
- Clone giọng bất kỳ ai từ một đoạn audio mẫu ngắn
- Thiết kế giọng nói từ đầu (age, accent, tone)
- Dubbing video: tự động thay giọng sang ngôn ngữ khác
- Dictation: đọc chính tả realtime
- Không cần API key, không cần kết nối internet khi dùng

So sánh thẳng với ElevenLabs: ElevenLabs tính phí theo ký tự/tháng, OmniVoice Studio dùng thoải mái không giới hạn sau khi cài xong.

## Setup từng bước
1. Clone repo:
```bash
git clone https://github.com/debpalash/OmniVoice-Studio
cd OmniVoice-Studio
```
2. Cài dependencies:
```bash
pip install -r requirements.txt
```
3. Download model weights (lần đầu tự động download khi chạy, cần khoảng 2-4GB dung lượng)
4. Chạy app:
```bash
python main.py
```
5. Giao diện desktop mở lên → chọn chế độ (Voice Clone / Design / Dubbing / Dictation) → dùng thôi

**Lưu ý:** Cần GPU để chạy nhanh. CPU cũng chạy được nhưng chậm hơn ~10x.

## Ví dụ thực tế
**Bài toán:** Mày muốn làm video YouTube Shorts không lộ mặt với giọng đọc chuyên nghiệp mà không trả phí ElevenLabs.

**Làm thế nào:**
1. Lấy 30-60 giây audio giọng mình đọc rõ ràng
2. Upload vào OmniVoice → chế độ Voice Clone
3. Nhập script → xuất file audio .wav/.mp3
4. Ghép vào OBS/CapCut như bình thường

Output: giọng clone tự nhiên, không còn nghe ra AI, chạy offline hoàn toàn.

## Lưu ý / Lỗi thường gặp
- **Lỗi CUDA out of memory** → giảm batch size trong settings hoặc dùng CPU mode
- **Audio output bị choppy** → tăng buffer size, giảm sample rate xuống 22050Hz
- **Clone giọng không giống** → cần audio mẫu chất lượng cao (không có tiếng ồn, ít nhất 30 giây), thu trong môi trường im
- **Windows Defender chặn** → whitelist thư mục app (false positive do file .exe tự tạo)

## Đánh giá cá nhân
- **Điểm mạnh:** Hoàn toàn miễn phí, offline, all-in-one, giao diện desktop thân thiện. 7,500+ sao GitHub — cộng đồng active.
- **Điểm yếu:** Cần máy có GPU decent để chạy mượt. Tiếng Việt chưa tốt bằng ElevenLabs. Setup ban đầu hơi phức tạp với người mới.
- **Có nên dùng không: 8/10** — Nếu mày dùng ElevenLabs chỉ để làm video content, chuyển sang cái này tiết kiệm được vài triệu/năm. Chấp nhận được đánh đổi một chút về chất lượng.

## Link
- Repo: https://github.com/debpalash/OmniVoice-Studio
- Stars: 7,500+
