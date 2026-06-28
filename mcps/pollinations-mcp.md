# pollinations-mcp — Image/Video/Audio FREE, Không Cần API Key

**GitHub:** https://github.com/atiaeno/pollinations-mcp
**npm:** pollinations-mcp | **License:** ISC
**Powered by:** pollinations.ai — open AI infrastructure
**Dùng với:** Claude Code, Claude Desktop, Cursor, Windsurf, Cascade

---

## 🆓 Hoàn Toàn Miễn Phí — Không Đăng Ký, Không API Key

```
pollinations.ai = free, open, no limits
Flux · Imagen 4 · GPT Image · 20+ image models
Veo · Seedance · Wan · video models
TTS 35+ voices · Whisper transcription
```

---

## Cài 1 Lệnh

```bash
# Option A: npx (không cần clone)
npx pollinations-mcp

# Option B: npm install
npm install -g pollinations-mcp
pollinations-mcp
```

```json
{
  "mcpServers": {
    "pollinations": {
      "command": "npx",
      "args": ["-y", "pollinations-mcp"]
    }
  }
}
```

**Không cần env variables, không cần API key. Chạy ngay.**

---

## Claude Code Plugin (Tollerable version)

```bash
# Cài plugin đầy đủ hơn (50+ models)
/plugin marketplace add Tolerable/pollinations-claude-code
/plugin install pollinations@tolerable-pollinations
```

---

## Dùng Ngay

```bash
# Image generation — FREE
"Generate image: dark cinematic thumbnail, glowing text 'AI Vibe Toolkit',
 floating particles, 1920x1080, ultra detailed"

"Tạo logo minimalist cho AI channel, white on dark background"

"Product mockup: laptop screen showing code, coffee cup, dark desk"

# Chọn model
"Generate image using flux-dev: [prompt]"     # FLUX Dev
"Generate image using gpt-image-1: [prompt]"  # GPT Image
"Generate image using imagen-4: [prompt]"     # Google Imagen 4
"Generate image using kontext: [prompt]"      # Adobe Firefly style

# Video — FREE
"Generate video: logo reveal animation, 3 seconds, dark background"
"Create video using veo: drone city shot night, 5 seconds"

# Audio — FREE
"Text to speech: 'Xin chào, đây là AI Vibe Toolkit' voice=vi-female"
"Transcribe audio file: interview.mp3"
```

---

## Models Available

### Image (20+ models, tất cả FREE)
| Model | Đặc điểm |
|-------|---------|
| `flux` | Default, cân bằng quality/speed |
| `flux-dev` | Quality cao nhất |
| `flux-schnell` | Nhanh nhất |
| `gpt-image-1` | OpenAI style |
| `imagen-4` | Google, photorealistic |
| `kontext` | Consistent characters |
| `turbo` | Draft, nhanh |

### Video (FREE)
- `veo` — Google Veo
- `seedance` — ByteDance
- `wan` — Wan2.1

### Audio (FREE)
- TTS: 35+ voices (ElevenLabs-style, OpenAI-style)
- STT: Whisper

---

## Workflow Thumbnail AI Vibe Toolkit

```bash
# 1. Generate thumbnail draft (free)
"Generate image using flux: dark bg, bold text '[TOOL NAME]',
 glowing neon accent, particle effects, cinematic, 1920x1080"

# 2. Generate nhiều variants
"Generate 4 variants của thumbnail trên với màu accent khác nhau:
 blue, green, purple, orange"

# 3. Pick best → done
# Không tốn 1 xu
```

---

*Nguồn: atiaeno/pollinations-mcp + Tolerable/pollinations-claude-code*
*pollinations.ai — FREE, no API key | tháng 6/2026*

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity — không phải cho human đọc.

### Hermes (Python — gọi thẳng, không cần MCP)
```python
import urllib.request, urllib.parse

def pollinations_image(prompt, width=1024, height=1024, model="flux"):
    """Tạo ảnh free, không cần API key"""
    p = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{p}?width={width}&height={height}&model={model}&nologo=true"
    # Download ảnh
    urllib.request.urlretrieve(url, "output.png")
    return url  # hoặc return path

def pollinations_text(prompt, model="openai"):
    """Generate text free, không cần API key"""
    payload = json.dumps({"messages": [{"role": "user", "content": prompt}],
                          "model": model}).encode()
    req = urllib.request.Request(
        "https://text.pollinations.ai/openai",
        data=payload, headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req).read().decode()

import json
# Dùng: url = pollinations_image("a beautiful sunset in Vietnam")
```

### OpenClaw (npm/ClawHub)
```bash
npx -y pollinations-mcp
```

### Antigravity (deploy nếu cần self-host)
```bash
# Không cần deploy — free public API, không cần key
```
> ⚠️ Hoàn toàn free, không cần API key. Rate limit thoải mái.
