"""
Trùm Sân Bay — Content Pipeline Agent
Chạy qua Hermes, nhận lệnh từ OpenClaw qua Telegram
"""
import urllib.request
import urllib.parse
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



# === COMMAND ROUTER (nhận từ OpenClaw) ===

def handle_command(cmd, args=""):
    """
    Router cho lệnh Telegram
    /tsb post [topic]
    /tsb approve [airtable_id]
    /tsb queue
    """
    if cmd == "post":
        # Route qua orchestrator thật (Writer Agent với prompt xịn), không
        # còn dùng generate_post() cũ (đã xóa — prompt mỏng, dùng SceneWorks)
        from orchestrator import run_writer_agent
        brief = {"topic": args, "pillar": "TOFU", "brief": args,
                  "key_points": [], "hook_direction": "curiosity", "cta_type": "save"}
        result = run_writer_agent(brief)
        record = airtable_create("content_queue", {
            **{k: v for k, v in result.items() if k != "self_check"},
            "topic": args, "status": "PENDING_REVIEW",
            "created_at": datetime.now().isoformat()
        })
        return f"✅ Đã tạo content: {record.get('id')}\n📝 Preview: {result.get('caption_fb', '')[:200]}..."

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
            {"Authorization": f"Bearer {get_tiktok_access_token()}", "Content-Type": "application/json; charset=UTF-8"}
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

        access_token = get_youtube_access_token()  # tự refresh nếu gần hết hạn
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
    if os.environ.get("TIKTOK_REFRESH_TOKEN"):
        configured_platforms.append("tiktok")
    if os.environ.get("YOUTUBE_REFRESH_TOKEN"):
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


# === TOKEN REFRESH — YouTube + TikTok (access token sống ngắn, phải tự refresh) ===
# Facebook long-lived token sống 60 ngày, không cần refresh tự động —
# chỉ cần cảnh báo trước hạn (đã có trong check_token_health bên dưới).

TOKEN_CACHE_FILE = "/opt/trum-san-bay/state/tokens.json"


def _load_token_cache():
    if not os.path.exists(TOKEN_CACHE_FILE):
        return {}
    with open(TOKEN_CACHE_FILE) as f:
        return json.load(f)


