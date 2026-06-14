# Remotion — Video Bằng React + Render Ra MP4 (49.9k⭐)

**Repo:** github.com/remotion-dev/remotion | Remotion License*
**Stars:** 49.9k | npm: 900k installs/tháng
**Website:** remotion.dev

*Free cho open-source/personal. Trả phí cho commercial production use.

---

## Cài & Setup

```bash
npx create-video@latest my-video
cd my-video
npm install
npm start  # preview tại localhost:3000
```

## Component Cơ Bản

```tsx
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';

export const MyVideo = () => {
  const frame = useCurrentFrame();
  
  // Animate opacity từ 0 → 1 trong 30 frames
  const opacity = interpolate(frame, [0, 30], [0, 1]);
  
  return (
    <AbsoluteFill style={{ backgroundColor: '#0a0a0a', opacity }}>
      <h1 style={{ color: 'white', fontSize: 80, textAlign: 'center' }}>
        AI Vibe Toolkit
      </h1>
    </AbsoluteFill>
  );
};
```

## Render Ra File

```bash
# Render MP4
npx remotion render MyVideo out/video.mp4

# Custom settings
npx remotion render MyVideo out/video.mp4   --fps=60   --width=1920   --height=1080

# TikTok vertical
npx remotion render MyVideo out/tiktok.mp4   --width=1080 --height=1920
```

## Templates Hay Nhất

```bash
# Clone templates
npx create-video@latest --template blank       # từ đầu
npx create-video@latest --template tailwind    # với Tailwind
npx create-video@latest --template three-js    # với Three.js 3D

# Community templates
npx create-video@latest --template starterkit  # data viz, charts
```

## Workflow Cho AI Vibe Toolkit

```tsx
// Video giới thiệu tool mới
// 1. Intro (3s) - hook text animation
// 2. Problem (5s) - illustrate pain point
// 3. Solution (10s) - demo screen recording
// 4. Code snippet (5s) - syntax highlighted
// 5. CTA (3s) - follow + link

// Data từ repo .md → feed vào React component → render video
```

## Khi Nào Dùng Remotion vs html-video

| Situation | Dùng gì |
|-----------|---------|
| Biết React | Remotion |
| Complex animations | Remotion |
| Quick simple video | html-video |
| Không biết code | HyperFrames |
| Data-driven video | Remotion |

---
*skills/remotion-skill.md | AI Vibe Toolkit | tháng 6/2026*
