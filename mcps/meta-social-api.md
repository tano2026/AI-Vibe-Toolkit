# Meta Graph API — Facebook, Instagram, Threads

## TL;DR
Official Meta API — post content lên FB/IG/Threads, lấy insights, quản lý comment. 1 access token dùng được cho cả 3 platform. Hermes gọi thẳng REST API, không cần SDK.

## Dùng để làm gì
- **Facebook:** Post text/ảnh/video lên Page, lấy Page insights, reply comment
- **Instagram:** Post feed, Reels, Stories, lấy metrics, media insights
- **Threads:** Post text/ảnh, get replies, delete post
- **Cross-platform:** Schedule post, bulk publish, lấy audience demographics

## Setup từng bước

1. Vào [developers.facebook.com](https://developers.facebook.com) → Create App
2. Chọn loại: **Business**
3. Add products: **Instagram Graph API** + **Facebook Pages API**
4. Lấy **Page Access Token** (long-lived, 60 ngày hoặc vĩnh viễn nếu dùng System User)
5. Verify domain nếu cần

```
Cần có:
- Facebook Page (không phải profile)
- Instagram Business/Creator account (link với FB Page)
- App với permissions: pages_manage_posts, instagram_basic, instagram_content_publish
```

## Ví dụ thực tế

Post video Reels lên IG cho ABTRIP, đồng thời đăng FB:
```python
# 1. Upload video container
container_id = ig_create_video_container(
    ig_user_id="123456789",
    video_url="https://cdn.example.com/abtrip_hue.mp4",
    caption="Tour Huế 3N2Đ chỉ 2 triệu 🌸 #ABTRIP #dulich",
    access_token=os.environ["META_ACCESS_TOKEN"]
)
# 2. Publish khi xử lý xong
ig_publish_container(container_id, ig_user_id, access_token)
# → Post live trên Instagram
```

## Lưu ý / Lỗi thường gặp
- **Token hết hạn:** Short-lived 1h, long-lived 60 ngày — dùng System User Token cho production
- **IG Reels cần video URL public:** Host video trên CDN/S3 trước rồi mới publish
- **Rate limit:** 200 calls/hour/user — đủ cho automation thông thường
- **Threads API:** Mới ra 2024, còn hạn chế — cần apply access
- **Stories:** Hết hạn sau 24h, không lấy lại được insights dài hạn

## Đánh giá cá nhân
- Điểm mạnh: 1 API cho 3 platform, stable, documentation tốt
- Điểm yếu: Token management phức tạp, hay thay đổi permissions policy
- Có nên dùng không: 9/10 — Bắt buộc cho agency làm social media

## Link
- Docs: https://developers.facebook.com/docs/graph-api
- IG API: https://developers.facebook.com/docs/instagram-api
- Threads API: https://developers.facebook.com/docs/threads
- Token debug: https://developers.facebook.com/tools/debug/accesstoken

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json, os
from urllib.parse import urlencode

BASE = "https://graph.facebook.com/v19.0"
TOKEN = os.environ.get("META_ACCESS_TOKEN", "")

# ── FACEBOOK PAGE ──

def fb_post_text(page_id, message, token=TOKEN):
    payload = urlencode({"message": message, "access_token": token}).encode()
    req = urllib.request.Request(
        f"{BASE}/{page_id}/feed", data=payload, method="POST")
    return json.loads(urllib.request.urlopen(req).read())

def fb_post_photo(page_id, image_url, caption, token=TOKEN):
    payload = urlencode({
        "url": image_url, "caption": caption, "access_token": token
    }).encode()
    req = urllib.request.Request(
        f"{BASE}/{page_id}/photos", data=payload, method="POST")
    return json.loads(urllib.request.urlopen(req).read())

def fb_post_video(page_id, video_url, title, description, token=TOKEN):
    payload = urlencode({
        "file_url": video_url, "title": title,
        "description": description, "access_token": token
    }).encode()
    req = urllib.request.Request(
        f"{BASE}/{page_id}/videos", data=payload, method="POST")
    return json.loads(urllib.request.urlopen(req).read())

def fb_page_insights(page_id, metrics, period="day", token=TOKEN):
    params = urlencode({
        "metric": metrics, "period": period, "access_token": token
    })
    req = urllib.request.Request(f"{BASE}/{page_id}/insights?{params}")
    return json.loads(urllib.request.urlopen(req).read())["data"]

# ── INSTAGRAM ──

def ig_post_photo(ig_user_id, image_url, caption, token=TOKEN):
    # Step 1: Create container
    payload = urlencode({
        "image_url": image_url, "caption": caption, "access_token": token
    }).encode()
    req = urllib.request.Request(
        f"{BASE}/{ig_user_id}/media", data=payload, method="POST")
    container_id = json.loads(urllib.request.urlopen(req).read())["id"]
    # Step 2: Publish
    payload2 = urlencode({
        "creation_id": container_id, "access_token": token
    }).encode()
    req2 = urllib.request.Request(
        f"{BASE}/{ig_user_id}/media_publish", data=payload2, method="POST")
    return json.loads(urllib.request.urlopen(req2).read())

def ig_post_reel(ig_user_id, video_url, caption, token=TOKEN):
    # Step 1: Create video container
    payload = urlencode({
        "media_type": "REELS", "video_url": video_url,
        "caption": caption, "share_to_feed": "true", "access_token": token
    }).encode()
    req = urllib.request.Request(
        f"{BASE}/{ig_user_id}/media", data=payload, method="POST")
    container_id = json.loads(urllib.request.urlopen(req).read())["id"]
    # Step 2: Wait for processing (poll status)
    import time
    for _ in range(10):
        time.sleep(5)
        status_req = urllib.request.Request(
            f"{BASE}/{container_id}?fields=status_code&access_token={token}")
        status = json.loads(urllib.request.urlopen(status_req).read())
        if status.get("status_code") == "FINISHED":
            break
    # Step 3: Publish
    payload3 = urlencode({
        "creation_id": container_id, "access_token": token
    }).encode()
    req3 = urllib.request.Request(
        f"{BASE}/{ig_user_id}/media_publish", data=payload3, method="POST")
    return json.loads(urllib.request.urlopen(req3).read())

def ig_media_insights(media_id, metrics="impressions,reach,likes,comments,shares", token=TOKEN):
    params = urlencode({"metric": metrics, "access_token": token})
    req = urllib.request.Request(f"{BASE}/{media_id}/insights?{params}")
    return json.loads(urllib.request.urlopen(req).read())["data"]

def ig_get_comments(media_id, token=TOKEN):
    params = urlencode({"fields": "text,username,timestamp", "access_token": token})
    req = urllib.request.Request(f"{BASE}/{media_id}/comments?{params}")
    return json.loads(urllib.request.urlopen(req).read()).get("data", [])

# ── THREADS ──

def threads_post(user_id, text, media_type="TEXT", image_url=None, token=TOKEN):
    # Step 1: Create container
    data = {"media_type": media_type, "text": text, "access_token": token}
    if image_url:
        data["image_url"] = image_url
        data["media_type"] = "IMAGE"
    payload = urlencode(data).encode()
    req = urllib.request.Request(
        f"{BASE}/{user_id}/threads", data=payload, method="POST")
    container_id = json.loads(urllib.request.urlopen(req).read())["id"]
    # Step 2: Publish
    payload2 = urlencode({"creation_id": container_id, "access_token": token}).encode()
    req2 = urllib.request.Request(
        f"{BASE}/{user_id}/threads_publish", data=payload2, method="POST")
    return json.loads(urllib.request.urlopen(req2).read())

def threads_get_replies(thread_id, token=TOKEN):
    params = urlencode({"fields": "text,username,timestamp", "access_token": token})
    req = urllib.request.Request(f"{BASE}/{thread_id}/replies?{params}")
    return json.loads(urllib.request.urlopen(req).read()).get("data", [])

# ENV VARS CẦN:
# META_ACCESS_TOKEN — Page Access Token (long-lived)
# META_PAGE_ID      — Facebook Page ID
# META_IG_USER_ID   — Instagram Business Account ID
# META_THREADS_USER_ID — Threads User ID (thường = IG User ID)
```

### OpenClaw
```bash
npx -y meta-mcp-server
# Set: META_ACCESS_TOKEN, META_PAGE_ID, META_IG_USER_ID
```

### Antigravity
```bash
# Không cần cài gì thêm — Hermes dùng urllib thuần
# Chỉ cần set env vars:
echo "META_ACCESS_TOKEN=xxx" >> ~/.hermes/.env
echo "META_PAGE_ID=xxx" >> ~/.hermes/.env
echo "META_IG_USER_ID=xxx" >> ~/.hermes/.env
echo "META_THREADS_USER_ID=xxx" >> ~/.hermes/.env

# Lấy long-lived token (60 ngày):
# curl "https://graph.facebook.com/v19.0/oauth/access_token
#   ?grant_type=fb_exchange_token
#   &client_id={APP_ID}
#   &client_secret={APP_SECRET}
#   &fb_exchange_token={SHORT_LIVED_TOKEN}"
```
> ⚠️ Token hết hạn sau 60 ngày. Set cron job refresh token hoặc dùng System User Token vĩnh viễn.
