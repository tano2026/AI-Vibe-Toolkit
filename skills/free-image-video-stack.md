# Free Image & Video Stack — $0 Hoàn Toàn

**Tổng hợp:** Pollinations MCP + CogVideoX + WanGP Kaggle + framecraft + SD WebUI + Supertonic
**Cập nhật:** tháng 6/2026

---

## Decision Tree — Chọn Tool Nào?

```
CẦN ẢNH:
├── Không có GPU → Pollinations MCP (free, no key, 20+ models)
├── Có GPU → Stable Diffusion WebUI local (full control, $0)
└── Cần text-in-image → Pollinations gpt-image-1 hoặc ideogram

CẦN VIDEO:
├── Nhanh, đơn giản → CogVideoX free (unlimited, 6s)
├── Chất lượng cao, miễn phí → WanGP trên Kaggle (30h/tuần T4)
├── Animated từ HTML → framecraft hoặc html-video ($0)
└── Ảnh → video ngắn → CogVideoX image-to-video

CẦN VOICEOVER:
└── Supertonic TTS local (31 ngôn ngữ, $0)

CẦN EDIT/MERGE:
└── FFmpeg CLI (free, powerful)
```

---

## Stack Đầy Đủ $0

```
Image:      Pollinations MCP (cloud) / SD WebUI (local GPU)
Video:      CogVideoX free / WanGP Kaggle / framecraft
Voiceover:  Supertonic TTS
Music:      CogVideoX music / Udio free tier
Edit:       FFmpeg
Thumbnail:  Pollinations → html-anything render
```

---

## Quick Commands

### Image Generation (Pollinations — FREE)
```bash
# Thumbnail YouTube
"Generate image: [hook text] bold on dark background,
 neon glow effect, particles floating, 1920x1080"

# TikTok cover
"Generate image: vertical 1080x1920, [topic] centered,
 gradient overlay, clean typography"

# Product mockup
"Generate image: laptop mockup showing [tool] interface,
 dark desk, professional"

# Logo
"Generate image: minimal logo for [channel name],
 geometric, white on black, scalable"
```

### Video Generation (CogVideoX — FREE UNLIMITED)
```bash
# B-roll footage
"Generate video: coding montage, dark monitor, typing hands,
 neon keyboard, 6 seconds" --provider cogvideox

# Intro
"Generate video: logo particle reveal, dark background,
 golden particles assembling into logo, 6 seconds"

# Transition
"Generate video: light leak effect, cinematic, 2 seconds"
```

### Video Generation (WanGP Kaggle — FREE 30h/tuần)
```bash
# Kaggle → WanGP → generate
# Quality cao hơn CogVideoX đáng kể
"Text to video 1080P: [detailed scene description], 10 seconds"
"Image to video: [product image] with subtle animation"
```

### Voiceover (Supertonic — FREE LOCAL)
```bash
supertonic --text "Xin chào! Video hôm nay về [topic]"   --lang vi --out voiceover.wav

# Nhiều giọng
supertonic --list-speakers  # xem giọng có sẵn
supertonic --speaker vi-female-2 --text "..." --out vo.wav
```

### Merge Final Video (FFmpeg — FREE)
```bash
# Video + voiceover
ffmpeg -i b_roll.mp4 -i voiceover.wav   -c:v copy -c:a aac   -shortest final.mp4

# Thêm background music
ffmpeg -i final.mp4 -i bgmusic.mp3   -filter_complex "[1:a]volume=0.2[bg];[0:a][bg]amix"   output.mp4

# Resize cho TikTok
ffmpeg -i horizontal.mp4   -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2"   tiktok.mp4
```

---

## Workflow Hoàn Chỉnh 1 Video TikTok ($0)

```bash
# 1. Script (5 phút)
# content-creator.md skill + viral-hooks

# 2. Voiceover (2 phút)  
supertonic --text "script.txt" --lang vi --out voice.wav

# 3. B-roll video (3 phút)
# Mô tả → CogVideoX → video.mp4 (6s, free)

# 4. Thumbnail/Cover (2 phút)
# Pollinations MCP → thumbnail.png (free)

# 5. Merge (2 phút)
ffmpeg -i video.mp4 -i voice.wav -shortest final.mp4

# 6. Post
# Upload TikTok manually hoặc Buffer MCP

Tổng: ~15 phút, $0
```

---

## Limit Thực Tế Của Free Tools

| Tool | Limit | Workaround |
|------|-------|-----------|
| Pollinations image | No limit | - |
| CogVideoX | Unlimited | Max 6s/video |
| WanGP Kaggle | 30h/tuần | Batch generate Thứ 2 |
| Supertonic | No limit | - |
| SD WebUI | No limit | Cần GPU |
| FFmpeg | No limit | - |

---

*AI Vibe Toolkit | Free Image & Video Stack | tháng 6/2026*
