# Image & Video Generation — MCP Guide Dùng Ngay

**Tổng hợp:** comfyui-mcp + fal-mcp
**Cập nhật:** tháng 6/2026

---

## Chọn Tool Nào?

```
Có GPU local + muốn control cao?  → comfyui-mcp
Không có GPU, cần nhanh?          → fal-mcp
Muốn cả hai?                      → fal cho draft, comfyui cho final
```

---

## FAL-MCP — Quick Start (Cloud, No GPU)

```bash
# Cài
git clone https://github.com/enescanguven/fal-mcp && cd fal-mcp
npm install && npm run build
claude mcp add fal-ai -e FAL_KEY=your-key -- node dist/index.js

# Generate ngay
generate_image "product mockup on dark background, studio lighting, 4k" --model flux-pro
generate_video "drone flyover neon city night, cinematic, 5 seconds" --model kling
generate_music "upbeat tech background, 30 seconds"
text_to_speech "Đây là AI Vibe Toolkit" --voice vi-female
```

**Chi phí:** FLUX Schnell $0.003/image | FLUX Pro $0.05/image | Video $0.1-0.5/video

---

## COMFYUI-MCP — Full Control (Local)

```bash
# Cài plugin
/plugin marketplace add artokun/comfyui-mcp

# Dùng ngay
/image "cinematic robot portrait, neon lighting, 8k" --model flux-dev
/video "logo reveal, particle effects, 3 seconds" --model wan
/upscale --input photo.jpg --scale 4x
/workflow list        # xem workflows
/model download flux-dev  # download models
```

---

## Prompt Templates — Copy Paste Dùng Ngay

### Thumbnails YouTube/TikTok
```
"Dark background, glowing [TEXT] title, particle effects floating,
 cinematic lighting, high contrast, 1920x1080, ultra detailed"

"Split screen comparison: [LEFT SIDE] vs [RIGHT SIDE],
 bold typography, neon accent colors, dark theme"
```

### Product Mockups
```
"Minimal product mockup, [PRODUCT] on white surface,
 soft shadow, studio lighting, clean background, professional"
```

### Profile/Avatar
```
"Professional headshot of [DESCRIPTION], neutral background,
 soft lighting, business attire, high resolution"
```

### Social Media Posts
```
"Infographic about [TOPIC], modern design, icons, 
 data visualization, clean layout, [COLOR SCHEME], 1080x1080"
```

### Background Removal → Transparent
```
edit_image --input product.jpg "remove background, transparent PNG"
```

---

## Video Generation Prompts

```bash
# Intro video
"[LOGO] appearing from particles, epic reveal, dark background, 
 golden particles, 3 seconds, cinematic"

# Product demo
"Screen recording of [APP], smooth scrolling, click highlights, 
 professional demo style, 30 seconds"

# Transitions
"Light leak transition effect, warm tones, 1 second, seamless loop"
```

---

## Workflow: Thumbnail → Upscale → Ready

```bash
# Step 1: Generate thumbnail draft
generate_image "thumbnail concept" --model flux-schnell  # nhanh + rẻ

# Step 2: Review → pick best

# Step 3: Upscale best pick
edit_image --input best.png "upscale 4x, enhance sharpness"

# Step 4: Final với full quality
generate_image "same prompt refined" --model flux-pro  # quality cao nhất
```

---
*skills/image-video-gen-mcp-guide.md | AI Vibe Toolkit | tháng 6/2026*
