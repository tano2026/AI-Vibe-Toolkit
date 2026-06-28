# /agents — Hướng dẫn cho AI Agents

Folder này chứa instruction riêng cho từng agent trong hệ thống.

## Agents trong hệ thống

| Agent | File | Vai trò | Runtime |
|-------|------|---------|---------|
| Hermes | HERMES-GUIDE.md | Research, xử lý task, gọi API | Python trong OpenClaw |
| OpenClaw | OPENCLAW-GUIDE.md | Orchestrator chính, browser, Telegram gateway | Node.js 22+ |
| Antigravity | ANTIGRAVITY-GUIDE.md | Install, deploy, maintain VPS | Shell/SSH |
| Research Pro | research-pro.md | Analyst chuyên sâu (sub-agent của Hermes) | Python |

## Phân công

```
Nhận lệnh từ chủ (Telegram)
    ↓
OpenClaw — điều phối
    ├── Task Python/API → Hermes
    ├── Task deploy/install → Antigravity
    ├── Task browser/UI → OpenClaw tự xử
    └── Task research phức tạp → Hermes → Research Pro
```

## Fetch kho (Python — Hermes dùng)

```python
import urllib.request, json, base64

def fetch_kho(path, token="[YOUR_GITHUB_TOKEN]"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode("utf-8")

# Examples
tracker = fetch_kho("TRACKER.md")
guide = fetch_kho("agents/HERMES-GUIDE.md")
firecrawl = fetch_kho("mcps/firecrawl.md")
```

## Claude (tao) dùng kho thế nào

Claude gọi thẳng GitHub API trong mỗi session — không download về local. Kho là shared knowledge base, mỗi agent đọc theo cách riêng của mình phù hợp với runtime.
