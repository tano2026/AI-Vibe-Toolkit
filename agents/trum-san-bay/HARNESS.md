# Harness — Trùm Sân Bay

## Vì sao file này tồn tại

Toàn bộ agent trước đó được build tập trung vào **chức năng** (agent làm gì, prompt viết sao) mà chưa có **harness** (khung giữ hệ thống chạy ổn định khi lỗi xảy ra thật, không phải lúc demo). Đây là khoảng trống thật — file này vá lại theo 3 trụ cột Harness Engineering (xem `skills/harness-engineering.md` trong kho gốc).

Nguyên tắc gốc: *"Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."* — không sửa prompt vá tạm, mà xây cơ chế để lỗi đó không lặp lại.

---

## Trụ 1 — Context Engineering (quản lý thông tin)

### Vấn đề hiện tại
Mỗi agent gọi LLM độc lập, không có persistence — nếu Hermes crash giữa chừng lúc đang publish 5 platform, không ai biết đã đăng được platform nào, dễ đăng trùng hoặc bỏ sót.

### Fix — Progress persistence file

```python
# /opt/trum-san-bay/state/progress.json
# Agent đọc/ghi file này ở MỌI bước, không giữ state chỉ trong RAM

import json
import os
from datetime import datetime

STATE_FILE = "/opt/trum-san-bay/state/progress.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE) as f:
        return json.load(f)

def save_state(content_id, step, status, extra=None):
    """
    Gọi hàm này SAU MỖI bước trong pipeline — không đợi xong cả pipeline
    mới ghi 1 lần. Nếu crash giữa chừng, restart đọc lại biết dừng ở đâu.
    """
    state = load_state()
    state[content_id] = {
        "step": step,  # "ideation" | "writer" | "visual" | "brand_check" | "adapter" | "publish" | "done"
        "status": status,  # "in_progress" | "success" | "failed"
        "updated_at": datetime.now().isoformat(),
        "extra": extra or {}
    }
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def resume_incomplete():
    """
    Chạy khi Hermes restart — tìm content nào đang dở, tiếp tục từ đó
    thay vì làm lại từ đầu (tốn token + có thể đăng trùng)
    """
    state = load_state()
    incomplete = {k: v for k, v in state.items() if v["status"] == "in_progress"}
    return incomplete
```

### Fix — Publish idempotency (chống đăng trùng)

```python
def publish_all_platforms_safe(content_id, package, publishers_map, ...):
    """
    Bản có persistence — biết platform nào đã đăng rồi thì skip,
    không đăng lại khi retry sau crash
    """
    state = load_state().get(content_id, {})
    already_posted = state.get("extra", {}).get("posted_platforms", [])

    for platform, publish_fn in publishers_map.items():
        if platform in already_posted:
            continue  # đã đăng rồi, skip — tránh đăng trùng

        result = safe_api_call(platform, publish_fn, package[platform])
        if result["status"] == "success":
            already_posted.append(platform)
            save_state(content_id, "publish", "in_progress",
                       {"posted_platforms": already_posted})

    save_state(content_id, "publish", "success" if len(already_posted) == len(publishers_map) else "failed",
               {"posted_platforms": already_posted})
```

### Fix — Context budget cho Research Agent

Research Agent crawl nhiều nguồn, dễ nhồi quá nhiều raw data vào 1 prompt Claude → tốn token vô ích. Giới hạn cứng:

```python
MAX_ITEMS_PER_SOURCE = {
    "rss": 5,
    "tiktok": 10,
    "facebook": 10
}
# Đã áp trong content-research/SKILL.md — [:5], [:10] trong code — 
# nhưng giờ ghi rõ đây là chủ đích harness, không phải tình cờ
```

---

## Trụ 2 — Architectural Constraints (giới hạn phạm vi)

### Tool access controls — từng agent được làm gì

