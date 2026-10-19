"""
Trùm Sân Bay — LLM Router (hiện thực thật của skills/llm-router/SKILL.md)

- llm_call(prompt, tier, max_tokens, temperature): route theo tier, KHÔNG hardcode
  model ở chỗ gọi. Claude đi thẳng Anthropic API, còn lại qua OmniRoute
  (định dạng OpenAI-compatible).
- CostTracker bất biến: MỖI lần gọi thành công đều GHI chi phí (ước tính theo
  bảng giá PRICING_PER_MTOK + usage trong phản hồi); khi tổng chi phí tháng vượt
  ngưỡng thì lần gọi kế tiếp bị chặn bằng BudgetExceededError.
- Điểm chạm mạng duy nhất là _http_post_json() — test/mock chỉ cần patch hàm này.

Biến môi trường (đúng tên trong SKILL.md, KHÔNG có khoá nào trong mã):
  OMNIROUTE_URL, OMNIROUTE_API_KEY, ANTHROPIC_API_KEY
Biến phụ (tuỳ chọn):
  TSB_BUDGET_MONTHLY_USD  ngưỡng ngân sách tháng, mặc định 10.00
  TSB_COST_FILE           nếu đặt: lưu/đọc lịch sử chi phí ở file JSON này
                          (không đặt thì chỉ giữ trong bộ nhớ tiến trình)

Giá trong PRICING_PER_MTOK là ƯỚC TÍNH để chặn ngân sách, không phải hoá đơn;
chỉnh lại theo bảng giá thật của OmniRoute/Anthropic trước khi tin con số.
"""
import json
import os
import threading
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime

OMNIROUTE_DEFAULT_URL = "http://localhost:PORT/v1/chat/completions"  # placeholder như SKILL.md

MODEL_MAP = {
    "cheap": "deepseek-v3",           # extract, classify, format
    "reasoning": "deepseek-r1",       # logic, dedup, decision
    "balanced": "gemini-2.0-flash",   # synthesis, translate, summarize
    "creative": "claude-sonnet-4-6",  # brand voice, caption, reply
    "factcheck": "claude-sonnet-4-6",  # accuracy-critical
}

# USD cho 1 triệu token: (input, output). ƯỚC TÍNH — xem docstring đầu file.
PRICING_PER_MTOK = {
    "deepseek-v3": (0.27, 1.10),
    "deepseek-r1": (0.55, 2.19),
    "gemini-2.0-flash": (0.10, 0.40),
    "claude-sonnet-4-6": (3.00, 15.00),
}
DEFAULT_PRICE = (3.00, 15.00)  # model lạ: tính theo giá cao nhất để không đánh giá thấp chi phí

DEFAULT_BUDGET_MONTHLY = 10.00


class BudgetExceededError(Exception):
    def __init__(self, current, limit):
        self.current = current
        self.limit = limit
        super().__init__(f"Budget exceeded: ${current:.2f} / ${limit:.2f}")


class LLMConfigError(Exception):
    """Thiếu biến môi trường bắt buộc cho tier được gọi."""


class LLMCallError(Exception):
    """Lỗi HTTP/định dạng khi gọi LLM (không chứa khoá)."""


# === COST TRACKER (bất biến, theo SKILL.md) ===

@dataclass(frozen=True)
class CostRecord:
    agent: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float


@dataclass(frozen=True)
class CostTracker:
    budget_limit_monthly: float = DEFAULT_BUDGET_MONTHLY
    records: tuple = ()
    month: str = ""  # "YYYY-MM"; sang tháng mới thì bắt đầu lại từ 0

    def add(self, record):
        return CostTracker(self.budget_limit_monthly, (*self.records, record), self.month)

    @property
    def total_cost(self):
        return sum(r.cost_usd for r in self.records)

    @property
    def over_budget(self):
        return self.total_cost > self.budget_limit_monthly

    def by_agent(self):
        breakdown = {}
        for r in self.records:
            breakdown[r.agent] = breakdown.get(r.agent, 0) + r.cost_usd
        return breakdown


_lock = threading.Lock()
_tracker = None  # khởi tạo lười, xem _current_tracker()


def _budget_limit():
    raw = os.environ.get("TSB_BUDGET_MONTHLY_USD")
    if raw:
        try:
            return float(raw)
        except ValueError:
            pass
    return DEFAULT_BUDGET_MONTHLY


def _this_month():
    return datetime.now().strftime("%Y-%m")


def _load_persisted(month):
    path = os.environ.get("TSB_COST_FILE")
    if not path or not os.path.exists(path):
        return ()
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if data.get("month") != month:
            return ()
        return tuple(CostRecord(**r) for r in data.get("records", []))
    except (OSError, ValueError, TypeError):
        return ()


def _persist(tracker):
    path = os.environ.get("TSB_COST_FILE")
    if not path:
        return
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"month": tracker.month,
                       "records": [r.__dict__ for r in tracker.records]},
                      f, ensure_ascii=False, indent=2)
    except OSError:
        pass  # mất file chi phí không được làm hỏng luồng đăng bài


def _current_tracker():
    """Trả tracker hiện tại; tự reset khi sang tháng mới. Gọi trong _lock."""
    global _tracker
    month = _this_month()
    if _tracker is None or _tracker.month != month:
        _tracker = CostTracker(_budget_limit(), _load_persisted(month), month)
    elif _tracker.budget_limit_monthly != _budget_limit():
        _tracker = CostTracker(_budget_limit(), _tracker.records, _tracker.month)
    return _tracker


