# Kokoro-82M — GitHub Repo

## TL;DR
Model TTS chỉ 82 triệu parameters, nặng 300MB — chạy được trên laptop bình thường không cần GPU xịn. Chất lượng vượt xa các model lớn hơn gấp 10 lần kích thước.

## Repo này dùng để làm gì
Kokoro-82M (`hexgrad/kokoro`) là TTS model được thiết kế tối ưu cho hiệu năng trên phần cứng thấp. "82M" là số parameters (82 triệu) — cực kỳ nhỏ so với các model TTS thông thường (thường 300M-1B+).

Điểm nổi bật:
- **300MB** dung lượng — download/load nhanh
- Chạy được trên CPU thường, không bắt buộc GPU
- Chất lượng audio đáng kinh ngạc so với kích thước
- Hỗ trợ nhiều giọng (voices) built-in
- Latency thấp — phù hợp real-time application

Lý do 7,600+ sao: người dùng edge AI, IoT, server chi phí thấp cực cần model nhỏ chất lượng tốt.

## Setup từng bước
1. Cài qua pip:
```bash
pip install kokoro>=0.9.2
pip install soundfile  # để lưu audio
```
2. Basic usage:
```python
from kokoro import KPipeline
import soundfile as sf
import numpy as np

pipeline = KPipeline(lang_code='a')  # 'a' = American English
text = "Hello! This is Kokoro TTS running locally."

generator = pipeline(text, voice='af_heart', speed=1.0)
audio_chunks = []
for chunk in generator:
    audio_chunks.append(chunk.audio)

audio = np.concatenate(audio_chunks)
sf.write("output.wav", audio, 24000)
```
3. Xem danh sách voices:
```python
# Voices: af_heart, af_bella, af_sarah, am_adam, am_michael, 
#         bf_emma, bf_isabella, bm_george, bm_lewis, và nhiều hơn
```

## Ví dụ thực tế
**Bài toán:** Deploy TTS lên VPS nhỏ (2CPU, 2GB RAM) để generate voiceover tự động cho pipeline content — server không có GPU.

**Tại sao Kokoro-82M phù hợp:**
- Load xong trong 2-3 giây (model 300MB)
- Generate 30 giây audio trong ~5 giây trên CPU
- RAM usage ~500MB khi chạy
- So sánh: model TTS thông thường cần 4-8GB RAM, GPU để real-time

**Kết quả:** Pipeline voiceover tự động chạy 24/7 trên VPS $5/tháng.

## Lưu ý / Lỗi thường gặp
- **Tiếng Việt không hỗ trợ** → Kokoro train tiếng Anh và một số ngôn ngữ châu Âu. Dùng để làm content English.
- **Lỗi `espeak-ng not found`** → cài: `sudo apt-get install espeak-ng` (Linux)
- **Audio bị clipped** → giảm `speed` parameter xuống 0.9
- **Muốn nhiều voices hơn** → check Hugging Face: `hexgrad/Kokoro-82M` có full voice pack

## Đánh giá cá nhân
- **Điểm mạnh:** Cực kỳ nhẹ và nhanh. Chạy được không cần GPU. Chất lượng tốt nhất trong class "tiny TTS model". Phù hợp deploy production chi phí thấp.
- **Điểm yếu:** Chỉ tiếng Anh (và vài ngôn ngữ châu Âu). Không clone được giọng — chỉ dùng voices có sẵn.
- **Có nên dùng không: 8/10** — Best choice nếu cần deploy TTS lên server/edge device không có GPU. Không phải lựa chọn nếu cần clone giọng hay tiếng Việt.

## Link
- Repo: https://github.com/hexgrad/kokoro
- Model: https://huggingface.co/hexgrad/Kokoro-82M
- Stars: 7,600+
