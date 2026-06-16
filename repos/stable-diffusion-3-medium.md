# Stable Diffusion 3 Medium — Image AI Free, Commercial OK (Stability AI)

**HuggingFace:** https://huggingface.co/stabilityai/stable-diffusion-3-medium
**Release:** 12/6/2026 | **By:** Stability AI | **License:** Free for all use
**Parameters:** 2B | Quality: Professional-grade

---

## Đây Là Gì

Stability AI release SD3 Medium hoàn toàn miễn phí — model tạo ảnh chất lượng cao, dùng được cho personal và commercial.

---

## Cài & Dùng

### Python (cần GPU 8GB+)

```python
from diffusers import StableDiffusion3Pipeline
import torch

pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers",
    torch_dtype=torch.float16
).to("cuda")

image = pipe(
    "dark cinematic thumbnail, glowing text AI Vibe Toolkit, neon particles",
    num_inference_steps=28,
    guidance_scale=7.0,
).images[0]
image.save("thumbnail.png")
```

### Không Có GPU — Dùng Pollinations MCP (Free)

```bash
# Đã có trong kho: mcps/pollinations-mcp.md
"Generate image using sd3: [prompt]"
```

---

## SD3 vs Trước

| | SD1.5 | SDXL | SD3 Medium |
|--|-------|------|-----------|
| Text trong ảnh | Poor | OK | Good |
| Quality | Good | Better | Best |
| VRAM | 4GB | 8GB | 8GB |
| Free | Yes | Yes | Yes |

---

## Prompts Cho Thumbnails

```
Dark background, bold text [TITLE], neon blue accent,
floating particles, dramatic lighting, 4k

Vertical 9:16, dark gradient, centered text [TEXT],
minimal design, neon glow, professional
```

---

## Kết Hợp Stack

SD3 Medium + pollinations-mcp + comfyui-mcp + fal-mcp
= Full image generation stack, $0

**Rating: 9/10** — Best free image model. Text rendering cuối cùng readable.

*huggingface.co/stabilityai/stable-diffusion-3-medium | Free | tháng 6/2026*
