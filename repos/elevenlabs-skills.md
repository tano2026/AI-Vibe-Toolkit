# ElevenLabs Skills — GitHub Repo

## TL;DR
Bộ 10 skill chính chủ của ElevenLabs để Claude Code (hoặc agent nào theo chuẩn Agent Skills) biết gọi đúng API ElevenLabs: đọc văn bản thành giọng, phiên âm, tạo SFX, nhạc, tách giọng, lồng tiếng. Cài một lệnh `npx skills add elevenlabs/skills`, license MIT. **Cảnh báo lớn nhất:** repo chỉ là "sách hướng dẫn" cho agent, mọi skill đều cần **API key ElevenLabs** và gọi dịch vụ tính phí theo gói. Code MIT không có nghĩa là audio sinh ra được dùng thương mại miễn phí.

## Repo này dùng để làm gì
Không phải thư viện giọng nói. Nó dạy agent cách dùng ElevenLabs cho đúng, đỡ phải tự mò docs:
- Agent viết script xong tự gọi text-to-speech ra voiceover.
- Agent tự phiên âm file audio có timestamp để làm phụ đề.
- Agent tạo SFX hoặc nhạc nền theo mô tả.
- Tách giọng khỏi tiếng ồn, hoặc lồng tiếng sang ngôn ngữ khác mà giữ giọng người nói.

Nó khớp thẳng với dây chuyền "script → giọng đọc → video" của kho (script video đã viết sẵn dạng ElevenLabs-ready).

## Số liệu đã kiểm (2026-10-10)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao | 482 | 📖 trang repo qua fetch, chưa đối chiếu bằng API |
| Fork | 81 | 📖 cùng nguồn |
| License | MIT | 📖 trang repo + README |
| Số commit | 238 | 📖 trang repo |
| Commit gần nhất | **chưa đo** (trang không hiện ngày) | ❓ |
| Số skill | 10 | 📖 bảng trong README gốc (✅ tải raw README) |

10 skill: `text-to-speech`, `speech-to-text`, `speech-engine`, `agents`, `sound-effects`, `music`, `voice-changer`, `voice-isolator`, `dubbing`, `setup-api-key`.

## Setup
Theo README gốc (📖 đọc từ raw, **chưa chạy**):
```bash
# Cài skill
npx skills add elevenlabs/skills

# Đặt API key (lấy ở dashboard ElevenLabs hoặc dùng skill setup-api-key)
export ELEVENLABS_API_KEY="your-api-key"

# SDK nếu cần tự viết code
pip install elevenlabs                       # Python
npm install @elevenlabs/elevenlabs-js        # JS/TS
```
Cảnh báo của chính README: dùng `@elevenlabs/elevenlabs-js`, **đừng** `npm install elevenlabs` (đó là gói v1.x cũ).

## ⚠️ License / Bảo mật / Quyền riêng tư
- Code skill: MIT.
- Dịch vụ ElevenLabs: tính theo gói. Quyền dùng thương mại với từng gói **tao chưa kiểm** trên trang giá chính thức. Infographic mày gửi có ghi gói miễn phí không dùng thương mại, nhưng đó là lời của người làm infographic, không phải tao tự đọc điều khoản. Đọc điều khoản trước khi gắn voiceover vào bài bán hàng.
- API key là bí mật: chỉ để trong biến môi trường, không dán vào file .md, không commit.

## Ví dụ thực tế
1. **Voiceover video ngắn:** đưa script 55 giây (như các script trong `/content/`), agent gọi text-to-speech, ra file mp3. Ghép với video bằng ffmpeg (xem `repos/ffmpeg.md`).
2. **Phụ đề:** có file audio, agent gọi speech-to-text lấy timestamp. Lựa chọn thay thế miễn phí chạy local là Whisper (xem `repos/whisper.md`).
3. **Làm sạch audio:** file ghi âm podcast có tiếng ồn nền, dùng voice-isolator trước khi dựng.

## Lưu ý / Lỗi thường gặp
- Mọi skill đòi API key. Không có key thì cài xong cũng không chạy được gì.
- Chạy bộ `evals/` của repo cần thêm Cursor Agent CLI và đăng nhập Cursor. Không cần cho việc dùng skill bình thường.
- Chất lượng giọng tiếng Việt ❓ chưa nghe thử, phải test bằng một đoạn script thật trước khi chọn voice.
- Tiêu tiền theo ký tự: nên đặt giới hạn dùng trong dashboard trước khi cho agent chạy hàng loạt.

## Đánh giá cá nhân
**7/10 cho nhu cầu có ElevenLabs sẵn.** Điểm mạnh: chính chủ, MIT, cấu trúc gọn, đủ cả TTS lẫn STT lẫn SFX nên một chỗ cover cả khâu âm thanh. Điểm yếu: chỉ ít giá trị nếu không trả tiền cho ElevenLabs, và 482 sao nghĩa là cộng đồng nhỏ, ít bài người khác đã thử thật để học lỗi. Chưa chạy skill nào nên tao không chấm chất lượng đầu ra.

## Link
- Repo: https://github.com/elevenlabs/skills
- Chuẩn Agent Skills: https://agentskills.io/specification
- Liên quan trong kho: `repos/ffmpeg.md`, `repos/whisper.md`

---

## 🤖 Agent Integration

> Repo này là skill cho agent, nhưng phần gọi API bên dưới viết bằng urllib để Hermes dùng thẳng, không cần cài gì.

### Hermes (Python)
```python
# ❓ Chưa chạy (chưa có API key). Endpoint và header theo tài liệu công khai của ElevenLabs,
#    kiểm lại trên docs trước khi dùng thật.
import json, os, urllib.request

def tts(text: str, voice_id: str, out_path: str, model_id: str = "eleven_multilingual_v2"):
    key = os.environ["ELEVENLABS_API_KEY"]          # không in, không log
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=json.dumps({"text": text, "model_id": model_id}).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r, open(out_path, "wb") as f:
        f.write(r.read())

# tts("Xin chào các bạn", "[VOICE_ID]", "out.mp3")
```

### OpenClaw
```bash
npx skills add elevenlabs/skills
```

### Antigravity
```bash
# ❓ chưa chạy. Chỉ kiểm có key hay chưa, không in giá trị.
python3 - <<'EOF'
import os
print("ELEVENLABS_API_KEY", "OK" if os.environ.get("ELEVENLABS_API_KEY") else "THIẾU")
EOF
```
> ⚠️ API key đặt trong biến môi trường của service (PM2/systemd), không để trong script hay repo.
