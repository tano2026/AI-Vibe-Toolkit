# DESIGN.md — Airfare Decoded (HyperFrames frame spec)

> Design system cho VIDEO, không phải web. Agent đọc file này trước khi compose bất kỳ scene nào.
> Atoms là bất biến. Composition tự do. Số liệu lấy từ script.

## Tokens (atoms — không đổi)

| Token | Value | Dùng cho |
|---|---|---|
| `--ink` | `#111111` | Nét vẽ, chữ chính |
| `--paper` | `#fdfdfb` | Nền giấy trắng ngà (KHÔNG dùng trắng tinh #fff — đỡ gắt) |
| `--accent` | `#d92b2b` | Red accent — **tối đa 1 element/scene** |
| `--muted` | `#8a8a86` | Chữ phụ, đường mờ, "myth" side |
| Display font | Patrick Hand (fallback Comic Sans MS) | Tiêu đề, chữ "tay viết" |
| Body font | Inter | Caption dài, số liệu |

## Type scale (1920×1080)

- Hook line: 110–130px
- Section title: 76–84px
- Step/card heading: 52–56px
- Caption/body: 40–48px
- Big number (stat hit): 300–360px
- KHÔNG xuống dưới 36px — không đọc được trên mobile

## Motion grammar (bắt buộc thống nhất)

| Pattern | Spec |
|---|---|
| Element vào | `y:40–60, opacity:0 → power3.out, 0.6–0.8s` |
| Accent nhấn | `scale từ 1.8 hoặc back.out(2)` |
| SVG draw-on | stroke-dashoffset → 0, `power2.inOut`, 1.2–2.5s — hiệu ứng "tay vẽ" chủ đạo của kênh |
| Compare resolve | Bên sai mờ đi (opacity 0.35, scale 0.96), bên đúng phồng nhẹ (scale 1.04) |
| Count-up | GSAP tween object → Math.round trong onUpdate (seek-safe) |
| Pulse | yoyo + repeat HỮU HẠN (≤5) — contract cấm repeat:-1 |

Nhịp scene: element mới mỗi 0.7–1.0s, không để màn hình tĩnh quá 3s.

## Stick figure assets (Pollinations)

Prefix cố định — chỉ đổi mô tả scene sau prefix:
```
minimalist stick figure illustration, hand-drawn black ink line art style, clean white background, single red accent color for key element, simple airport and airplane doodle elements, editorial cartoon style, no text, no words, 16:9
```
URL pattern: `https://image.pollinations.ai/prompt/{URL_ENCODED_PROMPT}?width=1024&height=1024&nologo=true`

Ảnh đặt trong `assets/`, đặt tên `s{scene}-figure.png`. Nền ảnh trắng hòa vào `--paper`.

## 6 scene archetypes (mix theo script — KHÔNG dùng đủ 6 mỗi video)

1. **HOOK** — kinetic title 2 dòng + accent word + sub. 5–7s.
2. **CONCEPT** — figure trái + circle/underline draw-on + title/text phải. 8–12s.
3. **COMPARE** — myth (muted border) vs reality (accent border), resolve animation. 8–10s.
4. **BIG NUMBER** — count-up + label. 6–8s. Tối đa 1–2 lần/video.
5. **PROCESS** — 3–5 bước + đường nối draw-on + stagger. 10–14s.
6. **CTA** — brand line + subscribe button pulse. 6–8s, luôn cuối.

## Variation guard (HARD RULE)

Mỗi video PHẢI khác video trước ít nhất 3 trong 5 trục — chống flag inauthentic content:
1. Thứ tự + tổ hợp scene archetypes (vd: video A mở bằng BIG NUMBER thay vì HOOK)
2. Layout trong scene (figure trái↔phải, compare dọc↔ngang)
3. Hình Pollinations mới 100% (không tái sử dụng asset giữa các video)
4. Nhịp timeline (offset, stagger, duration lệch nhau)
5. Micro-motion (draw-on circle ↔ underline ↔ arrow ↔ zigzag)

Kênh khác (Actually Tested) nếu dùng chung pack: BẮT BUỘC đổi tokens (accent khác màu, font khác) + motion grammar riêng.
