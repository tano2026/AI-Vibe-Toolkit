# animate (cth9191) — GitHub Repo

## TL;DR
Plugin Claude Code của `cth9191` làm video hoạt hình ngắn **bằng một `<canvas>` duy nhất**, vẽ và chấm nhạc theo thủ tục, render ra MP4 bằng trình duyệt headless + ffmpeg. Có **7 style dựng sẵn** (cut paper, crosshatch, riso, sketchbook, math, pixel, isometric) cộng slot thứ 8: style riêng khớp theo tài liệu tham khảo của mày. Điểm đáng giá: **ba lần duyệt trước khi tốn công animate** (câu chuyện, hình, storyboard). 526 sao. **Cảnh báo:** lồng tiếng dùng ElevenLabs (trả phí), chưa chạy gì.

## Repo này dùng để làm gì
Explainer, lịch sử, truyện ngắn hoạt hình 30–90 giây không cần After Effects:
| Bước | Mày thấy gì | Mày quyết gì |
|---|---|---|
| 0 Intake | vài câu hỏi + thư viện style | chủ đề, định dạng, giọng, look |
| 1 Story check | bảng beat đánh số, fact có tra web | duyệt/đổi beat |
| 2 Look check | 2–4 khung hình full-size | thumbs up từng khung |
| 3 Storyboard | mỗi beat một key frame kèm âm thanh | thumbs up/down theo số panel |
| 4–5 Build + Giao | video + số đo (cắt đúng lưới nhịp, loudness...) | ghi chú → vòng sửa |

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 526 / 86 | 📖 trang repo qua fetch, đã hỏi lại cho khớp tên repo |
| License | MIT | 📖 trang repo |
| Số commit | 10 | 📖 trang repo |
| Commit gần nhất | 2026-10-05 | ✅ `git log` trên bản clone nông |
| CLI `skills` nhận ra | 1 skill (`animate`) | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
- "7 phong cách thủ công (cắt giấy, riso, pixel art...)": đúng 7 style, nhưng `math` là kiểu manim chứ không phải thủ công.
- "Duyệt kỹ storyboard trước khi render canvas ra MP4": đúng theo README, có 3 cổng duyệt.

## Setup
📖 Theo README, **chưa chạy**:
```bash
npm i -g playwright && npx playwright install chromium
# Trong Claude Code:
/plugin marketplace add cth9191/animate
/plugin install animate@animate
/animate a narrated 45s explainer of how DNS works, math style, 16:9
```
Cần Claude Code, Node 18+, Playwright + Chromium, ffmpeg trong PATH.

## ⚠️ License / Bảo mật / Quyền riêng tư
- Lồng tiếng: viết script, lấy từng câu từ **ElevenLabs connector** (hoặc giọng mày thu), rồi lấy thời điểm từng từ bằng faster-whisper chạy local. ElevenLabs tính phí. Ghi chú từ kho: lần thử 11/10/2026 (`repos/elevenlabs-skills.md`) bị chặn gói miễn phí khi đi qua proxy/VPN.
- Tài liệu tham chiếu của mày (video, ảnh) ở lại máy mày theo README.
- Style kế thừa từ tác phẩm nào thì tránh bắt chước một tác giả cụ thể, README dùng "matched look" từ chính tài liệu của mày.

## Ví dụ thực tế
1. Explainer 45 giây "[KHÁI NIỆM] là gì" kiểu cut paper, 16:9 + bản dọc 9:16 (`export.mjs --formats 9:16,1:1,16:9`).
2. Dòng thời gian lịch sử của [NGÀNH] dạng chuỗi shape-morph (ví dụ mẫu: "history-of-ai" 60 giây, 15 mốc).

## Lưu ý / Lỗi thường gặp (theo chính README)
- Có công cụ `review` đo: cắt đúng lưới nhịp, chữ bị cắt/chồng, loudness. Dùng nó thay vì tin cảm giác.
- Có `tools/frame-hash` kiểm sau khi sửa kit, piece cũ có còn giống hệt từng điểm ảnh không.
- Mở `index.html` đã build trong trình duyệt để xem trước (`?t=12.5` đóng băng một khung).

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: quy trình duyệt trước khi tốn công, số đo giao hàng, style tách khỏi engine nên thêm style mới không phá cũ. Điểm yếu: chưa chạy, cần ElevenLabs cho bản có lời, hoạt hình thủ tục có trần chất lượng (nhân vật có mặt, cảnh phức tạp khó hơn explainer dạng sơ đồ). Hợp nhất cho explainer và video lịch sử dạng sơ đồ/shape, **không** hợp video quảng cáo sản phẩm thật (dùng `product-launch-motion`).

## Link
- Repo: https://github.com/cth9191/animate
- Liên quan trong kho: `repos/elevenlabs-skills.md`, `repos/whisper.md`, `repos/ffmpeg.md`, `stacks/motion-design-studio-claude-code.md`

---

## 🤖 Agent Integration

> Plugin dạng prompt + công cụ Node, không có HTTP API.

### Hermes (Python)
```python
# ✅ Hàm đã chạy thật 2026-10-12 (node, npx, ffmpeg có; chromium hệ thống không, cần playwright install).
import shutil

def check_env(tools=("node", "npx", "ffmpeg")) -> dict:
    return {t: bool(shutil.which(t)) for t in tools}
```

### OpenClaw
```bash
# ❓ chưa chạy. Lệnh /plugin chỉ có trong Claude Code, không áp dụng cho OpenClaw.
npx skills add cth9191/animate
```

### Antigravity
```bash
# ❓ chưa chạy
npm i -g playwright && npx playwright install chromium
```
> ⚠️ Bước lồng tiếng cần ElevenLabs. Không đặt key trong repo, chỉ dùng biến môi trường.
