# Supertonic — TTS Local $0, 31 Ngôn Ngữ, Không Cần GPU (5.3k⭐)

**Repo:** github.com/supertone-inc/supertonic | MIT (code) + OpenRAIL-M (model)
**Tác giả:** Supertone Inc., Seoul ($39.4M raised)
**Dùng cho:** Voiceover video, TTS local thay ElevenLabs

---

## Cài Nhanh

```bash
pip install supertonic

# Hoặc từ source
git clone https://github.com/supertone-inc/supertonic
cd supertonic
pip install -e .
```

## Generate Voiceover

```python
from supertonic import TTS

tts = TTS()

# Tiếng Việt
tts.generate(
    text="Xin chào! Đây là AI Vibe Toolkit.",
    language="vi",
    output="voice_vi.wav"
)

# Tiếng Anh
tts.generate(
    text="Today we're looking at the Hermes Agent.",
    language="en", 
    speaker="male_1",  # male_1, female_1, female_2...
    speed=1.0,         # 0.5 - 2.0
    output="voice_en.wav"
)

# Batch generate nhiều đoạn
texts = ["Hook: ...", "Problem: ...", "Solution: ..."]
for i, text in enumerate(texts):
    tts.generate(text=text, output=f"segment_{i}.wav")
```

## CLI

```bash
supertonic --text "Nội dung voiceover" --lang vi --out voice.wav
supertonic --file script.txt --lang vi --out voiceover.wav
supertonic --list-speakers  # xem giọng có sẵn
```

## Workflow Video AI Vibe Toolkit

```bash
# 1. Viết script (content-creator.md skill)
# 2. Generate voiceover
supertonic --file script-video-42.txt --lang vi --out voiceover.wav

# 3. Sync với video (FFmpeg)
ffmpeg -i screen_recording.mp4 -i voiceover.wav   -c:v copy -c:a aac -map 0:v:0 -map 1:a:0   final_video.mp4
```

## So Sánh ElevenLabs vs Supertonic

| | ElevenLabs | Supertonic |
|--|-----------|-----------|
| Chi phí | $5-22/tháng | $0 |
| Quality | 10/10 | 8/10 |
| Tiếng Việt | ✅ | ✅ |
| Local/Private | ❌ | ✅ |
| GPU cần | N/A | ❌ CPU ok |
| Speed | Fast | Medium |

**Rule:** Demo/test → Supertonic. Production quan trọng → ElevenLabs.

---
*skills/supertonic-skill.md | AI Vibe Toolkit | tháng 6/2026*
