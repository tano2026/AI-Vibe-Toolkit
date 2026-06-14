# framecraft — Describe → Claude Viết HTML → Render MP4 (FREE)

**GitHub:** https://github.com/vaddisrinivas/framecraft
**Stars:** 6⭐ | **Stack:** Python + FFmpeg + Playwright
**Dùng với:** Claude Code (skill + MCP)

---

## Concept

```
Mày describe video
→ Claude viết HTML scenes + narration
→ framecraft render HTML → MP4
→ $0, không cần GPU, không cần API key
```

Khác html-video: framecraft có narration, multi-scene, audio sync.

---

## Cài Đặt

```bash
git clone https://github.com/vaddisrinivas/framecraft
cd framecraft
pip install -r requirements.txt
playwright install chromium
```

```json
{
  "mcpServers": {
    "framecraft": {
      "command": "python",
      "args": ["/path/to/framecraft/mcp_server.py"]
    }
  }
}
```

---

## Dùng Ngay (Claude Code)

```bash
# Simple intro video
"Dùng framecraft tạo video intro 10 giây:
 Scene 1 (3s): Logo xuất hiện từ particles, dark background
 Scene 2 (4s): Text 'AI Vibe Toolkit' fade in, subtitle 'Tools for vibe coders'
 Scene 3 (3s): CTA 'Follow for more', particle explosion"

# Tool demo video
"Tạo demo video cho hermes-agent:
 Scene 1: Problem — generic AI không nhớ gì (5s)
 Scene 2: Solution — Hermes 8 loops diagram animate (10s)
 Scene 3: Code demo — terminal animation (8s)
 Scene 4: Results — 40% faster, 90 days compound (5s)"

# Tutorial style
"Video tutorial 30 giây: cách cài claude-seo plugin:
 Step 1: /plugin marketplace add (animated terminal)
 Step 2: /seo audit running (progress bar)
 Step 3: Results: score 87/100 (chart animate)"
```

---

## Output Formats

```bash
# MP4 (default)
framecraft render --input config.json --output video.mp4

# GIF (cho social media)
framecraft render --input config.json --output preview.gif --format gif

# Custom resolution
framecraft render --width 1080 --height 1920  # TikTok vertical
framecraft render --width 1920 --height 1080  # YouTube horizontal
```

---

## So Sánh Free Video Tools

| Tool | Cần GPU? | Quality | Effort |
|------|---------|---------|--------|
| **Pollinations MCP** | ❌ | Medium | Low |
| **CogVideoX (mcp-video-gen)** | ❌ Cloud | Good | Low |
| **WanGP Kaggle** | ❌ (Kaggle GPU) | Excellent | Medium |
| **framecraft** | ❌ | Programmatic | Low |
| **SD WebUI local** | ✅ | Excellent | High |
| **html-video** | ❌ | Programmatic | Low |

---

*Nguồn: github.com/vaddisrinivas/framecraft | MIT | tháng 6/2026*
