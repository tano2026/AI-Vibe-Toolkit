# sc-datav — Dashboard 3D Sci-Fi Từ Dữ Liệu Của Mày

**Repo:** github.com/knight-L/sc-datav | MIT
**Stack:** Three.js + Vue3
**Dùng cho:** Data visualization kiểu "màn hình lớn" trong phim

---

## Cài & Run

```bash
git clone https://github.com/knight-L/sc-datav
cd sc-datav
npm install
npm run dev  # localhost:5173
```

## Feed Data Của Mày

```javascript
// src/data/dashboard.js
export const dashboardData = {
  // Thay bằng data của mày
  metrics: [
    { label: "GitHub Stars", value: 188000, trend: "up" },
    { label: "Skills Built", value: 26, trend: "up" },
    { label: "Videos Scripted", value: 41, trend: "up" },
  ],
  
  charts: {
    starsOverTime: [
      { date: "2026-02", stars: 95000 },
      { date: "2026-03", stars: 130000 },
      { date: "2026-04", stars: 160000 },
      { date: "2026-05", stars: 188000 },
    ]
  }
}
```

## Use Cases

```bash
# 1. Portfolio showcase — vibe coder portfolio
# 2. Analytics dashboard — show metrics AI Vibe Toolkit
# 3. Video background — dùng làm background recording
# 4. Client demo — wow factor khi present
# 5. Thumbnail — screenshot làm thumbnail video
```

## Export Làm Thumbnail

```bash
# Screenshot tại resolution cao
npm run build
# Open dist/index.html
# Chrome DevTools → Device → Custom 1280x720
# Screenshot → dùng làm thumbnail YouTube
```

## Customization

```javascript
// Đổi color scheme (src/theme.js)
export const theme = {
  primary: '#00ff88',    // neon green
  secondary: '#0088ff',  // electric blue
  background: '#050510', // deep space
  grid: '#1a1a3e',      // subtle grid
}
```

---
*skills/sc-datav-skill.md | AI Vibe Toolkit | tháng 6/2026*