def get_tracker():
    with _lock:
        return _current_tracker()


def reset_tracker():
    """Xoá tracker trong bộ nhớ (dùng trong test / đầu tháng thủ công)."""
    global _tracker
    with _lock:
        _tracker = None


def check_budget():
    """Gọi TRƯỚC mỗi lần gọi LLM; ném BudgetExceededError nếu đã vượt ngưỡng."""
    with _lock:
        t = _current_tracker()
        if t.over_budget:
            raise BudgetExceededError(t.total_cost, t.budget_limit_monthly)


def estimate_cost(model, input_tokens, output_tokens):
    p_in, p_out = PRICING_PER_MTOK.get(model, DEFAULT_PRICE)
    return (input_tokens * p_in + output_tokens * p_out) / 1_000_000


def record_cost(agent, model, input_tokens, output_tokens):
    """GHI chi phí một lần gọi vào tracker (và file nếu TSB_COST_FILE đặt)."""
    global _tracker
    rec = CostRecord(agent, model, int(input_tokens), int(output_tokens),
                     estimate_cost(model, input_tokens, output_tokens))
    with _lock:
        _tracker = _current_tracker().add(rec)
        _persist(_tracker)
        return rec


# === ĐIỂM GỌI MẠNG DUY NHẤT — mock hàm này trong test ===

def _http_post_json(url, payload, headers, timeout=60):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return json.loads(res.read())
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", "replace")[:300]
        except Exception:
            pass
        raise LLMCallError(f"HTTP {e.code} từ {url}: {body}") from e


def _approx_tokens(text):
    return max(1, len(text or "") // 4)


def _call_anthropic(prompt, model, max_tokens, temperature):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise LLMConfigError("Thiếu ANTHROPIC_API_KEY cho tier dùng Claude")
    result = _http_post_json(
        "https://api.anthropic.com/v1/messages",
        {"model": model, "max_tokens": max_tokens, "temperature": temperature,
         "messages": [{"role": "user", "content": prompt}]},
        {"x-api-key": key, "anthropic-version": "2023-06-01",
         "Content-Type": "application/json"},
    )
    try:
        text = result["content"][0]["text"]
    except (KeyError, IndexError, TypeError) as e:
        raise LLMCallError(f"Phản hồi Anthropic sai định dạng: {str(result)[:200]}") from e
    usage = result.get("usage") or {}
    return text, usage.get("input_tokens"), usage.get("output_tokens")


def _call_omniroute(prompt, model, max_tokens, temperature):
    url = os.environ.get("OMNIROUTE_URL") or OMNIROUTE_DEFAULT_URL
    key = os.environ.get("OMNIROUTE_API_KEY")
    if "PORT" in url and not os.environ.get("OMNIROUTE_URL"):
        raise LLMConfigError("Thiếu OMNIROUTE_URL (đang là placeholder)")
    if not key:
        raise LLMConfigError("Thiếu OMNIROUTE_API_KEY cho tier qua OmniRoute")
    result = _http_post_json(
        url,
        {"model": model, "messages": [{"role": "user", "content": prompt}],
         "max_tokens": max_tokens, "temperature": temperature},
        {"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        text = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise LLMCallError(f"Phản hồi OmniRoute sai định dạng: {str(result)[:200]}") from e
    usage = result.get("usage") or {}
    return text, usage.get("prompt_tokens"), usage.get("completion_tokens")


def llm_call(prompt, tier="cheap", max_tokens=1500, temperature=0.7, agent="unknown"):
    """
    Universal LLM call — route theo tier, không hardcode model ở từng chỗ gọi.
    tier: cheap | reasoning | balanced | creative | factcheck
    Chặn (BudgetExceededError) nếu ngân sách tháng đã vượt; ghi chi phí sau khi gọi.
    """
    check_budget()
    model = MODEL_MAP.get(tier, "deepseek-v3")
    if model.startswith("claude"):
        text, tin, tout = _call_anthropic(prompt, model, max_tokens, temperature)
    else:
        text, tin, tout = _call_omniroute(prompt, model, max_tokens, temperature)
    if tin is None:
        tin = _approx_tokens(prompt)
    if tout is None:
        tout = _approx_tokens(text)
    record_cost(agent, model, tin, tout)
    return text


def guarded_llm_call(prompt, tier, agent_name, telegram_alert_fn=None, **kw):
    """Như llm_call, nhưng khi vượt ngân sách thì báo Telegram trước khi ném lỗi."""
    try:
        return llm_call(prompt, tier=tier, agent=agent_name, **kw)
    except BudgetExceededError as e:
        if telegram_alert_fn:
            telegram_alert_fn(
                f"🔴 Budget vượt ngưỡng ${e.limit}/tháng — pipeline TẠM DỪNG, cần review"
            )
        raise


def llm_call_with_fallback(prompt, tier="cheap", max_tokens=1500):
    """Model rẻ lỗi/timeout -> fallback Claude. Hết ngân sách thì KHÔNG fallback."""
    try:
        return llm_call(prompt, tier=tier, max_tokens=max_tokens)
    except (BudgetExceededError, LLMConfigError):
        raise
    except Exception as e:
        print(f"[LLM Router] {tier} model failed ({e}), falling back to Claude")
        return llm_call(prompt, tier="creative", max_tokens=max_tokens)
