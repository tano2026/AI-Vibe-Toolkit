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

def gen_content_with_claude(prompt):
    """Gọi Anthropic API để gen caption"""
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
    result = api_call(url, "POST", payload, headers)
    return result["content"][0]["text"] if "content" in result else None

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
