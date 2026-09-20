# HERMES-ADAPTER.md — Digital Marketing Agent

> Marketing dựa vào `claude-ads/*` (bộ skill ads-budget/ads-audit đã phát
> hiện trùng lặp, dùng thay vì viết lại) + các platform API quảng cáo
> (Google/Meta/TikTok Ads) — phần lớn cần OAuth phức tạp, khó làm thuần
> `urllib`. Phần logic tính toán (kill rule, sample size) chạy được ngay.

## 1. Fetch skill động

```python
import urllib.request, json, base64, os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "tano2026/AI-Vibe-Toolkit"

def github(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def fetch_skill_from_kho(skill_path):
    data = github(f"repos/{REPO}/contents/{skill_path}")
    return base64.b64decode(data['content']).decode()

MARKETING_SKILLS = {
    "digital-marketing-orchestrator": "agents/digital-marketing-agent/skills/digital-marketing-orchestrator/SKILL.md",
    "ad-budget-testing-discipline": "agents/digital-marketing-agent/skills/ad-budget-testing-discipline/SKILL.md",
    "ads-budget": "skills/claude-ads/ads-budget.md",
    "ads-audit": "skills/claude-ads/ads-audit.md",
}

def load_skill(name):
    path = MARKETING_SKILLS.get(name)
    if not path:
        return f"❌ Không tìm thấy skill '{name}'"
    return fetch_skill_from_kho(path)
```

## 2. Giới hạn thật — Ad Platform API cần OAuth, không đơn giản như GitHub

```
⚠️ Google Ads API, Meta Marketing API đều yêu cầu OAuth 2.0 flow (không
chỉ 1 API key tĩnh như GitHub/HubSpot) — refresh token, scope cụ thể,
thường cần bước xác thực qua trình duyệt lần đầu. Hermes (chạy nền,
không có UI trình duyệt) KHÔNG tự làm được bước OAuth đầu tiên.

Cách khả thi: Nobitano/Antigravity tự làm OAuth 1 lần (qua máy có trình
duyệt), lưu refresh token vào biến môi trường, Hermes chỉ dùng refresh
token có sẵn để lấy access token mới khi cần (không tự làm OAuth từ đầu).
```

```python
GOOGLE_ADS_REFRESH_TOKEN = os.environ.get("GOOGLE_ADS_REFRESH_TOKEN", "")
# Cần thêm client_id/client_secret để đổi refresh token → access token —
# chi tiết OAuth request cần verify đúng theo docs Google Ads API mới
# nhất trước khi code thật, KHÔNG đoán endpoint/param ở đây.
```

## 3. Kill rule + A/B test sample size — chạy thuần Python

```python
def check_kill_rule(spend, target_cpa, actual_cpa, conversions, learning_phase_done):
    """Áp đúng luật trong ad-budget-testing-discipline mục kill rule."""
    if spend >= 3 * target_cpa and conversions == 0:
        return {"action": "TẮT", "lý_do": "spend ≥ 3× CPA target, 0 conversion"}
    if learning_phase_done and actual_cpa > 1.5 * target_cpa:
        return {"action": "TẮT", "lý_do": "CPA thực > 1.5× target sau learning"}
    return {"action": "GIỮ", "lý_do": None}

def min_sample_for_ab_test(expected_lift=0.20):
    """Ước tính thô số conversion cần/variant — quy tắc ~100 conversion
    cho khác biệt ~20% (theo ad-budget-testing-discipline mục 3)."""
    return int(100 * (0.20 / expected_lift))
```

## Việc cần làm trước khi tin dùng thật

1. OAuth Google/Meta Ads cần làm thủ công 1 lần (không tự động hoá được qua Hermes) trước khi có refresh token dùng lâu dài
2. Chưa verify chi tiết endpoint Google Ads API thật (để trống, không đoán)
3. Đã dùng chung skill claude-ads/ads-budget.md + ads-audit.md thay vì viết lại (đúng bài học tránh trùng lặp)
