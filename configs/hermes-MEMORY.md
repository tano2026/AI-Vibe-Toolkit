# Hermes Agent — MEMORY.md Template v2

**Copy vào:** `~/.hermes/MEMORY.md`
**Mục đích:** Long-term context — Hermes đọc file này mỗi phiên
**Cập nhật:** 2026-06

---

```markdown
# Long-term Memory

## Kho AI Vibe Toolkit

### Stats hiện tại
- Repos: 74 | MCPs: 37 | Skills: 82 | Scripts: 102 | Stacks: 3
- GitHub: https://github.com/tano2026/AI-Vibe-Toolkit
- Token: [YOUR_GITHUB_TOKEN]

### Repos đã có — KHÔNG thêm lại:
Fetch TRACKER.md trước khi research bất kỳ entry mới.
URL: https://raw.githubusercontent.com/tano2026/AI-Vibe-Toolkit/main/TRACKER.md

### Script số tiếp theo:
Fetch content/ folder → đếm files → +1 (hiện tại đã có đến script-102)

## Environment — Tools Có Thể Dùng

### ✅ HOẠT ĐỘNG
- Python urllib.request / requests → fetch URL bất kỳ
- GitHub API → token đã có, full read/write access
- Free APIs: Wikipedia, HackerNews Algolia, npm registry, PyPI, Reddit public JSON
- Code execution: pandas, numpy, json, re, base64, time
- File I/O: đọc/ghi file local

### ❌ KHÔNG DÙNG ĐƯỢC
- Brave Search MCP → không mount được
- Firecrawl MCP → không mount được
- YouTube Data API → cần OAuth credentials.json
- Meta Ads API → cần Business token
- Google Analytics → cần OAuth
- Bất kỳ MCP nào cần npx/node process riêng

### 🔄 WORKAROUND
- Thay Brave Search → scrape Google Search HTML hoặc dùng HN Algolia
- Thay Firecrawl → urllib.request + regex extract text
- Thay YouTube API → scrape channel page HTML + SocialBlade
- Thay Meta Ads → user cung cấp screenshot/export thủ công

## Research Workflow (Python-native)

### Khi research GitHub repo:
```python
import urllib.request, json, base64

TOKEN = "[YOUR_GITHUB_TOKEN]"
headers = {"Authorization": f"token {TOKEN}"}

# 1. Metadata
url = f"https://api.github.com/repos/{owner}/{repo}"
# 2. README
url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md"
# 3. Releases
url = f"https://api.github.com/repos/{owner}/{repo}/releases?per_page=5"
# 4. Search
url = f"https://api.github.com/search/repositories?q={query}&sort=stars&per_page=10"
```

### Khi research market/trend:
```python
# HackerNews (community signal)
url = f"https://hn.algolia.com/api/v1/search?query={query}&tags=story&hitsPerPage=10"

# Wikipedia (background)
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

# Reddit (practitioner opinions)
url = f"https://www.reddit.com/r/MachineLearning/search.json?q={query}&sort=top&limit=10"
headers_reddit = {"User-Agent": "research-bot/1.0"}

# npm stats
url = f"https://registry.npmjs.org/{package}"

# PyPI
url = f"https://pypi.org/pypi/{package}/json"
```

### Khi push lên GitHub:
```python
# LUÔN GET SHA trước khi PUT (file đã tồn tại)
url = f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}"
r = urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": f"token {TOKEN}"}))
existing = json.loads(r.read())
sha = existing.get('sha')  # None nếu file mới

payload = {
    "message": f"add: {path}",
    "content": base64.b64encode(content.encode()).decode()
}
if sha:
    payload["sha"] = sha

req = urllib.request.Request(url, data=json.dumps(payload).encode(),
    headers={"Authorization": f"token {TOKEN}", "Content-Type": "application/json"},
    method="PUT")
urllib.request.urlopen(req)
```

## Content Channel

### Hook templates hay nhất:
- "[X]k stars — [feature độc đáo nhất]"
- "Tool này làm [Y] mà [tool cũ] không làm được"
- "Cài 1 lần, dùng mãi mãi — và miễn phí"
- "[Con số ấn tượng]. [Giải pháp]. [Miễn phí/local]."

### Format script: hook 3s → pain → solution → demo → CTA

## Quy Tắc Quan Trọng

1. KHÔNG bịa số liệu — luôn fetch thật từ API
2. Luôn update TRACKER.md sau mỗi batch push
3. Không nói "không làm được" trước khi thử ≥3 approach khác
4. Batch 3+ repos cùng lúc để tiết kiệm time
5. time.sleep(0.7) giữa các GitHub API calls để tránh rate limit
6. Duplicate check TRƯỚC khi research — fetch TRACKER.md
```
