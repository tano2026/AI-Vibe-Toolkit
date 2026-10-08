# buildfast-skills / generative-film-skill — GitHub Repo

## TL;DR
Skill (MIT, repo `buildfastwithai/buildfast-skills`, commit mới nhất 08/10/2026) cho agent làm **phim MP4 45–120 giây, 1920×1080, 30 fps về chủ đề bất kỳ** — mọi khung hình vẽ bằng code Python (pycairo + Pillow), nhạc tự tổng hợp bằng numpy/scipy, cắt đúng nhịp. Không stock footage, không ảnh AI, không nhạc bản quyền. Phim mẫu *SŪTRA* (văn minh Ấn Độ, 87 giây) phong cách in riso. **Nhẹ nhất trong 3 skill**: chỉ Python + ffmpeg, không cần Node/Chromium.

## Repo này dùng để làm gì
Repo là bộ 10 skill (ecommerce, SVG, HTML animation, landing page, motion studio, PDF→webbook, premium UI, talking avatar, game three.js, và `generative-film-skill`). Skill phim biến một chủ đề thành phim "explainer nghệ thuật": mỗi chương một ý hình ảnh (lưới thành phố tự dựng, fractal, đồng hồ dao động của chính nhạc…), một "sợi chỉ" xuyên suốt, bảng màu đặt tên theo chất liệu của nền văn hoá. Chủ đề kiểu "lịch sử vé máy bay", "bản đồ đường bay Việt Nam", "tại sao giá vé nhảy" hợp khẩu vị này.

## Số liệu đã kiểm (08/10/2026, đọc bản clone nông)
- License MIT. SKILL.md ~50KB, chứa luôn `engine.py` và `audio_kit.py` làm phụ lục (phòng khi thư mục `scripts/` không có)
- Có 2 ví dụ trong repo: `examples/sutra` (có contact sheet) và `examples/silk-road-demo` (15 giây, làm nhanh để thử)
- Số sao: **chưa đo** (API GitHub bị chặn trong phiên này)
- KHÔNG chạy thử được trong sandbox: máy này thiếu `pycairo` nên `engine.py` chưa chạy, chưa render khung nào

## Setup
```bash
npx skills@latest add https://github.com/buildfastwithai/buildfast-skills --skill generative-film-skill
# hoặc cài cả bộ: bỏ --skill, thêm --global nếu muốn dùng mọi dự án
pip install --break-system-packages pycairo fonttools   # numpy, scipy, Pillow thường có sẵn
which ffmpeg
python3 -c "from PIL import features; print('raqm', features.check('raqm'))"   # PHẢI True
```
Raqm bắt buộc vì nó xử lý chữ phức tạp (Devanagari, Ả Rập, Tamil…). Font tải lần đầu từ repo `google/fonts` trên GitHub → máy chạy phải ra được GitHub.

## Quy trình skill dặn agent (tóm từ SKILL.md)
1. **Ý tưởng trước code**: tra cứu mọi ngày/số/tên sẽ lên màn hình (ngày chưa chắc thì ghi "c."), chọn một vật xuyên suốt đặt tên phim, 6–10 chương mỗi chương một ý hình ảnh
2. **Nhạc trước**: viết `audio.py` theo nhịp (BPM), mọi cú cắt/flash rơi đúng sự kiện âm nhạc; kiểm loudness ~−16 đến −14 LUFS
3. **Cảnh** là hàm không trạng thái `scene(ctx, b, f)` (b = nhịp, f = khung) nên render song song được
4. **Khung thử → contact sheet → sửa** (bắt buộc, thường 2–3 vòng), rồi render, kiểm bằng `ffprobe -count_frames`, trả lời cuối: tên phim + 1 dòng ý tưởng + danh sách chương + nhạc + chỗ ước lượng

## Ví dụ thực tế
Prompt cho ABTRIP (nội dung kênh, không phải quảng cáo bán vé):
```text
Dùng generative-film-skill: làm phim 60 giây về "100 năm vé máy bay" — từ vé giấy
đến e-ticket. Mỗi chương một ý: PNR 6 ký tự, BSP, chuyển từ vé giấy sang điện tử.
Tra cứu đủ nguồn mọi số liệu trước khi lên màn hình, ngày chưa chắc ghi "c.".
```
Đầu ra: `film_full.mp4` + contact sheet để duyệt. Chọn chủ đề có nguồn kiểm được; skill buộc tra cứu nhưng agent vẫn có thể sai số liệu — mày duyệt trước khi đăng.

