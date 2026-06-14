# comfyui-mcp — Image & Video AI Ngay Trong Claude Code (152⭐)

**GitHub:** https://github.com/artokun/comfyui-mcp
**Stars:** 152⭐ | **License:** MIT | **Language:** TypeScript
**Docs:** comfyui-mcp.artokun.io
**Cập nhật:** hôm qua (13/6/2026)

---

## Đây Là Gì

Claude Code plugin + MCP server cho ComfyUI — generate images và video, chỉnh sửa workflows, quản lý models, **tất cả từ trong Claude session**.

**88 MCP tools | 16 AI skills | 11 slash commands | 4 autonomous agents**

---

## Cài Đặt

```bash
# Claude Code (recommended)
/plugin marketplace add artokun/comfyui-mcp
/plugin install comfyui-mcp@artokun-comfyui-mcp

# Cần ComfyUI đang chạy
# Default: http://127.0.0.1:8188
# Hoặc set: COMFYUI_URL=http://your-host:port
```

## Config

```json
{
  "mcpServers": {
    "comfyui": {
      "command": "npx",
      "args": ["-y", "comfyui-mcp"],
      "env": {
        "COMFYUI_URL": "http://127.0.0.1:8188"
      }
    }
  }
}
```

---

## 11 Slash Commands

```bash
/image "cinematic portrait of a robot in neon city, 4k"
/video "time-lapse of flowers blooming, 5 seconds"
/image-edit "remove background from this image"
/upscale "enhance this to 4x resolution"
/workflow list          # xem workflows có sẵn
/workflow run [name]    # chạy workflow cụ thể
/workflow edit [name]   # Claude tự edit workflow
/model list             # xem models đã install
/model download [name]  # download model từ Civitai
/node search [query]    # tìm custom nodes
/node install [name]    # cài custom nodes
```

---

## 16 AI Skills — Chọn Đúng Model

| Skill | Model | Dùng khi |
|-------|-------|---------|
| `flux-dev` | FLUX.1 Dev | Quality cao nhất, chậm hơn |
| `flux-schnell` | FLUX.1 Schnell | Nhanh, draft quality |
| `wan-video` | WAN | Video generation |
| `ltx-video` | LTX-Video | Video nhanh |
| `z-image` | Z-Image | Portrait tốt |
| `qwen-vl` | Qwen VL | Vision + text |
| `sdxl` | SDXL 1.0 | Classic stable diffusion |
| `civitai-*` | Civitai models | Anime, realistic, styles |

---

## 4 Autonomous Agents

```bash
# 1. Style Transfer Agent
"Activate style-transfer: apply Van Gogh style to my product photos"

# 2. Batch Image Agent  
"Activate batch-processor: generate 20 variations of this logo"

# 3. Video Pipeline Agent
"Activate video-pipeline: text to video to upscale"

# 4. Model Manager Agent
"Activate model-manager: find and install best portrait model from Civitai"
```

---

## Workflow Cho AI Vibe Toolkit

```bash
# Tạo thumbnail video
/image "dark background, glowing text 'AI Vibe Toolkit', floating particles, 1920x1080"

# Tạo nhiều variations
/image "same prompt" --count 4 --seed random

# Tạo intro video
/video "logo reveal animation, 3 seconds, dark theme, particle effects"

# Upscale thumbnail
/upscale --input thumbnail.png --scale 4x
```

---

## Điều Kiện Cần

- ComfyUI installed và chạy local (github.com/comfyanonymous/ComfyUI)
- GPU khuyến nghị (NVIDIA) — CPU chạy được nhưng chậm
- Models: tự download hoặc dùng `/model download`

---

*Nguồn: github.com/artokun/comfyui-mcp | 152⭐ | MIT | tháng 6/2026*
