# html-video — AI Viết HTML, Mày Nhận MP4 (~346⭐)

**Repo:** github.com/nexu-io/html-video | Apache 2.0 | nexu-io
**Dùng với:** Claude Code, Cursor, Codex, Gemini CLI

---

## Concept

```
Mày describe video → AI viết HTML animation → html-video render → MP4
```

Không cần biết edit video. Không cần Premiere, CapCut. AI làm hết.

## Cài & Setup

```bash
git clone https://github.com/nexu-io/html-video
cd html-video
npm install
npx playwright install chromium
```

## Dùng Trong Claude Code

```bash
# Cài skill
/plugin marketplace add nexu-io/html-video

# Generate video
/html-video "tạo video intro 10 giây: logo xuất hiện từ giữa, fade in text 'AI Vibe Toolkit', background dark với particles"
```

## CLI Usage

```bash
# Convert HTML file → MP4
node render.js --input animation.html --output video.mp4 --duration 10

# Với custom resolution
node render.js --input animation.html --output video.mp4   --width 1920 --height 1080 --fps 60 --duration 15
```

## Prompt Templates

```bash
# Intro video
"10 giây, dark background, logo pulse animation, text fade in, 1920x1080"

# TikTok hook
"3 giây, vertical 1080x1920, text animation nhanh, màu neon trên đen"

# Data visualization
"15 giây, bar chart animate từ 0 lên, số đếm lên real-time, clean white bg"

# Product demo
"30 giây, mockup browser scroll down, highlight features lần lượt"
```

## Kết Hợp Với Pipeline Video Của Mày

```
Script video (content-creator.md skill)
→ html-video tạo intro/outro/transitions
→ OBS record screen demo
→ CapCut ghép lại
→ ElevenLabs voiceover
→ TikTok/YouTube
```

## So Sánh Với Remotion

| | html-video | Remotion |
|--|-----------|---------|
| Cần biết React? | ❌ | ✅ |
| Setup | Dễ | Trung bình |
| Customization | HTML/CSS | React full |
| Best for | Quick videos | Complex animations |

---
*skills/html-video-skill.md | AI Vibe Toolkit | tháng 6/2026*
