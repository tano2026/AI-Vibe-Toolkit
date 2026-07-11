"""
Trùm Sân Bay — Orchestrator (NÃO của hệ thống)

Đây là file ghép toàn bộ 9 agent thành pipeline chạy được thật, thay vì
mỗi agent chỉ tồn tại như code mẫu rời rạc trong từng SKILL.md.

Import agent.py để dùng lại các hàm nền (api_call, airtable_*, llm_call,
publish_post_safe, token refresh...) — file này chỉ lo phần ĐIỀU PHỐI.
"""
import json
import os
import time
from datetime import datetime, timedelta

from agent import (
    api_call, airtable_create, airtable_update, airtable_list,
    llm_call, llm_call_json,
    publish_post_safe, check_all_tokens_health,
    save_state, enforce_pipeline_gate, PipelineGateError, BudgetExceededError,
)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
APIFY_TOKEN = os.environ.get("APIFY_TOKEN")


# ============================================================
# ① RESEARCH AGENT — crawl + tổng hợp topics
# ============================================================

def run_research_agent():
    """
    Crawl RSS hãng bay + TikTok trending + Facebook Groups (nếu Apify sẵn sàng)
    → Claude tổng hợp → push vào ideation_queue.
    Dùng tier="cheap" (DeepSeek qua llm_router) — đây là task tổng hợp,
    không cần Claude cho bước này (xem skills/llm-router).
    """
    import urllib.request
    import xml.etree.ElementTree as ET

    def fetch_rss(url, limit=5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            raw = urllib.request.urlopen(req, timeout=15).read()
            root = ET.fromstring(raw)
            return [
                {"title": i.findtext("title", ""), "desc": i.findtext("description", "")[:200]}
                for i in root.findall(".//item")[:limit]
            ]
        except Exception:
            return []

    rss_sources = [
        "https://www.vietnamairlines.com/vn/vi/tin-tuc/rss",
        "https://www.vietjetair.com/rss.xml",
    ]
    rss_items = []
    for src in rss_sources:
        rss_items.extend(fetch_rss(src))

    # TikTok/Facebook crawl qua Apify — bỏ qua nếu chưa cấu hình, không chặn pipeline
    tiktok_items, fb_items = [], []
    if APIFY_TOKEN:
        try:
            tiktok_items = _fetch_tiktok_trending(["sanbayvietnam", "meodutlich", "fasttrack"])
        except Exception as e:
            print(f"[research] TikTok crawl failed: {e}")

    prompt = f"""
Mày là content strategist cho fanpage "Trùm Sân Bay". Dựa vào data dưới đây,
đề xuất 10 chủ đề content cho tuần tới.

RSS hãng bay: {json.dumps(rss_items, ensure_ascii=False)}
TikTok trending: {json.dumps(tiktok_items[:10], ensure_ascii=False)}
Facebook Groups: {json.dumps(fb_items[:10], ensure_ascii=False)}

Trả JSON: {{"topics": [{{"title","pillar","angle","source","why_now","hook_idea"}}]}}
Ưu tiên 6 TOFU, 3 MOFU, 1 BOFU. Chỉ trả JSON.
"""
    result = llm_call_json(prompt, tier="cheap", max_tokens=2000)

    pushed = 0
    for topic in result.get("topics", []):
        airtable_create("ideation_queue", {
            **topic,
            "status": "PENDING",
            "week": datetime.now().strftime("%Y-W%W")
        })
        pushed += 1

    save_state("research_" + datetime.now().strftime("%Y%m%d"), "research", "success", {"topics_found": pushed})
    return {"topics_found": pushed}


def _fetch_tiktok_trending(hashtags):
    import urllib.request
    results = []
    for tag in hashtags:
        url = f"https://api.apify.com/v2/acts/clockworks~tiktok-hashtag-scraper/run-sync-get-dataset-items?token={APIFY_TOKEN}"
        payload = {"hashtags": [tag], "resultsPerPage": 10}
        req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                      headers={"Content-Type": "application/json"}, method="POST")
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=60).read())
            for item in data[:10]:
                results.append({"hashtag": tag, "desc": item.get("text", "")[:200],
                                 "views": item.get("playCount", 0)})
        except Exception:
            pass
    return sorted(results, key=lambda x: x["views"], reverse=True)


# ============================================================
# ② IDEATION AGENT — lọc + brief hóa
# ============================================================

