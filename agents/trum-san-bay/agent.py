"""
Trùm Sân Bay — Content Pipeline Agent
Chạy qua Hermes, nhận lệnh từ OpenClaw qua Telegram
"""
import urllib.request
import json
import base64
import time
import os
from datetime import datetime

# === CONFIG (set qua pm2 env) ===
FB_PAGE_ID = os.environ.get("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")
IG_USER_ID = os.environ.get("IG_USER_ID")
TIKTOK_ACCESS_TOKEN = os.environ.get("TIKTOK_ACCESS_TOKEN")
YOUTUBE_CHANNEL_ID = os.environ.get("YOUTUBE_CHANNEL_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
SCENEWORKS_URL = os.environ.get("SCENEWORKS_URL", "http://localhost:7860")

# === HELPERS ===

def api_call(url, method="GET", data=None, headers=None):
    """Generic HTTP call dùng urllib.request thuần"""
    req = urllib.request.Request(url, headers=headers or {}, method=method)
    if data:
        req.data = json.dumps(data).encode()
        req.add_header("Content-Type", "application/json")
    try:
        res = urllib.request.urlopen(req, timeout=30)
        return json.loads(res.read())
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode(), "status": e.code}

def airtable_create(table, fields):
    """Tạo record trong Airtable"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{table}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    return api_call(url, "POST", {"fields": fields}, headers)

def airtable_update(table, record_id, fields):
    """Update record trong Airtable"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{table}/{record_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    return api_call(url, "PATCH", {"fields": fields}, headers)

def airtable_list(table, filter_formula=None):
    """List records từ Airtable"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{table}"
    if filter_formula:
        url += f"?filterByFormula={urllib.parse.quote(filter_formula)}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    return api_call(url, headers=headers)

def gen_image(prompt, width=1080, height=1080):
    """Gen ảnh qua SceneWorks"""
    payload = {"prompt": prompt, "width": width, "height": height, "steps": 20}
    url = f"{SCENEWORKS_URL}/api/generate"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                  headers={"Content-Type": "application/json"}, method="POST")
    result = json.loads(urllib.request.urlopen(req, timeout=60).read())
    return result.get("image_path") or result.get("output_path")

# === LLM ROUTER (xem skills/llm-router/SKILL.md để biết chi tiết) ===

OMNIROUTE_URL = os.environ.get("OMNIROUTE_URL")
OMNIROUTE_KEY = os.environ.get("OMNIROUTE_API_KEY")

MODEL_MAP = {
    "cheap": "deepseek-v3",           # research, image prompt, sentiment
    "reasoning": "deepseek-r1",        # dedup, logic filter
    "balanced": "gemini-2.0-flash",    # ideation synthesis
    "creative": "claude-sonnet-4-6",   # writer, reply — đại diện brand voice
    "factcheck": "claude-sonnet-4-6",  # accuracy-critical
}

def llm_call(prompt, tier="cheap", max_tokens=1500, temperature=0.7):
    """
    Universal call — route theo tier thay vì hardcode Claude cho mọi thứ.
    Việc cần văn phong/brand voice (creative, factcheck) -> Claude.
    Việc nội bộ (cheap, reasoning, balanced) -> qua OmniRoute, rẻ hơn nhiều.
    """
    model = MODEL_MAP.get(tier, "deepseek-v3")

    if model.startswith("claude"):
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}]
        }
        result = api_call(url, "POST", payload, headers)
        return result["content"][0]["text"] if "content" in result else None

    # Model rẻ qua OmniRoute (OpenAI-compatible)
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    headers = {"Authorization": f"Bearer {OMNIROUTE_KEY}", "Content-Type": "application/json"}
    try:
        result = api_call(OMNIROUTE_URL, "POST", payload, headers)
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        # Fallback lên Claude nếu model rẻ lỗi
        print(f"[llm_call] tier={tier} failed ({e}), fallback to Claude")
        return llm_call(prompt, tier="creative", max_tokens=max_tokens, temperature=temperature)


def llm_call_json(prompt, tier="cheap", max_tokens=1500):
    """Parse JSON, retry 1 lần với instruction nhấn mạnh nếu parse fail"""
    raw = llm_call(prompt, tier=tier, max_tokens=max_tokens, temperature=0.5)
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        retry_prompt = prompt + "\n\nQUAN TRỌNG: Chỉ trả JSON hợp lệ, không markdown, không giải thích."
        raw2 = llm_call(retry_prompt, tier=tier, max_tokens=max_tokens, temperature=0.3)
        return json.loads(raw2)


# Giữ tên cũ để không phải sửa chỗ gọi khác — giờ route qua llm_call tier=creative
def gen_content_with_claude(prompt):
    return llm_call(prompt, tier="creative", max_tokens=2000)

# === CONTENT PIPELINE ===

def generate_post(topic, pillar="TOFU"):
    """
    Full pipeline: topic → caption + ảnh → Airtable queue
    """
    content_id = f"tsb_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # 1. Gen caption bằng Claude
    writer_prompt = f"""