@_with_state_lock
def _save_token_cache(platform, access_token, expires_at):
    cache = _load_token_cache()
    cache[platform] = {"access_token": access_token, "expires_at": expires_at}
    os.makedirs(os.path.dirname(TOKEN_CACHE_FILE), exist_ok=True)
    with open(TOKEN_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def get_youtube_access_token():
    """
    YouTube access token sống 1h — refresh tự động bằng refresh_token
    (refresh_token sống dài hạn, lấy 1 lần qua OAuth flow thủ công lúc setup).
    Gọi hàm này TRƯỚC MỌI lần publish YouTube, không dùng env var tĩnh nữa.
    """
    cache = _load_token_cache()
    cached = cache.get("youtube")

    # Còn hạn ít nhất 5 phút thì dùng lại, không refresh liên tục vô ích
    if cached and cached["expires_at"] > time.time() + 300:
        return cached["access_token"]

    refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")
    client_id = os.environ.get("YOUTUBE_CLIENT_ID")
    client_secret = os.environ.get("YOUTUBE_CLIENT_SECRET")

    if not refresh_token:
        raise TokenRefreshError(
            "youtube",
            "Thiếu YOUTUBE_REFRESH_TOKEN — cần chạy OAuth flow thủ công 1 lần "
            "để lấy refresh_token (xem mcp-setup.md mục 5)"
        )

    payload = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode()

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token", data=payload, method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    try:
        result = json.loads(urllib.request.urlopen(req, timeout=15).read())
    except urllib.error.HTTPError as e:
        raise TokenRefreshError("youtube", f"Refresh thất bại: {e.read().decode()}")

    access_token = result["access_token"]
    expires_in = result.get("expires_in", 3600)
    _save_token_cache("youtube", access_token, time.time() + expires_in)
    return access_token


def get_tiktok_access_token():
    """
    TikTok access token thường sống 24h, refresh_token sống ~365 ngày.
    Cùng pattern: cache local, refresh khi gần hết hạn.
    """
    cache = _load_token_cache()
    cached = cache.get("tiktok")

    if cached and cached["expires_at"] > time.time() + 600:
        return cached["access_token"]

    refresh_token = os.environ.get("TIKTOK_REFRESH_TOKEN")
    client_key = os.environ.get("TIKTOK_CLIENT_KEY")
    client_secret = os.environ.get("TIKTOK_CLIENT_SECRET")

    if not refresh_token:
        raise TokenRefreshError(
            "tiktok",
            "Thiếu TIKTOK_REFRESH_TOKEN — cần chạy OAuth flow thủ công 1 lần "
            "để lấy refresh_token (xem mcp-setup.md mục 4)"
        )

    payload = urllib.parse.urlencode({
        "client_key": client_key,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode()

    req = urllib.request.Request(
        "https://open.tiktokapis.com/v2/oauth/token/", data=payload, method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    try:
        result = json.loads(urllib.request.urlopen(req, timeout=15).read())
    except urllib.error.HTTPError as e:
        raise TokenRefreshError("tiktok", f"Refresh thất bại: {e.read().decode()}")

    access_token = result["access_token"]
    expires_in = result.get("expires_in", 86400)
    new_refresh_token = result.get("refresh_token")  # TikTok đôi khi rotate refresh_token
    _save_token_cache("tiktok", access_token, time.time() + expires_in)

    if new_refresh_token and new_refresh_token != refresh_token:
        # Refresh token mới — CẢNH BÁO, cần người cập nhật env var, không tự
        # ghi đè env process đang chạy (pm2 restart mới áp dụng được)
        _save_token_cache("tiktok_new_refresh_token_pending", new_refresh_token, time.time() + 31536000)

    return access_token


class TokenRefreshError(Exception):
    def __init__(self, platform, message):
        self.platform = platform
        self.message = message
        super().__init__(f"[{platform}] {message}")


def check_all_tokens_health(telegram_alert_fn=None):
    """
    Cron hàng ngày — chủ động check + refresh trước khi hết hạn, thay vì
    đợi publish fail mới biết. Cũng check Facebook long-lived token (không
    tự refresh được, chỉ cảnh báo).
    """
    issues = []

    # Facebook — không refresh tự động, chỉ cảnh báo trước 3 ngày
    if FB_ACCESS_TOKEN:
        fb_url = (f"https://graph.facebook.com/debug_token?"
                   f"input_token={FB_ACCESS_TOKEN}&access_token={FB_ACCESS_TOKEN}")
        try:
            data = json.loads(urllib.request.urlopen(fb_url, timeout=15).read())
            expires_at = data.get("data", {}).get("expires_at", 0)
            days_left = (expires_at - time.time()) / 86400
            if days_left < 3:
                issues.append(f"⚠️ Facebook token còn {int(days_left)} ngày — cần refresh thủ công")
        except Exception:
            issues.append("❌ Không check được Facebook token")

    # YouTube — thử refresh chủ động
    if os.environ.get("YOUTUBE_REFRESH_TOKEN"):
        try:
            get_youtube_access_token()
        except TokenRefreshError as e:
            issues.append(f"🔴 YouTube: {e.message}")

    # TikTok — thử refresh chủ động
    if os.environ.get("TIKTOK_REFRESH_TOKEN"):
        try:
            get_tiktok_access_token()
        except TokenRefreshError as e:
            issues.append(f"🔴 TikTok: {e.message}")
        # Check nếu có refresh_token mới cần người cập nhật env
        cache = _load_token_cache()
        if "tiktok_new_refresh_token_pending" in cache:
            issues.append(
                "⚠️ TikTok đã rotate refresh_token mới — cần cập nhật "
                "TIKTOK_REFRESH_TOKEN trong pm2 env (xem state/tokens.json)"
            )

    if issues and telegram_alert_fn:
        telegram_alert_fn("🔑 Token health check:\n" + "\n".join(issues))

    return issues
