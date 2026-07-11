# Content Research Agent — Trùm Sân Bay

## Mô tả
Tự động crawl Facebook Groups, TikTok trending, RSS hãng bay → tổng hợp danh sách chủ đề content mỗi tuần → đưa vào Ideation queue. Mày không cần nghĩ ra chủ đề nữa.

## Trigger
- Cron: mỗi sáng T2 lúc 7h → chạy research → 8h Ideation Agent nhận kết quả
- Manual: `/tsb research` qua Telegram

## Nguồn crawl

### 1. Facebook Groups (chủ đề nóng từ cộng đồng)
Target groups:
- "Hội những người mê đi máy bay" (~500k members)
- "Kinh nghiệm du lịch Việt Nam"
- "Bay giá rẻ - Vé máy bay khuyến mãi"
- Page chính thức: Vietnam Airlines, VietJet Air, Bamboo Airways

Lấy gì: post nhiều reaction/comment nhất trong 7 ngày → extract câu hỏi, pain point, chủ đề hot

Tool: Apify Facebook Scraper (có free tier) hoặc Bright Data

### 2. TikTok (trending content)
Target hashtags:
- #sanbayvietnam #maybay #checkin #fasttrack #meodutlich
- #vietnamairlines #vietjetair

Lấy gì: video nhiều view/comment nhất tuần → extract chủ đề, comment phổ biến (câu hỏi khách hay hỏi)

Tool: TikTok Research API hoặc Apify TikTok Scraper

### 3. Nguồn chính thống (tin tức + quy định mới)
RSS feeds:
- Vietnam Airlines: https://www.vietnamairlines.com/rss
- VietJet: https://www.vietjetair.com/rss
- Bamboo: https://www.bambooairways.com/rss
- Cục Hàng không VN: https://caa.gov.vn/rss
- IATA News: https://www.iata.org/en/pressroom/rss/

Lấy gì: thay đổi quy định, chính sách mới, thông báo quan trọng → content cảnh báo kịp thời

## Code Hermes — Research Pipeline

