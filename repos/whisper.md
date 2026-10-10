# Whisper (OpenAI) — GitHub Repo

## TL;DR
Model nhận dạng giọng nói mã nguồn mở của OpenAI: đưa file audio vào, ra văn bản (và có thể dịch sang tiếng Anh). Chạy **local**, MIT cho cả code lẫn trọng số model, hỗ trợ tiếng Việt. Cài một lệnh `pip install -U openai-whisper`, nhưng **bắt buộc có ffmpeg**. Cảnh báo lớn nhất: model xịn cần GPU nhiều VRAM, chạy CPU thì chậm, và model `turbo` mặc định **không dịch được**.

## Repo này dùng để làm gì
Biến giọng nói thành chữ mà không phải trả tiền theo phút cho dịch vụ nào:
- Phiên âm video/podcast/ghi âm cuộc gọi để lấy transcript.
- Làm phụ đề cho video ngắn (xuất file có mốc thời gian).
- Chuyển giọng nói tiếng nước ngoài thành văn bản tiếng Anh (chỉ với model đa ngôn ngữ, không phải turbo).

## Số liệu đã kiểm (2026-10-10)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao | ~109,4k | 📖 trang repo qua fetch, chưa đối chiếu bằng API |
| Fork | ~13,3k | 📖 cùng nguồn |
| License | MIT (code và trọng số model) | 📖 trang repo |
| Tiếng Việt | Có (`"vi": "vietnamese"` trong danh sách ngôn ngữ) | ✅ đọc `whisper/tokenizer.py` bản `main` |
| Số commit | 171 | 📖 trang repo |
| Commit gần nhất | **chưa đo** (trang không hiện ngày) | ❓ |

Bảng model (📖 README gốc, tốc độ đo trên A100 với tiếng Anh):

| Model | Tham số | VRAM cần | Tốc độ tương đối |
|---|---|---|---|
| tiny | 39M | ~1 GB | ~10x |
| base | 74M | ~1 GB | ~7x |
| small | 244M | ~2 GB | ~4x |
| medium | 769M | ~5 GB | ~2x |
| large | 1550M | ~10 GB | 1x |
| turbo | 809M | ~6 GB | ~8x |

Chất lượng tiếng Việt riêng (tỉ lệ lỗi theo ngôn ngữ) README chỉ cho dạng **biểu đồ ảnh**, tao chưa đọc được con số.

## Setup
📖 Theo README gốc, **chưa chạy** (không cài torch trong sandbox):
```bash
# 1. ffmpeg (bắt buộc)
sudo apt update && sudo apt install ffmpeg        # Ubuntu/Debian
# brew install ffmpeg                              # macOS

# 2. Cài whisper
pip install -U openai-whisper

# 3. Chạy thử
whisper audio.mp3 --model turbo
whisper audio.mp3 --model medium --language Vietnamese
```
README ghi: model `turbo` mặc định **không train cho tác vụ dịch**, muốn dịch phải dùng `medium` hoặc `large`.

Chuẩn bị audio (✅ đã chạy thật 2026-10-10 với ffmpeg 6.1.1, ra WAV mono 16kHz):
```bash
ffmpeg -y -i video.mp4 -vn -ac 1 -ar 16000 audio.wav
```

## ⚠️ License / Bảo mật / Quyền riêng tư
- MIT, dùng thương mại được theo giấy phép.
- Chạy local nên audio không rời máy. Hợp với file ghi âm có thông tin khách hàng.

## Ví dụ thực tế
1. **Phụ đề video:** lấy audio từ video bằng ffmpeg, chạy whisper ra transcript, chỉnh tay vài chỗ rồi đưa vào CapCut.
2. **Biên bản cuộc họp:** ghi âm họp, chạy `medium` với `--language Vietnamese`, rồi nhờ agent tóm tắt.
3. **Kho nội dung:** phiên âm video đối thủ hoặc podcast để nghiên cứu, thay cho gõ tay.

## Lưu ý / Lỗi thường gặp
- Không có ffmpeg thì cài xong vẫn lỗi khi đọc file audio.
- CPU-only chạy rất chậm với model lớn. Máy yếu thì dùng `small` hoặc `base`, chấp nhận sai nhiều hơn.
- ❓ Kinh nghiệm chung (chưa tự kiểm trong repo này): Whisper đôi khi "bịa" chữ ở đoạn im lặng hoặc nhạc nền. Luôn đọc soát lại transcript trước khi đăng.
- ❓ Chưa kiểm chất lượng tên riêng, tên hãng bay, mã sân bay tiếng Việt. Với nội dung hàng không cần soát kỹ.
- ❓ Chưa thử xuất file phụ đề `.srt` hay mốc thời gian từng từ. README có lệnh CLI nhưng tao chưa đọc hết tuỳ chọn.

## Đánh giá cá nhân
**8/10 cho việc phiên âm local.** Điểm mạnh: miễn phí, MIT, có tiếng Việt, chạy trên máy mình, ecosystem lớn nên dễ tìm cách xử lý lỗi. Điểm yếu: cần phần cứng ổn, không có sẵn giao diện, chất lượng tiếng Việt chưa được tao đo, và cần soát tay. Chưa chạy một lần nào trong sandbox nên điểm này là đánh giá độ trưởng thành của repo, không phải kết quả test.

## Link
- Repo: https://github.com/openai/whisper
- Bài báo: https://arxiv.org/abs/2212.04356
- Liên quan trong kho: `repos/ffmpeg.md`, `repos/elevenlabs-skills.md` (STT trả phí để so sánh)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# ❓ Chưa chạy (chưa cài whisper trong sandbox). Dùng subprocess gọi CLI, không cần import torch.
import subprocess, pathlib

def transcribe(audio: str, out_dir: str, model: str = "medium", language: str = "Vietnamese"):
    pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["whisper", audio, "--model", model, "--language", language,
         "--output_dir", out_dir, "--output_format", "txt"],
        check=True,
    )

def extract_audio(video: str, wav: str):
    # ✅ lệnh này đã chạy thật
    subprocess.run(["ffmpeg", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
```

### OpenClaw
```bash
pip install -U openai-whisper
whisper audio.mp3 --model turbo
```

### Antigravity
```bash
# Cài trên VPS (❓ chưa chạy). Kiểm RAM/GPU trước khi chọn model.
sudo apt install -y ffmpeg
pip install -U openai-whisper --break-system-packages
nvidia-smi 2>/dev/null || echo "Không có GPU, chọn model nhỏ (small/base)"
free -h
```
> ⚠️ Model lớn tải về vài GB và ăn nhiều RAM/VRAM. Kiểm dung lượng đĩa và RAM VPS trước khi cài, đừng cài thẳng `large` lên máy nhỏ.