```
① Research Agent
   ALLOWED: web_search, RSS fetch, Apify API (read-only)
   FORBIDDEN: ghi Airtable trực tiếp status=POSTED, gọi Publisher API

② Ideation Agent
   ALLOWED: đọc ideation_queue, ghi content_queue (status=DRAFT_BRIEF)
   FORBIDDEN: gọi bất kỳ social media API nào

③ Writer Agent
   ALLOWED: đọc brief, ghi caption vào content_queue
   FORBIDDEN: đổi status thành APPROVED (chỉ người mới approve được)

④ Visual Agent
   ALLOWED: gọi HyperFrames, ffmpeg, ghi file vào /opt/trum-san-bay/assets/
   FORBIDDEN: ghi ra ngoài thư mục assets/, xóa file cũ không hỏi

④b Brand Design System
   ALLOWED: đọc asset, validate, reject (gửi lại Visual Agent)
   FORBIDDEN: tự sửa asset — chỉ được reject, không tự ý overlay đè

⑥ Publisher Agent
   ALLOWED: gọi API publish CHỈ KHI status=APPROVED trong Airtable
   FORBIDDEN: publish khi status != APPROVED — đây là guardrail cứng nhất
   REQUIRE HUMAN APPROVAL: mọi lần publish (ở mode semi-auto)

⑦⑧ Comment Monitor / Reply Agent
   ALLOWED: đọc comment, ghi draft reply
   FORBIDDEN: tự động gửi reply khi label=URGENT_COMPLAINT hoặc 
              needs_human_review=true, DÙ ĐANG Ở MODE FULL-AUTO
```

### Structural enforcement — check trước khi cho qua bước tiếp

```python
def enforce_pipeline_gate(content_id, current_step, airtable_get_fn):
    """
    Gọi TRƯỚC mỗi bước — không cho agent nhảy cóc step
    """
    record = airtable_get_fn("content_queue", content_id)
    status = record["fields"]["status"]

    GATE_RULES = {
        "writer": ["DRAFT_BRIEF"],           # Writer chỉ chạy nếu đang ở DRAFT_BRIEF
        "visual": ["CAPTION_READY"],          # Visual chỉ chạy nếu caption xong
        "brand_check": ["ASSET_RAW"],
        "adapter": ["ASSET_APPROVED"],
        "publish": ["APPROVED"],              # Publisher CHỈ chạy nếu người đã approve
    }

    allowed_from = GATE_RULES.get(current_step, [])
    if status not in allowed_from:
        raise PipelineGateError(
            f"{content_id} đang ở status={status}, không đủ điều kiện chạy "
            f"bước {current_step} (cần {allowed_from})"
        )
    return True
```

Đây là chỗ quan trọng nhất bị thiếu trước đó — `agent.py` gốc gọi `publish_post()` mà không check status thật sự đã APPROVED chưa. Giờ bắt buộc gate check trước mọi bước.

### Safety guardrail — filter output trước khi lộ ra ngoài

```python
FORBIDDEN_PATTERNS = [
    r"100%\s*đảm bảo",
    r"cam kết.*hoàn tiền",
    r"giá.*(chỉ|chỉ còn)\s*\d+",  # cam kết giá cụ thể — rủi ro sai lệch
]

def safety_filter(text):
    import re
    issues = []
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f"Match forbidden pattern: {pattern}")
    return {"safe": len(issues) == 0, "issues": issues}

# Gọi filter này sau MỌI output từ Writer + Reply Agent, trước khi vào queue
```

---

## Trụ 3 — Entropy Management (chống rỉ sét)

### Vấn đề sẽ xảy ra theo thời gian
- Hook templates lặp lại, khách quen mặt chữ → hiệu quả giảm dần
- Fact trong `aviation-knowledge` lỗi thời (quy định đổi) mà không ai cập nhật
- Airtable phình to, không dọn record cũ → query chậm dần
- Token API hết hạn âm thầm nếu không có proactive check

### Fix — Audit định kỳ (chạy hàng tuần, sau khi có data thật)

```python
def weekly_entropy_audit():
    """
    Chạy T7 hàng tuần — review sức khỏe hệ thống, không phải content mới
    """
    report = []

    # 1. Check hook có bị lặp không
    recent_hooks = get_hooks_used(weeks=4)
    duplicate_ratio = calculate_duplicate_ratio(recent_hooks)
    if duplicate_ratio > 0.3:
        report.append(f"⚠️ {duplicate_ratio*100:.0f}% hook lặp lại trong 4 tuần — cần đa dạng hook_direction")

    # 2. Check token sắp hết hạn (dùng lại check_token_health từ api-error-handler)
    token_issues = check_token_health()
    report.extend(token_issues)

    # 3. Check engagement trend — content có đang giảm hiệu quả không
    engagement_trend = get_engagement_trend(weeks=4)
    if engagement_trend < -0.15:  # giảm >15%
        report.append(f"⚠️ Engagement giảm {abs(engagement_trend)*100:.0f}% trong 4 tuần — cần review content strategy")

    # 4. Airtable cleanup — archive record cũ hơn 90 ngày
    archived_count = archive_old_records(days=90)
    report.append(f"📦 Đã archive {archived_count} record cũ hơn 90 ngày")

    return report
```

