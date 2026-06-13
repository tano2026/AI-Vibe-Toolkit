# Remotion — Tạo Video Bằng React, Render Ra MP4 Thật

**GitHub:** https://github.com/remotion-dev/remotion
**Stars:** 49.9k | **Forks:** 3.6k | **License:** Remotion License*
**Tác giả:** Jonny Burger (Swiss developer, full-time từ 2021)
**Website:** remotion.dev | **npm:** 900k installs/tháng

*Source-available. Free cho cá nhân. Công ty 4+ người cần mua commercial license.*

---

## Concept

Thay vì kéo timeline trong Premiere — mày viết React components để mô tả video. Remotion biết frame nào đang hiển thị, render từng frame thành ảnh, ghép thành MP4 thật.

```jsx
// Video là React component
export const MyVideo = () => {
  const frame = useCurrentFrame(); // frame hiện tại
  const opacity = interpolate(frame, [0, 30], [0, 1]); // fade in 1 giây

  return (
    <div style={{ opacity, fontSize: 80, color: 'white' }}>
      Hello from frame {frame}
    </div>
  );
};
```

Mày có thể dùng: CSS, SVG, WebGL, Canvas, Three.js, Lottie — bất cứ thứ gì chạy trong browser.

---

## Tại Sao 49.9k Stars?

**Data-driven videos at scale:** GitHub Unwrapped — video năm tóm tắt activity của mỗi user GitHub — được build bằng Remotion. Hàng triệu video unique, cùng 1 codebase.

**Developer workflow:** Video trong Git, có version control, review được, CI/CD được. Không có "tôi không biết file nào là bản cuối" nữa.

**AI agent friendly:** Prompt → agent viết React component → Remotion render → MP4. Không cần biết Premiere.

```bash
npx create-video@latest
npx skills add remotion-dev/skills  # 30+ skill modules
# Bắt đầu prompt trong terminal
```

---

## AI-Powered Workflow

```bash
# Cài skills
npx skills add remotion-dev/skills

# Prompt với Claude Code / Codex
"Tạo video 30 giây giải thích Decision Tree với animated diagram"
→ Agent viết React components
→ Remotion render ra MP4
```

**30+ skill modules** cho agent: animations, audio sync, 3D, charts, transitions, captions, text effects... Agent biết dùng đúng skill cho đúng task.

---

## Render Options

**Local (free):**
```bash
npx remotion render src/index.ts MyVideo output.mp4
```

**Lambda (serverless, trả tiền per-render):**
```bash
# Render 1000 videos song song trên AWS Lambda
npx remotion lambda render
```

**Server-side rendering:** Deploy lên VPS, render theo request.

---

## Templates Nổi Bật

- **GitHub Unwrapped style** — year in review với data visualization
- **Fireship style** — fast-paced developer tutorial format
- **Data visualization** — animated charts, graphs
- **Social media** — Instagram Reels, TikTok format
- **Podcast** — audio waveform + transcript

---

## License — Đọc Kỹ

- **Cá nhân / side project / freelancer:** Free
- **Startup / công ty < 3 người:** Free
- **Công ty 4+ người:** Cần mua commercial license ($$$)
- **Students / non-profit:** Free

Source code public trên GitHub nhưng không phải MIT/Apache.

---

## Đánh Giá Cá Nhân

49.9k stars là xứng đáng — Remotion giải quyết đúng vấn đề mà không tool nào giải quyết tốt hơn: tạo video programmatic với developer workflow.

Với content creator: curve khá dốc nếu không biết React. html-video (nexu-io) hoặc html-anything dễ hơn nhiều cho người không code.

Với developer: đây là best-in-class. Version control cho video, data-driven generation, AI agent workflow đầy đủ.

**Rating: 9/10** cho developers. **6/10** cho non-coders.

---

*Nguồn: github.com/remotion-dev/remotion | Cập nhật: tháng 6/2026*
