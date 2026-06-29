# TikTok for Developers API — Upload, Analytics, Research

## TL;DR
Official TikTok APIs gồm 3 loại: Content Posting API (upload video), Research API (analytics dữ liệu lớn), Display API (basic user info). Hermes dùng được cả 3 bằng Python thuần.

## Dùng để làm gì
- **Upload video** lên TikTok Business/Creator account tự động
- **Lấy analytics:** views, likes, shares, comments, watch time, audience demographics
- **Research trending:** top videos, hashtag analytics, creator stats (cần Research API access)
- **Quản lý comment:** list, reply (limited)

## Setup từng bước

1. Vào [developers.tiktok.com](https://developers.tiktok.com) → Create App
2. Chọn permissions:
   - `video.upload` — để upload
   - `video.list` — để list videos của account
   - `user.info.basic` — basic profile
3. Submit app review (mất 1-3 ngày)
4. Sau khi approve → lấy Client Key + Client Secret
5. OAuth flow để lấy Access Token

```bash
# Không cần cài gì — Hermes dùng urllib thuần
# Chỉ cần: TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_ACCESS_TOKEN
```

## Ví dụ thực tế

Upload video Shorts từ content factory lên TikTok:
```python
# Input: video file đã render xong
# Output: TikTok post ID
post_id = tiktok_upload_video(
    video_path="tano_ai_tools_review.mp4",
    title="5 AI tools miễn phí thay thế ChatGPT Plus #AItools #tano",
    privacy="PUBLIC_TO_EVERYONE"
)
# → TikTok post live
```

## Lưu ý / Lỗi thường gặp
- **App review:** TikTok review khá chặt, cần describe use case rõ ràng
- **Video requirements:** MP4/WebM, tối đa 4GB, 15s-10 phút
- **Research API:** Cần apply riêng, dành cho academic/research — không phải ai cũng được duyệt
- **Access Token hết hạn:** 24h, cần refresh thường xuyên hoặc dùng refresh_token
- **Rate limit:** 100 requests/day cho upload với basic tier

## Đánh giá cá nhân
- Điểm mạnh: Official, không bị ban như unofficial tools, có analytics đầy đủ
- Điểm yếu: App review chậm, rate limit thấp, API docs còn thiếu nhiều
- Có nên dùng không: 7/10 — Dùng song song với tiktokautouploader (cookies-based) để backup

## Link
- Docs: https://developers.tiktok.com/doc
- App portal: https://developers.tiktok.com
- Research API: https://developers.tiktok.com/products/research-api

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json, os
from urllib.parse import urlencode

TIKTOK_BASE = "https://open.tiktokapis.com/v2"

# ── AUTH ──
def tiktok_refresh_token(client_key, client_secret, refresh_token):
    payload = urlencode({
        "client_key": client_key,
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }).encode()
    req = urllib.request.Request(
        "https://open.tiktokapis.com/v2/oauth/token/",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["access_token"], r["refresh_token"]

def get_tiktok_token():
    return os.environ["TIKTOK_ACCESS_TOKEN"]

# ── UPLOAD VIDEO (Content Posting API) ──
def tiktok_init_upload(file_size, chunk_size=None, token=None):
    token = token or get_tiktok_token()
    payload = json.dumps({
        "post_info": {
            "title": "",  # set ở publish step
            "privacy_level": "PUBLIC_TO_EVERYONE",
            "disable_duet": False,
            "disable_comment": False,
            "disable_stitch": False
        },
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": file_size,
            "chunk_size": chunk_size or file_size,
            "total_chunk_count": 1
        }
    }).encode()
    req = urllib.request.Request(
        f"{TIKTOK_BASE}/post/publish/video/init/",
        data=payload,
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json; charset=UTF-8"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["data"]["publish_id"], r["data"]["upload_url"]

def tiktok_upload_video(video_path, title, privacy="PUBLIC_TO_EVERYONE",
                        hashtags=None, token=None):
    token = token or get_tiktok_token()
    file_size = os.path.getsize(video_path)
    publish_id, upload_url = tiktok_init_upload(file_size, token=token)
    # Upload file
    with open(video_path, "rb") as f:
        video_data = f.read()
    upload_req = urllib.request.Request(
        upload_url, data=video_data,
        headers={
            "Content-Type": "video/mp4",
            "Content-Range": f"bytes 0-{file_size-1}/{file_size}",
            "Content-Length": str(file_size)
        }, method="PUT"
    )
    urllib.request.urlopen(upload_req)
    # Add hashtags vào title
    if hashtags:
        title += " " + " ".join([f"#{h}" for h in hashtags])
    return publish_id

def tiktok_check_status(publish_id, token=None):
    token = token or get_tiktok_token()
    payload = json.dumps({"publish_id": publish_id}).encode()
    req = urllib.request.Request(
        f"{TIKTOK_BASE}/post/publish/status/fetch/",
        data=payload,
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())["data"]

# ── USER INFO & VIDEOS ──
def tiktok_user_info(token=None):
    token = token or get_tiktok_token()
    params = urlencode({"fields": "open_id,union_id,avatar_url,display_name,follower_count,following_count,video_count"})
    req = urllib.request.Request(
        f"{TIKTOK_BASE}/user/info/?{params}",
        headers={"Authorization": f"Bearer {token}"}
    )
    return json.loads(urllib.request.urlopen(req).read())["data"]["user"]

def tiktok_list_videos(max_count=20, token=None):
    token = token or get_tiktok_token()
    payload = json.dumps({
        "max_count": max_count,
        "fields": ["id","title","create_time","cover_image_url",
                   "share_url","view_count","like_count","comment_count",
                   "share_count","video_duration"]
    }).encode()
    req = urllib.request.Request(
        f"{TIKTOK_BASE}/video/list/",
        data=payload,
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())["data"]["videos"]

# ── RESEARCH API (cần apply riêng) ──
def tiktok_research_search(query, max_count=20, client_key=None, client_secret=None):
    # Lấy client access token (khác user access token)
    payload = urlencode({
        "client_key": client_key or os.environ["TIKTOK_CLIENT_KEY"],
        "client_secret": client_secret or os.environ["TIKTOK_CLIENT_SECRET"],
        "grant_type": "client_credentials"
    }).encode()
    req = urllib.request.Request(
        "https://open.tiktokapis.com/v2/oauth/token/",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    client_token = json.loads(urllib.request.urlopen(req).read())["access_token"]
    # Search videos
    search_payload = json.dumps({
        "query": {"and": [{"operation": "EQ", "field_name": "keyword",
                           "field_values": [query]}]},
        "max_count": max_count,
        "cursor": 0,
        "start_date": "20240101",
        "end_date": "20261231"
    }).encode()
    search_req = urllib.request.Request(
        "https://open.tiktokapis.com/v2/research/video/query/"
        "?fields=id,video_description,create_time,region_code,share_count,view_count,like_count",
        data=search_payload,
        headers={"Authorization": f"Bearer {client_token}",
                 "Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(search_req).read())["data"]["videos"]

# ENV VARS CẦN:
# TIKTOK_CLIENT_KEY      — App Client Key
# TIKTOK_CLIENT_SECRET   — App Client Secret
# TIKTOK_ACCESS_TOKEN    — User Access Token (refresh mỗi 24h)
# TIKTOK_REFRESH_TOKEN   — Để refresh access token
```

### OpenClaw
```bash
# Dùng tiktokautouploader (đã có trong kho) cho upload đơn giản:
# repos/tiktokautouploader.md

# Hoặc gọi API qua Hermes delegate
```

### Antigravity
```bash
# Không cần cài thêm gì — Hermes dùng urllib thuần
# Set env:
echo "TIKTOK_CLIENT_KEY=xxx" >> ~/.hermes/.env
echo "TIKTOK_CLIENT_SECRET=xxx" >> ~/.hermes/.env
echo "TIKTOK_ACCESS_TOKEN=xxx" >> ~/.hermes/.env
echo "TIKTOK_REFRESH_TOKEN=xxx" >> ~/.hermes/.env

# Setup cron refresh token mỗi 23h (token hết hạn sau 24h):
# 0 */23 * * * python3 /scripts/refresh_tiktok_token.py
```
> ⚠️ Access Token hết hạn sau 24h. Antigravity setup cron refresh token tự động.
