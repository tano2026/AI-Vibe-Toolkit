# TikTokAutoUploader — GitHub Repo

## TL;DR
Python lib upload + schedule video lên TikTok tự động, tự né captcha, tự né bot-detection (Phantomwright), không cần TikTok API chính thức. ~273⭐, đang active maintain (update tháng 4/2026).

## Repo này dùng để làm gì
Đây là bước cuối trong pipeline content tự động (Script → ElevenLabs → OBS → CapCut → Canva → TikTok): video edit xong, gọi 1 hàm Python là tự đăng lên TikTok, kèm sound trending, hashtag, lên lịch giờ đăng. Login TikTok 1 lần đầu duy nhất (lưu cookie vào file json), từ lần sau không cần login lại. Né bot detection bằng Phantomwright — bản patch của Playwright chuyên chống bị phát hiện automation (fingerprint spoofing, thao tác giống người thật).

## Setup từng bước
1. `pip install tiktokautouploader`
2. Cài Node.js (cần cho phần JS chạy ngầm — `playwright`, `playwright-extra`, `puppeteer-extra-plugin-stealth` tự install ở lần chạy đầu, chỉ cần `npm` có trong PATH)
3. `phantomwright_driver install chromium` — cài browser binary 1 lần
4. Chạy hàm upload lần đầu cho 1 account → trình duyệt tự mở, đăng nhập TikTok 1 lần → cookie lưu vào file `TK_cookies_(tênaccount).json`, lần sau không cần login lại
5. Từ lần 2 trở đi gọi hàm bình thường, không cần thao tác tay nữa

```python
from tiktokautouploader import upload_tiktok

upload_tiktok(
    video='path/to/video.mp4',
    description='Check out my latest video!',
    accountname='mytiktokaccount',
    hashtags=['#fun', '#viral']
)
```

## Ví dụ thực tế
Đăng kèm sound trending + lên lịch giờ đăng + check copyright trước khi đăng:
```python
upload_tiktok(
    video=video_path,
    description=description,
    accountname=accountname,
    sound_name='trending_sound',
    sound_aud_vol='mix',
    schedule='15:00',
    day=5,
    copyrightcheck=True
)
```

Chạy headless + stealth cho VPS không màn hình (đúng setup CentOS/RHEL của AI Vibe Toolkit):
```python
upload_tiktok(
    video=video_path,
    description=description,
    accountname=accountname,
    headless=True,
    stealth=True,
    suppressprint=True
)
```

Custom cover ảnh — TikTok âm thầm bỏ ảnh cover mình upload, luôn lấy random frame. Cách lách: ghép ảnh cover thành frame cuối video bằng ffmpeg trước, rồi truyền `cover_image=` để code tự kéo slider tới frame cuối:
```bash
ffmpeg -loop 1 -i cover.png -t 2.5 -vf "scale=1080:1920,setsar=1" -c:v libx264 -pix_fmt yuv420p cover_clip.mp4
printf "file 'main.mp4'\nfile 'cover_clip.mp4'" > concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -c copy final.mp4
```

## Lưu ý / Lỗi thường gặp
- README ghi rõ: *"Use this tool at your own risk, as automated uploading may violate TikTok's Terms of Service"* — đây không phải API chính thức, là automation qua browser giả lập (Phantomwright), không phải Content Posting API của TikTok.
- Tài liệu khuyên dùng account đã có vài tuần lịch sử hoạt động, account mới tạo dễ bị soi hơn.
- Lịch đăng tối đa 240 giờ (10 ngày) trước, và phút (`MM`) trong `schedule` phải là số chia hết cho 5, giờ đăng phải cách hiện tại ít nhất 15 phút.
- Lần chạy đầu tiên luôn chậm hơn (20-30s) vì build JS lib lần đầu, các lần sau bình thường (<20s mỗi upload, không tính `stealth=True` làm chậm thêm vài giây).
- `sound_aud_vol` hiện chỉ ổn định với giá trị default `'mix'` — README ghi rõ 2 giá trị khác (`'main'`, `'background'`) còn đang có vấn đề nhỏ tính tới bản mới nhất.

## Đánh giá cá nhân
- Điểm mạnh: setup nhanh, có sẵn trên PyPI, support schedule + hashtag + sound + proxy + multi-account + tích hợp Telegram bot báo trạng thái, đang active maintain.
- Điểm yếu: không phải API official → rủi ro ban account thật, TikTok có thể đổi UI/anti-bot bất kỳ lúc nào làm code gãy (chính README cũng tự ghi "WORKING AS OF FEB 2026" nghĩa là phải theo dõi update liên tục, không set-and-forget được mãi). Không nên gắn thẳng vào account chính ngay từ đầu.
- Có nên dùng: 7/10 — rất hợp để tự động hoá bước cuối pipeline content, nhưng bắt buộc test với account phụ trước khi đưa vào account thật của kênh.

## Link
- Repo: https://github.com/haziq-exe/TikTokAutoUploader
- Docs: https://github.com/haziq-exe/TikTokAutoUploader/blob/main/Documentation.md
- PyPI: https://pypi.org/project/tiktokautouploader/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Antigravity phải cài trước: pip install tiktok-uploader
# Cần TikTok session cookies — lấy từ browser

from tiktok_uploader.upload import upload_videos

def upload_to_tiktok(video_path, title, tags=None, cookies="cookies.txt"):
    """Upload video lên TikTok tự động"""
    videos = [{
        "path": video_path,
        "description": title + " " + " ".join([f"#{t}" for t in (tags or [])])
    }]
    upload_videos(videos=videos, cookies=cookies, headless=True)
    return f"Uploaded: {video_path}"

# Workflow content factory:
# 1. Tạo video (HyperFrames/Remotion)
# 2. Hermes gọi upload_to_tiktok() → lên TikTok tự động
# 3. Báo chủ qua Telegram

# Lấy cookies: đăng nhập TikTok trên browser → export cookies → lưu cookies.txt
```

### OpenClaw
```bash
# CLI tool — không cần npm config
```

### Antigravity
```bash
pip install tiktok-uploader
# Export cookies từ browser (dùng EditThisCookie extension):
# Chrome → TikTok đã login → Export → lưu tiktok_cookies.txt
playwright install chromium  # cần cho upload
```
> ⚠️ Đây là mảnh ghép cuối content factory: video xong → tự upload TikTok.
