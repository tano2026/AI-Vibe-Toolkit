# LLM Router — Chọn Model Đúng Việc, Đúng Giá

## Mô tả
Không phải task nào cũng cần Claude. Skill này định nghĩa: task nào dùng model nào, qua OmniRoute gateway đang chạy sẵn trên VPS — tiết kiệm chi phí mà vẫn giữ chất lượng ở chỗ cần.

## Nguyên tắc phân bổ

```
DeepSeek V3/Flash  → Task đơn giản, khối lượng lớn, không cần sáng tạo cao
                      (classify, extract, format, summarize ngắn)

DeepSeek R1         → Task cần reasoning nhưng không cần văn phong hay
                      (lọc trùng, đánh giá logic, quyết định routing)

Gemini Flash/Pro     → Task cần đa ngôn ngữ tốt + tốc độ, giá giữa
                      (research synthesis, dịch, tóm tắt dài)

Claude Sonnet        → Task cần sáng tạo, văn phong, tone chuẩn, fact-sensitive
                      (viết caption, reply comment, brand voice)
```

## Bảng phân bổ theo agent — Trùm Sân Bay

| Agent | Task | Model đề xuất | Lý do |
|-------|------|---------------|-------|
| ① Research | Tổng hợp raw data → topics | **DeepSeek V3** | Task extract/summarize, không cần văn hay |
| ② Ideation | Lọc + brief hóa 7 bài | **Gemini Flash** | Cần reasoning vừa phải + tốc độ |
| ③ Writer | Viết caption 5 platform | **Claude Sonnet** | Văn phong + tone brand là core value, không thể rẻ hóa |
| ④ Image prompt | Viết prompt gen ảnh | **DeepSeek V3** | Task kỹ thuật, template hóa cao |
| ⑦ Sentiment | Classify comment | **DeepSeek V3** | Classification thuần, khối lượng lớn, không cần văn hay |
| ⑧ Reply | Viết reply comment | **Claude Sonnet** | Đại diện brand nói chuyện trực tiếp với khách — không rẻ hóa |
| Fact-check | Verify thông tin hàng không | **Claude Sonnet** | Độ chính xác quan trọng hơn giá |

**Quy tắc:** Bất cứ chỗ nào **đại diện trực tiếp giọng nói thương hiệu** (Writer, Reply, Fact-check) → luôn Claude. Chỗ nào **xử lý nội bộ, không lộ ra ngoài** (Research, Sentiment, Image prompt) → dùng model rẻ hơn.

## Code Router — gọi qua OmniRoute

```python
import json
import os
import urllib.request

OMNIROUTE_URL = os.environ.get("OMNIROUTE_URL", "http://localhost:PORT/v1/chat/completions")
OMNIROUTE_KEY = os.environ.get("OMNIROUTE_API_KEY")

MODEL_MAP = {
    "cheap": "deepseek-v3",           # extract, classify, format
    "reasoning": "deepseek-r1",        # logic, dedup, decision
    "balanced": "gemini-2.0-flash",    # synthesis, translate, summarize
    "creative": "claude-sonnet-4-6",   # brand voice, caption, reply
    "factcheck": "claude-sonnet-4-6",  # accuracy-critical
}

def llm_call(prompt, tier="cheap", max_tokens=1500, temperature=0.7):
    """
    Universal LLM call — route theo tier, không hardcode model ở từng chỗ gọi
    tier: cheap | reasoning | balanced | creative | factcheck
    """
    model = MODEL_MAP.get(tier, "deepseek-v3")

    # Claude dùng Anthropic API trực tiếp (không qua OmniRoute vì cần citation/tool use sau này)
    if model.startswith("claude"):
        return _call_anthropic(prompt, model, max_tokens, temperature)

    # Còn lại qua OmniRoute (OpenAI-compatible format)
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    req = urllib.request.Request(
        OMNIROUTE_URL,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {OMNIROUTE_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    result = json.loads(urllib.request.urlopen(req, timeout=60).read())
    return result["choices"][0]["message"]["content"]


def _call_anthropic(prompt, model, max_tokens, temperature):
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
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return result["content"][0]["text"]


def llm_call_json(prompt, tier="cheap", max_tokens=1500):
    """Wrapper — parse JSON response, retry 1 lần nếu parse fail"""
    raw = llm_call(prompt, tier=tier, max_tokens=max_tokens, temperature=0.5)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Retry với instruction nhấn mạnh JSON-only
        retry_prompt = prompt + "\n\nQUAN TRỌNG: Chỉ trả về JSON hợp lệ, không markdown, không giải thích."
        raw2 = llm_call(retry_prompt, tier=tier, max_tokens=max_tokens, temperature=0.3)
        return json.loads(raw2)
```

## Ước tính chi phí/tháng (1 fanpage, nhịp 7 bài/tuần)