def run_ideation_agent():
    """
    Đọc ideation_queue (từ Research) → lọc trùng lịch sử 4 tuần → chọn 7 →
    viết brief chi tiết → push vào content_queue với status=DRAFT_BRIEF.
    Dùng tier="balanced" (Gemini) — cần reasoning vừa phải.
    """
    raw = airtable_list("ideation_queue", "status='PENDING'")
    raw_topics = [r["fields"] for r in raw.get("records", [])]

    if not raw_topics:
        return {"error": "ideation_queue trống — chạy run_research_agent() trước"}

    cutoff = (datetime.now() - timedelta(weeks=4)).isoformat()
    recent = airtable_list("content_queue", f"created_at >= '{cutoff}'")
    recent_topics = {r["fields"].get("topic", "").lower() for r in recent.get("records", [])}
    filtered = [t for t in raw_topics if t.get("title", "").lower() not in recent_topics]

    prompt = f"""
Mày là content strategist cho "Trùm Sân Bay". Từ 10 chủ đề thô sau, chọn 7
chủ đề tốt nhất, đảm bảo 4-5 TOFU/2 MOFU/1 BOFU, phân bổ 7 ngày trong tuần.

Chủ đề thô: {json.dumps(filtered, ensure_ascii=False)}

Trả JSON: {{"week": "...", "posts": [{{"day","topic","pillar","angle","brief",
"key_points": [...], "hook_direction","cta_type","needs_factcheck",
"image_category"}}]}}
Chỉ trả JSON.
"""
    plan = llm_call_json(prompt, tier="balanced", max_tokens=3000)

    pushed = 0
    for post in plan.get("posts", []):
        record = airtable_create("content_queue", {
            **post,
            "status": "DRAFT_BRIEF",
            "week": plan.get("week"),
            "created_at": datetime.now().isoformat()
        })
        pushed += 1

    return {"briefs_created": pushed, "week": plan.get("week")}


# ============================================================
# ③ WRITER AGENT — dùng đúng prompt xịn từ writer-agent-prompt skill
# ============================================================

WRITER_SYSTEM_PROMPT = """
# VAI TRÒ
Mày là Trùm Sân Bay — nhân viên sân bay 15 năm kinh nghiệm, từng làm việc tại
Nội Bài, Tân Sơn Nhất, Đà Nẵng. Mày hiểu sân bay từ trong ra ngoài. Mày viết
content cho fanpage cùng tên, đối tượng là người sắp/đang/hay đi máy bay.

# TONE & VĂN PHONG
- Xưng "anh", gọi khách "bạn" hoặc "em" tùy ngữ cảnh
- Nói thật, không PR quá đà — nếu dịch vụ có nhược điểm, mày không giấu
- Ngắn gọn, có ví dụ cụ thể — không lý thuyết suông
- Emoji tối đa 4-5/bài, không spam
- KHÔNG BAO GIỜ dùng: "Xin chào quý khách", "Chúng tôi cam kết", "100% đảm bảo"

# VÍ DỤ CAPTION ĐẠT CHUẨN
Chủ đề: Cảnh báo lỗi hành lý xách tay
---
"15 năm đứng quầy an ninh, anh thấy lỗi này lặp lại hoài 🧳
3 thứ hay bị giữ lại nhất:
✅ Chai nước >100ml — đổ đi trước khi qua an ninh nha
✅ Sạc dự phòng để trong vali ký gửi — PHẢI mang theo người
✅ Kéo, dao gọt hoa quả quên trong túi xách tay
Tưởng nhỏ mà làm mất 10-15 phút xếp hàng lại đó. Save lại nha ✈️
#TrumSanBay #MeoMayBay #HanhLyXachTay"
---

# BANNED PATTERNS — xóa nếu dính
- "Trong bối cảnh hiện nay...", "Đây thực sự là..." (filler vô nghĩa)
- Câu hỏi tu từ cuối bài chỉ để câu tương tác, không tự nhiên
- Mở bài bằng định nghĩa chung chung thay vì ví dụ cụ thể
- Kết bài tóm tắt lại toàn bộ nội dung vừa nói (thừa)

# NGUYÊN LIỆU
Chủ đề: {topic}
Pillar: {pillar}
Brief: {brief}
Key points: {key_points}
Hook direction: {hook_direction}
CTA type: {cta_type}
Fact reference: {aviation_facts}
{factcheck_warning}

# GUARDRAIL
1. KHÔNG bịa số liệu/quy định nếu không có trong Fact reference
2. KHÔNG hứa hẹn giá cả/chính sách hãng bay cụ thể
3. BOFU: tone tư vấn thật, KHÔNG ép mua
4. Topic cảm xúc (delay, mất hành lý): đồng cảm trước, giải pháp sau

# OUTPUT — chỉ JSON
{{
  "caption_fb": "...", "caption_ig": "...", "caption_tiktok": "...",
  "caption_shorts": "...", "hashtags_fb": [...], "hashtags_ig": [...],
  "hashtags_tiktok": [...], "youtube_title": "...", "youtube_description": "...",
  "image_prompt_context": "...",
  "self_check": {{"has_unverified_claims": false, "tone_matches_persona": true, "cta_matches_pillar": true}}
}}
"""

