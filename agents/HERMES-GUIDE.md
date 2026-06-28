# Hermes — Hướng dẫn dùng kho AI Vibe Toolkit

> File này dành riêng cho Hermes agent. Đọc file này trước khi fetch bất kỳ file nào khác trong kho.

---

## Mày là ai trong hệ thống

- **Runtime:** Python 3.x bên trong OpenClaw
- **Kênh nhận lệnh:** Telegram
- **Không có:** browser, npm, Claude Desktop, MCP mount
- **Có:** urllib, requests, subprocess, filesystem access, GitHub token

---

## Nguyên tắc đọc kho này

Kho có 2 loại nội dung:

| Loại | Folder | Mày đọc như thế nào |
|------|--------|----------------------|
| Docs cho human/Claude | /mcps/, /repos/, /skills/, /stacks/ | Bỏ qua phần "Setup cho Claude Desktop". Chỉ đọc TL;DR, Dùng để làm gì, và HTTP API section |
| Docs cho mày | /agents/ | Đọc toàn bộ — đây là instruction trực tiếp |

**Quy tắc vàng:** Bất cứ khi nào file .md nói `npx`, `claude_desktop_config.json`, hay `MCP server` → đó là cho Claude Desktop, không phải cho mày. Tìm HTTP API hoặc Python SDK thay thế.

---

## Cách mày dùng từng loại tool trong kho

### MCPs → Gọi HTTP API trực tiếp

Mày không cài MCP. Nhưng hầu hết MCP đều wrap một HTTP API. Gọi thẳng vào API đó.

```python
import urllib.request, json

# FIRECRAWL — thay vì MCP, gọi REST API
def firecrawl_scrape(url, api_key):
    payload = json.dumps({"url": url, "formats": ["markdown"]}).encode()
    req = urllib.request.Request(
        "https://api.firecrawl.dev/v1/scrape",
        data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())["data"]["markdown"]

# BRAVE SEARCH — thay vì MCP, gọi REST API
def brave_search(query, api_key, count=5):
    import urllib.parse
    q = urllib.parse.quote(query)
    req = urllib.request.Request(
        f"https://api.search.brave.com/res/v1/web/search?q={q}&count={count}",
        headers={"Accept": "application/json", "X-Subscription-Token": api_key}
    )
    resp = urllib.request.urlopen(req)
    results = json.loads(resp.read())["web"]["results"]
    return [{"title": r["title"], "url": r["url"], "snippet": r.get("description","")} for r in results]

# TAVILY — semantic search tốt hơn cho AI agent
def tavily_search(query, api_key, max_results=5):
    payload = json.dumps({"api_key": api_key, "query": query, "max_results": max_results}).encode()
    req = urllib.request.Request(
        "https://api.tavily.com/search",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())["results"]

# GITHUB API — fetch kho này
def fetch_kho(path, token="[YOUR_GITHUB_TOKEN]"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    import base64
    return base64.b64decode(data["content"]).decode("utf-8")
```

### Repos → Reference only, không cài

Khi kho có `/repos/browser-use.md` hay `/repos/mem0.md` → mày đọc để hiểu tool đó làm gì. Nếu tool cần Python và đã được Antigravity deploy lên VPS → gọi endpoint của nó.

```python
# Mem0 — nếu đã deploy trên VPS
def mem0_search(query, user_id, mem0_url, api_key):
    payload = json.dumps({"query": query, "user_id": user_id}).encode()
    req = urllib.request.Request(
        f"{mem0_url}/v1/memories/search/",
        data=payload,
        headers={"Authorization": f"Token {api_key}", "Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())
```

### Skills → Copy prompt, không cần cài gì

File `/skills/*.md` chứa system prompt. Mày fetch → nhúng vào lượt gọi LLM.

```python
skill_text = fetch_kho("skills/research-agent.md")
# Dùng skill_text làm system prompt khi gọi Claude/DeepSeek
```

### Stacks → Đọc để biết combo tool nào dùng với nhau

File `/stacks/*.md` là bản đồ workflow — biết khi task X thì gọi tool A rồi B rồi C theo thứ tự nào.

---

## API keys mày cần (hỏi chủ nếu chưa set trong env)

| Key | Dùng cho | Free tier |
|-----|----------|-----------|
| FIRECRAWL_API_KEY | Scrape web sạch | 500 req/tháng |
| BRAVE_API_KEY | Web search | 2000 req/tháng |
| TAVILY_API_KEY | AI-optimized search | 1000 req/tháng |
| GITHUB_TOKEN | Fetch kho này | Unlimited |
| RESEND_API_KEY | Gửi email | 3000/tháng |

---

## Workflow chuẩn khi nhận task

```
1. Nhận task từ Telegram qua OpenClaw
2. Nếu cần tool → fetch TRACKER.md để biết file nào có
3. Fetch file .md tương ứng → đọc TL;DR + xem API endpoint
4. Thực thi bằng Python urllib/requests (KHÔNG npm, KHÔNG MCP)
5. Báo kết quả về Telegram
6. Nếu cần install package mới → báo Antigravity, không tự cài
```

---

## Những thứ mày KHÔNG làm được — báo chủ/Antigravity

- npm install / npx → không có Node
- Mount MCP server → không phải Claude Desktop  
- Mở browser, click UI → không có display
- pip install package chưa có → nhờ Antigravity deploy trước
- Chạy Docker → nhờ Antigravity
