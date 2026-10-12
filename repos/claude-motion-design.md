# claude-motion-design — GitHub Repo

## TL;DR
Skill Claude Code của Raphaël Aubry (`howseen-ai`, MIT) dựng video motion **hoàn toàn bằng code**: HTML + Playwright + ffmpeg, **không Remotion, không license nào**. Điểm riêng: cắt cảnh khớp nhịp nhạc (tìm "drop" thật bằng năng lượng dải tần), đặt từng hiệu ứng âm thanh tại đỉnh đo được, và có "remake mode" dựng lại 1:1 một video launch có sẵn. **Cảnh báo:** 0 sao, 17 commit, `npx skills add` **không nhận ra** cấu trúc repo (phải copy tay), và tao chưa chạy gì.

## Repo này dùng để làm gì
Cho Claude cách làm video ngắn 24–45 giây theo kiểu "toàn bộ phim là một hàm `seek(t)`": cùng đầu vào ra cùng khung hình, sửa một cảnh không đụng cảnh khác. Quy trình: đầu vào → bản đồ nhịp → duyệt 4 ảnh tĩnh → render đầy đủ → quét lỗi giật → âm thanh → ghép cuối.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 0 / 0 | 📖 trang repo qua fetch, chưa đối chiếu API |
| License | MIT (code) | 📖 README + trang repo |
| Số commit | 17 | 📖 trang repo |
| Commit gần nhất | 2026-10-02 | ✅ `git log` trên bản clone nông |
| CLI `skills` nhận ra | **Không** (skill nằm ở `skill/motion-design/`) | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
- Post: "Video demo chỉ mất đúng 5 lần prompt trên Opus 5.5". README ghi: làm bằng Claude Opus 5.5 và skill "**in 5 iterations**" (5 vòng lặp). Vòng lặp không đồng nghĩa 5 prompt, chưa có log để biết.
- Post: "Cắt dựng khớp từng nhịp bass của nhạc bằng Playwright và FFmpeg". README: đúng, scene đặt theo beat map, `analyze_song.py` tìm drop bằng năng lượng dải tần, SFX đặt theo đỉnh đo, loudnorm 2 lượt -14 LUFS (📖).

## Setup
📖 Theo README, **chưa chạy**:
```bash
# Cài tay (CLI skills không nhận ra repo này)
mkdir -p ~/.claude/skills && cp -r skill/motion-design ~/.claude/skills/
pip install playwright imageio-ffmpeg numpy pillow
python -m playwright install chromium
```
Rồi trong Claude Code gõ `/motion-design` hoặc xin một video.

Chạy ví dụ: `cd examples/howseen-launch && python fetch_assets.py && python render.py full` (24 giây, 60 fps, có motion blur). `fetch_assets.py` tải nhạc, SFX, logo, font từ nguồn miễn phí bên ngoài.

## ⚠️ License / Bảo mật / Quyền riêng tư
- Code MIT. Media bên thứ ba **do script tải về, không nằm trong repo** và theo license riêng (Mixkit, Pexels/Unsplash, font OFL). Kiểm license từng file trước khi dùng cho video thương mại.
- Logo trong ví dụ thuộc chủ sở hữu của nó, không phải của mày.
- **Remake mode** ("dựng lại 1:1 một video launch cho brand của mày, so sánh chia đôi màn hình"): README dặn không dùng lại nhạc, giọng, ảnh người của bản gốc. Dù vậy đây vẫn là dựng lại cấu trúc và nhịp cắt của video người khác. Đừng dùng cho video thương mại khi chưa xem lại quyền.
- Tránh dùng chuỗi `fetch_assets.py` trong pipeline tự động khi chưa đọc script (tải file từ web về máy chạy).

## Ví dụ thực tế
1. Video loop 20–24 giây cho trang chủ của [SẢN PHẨM], khớp một bản nhạc miễn phí.
2. Video ngắn cho LinkedIn/Reels: lời nhắn "make the transitions faster" chỉ là sửa code, render lại.

## Lưu ý / Lỗi thường gặp (theo chính README)
- Chỉ dùng `seek(t)`: không CSS transition, không timer. Viết kiểu khác là lỗi giật.
- Dữ liệu minh hoạ phải ghi "Example data" trên màn hình, README đặt thành luật trung thực.
- Có bản `draft` 540p để duyệt trước khi render master.

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: không phụ thuộc Remotion (quan trọng với công ty đủ lớn, xem `repos/remotion.md`), kỷ luật đo (nhịp, âm lượng, vòng lặp nối). Điểm yếu: 0 sao, chưa ai kiểm, cài tay, remake mode có vùng xám bản quyền. Hợp nhất khi mày muốn video có nhạc khớp nhịp và không muốn dính license Remotion.

## Link
- Repo: https://github.com/howseen-ai/claude-motion-design
- Liên quan trong kho: `repos/product-launch-motion.md`, `repos/hyperframes.md`, `repos/remotion.md`, `stacks/motion-design-studio-claude-code.md`

---

## 🤖 Agent Integration

> Skill dạng prompt + script Python, không có HTTP API.

### Hermes (Python)
```python
# ✅ Hàm check đã chạy thật 2026-10-12. Chromium hệ thống KHÔNG có trong sandbox này (False),
# nhưng `playwright install chromium` mới là bước cài đúng, nên False chưa phải lỗi.
import shutil

def check_env(tools=("python3", "ffmpeg", "ffprobe", "chromium")) -> dict:
    return {t: bool(shutil.which(t)) for t in tools}
```

### OpenClaw
```bash
# ❓ chưa chạy. CLI skills KHÔNG nhận ra repo này, copy tay:
git clone https://github.com/howseen-ai/claude-motion-design
mkdir -p ~/.claude/skills && cp -r claude-motion-design/skill/motion-design ~/.claude/skills/
```

### Antigravity
```bash
# ❓ chưa chạy
pip install playwright imageio-ffmpeg numpy pillow
python -m playwright install chromium
```
> ⚠️ `fetch_assets.py` và các script `mixkit_sfx_search.py`, `svgl_logos.py` gọi ra web ngoài. Đọc trước khi chạy trên VPS.
