# yt-dlp — Download & Extract Info Mọi Platform

## TL;DR
174k stars — downloader video/audio mạnh nhất hiện tại. Hỗ trợ 1000+ website: YouTube, TikTok, Instagram, Facebook, Twitter/X, Twitch... Hermes dùng để extract metadata, download video để xử lý tiếp, research competitor content.

## Dùng để làm gì
- Download video/audio từ mọi platform về VPS để xử lý
- Extract metadata: title, description, tags, view count, duration, subtitles
- Download subtitles/transcript để phân tích content
- Monitor competitor channels — track video mới
- Research trending content trước khi sản xuất

## Setup từng bước

```bash
pip install yt-dlp
# Kiểm tra:
yt-dlp --version
```

## Ví dụ thực tế

Research top 10 video về "AI tools Vietnam" trên YouTube:
```python
videos = ytdlp_search("AI tools Vietnam", max_results=10)
# → list metadata: title, views, duration, channel, upload_date
# → Hermes phân tích → báo Nobitano trend đang hot
```

Download video TikTok competitor để phân tích hook:
```python
info = ytdlp_extract_info("https://tiktok.com/@competitor/video/xxx")
# → title, duration, view_count, description, subtitles
```

## Lưu ý / Lỗi thường gặp
- **Cookies:** Một số video private/age-restricted cần cookies từ browser
- **Rate limit:** YouTube hay block IP nếu download quá nhiều — dùng `--sleep-interval`
- **Format:** Mặc định download quality tốt nhất — chỉ định format nếu cần nhẹ hơn
- **Update thường xuyên:** `pip install -U yt-dlp` — platforms hay thay đổi

## Đánh giá cá nhân
- Điểm mạnh: Hỗ trợ 1000+ sites, cực kỳ stable, update liên tục, cộng đồng lớn
- Điểm yếu: Không phải official API — có thể bị break khi platform update
- Có nên dùng không: 10/10 — Must-have cho bất kỳ content research workflow nào

## Link
- Repo: https://github.com/yt-dlp/yt-dlp
- Docs: https://github.com/yt-dlp/yt-dlp#readme
- Supported sites: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json, os

# ── EXTRACT METADATA (không download) ──
def ytdlp_extract_info(url, cookies_file=None):
    cmd = ["yt-dlp", "--dump-json", "--no-download", url]
    if cookies_file:
        cmd += ["--cookies", cookies_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"yt-dlp error: {result.stderr}")
    return json.loads(result.stdout)

# ── SEARCH YOUTUBE ──
def ytdlp_search(query, max_results=10, extract_flat=True):
    cmd = [
        "yt-dlp",
        f"ytsearch{max_results}:{query}",
        "--dump-json", "--no-download",
        "--flat-playlist" if extract_flat else "--no-flat-playlist"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    videos = []
    for line in result.stdout.strip().split("\n"):
        if line:
            try:
                videos.append(json.loads(line))
            except:
                pass
    return [{"title": v.get("title"), "url": v.get("url") or f"https://youtube.com/watch?v={v.get('id')}",
             "duration": v.get("duration"), "view_count": v.get("view_count"),
             "channel": v.get("channel") or v.get("uploader"),
             "upload_date": v.get("upload_date")} for v in videos]

# ── DOWNLOAD VIDEO ──
def ytdlp_download(url, output_dir="/tmp/videos", format="mp4",
                   max_height=1080, cookies_file=None):
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "yt-dlp", url,
        "-o", f"{output_dir}/%(title)s.%(ext)s",
        "--format", f"bestvideo[height<={max_height}][ext={format}]+bestaudio/best[ext={format}]/best",
        "--merge-output-format", format
    ]
    if cookies_file:
        cmd += ["--cookies", cookies_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

# ── DOWNLOAD SUBTITLES/TRANSCRIPT ──
def ytdlp_get_transcript(url, lang="vi", output_dir="/tmp/subs"):
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "yt-dlp", url,
        "--write-subs", "--write-auto-subs",
        "--sub-lang", lang,
        "--sub-format", "vtt",
        "--skip-download",
        "-o", f"{output_dir}/%(title)s.%(ext)s"
    ]
    subprocess.run(cmd, capture_output=True, text=True)
    # Tìm file .vtt vừa tạo
    for f in os.listdir(output_dir):
        if f.endswith(".vtt"):
            with open(f"{output_dir}/{f}") as fp:
                return fp.read()
    return None

# ── MONITOR CHANNEL (video mới nhất) ──
def ytdlp_channel_latest(channel_url, max_videos=5):
    cmd = [
        "yt-dlp", channel_url,
        "--dump-json", "--no-download",
        "--playlist-end", str(max_videos),
        "--flat-playlist"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    videos = []
    for line in result.stdout.strip().split("\n"):
        if line:
            try:
                v = json.loads(line)
                videos.append({"title": v.get("title"), "id": v.get("id"),
                               "url": f"https://youtube.com/watch?v={v.get('id')}",
                               "upload_date": v.get("upload_date")})
            except:
                pass
    return videos

# Use cases:
# info = ytdlp_extract_info("https://youtube.com/watch?v=xxx")
# videos = ytdlp_search("AI tools Vietnam 2026", max_results=10)
# ytdlp_download("https://tiktok.com/@user/video/xxx", output_dir="/tmp/videos")
# transcript = ytdlp_get_transcript("https://youtube.com/watch?v=xxx", lang="vi")
```

### OpenClaw
```bash
# Dùng qua Hermes delegate cho Python processing
# OpenClaw không cần cài trực tiếp
```

### Antigravity
```bash
pip install yt-dlp
# Update định kỳ:
pip install -U yt-dlp
# Verify:
yt-dlp --version

# Cron update hàng tuần:
# 0 3 * * 1 pip install -U yt-dlp >> /var/log/yt-dlp-update.log
```
