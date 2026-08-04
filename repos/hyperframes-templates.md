# HyperFrames Templates — 19 HTML Video Blocks Copy-Paste Sẵn

> *19 HTML templates free, render ra MP4 bằng HyperFrames — không cần build step, không cần framework*

---

## 📌 Thông tin

| | |
|--|--|
| **GitHub** | [reactvideoeditor/hyperframes-templates](https://github.com/reactvideoeditor/hyperframes-templates) |
| **Stars** | ⭐ mới (07/2026) |
| **Ngôn ngữ** | HTML / CSS / Vanilla JS |
| **License** | MIT — dùng thoải mái, kể cả thương mại |
| **Cập nhật gần nhất** | 07/2026 |
| **Live demo** | [reactvideoeditor.com/hyperframes-templates](https://www.reactvideoeditor.com/hyperframes-templates) |

---

## 🎯 Dùng để làm gì

Kho chứa 19 HTML blocks sẵn sàng render thành video MP4 qua HyperFrames. Mỗi file là 1 HTML hoàn chỉnh — không cần cài thêm gì ngoài HyperFrames.

**Dùng cho pipeline video kênh của mày:**
```
Chọn template từ kho này
    → Sửa text/màu/số trong :root CSS variables
    → npx hyperframes render template.html --out output.mp4
    → Ghép vào video chính
```

---

## 📂 Danh sách 19 Templates

### 📊 Data (9 templates)
| Template | File | Dùng cho |
|----------|------|----------|
| Activity Rings | `activity-rings.html` | Visualize % progress kiểu Apple Watch |
| Animated Bar Chart | `bar-chart.html` | Bar chart từ 0 lên, stagger theo thứ tự |
| Dual Area Chart | `dual-area.html` | So sánh 2 series data, glowing dot |
| Liquid Counter | `liquid-counter.html` | Số đếm lên với liquid fill effect |
| Metric Grid | `metric-grid.html` | 3 KPI tiles đếm lên + sparklines |
| Radial Gauge | `radial-gauge.html` | Donut gauge quét tới giá trị target |
| Ranked Bars | `ranked-bars.html` | Horizontal ranking bars + số đếm |
| Signal Line | `signal-line.html` | Area chart vẽ dần với gradient fill |
| Stat Counter | `stat-counter.html` | Số to đếm lên tới target |

### ✏️ Text (3 templates)
| Template | File | Dùng cho |
|----------|------|----------|
| Aurora Headline | `aurora-headline.html` | Hero text đẹp với aurora background |
| Kinetic Title | `kinetic-title.html` | Gradient title fade-up, dùng mở đầu video |
| Particle Wordmark | `particle-wordmark.html` | Particles bay vào lắp thành chữ/logo |

### 🎬 Overlay (2 templates)
| Template | File | Dùng cho |
|----------|------|----------|
| Lower Third | `lower-third.html` | Banner tên/chức vụ trượt từ cạnh vào |
| Prism Lower Third | `prism-lower-third.html` | Glass name badge nghiêng vào với light bar |

### 📱 Social (3 templates)
| Template | File | Dùng cho |
|----------|------|----------|
| Follow Pill | `follow-pill.html` | "Follow" button TikTok-style pop in |
| Notification Stack | `notification-stack.html` | Glass notifications xếp chồng spring in |
| Spotlight Testimonial | `spotlight-testimonial.html` | Glass review card + spotlight + stars |

### 🔀 Transitions (2 templates)
| Template | File | Dùng cho |
|----------|------|----------|
| Fade Through White | `fade-through-white.html` | Flash trắng chuyển cảnh |
| Light Leak Wipe | `light-leak-wipe.html` | Light leak sweep giữa 2 cảnh (có RGB split) |

---

## 🚀 Bắt đầu nhanh

```bash
# Clone về
git clone https://github.com/reactvideoeditor/hyperframes-templates
cd hyperframes-templates

# Preview template trong browser (mở file thẳng)
open templates/kinetic-title.html

# Render ra MP4
npx hyperframes render templates/kinetic-title.html --out output.mp4

# Render TikTok vertical
npx hyperframes render templates/aurora-headline.html --out hook.mp4 \
  --width 1080 --height 1920 --fps 60
```

---

## 💡 Tại sao repo này hay

- **Copy-paste hoàn toàn** — mỗi file là HTML độc lập, không phụ thuộc file khác
- **Tunable bằng CSS variables** — sửa màu/text/timing trong `:root` là xong
- **Render deterministic** — HyperFrames render ra frame-perfect, không random
- **MIT license** — dùng thoải mái trong video thương mại kênh YouTube/TikTok

---

## ⚠️ Cần biết trước

- Cần **HyperFrames** (Node.js 22+ + FFmpeg) để render ra MP4
- Templates dùng `animation: infinite` để preview trong browser — khi render thật HyperFrames tự xử lý theo frame clock, không bị loop
- Xem live demo trước tại `reactvideoeditor.com/hyperframes-templates` trước khi chọn

---

## 🔗 Tài nguyên liên quan

- [Live demo tất cả templates](https://www.reactvideoeditor.com/hyperframes-templates)
- [HyperFrames (HeyGen)](https://github.com/heygen-com/hyperframes) — tool render HTML → MP4
- [skills/hyperframes-templates-skill.md](../skills/hyperframes-templates-skill.md) — cách dùng với Claude Code
- [skills/hyperframes-skill.md](../skills/hyperframes-skill.md) — HyperFrames workflow đầy đủ

---

*Phát hiện bởi: tano2026 | Ngày thêm vào kho: 08/2026*
