# Supertonic — TTS local siêu nhanh, 31 ngôn ngữ, không cần GPU, không cần API

**GitHub:** https://github.com/supertone-inc/supertonic
**Stars:** 5.3k | **Forks:** 528 | **License:** MIT (code) + OpenRAIL-M (model)
**Tác giả:** Supertone Inc. (Seoul, $39.4M raised)
**Version:** Supertonic 3 (tháng 4/2026)
**Language:** Swift, Python, JS, Java, C++, Go, Rust, Flutter...

---

## Vấn đề nó giải quyết

Mày cần TTS (text-to-speech) để làm voiceover video, đọc app, hoặc tích hợp vào sản phẩm.

**Lựa chọn thông thường:**
- ElevenLabs, Google TTS, OpenAI TTS → tốn tiền, gửi data lên cloud, latency
- TTS model lớn local (VoxtLM, Chatterbox...) → cần GPU, nặng 500MB-2GB

**Supertonic:** 99M parameters, chạy trên CPU thường, không cần cloud, không cần GPU. Trên M4 Pro đạt **1,263 ký tự/giây** — nhanh hơn real-time 167 lần.

---

## Supertonic 3 — Điểm Nổi Bật

**31 ngôn ngữ** từ 1 model duy nhất — không cần fine-tune riêng từng ngôn ngữ:

| EN | KO | JA | VI | AR | DE | FR | ES | HI | RU |
|----|----|----|----|----|----|----|----|----|-----|
| + 21 ngôn ngữ khác | | | | | | | | | |

**Vietnamese có trong danh sách** — code `vi`.

**Lang fallback:** Không biết ngôn ngữ là gì? Pass `lang="na"`, model tự xử lý.

**So sánh với model lớn hơn:**

| Model | Params | Hardware | Speed (M4 CPU) |
|-------|--------|----------|----------------|
| **Supertonic 3** | **99M** | **CPU** | **1,263 chars/s** |
| Chatterbox Multilingual | 500M | GPU | Slower |
| OmniVoice | 800M | GPU | Slower |

Nhỏ hơn 5-8x, chạy CPU, nhanh hơn — đây là điểm bán hàng chính.

---

## Cài & Dùng

**Python (nhanh nhất):**
```bash
pip install supertonic
```

```python
from supertonic import TTS

tts = TTS()  # tự download model lần đầu

# TTS cơ bản
wav, sample_rate = tts.synthesize(
    "Xin chào, đây là Supertonic chạy local.",
    lang="vi"
)

# Lưu file
import soundfile as sf
sf.write("output.wav", wav, sample_rate)
```

**Local HTTP server (OpenAI-compatible API):**
```bash
supertonic serve
# Tự động expose:
# POST /v1/tts          — native endpoint
# POST /v1/audio/speech — OpenAI-compatible
```

Bất kỳ tool nào support OpenAI TTS API đều dùng được ngay với endpoint local này.

**Voice cloning:**
```python
wav, _ = tts.synthesize(
    "Text muốn đọc",
    voice_style=style,  # JSON từ Voice Builder
    lang="vi"
)
```

---

## Voice Builder

Supertone cung cấp tool web để **clone giọng của mày**:
1. Upload 10-30 giây audio giọng mày
2. Voice Builder tạo voice profile JSON
3. Download JSON → dùng local với Supertonic

**Kết quả:** AI đọc text bằng giọng của mày, chạy hoàn toàn local.

---

## Các Platform Hỗ Trợ

```
Python    → pip install supertonic
Node.js   → npm install supertonic
Browser   → WebGPU / WASM (chạy trong browser)
iOS       → Swift native
Android   → Java / Kotlin
Desktop   → C++, C#, Go, Rust
Mobile    → Flutter
Edge      → Raspberry Pi, e-reader (Onyx Boox)
```

---

## Tích Hợp Với Vibe Coding Pipeline

**Dùng cho video content (pipeline của mày):**
```
Script text → Supertonic (local TTS) → .wav file
→ OBS (ghép với screen record)
→ CapCut (edit)
```

Thay ElevenLabs bằng Supertonic cho voiceover script video — $0/tháng thay vì $22+.

**Lưu ý tiếng Việt:** Supertonic 3 support `vi` nhưng quality tiếng Việt chưa được test kỹ trên benchmark chính thức. Nên test thử trước khi dùng production.

---

## Đánh Giá Cá Nhân

Supertonic 3 là TTS local đáng dùng nhất hiện tại nếu mày cần chạy on-device, không muốn pay cloud API.

Con số ấn tượng nhất: **99M params chạy CPU nhanh hơn 500M params chạy GPU**. Đây là kết quả của architecture tốt (flow-matching + ONNX optimization), không phải chỉ shrink model nhỏ đi.

Điểm tao thích nhất là OpenAI-compatible local server — mày có thể swap ElevenLabs bằng Supertonic mà không cần đổi code, chỉ đổi endpoint từ cloud sang `localhost`.

Điểm trừ: tiếng Việt chưa có benchmark chính thức, chất lượng có thể không bằng tiếng Anh/Hàn. Với content creator người Việt cần test kỹ.

**Với pipeline video của vibe coders:** Đây là thứ đáng cài thử để replace ElevenLabs cho bước voiceover — nếu quality đủ tốt thì tiết kiệm được $22+/tháng.

**Rating: 8/10** — trừ điểm vì chưa có benchmark tiếng Việt rõ ràng.

---

*Nguồn: github.com/supertone-inc/supertonic*
*Cập nhật: tháng 6/2026*
