# HyperFrames (HeyGen) — Viết HTML, AI Render Thành Video

> 200k downloads/tháng. Viết HTML → Claude render thành video MP4. Không cần biết edit video. Built for AI agents. Free, Apache 2.0.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| **Downloads** | 200,000+/tháng |
| **Dùng với** | Claude Code, Cursor, Codex, Gemini CLI |
| **Output** | MP4 video |
| **Free** | ✅ Apache 2.0, không tính phí per-render |
| **Yêu cầu** | Node.js 22+, FFmpeg |

---

## 🎯 Vấn đề nó giải quyết

Mày có script video → cần render thành video thật → phải dùng CapCut, Premiere, After Effects... tốn công edit tay.

**HyperFrames fix:** Claude Code viết HTML → HyperFrames render thành video MP4. AI làm hết từ đầu đến cuối.

**Pipeline mới cho kênh của mày:**
```
Script .md trong kho
    → Claude Code đọc script
    → Viết HTML composition
    → HyperFrames render MP4
    → Video sẵn sàng đăng
```

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Cài dependencies
# Node.js 22+ từ nodejs.org
# FFmpeg từ ffmpeg.org

# Bước 2: Dạy Claude Code framework
npx skills add heygen-com/hyperframes

# Bước 3: Tạo project đầu tiên
npx hyperframes init my-video
cd my-video
npx hyperframes preview   # xem trước trong browser
npx hyperframes render --output final.mp4  # xuất MP4
```

---

## 💡 Dùng với Claude Code thế nào

```bash
# Trong Claude Code, gõ:
/hyperframes Tạo video 60 giây giới thiệu Context7 MCP.
Background tối, text animation, style tech modern.
Dùng script từ file content/script-video-01-context7.md
```

→ Claude đọc script → viết HTML → render thành video

---

## 🎨 Hỗ trợ animation gì

- GSAP animations
- CSS animations  
- Lottie
- Three.js (3D!)
- Anime.js
- Custom shaders và transitions

→ Làm được video đẹp không kém CapCut

---

## 🔗 Liên quan trực tiếp đến kênh

Đây chính là **mảnh ghép còn thiếu** trong pipeline tự động:

```
Kho AI Vibe Toolkit
    → Script video (.md)
    → Claude Code + HyperFrames
    → MP4 tự động
    → Đăng TikTok/YouTube
```

Không cần quay, không cần edit, không cần CapCut.

---

## ⚠️ Lưu ý

- Cần **Claude Code** (terminal) — không phải Claude Desktop
- FFmpeg phải cài trước
- Video phức tạp render lâu hơn
- Đang active development — update liên tục

---

## 🔗 Hay kết hợp với

- **Script videos trong kho** — feed thẳng vào HyperFrames
- **Superpowers** — plan video → HyperFrames execute
- **n8n-claw** — tự động hóa toàn bộ pipeline

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Relevance với kênh | ⭐⭐⭐⭐⭐ |
| Thay thế CapCut | ⭐⭐⭐⭐☆ |
| Wow factor | ⭐⭐⭐⭐⭐ |
| Cần học thêm | ⭐⭐⭐☆☆ |

**Tóm lại:** Đây là **game changer** cho project của mày. Thay vì mày phải dùng ElevenLabs + OBS + CapCut tay — HyperFrames + Claude Code làm hết. Vision "AI tự tạo video" bắt đầu từ đây. 200k downloads/tháng — không phải hype.

---

*Thêm vào kho: 06/2025 | Phát hiện qua: @100day Vibe Coding TikTok | Nguồn: github.com/heygen-com/hyperframes*
