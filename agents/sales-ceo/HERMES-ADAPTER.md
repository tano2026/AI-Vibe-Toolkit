# HERMES-ADAPTER.md — Sales-CEO

> Sales-CEO dựa nhiều vào `hubspot-mcp` (33 tools qua MCP) — Hermes không
> chạy được giao thức MCP, phải gọi thẳng HubSpot REST API qua `urllib`.
> Phần scoring/forecast (logic thuần, không cần tool ngoài) chạy được
> ngay trên Hermes không cần adapter gì thêm.

## 1. Fetch skill động (đúng pattern đã dùng cho Content Pro)

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

SALES_SKILLS = {
    "ceo-decision-lens": "agents/sales-ceo/skills/ceo-decision-lens/SKILL.md",
    "gtm-strategy": "agents/sales-ceo/skills/gtm-strategy/SKILL.md",
    "negotiation-deal-structuring": "agents/sales-ceo/skills/negotiation-deal-structuring/SKILL.md",
    "deal-scoring-forecast-discipline": "agents/sales-ceo/skills/deal-scoring-forecast-discipline/SKILL.md",
    "forward-deployed-engineer-model": "agents/sales-ceo/skills/forward-deployed-engineer-model/SKILL.md",
}

def load_skill(name):
    path = SALES_SKILLS.get(name)
    if not path:
        return f"❌ Không tìm thấy skill '{name}'"
    return fetch_skill_from_kho(path)
```

## 2. HubSpot — thay MCP bằng REST API trực tiếp

```python
HUBSPOT_TOKEN = os.environ.get("HUBSPOT_TOKEN", "")

def hubspot_api(endpoint, method="GET", body=None):
    url = f"https://api.hubapi.com{endpoint}"
    headers = {"Authorization": f"Bearer {HUBSPOT_TOKEN}", "Content-Type": "application/json"}
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def get_deal(deal_id):
    return hubspot_api(f"/crm/v3/objects/deals/{deal_id}")

def update_deal_stage(deal_id, new_stage):
    return hubspot_api(f"/crm/v3/objects/deals/{deal_id}", method="PATCH",
                        body={"properties": {"dealstage": new_stage}})

def list_stale_deals(days=14):
    """Deal không activity >= N ngày — đúng luật CRM hygiene trong
    deal-scoring-forecast-discipline mục 6."""
    # Cần query HubSpot theo lastActivityDate — filter cụ thể theo
    # HubSpot Search API, verify đúng field name trước khi chạy thật
    pass  # placeholder — cần verify field HubSpot thật trước khi dùng
```

⚠️ `list_stale_deals` để placeholder — chưa verify đúng field HubSpot API thật (`hs_lastmodifieddate` hay field riêng), không đoán field để tránh lỗi giống bài học no-fabrication.

## 3. Deal scoring — chạy thuần Python, không cần tool ngoài

```python
def score_deal(fit_signals: dict, intent_signals: dict):
    """
    Áp đúng công thức fit×intent trong deal-scoring-forecast-discipline.
    fit_signals/intent_signals: dict các tiêu chí đã có sẵn điểm 0-5 mỗi cái
    """
    fit_score = sum(fit_signals.values()) / len(fit_signals)
    intent_score = sum(intent_signals.values()) / len(intent_signals)
    total = fit_score + intent_score

    if total >= 7:
        action = "outreach trong 24h"
    elif total >= 5:
        action = "nurture"
    else:
        action = "không đụng"

    return {"fit": fit_score, "intent": intent_score, "total": total, "action": action}
```

## Việc cần làm trước khi tin dùng thật

1. Verify đúng field HubSpot API cho `list_stale_deals` (lastActivityDate thật, không đoán)
2. Set `HUBSPOT_TOKEN` qua biến môi trường, không hard-code
3. `outbound-engine`/`cold-email`/`lead-dossier`/`lead-intelligence` (skill khác trong Capability Map) chưa có adapter riêng ở đây — cần fetch + đánh giá từng cái có tool ngoài nào cần thay thế không trước khi Hermes dùng
