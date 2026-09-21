# HERMES-ADAPTER.md — Customer Satisfaction Pro

> Agent này CHƯA nối kênh inbox thật — Hermes hiện chỉ chạy được phần LOGIC
> PHÂN LOẠI (thuần Python, không cần tool ngoài), chưa tự động quét
> Facebook/Zalo OA/Email thật.

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

CS_SKILLS = {
    "churn-risk-escalation-discipline": "agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline/SKILL.md",
    "critical-path-briefing": "agents/customer-satisfaction-pro/skills/critical-path-briefing/SKILL.md",
}
```

## 2. Phân loại tín hiệu rời bỏ — chạy thuần Python, không cần tool ngoài

```python
CHURN_SIGNALS = ["huỷ", "hủy", "chuyển", "đối thủ", "không dùng nữa",
                  "hoàn tiền", "bồi thường", "thất vọng", "tệ quá"]

def classify_message(text):
    text_lower = text.lower()
    matched = [s for s in CHURN_SIGNALS if s in text_lower]
    if matched:
        return {"loai": "ROI_BO_THAT", "escalate": "NGAY", "tin_hieu_khop": matched}
    return {"loai": "PHAN_NAN_NHO", "escalate": "cho lap lai >=3 lan"}
```

Lưu ý: danh sách từ khoá trên là khung mẫu ĐƠN GIẢN (rule-based, không phải NLP thật) — dễ bỏ sót cách diễn đạt khác (mỉa mai, viết tắt, tiếng lóng). Chỉ dùng làm bước lọc thô ban đầu, KHÔNG thay thế việc đọc thật khi case có vẻ nghiêm trọng — luôn để người/Claude đọc lại toàn bộ tin nhắn trước khi kết luận, không chỉ dựa vào match từ khoá.

## 3. SLA check — thuần Python

```python
from datetime import datetime

SLA_SECONDS = {"chat": 40, "email_thuong": 4*3600, "email_uu_tien": 2*3600, "social": 60*60}

def check_sla(channel, received_time_iso):
    elapsed = (datetime.now() - datetime.fromisoformat(received_time_iso)).total_seconds()
    limit = SLA_SECONDS.get(channel, 4*3600)
    return {"trong_sla": elapsed <= limit, "da_troi_qua_giay": elapsed, "gioi_han_giay": limit}
```

## Việc CHƯA làm — nói thẳng

- Chưa có code đọc Facebook/Zalo OA/Email inbox thật — cần xác nhận kênh + API trước khi viết
- CHURN_SIGNALS là danh sách từ khoá tiếng Việt cơ bản, chưa qua kiểm thử với case thật — cần tinh chỉnh sau khi chạy thử
