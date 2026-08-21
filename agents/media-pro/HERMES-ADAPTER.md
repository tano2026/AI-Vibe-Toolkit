# HERMES-ADAPTER.md — Media Pro

> Media Pro trên Hermes chủ yếu là ĐỌC/PHÂN TÍCH số liệu — vidIQ MCP không
> có trên Hermes (đó là tool riêng Claude.ai), cần thay bằng cách khác.

## Vấn đề: vidIQ MCP không có trên Hermes

Media Pro gốc dựa hoàn toàn vào vidIQ MCP để lấy stats YouTube/TikTok/Instagram. Hermes không có tool này. 2 lựa chọn:

```python
# Lựa chọn A — YouTube Data API trực tiếp (free quota, cần API key riêng)
import urllib.request, json, os

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

def youtube_video_stats(video_id):
    url = (f"https://www.googleapis.com/youtube/v3/videos?"
           f"part=statistics,contentDetails&id={video_id}&key={YOUTUBE_API_KEY}")
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

# Lựa chọn B — TikTok/Instagram: KHÔNG có API free ổn định qua urllib thuần.
# Với 2 platform này, Hermes CHƯA có cách tự động lấy data — cần:
#   (a) Nobitano tự export CSV từ TikTok/Instagram Studio định kỳ, Hermes đọc
#       file CSV đó (open().read() + csv module, stdlib thuần), HOẶC
#   (b) Chạy phần này qua Claude.ai/Mission Control (có vidIQ MCP thật) thay
#       vì Hermes, chỉ dùng Hermes cho phần YouTube
```

## Việc Hermes làm được ngay (không cần API ngoài)

```python
# Pre-Publish Gate — thuần logic, không cần tool ngoài
def pre_publish_check(content_actual, content_approved, channel_actual, channel_planned,
                       time_actual, time_planned, pack_actual, pack_approved):
    checks = {
        "nội dung khớp": content_actual == content_approved,
        "kênh khớp": channel_actual == channel_planned,
        "giờ khớp": time_actual == time_planned,
        "PACK khớp": pack_actual == pack_approved,
    }
    failed = [k for k, v in checks.items() if not v]
    if failed:
        return {"status": "STOP", "lệch": failed}
    return {"status": "GO"}

# Đếm escalation — thuần logic
def check_escalation(complaint_text, complaint_history):
    """complaint_history: list các complaint trước đó (đã phân loại tương tự)"""
    similar_count = sum(1 for c in complaint_history if is_similar(c, complaint_text))
    if similar_count >= 3:
        return {"action": "ESCALATE", "count": similar_count}
    return {"action": "LOG_ONLY", "count": similar_count}

def is_similar(a, b):
    # Đơn giản nhất: so khớp từ khoá chính — có thể nâng cấp bằng
    # embedding/semantic sau, nhưng bản Hermes-thuần dùng rule-based trước
    keywords_a = set(a.lower().split())
    keywords_b = set(b.lower().split())
    overlap = len(keywords_a & keywords_b) / max(len(keywords_a), 1)
    return overlap > 0.5
```

## Timing check (24-72h) — thuần Python, không cần tool ngoài

```python
from datetime import datetime, timedelta

def can_evaluate_performance(publish_time_iso):
    publish_time = datetime.fromisoformat(publish_time_iso)
    hours_elapsed = (datetime.now() - publish_time).total_seconds() / 3600
    if hours_elapsed < 24:
        return {"ready": False, "note": f"Mới {hours_elapsed:.0f}h, cần đợi ít nhất 24h"}
    return {"ready": True, "hours_elapsed": hours_elapsed}
```

## Cách dùng thật trên Hermes

```python
# 1. Pre-publish check — chạy được ngay, thuần logic
result = pre_publish_check(...)
if result["status"] == "STOP":
    # Báo Telegram, không cho đăng
    pass

# 2. Performance check — cần YouTube API key cho YouTube, còn TikTok/Instagram
#    báo rõ giới hạn thay vì im lặng bỏ qua
if platform == "youtube":
    stats = youtube_video_stats(video_id)
else:
    stats = {"note": "⚠️ Chưa có cách tự động lấy data platform này qua Hermes "
                      "— cần export CSV thủ công hoặc chạy qua Claude.ai/Mission Control"}
```

## Giới hạn thật (không giấu)

Media Pro trên Hermes hiện chỉ mạnh cho: Pre-Publish Gate (logic thuần), timing check (logic thuần), escalation counting (logic thuần đơn giản, chưa có semantic matching thật). Phần **Performance Reader thật** (đọc số liệu chi tiết) và **Cross-Channel Analysis** vẫn cần vidIQ MCP — trên Hermes chỉ làm được với YouTube (qua API riêng), TikTok/Instagram cần chạy qua Claude.ai/Mission Control hoặc export CSV thủ công.
