# Poppify — Ảnh → TikTok/Reels/YouTube Shorts ($0.06/reel)

**GitHub:** github.com/Poppify/poppify-claude-plugin
**Website:** poppify.ai | **License:** MIT
**Dùng với:** Claude Code
**Giá:** $0.06/reel (50 free seeds khi signup)

---

## Cài Đặt

```bash
# Claude Code
/plugin marketplace add Poppify/poppify-claude-plugin
/plugin install poppify@poppify
```

Sau install, register để lấy API key + 50 free seeds:
```bash
register({ source: "claude" })
# → trả về apiKey + signupBonusUrl (claim 50 free seeds)
```

---

## Cách Hoạt Động

```
1-10 Photos upload
    ↓
Poppify analyze (mood, color, subject)
    ↓
FFmpeg motion effects (zoom, pan, Ken Burns)
    ↓
Music library matching (mood-based)
    ↓
On-screen text + captions
    ↓  
Optional: AI voiceover
    ↓
15s / 30s / 60s Reel ready
```

---

## Dùng Ngay

```bash
# Basic reel từ ảnh
"Make a reel from these 5 photos for Instagram"

# Với instructions cụ thể
"Tạo TikTok 30 giây từ ảnh screen recording tool này:
 - Style: tech/dark aesthetic
 - Music: upbeat electronic
 - Text overlay: tên tool + 1 key benefit
 - Caption: [tự generate]"

# YouTube Shorts
"Create 60-second YouTube Short từ product demo screenshots:
 - Highlight key features theo thứ tự
 - Add text animation cho mỗi feature
 - Voiceover: casual Vietnamese"

# Batch
"Tạo 7 reels từ folder /week-content/ — 1 reel/ngày cho content calendar"
```

---

## Kết Hợp Workflow

```bash
# Screen record demo tool → Poppify → TikTok

# Step 1: OBS record demo (30 giây)
# Step 2: Screenshot key moments (5-10 ảnh)
# Step 3: Poppify → TikTok/Reels/Shorts

# Với voiceover
# Supertonic TTS → generate voiceover.wav
# Poppify --audio voiceover.wav → reel with voice
```

---

## Chi Phí

| Format | Seeds | Giá |
|--------|-------|-----|
| 15s reel | 1 seed | $0.06 |
| 30s reel | 2 seeds | $0.12 |
| 60s reel | 3 seeds | $0.18 |
| Batch 10 reels | 10-30 seeds | $0.60-1.80 |

**50 free seeds khi signup = ~17-50 reels free**

---
*Nguồn: github.com/Poppify/poppify-claude-plugin | MIT | poppify.ai | tháng 6/2026*
