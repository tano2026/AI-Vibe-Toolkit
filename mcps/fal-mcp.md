# fal-mcp — 600+ AI Models: Image, Video, Audio, Music (Cloud, No GPU)

**GitHub:** https://github.com/enescanguven/fal-mcp
**fal.ai:** 600+ models | **License:** MIT | Không cần GPU
**Cập nhật:** 3/2026

---

## Đây Là Gì

MCP server cho fal.ai — access 600+ AI models cho image generation, video creation, speech-to-text, TTS, music generation **thẳng từ Claude**. Không cần GPU, chạy trên cloud.

---

## Cài Đặt

```bash
git clone https://github.com/enescanguven/fal-mcp.git
cd fal-mcp
npm install && npm run build

claude mcp add fal-ai -e FAL_KEY=your-key -- node dist/index.js
```

**Lấy API key:** fal.ai → Dashboard → API Keys (free tier có $5 credit)

## Config Claude Desktop

```json
{
  "mcpServers": {
    "fal-ai": {
      "command": "node",
      "args": ["/path/to/fal-mcp/dist/index.js"],
      "env": { "FAL_KEY": "your-fal-api-key" }
    }
  }
}
```

---

## 8 Tools

```bash
# Image Generation
generate_image "minimalist logo for AI tool, white on dark background"
generate_image "photorealistic product shot, studio lighting" --model flux-pro

# Image Editing
edit_image --input photo.jpg "remove background, add transparent"
edit_image --input product.jpg "upscale 4x, enhance details"

# Video Generation
generate_video "drone shot flying over neon city at night, 5 seconds"
generate_video --image thumbnail.jpg "camera slowly zooming in, 3 seconds"

# Audio
speech_to_text --audio interview.mp3  # transcribe
text_to_speech "Xin chào! Đây là AI Vibe Toolkit" --voice vi-female
generate_music "upbeat electronic background music, 30 seconds"

# Discovery
search_models "video generation"  # tìm model phù hợp
run_model "fal-ai/flux-pro" --prompt "..." --params {...}
```

---

## Top Models Trên fal.ai

### Image
- `fal-ai/flux-pro` — chất lượng cao nhất ($0.05/image)
- `fal-ai/flux-schnell` — nhanh + rẻ ($0.003/image)
- `fal-ai/recraft-v3` — vector style, logo, illustration
- `fal-ai/ideogram-v2` — text trong image cực tốt

### Video
- `fal-ai/kling-video` — realistic video quality
- `fal-ai/veo2` — Google Veo2
- `fal-ai/ltx-video` — nhanh, phù hợp draft

### Audio
- `fal-ai/whisper` — transcription tốt nhất
- `fal-ai/playai-tts` — TTS natural
- `fal-ai/stable-audio` — music generation

---

## So Sánh Với comfyui-mcp

| | fal-mcp | comfyui-mcp |
|--|---------|-------------|
| GPU cần | ❌ Cloud | ✅ Local GPU |
| Setup | Dễ (5 phút) | Phức tạp hơn |
| Chi phí | Per-image/video | Điện + hardware |
| Models | 600+ | Phụ thuộc cài gì |
| Video | ✅ (Kling, Veo2) | ✅ (WAN, LTX) |
| Privacy | Cloud | Local |
| Best for | Quick, cloud | Customization |

**Rule:** Cần nhanh, không có GPU → fal-mcp. Cần control, có GPU → comfyui-mcp.

---

*Nguồn: github.com/enescanguven/fal-mcp | fal.ai 600+ models | tháng 6/2026*

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity — không phải cho human đọc.

### Hermes (Python — gọi thẳng, không cần MCP)
```python
import urllib.request, json

def fal_generate_image(prompt, model="fal-ai/flux/schnell", api_key=None):
    """Generate ảnh qua fal.ai API"""
    payload = json.dumps({"prompt": prompt}).encode()
    req = urllib.request.Request(
        f"https://fal.run/{model}",
        data=payload,
        headers={"Authorization": f"Key {api_key}",
                 "Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["images"][0]["url"]  # URL ảnh đã generate

def fal_text_to_speech(text, voice="af_bella", api_key=None):
    payload = json.dumps({"input": text, "voice": voice}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/kokoro/american-english",
        data=payload,
        headers={"Authorization": f"Key {api_key}",
                 "Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["audio"]["url"]

# Dùng: img_url = fal_generate_image("sunset Vietnam", api_key=os.environ["FAL_KEY"])
```

### OpenClaw (npm/ClawHub)
```bash
# Gọi thẳng API — không cần MCP
# pip install fal-client (nếu muốn SDK)
```

### Antigravity (deploy nếu cần self-host)
```bash
# Không cần deploy
# Set env: FAL_KEY=xxx
# Lấy key: fal.ai/dashboard
```
> ⚠️ Pay-per-use. Flux Schnell rất rẻ (~$0.003/ảnh). Có free credits khi signup.
