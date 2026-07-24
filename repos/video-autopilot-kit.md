# video-autopilot-kit — GitHub Repo

## TL;DR
Bộ khung (không phải sản phẩm đóng gói) để tự động hoá làm video YouTube/short-form: vừa có pipeline thuần code (ffmpeg + Python, chạy được trên Mac/Linux/Windows), vừa có nhánh tự động hoá CapCut Desktop (chỉnh draft JSON trực tiếp) cho ai cần hiệu ứng/chữ động của CapCut. 1.5k+ sao, MIT license.

## Repo này dùng để làm gì
Khác với đa số "creator system" bán sẵn setup của 1 người (Nobitano rập khuôn theo không match kênh mình), repo này cho cái khung rỗng — `SETUP.md` hỏi từng câu về kênh của mày (voice, chiến lược, số liệu cộng đồng), mày trả lời để điền vào, tự nó thành hệ thống riêng. Không dính data cá nhân của tác giả gốc.

Có 2 nhánh ngang hàng, không phải chính/phụ:
- **Path 1 — Programmatic** (khuyến nghị mặc định): `longform_maker` (video dài, Ken Burns sub-pixel, bloom 2 lớp, light sweep, phụ đề theo từng chữ), `silent_vlog_maker` (Shorts dọc, phụ đề nhiều màu, chuẩn hoá âm thanh), cộng bộ QA cơ khí trước khi xuất (kiểm tra nhấp nháy, khoảng chết, đồng bộ caption — chạy thuần ffmpeg/Python, không cần CapCut). Chạy được Win/Mac/Linux.
- **Path 2 — CapCut-assisted**: sửa thẳng file JSON draft của CapCut Desktop (mute 4 cấp độ, chèn chữ động, sửa phụ đề AI) + dùng Computer Use điều khiển cửa sổ CapCut để áp template/export. Ưu tiên Windows, nhạy version CapCut nên phải theo dõi `TROUBLESHOOTING.md`.

Kèm 1 thư mục `knowledge/` — hơn 100 mục "M1-M106" đúc kết kinh nghiệm thực chiến (tránh bẫy kỹ thuật, thuật toán, SOP dựng phim).

## Setup từng bước
1. Clone repo, cần Python 3.9+ và `ffmpeg`/`ffprobe` (chỉ example 01 cần ffmpeg thật).
2. Chạy demo tự chứa để xem pipeline hoạt động thật, không cần CapCut hay footage thật:
   ```bash
   python examples/01_vertical_short.py       # ghép asset giả -> Short dọc 1080x1920 hoàn chỉnh
   python examples/02_caption_broll_match.py  # test tự động khớp b-roll theo tên file, zero config
   ```
3. Copy `config.example.py` -> `config.py`, điền path thật của máy mày (file mẫu không chứa tên tài khoản nào).
4. Mở `SETUP.md`, trả lời từng mục về voice/brand/thuật toán/cộng đồng của kênh mày — hệ thống tự điền theo câu trả lời.
5. Nếu cần hiệu ứng CapCut (Path 2): đọc `TROUBLESHOOTING.md` trước để check ma trận tương thích version CapCut, vì nhánh này cực nhạy version.

## Ví dụ thực tế
Áp cho kênh "Airfare Decoded" (aviation niche, đang dùng HyperFrames): thay vì build lại toàn bộ Ken Burns/bloom engine như Nobitano đã tự làm trong HyperFrames, có thể dùng thẳng `longform_maker` của kit này cho các đoạn giải thích dài (GDS/Amadeus explainer), rồi dùng bộ `delivery_qa` để tự động quét lỗi nhấp nháy/khoảng chết trước khi xuất — đỡ phải tự viết script kiểm tra riêng như đang làm.

## Lưu ý / Lỗi thường gặp
- Path 2 (CapCut) chỉ test thật trên Windows; trên Mac phần tự động hoá GUI (Computer Use) KHÔNG chạy được vì CapCut Mac không có AppleScript dictionary.
- Tự động sửa draft JSON của CapCut rất nhạy version app — cập nhật CapCut mà không check `TROUBLESHOOTING.md` trước dễ hỏng draft.
- Đây là khung để mày TỰ điền, không phải plug-and-play có sẵn voice/strategy — cần bỏ thời gian trả lời `SETUP.md` mới ra giá trị thật.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc 2 nhánh rõ ràng, có bộ QA cơ khí trước khi xuất (hiếm repo tự động hoá video nào làm kỹ phần này), knowledge base 100+ mục thực chiến rất đáng đọc dù không dùng code.
- Điểm yếu: đây là framework cần tự cấu hình, không phải tool chạy ngay; nhánh CapCut nhạy version, dễ gãy khi CapCut update; tài liệu phần lớn tiếng Trung (cần README.en / SETUP.en để đọc bản tiếng Anh).
- Có nên dùng: 7/10 — hợp nếu Nobitano muốn tham khảo kiến trúc QA gate + knowledge base để bổ sung cho HyperFrames pipeline hiện có, không hợp nếu muốn 1 tool cắm là chạy ngay.

## Link
- Repo: https://github.com/Hao0321/video-autopilot-kit
- Setup guide (EN): https://github.com/Hao0321/video-autopilot-kit/blob/main/SETUP.en.md
- Troubleshooting: https://github.com/Hao0321/video-autopilot-kit/blob/main/TROUBLESHOOTING.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Chạy demo tự kiểm tra pipeline hoạt động (không cần API ngoài, chỉ cần ffmpeg cài sẵn trên VPS)
import subprocess

def run_autopilot_demo(repo_path="/opt/video-autopilot-kit"):
    result = subprocess.run(
        ["python3", "examples/01_vertical_short.py"],
        cwd=repo_path, capture_output=True, text=True
    )
    return result.stdout, result.returncode
```

### OpenClaw
```bash
git clone https://github.com/Hao0321/video-autopilot-kit.git
cd video-autopilot-kit && pip install -r requirements.txt
# Điền config.py + SETUP.md thủ công 1 lần, sau đó OpenClaw gọi module qua Hermes
```

### Antigravity
```bash
# Cần ffmpeg + ffprobe trên VPS (đã có sẵn cho HyperFrames)
apt-get install -y ffmpeg
```
> ⚠️ Đây là framework để tự điền cấu hình (SETUP.md), không phải service chạy nền — không set cron cho tới khi đã điền xong config thật.
