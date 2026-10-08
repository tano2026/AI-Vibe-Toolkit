# cinetic — GitHub Repo

## TL;DR
Skill (MIT, v1.0.0 ra 04/10/2026, tác giả Leon Lin / `Leonxlnx`) bắt agent **đạo diễn một phim ngắn** thay vì ghép component animation: viết 3 concept → chọn 1 → dựng brand → dựng phim bằng **Remotion** (mặc định) hoặc **HyperFrames** → nhạc tổng hợp khớp từng beat → render + tự chấm điểm. Phim mẫu "Kiln" 25 giây làm từ brief 2 câu. Mạnh nhất trong 3 skill phim của prompt-motion, nhưng **nặng**: 1 phim ≈ 95 phút và ~626K token theo chính tác giả.

## Repo này dùng để làm gì
Làm video launch/teaser, feature loop cho landing page, logo sting, UI walkthrough, vertical cho Reels/TikTok — hoàn toàn bằng code, có nhạc + SFX. Khác `product-film-skill` (dựng từ UI thật của app): cinetic mạnh ở **ý tưởng + thương hiệu + kỹ thuật chuyển động**, có cả thư viện kỹ thuật bốc ngẫu nhiên để các phim khỏi giống nhau.

## Số liệu đã kiểm (08/10/2026, đọc từ bản clone nông của repo)
- License: MIT (LICENSE đã mở xem). Release `1.0.0` ngày 04/10/2026, commit mới nhất 05/10/2026
- 273 kỹ thuật / 14 nhóm trong `assets/library/techniques.json`; `scripts/pick.py` bốc ngẫu nhiên có seed
- Số sao / issue: **chưa đo** (API GitHub bị chặn trong phiên này)
- Số liệu "thắng baseline" là của tác giả, tự chấm bằng agent giám khảo: vòng 7 đạt 54/56 kỳ vọng so với 41/56; thắng giám khảo trung lập 2/4 phim, giám khảo "house style" 4/4 (giám khảo house-style dùng đúng luật cấm của chính skill nên thiên vị — đừng đọc là "ngon hơn 4/4")
- ĐÃ CHẠY THẬT: `python3 -I skills/cinetic/scripts/pick.py --seconds 20 --seed 7` → ra 8 kỹ thuật kèm công thức dựng, chạy offline, không cần cài gì. CHƯA render phim nào (cần Chromium + Node + Python lib)

## Setup
```bash
npx skills add Leonxlnx/cinetic
```
Yêu cầu (README): macOS hoặc Linux (Windows chỉ qua WSL2, tác giả chưa test), Node 22+, ffmpeg 6+ có libx264, Python 3.11+ với `numpy scipy soundfile pyloudnorm opencv-python librosa` (+ `fonttools brotli uharfbuzz pillow`), Chromium/Chrome headless.
```bash
python3 -m venv ~/.venvs/cinetic && source ~/.venvs/cinetic/bin/activate
pip install numpy scipy soundfile pyloudnorm opencv-python librosa fonttools brotli uharfbuzz pillow
```
Kích hoạt venv TRƯỚC khi chạy agent (script gọi `python3` trần).

## ⚠️ License engine — đọc trước khi dùng cho dự án thương mại
cinetic MIT, nhưng engine mặc định **Remotion có license riêng**: miễn phí cho cá nhân và công ty ≤ 3 người, từ 4 người trở lên phải mua license công ty (theo README cinetic; kiểm lại trang Remotion trước khi dùng thương mại). **HyperFrames là Apache-2.0** → khi làm cho khách hàng hay brand của Tano Agency, mặc định bảo agent dùng engine HyperFrames; chỉ dùng Remotion sau khi kiểm license theo quy mô công ty đứng tên dự án. Tao không phải luật sư.

## Ví dụ thực tế
Prompt mẫu (từ README, thay sản phẩm/brand của dự án đang làm):
```text
Làm teaser 20 giây dạng dọc 1080x1920 cho [TÊN SẢN PHẨM] về [TÍNH NĂNG CHÍNH, 1 câu].
Dùng brand: [ink #HEX, paper #HEX, accent #HEX, font]. Engine HyperFrames. Có nhạc.
(Không có brand → ghi "Invent the brand" để agent tự dựng.)
```
Đầu ra theo README: master + poster; teaser launch thì kèm bản 9:16 và 1:1 dựng lại bố cục (không cắt từ bản gốc). Phim vẫn là source code: sửa 1 dòng chữ hoặc đổi màu accent rồi render lại.

