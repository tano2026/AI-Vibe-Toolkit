# Clipify — GitHub Repo

## TL;DR
Toolkit Python biến 1 video dài thành nhiều clip ngắn viral-ready — tự transcribe, tự chọn đoạn hay (thematic segmentation), tự convert tỷ lệ (9:16/4:5/1:1), tự gắn caption. Có cả CLI, thư viện Python, UI desktop, lẫn REST API để tự host.

## Repo này dùng để làm gì
Đưa 1 video dài (podcast, talk, livestream) vào → Clipify tự cắt ra nhiều clip ngắn "đáng xem nhất", kèm luôn: transcript, phân đoạn theo chủ đề (AI phân tích ngữ nghĩa, không cắt máy móc theo thời gian), title gợi ý, hashtag, phân tích sentiment để ưu tiên đoạn nào "viral" hơn. Ra thẳng định dạng dọc cho TikTok/Reels/Shorts.

## Setup từng bước
1. Cài đặt:
```bash
pip install clipify
# hoặc từ source để chỉnh sửa
git clone https://github.com/adelelawady/Clipify.git
cd Clipify
pip install -r requirements.txt
```
2. Set API key cho AI provider (mặc định Gemini, có thể đổi OpenAI):
```bash
export AI_PROVIDER=gemini
export GEMINI_API_KEY=your_key
```
3. Chạy nhanh qua Gradio UI (test thử, không cần code):
```bash
python app.py
# mở http://127.0.0.1:7860, upload video, bấm "Generate clips"
```
4. Dùng CLI/thư viện cho batch xử lý (khi cần tự động hoá):
```python
from clipify import Clipify

clipper = Clipify(ai_provider="gemini")
clips = clipper.process("long_video.mp4", formats=["9:16", "1:1"])
```
5. Muốn scale (nhiều video, nhiều tenant): dùng bản đầy đủ `Clipify-Hub` — có REST API, webhook, containerized deployment sẵn.

## Ví dụ thực tế
Áp cho podcast GMSP (Giải Mã Số Phận) đã ghi âm/quay full tập — thay vì tự ngồi nghe lại chọn đoạn hay để cắt Shorts quảng bá tập mới, đưa file video gốc qua Clipify, để nó tự chấm đoạn nào "đáng xem nhất" theo sentiment + thematic segmentation, ra sẵn 5-10 clip dọc kèm caption — Nobitano chỉ cần duyệt lại chọn clip đăng, không phải tự cắt từ đầu.

## Lưu ý / Lỗi thường gặp
- Có **nhiều repo cùng tên "Clipify"** trên GitHub (ít nhất 4-5 fork/bản độc lập khác nhau) — bản dùng ở đây là `adelelawady/Clipify` (bản gốc, có release v2.1.4, đầy đủ tính năng nhất, có cả bản Hub mở rộng). Kiểm tra kỹ đúng repo trước khi clone, tránh nhầm bản fork thiếu tính năng.
- Phụ thuộc AI provider ngoài (Gemini/OpenAI) cho bước chọn đoạn hay — không có key thì fallback về "simple deterministic highlight-picker" (chọn máy móc, chất lượng thấp hơn nhiều).
- SpeechRecognition dùng để transcribe — chất lượng cho tiếng Việt chưa được xác nhận tốt, cần tự test, có thể cân nhắc thay bằng FunASR/Whisper cho bước transcribe rồi feed transcript vào Clipify thay vì để nó tự transcribe.
- README ghi rõ "detailed contributing guidelines sẽ có sau" — dự án vẫn đang hoàn thiện, không kỳ vọng docs đầy đủ 100%.

## Đánh giá cá nhân
- Điểm mạnh: pipeline đầy đủ nhất trong nhóm "long-to-short" tool đã research (transcribe + chọn đoạn AI + convert tỷ lệ + caption + hashtag trong 1 lần chạy), có cả bản Hub để scale thật.
- Điểm yếu: phụ thuộc AI provider trả phí để có chất lượng tốt, chưa xác nhận chất lượng transcribe tiếng Việt, nhiều bản trùng tên dễ nhầm.
- Có nên dùng: 7/10 — rất đáng thử cho việc tái sử dụng nội dung GMSP/Trùm Sân Bay đã có sẵn, nhưng nên tự feed transcript từ FunASR vào thay vì để Clipify tự transcribe, để kiểm soát chất lượng tiếng Việt tốt hơn.

## Link
- Repo chính: https://github.com/adelelawady/Clipify
- Bản mở rộng (Hub, REST API, webhook): https://github.com/adelelawady/Clipify-hub
- Demo: https://adelelawady.github.io/Clipify-Hub/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
from clipify import Clipify
import os

os.environ["GEMINI_API_KEY"] = "..."  # lấy từ env thật, không hardcode

def make_clips(video_path, formats=("9:16",)):
    clipper = Clipify(ai_provider="gemini")
    return clipper.process(video_path, formats=list(formats))
```

### OpenClaw
```bash
pip install clipify
# hoặc deploy bản Hub để có REST API gọi qua HTTP thay vì import Python trực tiếp
git clone https://github.com/adelelawady/Clipify-hub /opt/clipify-hub
```

### Antigravity
```bash
pip install clipify --break-system-packages
pm2 start "python app.py" --name clipify-gradio   # nếu muốn giữ UI Gradio chạy 24/7
```
> ⚠️ Cân nhắc thay bước transcribe nội bộ của Clipify bằng transcript từ FunASR (đã có trong kho) nếu độ chính xác tiếng Việt của SpeechRecognition không đạt.
