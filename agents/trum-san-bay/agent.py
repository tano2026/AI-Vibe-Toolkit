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
        result = publish_post(args)
        return f"🚀 Đã đăng lên {len(result.get('post_ids', {}))} platform"

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


def publish_post_safe(airtable_record_id):
    """
    Bản publish_post() có harness đầy đủ: gate check + idempotency (không
    đăng trùng platform đã đăng nếu retry sau crash) + progress persistence.
    THAY THẾ publish_post() gốc — dùng hàm này trong handle_command().
    """
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/content_queue/{airtable_record_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}
    record = api_call(url, headers=headers)
    fields = record.get("fields", {})

    # GATE — chặn cứng nếu chưa APPROVED, dù ai gọi hàm này từ đâu
    enforce_pipeline_gate(airtable_record_id, "publish", fields)

    # Idempotency — check đã đăng platform nào rồi (từ progress.json)
    state = _load_state().get(airtable_record_id, {})
    already_posted = state.get("extra", {}).get("posted_platforms", [])

    save_state(airtable_record_id, "publish", "in_progress", {"posted_platforms": already_posted})

    post_ids = {}

    if "facebook" not in already_posted:
        fb_result = api_call(
            f"https://graph.facebook.com/v18.0/{FB_PAGE_ID}/photos", "POST",
            {"message": fields.get("caption_fb"), "url": fields.get("asset_path")},
            {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
        )
        if fb_result.get("id"):
            post_ids["facebook"] = fb_result["id"]
            already_posted.append("facebook")
            save_state(airtable_record_id, "publish", "in_progress", {"posted_platforms": already_posted})
        _time.sleep(1)

    if "instagram" not in already_posted:
        ig_container = api_call(
            f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media", "POST",
            {"image_url": fields.get("asset_path"), "caption": fields.get("caption_ig")},
            {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
        )
        if ig_container.get("id"):
            _time.sleep(2)
            ig_publish = api_call(
                f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish", "POST",
                {"creation_id": ig_container["id"]},
                {"Authorization": f"Bearer {FB_ACCESS_TOKEN}"}
            )
            if ig_publish.get("id"):
                post_ids["instagram"] = ig_publish["id"]
                already_posted.append("instagram")
                save_state(airtable_record_id, "publish", "in_progress", {"posted_platforms": already_posted})

    all_done = len(already_posted) >= 2  # điều chỉnh theo số platform thật cấu hình
    final_status = "success" if all_done else "failed"
    save_state(airtable_record_id, "publish", final_status, {"posted_platforms": already_posted})

    airtable_update("content_queue", airtable_record_id, {
        "status": "POSTED" if all_done else "PARTIAL_FAIL",
        "post_ids": json.dumps(post_ids)
    })

    return {"status": final_status, "post_ids": post_ids, "already_posted": already_posted}
