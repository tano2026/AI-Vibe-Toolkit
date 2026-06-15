# AI Vibe Toolkit Skill — OpenClaw Format

**Copy file này vào:** `~/.openclaw/skills/ai-vibe-toolkit/SKILL.md`

---

```markdown
---
name: ai-vibe-toolkit
description: "Quản lý kho AI Vibe Toolkit: research repos, push .md, viết scripts video, update TRACKER. Dùng khi cần thêm tool mới vào kho hoặc viết script video."
metadata:
  {
    "openclaw":
      {
        "emoji": "🛠️",
        "requires":
          {
            "config": ["skills.entries.ai-vibe-toolkit.enabled"],
          },
      },
  }
---

# AI Vibe Toolkit

Kho tổng hợp MCP, Skills, Repos, Tools cho vibe coders.

**GitHub:** https://github.com/tano2026/AI-Vibe-Toolkit
**Token:** [YOUR_GITHUB_TOKEN] ← thay bằng token thật

## Kho có gì

- /repos/ — 49 repos đã research
- /mcps/ — 34 MCPs đã test
- /skills/ — 406 skills files
- /content/ — 59 script videos
- TRACKER.md — toàn bộ danh sách

## Commands Chính

### Thêm repo mới
Khi user nhắn "thêm repo [URL]":
1. Fetch GitHub API: GET /repos/{owner}/{repo}
2. Fetch README.md raw
3. Viết /repos/{tên}.md (Tiếng Việt, có đánh giá, Rating X/10)
4. Viết /content/script-video-{XX}-{tên}.md (hook mạnh đầu tiên)
5. Push cả 2 lên GitHub
6. Update TRACKER.md
7. Reply: "Xong! Script #{XX} ready"

### Viết script video
Khi user nhắn "viết script [tool]":
1. Fetch /repos/{tool}.md từ kho
2. Fetch /skills/viral-hooks/hooks-database.md
3. Viết script 60-90s, hook psychology mạnh
4. Push /content/script-video-{XX}-{tool}.md
5. Reply preview hook + "Script #{XX} pushed"

### Check kho
Khi user nhắn "kho có gì" hoặc "kho mới gì":
1. Fetch TRACKER.md
2. Tóm tắt: repos mới, scripts mới, MCPs mới
3. Reply tóm tắt

### Research nhanh
Khi user nhắn "research [topic]":
1. Dùng Brave Search MCP hoặc last30days skill
2. Tóm tắt 200 words, real signals
3. Reply kết quả

## Hard Rules

- KHÔNG bịa số liệu — luôn fetch GitHub API thật
- KHÔNG push lên kho nếu không có đủ thông tin
- Luôn update TRACKER.md sau mỗi batch
- Script video: hook đầu tiên quan trọng nhất
- Reply bằng tiếng Việt, casual

## GitHub Push Pattern

```python
import requests, base64
TOKEN = "[YOUR_GITHUB_TOKEN]"
REPO = "tano2026/AI-Vibe-Toolkit"
headers = {"Authorization": f"token {TOKEN}"}

def push(path, content, message):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    r = requests.get(url, headers=headers)
    sha = r.json().get('sha')
    payload = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode()
    }
    if sha: payload["sha"] = sha
    requests.put(url, headers=headers, json=payload)
```
```
