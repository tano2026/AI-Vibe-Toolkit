# Content Strategy — Ideation Agent

## Mô tả
Nhận raw topics từ Research Agent → lọc, rank, gắn brief chi tiết → xuất ra 7 post plan cho tuần. Đây là bước "biên tập" giữa research thô và viết caption thật.

## Trigger
Chạy ngay sau Research Agent xong (T2 8h), hoặc lệnh `/tsb tạo tuần`.

## Vị trí trong pipeline
```
Research Agent (10 topics thô trong ideation_queue)
        ↓
Content Strategy / Ideation Agent  ← skill này
        ↓
Writer Agent (nhận 7 brief để viết caption)
```

## Prompt thực tế

```python
IDEATION_PROMPT = """
Mày là content strategist cho fanpage "Trùm Sân Bay" — nhân viên sân bay 
15 năm kinh nghiệm, tư vấn đi máy bay, bán Fast Track/SIM/đổi tiền.

Đây là 10 chủ đề thô từ research tuần này:
{raw_topics}

Nhiệm vụ:
1. Chọn ra 7 chủ đề tốt nhất cho tuần — loại bỏ chủ đề trùng lặp, 
   chủ đề không phù hợp brand, hoặc chủ đề thiếu cơ sở thông tin
2. Đảm bảo tỷ lệ pillar: 4-5 TOFU, 2 MOFU, 1 BOFU (không cứng nhắc 
   nhưng giữ tinh thần "cho trước, bán sau")
3. Phân bổ đều 7 ngày trong tuần, tránh 2 ngày liên tiếp cùng pillar BOFU
4. Với mỗi chủ đề, viết brief chi tiết để Writer Agent viết caption

Kiểm tra loại bỏ nếu:
- Thông tin không chắc chắn / không verify được (đánh dấu để research thêm)
- Trùng chủ đề đã làm trong 4 tuần gần đây (check lịch sử)
- Không phù hợp tone "nhân viên sân bay kỳ cựu, tư vấn thật"

Trả về JSON:
{{
  "week": "2024-W03",
  "posts": [
    {{
      "day": "Monday",
      "topic": "...",
      "pillar": "TOFU|MOFU|BOFU",
      "angle": "tip|cảnh báo|hướng dẫn|so sánh|promote",
      "brief": "2-3 câu mô tả nội dung chính cần truyền tải",
      "key_points": ["điểm 1", "điểm 2", "điểm 3"],
      "hook_direction": "loại hook nên dùng - curiosity/contrarian/authority/story",
      "cta_type": "save|comment|share|purchase",
      "needs_factcheck": true/false,
      "image_category": "checkin|security|baggage|fasttrack|warning|currency|sim"
    }}
  ]
}}

Chỉ trả JSON.
"""
```

## Code Hermes — chạy Ideation

```python
import json
import os
import urllib.request

def check_topic_history(topic, airtable_list_fn, weeks_back=4):
    """
    Check xem topic có bị trùng với 4 tuần gần đây không
    """
    from datetime import datetime, timedelta
    cutoff = (datetime.now() - timedelta(weeks=weeks_back)).isoformat()
    recent_posts = airtable_list_fn("content_queue", f"created_at >= '{cutoff}'")
    recent_topics = [r["fields"].get("topic", "").lower() for r in recent_posts.get("records", [])]
    return topic.lower() in recent_topics


def run_ideation(raw_topics, airtable_list_fn, airtable_push_fn):
    """
    raw_topics: list từ ideation_queue (output của Research Agent)
    """
    # Lọc trùng lịch sử trước khi đưa vào prompt
    filtered = [t for t in raw_topics if not check_topic_history(t["title"], airtable_list_fn)]

    prompt = IDEATION_PROMPT.format(raw_topics=json.dumps(filtered, ensure_ascii=False))

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 3000,
        "messages": [{"role": "user", "content": prompt}]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    plan = json.loads(result["content"][0]["text"])

    # Push từng brief vào content_queue với status DRAFT_BRIEF
    for post in plan["posts"]:
        airtable_push_fn("content_queue", {
            **post,
            "status": "DRAFT_BRIEF",  # chưa viết caption, chỉ có brief
            "week": plan["week"]
        })

    return plan
```

## Output mẫu (1 brief trong 7 cái)

```json
{
  "day": "Monday",
  "topic": "3 lỗi khiến khách bị giữ lại ở an ninh sân bay",
  "pillar": "TOFU",
  "angle": "cảnh báo",
  "brief": "Liệt kê 3 lỗi phổ biến nhất khách hay mắc khi qua an ninh: 
            mang chất lỏng quá quy định, quên bỏ laptop ra khỏi túi, 
            mang vật sắc nhọn không để ý. Tone nhẹ nhàng, không dọa dẫm.",
  "key_points": [
    "Chất lỏng quá 100ml/chai",
    "Laptop phải để riêng qua máy soi",
    "Vật sắc nhọn: kéo, dao gọt hoa quả để trong balo"
  ],
  "hook_direction": "curiosity",
  "cta_type": "save",
  "needs_factcheck": true,
  "image_category": "security"
}
```

## Điểm khác biệt Ideation vs Writer

| | Ideation Agent | Writer Agent |
|---|-----------------|--------------|
| Input | 10 topic thô | 1 brief chi tiết |
| Output | Brief + structure | Caption hoàn chỉnh 5 platform |
| Model call | 1 lần cho cả 7 bài | 1 lần / bài (7 lần/tuần) |
| Vai trò | Biên tập viên | Copywriter |

## Guardrail

- Nếu Research Agent trả về ít hơn 7 topic hợp lệ (sau khi lọc trùng) → Ideation tự bổ sung bằng cách hỏi Claude gợi ý thêm dựa trên `aviation-knowledge`, không để queue trống
- `needs_factcheck: true` → Writer Agent BẮT BUỘC chạy `fact-checker` skill trước khi viết caption cho bài đó