```python
import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import os
from datetime import datetime, timedelta

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
APIFY_TOKEN = os.environ.get("APIFY_TOKEN")  # free tier đủ dùng

def fetch_rss(url):
    """Fetch RSS feed từ hãng bay / cục hàng không"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(req, timeout=15).read()
        root = ET.fromstring(raw)
        items = []
        for item in root.findall('.//item')[:10]:
            title = item.findtext('title', '')
            desc = item.findtext('description', '')
            pub = item.findtext('pubDate', '')
            items.append({"title": title, "description": desc[:200], "published": pub})
        return items
    except Exception as e:
        return []

def fetch_tiktok_trending(hashtags):
    """
    Dùng Apify TikTok Hashtag Scraper (free tier: 100 results/run)
    https://apify.com/clockworks/tiktok-hashtag-scraper
    """
    results = []
    for tag in hashtags:
        url = "https://api.apify.com/v2/acts/clockworks~tiktok-hashtag-scraper/run-sync-get-dataset-items"
        payload = {
            "hashtags": [tag],
            "resultsPerPage": 20,
            "shouldDownloadVideos": False,
            "shouldDownloadCovers": False
        }
        req = urllib.request.Request(
            f"{url}?token={APIFY_TOKEN}",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=60).read())
            for item in data[:10]:
                results.append({
                    "source": "tiktok",
                    "hashtag": tag,
                    "desc": item.get("text", "")[:200],
                    "views": item.get("playCount", 0),
                    "comments": item.get("commentCount", 0),
                    "likes": item.get("diggCount", 0)
                })
        except Exception:
            pass
    # Sort by views
    return sorted(results, key=lambda x: x["views"], reverse=True)

def fetch_facebook_group_topics(group_ids):
    """
    Dùng Apify Facebook Group Scraper
    https://apify.com/apify/facebook-groups-scraper
    """
    results = []
    for group_id in group_ids:
        url = "https://api.apify.com/v2/acts/apify~facebook-groups-scraper/run-sync-get-dataset-items"
        payload = {
            "startUrls": [{"url": f"https://www.facebook.com/groups/{group_id}"}],
            "maxPosts": 30,
            "maxPostComments": 10
        }
        req = urllib.request.Request(
            f"{url}?token={APIFY_TOKEN}",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=120).read())
            for post in data[:15]:
                results.append({
                    "source": "facebook",
                    "text": post.get("text", "")[:300],
                    "reactions": post.get("reactionsCount", 0),
                    "comments": post.get("commentsCount", 0),
                    "shares": post.get("sharesCount", 0)
                })
        except Exception:
            pass
    return sorted(results, key=lambda x: x["reactions"] + x["comments"] * 2, reverse=True)

def synthesize_topics(rss_items, tiktok_items, fb_items):
    """
    Dùng Claude để tổng hợp → ra danh sách chủ đề content
    """
    prompt = f"""
Mày là content strategist cho fanpage "Trùm Sân Bay" — nhân viên sân bay kỳ cựu, tư vấn đi máy bay.

Dựa vào dữ liệu social media và tin tức hàng không dưới đây, đề xuất 10 chủ đề content cho tuần tới.

RSS/Tin tức hãng bay:
{json.dumps(rss_items[:5], ensure_ascii=False)}

TikTok trending (sân bay):
{json.dumps(tiktok_items[:10], ensure_ascii=False)}

Facebook Groups (câu hỏi/pain point phổ biến):
{json.dumps(fb_items[:10], ensure_ascii=False)}

Trả về JSON:
{{
  "topics": [
    {{
      "title": "Tên chủ đề ngắn gọn",
      "pillar": "TOFU|MOFU|BOFU",
      "angle": "Góc tiếp cận — tip/cảnh báo/hướng dẫn/promote",
      "source": "facebook|tiktok|news",
      "why_now": "Lý do chủ đề này hot tuần này (1 câu)",
      "hook_idea": "Câu hook gợi ý"
    }}
  ]
}}

Ưu tiên: 6 TOFU, 3 MOFU, 1 BOFU.
Chỉ trả JSON.
"""
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": prompt}]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return json.loads(result["content"][0]["text"])

def push_to_ideation_queue(topics):
    """Đẩy danh sách chủ đề vào Airtable ideation table"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/ideation_queue"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    pushed = 0
    for topic in topics.get("topics", []):
        payload = {"fields": {
            "title": topic["title"],
            "pillar": topic["pillar"],
            "angle": topic["angle"],
            "source": topic["source"],
            "why_now": topic["why_now"],
            "hook_idea": topic["hook_idea"],
            "status": "PENDING",
            "week": datetime.now().strftime("%Y-W%W")
        }}
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
        urllib.request.urlopen(req)
        pushed += 1
    return pushed

def run_research():
    """Main research pipeline — chạy mỗi sáng T2"""

    # 1. RSS hãng bay
    rss_sources = [
        "https://www.vietnamairlines.com/vn/vi/tin-tuc/rss",
        "https://www.vietjetair.com/rss.xml",
        "https://caa.gov.vn/rss/",
    ]
    rss_items = []
    for src in rss_sources:
        rss_items.extend(fetch_rss(src))

    # 2. TikTok trending
    tiktok_items = fetch_tiktok_trending([
        "sanbayvietnam", "maybay", "checkin", "fasttrack", "meodutlich"
    ])

    # 3. Facebook groups
    fb_items = fetch_facebook_group_topics([
        "hoinhungnguoimedimayBay",  # thay bằng group ID thật
        "kinhnghiemdulichtrongnuoc"
    ])

    # 4. Tổng hợp bằng Claude
    topics = synthesize_topics(rss_items, tiktok_items, fb_items)

    # 5. Push vào Airtable
    count = push_to_ideation_queue(topics)

    return f"✅ Research xong: {count} chủ đề mới vào ideation queue"

if __name__ == "__main__":
    print(run_research())
```

## Airtable — ideation_queue table

Fields cần tạo:
- `title` (text) — tên chủ đề
- `pillar` (single select: TOFU/MOFU/BOFU)
- `angle` (text) — tip/cảnh báo/hướng dẫn/promote
- `source` (single select: facebook/tiktok/news)
- `why_now` (text) — lý do hot tuần này
- `hook_idea` (text) — câu hook gợi ý
- `status` (single select: PENDING/IN_PROGRESS/DONE/SKIPPED)
- `week` (text) — "2024-W03"

## Lịch chạy

```
T2 7:00 → Research Agent crawl + synthesize
T2 8:00 → Ideation Agent nhận topics → gen 7 post draft
T2 9:00 → Telegram notify Nobitano: "7 bài draft chờ review"
T3-CN   → Publisher đăng theo lịch đã approve
```

## Lưu ý

- **Apify free tier:** 5 USD credit/tháng — đủ cho ~50 scraping runs
- **Facebook Group scraping:** Terms of Service greyzone — dùng ở mức độ vừa phải, không spam
- **RSS feeds:** Hoàn toàn hợp lệ, không có vấn đề gì
- **Rate limit:** Sleep 2s giữa các Apify calls để tránh bị block
