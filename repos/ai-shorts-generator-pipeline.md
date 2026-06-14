# AI Shorts Generator — Pipeline Playwright + Claude Code → MP4 Tự Động

**Concept từ:** TikTok @Meii | **Stack:** Claude Code + Playwright + FFmpeg
**Dạng:** Pattern/Workflow — không phải 1 repo cụ thể mà là pipeline architecture

---

## Pipeline Tổng Quan

```
MÀY                CLAUDE              CLAUDE
/promo [URL]  →  Fetch + analyze  →  Draft storyboard
/news [URL]      README, metadata     6 scenes · 25-32s

                        ↓
              MÀY REVIEW & APPROVE
                 storyboard.json
               (human-in-the-loop)

                        ↓
                  PLAYWRIGHT
              Record render.html
            16×9 + 9×16 viewports

                        ↓
                    FFMPEG
                 WebM → MP4
            + ElevenLabs voice mux

                        ↓
         OUTPUT 16×9 MP4          OUTPUT 9×16 MP4
        YouTube · LinkedIn        TikTok · Reels
```

---

## Scene Templates

```
hero-text     → Tên tool + tagline lớn, animation
terminal      → Code/command demo animated
stats-grid    → Numbers: stars, forks, performance
iframe        → Live demo embed
quote         → User testimonial hoặc key statement
cta-url       → Call to action + link
```

---

## Cách Implement

### Bước 1: Claude Code analyze repo

```bash
# Trong Claude Code
/promo https://github.com/owner/repo

# Claude sẽ:
# - Fetch README, package.json, stars, forks
# - Extract: what it does, key features, target audience
# - Draft storyboard.json với 6 scenes
```

### Bước 2: storyboard.json format

```json
{
  "title": "Tool Name",
  "duration": 28,
  "scenes": [
    {
      "type": "hero-text",
      "duration": 4,
      "content": {
        "headline": "Hook text here",
        "subtitle": "Supporting point"
      }
    },
    {
      "type": "terminal",
      "duration": 5,
      "content": {
        "command": "npx install tool",
        "output": "✅ Ready in 3s"
      }
    },
    {
      "type": "stats-grid",
      "duration": 4,
      "content": {
        "stats": [
          {"label": "Stars", "value": "59k"},
          {"label": "Time saved", "value": "4h→15min"}
        ]
      }
    },
    {
      "type": "cta-url",
      "duration": 4,
      "content": {
        "text": "Link trong bio",
        "url": "github.com/..."
      }
    }
  ]
}
```

### Bước 3: Render HTML

```javascript
// render.html — Claude generates này
// Mỗi scene = 1 div với CSS animation
// Playwright record với viewport 1920×1080 (16:9)
// và 1080×1920 (9:16) cho TikTok
```

### Bước 4: Playwright record

```bash
# Playwright chụp từng scene
npx playwright chromium   --screenshot render.html   --viewport 1920,1080

# Hoặc record video
node record.js --input render.html   --output output.webm   --viewport 1920x1080
```

### Bước 5: FFmpeg merge

```bash
# WebM → MP4 + voiceover
ffmpeg -i scenes.webm -i voice.mp3   -c:v libx264 -c:a aac   -shortest output_16x9.mp4

# Resize cho TikTok 9:16
ffmpeg -i output_16x9.mp4   -vf "scale=1080:1920:force_original_aspect_ratio=decrease,       pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black"   output_9x16.mp4
```

---

## Repos Có Thể Dùng Làm Base

| Repo | Stars | Dùng cho |
|------|-------|---------|
| **framecraft** | 6⭐ | Closest match — Claude generates HTML scenes → MP4 |
| **html-video** | 2.9k⭐ | HTML → MP4, 21 templates, AI soundtrack |
| **html-anything** | 6.2k⭐ | HTML rendering đẹp |
| **Remotion** | 49.9k⭐ | React → MP4, complex animations |

---

## Adapt Cho AI Vibe Toolkit

```bash
# Workflow cho mỗi video trong kho:

# 1. Mày quẳng link tool mới
/promo https://github.com/owner/tool

# 2. Claude fetch + analyze (dùng Context7 + Firecrawl MCP)
# → Tóm tắt: stars, features, install command, use case

# 3. Claude draft storyboard 6 scenes:
# Scene 1: Hook (hero-text) — vấn đề tool giải quyết
# Scene 2: Tool intro (hero-text) — tên + tagline
# Scene 3: Install (terminal) — 1 lệnh
# Scene 4: Demo (terminal/iframe) — cách dùng
# Scene 5: Stats (stats-grid) — stars, savings
# Scene 6: CTA (cta-url) — link trong bio

# 4. Mày review storyboard.json
# 5. Playwright render → FFmpeg → 2 formats
# 6. Supertonic voiceover (free) → mux

# Output: video YouTube + TikTok/Reels, $0
```

---

## Repos Liên Quan Đã Có Trong Kho

- `mcps/framecraft.md` — gần nhất với pipeline này
- `repos/html-video.md` — HTML → MP4 có sẵn templates
- `mcps/playwright.md` — record browser
- `skills/free-image-video-stack.md` — FFmpeg commands

---
*Pattern research từ TikTok @Meii | AI Vibe Toolkit | tháng 6/2026*
