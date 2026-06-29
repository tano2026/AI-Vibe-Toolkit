# ResearchTikPy — TikTok Research API Wrapper

## TL;DR
45 stars — Python wrapper cho TikTok Research API chính thức. Lấy được dữ liệu lớn: top videos theo hashtag/keyword, user info, comment threads, follower list. Cần apply access từ TikTok (dành cho researcher/business).

## Dùng để làm gì
- Research trending videos theo keyword/hashtag
- Phân tích competitor: top videos, engagement rate, audience
- Monitor brand mentions trên TikTok
- Lấy dữ liệu analytics lớn để báo cáo cho client agency
- Track trend trước khi sản xuất content

## Setup từng bước

```bash
pip install ResearchTikPy

# Cần apply TikTok Research API access:
# developers.tiktok.com → Research API → Apply
# Sau khi approve: lấy Client Key + Client Secret
```

## Ví dụ thực tế

Research top videos về "AI tools" trên TikTok để báo cáo cho client:
```python
videos = tiktok_research_videos(
    query="AI tools",
    start_date="20260601",
    end_date="20260629",
    max_count=100
)
# → list 100 videos: views, likes, shares, creator info, caption
# Hermes phân tích → report trend → gửi Telegram cho Nobitano
```

## Lưu ý / Lỗi thường gặp
- **Apply access:** Cần điền form, nêu rõ mục đích research — business OK
- **Rate limit:** 1000 requests/day, mỗi request max 100 videos
- **Date range:** Tối đa 30 ngày/query
- **Khác với Content Posting API:** Research API chỉ đọc, không upload được

## Đánh giá cá nhân
- Điểm mạnh: Official data, không bị ban, data chất lượng cao
- Điểm yếu: Cần apply (mất 1-2 tuần), rate limit vừa phải
- Có nên dùng không: 8/10 — Bắt buộc cho agency cần báo cáo TikTok analytics

## Link
- Repo: https://github.com/HohnerJulian/ResearchTikPy
- TikTok Research API: https://developers.tiktok.com/products/research-api
- PyPI: https://pypi.org/project/ResearchTikPy

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# pip install ResearchTikPy (Antigravity cài trước)
import os
from researchtikpy import TikTokResearchAPI

CLIENT_KEY = os.environ.get("TIKTOK_CLIENT_KEY")
CLIENT_SECRET = os.environ.get("TIKTOK_CLIENT_SECRET")

def get_client():
    return TikTokResearchAPI(CLIENT_KEY, CLIENT_SECRET)

# ── SEARCH VIDEOS THEO KEYWORD ──
def tiktok_research_videos(query, start_date, end_date, max_count=100):
    client = get_client()
    results = client.query_videos(
        query={"and": [{"operation": "EQ", "field_name": "keyword",
                        "field_values": [query]}]},
        start_date=start_date,
        end_date=end_date,
        max_count=max_count,
        fields=["id","video_description","create_time","region_code",
                "share_count","view_count","like_count","comment_count",
                "music_id","hashtag_names","username","voice_to_text"]
    )
    return results

# ── TOP HASHTAG VIDEOS ──
def tiktok_hashtag_videos(hashtag, start_date, end_date, max_count=50):
    client = get_client()
    return client.query_videos(
        query={"and": [{"operation": "EQ", "field_name": "hashtag_name",
                        "field_values": [hashtag]}]},
        start_date=start_date,
        end_date=end_date,
        max_count=max_count,
        fields=["id","video_description","view_count","like_count",
                "share_count","comment_count","username","create_time"]
    )

# ── USER INFO ──
def tiktok_user_info_research(username):
    client = get_client()
    return client.query_users(
        query={"and": [{"operation": "EQ", "field_name": "username",
                        "field_values": [username]}]},
        fields=["display_name","bio_description","avatar_url","is_verified",
                "follower_count","following_count","likes_count","video_count"]
    )

# ── COMMENTS TRÊN VIDEO ──
def tiktok_video_comments(video_id, max_count=100):
    client = get_client()
    return client.query_comments(
        video_id=video_id,
        max_count=max_count,
        fields=["text","like_count","reply_count","parent_comment_id",
                "create_time","username"]
    )

# Workflow research cho agency client:
# 1. videos = tiktok_research_videos("tên brand client", "20260601", "20260629")
# 2. Hermes phân tích: top videos, engagement, trending themes
# 3. Tổng hợp report → gửi Telegram

# ENV VARS CẦN:
# TIKTOK_CLIENT_KEY    — Research API Client Key
# TIKTOK_CLIENT_SECRET — Research API Client Secret
```

### OpenClaw
```bash
# Giao Hermes xử lý — Python task
```

### Antigravity
```bash
pip install ResearchTikPy
# Verify:
python3 -c "from researchtikpy import TikTokResearchAPI; print('OK')"

# Set env:
echo "TIKTOK_CLIENT_KEY=xxx" >> ~/.hermes/.env
echo "TIKTOK_CLIENT_SECRET=xxx" >> ~/.hermes/.env
```
> ⚠️ Cần apply TikTok Research API access trước. Khác với Content Posting API — cần key riêng.