## Lưu ý / Lỗi thường gặp
- **Tốn**: tác giả ghi trung bình 95 phút và 626K token/phim (gấp ~3 lần chạy không có skill). Motion blur nhân thời gian render 3–8 lần; `render.sh --blur --budget` để giới hạn
- **Luật cấm cứng** (lint tự bắt): không serif, không chữ nghiêng, không cam/vàng/be/tím, không glow, không emoji, không "Introducing…". Brand bạn đưa luôn thắng. Nghĩa là phim "sạch kiểu cinetic" — không hợp phong cách nhiều màu/nhiều chữ kiểu TikTok VN
- **Chữ tiếng Việt có dấu**: chưa kiểm font nào trong luồng của cinetic đủ dấu. Làm thử 1 câu có dấu trước khi cam kết
- Cần máy mạnh có Chromium: không chạy trên điện thoại. Nếu máy làm việc là Windows và Claude Code chưa chạy ổn → chạy qua VPS Linux (Antigravity cài)
- Chưa render phim nào trong kho này; chưa biết thật trên VPS mất bao lâu

## Đánh giá cá nhân
- Điểm mạnh: MIT, có quy trình kiểm thật (forensics từng khung, audit đồng bộ âm thanh, ship gate), thư viện kỹ thuật bốc ngẫu nhiên chống phim giống nhau, chọn được engine Apache
- Điểm yếu: đắt (thời gian + token), dùng Remotion thì dính license công ty, thẩm mỹ bị ép vào một gu, chữ có dấu chưa kiểm, số liệu đánh giá do tác giả tự chấm
- Có nên dùng: 7/10. Dùng cho 1–2 phim thương hiệu quan trọng (launch sản phẩm, teaser thương hiệu của khách) chứ không phải dây chuyền video hàng ngày. Làm hàng loạt thì `repos/hyperframes.md` + template rẻ hơn nhiều
- Dùng kèm: lấy riêng `pick.py` + `technique-library.md` làm nguồn tra kỹ thuật cho Designer Pro, không cần chạy cả pipeline

## Link
- Repo: https://github.com/Leonxlnx/cinetic
- Cài: `npx skills add Leonxlnx/cinetic`
- Phim mẫu "Kiln" 25 giây: link MP4 trong README của repo
- Liên quan: `repos/hyperframes.md`, `repos/product-film-skill.md`, `repos/prompt-motion.md`, `agents/designer-pro/skills/prompt-motion-reference/SKILL.md`, `stacks/cinematic-techniques-ai-video.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# cinetic không có HTTP API — nó là skill cho agent. Hermes chỉ làm được 2 việc:
# (1) cài skill vào VPS, (2) bốc kỹ thuật ngẫu nhiên (chạy offline, đã test).
import subprocess, json

def install_cinetic():
    # cần Node 22+; chạy trên VPS Linux, KHÔNG phải máy Windows
    return subprocess.run(["npx", "--yes", "skills", "add", "Leonxlnx/cinetic"],
                          capture_output=True, text=True, timeout=300)

def pick_techniques(skill_dir, seconds=20, seed=7):
    # in kế hoạch kỹ thuật bằng Markdown (đã chạy thật 08/10/2026)
    r = subprocess.run(["python3", "-I", f"{skill_dir}/scripts/pick.py",
                        "--seconds", str(seconds), "--seed", str(seed)],
                       capture_output=True, text=True, timeout=60)
    return r.stdout
```
Phần dựng phim thật cần agent có shell + Chromium (Claude Code / DeepSeek Harness trên VPS), Hermes đơn lẻ không đủ.

### OpenClaw
```bash
# Cài như skill chuẩn SKILL.md; nhờ agent dùng engine HyperFrames
npx skills add Leonxlnx/cinetic
```

### Antigravity
```bash
# Chuẩn bị VPS Linux để render (chưa chạy thử trên VPS thật)
sudo apt-get install -y ffmpeg chromium python3-venv
python3 -m venv ~/.venvs/cinetic && . ~/.venvs/cinetic/bin/activate
pip install numpy scipy soundfile pyloudnorm opencv-python librosa fonttools brotli uharfbuzz pillow
node -v   # phải >= 22
# test máy theo docs/setup.md mục "A first test render" của repo trước khi giao việc thật
```
> ⚠️ Mỗi phim ~95 phút / ~626K token (số của tác giả). Đặt giới hạn token/thời gian trước khi giao agent. Remotion cần license nếu công ty ≥ 4 người.