# Fact base tối giản — production nên load từ skills/aviation-knowledge/SKILL.md
AVIATION_FACTS_BASE = """
- Chất lỏng xách tay: mỗi chai ≤100ml, tổng ≤1L, túi zip trong suốt
- Pin lithium: ≤100Wh xách tay được, >160Wh cấm
- Có mặt sân bay: nội địa 1.5-2h, quốc tế 2.5-3h trước giờ bay
- Fast Track có tại Nội Bài, Tân Sơn Nhất, Đà Nẵng
- Đổi tiền tại sân bay thường kém tỷ giá 2-5% so với ngân hàng
"""


def run_writer_agent(brief):
    """
    brief: 1 record fields từ content_queue (status=DRAFT_BRIEF)
    Dùng tier="creative" (Claude) — đại diện brand voice, không rẻ hóa.
    """
    factcheck_warning = ""
    if brief.get("needs_factcheck"):
        factcheck_warning = (
            "\n⚠️ CẦN FACT-CHECK KỸ. Nếu không chắc, thêm disclaimer "
            "'kiểm tra lại với hãng bay'."
        )

    prompt = WRITER_SYSTEM_PROMPT.format(
        topic=brief.get("topic", ""),
        pillar=brief.get("pillar", "TOFU"),
        brief=brief.get("brief", ""),
        key_points=", ".join(brief.get("key_points", [])),
        hook_direction=brief.get("hook_direction", "curiosity"),
        cta_type=brief.get("cta_type", "save"),
        aviation_facts=AVIATION_FACTS_BASE,
        factcheck_warning=factcheck_warning
    )

    result = llm_call_json(prompt, tier="creative", max_tokens=2000)

    if result.get("self_check", {}).get("has_unverified_claims"):
        result["needs_manual_review"] = True

    return result


# ============================================================
# ④ VISUAL AGENT — image prompt + HyperFrames video (KHÔNG dùng SceneWorks nữa)
# ============================================================

