---
name: minimax-mcp
description: >
  MCP server chính thức từ MiniMax — tích hợp text-to-speech, voice cloning,
  video generation, image generation và music generation vào Claude workflow.
  1.5K stars, update liên tục, có cả model Hailuo-02 1080P.
---

# MiniMax MCP — TTS + Video + Nhạc Trong 1 MCP Server

## TL;DR
MCP server chính thức từ MiniMax — tích hợp text-to-speech, voice cloning, video generation, image generation và music generation vào Claude workflow. 1.5K stars, update liên tục, có cả model Hailuo-02 1080P.

## Tool này dùng để làm gì
MiniMax là AI company lớn của Trung Quốc (ngang tầm OpenAI ở thị trường CN). MCP server này cho phép Claude gọi thẳng API MiniMax để:

- **Text-to-Speech** — đọc text thành giọng nói, nhiều voice khác nhau
- **Voice Cloning** — clone giọng từ file audio của mày
- **Voice Design** — mô tả giọng muốn bằng text, AI tạo ra
- **Video Generation** — generate video từ prompt (model Hailuo-02, 6s hoặc 10s, 768P/1080P)
- **Image Generation** — text-to-image
- **Music Generation** — generate nhạc từ prompt + lyrics (model music-1.5) — ⚠️ tool này KHÔNG thấy trong bảng công cụ chính thức mới nhất (chỉ có text_to_audio, list_voices, voice_clone, voice_design, generate_video, query_video_generation, text_to_image) — có thể đã bị gỡ hoặc chưa release rộng, test lại trước khi dựa vào.

Dùng thẳng trong Claude Code hoặc bất kỳ MCP client nào.

## Setup từng bước

> ⚠️ **Sửa lại so với bản cũ trong kho:** package `@minimax-ai/mcp` qua `npx` KHÔNG đúng — server chính thức là gói Python `minimax-mcp`, cài qua `uv`/`uvx`, không phải npm.

```bash
# Bước 1: Lấy API key
# Global: https://www.minimax.io/platform/user-center/basic-information/interface-key
# Mainland CN: https://platform.minimaxi.com

# Bước 2: Cài uv (trình quản lý gói Python) nếu chưa có
curl -LsSf https://astral.sh/uv/install.sh | sh

# Bước 3: Thêm vào claude_desktop_config.json (đúng cấu hình chính thức)
{
  "mcpServers": {
    "MiniMax": {
      "command": "uvx",
      "args": ["minimax-mcp", "-y"],
      "env": {
        "MINIMAX_API_KEY": "your_api_key_here",
        "MINIMAX_MCP_BASE_PATH": "local-output-dir-path, ví dụ /User/xxx/Desktop",
        "MINIMAX_API_HOST": "https://api.minimax.io hoặc https://api.minimaxi.com (CN)",
        "MINIMAX_API_RESOURCE_MODE": "url (mặc định) hoặc local"
      }
    }
  }
}

# Bước 4: Restart Claude và test
# Claude sẽ thấy tools: text_to_audio, list_voices, voice_clone, voice_design,
# generate_video, query_video_generation, text_to_image
```

**Có sẵn CLI tác nhân riêng (đáng chú ý cho OpenClaw):** MiniMax CLI (`mmx-cli`, github.com/MiniMax-AI/cli) — hoạt động như 1 agent skill trực tiếp cho Claude Code/Cursor/OpenClaw, không cần qua MCP config, có sẵn model mới nhất + text/vision/search.

## Ví dụ thực tế
**Tình huống 1 — Clone giọng để làm voiceover:**
```
Tool: voice_clone
Input: file audio giọng mày đọc 30 giây
Output: voice ID → dùng cho text_to_audio sau đó
```

**Tình huống 2 — Generate video clip cho content:**
```
Tool: generate_video
Prompt: "Close-up of hands typing on keyboard, cinematic, dark mood"
Model: MiniMax-Hailuo-02
Duration: 6s
Resolution: 1080P
→ Claude generate và trả về link download video
```

**Tình huống 3 — Nhạc nền tự động:**
```
Tool: music_generation
Prompt: "chill lo-fi beats, calm, for study content"
→ File nhạc mp3 download được
```

## Lưu ý / Lỗi thường gặp
- API key phải khớp region: Global key dùng `api.minimax.io`, CN key dùng endpoint khác
- Video generation tốn credit nhiều hơn TTS — xem pricing trước
- `query_video_generation` phải poll để lấy kết quả (video gen async, không phải instant)
- Voice cloning cần ít nhất 30 giây audio sạch, không có tiếng ồn
- Model Hailuo-02 cho video đẹp hơn nhưng tốn credit hơn

## Đánh giá cá nhân
- **Điểm mạnh:** All-in-one — TTS + video + nhạc + image trong 1 MCP. Voice cloning mạnh, video gen Hailuo-02 quality tốt. Chính thức từ MiniMax, update thường xuyên
- **Điểm yếu:** Tốn credit (không free nhiều), video gen có delay vì async. Pricing không rẻ nếu dùng nhiều video gen
- **Có nên dùng không:** 7.5/10 — tốt nhất cho voice cloning và TTS trong Claude workflow. Video gen thì dùng cho clip ngắn thôi, đừng lạm dụng vì tốn credit

## Link
- Repo: https://github.com/MiniMax-AI/MiniMax-MCP
- API platform: https://www.minimax.io/platform
- Docs: https://www.minimax.io/docs

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
import urllib.request, json

def minimax_tts(text, voice_id="male-qn-qingse", api_key=None, group_id=None):
    payload = json.dumps({
        "model": "speech-01-turbo", "text": text,
        "voice_setting": {"voice_id": voice_id, "speed": 1.0, "vol": 1.0, "pitch": 0},
        "audio_setting": {"sample_rate": 32000, "bitrate": 128000, "format": "mp3"}
    }).encode()
    req = urllib.request.Request(
        f"https://api.minimax.chat/v1/t2a_v2?GroupId={group_id}",
        data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    # Decode audio từ hex
    audio_hex = r["data"]["audio"]
    with open("output.mp3", "wb") as f:
        f.write(bytes.fromhex(audio_hex))
    return "output.mp3"

# Vietnamese voices: female-shaonv, male-qn-qingse, presenter_female
# Dùng: minimax_tts("Xin chào", voice_id="female-shaonv",
#            api_key=os.environ["MINIMAX_API_KEY"], group_id=os.environ["MINIMAX_GROUP_ID"])
```

### OpenClaw
```bash
# Cách 1: qua MCP config (giống Claude Desktop ở trên, dùng uvx minimax-mcp)
# Cách 2: qua CLI skill chính thức, không cần MCP config
uvx mmx-cli   # hoặc theo hướng dẫn github.com/MiniMax-AI/cli
# Set MINIMAX_API_KEY (theo đúng region — global vs CN, xem bảng ở trên)
```

### Antigravity
```bash
# Không cần deploy — cloud API
# Lấy key: platform.minimax.io
```
> ⚠️ Có tiếng Việt. TTS tốt thay thế ElevenLabs. Free credits khi signup.
