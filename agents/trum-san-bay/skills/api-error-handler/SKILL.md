# API Error Handler — Publisher Resilience

## Mô tả
Publisher Agent gọi 4 API khác nhau (Meta, TikTok, YouTube) — mỗi cái có kiểu lỗi riêng. Không có skill này, khi 1 platform fail thì cả batch có thể fail im lặng, mất bài, hoặc đăng trùng. Skill này bắt lỗi đúng chỗ, retry đúng cách, báo đúng người.

## Trigger
Dùng khi: Publisher Agent gọi bất kỳ API đăng bài nào (Facebook, Instagram, TikTok, YouTube).

## Vị trí trong pipeline

```
Publisher Agent gọi API
        ↓
API Error Handler (wrap mọi call)  ← skill này
        ↓
   Success?  ──Yes──► Update Airtable POSTED
        │
        No
        ↓
   Retry-able? ──Yes──► Retry với backoff (max 3 lần)
        │
        No
        ↓
   Update Airtable FAILED + Telegram alert Nobitano
```

## Bảng lỗi thường gặp theo platform

### Facebook / Instagram (Meta Graph API)
| Error code | Nghĩa | Retry? | Hành động |
|------------|-------|--------|-----------|
| 190 | Access token hết hạn/invalid | ❌ | Alert ngay — cần refresh token thủ công |
| 200 | Thiếu permission | ❌ | Alert — check lại app permissions |
| 4 | Rate limit (app-level) | ✅ | Backoff 60s, retry |
| 32 | Rate limit (page-level) | ✅ | Backoff 5 phút, retry |
| 100 | Invalid parameter (ảnh lỗi format/size) | ❌ | Alert kèm chi tiết — cần fix asset |
| 368 | Content bị flag spam/policy | ❌ | Alert — cần review nội dung thủ công |

### TikTok Content Posting API
| Error code | Nghĩa | Retry? | Hành động |
|------------|-------|--------|-----------|
| `access_token_invalid` | Token hết hạn | ❌ | Alert — cần re-auth OAuth |
| `rate_limit_exceeded` | Quá rate limit | ✅ | Backoff 60s |
| `video_format_invalid` | Video sai format/duration | ❌ | Alert — gửi lại cho Visual Agent |
| `spam_risk_too_many_posts` | Đăng quá nhiều trong thời gian ngắn | ✅ | Backoff 30 phút |

### YouTube Data API v3
| Error code | Nghĩa | Retry? | Hành động |
|------------|-------|--------|-----------|
| 401 | Token hết hạn | ❌ | Alert — refresh OAuth token |
| 403 quotaExceeded | Hết quota ngày (10,000 units) | ❌ | Alert — chờ reset lúc 00:00 PT |
| 400 invalidVideo | Video lỗi format | ❌ | Alert — gửi lại Visual Agent |
| 503 backendError | Lỗi tạm thời từ Google | ✅ | Backoff 30s, retry |

## Code Hermes — Wrapper resilient