## Lưu ý / Lỗi thường gặp
- **Chưa chạy thử** — không biết thời gian render thật; skill có `workers` (dùng hết CPU) nhưng 87 giây × 30 fps ≈ 2.600 khung vẽ bằng cairo/Python, đoán là chậm, chưa đo
- **Tiếng Việt có dấu**: Raqm xử lý được shaping, nhưng font gợi ý (Anton, Space Mono, Fraunces…) có đủ dấu tiếng Việt hay không là **chưa kiểm** — thử 1 câu có dấu trước khi cam kết
- Gu thẩm mỹ rất riêng (in riso, lệch màu). Không hợp video bán hàng trực tiếp
- Nội dung do agent tra cứu → rủi ro sai thật; skill dặn gắn "c." và "schematic" nhưng không thay được việc kiểm tay
- Tải font từ GitHub lúc chạy → môi trường chặn mạng sẽ lỗi, tải font sẵn nếu dùng VPS bị giới hạn
- Chỉ một người tác giả/nhóm nhỏ, repo mới; chưa thấy đánh giá độc lập

## Đánh giá cá nhân
- Điểm mạnh: MIT, rất nhẹ (Python + ffmpeg), không phụ thuộc Chromium/Node nên hợp VPS nhỏ, nhạc + hình cùng một lưới nhịp, quy trình có bước kiểm khung bắt buộc, có ví dụ chạy thử 15 giây
- Điểm yếu: chưa chạy thử, tốc độ render chưa rõ, font có dấu chưa kiểm, gu thẩm mỹ hẹp, số liệu phụ thuộc agent tra cứu, repo mới
- Có nên dùng: 6/10. Là ứng viên số 1 để thử cho nội dung giáo dục dài 60–90 giây (kênh Tano / ABTRIP) vì chi phí thấp nhất. Làm đúng 1 phim thử `silk-road-demo` 15 giây trước, đo thời gian + kiểm chữ có dấu rồi mới quyết

## Link
- Repo: https://github.com/buildfastwithai/buildfast-skills
- Skill: https://github.com/buildfastwithai/buildfast-skills/tree/main/generative-film-skill
- Liên quan: `repos/cinetic.md`, `repos/hyperframes.md`, `repos/product-film-skill.md`, `repos/prompt-motion.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Skill này không có API; nó là bộ hướng dẫn + engine Python cục bộ.
# Hermes kiểm máy đã đủ đồ chưa TRƯỚC khi giao việc (chưa chạy thật trên VPS):
import importlib.util, shutil, subprocess

def check_genfilm_env():
    has = lambda m: importlib.util.find_spec(m) is not None
    missing = [m for m in ("cairo", "numpy", "scipy", "PIL", "fontTools") if not has(m)]
    ffmpeg = shutil.which("ffmpeg") is not None
    raqm = None
    if has("PIL"):
        from PIL import features
        raqm = features.check("raqm")
    return {"missing_py": missing, "ffmpeg": ffmpeg, "raqm": raqm}

def install_skill():
    return subprocess.run(["npx", "--yes", "skills@latest", "add",
        "https://github.com/buildfastwithai/buildfast-skills",
        "--skill", "generative-film-skill"], capture_output=True, text=True, timeout=300)
```

### OpenClaw
```bash
npx skills@latest add https://github.com/buildfastwithai/buildfast-skills --skill generative-film-skill
```

### Antigravity
```bash
# VPS Linux (chưa chạy thử)
sudo apt-get install -y ffmpeg libcairo2-dev pkg-config libraqm0
pip install --break-system-packages pycairo fonttools numpy scipy pillow
python3 -c "from PIL import features; print(features.check('raqm'))"   # phải True
# Thử trước bằng ví dụ 15 giây trong repo: examples/silk-road-demo (đo thời gian render)
```
> ⚠️ Tên gói `libraqm0` / `libcairo2-dev` theo Debian/Ubuntu phổ biến, chưa xác nhận trên VPS của mày. Font tải từ GitHub lúc chạy. Mọi số liệu lên phim phải được người duyệt.
