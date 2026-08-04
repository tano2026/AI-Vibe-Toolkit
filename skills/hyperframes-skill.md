# HyperFrames — Viết HTML Prompt, AI Render Thành Video MP4

> *Skill này dạy Claude Code tạo video hoàn chỉnh từ HTML — không cần CapCut, không cần edit tay*

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Loại** | Claude Skill / CLI Tool |
| **Repo** | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| **Dùng với** | Claude Code, Cursor, Codex, Gemini CLI |
| **Downloads** | 200,000+/tháng |
| **License** | Apache 2.0 — Free hoàn toàn |
| **Yêu cầu** | Node.js 22+, FFmpeg |
| **Output** | MP4 video |

---

## 🎯 Skill này làm được gì

Thay vì dùng CapCut, Premiere hay After Effects — mày describe video bằng ngôn ngữ thường, Claude Code viết HTML composition, HyperFrames render ra MP4.

**Pipeline tự động cho kênh:**
```
Script .md trong kho
    → Claude Code đọc script
    → Viết HTML composition (multi-slide)
    → HyperFrames render MP4
    → Video sẵn sàng đăng
```

Hỗ trợ: GSAP, CSS animations, Lottie, Three.js (3D), Anime.js, custom shaders và transitions.

---

## 📋 Cách dùng

### Bước 0: Cài đặt

```bash
# Cài HyperFrames
npx skills add heygen-com/hyperframes

# Cài FFmpeg (cần thiết để render)
# macOS:
brew install ffmpeg
# Ubuntu/Debian:
sudo apt install ffmpeg
```

### Option 1: Dùng trực tiếp trong Claude Code

Copy đoạn prompt bên dưới, paste vào Claude Code:

```
/hyperframes [MÔ TẢ VIDEO CỦA MÀY]

Yêu cầu:
- Thời lượng: [X] giây
- Platform: [TikTok/YouTube/LinkedIn]
- Style: [tech dark / clean light / vibrant]
- Nội dung: [tóm tắt từng phần]
- Nguồn script: [đường dẫn file .md nếu có]
```

### Option 2: CLI trực tiếp

```bash
# Init project mới
npx hyperframes init my-video
cd my-video

# Preview trong browser
npx hyperframes preview

# Render ra MP4
npx hyperframes render --output final.mp4

# Custom resolution
npx hyperframes render --output tiktok.mp4 \
  --width 1080 --height 1920 \
  --fps 60 \
  --duration 60
```

### Prompt Templates

```bash
# Template 1: Video giới thiệu tool AI
/hyperframes "Tạo video 60 giây giới thiệu [TÊN TOOL].
Background tối (#0a0a0a), text animation trắng/xanh neon.
Cấu trúc: hook 3s → problem 8s → solution 35s → CTA 14s.
Dùng script từ content/script-video-XX-[tên].md"

# Template 2: TikTok Hook nhanh
/hyperframes "Tạo video TikTok 15 giây.
Vertical 1080x1920. Hook text đập vào mặt trong 2 giây đầu.
Chữ lớn, animation nhanh, nền tối, màu accent: [MÀU]."

# Template 3: Tutorial step-by-step
/hyperframes "Tạo video tutorial [X BƯỚC] cho [CHỦ ĐỀ].
Mỗi bước 1 slide riêng với icon + text. Clean white background.
Thời lượng tổng: [Y] giây. Export 1920x1080."

# Template 4: Data visualization
/hyperframes "Tạo video so sánh [A] vs [B].
Bảng so sánh animate từng dòng xuất hiện. Background tối.
Highlight phần [A] chiếm ưu thế bằng màu xanh lá."
```

---

## 💡 Ví dụ thực tế

**Input:**
```
/hyperframes "Tạo video 60 giây giới thiệu Context7 MCP.
Background tối, text animation, style tech modern.
Dùng script từ file content/script-video-01-context7.md"
```

**Output Claude trả về:**

```html
<!-- slide-01-hook.html -->
<html>
<head>
  <style>
    body { background: #0a0a0a; display: flex; align-items: center;
           justify-content: center; margin: 0; height: 100vh; }
    h1 { color: white; font-size: 72px; font-family: monospace;
         animation: fadeIn 0.5s ease-in; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); }
                        to   { opacity: 1; transform: translateY(0); } }
  </style>
</head>
<body>
  <h1>Context7 thay đổi cách mày dùng AI</h1>
</body>
</html>
```

Sau đó chạy:
```bash
npx hyperframes compile slides/ --output context7-video.mp4
# → context7-video.mp4 sẵn sàng đăng
```

**Kết quả:** Video MP4 60 giây, không cần mở CapCut một lần.

---

## 🔧 Tùy chỉnh

Mày có thể thay đổi các phần trong prompt template:

- `[TÊN TOOL]` → tên tool muốn giới thiệu (Context7, HyperFrames, n8n-claw...)
- `[X BƯỚC]` / `[CHỦ ĐỀ]` → số bước và chủ đề tutorial
- `[A] vs [B]` → hai thứ muốn so sánh
- `[MÀU]` → hex color cho accent (#00ff88, #7c3aed, #f59e0b...)
- Platform:
  - TikTok/Reels: `--width 1080 --height 1920`
  - YouTube/LinkedIn: `--width 1920 --height 1080`
  - YouTube Shorts: `--width 1080 --height 1920`
- FPS: `--fps 30` (tiêu chuẩn) hoặc `--fps 60` (mượt hơn, file nặng hơn)

---

## ⚖️ So Sánh Với Các Tool Tương Tự

| | HyperFrames | html-video | Remotion |
|--|-------------|-----------|---------|
| Cần biết React? | ❌ | ❌ | ✅ |
| Multi-slide | ✅ Built-in | ❌ Manual | ✅ |
| Transitions | ✅ Built-in | ❌ Manual CSS | ✅ |
| HeyGen integration | ✅ | ❌ | ❌ |
| Downloads/tháng | 200k | Nhỏ hơn | 900k |
| Best for | Slide-based AI video | Custom animation | Data-driven React |

---

## 📊 Đánh giá

| Tiêu chí | Điểm |
|----------|------|
| Tiết kiệm thời gian | ⭐⭐⭐⭐⭐ |
| Dễ dùng với Claude Code | ⭐⭐⭐⭐⭐ |
| Thay thế CapCut | ⭐⭐⭐⭐☆ |
| Relevance kênh mày | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Game changer cho pipeline video của kênh. Kết hợp với scripts trong `/content/` → video tự động không cần đụng tay.

---

## 🔗 Hay kết hợp với

- **Scripts trong `/content/`** — feed thẳng vào HyperFrames
- **html-video-skill.md** — dùng html-video cho single-slide animation phức tạp
- **remotion-skill.md** — khi cần React component + data-driven video
- **n8n-claw-skill.md** — tự động hóa toàn bộ pipeline

---

*skills/hyperframes-skill.md | AI Vibe Toolkit | tháng 8/2026*
