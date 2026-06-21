# OpenMontage — Hệ Thống Sản Xuất Video AI Agent Đầu Tiên Thế Giới

## TL;DR
7.4K stars, 12 pipeline, 52 tools, 500+ agent skills — biến Claude Code (hoặc Cursor/Copilot) thành studio video production đầy đủ. Mô tả bằng tiếng thường, agent tự lo toàn bộ: research, script, hình ảnh, voiceover, nhạc, caption, render. Video Pixar-style 60 giây tốn $1.33.

## Tool này dùng để làm gì
OpenMontage không phải tool "animate vài ảnh rồi gọi là video". Nó là hệ thống agent thật sự với 12 pipeline riêng biệt:

- **Animated short** — phim hoạt hình kiểu Pixar/Ghibli từ script (dùng Kling v3, FLUX)
- **Documentary montage** — ghép real footage từ stock, không cần narration
- **Product ad** — quảng cáo sản phẩm chỉ cần 1 API key OpenAI ($0.69/video)
- **Explainer** — video giải thích concept với animation
- **Cinematic trailer** — trailer phim sci-fi với Veo-generated clips
- ...và 7 pipeline khác

Agent tự động làm:
1. Research topic bằng live web search
2. Viết script + scene plan
3. Generate hình ảnh / video clip (FLUX, Kling, Veo, gpt-image-1...)
4. Voiceover (ElevenLabs, Google Chirp3-HD, OpenAI TTS, hoặc Piper TTS miễn phí)
5. Nhạc nền tự tìm royalty-free hoặc gen Suno
6. Caption word-by-word kiểu TikTok (WhisperX)
7. Render file hoàn chỉnh qua Remotion + FFmpeg
8. Self-review: ffprobe validation, frame sampling, audio check trước khi xong

Dùng được với: Claude Code, Cursor, Copilot, Windsurf, Codex, OpenClaw.

## Setup từng bước
```bash
# Prerequisites: Python 3.10+, FFmpeg, Node.js 18+, 1 AI coding assistant

# Bước 1: Clone và setup
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
# (Nếu không có make: pip install -r requirements.txt && cd remotion-composer && npm install && cd ..)

# Bước 2: Config API keys trong .env
cp .env.example .env
# Thêm key vào — mọi key đều optional, thêm cái nào có cái đó:

# Image/video:  FAL_KEY (FLUX + Kling + Veo qua fal.ai)
# Stock media:  PEXELS_API_KEY, PIXABAY_API_KEY (miễn phí)
# Music:        SUNO_API_KEY hoặc ELEVENLABS_API_KEY
# Voice:        ELEVENLABS_API_KEY hoặc OPENAI_API_KEY
# Chỉ cần 1 key là đã chạy được pipeline cơ bản

# Bước 3: Mở project trong Claude Code (hoặc Cursor)
# Gõ prompt mô tả video muốn làm
```

**Key tối thiểu để bắt đầu:**
- Chỉ có `OPENAI_API_KEY` → đủ làm product ad pipeline ($0.69/video)
- Thêm `FAL_KEY` → unlock Kling v3 animated shorts ($1.33/video Pixar-style)
- Thêm `PEXELS_API_KEY` (miễn phí) → real footage documentary

## Ví dụ thực tế
**Video 1 — Pixar-style animated short:**
```
"THE LAST BANANA" — chuối cô đơn kết bạn với kiwi
Pipeline: Kling v3 (6 clips) + Google Chirp3-HD narration + piano nhạc nền + TikTok captions + Remotion
Chi phí: $1.33
```

**Video 2 — Product ad:**
```
"VOID — Neural Interface" — quảng cáo thiết bị AI
Pipeline: gpt-image-1 (4 ảnh) + OpenAI TTS + nhạc royalty-free auto + WhisperX subtitles
Chi phí: $0.69 — chỉ cần 1 API key OpenAI
```

**Video 3 — Ghibli anime:**
```
"Afternoon in Candyland" — cô bé trong thế giới kẹo
Pipeline: 12 FLUX images + Ken Burns motion + sparkle particles + ambient music
Chi phí: $0.15 — không cần video gen, chỉ cần FLUX images
```

**Với content không lộ mặt của mày:**
```
"Làm video 60s về top 3 Claude Code tools tuần này.
Style: animated explainer, giọng nam trẻ, nhạc lo-fi, caption TikTok, format 9:16"
→ Agent research → script → generate → render → file xong
```

Hoặc clone từ video có sẵn:
```
"Here's a TikTok I love [paste link]. 
Make me something like this, but about AI tools for Vietnamese developers."
```

## Lưu ý / Lỗi thường gặp
- Windows: nếu `npm install` báo `ERR_INVALID_ARG_TYPE` → dùng `npx --yes npm install`
- Không có `make` → chạy thủ công từng lệnh trong README
- Mỗi pipeline có cost khác nhau — đọc pipeline manifest trước khi chạy
- Video gen async (Kling, Veo) — agent poll kết quả, cần đợi vài phút
- Self-review chạy tự động trước khi xong — nếu fail thì agent tự fix lại
- Tốt nhất khi dùng với Claude Code (có AGENT_GUIDE.md riêng cho agentic flow)

## Đánh giá cá nhân
- **Điểm mạnh:** Đây là cái gần "fully automated content factory" nhất hiện tại. 12 pipeline cover mọi style video. Chi phí cực thấp ($0.15-$1.33/video). Self-review loop là điểm cộng lớn — output chất lượng hơn hẳn so với gen thẳng. Remotion + FFmpeg render thật sự, không fake
- **Điểm yếu:** Setup cần nhiều prerequisite (Python + Node + FFmpeg + AI assistant). Nhiều pipeline và tool có thể overwhelm lúc đầu. Vẫn cần hiểu cơ bản về agentic workflow để dùng hiệu quả
- **Có nên dùng không:** 9.5/10 — đây là tool quan trọng nhất cho content factory tự động. Nếu mày đang nghĩ đến việc scale content, OpenMontage là infrastructure cần build trước. Priority cao hơn cả Remotion Superpowers vì scope lớn hơn nhiều

## Link
- Repo: https://github.com/calesthio/OpenMontage
- YouTube demos: https://www.youtube.com/@OpenMontage
- X/Twitter: https://x.com/calesthioailabs
- Agent Guide: https://github.com/calesthio/OpenMontage/blob/main/AGENT_GUIDE.md
