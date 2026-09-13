---
name: hyperframes-skill
description: >
  Repo: github.com/heygen-com/hyperframes (Apache 2.0, HeyGen).
  Open-source HTML-to-video rendering framework, cài qua `npx skills add`.
---

# HyperFrames (HeyGen) — HTML → Video MP4

**Repo:** github.com/heygen-com/hyperframes | Apache 2.0 | HeyGen
**Cách hoạt động:** composition là 1 file HTML, DOM khai báo timing bằng `data-*` attribute, animation runtime seekable, HyperFrames capture frame qua headless Chrome (Puppeteer + FFmpeg) ra MP4 xác định (deterministic) — khác hẳn video generation AI thường (mỗi lần render ra kết quả y hệt, không random).

> ⚠️ **Sửa lại so với bản cũ trong kho:** lệnh `npm install -g @heygen/hyperframes` KHÔNG đúng — package đó không tồn tại. Cách cài đúng là qua `npx skills add` (skill-based) hoặc clone repo dùng trực tiếp CLI `hyperframes` từ `@hyperframes/*` packages.

---

## Cài Nhanh (đúng)

```bash
# Cài toàn bộ skill của HyperFrames vào Claude Code/Cursor/Codex/Gemini CLI
npx skills add heygen-com/hyperframes

# Hoặc cài từng skill riêng
npx skills add heygen-com/hyperframes --skill hyperframes
npx skills add heygen-com/hyperframes --skill hyperframes-cli
```

Sau khi cài, Claude Code nhận các slash command: `/hyperframes` (author composition), `/hyperframes-cli` (dev-loop: init/lint/preview/render/doctor), `/hyperframes-media` (TTS Kokoro, transcribe Whisper, remove-background u2net), `/hyperframes-registry` (cài block/overlay có sẵn qua `hyperframes add`), `/gsap`, `/animejs`, `/lottie`, `/three`, `/waapi` (animation adapter theo runtime dùng trong composition).

## Skill con đáng chú ý (bên trong repo, cài lẻ được)

| Skill | Dùng khi |
|---|---|
| `hyperframes-cli` | Cần biết lệnh CLI: `init`, `lint`, `preview`, `render`, `doctor` |
| `hyperframes-animation` | Cần animation seek-safe: atomic motion rule + 7 runtime adapter (GSAP, Lottie, Three.js, Anime.js, CSS, WAAPI, TypeGPU) |
| `hyperframes-keyframes` | Cần keyframe 2D/3D chi tiết hơn animation cơ bản — FLIP transition, SVG morph, motion path |
| `motion-graphics` | Video ngắn <10-30s không lời (kinetic typography, logo reveal, lower-third, social overlay) |
| `talking-head-recut` | ⚠️ **Tên cũ là `graphic-overlays`, đã đổi tên (PR #1720, 25/6/2026)**. Lồng overlay/lower-third/quote card lên video talking-head/podcast có sẵn, sync theo transcript (Whisper local, không cần API key). Gọi bằng tên mới: `--skill talking-head-recut` |
| `website-to-hyperframes` | Chụp 1 URL biến thành video (pipeline 7 bước) |

## Workflow Cơ Bản

```bash
hyperframes init my-video --tailwind   # tạo project, có Tailwind v4 runtime
hyperframes preview                     # live reload, edit composition.html
hyperframes lint                        # check lỗi trước khi render
hyperframes render --output out.mp4     # render MP4 cuối
```

## Ví dụ thực tế
"Dùng /hyperframes, tạo video intro sản phẩm 10 giây: title fade-in, video nền, nhạc nền." — Claude Code tự viết `composition.html`, dùng GSAP timeline cho fade-in, render ra MP4 qua `hyperframes render`.

## Khác Biệt Với Remotion / html-video (đã có trong kho)

| | HyperFrames | Remotion | html-video |
|--|--|--|--|
| Ngôn ngữ compose | HTML + data-* timing | React (JSX) | HTML thuần |
| Render engine | Puppeteer + FFmpeg | Chromium headless | Playwright + FFmpeg |
| Có sẵn adapter animation | 7 runtime (GSAP/Lottie/Three/Anime/CSS/WAAPI/TypeGPU) | Interpolate API riêng | Tự viết CSS |
| Skill AI-agent sẵn có | Có (npx skills add) | Có (`remotion-best-practices`) | Không |
| Tốt nhất cho | Overlay/social clip/talking-head recut | Data-driven video (bar chart, animated report) | Custom animation đơn giản |

## Lưu ý / Lỗi thường gặp
- Đừng nhầm `graphic-overlays` — tên đã đổi thành `talking-head-recut`, cài tên cũ sẽ không tìm thấy skill.
- Audit bảo mật của `hyperframes-animation` chỉ pass 1/3 scanner (MEDIUM risk) — review kỹ trước khi cho Hermes tự chạy composition từ input không tin tưởng.
- Cần Node.js hiện đại + Chrome for Testing (tự tải lần đầu qua `hyperframes doctor`).

## Đánh giá cá nhân
- Điểm mạnh: open-source, miễn phí (Apache 2.0), skill AI-agent viết chi tiết hơn hẳn docs generic; overlay/talking-head-recut giải quyết đúng nhu cầu content thoại (voiceover-heavy) của kho.
- Điểm yếu: cần biết CSS/JS cơ bản để chỉnh sâu; kém hơn Remotion khi cần data-viz phức tạp kiểu React state.
- Có nên dùng không: 8/10 — hợp cho social clip/overlay nhanh; giữ Remotion cho case cần logic React phức tạp.

## Link
- Repo: https://github.com/heygen-com/hyperframes
- Skill mới nhất (renamed): `talking-head-recut` (trước là `graphic-overlays`)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess

def hyperframes_render(project_dir: str, output: str = "out.mp4") -> str:
    subprocess.run(["hyperframes", "lint"], cwd=project_dir, check=True)
    result = subprocess.run(
        ["hyperframes", "render", "--output", output],
        cwd=project_dir, capture_output=True, text=True
    )
    return result.stdout
```

### OpenClaw
```bash
npx skills add heygen-com/hyperframes --skill hyperframes-cli
npx skills add heygen-com/hyperframes --skill talking-head-recut
# gọi: "/hyperframes-cli render composition.html thành video 1080x1920"
```

### Antigravity
```bash
# Deploy trên VPS: cần Chrome for Testing + Node
npm install -g @hyperframes/cli
hyperframes doctor   # kiểm tra môi trường trước khi giao Hermes chạy tự động
```
> ⚠️ Render tốn CPU/RAM nếu chạy nhiều composition song song — giới hạn concurrency trên VPS.
