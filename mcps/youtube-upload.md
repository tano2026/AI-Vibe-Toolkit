# YouTube Data API v3 — Upload, Analytics, Management

## TL;DR
Official Google API cho YouTube — upload video, lấy analytics, quản lý comment, search. Dùng được với Hermes bằng Python thuần, không cần thư viện nặng.

## Dùng để làm gì
- Upload video lên YouTube (kể cả Shorts)
- Lấy analytics: views, watch time, revenue, CTR
- Quản lý comments: list, reply, moderate
- Search video, channel, playlist
- Update metadata: title, description, tags, thumbnail

## Setup từng bước

1. Vào [console.cloud.google.com](https://console.cloud.google.com)
2. Tạo project → Enable **YouTube Data API v3**
3. Tạo **OAuth 2.0 Client ID** (loại Desktop App)
4. Download `client_secrets.json`
5. Lần đầu chạy → browser mở xin quyền → lưu `token.json` → các lần sau dùng token

```bash
pip install google-auth google-auth-oauthlib google-api-python-client
```

## Ví dụ thực tế

Upload video Shorts cho kênh ABTRIP:
```python
# Input: file video .mp4, title, description
# Output: YouTube video ID
video_id = youtube_upload(
    file_path="abtrip_tour_hue.mp4",
    title="Tour Huế 3N2Đ chỉ 2 triệu - ABTRIP",
    description="Khám phá Cố đô Huế...",
    tags=["du lịch Huế", "ABTRIP", "tour giá rẻ"],
    category_id="19",  # Travel & Events
    privacy="public"
)
# → https://youtube.com/watch?v={video_id}
```

## Lưu ý / Lỗi thường gặp
- **Quota:** 10,000 units/ngày free. Upload = 1600 units, search = 100 units
- **OAuth token hết hạn:** Dùng refresh_token để tự gia hạn, không cần login lại
- **Shorts:** video dọc < 60s tự động thành Shorts — không cần flag riêng
- **Rate limit:** Upload tối đa ~6 video/ngày với free quota
- **Thumbnail custom:** Cần verify channel trước mới upload được thumbnail

## Đánh giá cá nhân
- Điểm mạnh: Official API, stable, đầy đủ tính năng, free quota đủ dùng cho SMB
- Điểm yếu: OAuth flow phức tạp lần đầu setup, quota upload khá thấp
- Có nên dùng không: 9/10 — Bắt buộc phải có cho content factory

## Link
- Docs: https://developers.google.com/youtube/v3
- Console: https://console.cloud.google.com
- Quota calculator: https://developers.google.com/youtube/v3/determine_quota_cost

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json, os, base64
from urllib.parse import urlencode

# ── AUTH — lấy access token từ refresh token ──
def get_access_token(client_id, client_secret, refresh_token):
    payload = urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return json.loads(urllib.request.urlopen(req).read())["access_token"]

# ── UPLOAD VIDEO ──
def youtube_upload(file_path, title, description, tags, category_id="22",
                   privacy="public", client_id=None, client_secret=None, refresh_token=None):
    token = get_access_token(
        client_id or os.environ["YT_CLIENT_ID"],
        client_secret or os.environ["YT_CLIENT_SECRET"],
        refresh_token or os.environ["YT_REFRESH_TOKEN"]
    )
    # Step 1: Initiate resumable upload
    metadata = json.dumps({
        "snippet": {"title": title, "description": description,
                    "tags": tags, "categoryId": category_id},
        "status": {"privacyStatus": privacy}
    }).encode()
    init_req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos"
        "?uploadType=resumable&part=snippet,status",
        data=metadata,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Upload-Content-Type": "video/*",
            "X-Upload-Content-Length": str(os.path.getsize(file_path))
        }, method="POST"
    )
    resp = urllib.request.urlopen(init_req)
    upload_url = resp.headers["Location"]
    # Step 2: Upload file
    with open(file_path, "rb") as f:
        video_data = f.read()
    upload_req = urllib.request.Request(
        upload_url, data=video_data,
        headers={"Content-Type": "video/*",
                 "Authorization": f"Bearer {token}"},
        method="PUT"
    )
    result = json.loads(urllib.request.urlopen(upload_req).read())
    return result["id"]  # video ID

# ── GET ANALYTICS ──
def youtube_analytics(channel_id, start_date, end_date, metrics="views,estimatedMinutesWatched,likes",
                      client_id=None, client_secret=None, refresh_token=None):
    token = get_access_token(
        client_id or os.environ["YT_CLIENT_ID"],
        client_secret or os.environ["YT_CLIENT_SECRET"],
        refresh_token or os.environ["YT_REFRESH_TOKEN"]
    )
    params = urlencode({
        "ids": f"channel=={channel_id}",
        "startDate": start_date,
        "endDate": end_date,
        "metrics": metrics,
        "dimensions": "day"
    })
    req = urllib.request.Request(
        f"https://youtubeanalytics.googleapis.com/v2/reports?{params}",
        headers={"Authorization": f"Bearer {token}"}
    )
    return json.loads(urllib.request.urlopen(req).read())

# ── LIST COMMENTS ──
def youtube_comments(video_id, max_results=50, api_key=None):
    key = api_key or os.environ["YOUTUBE_API_KEY"]
    params = urlencode({
        "part": "snippet", "videoId": video_id,
        "maxResults": max_results, "order": "relevance", "key": key
    })
    req = urllib.request.Request(
        f"https://www.googleapis.com/youtube/v3/commentThreads?{params}")
    r = json.loads(urllib.request.urlopen(req).read())
    return [{"text": x["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
             "author": x["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
             "likes": x["snippet"]["topLevelComment"]["snippet"]["likeCount"]}
            for x in r.get("items", [])]

# ── SEARCH VIDEOS ──
def youtube_search(query, max_results=10, api_key=None):
    key = api_key or os.environ["YOUTUBE_API_KEY"]
    params = urlencode({"part": "snippet", "q": query,
                        "maxResults": max_results, "type": "video", "key": key})
    req = urllib.request.Request(
        f"https://www.googleapis.com/youtube/v3/search?{params}")
    r = json.loads(urllib.request.urlopen(req).read())
    return [{"title": x["snippet"]["title"],
             "videoId": x["id"]["videoId"],
             "url": f"https://youtube.com/watch?v={x['id']['videoId']}",
             "channel": x["snippet"]["channelTitle"]}
            for x in r.get("items", [])]

# ENV VARS CẦN:
# YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN (cho upload/analytics)
# YOUTUBE_API_KEY (cho search/comments — không cần OAuth)
```

### OpenClaw
```bash
# Dùng Google Workspace MCP:
npx -y @evolsb/claude-code-google-workspace
# Set: GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN
```

### Antigravity
```bash
pip install google-auth google-auth-oauthlib google-api-python-client

# Setup OAuth lần đầu (chạy trên máy có browser):
python3 << 'SETUP'
from google_auth_oauthlib.flow import InstalledAppFlow
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secrets.json",
    scopes=["https://www.googleapis.com/auth/youtube.upload",
            "https://www.googleapis.com/auth/youtube.force-ssl",
            "https://www.googleapis.com/auth/yt-analytics.readonly"]
)
creds = flow.run_local_server(port=0)
print("REFRESH_TOKEN:", creds.refresh_token)
SETUP
# Lưu refresh_token vào .env → Hermes dùng mãi mãi không cần login lại
```
> ⚠️ OAuth phải setup 1 lần trên máy có browser. Sau đó Hermes dùng refresh_token tự động.
