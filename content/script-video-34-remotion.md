# Script Video #34 — Remotion: Viết React, Nhận Video MP4

**Format:** TikTok / YouTube Shorts (~80s)
**Hook type:** "GitHub Unwrapped — bạn đã xem chưa?"
**Style:** Không lộ mặt, code demo + video output

---

## 🎬 SCRIPT

**[0s - 8s] HOOK**
> "GitHub Unwrapped — cái video tóm tắt activity GitHub của mày cuối năm đó — được tạo ra bằng React. Hàng triệu video unique, 1 codebase. Framework đó là Remotion và giờ có 49.9k stars."

*[Show: GitHub Unwrapped video example]*

**[8s - 25s] CONCEPT**
> "Remotion cho phép mày viết video bằng React component. Thay vì kéo timeline trong Premiere, mày viết code."

```jsx
export const MyVideo = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1]);
  return <div style={{ opacity }}>Hello!</div>;
};
```

> "Mày có thể dùng CSS, SVG, WebGL, Three.js — bất cứ thứ gì chạy trong browser. Remotion render từng frame thành ảnh, ghép thành MP4 thật."

**[25s - 50s] AI AGENT WORKFLOW**
> "Phần hay nhất: kết hợp với AI agent."

```bash
npx create-video@latest
npx skills add remotion-dev/skills
# 30+ skill modules: animations, audio, 3D, charts, captions...
```

> "Prompt với Claude Code:"
> "'Tạo video 30 giây giải thích Decision Tree với animated diagram'"
> "Agent viết React component → Remotion render → MP4."

*[Show: agent code → render progress → MP4 output]*

> "900k npm installs mỗi tháng. Developer community lớn. Data-driven video at scale."

**[50s - 65s] ĐIỂM TRỪ THẲNG THẮN**
> "License không phải MIT — công ty 4+ người cần mua commercial license. Đọc kỹ trước khi dùng production."

> "Và cần biết React. Nếu không code — html-video của nexu-io dễ hơn nhiều."

**[65s - 80s] CTA**
> "49.9k stars không phải ngẫu nhiên. Đây là best-in-class cho developer muốn tạo video programmatic. Link trong bio."

---

## 📝 CAPTION
```
GitHub Unwrapped — hàng triệu video unique, 1 codebase React 🎥

Remotion: viết video bằng React component → render MP4 thật

49.9k ⭐ · AI agent workflow · 900k npm installs/tháng

⚠️ Cần biết React | Công ty 4+ người cần commercial license

#remotion #react #vibecoding #video #mp4 #developer #ai
```

## 🎯 B-ROLL
1. GitHub Unwrapped video (dẫn chứng real use case)
2. Code editor: React component → preview browser
3. Terminal: render progress → MP4 output
4. Agent workflow: prompt → agent code → MP4

---
*Script v1 — tháng 6/2026*