Mày là Trùm Sân Bay — nhân viên sân bay 15 năm kinh nghiệm, tone thân thiện, nói thật.
Viết content về: "{topic}"
Pillar: {pillar}

Trả về JSON với format:
{{
  "caption_fb": "caption dài cho Facebook (500-1000 ký tự, 3-5 emoji, 3 hashtag)",
  "caption_ig": "caption Instagram (hook + body ngắn hơn, 5 hashtag)",
  "caption_tiktok": "caption TikTok (ngắn, punch, 3 hashtag trending)",
  "caption_shorts": "title YouTube Shorts (max 70 ký tự)",
  "image_prompt": "prompt tiếng Anh để gen ảnh sân bay phù hợp nội dung"
}}

Chỉ trả JSON, không giải thích thêm.
"""
    raw = gen_content_with_claude(writer_prompt)
    try:
        content = json.loads(raw)
    except Exception:
        return {"error": "JSON parse failed", "raw": raw}

    # 2. Gen ảnh 1:1
    image_path = gen_image(content.get("image_prompt", f"Vietnamese airport {topic}"))

    # 3. Đẩy vào Airtable queue
    record = airtable_create("content_queue", {
        "content_id": content_id,
        "topic": topic,
        "pillar": pillar,
        "caption_fb": content.get("caption_fb"),
        "caption_ig": content.get("caption_ig"),
        "caption_tiktok": content.get("caption_tiktok"),
        "caption_shorts": content.get("caption_shorts"),
        "asset_path": image_path or "",
        "status": "PENDING_REVIEW",
        "created_at": datetime.now().isoformat()
    })

    return {
        "content_id": content_id,
        "airtable_id": record.get("id"),
        "topic": topic,
        "preview_caption": content.get("caption_fb", "")[:200] + "...",
        "image": image_path,
        "status": "PENDING_REVIEW"
    }

def publish_post(airtable_record_id):
    """
    Sau khi approve: lấy từ Airtable → đăng lên tất cả platform
    """
    # Lấy record
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/content_queue/{airtable_record_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    record = api_call(url, headers=headers)
    fields = record.get("fields", {})

    post_ids = {}

    # Facebook
    fb_result = api_call(
        f"https://graph.facebook.com/v18.0/{FB_PAGE_ID}/photos",
        "POST",
        {"message": fields.get("caption_fb"), "url": fields.get("asset_path")},
        {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
    )
    post_ids["facebook"] = fb_result.get("id")
    time.sleep(1)

    # Instagram (2 bước: upload container → publish)
    ig_container = api_call(
        f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media",
        "POST",
        {"image_url": fields.get("asset_path"), "caption": fields.get("caption_ig")},
        {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
    )
    if ig_container.get("id"):
        time.sleep(2)
        ig_publish = api_call(
            f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish",
            "POST",
            {"creation_id": ig_container["id"]},
            {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
        )
        post_ids["instagram"] = ig_publish.get("id")

    # Update Airtable → POSTED
    airtable_update("content_queue", airtable_record_id, {
        "status": "POSTED",
        "post_ids": json.dumps(post_ids)
    })

    return {"status": "posted", "post_ids": post_ids}

# === COMMAND ROUTER (nhận từ OpenClaw) ===

def handle_command(cmd, args=""):
    """
    Router cho lệnh Telegram
    /tsb post [topic]
    /tsb approve [airtable_id]
    /tsb queue
    """
    if cmd == "post":
        result = generate_post(args)
        return f"✅ Đã tạo content: {result.get('content_id')}\n📝 Preview: {result.get('preview_caption')}"

    elif cmd == "approve":
        try:
            # telegram_alert_fn thật sẽ được OpenClaw wire vào lúc gọi hàm này
            # (Hermes không tự gửi Telegram trực tiếp — trả message, OpenClaw gửi)
            result = publish_post_safe(args, telegram_alert_fn=None)
            posted = len(result.get("posted_platforms", []))
            failed = result.get("failed_platforms", {})
            msg = f"🚀 Đã đăng lên {posted} platform"
            if failed:
                msg += f"\n⚠️ Lỗi: {', '.join(f'{p} ({e})' for p, e in failed.items())}"
            return msg
        except PipelineGateError as e:
            return f"⛔ {str(e)}"
        except BudgetExceededError as e:
            return f"🔴 Vượt budget: ${e.current:.2f}/${e.limit:.2f} — cần review trước khi tiếp tục"

    elif cmd == "queue":
        records = airtable_list("content_queue", "status='PENDING_REVIEW'")
        items = records.get("records", [])
        if not items:
            return "Queue trống, không có bài nào chờ review"
        lines = [f"📋 {len(items)} bài chờ review:"]
        for r in items[:5]:
            f = r["fields"]
            lines.append(f"• [{r['id']}] {f.get('topic')} ({f.get('pillar')})")
        return "\n".join(lines)

    return f"Lệnh không nhận ra: {cmd}"

if __name__ == "__main__":
    # Test local
    print(handle_command("queue"))


# === HARNESS — Progress persistence + Pipeline gate (xem HARNESS.md) ===

import fcntl
import time as _time

STATE_FILE = "/opt/trum-san-bay/state/progress.json"
STATE_LOCK = "/opt/trum-san-bay/state/progress.lock"

class PipelineGateError(Exception):
    pass

class BudgetExceededError(Exception):
    def __init__(self, current, limit):
        self.current = current
        self.limit = limit
        super().__init__(f"Budget exceeded: ${current:.2f} / ${limit:.2f}")


def _with_state_lock(fn):
    """
    File lock chống race condition — nếu Hermes chạy 2 instance cùng lúc
    (vd cron trigger trùng lệnh Telegram thủ công), chỉ 1 process được
    ghi state tại 1 thời điểm.
    """
    def wrapper(*args, **kwargs):
        os.makedirs(os.path.dirname(STATE_LOCK), exist_ok=True)
        with open(STATE_LOCK, "w") as lockfile:
            fcntl.flock(lockfile, fcntl.LOCK_EX)
            try:
                return fn(*args, **kwargs)
            finally:
                fcntl.flock(lockfile, fcntl.LOCK_UN)
    return wrapper


def _load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE) as f:
        return json.load(f)


@_with_state_lock
def save_state(content_id, step, status, extra=None):
    """Gọi SAU MỖI bước trong pipeline, không đợi hết pipeline mới ghi 1 lần."""
    state = _load_state()
    state[content_id] = {
        "step": step,
        "status": status,
        "updated_at": datetime.now().isoformat(),
        "extra": extra or {}
    }
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def resume_incomplete():
    """Chạy khi Hermes restart — tìm content đang dở để tiếp tục, không làm lại từ đầu."""
    state = _load_state()
    return {k: v for k, v in state.items() if v["status"] == "in_progress"}


# Gate rule — step nào chỉ được chạy khi Airtable status đang ở đâu
GATE_RULES = {
    "writer": ["DRAFT_BRIEF"],
    "visual": ["CAPTION_READY"],
    "brand_check": ["ASSET_RAW"],
    "adapter": ["ASSET_APPROVED"],
    "publish": ["APPROVED"],  # Publisher CHỈ chạy nếu người đã approve — gate quan trọng nhất
}


def enforce_pipeline_gate(content_id, current_step, record_fields):
    """
    Gọi TRƯỚC mỗi bước pipeline. record_fields = fields dict lấy từ Airtable.
    Không cho agent nhảy cóc step hoặc tự publish khi chưa được approve.
    """
    status = record_fields.get("status")
    allowed_from = GATE_RULES.get(current_step, [])
    if status not in allowed_from:
        raise PipelineGateError(
            f"{content_id} đang ở status={status}, KHÔNG đủ điều kiện chạy "
            f"bước '{current_step}' (yêu cầu status thuộc {allowed_from})"
        )
    return True


# === PER-PLATFORM PUBLISHERS — mỗi hàm trả (success: bool, response: dict, error_code) ===
# Theo đúng contract của safe_api_call trong skills/api-error-handler/SKILL.md

RETRYABLE_ERRORS = {
    "facebook": [4, 32],
    "instagram": [4, 32],
    "tiktok": ["rate_limit_exceeded", "spam_risk_too_many_posts"],
    "youtube": [503],
}


def _retry_call(platform, fn, max_retries=3, base_backoff=5):
    """
    Wrapper retry cho MỌI publish call — theo bảng lỗi trong api-error-handler.
    fn phải trả về (success, response, error_code).
    """
    attempt = 0
    while attempt < max_retries:
        success, response, error_code = fn()
        if success:
            return {"status": "success", "response": response}

        retryable = RETRYABLE_ERRORS.get(platform, [])
        if error_code in retryable:
            _time.sleep(base_backoff * (5 ** attempt))
            attempt += 1
            continue
        return {"status": "failed", "error_code": error_code, "response": response}

    return {"status": "failed_after_retries", "error_code": error_code}


def _publish_facebook(fields):
    def call():
        result = api_call(
            f"https://graph.facebook.com/v18.0/{FB_PAGE_ID}/photos", "POST",
            {"message": fields.get("caption_fb"), "url": fields.get("asset_path")},
            {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
        )
        if result.get("id"):
            return True, result, None
        err = result.get("error", {})
        return False, result, err.get("code")
    return _retry_call("facebook", call)


def _publish_instagram(fields):
    def call():
        container = api_call(
            f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media", "POST",
            {"image_url": fields.get("asset_path"), "caption": fields.get("caption_ig")},
            {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
        )
        if not container.get("id"):
            err = container.get("error", {})
            return False, container, err.get("code")
        _time.sleep(2)
        publish = api_call(
            f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish", "POST",
            {"creation_id": container["id"]},
            {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
        )
        if publish.get("id"):
            return True, publish, None
        err = publish.get("error", {})
        return False, publish, err.get("code")
    return _retry_call("instagram", call)


def _publish_tiktok(fields):
    """
    TikTok Content Posting API — flow 2 bước: init upload (lấy upload_url),
    sau đó publish. Dùng PULL_FROM_URL nếu video đã có URL public (vd host
    trên VPS qua nginx), tránh phải upload multipart bằng urllib thuần.
    """
    def call():
        video_url = fields.get("video_path_public_url")  # URL public trỏ tới file mp4 trên VPS
        if not video_url:
            return False, {"error": "missing video_path_public_url"}, "video_format_invalid"

        init_payload = {
            "post_info": {
                "title": fields.get("caption_tiktok", "")[:150],
                "privacy_level": "PUBLIC_TO_EVERYONE",
                "disable_duet": False,
                "disable_comment": False,
                "disable_stitch": False,
            },
            "source_info": {
                "source": "PULL_FROM_URL",
                "video_url": video_url
            }
        }
        result = api_call(
            "https://open.tiktokapis.com/v2/post/publish/video/init/", "POST",
            init_payload,
            {"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}", "Content-Type": "application/json; charset=UTF-8"}
        )
        error = result.get("error", {})
        if error.get("code") and error["code"] != "ok":
            return False, result, error["code"]
        publish_id = result.get("data", {}).get("publish_id")
        if publish_id:
            return True, {"publish_id": publish_id}, None
        return False, result, "unknown_error"
    return _retry_call("tiktok", call)


def _publish_youtube(fields):
    """
    YouTube Data API v3 — resumable upload, thuần urllib (Hermes constraint:
    không pip install thư viện ngoài). 2 bước: khởi tạo session resumable
    (metadata), rồi PUT file bytes.
    """
    def call():
        video_path = fields.get("video_local_path")
        if not video_path or not os.path.exists(video_path):
            return False, {"error": "video file not found"}, 400

        metadata = {
            "snippet": {
                "title": fields.get("youtube_title", "")[:100],
                "description": fields.get("youtube_description", ""),
                "categoryId": "19"  # Travel & Events
            },
            "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False}
        }

        access_token = os.environ.get("YOUTUBE_ACCESS_TOKEN")  # refreshed riêng qua OAuth flow
        init_req = urllib.request.Request(
            "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
            data=json.dumps(metadata).encode(),
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json; charset=UTF-8",
                "X-Upload-Content-Type": "video/mp4"
            },
            method="POST"
        )
        try:
            init_res = urllib.request.urlopen(init_req)
            upload_url = init_res.headers.get("Location")
        except urllib.error.HTTPError as e:
            return False, {"error": e.read().decode()}, e.code

        with open(video_path, "rb") as f:
            video_bytes = f.read()

        upload_req = urllib.request.Request(
            upload_url, data=video_bytes,
            headers={"Content-Type": "video/mp4", "Content-Length": str(len(video_bytes))},
            method="PUT"
        )
        try:
            upload_res = json.loads(urllib.request.urlopen(upload_req).read())
            if upload_res.get("id"):
                return True, upload_res, None
            return False, upload_res, "unknown_error"
        except urllib.error.HTTPError as e:
            return False, {"error": e.read().decode()}, e.code

    return _retry_call("youtube", call)


# Map platform -> (publisher_fn, required_field_check)
PLATFORM_PUBLISHERS = {
    "facebook": _publish_facebook,
    "instagram": _publish_instagram,
    "tiktok": _publish_tiktok,
    "youtube": _publish_youtube,
}

ERROR_MESSAGES = {
    190: "Token Facebook/Instagram hết hạn — cần refresh ngay",
    200: "Thiếu permission trên Meta App",
    368: "Nội dung bị Facebook flag — cần review thủ công",
    "access_token_invalid": "Token TikTok hết hạn — cần re-auth",
    "video_format_invalid": "Video TikTok lỗi format/thiếu URL public",
    401: "Token YouTube hết hạn — cần refresh OAuth",
    403: "YouTube hết quota API hôm nay hoặc thiếu permission",
}


def publish_post_safe(airtable_record_id, telegram_alert_fn=None):
    """
    Bản publish_post() có harness đầy đủ: gate check + idempotency (không
    đăng trùng platform đã đăng nếu retry sau crash) + progress persistence
    + retry theo bảng lỗi từng platform + alert khi cần người xử lý.
    THAY THẾ publish_post() gốc — dùng hàm này trong handle_command().

    Chỉ publish lên platform nào CÓ credential set trong env — cho phép
    launch dần (vd chỉ Facebook trước, thêm TikTok sau) mà không sửa code.
    """
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/content_queue/{airtable_record_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    record = api_call(url, headers=headers)
    fields = record.get("fields", {})

    # GATE — chặn cứng nếu chưa APPROVED, dù ai gọi hàm này từ đâu
    enforce_pipeline_gate(airtable_record_id, "publish", fields)

    # Chỉ đăng platform nào đã cấu hình credential (tránh lỗi thừa khi launch dần)
    configured_platforms = []
    if FB_ACCESS_TOKEN and FB_PAGE_ID:
        configured_platforms.append("facebook")
    if FB_ACCESS_TOKEN and IG_USER_ID:
        configured_platforms.append("instagram")
    if TIKTOK_ACCESS_TOKEN:
        configured_platforms.append("tiktok")
    if os.environ.get("YOUTUBE_ACCESS_TOKEN"):
        configured_platforms.append("youtube")

    # Idempotency — check đã đăng platform nào rồi (từ progress.json)
    state = _load_state().get(airtable_record_id, {})
    already_posted = state.get("extra", {}).get("posted_platforms", [])
    already_failed = state.get("extra", {}).get("failed_platforms", {})

    save_state(airtable_record_id, "publish", "in_progress",
               {"posted_platforms": already_posted, "failed_platforms": already_failed})

    post_ids = {}
    newly_failed = {}

    for platform in configured_platforms:
        if platform in already_posted:
            continue  # đã đăng rồi, skip — tránh đăng trùng khi retry sau crash

        publisher_fn = PLATFORM_PUBLISHERS[platform]
        result = publisher_fn(fields)

        if result["status"] == "success":
            post_id = result["response"].get("id") or result["response"].get("publish_id")
            post_ids[platform] = post_id
            already_posted.append(platform)
            save_state(airtable_record_id, "publish", "in_progress",
                       {"posted_platforms": already_posted, "failed_platforms": already_failed})
        else:
            error_code = result.get("error_code")
            message = ERROR_MESSAGES.get(error_code, f"Lỗi không xác định: {error_code}")
            newly_failed[platform] = message
            already_failed[platform] = message
            if telegram_alert_fn:
                telegram_alert_fn(
                    f"🔴 Publish FAILED — {platform} — {airtable_record_id}\n"
                    f"Lỗi: {message}\nCần xử lý thủ công."
                )

        _time.sleep(1)  # tránh burst request liên tiếp giữa các platform

    all_done = len(already_posted) == len(configured_platforms)
    final_status = "success" if all_done else ("partial" if already_posted else "failed")
    save_state(airtable_record_id, "publish", final_status,
               {"posted_platforms": already_posted, "failed_platforms": already_failed})

    airtable_update("content_queue", airtable_record_id, {
        "status": "POSTED" if all_done else "PARTIAL_FAIL",
        "post_ids": json.dumps(post_ids),
        "publish_errors": json.dumps(already_failed) if already_failed else ""
    })

    if telegram_alert_fn:
        if all_done:
            telegram_alert_fn(f"✅ {airtable_record_id}: đã đăng thành công {len(already_posted)} platform")
        else:
            telegram_alert_fn(
                f"⚠️ {airtable_record_id}: {len(already_posted)}/{len(configured_platforms)} platform "
                f"thành công, {len(newly_failed)} lỗi mới — check chi tiết ở trên"
            )

    return {
        "status": final_status,
        "post_ids": post_ids,
        "posted_platforms": already_posted,
        "failed_platforms": already_failed
    }