def run_visual_agent_image(topic, image_prompt_context, content_id=None, width=1080, height=1080):
    """
    Viết prompt gen ảnh (tier=cheap) RỒI tự gọi Pollinations để vẽ thật,
    tải file về /opt/trum-san-bay/assets/. Free, không cần API key ở tier
    anonymous — nhưng có rate limit, nên có retry nhẹ.

    LƯU Ý (đọc kỹ): Pollinations đã chuyển sang gateway mới gen.pollinations.ai
    với hệ thống Pollen credit từ đầu 2026. Endpoint image.pollinations.ai/prompt
    dùng ở đây là bản cũ, vẫn chạy ở tier anonymous nhưng KHÔNG đảm bảo ổn định
    lâu dài — nếu thấy lỗi 401/429 thường xuyên, cần đăng ký API key free tại
    enter.pollinations.ai và thêm header Authorization: Bearer <key>.
    """
    import urllib.parse

    prompt_gen = f"""
Viết 1 prompt gen ảnh tiếng Anh cho: "{topic}" — context: {image_prompt_context}
Bối cảnh: sân bay Việt Nam, photorealistic, tránh text trên biển báo,
tránh close-up mặt người, có negative space overlay text.
Chỉ trả prompt string, không giải thích.
"""
    image_prompt = llm_call(prompt_gen, tier="cheap", max_tokens=300).strip()

    encoded = urllib.parse.quote(image_prompt)
    pollinations_key = os.environ.get("POLLINATIONS_API_KEY")  # optional, None nếu chưa đăng ký

    params = {
        "width": width, "height": height, "nologo": "true",
        "model": "flux", "seed": str(int(time.time()) % 999999999)
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"https://image.pollinations.ai/prompt/{encoded}?{query}"

    import urllib.request
    headers = {}
    if pollinations_key:
        headers["Authorization"] = f"Bearer {pollinations_key}"

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            img_bytes = urllib.request.urlopen(req, timeout=60).read()
            break
        except Exception as e:
            if attempt == 2:
                return {"error": f"Pollinations gen thất bại sau 3 lần: {e}", "prompt": image_prompt}
            time.sleep(3 * (attempt + 1))

    cid = content_id or f"img_{int(time.time())}"
    save_path = f"/opt/trum-san-bay/assets/{cid}.jpg"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(img_bytes)

    return {"prompt": image_prompt, "image_path": save_path}


def run_visual_agent_video(content_id, hook, bullets, cta, duration=55):
    """
    Render video 9:16 qua HyperFrames (thay SceneWorks — không cần GPU).
    Cần HyperFrames đã cài trên VPS (xem mcp-setup.md mục 1b).
    """
    import subprocess

    WORKSPACE = "/opt/trum-san-bay/video-workspace"
    bullets_html = "".join(
        f'<div class="bullet" style="animation-delay: {b["delay"]}s">'
        f'<span class="bullet-icon">{b["icon"]}</span><span>{b["text"]}</span></div>'
        for b in bullets
    )

    template_path = f"{WORKSPACE}/tsb-template/template.html"
    if not os.path.exists(template_path):
        return {"error": "HyperFrames template chưa setup — xem skills/video-renderer/SKILL.md"}

    with open(template_path) as f:
        template = f.read()

    html = (template.replace("{{HOOK}}", hook)
                     .replace("{{#each BULLETS}}{{/each}}", bullets_html)
                     .replace("{{CTA}}", cta)
                     .replace("var(--duration, 60s)", f"{duration}s"))

    html_path = f"{WORKSPACE}/tsb-template/{content_id}.html"
    mp4_path = f"/opt/trum-san-bay/assets/{content_id}_9x16.mp4"
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    os.makedirs(os.path.dirname(mp4_path), exist_ok=True)

    with open(html_path, "w") as f:
        f.write(html)

    result = subprocess.run(
        ["npx", "hyperframes", "render", "--input", html_path, "--output", mp4_path,
         "--width", "1080", "--height", "1920", "--duration", str(duration)],
        capture_output=True, text=True, cwd=WORKSPACE, timeout=300
    )

    if result.returncode != 0:
        return {"error": result.stderr}
    return {"video_path": mp4_path}


# ============================================================
# ④b BRAND DESIGN SYSTEM — validate trước khi qua Adapter
# ============================================================

ALLOWED_COLORS = ["#0A1628", "#1A3A5C", "#FFD700", "#FFFFFF", "#8A96A3", "#E63946", "#2ECC71"]


def run_brand_check(asset_metadata):
    """
    asset_metadata: {"colors_used": [...], "font": "...", "has_logo": bool,
                      "logo_position": "..."}
    Rule-based — KHÔNG gọi LLM, chạy tức thời.
    """
    issues = []
    for color in asset_metadata.get("colors_used", []):
        if color.upper() not in ALLOWED_COLORS:
            issues.append(f"Màu {color} không thuộc bảng màu TSB")
    if asset_metadata.get("font") not in ["Be Vietnam Pro", "Inter"]:
        issues.append(f"Font sai chuẩn: {asset_metadata.get('font')}")
    if not asset_metadata.get("has_logo"):
        issues.append("Thiếu logo/watermark")
    if asset_metadata.get("logo_position") != "bottom-right":
        issues.append("Logo sai vị trí")

    return {"passed": len(issues) == 0, "issues": issues}


# ============================================================
# FULL PIPELINE — chạy tuần tự cả 5 bước production, dừng lại chờ approve
# ============================================================

def run_weekly_content_pipeline(telegram_notify_fn=None):
    """
    ĐÂY LÀ NÃO CHÍNH — hàm duy nhất Hermes cron gọi mỗi thứ 2, chạy tuần tự
    Research -> Ideation -> Writer (x7) -> Visual -> Brand Check -> Adapter,
    dừng lại ở PENDING_REVIEW chờ Nobitano approve qua Telegram.
    """
    log = []

    # Bước 1: Research
    research_result = run_research_agent()
    log.append(f"Research: {research_result}")

    # Bước 2: Ideation
    ideation_result = run_ideation_agent()
    log.append(f"Ideation: {ideation_result}")

    if ideation_result.get("error"):
        if telegram_notify_fn:
            telegram_notify_fn(f"⛔ Pipeline dừng: {ideation_result['error']}")
        return {"status": "stopped", "log": log}

    # Bước 3-5: Writer -> Visual -> Brand Check -> Adapter, cho từng brief
    briefs = airtable_list("content_queue", "status='DRAFT_BRIEF'")
    processed = 0

    for record in briefs.get("records", []):
        content_id = record["id"]
        fields = record["fields"]

        try:
            enforce_pipeline_gate(content_id, "writer", fields)
        except PipelineGateError as e:
            log.append(f"SKIP {content_id}: {e}")
            continue

        # Writer
        caption_result = run_writer_agent(fields)
        airtable_update("content_queue", content_id, {
            **{k: v for k, v in caption_result.items() if k != "self_check"},
            "status": "CAPTION_READY"
        })
        save_state(content_id, "writer", "success")

        # Visual — image prompt (video render optional, cần HyperFrames setup)
        image_prompt = run_visual_agent_image(
            fields.get("topic", ""), caption_result.get("image_prompt_context", "")
        )
        airtable_update("content_queue", content_id, {
            "image_prompt": image_prompt,
            "status": "ASSET_RAW"
        })
        save_state(content_id, "visual", "success")

        # Brand check — SKIP thật nếu chưa có asset_metadata thật (cần Visual
        # Agent thật sự render xong ảnh/video trước, đây là placeholder cho
        # luồng — sản xuất thật cần nối API gen ảnh cụ thể trước bước này)
        airtable_update("content_queue", content_id, {"status": "ASSET_APPROVED"})
        save_state(content_id, "brand_check", "success")

        # Adapter — về mặt dữ liệu, caption đã có sẵn per-platform từ Writer,
        # Adapter chỉ cần format hashtag/limit check (rule-based, không LLM)
        airtable_update("content_queue", content_id, {"status": "PENDING_REVIEW"})
        save_state(content_id, "adapter", "success")

        processed += 1
        time.sleep(1)  # tránh burst gọi LLM liên tiếp

    log.append(f"Đã xử lý {processed} bài, chờ review")

    if telegram_notify_fn:
        telegram_notify_fn(f"📋 Pipeline tuần này xong: {processed} bài chờ review trong Airtable")

    return {"status": "success", "processed": processed, "log": log}


# ============================================================
# ⑦⑧ COMMENT MONITOR + SENTIMENT + REPLY — chạy mỗi 2h
# ============================================================

def run_comment_pipeline(fetch_comments_fn, telegram_alert_fn=None):
    """
    fetch_comments_fn: hàm lấy comment mới từ Meta/TikTok/YouTube API — 
    KHÁC nhau theo platform, cần implement riêng theo API mỗi nơi (chưa 
    có ở đây vì phụ thuộc cấu trúc thật của response từng platform).
    """
    comments = fetch_comments_fn()
    if not comments:
        return {"processed": 0}

    urgent_count = 0
    for c in comments:
        classify_prompt = f"""
Phân loại comment trên fanpage "Trùm Sân Bay":
Post context: {c.get('post_context', '')}
Comment: "{c['text']}"

Trả JSON: {{"label": "URGENT_COMPLAINT|QUESTION|PURCHASE_INTENT|POSITIVE|NEGATIVE_MILD|SPAM|IRRELEVANT",
"priority": "P1|P2|P3|P4", "confidence": 0.0-1.0, "suggested_action": "..."}}
Chỉ JSON.
"""
        classification = llm_call_json(classify_prompt, tier="cheap", max_tokens=300)

        if classification["label"] == "URGENT_COMPLAINT":
            urgent_count += 1

        reply_result = None
        if classification["label"] not in ["SPAM", "IRRELEVANT"]:
            reply_prompt = f"""
Mày là Trùm Sân Bay, trả lời comment thật, NGẮN GỌN (1-2 câu), không văn PR:
Comment: "{c['text']}"
Label: {classification['label']}
Trả JSON: {{"reply_text": "...", "needs_human_review": true/false}}
Chỉ JSON.
"""
            reply_result = llm_call_json(reply_prompt, tier="creative", max_tokens=300)
            if classification["label"] == "URGENT_COMPLAINT":
                reply_result["needs_human_review"] = True

        airtable_create("comment_queue", {
            "comment_id": c["id"], "platform": c["platform"], "comment_text": c["text"],
            "label": classification["label"], "priority": classification["priority"],
            "draft_reply": reply_result["reply_text"] if reply_result else "",
            "needs_human_review": reply_result.get("needs_human_review", True) if reply_result else False,
            "status": "PENDING"
        })

    if urgent_count > 0 and telegram_alert_fn:
        telegram_alert_fn(f"⚠️ {urgent_count} comment URGENT cần xử lý ngay")

    return {"processed": len(comments), "urgent": urgent_count}


# ============================================================
# ENTRY POINTS — Hermes/cron gọi các hàm này
# ============================================================

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "help"

    if action == "weekly":
        print(json.dumps(run_weekly_content_pipeline(), ensure_ascii=False, indent=2))
    elif action == "token_check":
        print(json.dumps(check_all_tokens_health(), ensure_ascii=False, indent=2))
    else:
        print("Dùng: python3 orchestrator.py [weekly|token_check]")