```python
import time
import json
import urllib.request
import urllib.error
import os

RETRY_CONFIG = {
    "max_retries": 3,
    "base_backoff": 5,  # giây, exponential: 5, 25, 125
}

# Lỗi nào được retry, lỗi nào escalate ngay
RETRYABLE_PATTERNS = {
    "facebook": [4, 32],  # rate limit codes
    "tiktok": ["rate_limit_exceeded", "spam_risk_too_many_posts"],
    "youtube": [503],
}

NON_RETRYABLE_PATTERNS = {
    "facebook": [190, 200, 100, 368],
    "tiktok": ["access_token_invalid", "video_format_invalid"],
    "youtube": [401, 403, 400],
}

def safe_api_call(platform, call_fn, *args, **kwargs):
    """
    Wrap mọi API call với retry logic + error classification
    call_fn: hàm thực hiện API call thật, trả về (success: bool, response: dict, error_code)
    """
    attempt = 0
    last_error = None

    while attempt < RETRY_CONFIG["max_retries"]:
        try:
            success, response, error_code = call_fn(*args, **kwargs)

            if success:
                return {"status": "success", "response": response, "attempts": attempt + 1}

            # Check nếu lỗi retryable
            retryable_codes = RETRYABLE_PATTERNS.get(platform, [])
            if error_code in retryable_codes:
                backoff = RETRY_CONFIG["base_backoff"] * (5 ** attempt)
                time.sleep(backoff)
                attempt += 1
                last_error = error_code
                continue
            else:
                # Non-retryable — escalate ngay
                return {
                    "status": "failed",
                    "error_code": error_code,
                    "retryable": False,
                    "response": response
                }

        except urllib.error.HTTPError as e:
            last_error = e.code
            attempt += 1
            time.sleep(RETRY_CONFIG["base_backoff"] * attempt)
        except Exception as e:
            return {"status": "failed", "error_code": "unknown", "message": str(e), "retryable": False}

    return {
        "status": "failed_after_retries",
        "error_code": last_error,
        "attempts": attempt,
        "retryable": True  # đã hết retry nhưng bản chất lỗi retryable
    }


def handle_publish_result(content_id, platform, result, airtable_update_fn, telegram_alert_fn):
    """
    Xử lý kết quả publish — update Airtable + alert nếu cần
    """
    if result["status"] == "success":
        airtable_update_fn(content_id, {
            f"{platform}_status": "POSTED",
            f"{platform}_post_id": result["response"].get("id")
        })
        return True

    else:
        # Failed — update Airtable + alert
        airtable_update_fn(content_id, {
            f"{platform}_status": "FAILED",
            f"{platform}_error": str(result.get("error_code"))
        })

        error_messages = {
            190: "Token Facebook/Instagram hết hạn — cần refresh ngay",
            200: "Thiếu permission trên Meta App",
            "access_token_invalid": "Token TikTok hết hạn — cần re-auth",
            401: "Token YouTube hết hạn — cần refresh OAuth",
            403: "YouTube hết quota API hôm nay",
            368: "Nội dung bị Facebook flag — cần review thủ công",
        }

        error_code = result.get("error_code")
        message = error_messages.get(error_code, f"Lỗi không xác định: {error_code}")

        telegram_alert_fn(
            f"🔴 Publish FAILED — {platform} — {content_id}\n"
            f"Lỗi: {message}\n"
            f"Cần xử lý thủ công."
        )
        return False


def publish_all_platforms(content_id, package, publishers_map, airtable_update_fn, telegram_alert_fn):
    """
    Đăng lên tất cả platform, mỗi cái độc lập — 1 platform fail không chặn platform khác
    """
    results = {}
    for platform, publish_fn in publishers_map.items():
        if platform not in package:
            continue
        result = safe_api_call(platform, publish_fn, package[platform])
        success = handle_publish_result(content_id, platform, result, airtable_update_fn, telegram_alert_fn)
        results[platform] = "success" if success else "failed"

    fail_count = sum(1 for v in results.values() if v == "failed")
    if fail_count > 0:
        telegram_alert_fn(f"⚠️ {content_id}: {fail_count}/{len(results)} platform fail — check chi tiết ở trên")
    else:
        telegram_alert_fn(f"✅ {content_id}: đã đăng thành công {len(results)} platform")

    return results
```

## Token expiry — Proactive check

```python
def check_token_health():
    """
    Chạy cron hàng ngày — check token còn hạn không, cảnh báo trước 3 ngày
    """
    checks = []

    # Facebook long-lived token: ~60 ngày
    # TikTok access token: thường 24h, cần refresh token riêng
    # YouTube OAuth: refresh token dài hạn nhưng access token 1h

    # Gọi debug_token endpoint của Meta để check expiry
    fb_url = f"https://graph.facebook.com/debug_token?input_token={os.environ.get('FB_ACCESS_TOKEN')}&access_token={os.environ.get('FB_ACCESS_TOKEN')}"
    req = urllib.request.Request(fb_url)
    try:
        data = json.loads(urllib.request.urlopen(req).read())
        expires_at = data.get("data", {}).get("expires_at", 0)
        days_left = (expires_at - time.time()) / 86400
        if days_left < 3:
            checks.append(f"⚠️ Facebook token còn {int(days_left)} ngày — cần refresh")
    except Exception:
        checks.append("❌ Không check được Facebook token")

    return checks
```

## Alert priority

| Tình huống | Kênh alert | Urgency |
|------------|-----------|---------|
| Token hết hạn | Telegram ngay | 🔴 Cao — chặn toàn bộ platform đó |
| Rate limit (đang retry) | Không alert, chỉ log | ⚪ Thấp — tự phục hồi |
| Content bị flag policy | Telegram ngay | 🔴 Cao — cần review nội dung |
| Video format lỗi | Telegram + gửi lại Visual Agent | 🟡 Trung bình |
| Token sắp hết hạn (<3 ngày) | Telegram cron hàng ngày | 🟡 Trung bình — chủ động refresh |
