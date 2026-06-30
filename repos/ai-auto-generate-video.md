# AI-auto-generate-video — GitHub Repo

## TL;DR
Pipeline tu dong: bai viet tieng Viet (URL hoac .txt) → video 9:16 hoan chinh trong vai phut. Dung Claude Code slash command `/create-template-video`, ket hop OmniVoice (TTS local, khong can API key) + HyperFrames (render template) + FFmpeg (mux). Output: video.mp4 + voice.mp3 + script.txt — san sang up CapCut/TikTok/Shorts/Reels.

## Repo nay dung de lam gi
Day chinh la pipeline ma kho dang can: bai viet → video, khong can mo CapCut thu cong, khong can ElevenLabs tra phi.

**Triet ly thiet ke:** AI lo phan *content* (script + chon template). Code deterministic lo phan *production* (render pixel). Cung mot `script.json` luon render ra video giong nhau — khong bat ngo, khong sua tay.

**8 buoc pipeline (deterministic, trong `src/render/template-pipeline.ts`):**
1. Validate `script.json` theo Zod schema
2. Caption text → `script.txt` (CapCut auto-caption dung file nay)
3. TTS moi scene qua OmniVoice → `voice/scene-<id>.mp3`
4. Concat voice voi gap 0.3s → `voice-raw.mp3`
5. Mix SFX vao narration → `voice.mp3`
6. Render moi template qua HyperFrames (Chromium) → `clips/scene-<id>-fit.mp4`
7. Concat clips + mux audio → `video.mp4`
8. Done — in duong dan + tong thoi luong

**Output 3 file:**
| File | Dung de |
|------|---------|
| `video.mp4` | Video 9:16 hoan chinh, co voice + SFX |
| `voice.mp3` | Track narration rieng — keo vao CapCut |
| `script.txt` | Text thuan — CapCut auto-caption |

## Setup tung buoc

### Yeu cau
```
Node.js >= 22
FFmpeg + ffprobe (phai co trong PATH)
Chrome/Chromium (HyperFrames dung de render)
OmniVoice server chay local (TTS, khong can API key)
Claude Code CLI (optional — chi can cho slash command)
```

```bash
# Cai FFmpeg
# Windows: winget install Gyan.FFmpeg
# macOS:   brew install ffmpeg
# Linux:   sudo apt install ffmpeg

# Clone repo
git clone https://github.com/huytranvan2010/AI-auto-generate-video
cd AI-auto-generate-video
npm install
```

### Config `.env.local`

```env
TTS_PROVIDER=omnivoice
OMNIVOICE_ENDPOINT=http://127.0.0.1:8123
```

OmniVoice la TTS provider duy nhat — chay local, khong can API key. Server phai nhan `POST /tts` voi `{ text }`, tra ve `audio/mpeg` bytes.

### Chay pipeline

**Cach 1 — Trong Claude Code (khuyen nghi):**
```text
/create-template-video https://link-bai-viet.com/article
/create-template-video news/my-article.txt
```
Claude tu fetch noi dung, viet `script.json`, chay het pipeline.

**Cach 2 — Chay truc tiep voi script.json co san:**
```bash
npm run pipeline -- output/my-video/script.json
```

Vai phut sau → `output/<slug>/video.mp4` (1080x1920).

## Ung dung cho kho AI Vibe Toolkit

**Pipeline hien tai cua may (script viet san trong /content/):**
```
Script .md trong kho
    ↓ (convert sang script.json theo schema)
/create-template-video kho/content/script-video-XXX.txt
    ↓
OmniVoice TTS (hoac thay bang Resona qua wrapper)
    ↓
HyperFrames render template
    ↓
video.mp4 + voice.mp3 + script.txt
    ↓
Upload TikTok/YouTube Shorts
```

**Thay OmniVoice bang Resona (giong VN tot hon):**
```javascript
// Sua endpoint trong .env.local de tro ve Resona wrapper
// hoac viet adapter nho:
// POST /tts { text } → goi Resona API → tra ve audio/mpeg
```

## Vi du thuc te

**Lay 1 script da co trong kho, render thanh video:**
```bash
# Gia su da co script.json cho "script-video-107-gstack"
npm run pipeline -- output/gstack-review/script.json

# Output sau ~3-5 phut:
# output/gstack-review/video.mp4   ← upload thang
# output/gstack-review/voice.mp3   ← backup audio
# output/gstack-review/script.txt ← paste vao CapCut auto-caption
```

## Luu y / Loi thuong gap
- OmniVoice phai chay truoc khi goi pipeline — server local, khong tu start
- Chrome/Chromium can cai dung version — HyperFrames dung Chromium de render template
- Script.json phai dung Zod schema — sai format se bi reject o buoc Validate
- Templates own toan bo design — chi cung cap text, khong chinh duoc layout thu cong (deu tot voi nguoi khong biet design)
- 77 stars — con moi, nhung concept va execution rat chac

## Danh gia ca nhan
- Diem manh: Pipeline deterministic that su (cung input → cung output, khong bat ngo); tich hop Claude Code slash command tien loi; TTS local khong ton API; 3 file output deu huu ich rieng
- Diem yeu: Can setup OmniVoice server rieng; templates co dinh, it tuy chinh visual; community con nho (77 stars)
- Co nen dung khong: **8.5/10** — Day la huong dung dan voi pipeline tu dong hoa content da de xuat truoc do (HyperFrames + TTS + FFmpeg). Setup mot lan, moi script trong kho deu render duoc thanh video chi voi mot slash command.

## Link
- Repo: https://github.com/huytranvan2010/AI-auto-generate-video
- Demo: https://youtube.com/shorts/LUAgRhPBONg
- License: MIT
- Stack: Node.js 22+, TypeScript, HyperFrames, OmniVoice, FFmpeg
