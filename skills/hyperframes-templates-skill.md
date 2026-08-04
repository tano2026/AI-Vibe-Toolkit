# HyperFrames Templates — Copy-Paste HTML Blocks cho Video

> *Skill này giúp mày chọn đúng template từ kho 19 blocks và customize nhanh*

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Loại** | Prompt Template / Workflow Guide |
| **Repo** | [reactvideoeditor/hyperframes-templates](https://github.com/reactvideoeditor/hyperframes-templates) |
| **Dùng với** | Claude Code, HyperFrames CLI |
| **License** | MIT — free commercial |
| **Yêu cầu** | HyperFrames đã setup (Node.js 22+ + FFmpeg) |

---

## 🎯 Skill này làm được gì

Thay vì viết HTML animation từ đầu — dùng 19 templates có sẵn, chỉ cần sửa text/màu/số rồi render. Mỗi template có CSS variables để tùy chỉnh mà không cần đụng code.

---

## 📋 Cách dùng

### Bước 1: Clone kho templates

```bash
git clone https://github.com/reactvideoeditor/hyperframes-templates
cd hyperframes-templates
```

### Bước 2: Chọn template phù hợp

| Mày cần làm gì | Dùng template |
|----------------|---------------|
| Mở đầu video với text đẹp | `aurora-headline.html` hoặc `kinetic-title.html` |
| Hiện số liệu / stats | `stat-counter.html`, `metric-grid.html`, `liquid-counter.html` |
| So sánh 2 thứ | `bar-chart.html`, `ranked-bars.html`, `dual-area.html` |
| Logo / brand reveal | `particle-wordmark.html` |
| Tên người / chức vụ | `lower-third.html`, `prism-lower-third.html` |
| CTA follow TikTok | `follow-pill.html` |
| Review / testimonial | `spotlight-testimonial.html` |
| Thông báo / alert UI | `notification-stack.html` |
| Chuyển cảnh | `fade-through-white.html`, `light-leak-wipe.html` |

### Bước 3: Customize bằng CSS variables

Mỗi template có phần `:root` hoặc `<script>` config ở đầu file:

```css
/* Ví dụ aurora-headline.html */
:root {
  --dur: 6s;        /* thời lượng 1 loop */
  --a: #6fe4ff;     /* màu accent 1 */
  --b: #9d7bff;     /* màu accent 2 */
  --ink: #eef3fb;   /* màu chữ */
  --bg: #060810;    /* màu nền */
}
```

Sửa text trong HTML:
```html
<!-- aurora-headline.html — tìm phần này -->
<span class="kicker">HyperFrames</span>   ← đổi thành tagline của mày
<span class="word">Write</span>           ← đổi text chính
```

### Bước 4: Preview và render

```bash
# Preview trong browser
open templates/aurora-headline.html

# Render MP4 YouTube (1920x1080)
npx hyperframes render templates/aurora-headline.html \
  --out intro.mp4 --width 1920 --height 1080 --fps 60

# Render TikTok vertical (1080x1920)
npx hyperframes render templates/follow-pill.html \
  --out cta.mp4 --width 1080 --height 1920 --fps 60
```

---

## 💡 Prompt Templates — Dùng với Claude Code

### Option 1: Customize template có sẵn

```
/task Customize template `templates/aurora-headline.html` từ repo
reactvideoeditor/hyperframes-templates cho video giới thiệu [TÊN TOOL]:
- Kicker text: "[TAGLINE NGẮN]"
- Main text: "[CHỮ CHÍNH DÒNG 1]" + "[CHỮ CHÍNH DÒNG 2]"  
- Màu accent: [MÀU HEX 1] và [MÀU HEX 2]
- Duration: [X] giây
Sau đó render: npx hyperframes render --out [tên].mp4 --width 1080 --height 1920
```

### Option 2: Build video hoàn chỉnh từ nhiều templates

```
/task Tạo video 60 giây cho TikTok từ script content/script-video-[XX]-[tên].md.
Dùng templates từ ~/hyperframes-templates:
- Slide 1 (0-3s): kinetic-title.html — hook text
- Slide 2 (3-12s): aurora-headline.html — vấn đề
- Slide 3 (12-50s): [custom HTML] — demo/solution
- Slide 4 (50-57s): stat-counter.html — social proof số liệu
- Slide 5 (57-60s): follow-pill.html — CTA
Render từng slide → compile thành 1 video 1080x1920
```

### Option 3: Data visualization nhanh

```
/task Dùng template `templates/ranked-bars.html`.
Thay data bằng:
- [ITEM 1]: [GIÁ TRỊ 1]
- [ITEM 2]: [GIÁ TRỊ 2]
- [ITEM 3]: [GIÁ TRỊ 3]
Màu bars: gradient từ [MÀU A] → [MÀU B].
Render 1920x1080, 8 giây.
```

---

## 💡 Ví dụ thực tế

**Input:**
```
Customize kinetic-title.html cho video giới thiệu Context7 MCP.
Text: "Context7" + "No more hallucination."
Màu: xanh lam #60a5fa.
Render TikTok.
```

**Output (Claude Code sửa CSS variables):**
```css
.title {
  background: linear-gradient(90deg, #60a5fa, #38bdf8, #60a5fa);
}
```
```html
<h1 class="title">Context7<br>No more hallucination.</h1>
```
```bash
npx hyperframes render kinetic-title.html \
  --out context7-hook.mp4 --width 1080 --height 1920 --fps 60
```

---

## 🔧 Tùy chỉnh

- `[TÊN TOOL]` → tên tool đang làm video
- `[MÀU HEX]` → brand color của tool (lấy từ logo/website của họ)
- `[GIÁ TRỊ]` → số liệu thực tế (stars, downloads, users...)
- Duration: mặc định loop trong browser, HyperFrames tự xử lý theo frame clock
- Kết hợp nhiều templates: mỗi cái là 1 slide, compile lại bằng `hyperframes compile`

---

## 📊 Đánh giá

| Tiêu chí | Điểm |
|----------|------|
| Tiết kiệm thời gian | ⭐⭐⭐⭐⭐ |
| Dễ customize | ⭐⭐⭐⭐⭐ |
| Chất lượng visual | ⭐⭐⭐⭐⭐ |
| Dùng ngay không cần code | ⭐⭐⭐⭐☆ |

---

## 🔗 Hay kết hợp với

- **hyperframes-skill.md** — setup HyperFrames + workflow cơ bản
- **Scripts trong `/content/`** — đọc script → chọn template phù hợp từng phần
- **html-video-skill.md** — khi cần animation phức tạp hơn ngoài 19 blocks này
- **remotion-skill.md** — khi cần React + data-driven video

---

*skills/hyperframes-templates-skill.md | AI Vibe Toolkit | tháng 8/2026*
