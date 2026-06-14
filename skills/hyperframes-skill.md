# HyperFrames (HeyGen) — HTML → Video MP4 (200k downloads/tháng)

**Repo:** github.com/heygen-com/hyperframes | Apache 2.0 | HeyGen
**Downloads:** 200k/tháng | Built for AI agents

---

## Cài Nhanh

```bash
npm install -g @heygen/hyperframes
# hoặc
npx @heygen/hyperframes
```

## Workflow Cơ Bản

```bash
# 1. Viết HTML animation
cat > slide.html << 'EOF'
<html>
<body style="background:#0a0a0a; display:flex; align-items:center; justify-content:center;">
  <h1 style="color:white; font-size:72px; animation:fadeIn 1s ease-in">
    AI Vibe Toolkit
  </h1>
</body>
</html>
EOF

# 2. Render thành video
hyperframes render slide.html --output slide.mp4 --duration 3

# 3. Multiple slides → full video
hyperframes compile slides/ --output final.mp4
```

## Trong Claude Code

```bash
# Claude Code + HyperFrames = video generation pipeline
/hyperframes "tạo 5 slides cho video TikTok về hermes agent:
slide 1: hook question
slide 2: problem
slide 3: solution  
slide 4: demo
slide 5: CTA"
```

## Khác Biệt Với html-video

| | HyperFrames | html-video |
|--|-------------|-----------|
| Tổ chức | Multi-slide | Single HTML |
| Transitions | Built-in | Manual CSS |
| HeyGen integration | ✅ | ❌ |
| Community | Lớn hơn | Nhỏ hơn |
| Best for | Slide-based | Custom animation |

## Tips

- Dùng CSS `@keyframes` cho smooth animations
- `--fps 60` cho video mượt
- `--width 1080 --height 1920` cho TikTok/Reels vertical
- Batch compile nhiều slides → 1 video hoàn chỉnh

---
*skills/hyperframes-skill.md | AI Vibe Toolkit | tháng 6/2026*
