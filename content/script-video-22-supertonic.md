# Script Video #22 — Supertonic: TTS Local Nhanh Hơn ElevenLabs, $0/Tháng

**Format:** TikTok / YouTube Shorts (~80s)
**Hook type:** Cost savings — "Mày đang trả tiền thừa"
**Style:** Không lộ mặt, audio demo + terminal

---

## 🎬 SCRIPT

**[0s - 7s] HOOK**
> "ElevenLabs $22/tháng cho voiceover video. Cái này chạy trên laptop mày, nhanh hơn real-time 167 lần, và tốn $0/tháng."

*[Show: ElevenLabs pricing → Supertonic GitHub]*

**[7s - 20s] SPECS ĐÁNG NGỠ**
> "Supertonic 3 của Supertone — company Hàn Quốc raise được 39 triệu đô. Họ vừa open source engine TTS của mình."

> "99 triệu parameters. Chạy CPU. Không cần GPU. Trên M4 Pro đạt 1,263 ký tự mỗi giây — tức là đọc 1 trang A4 trong chưa đầy 2 giây."

*[Show: benchmark numbers trên màn hình]*

**[20s - 45s] DEMO**
> "Cài:"
```bash
pip install supertonic
```

```python
from supertonic import TTS
tts = TTS()
wav, sr = tts.synthesize(
    "Xin chào, đây là Supertonic chạy local trên máy tao.",
    lang="vi"  # Tiếng Việt có support
)
```

*[Play audio output — người xem nghe kết quả]*

> "31 ngôn ngữ từ 1 model duy nhất. Tiếng Việt code 'vi' có trong danh sách."

**[45s - 62s] WORKFLOW THỰC TẾ**
> "Với pipeline làm video của tao: Script text → Supertonic → file WAV → OBS ghép screen record → CapCut. Thay ElevenLabs hoàn toàn."

> "Thêm nữa: nó có local API tương thích OpenAI — bất kỳ app nào dùng OpenAI TTS đều swap được sang local không cần đổi code."

```bash
supertonic serve
# localhost:8080/v1/audio/speech
```

**[62s - 80s] LƯU Ý + CTA**
> "Một lưu ý thật thà: tiếng Việt chưa có benchmark chính thức — chất lượng tốt nhưng mày nên test thử trước khi dùng production."

> "5.3k stars, MIT license. Link trong bio."

---

## 📝 CAPTION
```
ElevenLabs $22/tháng → $0/tháng với Supertonic local TTS 🎙️

99M params · CPU only · 31 ngôn ngữ · tiếng Việt có · 1,263 ký tự/giây

Thay ElevenLabs không cần đổi code — local OpenAI-compatible API

5.3k ⭐ MIT · github.com/supertone-inc/supertonic

#tts #voiceover #vibecoding #contentcreator #ai #python #elevenlabs
```

## 🎯 B-ROLL
1. ElevenLabs pricing → Supertonic GitHub (contrast)
2. **Audio demo quan trọng nhất** — người xem cần nghe output
3. Terminal: `pip install supertonic` → chạy synthesis → play audio
4. Benchmark chart: 1,263 chars/s
5. `supertonic serve` → show API endpoint

---
*Script v1 — tháng 6/2026*
