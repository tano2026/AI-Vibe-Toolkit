# KHO-INDEX — AI Vibe Toolkit

> Entry point cho mọi agent. Fetch file này đầu tiên.
> Sau khi đọc → đọc tiếp AGENT-PLAYBOOK của mày ở /agents/

---

## Kho này là gì

GitHub repo: https://github.com/tano2026/AI-Vibe-Toolkit  
Chủ: Nobitano — vibe coder, content creator, digital marketer  
Mục đích kép: (1) knowledge base để agents dùng, (2) content factory ra video TikTok/YouTube

---

## Cấu trúc kho — map nhanh

```
/mcps/          39 files   MCP servers — phần lớn dành cho Claude Desktop
/repos/         94 files   GitHub repos — reference + có thể deploy
/skills/        98 files   Prompt templates + system prompts — dùng ngay không cài gì
/stacks/         5 files   Combo tools theo use case
/agents/         6 files   Playbook riêng cho từng agent  ← MÀY ĐỌC TIẾP Ở ĐÂY
/content/      127 files   Script video TikTok/YouTube
TRACKER.md               Danh sách toàn bộ entries
```

---

## Mày là agent nào → đọc file nào tiếp

| Agent | File cần đọc ngay sau file này |
|-------|-------------------------------|
| Hermes | /agents/HERMES-PLAYBOOK.md |
| OpenClaw | /agents/OPENCLAW-PLAYBOOK.md |
| Antigravity | /agents/ANTIGRAVITY-PLAYBOOK.md |
| Claude | Không cần — tự gọi GitHub API trong session |

---

## Quy tắc đọc file .md trong kho

Mỗi file trong kho có các section sau. Agent đọc đúng section, bỏ qua phần còn lại:

| Section | Claude dùng | Hermes dùng | OpenClaw dùng | Antigravity dùng |
|---------|-------------|-------------|---------------|------------------|
| TL;DR | ✅ | ✅ | ✅ | ✅ |
| Dùng để làm gì | ✅ | ✅ | ✅ | ✅ |
| Setup từng bước | ✅ | ❌ skip | Một phần | ✅ |
| claude_desktop_config | ✅ | ❌ skip | ❌ skip | ❌ skip |
| npx / npm install | ❌ | ❌ | ✅ | ✅ |
| HTTP API / REST | ✅ | ✅ | ✅ | - |
| Python SDK | ✅ | ✅ | - | ✅ |
| Ví dụ thực tế | ✅ | ✅ | ✅ | - |
| Đánh giá cá nhân | ✅ | ✅ reference | ✅ reference | - |

---

## Fetch function chuẩn

### Python (Hermes)
```python
import urllib.request, json, base64

def fetch(path, token="[GITHUB_TOKEN]"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode("utf-8")

# Bắt đầu bằng:
playbook = fetch("agents/HERMES-PLAYBOOK.md")
```

### Node.js (OpenClaw)
```javascript
const https = require("https");
function fetch(path, token) {
  return new Promise((res, rej) => {
    https.get({
      hostname: "api.github.com",
      path: `/repos/tano2026/AI-Vibe-Toolkit/contents/${path}`,
      headers: { "Authorization": `token ${token}`, "User-Agent": "openclaw", "Accept": "application/vnd.github.v3+json" }
    }, r => { let d=""; r.on("data",c=>d+=c); r.on("end",()=>res(Buffer.from(JSON.parse(d).content,"base64").toString())); }).on("error",rej);
  });
}
// Bắt đầu bằng:
const playbook = await fetch("agents/OPENCLAW-PLAYBOOK.md", process.env.GITHUB_TOKEN);
```

### Shell/curl (Antigravity)
```bash
fetch_kho() {
  curl -s     -H "Authorization: token [GITHUB_TOKEN]"     -H "Accept: application/vnd.github.v3+json"     "https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/$1"     | python3 -c "import sys,json,base64; print(base64.b64decode(json.load(sys.stdin)['content']).decode())"
}
# Bắt đầu bằng:
fetch_kho "agents/ANTIGRAVITY-PLAYBOOK.md"
```
