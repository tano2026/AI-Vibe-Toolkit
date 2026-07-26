# PyCaps — GitHub Repo

## TL;DR
Thư viện Python tạo phụ đề động, style bằng CSS, cho video TikTok/Shorts/Reels — vừa dùng CLI 1 lệnh với template có sẵn, vừa dùng như thư viện Python để tự custom pipeline. Chạy offline hoàn toàn (transcribe + style + render đều local).

## Repo này dùng để làm gì
Thay vì tự lo transcribe + canh timing + style phụ đề bằng tay hoặc qua CapCut, PyCaps làm hết trong 1 pipeline: nhận video → tự transcribe (Whisper local) → áp template CSS có sẵn (hoặc CSS tự viết) → render ra video có phụ đề động, hiệu ứng theo từng từ. Có thể bỏ qua bước transcribe nếu đã có transcript sẵn (từ FunASR/Whisper khác) — nhận đủ format `whisper_json`, `pycaps_json`, `srt`, `vtt`.

## Setup từng bước
1. Cài đặt (repo còn ở giai đoạn alpha, chưa lên PyPI — cài từ source):
```bash
git clone https://github.com/francozanardi/pycaps
cd pycaps
pip install -e .
```
2. Đảm bảo có FFmpeg trong PATH (bắt buộc cho mọi xử lý audio/video):
```bash
ffmpeg -version   # phải chạy được, không lỗi "command not found"
```
3. Cách nhanh nhất — dùng template có sẵn:
```bash
pycaps render --input my_video.mp4 --template minimalist
```
4. Nếu đã có transcript sẵn (vd từ FunASR), bỏ qua bước tự transcribe:
```bash
pycaps render --input my_video.mp4 --template minimalist --transcript transcript.json --transcript-format whisper_json
```
5. Custom pipeline đầy đủ bằng code (khi cần style riêng theo brand):
```python
from pycaps import CapsPipelineBuilder

pipeline = (
    CapsPipelineBuilder()
    .with_input_video("input.mp4")
    .add_css("brand_style.css")
    .build()
)
pipeline.run()
```

## Ví dụ thực tế
Ghép trực tiếp vào `agents/shorts-affiliate-system` đã có trong kho — hiện pipeline đó tự vẽ text bằng HTML/CSS scene tĩnh (`hero-text`, `terminal`...), còn phần phụ đề động cho lời thoại/voiceover thì chưa có. PyCaps lấp đúng khoảng trống này: sau khi FFmpeg merge video + voiceover xong, chạy PyCaps 1 lần nữa để phủ phụ đề động theo từng từ lên trên, dùng transcript JSON đã có sẵn (không cần tự transcribe lại).

## Lưu ý / Lỗi thường gặp
- Repo đang ở giai đoạn **rất alpha** ("very alpha stage"), tự ghi rõ trong README — chưa publish lên PyPI, API có thể đổi bất ngờ giữa các bản.
- Cần đúng Python 3.10-3.12 — bản khác "có thể gặp vấn đề" theo cảnh báo của tác giả, không đảm bảo tương thích ngược/xuôi.
- Test online demo (HuggingFace Space) chỉ chạy CPU, giới hạn video dưới 60 giây — muốn test video dài hơn phải tự cài local hoặc dùng bản Colab (có GPU free).
- Có 1 fork riêng (`MarianoFacundoArch/pycaps`) thêm `--whisper-prompt` để hint từ vựng riêng (tên brand, thuật ngữ chuyên ngành) — hữu ích nếu transcribe hay sai tên tool/brand, nhưng là fork cộng đồng, không phải bản chính.

## Đánh giá cá nhân
- Điểm mạnh: style bằng CSS thuần (không phải học 1 DSL riêng), nhận transcript có sẵn nên ghép thẳng với FunASR/pipeline khác không phải transcribe lại, chạy offline-first không lệ thuộc API ngoài.
- Điểm yếu: còn alpha, chưa lên PyPI, dễ breaking change; giới hạn Python version khá chặt.
- Có nên dùng: 7/10 — đáng ghép ngay vào `shorts-affiliate-system` để có phụ đề động, nhưng đừng phụ thuộc 100% vào nó cho production ổn định lâu dài vì còn alpha.

## Link
- Repo: https://github.com/francozanardi/pycaps
- Demo online (CPU, video <60s): xem link "Space" trong README repo
- Fork có whisper-prompt: https://github.com/MarianoFacundoArch/pycaps

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess

def add_captions(video_path, transcript_json_path, output_path, template="minimalist"):
    subprocess.run([
        "pycaps", "render",
        "--input", video_path,
        "--template", template,
        "--transcript", transcript_json_path,
        "--transcript-format", "whisper_json",
        "--output", output_path,
    ], check=True)
```

### OpenClaw
```bash
# Cài trực tiếp trên VPS (không cần GPU, chạy CPU được với video ngắn dạng Shorts)
git clone https://github.com/francozanardi/pycaps /opt/pycaps
cd /opt/pycaps && pip install -e .
```

### Antigravity
```bash
apt-get install -y ffmpeg
git clone https://github.com/francozanardi/pycaps /opt/pycaps
cd /opt/pycaps && pip install -e . --break-system-packages
```
> ⚠️ Bản alpha — pin lại đúng commit hash khi deploy production, tránh pull `main` mới nhất giữa chừng dự án làm gãy pipeline.
