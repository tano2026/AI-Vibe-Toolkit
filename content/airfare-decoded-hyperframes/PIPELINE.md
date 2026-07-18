# PIPELINE.md — Airfare Decoded × HyperFrames

> Chạy trên Windows machine local (đã có `HYPERFRAMES_BROWSER_PATH`). Render local = free.
> Yêu cầu: Node.js 22+, FFmpeg.

## Setup 1 lần

```bash
# 1. Cài skills chính thức cho Claude Code / coding agent (core set)
npx skills add heygen-com/hyperframes --full-depth

# 2. Init project
npx hyperframes init airfare-decoded
cd airfare-decoded
# Copy index.html + DESIGN.md của pack này vào project
```

## Loop sản xuất mỗi video

```
Script (Claude, creative tier qua OmniRoute)
  → SCRIPT.md (narration lock) + timing từng scene
  ↓
Pollinations gen figures (prefix trong DESIGN.md)
  → curl vào assets/s{n}-figure.png
  ↓
ElevenLabs voiceover
  → assets/vo.mp3 — đo duration thật → chỉnh data-start/data-duration các scene khớp audio
  ↓
Agent compose index.html (đọc DESIGN.md + variation guard checklist)
  ↓
npx hyperframes check      # 0 findings mới đi tiếp (lint + runtime + layout + motion + contrast)
npx hyperframes snapshot --at 3,10,20,30,40,50   # eyeball từng frame giữa scene
npx hyperframes preview    # xem live, sửa timeline trong Studio
npx hyperframes render     # → MP4
  ↓
CapCut: sub + polish nhẹ → upload
```

## Gen assets nhanh (paste chạy luôn)

```bash
# Pollinations — ví dụ figure scene 2 (người bối rối nhìn 2 giá vé khác nhau)
PROMPT="minimalist stick figure illustration, hand-drawn black ink line art style, clean white background, single red accent color for key element, confused stick figure looking at two different price tags on airplane tickets, editorial cartoon style, no text, no words"
curl -o assets/s2-figure.png "https://image.pollinations.ai/prompt/$(python3 -c "import urllib.parse,os;print(urllib.parse.quote(os.environ['PROMPT']))")?width=1024&height=1024&nologo=true"
```

## Contract rules — vi phạm là render hỏng âm thầm

- Root phải sized px cụ thể; nền full-screen đặt trên CHILD absolute inset:0, KHÔNG đặt background lên root
- 1 timeline duy nhất `gsap.timeline({paused:true})` tại `window.__timelines["<id>"]`, build đồng bộ lúc load
- `<audio>`/`<video>` là con TRỰC TIẾP của root — framework tự quản playback
- Không đụng visibility của `.clip` — framework quản; chỉ animate element BÊN TRONG clip
- Cấm: `repeat:-1`, `Math.random` không seed, clock/Date.now, network call lúc render
- Mọi `id` unique toàn trang — trùng id ảnh → render blank
- Render duration = `data-duration` của root, không phải độ dài timeline

## Sync audio ↔ scene

1. ElevenLabs xuất vo.mp3 → `ffprobe -i assets/vo.mp3 -show_entries format=duration -v quiet -of csv="p=0"`
2. Chia narration theo scene trong SCRIPT.md, lấy timestamp từng đoạn
3. Set `data-start`/`data-duration` mỗi scene = timestamp đó (+0.3s đệm đầu)
4. Root `data-duration` = tổng audio + 1s tail

## Cloud render (khi cần batch trên VPS, không muốn treo máy local)

`npx hyperframes cloud render` — qua HeyGen API, $0.10/phút 1080p30. Video 10 phút = $1. Chỉ dùng khi batch; mặc định render local free.

## Checklist trước upload

- [ ] `check` 0 findings
- [ ] Variation guard: khác video trước ≥3/5 trục (xem DESIGN.md)
- [ ] Insider detail ≥2 chỗ trong script (moat của kênh)
- [ ] Quy định/luật trong script đã verify bằng web search (DOT/EU261/visa đổi liên tục)
- [ ] Audio khớp scene, không có scene tĩnh >3s
- [ ] YouTube disclosure "altered/synthetic" nếu cần
