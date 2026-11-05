# Lemo-Opuscar (lemomo-ai/lemo-opuscar) — Bộ phong cách phim làm bằng code cho Claude Code

## TL;DR
Thư viện 66 "phong cách phim" (màu nước, tranh khắc gỗ, ukiyo-e, bản tin vệ tinh, pixel RPG...) cho coding agent. Mỗi phong cách là một file prompt `STYLE.md` kèm một phim demo vẽ hoàn toàn bằng code (canvas/WebGL render từng khung, nhạc và giọng đọc cũng sinh bằng code), không dùng model video, không dùng stock footage. Cài như một plugin Claude Code, rồi nói "làm phim 45 giây phong cách watercolor về...". Khoảng 12,6 nghìn sao, giấy phép code MIT, phim demo CC BY 4.0. Tác giả ghi thẳng: **tinh chỉnh cho Claude Opus 5.5, model khác có thể không ra đúng**. Tao đã chạy thử bước tải thư viện, **chưa render phim nào** (một phim tốn khoảng 30 đến 60 phút và nhiều token theo README).

## Repo này dùng để làm gì
Vấn đề nó giải: muốn video có phong cách riêng mà không có thợ dựng, không trả tiền model video. Thay vì sinh video bằng AI, agent đóng vai đạo diễn kiêm họa sĩ: viết code vẽ từng khung hình, ghép nhạc, giọng đọc, phụ đề rồi xuất MP4 (mặc định 1920x1080, 24 fps).

Cách nó vận hành (theo README và `plugin/skills/lemo-opuscar/SKILL.md`):
- `DIRECTOR.md`: cách đạo diễn (cốt truyện, âm thanh, nhịp, camera, tự kiểm tra).
- `TECHNIQUE.md`: cách dựng (render từng khung, giọng đọc, nhạc, trộn âm).
- `styles/<tên>/STYLE.md`: ngoại hình và âm thanh của phong cách đó. Câu chuyện là của mày.
- `core/`: bộ công cụ chung (render bằng Playwright + headless Chromium, three.js, TTS, mix).

Nhóm phong cách: Edit & Documentary (8), Evidence Films (8), Hand-drawn & Painting, East Asian Traditions, Print & Printmaking, Graphic & Type, Information & Keynote, Cartoon & Anime, Games... Có tính năng "tạo phong cách riêng": sửa một phong cách có sẵn hoặc bắt đầu từ trang trắng, lưu ở `~/lemo-my-styles/<tên>/`.

## Setup từng bước
Cách 1 (khuyên dùng, theo README):
```bash
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
# rồi trong Claude Code, ở thư mục muốn đặt phim:
# /lemo-opuscar:lemo-opuscar   (nó hỏi ngôn ngữ, rồi hỏi mày muốn làm gì)
```
Lần đầu dùng, skill tự tải thư viện về `~/lemo-opuscar` (clone thưa, bỏ file demo nặng), phim của từng dự án nằm trong thư mục mày đang đứng.

Cách 2: `git clone https://github.com/lemomo-ai/lemo-opuscar.git && cd lemo-opuscar && claude` (phim vào `films/<tên>/`).

Cài thư viện phụ thuộc (skill tự gọi, vài phút):
```bash
sh plugin/skills/lemo-opuscar/scripts/setup.sh deps          # lõi: Node + Chromium headless + Python lõi
sh plugin/skills/lemo-opuscar/scripts/setup.sh deps voice    # thêm giọng đọc (Kokoro) nếu phim có lời
sh plugin/skills/lemo-opuscar/scripts/setup.sh deps music    # thêm công cụ nhạc
```
Yêu cầu hệ thống theo README: Node 20+, **ffmpeg 7+**, Python 3.11+ (hoặc uv). Ubuntu 24.04 chỉ có ffmpeg 6.1, README bảo dùng bản static build.

## Đã kiểm gì, chưa kiểm gì
- Đã chạy: `sh -n setup.sh` (cú pháp ổn) và `setup.sh` không tham số với `LEMO_OPUSCAR_HOME` trỏ vào thư mục tạm. Kết quả: tải thư viện thành công (khoảng 31 MB sau clone thưa) và in `LIB=<đường dẫn>`. Nó **cảnh báo thiếu ffmpeg 7+** (máy tao có 6.1.1) và nhắc chạy `deps` trước khi render. Đúng như README.
- Đã đếm: 66 thư mục phong cách trong `styles/` (khớp con số 66 ở README).
- Chưa chạy: `setup.sh deps` (tải Chromium, nặng), render bất kỳ phim nào, giọng đọc, nhạc. Chưa kiểm được chất lượng phim, chỉ đọc mô tả `STYLE.md` và README.
- Chưa kiểm lệnh `claude plugin marketplace add` thật (tao đọc từ README và file `.claude-plugin/marketplace.json`, tên marketplace `lemolab`, plugin `lemo-opuscar`).