| Agent | Calls/tuần | Model | Chi phí ước tính/tháng |
|-------|-----------|-------|------------------------|
| Research | 4 (1/tuần) | DeepSeek V3 | ~$0.10 |
| Ideation | 4 | Gemini Flash | ~$0.20 |
| Writer | 28 (7 bài × 4 tuần) | Claude Sonnet | ~$2-3 |
| Image prompt | 28 | DeepSeek V3 | ~$0.15 |
| Sentiment | ~200 comment/tháng | DeepSeek V3 | ~$0.30 |
| Reply | ~80 comment cần reply | Claude Sonnet | ~$1-2 |
| Fact-check | ~15 bài cần verify | Claude Sonnet | ~$0.50 |
| **Tổng** | | | **~$4-6/tháng** |

So với dùng Claude cho toàn bộ pipeline: ước tính ~$15-20/tháng. Router tiết kiệm ~70%.

## Fallback khi model rẻ fail

```python
def llm_call_with_fallback(prompt, tier="cheap", max_tokens=1500):
    """Nếu model rẻ lỗi/timeout → tự động fallback lên Claude"""
    try:
        return llm_call(prompt, tier=tier, max_tokens=max_tokens)
    except Exception as e:
        print(f"[LLM Router] {tier} model failed ({e}), falling back to Claude")
        return llm_call(prompt, tier="creative", max_tokens=max_tokens)
```

## Lưu ý setup

- OmniRoute đã chạy sẵn trên VPS — chỉ cần set `OMNIROUTE_URL` và `OMNIROUTE_API_KEY` trong pm2 env
- Tên model (`deepseek-v3`, `gemini-2.0-flash`...) phải khớp đúng với config OmniRoute đang route — check lại tên chính xác trong OmniRoute dashboard trước khi deploy
- `temperature` thấp (0.3-0.5) cho task classify/extract, cao hơn (0.7-0.9) cho task sáng tạo (Writer, Reply)


---

## Prompt Caching — tiết kiệm thêm cho Writer/Reply prompt dài

System prompt của Writer Agent (~2000 token) được gọi 28 lần/tháng — cache 
phần cố định (persona, tone matrix, few-shot examples, banned patterns), 
chỉ phần biến đổi (topic, brief) mới tính token mới mỗi lần gọi.

```python
def llm_call_cached(system_prompt_static, user_content_variable, model="claude-sonnet-4-6", max_tokens=2000):
    """
    Dùng cho Writer + Reply — phần persona/rule cố định được cache, 
    chỉ trả tiền đầy đủ ở lần gọi đầu, các lần sau rẻ hơn nhiều (~90% giảm 
    cho phần cached).
    """
    import os, json, urllib.request

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": system_prompt_static,
                    "cache_control": {"type": "ephemeral"}
                },
                {
                    "type": "text",
                    "text": user_content_variable
                }
            ]
        }]
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    result = json.loads(urllib.request.urlopen(req).read())
    return result["content"][0]["text"]
```

**Áp dụng:** Tách `WRITER_SYSTEM_PROMPT` (persona + few-shot + banned patterns 
— phần không đổi) khỏi phần `{topic}, {brief}, {key_points}` (phần đổi mỗi 
bài) — gọi qua `llm_call_cached()` thay vì nhét chung 1 khối như hiện tại.

## Budget Tracker — theo dõi chi phí tích lũy, chặn khi vượt ngưỡng

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CostRecord:
    agent: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float

@dataclass(frozen=True, slots=True)
class CostTracker:
    budget_limit_monthly: float = 10.00  # ngưỡng an toàn cho 1 fanpage
    records: tuple = ()

    def add(self, record):
        return CostTracker(self.budget_limit_monthly, (*self.records, record))

    @property
    def total_cost(self):
        return sum(r.cost_usd for r in self.records)

    @property
    def over_budget(self):
        return self.total_cost > self.budget_limit_monthly

    def by_agent(self):
        """Breakdown chi phí theo agent — biết agent nào đang tốn nhất"""
        breakdown = {}
        for r in self.records:
            breakdown[r.agent] = breakdown.get(r.agent, 0) + r.cost_usd
        return breakdown


# Check trước MỖI lần gọi LLM trong pipeline
def guarded_llm_call(prompt, tier, tracker, agent_name, telegram_alert_fn):
    if tracker.over_budget:
        telegram_alert_fn(
            f"🔴 Budget vượt ngưỡng ${tracker.budget_limit_monthly}/tháng "
            f"— pipeline TẠM DỪNG, cần review"
        )
        raise BudgetExceededError(tracker.total_cost, tracker.budget_limit_monthly)
    return llm_call(prompt, tier=tier)
```

**Nguồn:** kết hợp từ `skills/ecc/cost-aware-llm-pipeline` (kho gốc) — pattern 
immutable dataclass tránh side-effect khi nhiều agent cùng update tracker.
