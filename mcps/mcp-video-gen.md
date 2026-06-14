# mcp-video-gen — Video AI Miễn Phí: CogVideoX Unlimited + 6 Providers

**GitHub:** https://github.com/kevinten-ai/mcp-video-gen
**Stars:** 2⭐ | **License:** MIT | **Version:** 1.2.0
**Dùng với:** Claude Code, Claude Desktop, Cursor

---

## FREE Tier Thực Sự

| Provider | Free Tier | Quality | Duration |
|----------|-----------|---------|----------|
| **CogVideoX-Flash** | ✅ **Unlimited FREE** | 1440x960 | 6s |
| DashScope/Wan | 50s free (90 ngày) | 1080P | 5-10s |
| Kling AI | 66 credits/ngày | 720p | 5-10s |
| SiliconFlow | $1 signup bonus | 720p | varies |
| Vidu | 200 promo credits | 720p | 4s |

**→ Dùng CogVideoX trước: unlimited + free mãi mãi**

---

## Cài Đặt

```bash
git clone https://github.com/kevinten-ai/mcp-video-gen
cd mcp-video-gen
pip install -r requirements.txt

# Chỉ cần API key của provider mày dùng
# CogVideoX (free unlimited): đăng ký bigmodel.cn → free
export ZHIPUAI_API_KEY="..."  # CogVideoX — free tier
```

```json
{
  "mcpServers": {
    "video-gen": {
      "command": "python",
      "args": ["/path/to/mcp-video-gen/server.py"],
      "env": {
        "ZHIPUAI_API_KEY": "your-key"
      }
    }
  }
}
```

---

## Dùng Ngay

```bash
# CogVideoX — FREE UNLIMITED
"Generate video: AI robot typing code, neon office background,
 cinematic lighting, 6 seconds" --provider cogvideox

# Wan2.1 — HIGH QUALITY (50s free)
"Generate video: product launch reveal, dramatic lighting,
 slow motion, 10 seconds" --provider dashscope

# Image to video
"Convert this thumbnail image to 3-second animation,
 subtle camera zoom in" --provider veo
```

---

## Tools

| Tool | Làm gì |
|------|--------|
| `generate_video` | Text → video |
| `query_video_status` | Check tiến độ |
| `image_to_video` | Ảnh → video |
| `generate_speech` | TTS |
| `generate_music` | Background music |
| `transcribe_audio` | STT với timestamps |

---

## Workflow Video Ngắn (FREE)

```bash
# Step 1: Script → Voiceover (supertonic, free)
supertonic --text "script.txt" --lang vi --out voice.wav

# Step 2: Video background (CogVideoX, free)
"Generate video: [scene description], 6 seconds" --provider cogvideox

# Step 3: Thumbnail (pollinations-mcp, free)
"Generate image: thumbnail for this video" → pollinations

# Step 4: Merge (FFmpeg)
ffmpeg -i background.mp4 -i voice.wav -i thumbnail.jpg   -map 0:v -map 1:a final.mp4
```

---

*Nguồn: github.com/kevinten-ai/mcp-video-gen | MIT | tháng 6/2026*