## Ví dụ thực tế
**Minh hoạ, chưa render thật.** Làm clip giới thiệu tour cho ABTRIP:
- Input cho Claude Code: "Làm phim 45 giây phong cách **silkscreen-poster** về hành trình Hà Nội đi Đà Nẵng, mỗi cảnh là một tấm poster in lụa, giọng nữ ấm."
- Output theo thiết kế của nó: thư mục `<tên>/` chứa treatment, mã nguồn từng cảnh, âm thanh và MP4 cuối (danh sách chính xác nằm ở `DIRECTOR.md` mục 11).
- Chỉ định phong cách bằng tên tiếng Anh, tên tiếng Trung hoặc tên thư mục đều được (tra `styles/README.md`).

## Lưu ý / Lỗi thường gặp
- **Gắn chặt với Claude Opus 5.5.** README cảnh báo model khác có thể không tái hiện tốt. Chạy bằng Sonnet hay Haiku là tự chịu rủi ro, và tao chưa thử model nào.
- **Tốn thời gian và token**: 30 đến 60 phút mỗi phim, theo README. Không hợp để làm hàng loạt video TikTok mỗi ngày.
- **ffmpeg 7+** là chỗ dễ vấp nhất trên Ubuntu 24.04 và VPS (tao gặp đúng cảnh báo này).
- Phiên bản Node, Playwright, Chromium headless cần tải được từ mạng. Trên VPS chặn mạng sẽ hỏng ở bước `deps`.
- Giấy phép: code MIT, phim demo CC BY 4.0 (phải ghi nguồn LemoLab và link repo nếu dùng lại phim mẫu). Phim mày tự làm bằng thư viện thuộc về mày, không cần ghi nguồn. Ba bản thu giọng trong demo (Game Show Flat, Paper-cut Lightbox, Broadcast News Package) **không** thuộc CC BY 4.0, đừng tái sử dụng.
- Style đơn giản về nội dung nhưng nặng về kỹ thuật render: phim có số liệu thật (Evidence Films) cần agent tìm nguồn dữ liệu, mày nên kiểm lại các con số.

## Đánh giá cá nhân
- Điểm mạnh: ý tưởng sạch (phim hoàn toàn bằng code, tái lập được, sửa từng khung được), có hướng dẫn đạo diễn chi tiết thay vì chỉ ném prompt, hỗ trợ "phong cách riêng" lưu lại dùng sau, giấy phép rộng, cài như plugin chính thống.
- Điểm yếu: phụ thuộc Opus 5.5, chậm và tốn token, cần ffmpeg 7+ và Chromium, tao chưa render thử nên chưa biết thực tế đẹp tới đâu, không hợp làm video nhanh số lượng lớn.
- Có nên dùng không: 7/10 để làm vài video thương hiệu có chất riêng (ABTRIP, Tano) khi mày có Opus và thời gian. 3/10 nếu cần cỗ máy đẻ video hằng ngày cho TikTok.

## Link
- Repo: https://github.com/lemomo-ai/lemo-opuscar
- Gallery: https://lemomo-ai.github.io/lemo-opuscar/
- Tác giả: Lemomo (@lemomo_ai)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes không chạy được skill này (cần Claude Code + Opus). Hermes chỉ nên KIỂM tình trạng thư viện
# và đọc danh sách phong cách để gợi ý cho Claude Code, bằng urllib.
import json, urllib.request

RAW = "https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/main/styles/{slug}/style.json"

def style_info(slug):
    with urllib.request.urlopen(RAW.format(slug=slug), timeout=20) as r:
        d = json.loads(r.read())
    return {k: d.get(k) for k in ("en", "cn", "film", "line", "uses", "dur")}

# style_info("watercolor") -> {"en": "Watercolor Brush", ..., "uses": ["Nature documentary", ...]}
```
> ⚠️ Đoạn trên tao chưa chạy với mạng thật (chỉ đọc cấu trúc `style.json` từ bản clone). Việc render phim đi qua Claude Code, không qua Hermes.

### OpenClaw
```bash
# Nhờ OpenClaw (hoặc mày) mở Claude Code trên máy dev có Opus, rồi:
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

### Antigravity
```bash
# Chuẩn bị máy render (cần ffmpeg 7+; Ubuntu 24.04 mặc định là 6.1 nên dùng bản static)
node --version && python3 --version && ffmpeg -version | head -1
sh ~/lemo-opuscar/plugin/skills/lemo-opuscar/scripts/setup.sh deps
```
> ⚠️ Render nặng CPU và chạy lâu. Đừng chạy trên VPS nhỏ. Dùng máy dev, hoặc giao qua hộp thư với `risk: medium`.
