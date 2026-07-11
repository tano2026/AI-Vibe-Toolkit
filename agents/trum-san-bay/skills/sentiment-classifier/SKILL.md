# Sentiment Classifier — Comment Triage

## Mô tả
Phân loại nhanh mọi comment mới trước khi vào queue, để Reply Agent không phải đọc từng cái mà biết ngay cái nào cần xử lý gấp, cái nào auto-reply được, cái nào bỏ qua.

## Trigger
Dùng khi: Comment Monitor fetch comment mới từ Facebook/TikTok/Instagram/YouTube, TRƯỚC khi đưa vào comment_queue.

## Vị trí trong pipeline

```
Comment Monitor (cron 2h/lần, fetch comment mới)
        ↓
Sentiment Classifier (phân loại)  ← skill này
        ↓
comment_queue (đã gắn nhãn, sort theo priority)
        ↓
Reply Agent (xử lý theo priority)
```

## Nhãn phân loại

| Label | Mô tả | Priority | Hành động |
|-------|-------|----------|-----------|
| `URGENT_COMPLAINT` | Phàn nàn nghiêm trọng, sắp mất khách | 🔴 P1 | Notify Telegram ngay, cần người xử lý |
| `QUESTION` | Câu hỏi cần trả lời | 🟡 P2 | Draft reply, review nhanh |
| `PURCHASE_INTENT` | Có ý định mua (hỏi giá, cách đặt) | 🟢 P1 | Draft reply + đẩy sang sales flow |
| `POSITIVE` | Khen, cảm ơn, đồng tình | 🟢 P3 | Auto-reply đơn giản (emoji + cảm ơn) |
| `NEGATIVE_MILD` | Không hài lòng nhẹ, góp ý | 🟡 P2 | Draft reply, cần review |
| `SPAM` | Quảng cáo, link lạ, không liên quan | ⚪ P4 | Auto-hide/delete, không cần reply |
| `IRRELEVANT` | Không liên quan nội dung, chit-chat | ⚪ P4 | Bỏ qua, không cần reply |

## Code Hermes — Classify comment

```python
import json
import os
import urllib.request

def classify_comment(comment_text, post_context=""):
    """
    Trả về label + priority + suggested_action
    """
    prompt = f"""
Phân loại comment sau đây trên fanpage "Trùm Sân Bay" (tư vấn đi máy bay, bán Fast Track/SIM/đổi tiền).

Post context: {post_context}
Comment: "{comment_text}"

Trả về JSON:
{{
  "label": "URGENT_COMPLAINT|QUESTION|PURCHASE_INTENT|POSITIVE|NEGATIVE_MILD|SPAM|IRRELEVANT",
  "priority": "P1|P2|P3|P4",
  "confidence": 0.0-1.0,
  "reasoning": "lý do phân loại, 1 câu ngắn",
  "suggested_action": "auto_reply|draft_review|escalate|ignore|hide"
}}

Quy tắc:
- URGENT_COMPLAINT: từ khóa như "lừa đảo", "mất tiền", "không nhận được", "tệ", kèm cảm xúc mạnh
- PURCHASE_INTENT: hỏi giá, "làm sao để mua", "đặt ở đâu", "còn chỗ không"
- SPAM: link lạ, quảng cáo dịch vụ khác, ký tự spam
- Nếu không chắc giữa 2 label, chọn label có priority cao hơn (an toàn hơn)

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
        "max_tokens": 300,
        "messages": [{"role": "user", "content": prompt}]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return json.loads(result["content"][0]["text"])


def batch_classify_and_route(comments, airtable_push_fn, telegram_notify_fn):
    """
    comments = [{"id": ..., "text": ..., "platform": ..., "post_id": ..., "author": ...}, ...]
    """
    urgent_count = 0

    for c in comments:
        result = classify_comment(c["text"], c.get("post_context", ""))

        # Push vào Airtable comment_queue kèm nhãn
        airtable_push_fn({
            "comment_id": c["id"],
            "platform": c["platform"],
            "post_id": c["post_id"],
            "author": c["author"],
            "comment_text": c["text"],
            "label": result["label"],
            "priority": result["priority"],
            "confidence": result["confidence"],
            "suggested_action": result["suggested_action"],
            "status": "PENDING" if result["suggested_action"] != "ignore" else "SKIPPED"
        })

        if result["label"] == "URGENT_COMPLAINT":
            urgent_count += 1

    if urgent_count > 0:
        telegram_notify_fn(f"⚠️ {urgent_count} comment URGENT cần xử lý ngay — check queue")

    return {"total": len(comments), "urgent": urgent_count}
```

## Threshold xử lý theo mode

### Semi-auto (hiện tại)
```
POSITIVE (confidence > 0.8)     → auto-reply template đơn giản
SPAM (confidence > 0.9)         → auto-hide
Còn lại                          → vào queue chờ Nobitano approve
```

### Full-auto (tương lai, sau khi ổn định)
```
POSITIVE, QUESTION đơn giản      → auto-reply
SPAM                              → auto-hide
URGENT_COMPLAINT, PURCHASE_INTENT → vẫn queue thủ công (rủi ro cao, cần người)
NEGATIVE_MILD                     → vẫn queue thủ công
```

## Reply template cho POSITIVE (auto-reply an toàn)

```python
POSITIVE_TEMPLATES = [
    "Cảm ơn bạn đã ủng hộ Trùm Sân Bay nha! ✈️",
    "Cảm ơn bạn nhiều! Có gì thắc mắc cứ hỏi anh nha 😊",
    "🙏 Cảm ơn bạn, chúc chuyến bay tới suôn sẻ!",
]
```

## Lưu ý

- **False positive URGENT:** thà báo nhầm còn hơn bỏ sót — threshold ưu tiên an toàn
- **Confidence thấp (<0.6):** luôn route vào queue thủ công, không tự động
- **Rate limit:** batch tối đa 20 comment/lần gọi Claude để tránh tốn token