### Fix — aviation-knowledge cần review định kỳ

```
Cron 1 tháng/lần: /tsb audit-facts
→ Research Agent chạy lại, so sánh fact hiện tại trong 
  skills/aviation-knowledge/SKILL.md với tin tức mới nhất từ RSS hãng bay
→ Nếu phát hiện thay đổi (vd quy định hành lý mới) → alert Nobitano, 
  KHÔNG tự động sửa file skill (fact về quy định cần người xác nhận trước khi 
  đổi baseline)
```

---

## Bảng tổng kết — Harness đã áp cho từng agent

| Agent | Context (Trụ 1) | Constraint (Trụ 2) | Entropy (Trụ 3) |
|-------|-----------------|---------------------|-------------------|
| Research | Limit item/nguồn, không nhồi hết | Read-only, không ghi status POSTED | Audit fact hàng tháng |
| Ideation | Check lịch sử 4 tuần chống trùng | Không gọi social API | Track hook repetition |
| Writer | Fact injection có giới hạn | Không tự approve | Safety filter mọi output |
| Visual | — | Chỉ ghi trong /assets/ | — |
| Publisher | Idempotent — biết platform nào đã đăng | **Gate cứng: chỉ chạy khi status=APPROVED** | Token health check hàng ngày |
| Reply | — | URGENT luôn cần người, dù full-auto | — |

---

## Việc còn phải làm để harness hoàn chỉnh

1. ~~`enforce_pipeline_gate()` cần được code hóa vào `agent.py`~~ ✅ Đã xong — 
   `publish_post_safe()` trong `agent.py` gọi gate check trước khi publish
2. ~~`progress.json` chưa có file lock~~ ✅ Đã xong — `_with_state_lock()` dùng 
   `fcntl.flock` chống race condition khi 2 process cùng ghi
3. Chưa có dashboard xem `progress.json` trực quan — hiện phải đọc JSON tay 
   (còn nợ, độ ưu tiên thấp — không chặn vận hành)
4. ~~`publish_post_safe()` mới code cứng 2 platform~~ ✅ Đã xong — mở rộng đủ 
   4 platform (Facebook, Instagram, TikTok, YouTube), mỗi platform có hàm 
   riêng `_publish_*()`, retry theo bảng lỗi trong `api-error-handler`, chỉ 
   đăng platform nào có credential cấu hình (cho phép launch dần platform), 
   và `PipelineGateError`/`BudgetExceededError` được bắt riêng trong 
   `handle_command()` để trả message rõ ràng thay vì crash im lặng

## Việc còn nợ thật (chưa test với credential thật)

- TikTok publisher dùng `PULL_FROM_URL` — cần video có URL public truy cập 
  được từ ngoài (vd host qua nginx trên VPS), chưa verify với account TikTok 
  Developer thật
- YouTube publisher dùng resumable upload thuần urllib — chưa test với OAuth 
  token thật, `YOUTUBE_ACCESS_TOKEN` cần refresh định kỳ (access token chỉ 
  sống 1h) — refresh flow riêng CHƯA code, hiện giả định token luôn valid
- Chưa có dashboard xem `progress.json` trực quan (độ ưu tiên thấp)

---

## Về Superpowers

`superpowers` skill trong kho là cho **Claude Code** (think-before-code, TDD, self-review khi viết code) — không áp trực tiếp cho runtime agent của Trùm Sân Bay vì đây không phải coding agent. Nhưng nguyên tắc "self-review trước khi output" đã áp gián tiếp qua `self_check` field trong Writer prompt và `needs_human_review` trong Reply prompt — cùng tinh thần, khác cơ chế.
