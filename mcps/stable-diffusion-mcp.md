# stable-diffusion-mcp — Image AI Local, $0 Mãi Mãi (GPU Cần Thiết)

**GitHub:** https://github.com/Ichigo3766/image-gen-mcp
**Stars:** 39⭐ | **License:** MIT
**Requires:** Stable Diffusion WebUI (AUTOMATIC1111 hoặc ForgeUI) đang chạy local

---

## Đây Là Gì

MCP server kết nối Claude với **Stable Diffusion WebUI local** — generate images $0 mãi mãi sau khi setup.

---

## Cần Có Trước

```bash
# Cài AUTOMATIC1111 Stable Diffusion WebUI
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui

# Chạy với API enabled
./webui.sh --api  # macOS/Linux
webui-user.bat --api  # Windows
# → http://127.0.0.1:7860
```

---

## Cài MCP

```bash
git clone https://github.com/Ichigo3766/image-gen-mcp
cd image-gen-mcp
npm install && npm run build
```

```json
{
  "mcpServers": {
    "stable-diffusion": {
      "command": "node",
      "args": ["/path/to/image-gen-mcp/build/index.js"],
      "env": {
        "SD_API_URL": "http://127.0.0.1:7860"
      }
    }
  }
}
```

---

## Dùng Ngay

```bash
# Basic
"Generate image: photorealistic portrait, studio lighting, 512x512"

# Advanced params
"Generate image: anime girl, fantasy background
 --model animagine-xl
 --steps 30
 --cfg 7
 --width 768 --height 1024"

# Img2img
"Take this rough sketch and render it as photorealistic"

# Inpainting
"Remove the background from this image"
```

---

## Models Hay Nhất Để Download

```bash
# Photorealistic
# → civitai.com/models/4201 (Realistic Vision V6)

# Anime/Illustration
# → civitai.com/models/81458 (AnimagineXL 3.1)

# FLUX (chất lượng cao nhất hiện tại)
# → huggingface.co/black-forest-labs/FLUX.1-dev
# (Cần 24GB+ VRAM)

# SDXL (balance quality/speed)
# → huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
```

---

## Khi Nào Dùng SD Local vs Pollinations

| | SD Local | Pollinations |
|--|----------|-------------|
| Chi phí | $0 (điện) | $0 |
| GPU cần | ✅ 6GB+ VRAM | ❌ Cloud |
| Privacy | ✅ Local | Cloud |
| Control | ✅ Full | Limited |
| Speed | Phụ thuộc GPU | Medium |
| Models | Hàng nghìn Civitai | 20 fixed |

**Rule:** Có GPU → SD Local (control tối đa, $0).
Không có GPU → Pollinations (cloud free, nhanh).

---

*Nguồn: github.com/Ichigo3766/image-gen-mcp | 39⭐ | MIT | tháng 6/2026*
