# motion-graphics (Barty-Bart) — GitHub Repo

## TL;DR
6 skill Claude Code miễn phí của `Barty-Bart`, mỗi skill một việc: `motion-broll` (B-roll chuyển động bám theo lời nói từ transcript), `object-separation` (tách người/sản phẩm/bàn tay khỏi nền **ngay trên máy** bằng SAM 2), 3 skill explainer (hype 12–20s, demo 45–90s, one-take 10–30s) và `sound-effects` (SFX + nhạc đặt theo nhịp, có đo). 374 sao. **Cảnh báo:** tác giả dùng repo để dẫn tới cộng đồng trả phí, `object-separation` tải model 156 MB–898 MB ở lần đầu và rất chậm nếu không có GPU.

## Repo này dùng để làm gì
Thêm lớp motion cho video có sẵn:
1. Đưa video + transcript (SRT) → `motion-broll` lên bảng kế hoạch từng clip, chờ mày OK, rồi dựng.
2. Mỗi clip là một hình khối biến hình liên tục (pill → card → terminal → chart), không cắt, có con trỏ điều khiển.
3. Ra clip MP4 (toàn khung) hoặc `.mov` ProRes 4444 nền trong suốt, `compare.html`, `viewer.html`, `TIMING.md`.

## Số liệu đã kiểm (2026-10-12)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao / Fork | 374 / 60 | 📖 trang repo qua fetch, đã hỏi lại cho khớp tên repo |
| License | MIT. SFX đi kèm là **CC0** (Kenney + Freesound), README ghi đã kiểm từng file ngày 12/10/2026 | ✅ đọc `LICENSES.md` trong clone |
| Số commit | 1 (trên trang) | 📖 |
| Commit gần nhất | 2026-10-12 (repo rất mới) | ✅ `git log` trên bản clone nông |
| CLI `skills` nhận ra | 6 skill | ✅ `npx skills add <clone cục bộ> --list` |

## Đối chiếu với bài post
- "Tự tạo B-roll biến hình theo từng lời bạn nói": đúng theo README, dựa trên **transcript** mày đưa (ước lượng thời điểm từ), không tự nghe video.
- "Tự bóc tách người khỏi phông nền ngay trên máy": đúng theo SKILL.md (SAM 2 chạy local, video không upload). Nhưng **model weights vẫn tải từ mạng lần đầu**, và CPU-only khoảng 5 giây/khung → clip 10 giây 30fps mất cỡ nửa tiếng (số của tác giả).

## Setup
📖 Theo README, **chưa chạy**:
```bash
npx skills add Barty-Bart/motion-graphics   # chọn motion-broll và/hoặc object-separation
```
Rồi trong Claude Code: `/motion-broll`. Cần Node 18+, Python 3, ffmpeg **có ProRes encoder**. Lần đầu skill tự cài Playwright + Chromium vào thư mục `motion/` cục bộ.

`object-separation` tạo venv riêng (`python3 -m venv .object-separation`) và cài `torch transformers opencv-python-headless pillow numpy`. Chọn model theo máy: NVIDIA ≥12 GB → large (898 MB), GPU nhỏ/Apple Silicon → base-plus (323 MB), CPU → tiny (156 MB).

## ⚠️ License / Bảo mật / Quyền riêng tư
- MIT; SFX CC0 (dùng được cả video kiếm tiền). Đây là phần license sạch nhất trong cả nhóm.
- Video không bị upload khi tách nền, nhưng model SAM 2 tải từ Hugging Face lần đầu. Máy offline hoặc VPS chặn mạng sẽ hỏng bước này.
- README dẫn tới cộng đồng trả phí của tác giả ("full process"). Repo dùng được độc lập, đó chỉ là quảng cáo.

## Ví dụ thực tế
1. Video giải thích 8 phút của [CHỦ ĐỀ]: chèn 6 clip B-roll biến hình ở đúng các câu quan trọng.
2. Tách người nói khỏi nền để đặt panel trong suốt bên cạnh.

## Lưu ý / Lỗi thường gặp (theo chính README)
- Skill **không bịa số liệu**: biểu đồ chỉ thể hiện kích thước tương đối, chữ dùng "skeleton lines" tới khi mày đưa số thật.
- Preview chỉ để duyệt. Bản cuối mày ghép clip vào editor của mình.
- Panel nền trong suốt cần ProRes 4444, ffmpeg bản thiếu encoder sẽ không ra.

## Đánh giá cá nhân
**Chưa chấm điểm.** Điểm mạnh: skill nhỏ, một việc, license rõ, có luật "không bịa số", có bước duyệt kế hoạch. Điểm yếu: repo mới (ngày commit gần nhất là hôm nay), `object-separation` nặng với máy không GPU, chưa chạy. Hợp khi mày đã có video quay sẵn và chỉ cần thêm B-roll motion, **không** thay thế bộ dựng đầy đủ như `hyperframes-student-kit`.

## Link
- Repo: https://github.com/Barty-Bart/motion-graphics
- Liên quan trong kho: `repos/hyperframes-student-kit.md`, `repos/ffmpeg.md`, `stacks/motion-design-studio-claude-code.md`

---

## 🤖 Agent Integration

> Skill dạng prompt + script Python/Node, không có HTTP API.

### Hermes (Python)
```python
# ✅ Hàm đã chạy thật 2026-10-12. ProRes encoder chưa kiểm: cần `ffmpeg -encoders | grep prores`.
import shutil, subprocess

def check_env() -> dict:
    out = {t: bool(shutil.which(t)) for t in ("node", "python3", "ffmpeg")}
    if out["ffmpeg"]:
        enc = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
        out["prores"] = "prores" in enc
    return out
```

### OpenClaw
```bash
# ❓ chưa chạy từ GitHub
npx skills add Barty-Bart/motion-graphics
```

### Antigravity
```bash
# ❓ chưa chạy
ffmpeg -hide_banner -encoders | grep -i prores
python3 --version   # object-separation cần >= 3.10
```
> ⚠️ Không chạy `object-separation` trên VPS không có GPU với clip dài. ~5 giây/khung trên CPU (số của tác giả).
