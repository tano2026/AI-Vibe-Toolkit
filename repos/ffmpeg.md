# FFmpeg — GitHub Repo (mirror)

## TL;DR
Bộ công cụ xử lý audio/video/phụ đề nền tảng của gần như mọi phần mềm dựng video: cắt, ghép, đổi định dạng, đổi khung hình, tách tiếng, nén. Chạy bằng dòng lệnh (`ffmpeg`, `ffprobe`, `ffplay`). Repo GitHub chỉ là **bản mirror**, không nhận pull request. License chính LGPL, một số thành phần GPL. Mày không "học xong" ffmpeg, mày chỉ cần vài công thức lệnh, và agent gọi được hết.

## Repo này dùng để làm gì
- **Đổi khung hình:** video ngang thành dọc 1080x1920 cho Reels/TikTok.
- **Ghép:** đè audio voiceover lên video, nối nhiều clip.
- **Tách:** lấy riêng tiếng ra file WAV để phiên âm (xem `repos/whisper.md`).
- **Nén:** giảm dung lượng để upload nhanh.
- **Kiểm:** `ffprobe` đọc độ phân giải, thời lượng, codec để agent tự kiểm file trước khi đăng.

Gần như mọi tool trong kho dựng video (Remotion, Hyperframes, các script render) đều gọi ffmpeg ở bên dưới.

## Số liệu đã kiểm (2026-10-10)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao (mirror GitHub) | ~63,3k | 📖 trang repo qua fetch, chưa đối chiếu bằng API |
| Fork | ~14,1k | 📖 cùng nguồn |
| License | Chủ yếu LGPL, thành phần tuỳ chọn GPL (có file GPL-2.0/3.0, LGPL-2.1/3.0) | 📖 README repo |
| Nguồn chính thức | `git.ffmpeg.org`, GitHub chỉ mirror | 📖 README repo |
| Bản đã chạy thử | ffmpeg 6.1.1 (Ubuntu) | ✅ `ffmpeg -version` trong sandbox |
| Release trên GitHub | không hiện | 📖 trang repo |
| Commit gần nhất | **chưa đo** | ❓ |

Lưu ý: tên "FFmpeg" khớp nhiều repo bọc (wrapper, GUI). Entry này chỉ nói về dự án gốc.

## Setup
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y ffmpeg
# macOS
brew install ffmpeg

ffmpeg -version
```
Các lệnh dưới đây **đã chạy thật** trong sandbox (ffmpeg 6.1.1, ✅ 2026-10-10), dùng video test tạo bằng `testsrc`:

```bash
# 1. Video ngang thành dọc 1080x1920 (cắt giữa, giữ tỉ lệ) ✅
ffmpeg -y -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" \
  -c:v libx264 -crf 23 -c:a aac out.mp4

# 2. Tách audio mono 16kHz để phiên âm ✅
ffmpeg -y -i in.mp4 -vn -ac 1 -ar 16000 audio.wav

# 3. Kiểm kích thước video ✅
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 out.mp4
```
Kết quả đo được: file ra `1080,1920`; audio `16000,1` (16kHz, 1 kênh).

Ghép voiceover lên video (❓ chưa chạy, công thức quen thuộc):
```bash
ffmpeg -y -i video.mp4 -i voice.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -shortest final.mp4
```

## ⚠️ License / Bảo mật / Quyền riêng tư
- LGPL cho phần lõi, một số encoder (ví dụ libx264) kéo theo GPL tuỳ cách build. ❓ Tao chưa kiểm build trong sandbox có bật GPL không. Nếu nhúng ffmpeg vào sản phẩm bán ra, phải đọc kỹ điều kiện license.
- Chạy local, file không rời máy.
- Không bao giờ ghép lệnh ffmpeg từ chuỗi do người dùng nhập mà không kiểm đường dẫn, dễ bị chèn tham số.

## Ví dụ thực tế
1. **Video ngang YouTube thành Reels/TikTok:** công thức số 1 ở trên.
2. **Voiceover từ ElevenLabs lên video dựng bằng Remotion:** ghép bằng lệnh ghép ở trên.
3. **Kiểm trước khi đăng:** `ffprobe` đọc kích thước và thời lượng, agent tự chặn nếu video dài quá 60 giây hoặc sai tỉ lệ.

## Lưu ý / Lỗi thường gặp
- Cú pháp lệnh dài và dễ sai thứ tự tham số. Tham số đầu vào (`-i`) và đầu ra đặt sai chỗ cho kết quả khác hẳn.
- Thiếu `-y` thì ffmpeg dừng hỏi ghi đè, agent chạy tự động sẽ treo.
- Cắt crop giữa có thể mất chữ ở mép. Video có chữ phải kiểm bằng mắt.
- GitHub PR bị bỏ qua, muốn báo lỗi hay vá phải đi qua mailing list.

## Đánh giá cá nhân
**9/10 là hạ tầng, không phải tính năng.** Điểm mạnh: ổn định, miễn phí, mọi thứ trong dựng video đều dựa vào nó, agent gọi qua subprocess rất dễ. Điểm yếu: cú pháp khó nhớ, thông báo lỗi khó đọc, license cần chú ý khi đóng gói bán. Điểm này tao chấm theo độ phổ biến và 3 lệnh đã chạy thật, không phải theo kiểm thử toàn diện.

## Link
- Mirror GitHub: https://github.com/FFmpeg/FFmpeg
- Nguồn chính thức: https://git.ffmpeg.org/ffmpeg.git
- Liên quan trong kho: `repos/whisper.md`, `repos/elevenlabs-skills.md`, `repos/remotion.md`, `repos/hyperframes.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# ✅ Hai lệnh crop_vertical và probe_size đã chạy thật 2026-10-10 (ffmpeg 6.1.1).
import subprocess

def crop_vertical(src: str, dst: str):
    """Ngang -> dọc 1080x1920, giữ tỉ lệ rồi cắt giữa."""
    subprocess.run(
        ["ffmpeg", "-y", "-i", src,
         "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
         "-c:v", "libx264", "-crf", "23", "-c:a", "aac", dst],
        check=True,
    )

def probe_size(path: str) -> tuple[int, int]:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    w, h = out.split(",")
    return int(w), int(h)

# assert probe_size("out.mp4") == (1080, 1920)   # dùng làm cổng kiểm trước khi đăng
```
> Truyền tham số dạng **list** (như trên), không ghép chuỗi `shell=True`, để chặn chèn lệnh.

### OpenClaw
```bash
ffmpeg -y -i in.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" out.mp4
```

### Antigravity
```bash
sudo apt install -y ffmpeg
ffmpeg -version | head -1
```
> ⚠️ Render video ăn CPU lâu. Chạy nền, đặt giới hạn thời gian và dung lượng đĩa trống trước khi cho agent chạy hàng loạt.
