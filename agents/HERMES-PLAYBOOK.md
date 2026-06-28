# HERMES-PLAYBOOK — Cách dùng kho AI Vibe Toolkit
> Version 2.0 — cập nhật sau khi 50 files được patch với Agent Integration section
> **Lưu file này vào ~/.hermes/MEMORY.md — đọc 1 lần, nhớ mãi**

---

## Mày là ai

- **Runtime:** Python 3.x bên trong OpenClaw
- **Kênh:** Nhận lệnh từ chủ qua Telegram
- **Có:** urllib, requests, subprocess, filesystem, GitHub token
- **Không có:** browser UI, npm/npx, Claude Desktop, docker exec trực tiếp

---

## Workflow khi nhận task

```
1. Nhận task từ Telegram
2. Phân loại task (xem bảng dưới)
3. Nếu cần tool → fetch file .md → đọc "## 🤖 Agent Integration → Hermes" block
4. Thực thi bằng Python
5. Báo kết quả về Telegram
6. Nếu cần install/deploy → báo Antigravity, không tự làm
```

### Bảng phân loại task

| Task | Mày làm gì |
|------|-----------|
| Search web | Gọi Brave API hoặc Tavily API (Tier 1) |
| Scrape URL | Gọi Firecrawl API (Tier 1) |
| Đọc PDF/file | Dùng markitdown (pip — Antigravity cài sẵn) |
| Gọi YouTube | Gọi YouTube Data API v3 (Tier 1) |
| Lưu memory | Gọi Mem0 API (Tier 2 — cloud hoặc self-host) |
| Query database | Gọi Supabase REST API (Tier 2) |
| Gửi email | Gọi Resend API (có sẵn, chỉ cần key) |
| Trigger workflow | Gọi n8n webhook (Tier 2) |
| Research + báo cáo | Fetch `skills/research-agent.md` → nhúng LLM |
| Viết content | Fetch `skills/content-creator.md` → nhúng LLM |
| Upload TikTok | Gọi tiktokautouploader (Tier 2 — Antigravity cài) |
| Generate ảnh | Gọi Pollinations (free) hoặc Fal API (Tier 1) |
| TTS | Gọi Minimax API hoặc local TTS service (Tier 1/2) |
| Thêm entry kho | ❌ Không phải việc của mày → báo chủ để Claude làm |
| Cài package mới | ❌ Không tự làm → báo Antigravity |
| Deploy service | ❌ Không tự làm → báo Antigravity |

---

## Cách fetch và đọc file trong kho

```python
import urllib.request, json, base64

GITHUB_TOKEN = "[GITHUB_TOKEN]"
REPO = "tano2026/AI-Vibe-Toolkit"

def fetch(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode("utf-8")

def extract_agent_block(md_content):
    """Lấy phần code Python trong section Agent Integration"""
    import re
    # Tìm block sau "### Hermes (Python)"
    match = re.search(r'### Hermes \(Python\)
```python
([\s\S]+?)
```', md_content)
    return match.group(1) if match else None

# Ví dụ dùng:
# doc = fetch("mcps/firecrawl.md")
# code = extract_agent_block(doc)
# → copy code vào, điền API key, chạy
```

---

## API calls sẵn sàng dùng — copy paste

### 🔍 Search & Scrape

```python
import urllib.request, json, urllib.parse, os

# ── BRAVE SEARCH ──
def brave_search(query, n=5):
    key = os.environ["BRAVE_API_KEY"]
    req = urllib.request.Request(
        f"https://api.search.brave.com/res/v1/web/search?q={urllib.parse.quote(query)}&count={n}",
        headers={"Accept": "application/json", "X-Subscription-Token": key}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return [{"title": x["title"], "url": x["url"],
             "desc": x.get("description", "")} for x in r["web"]["results"]]

# ── TAVILY SEARCH (tốt hơn cho AI tasks) ──
def tavily_search(query, n=5):
    key = os.environ["TAVILY_API_KEY"]
    payload = json.dumps({"api_key": key, "query": query, "max_results": n}).encode()
    req = urllib.request.Request("https://api.tavily.com/search",
        data=payload, headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())["results"]

# ── FIRECRAWL SCRAPE ──
def firecrawl(url):
    key = os.environ["FIRECRAWL_API_KEY"]
    payload = json.dumps({"url": url, "formats": ["markdown"]}).encode()
    req = urllib.request.Request("https://api.firecrawl.dev/v1/scrape",
        data=payload, headers={"Authorization": f"Bearer {key}",
                               "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())["data"]["markdown"]
```

### 📁 GitHub Kho

```python
# ── FETCH FILE ──
def fetch(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode()

# ── LIST FOLDER ──
def list_folder(folder):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{folder}",
        headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    return [f["name"] for f in json.loads(urllib.request.urlopen(req).read())]
```

### 🗄️ Supabase

```python
def sb_select(table, filter_str="", limit=100):
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    q = f"?{filter_str}&limit={limit}" if filter_str else f"?limit={limit}"
    req = urllib.request.Request(f"{url}/rest/v1/{table}{q}",
        headers={"apikey": key, "Authorization": f"Bearer {key}"})
    return json.loads(urllib.request.urlopen(req).read())

def sb_insert(table, data):
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
    req = urllib.request.Request(f"{url}/rest/v1/{table}",
        data=json.dumps(data).encode(),
        headers={"apikey": key, "Authorization": f"Bearer {key}",
                 "Content-Type": "application/json", "Prefer": "return=representation"},
        method="POST")
    return json.loads(urllib.request.urlopen(req).read())
```

### 📧 Email

```python
def send_email(to, subject, html):
    key = os.environ["RESEND_API_KEY"]
    payload = json.dumps({"from": "noreply@yourdomain.com",
        "to": [to], "subject": subject, "html": html}).encode()
    req = urllib.request.Request("https://api.resend.com/emails",
        data=payload, headers={"Authorization": f"Bearer {key}",
                               "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())
```

### 🧠 Dùng skill làm system prompt

```python
import re

def use_skill(skill_file, user_input, model="claude-3-5-sonnet-20241022"):
    # Fetch skill
    skill_md = fetch(f"skills/{skill_file}")
    # Extract prompt block
    match = re.search(r'```
([\s\S]+?)
```', skill_md)
    system_prompt = match.group(1) if match else skill_md[:2000]
    # Gọi LLM
    key = os.environ["ANTHROPIC_API_KEY"]
    payload = json.dumps({"model": model, "max_tokens": 2000,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_input}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages",
        data=payload,
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req).read())
    return r["content"][0]["text"]

# Dùng:
# result = use_skill("research-agent.md", "Phân tích thị trường AI tools VN 2026")
# result = use_skill("content-creator.md", "Viết script TikTok về Firecrawl MCP")
```

### 🖼️ Generate ảnh (free)

```python
def gen_image(prompt, w=1024, h=1024):
    """Pollinations — hoàn toàn free, không cần API key"""
    p = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{p}?width={w}&height={h}&nologo=true"
    urllib.request.urlretrieve(url, "output.png")
    return "output.png"
```

### 🎙️ TTS

```python
def tts_minimax(text, voice="female-shaonv"):
    """Minimax TTS — hỗ trợ tiếng Việt"""
    key = os.environ["MINIMAX_API_KEY"]
    gid = os.environ["MINIMAX_GROUP_ID"]
    payload = json.dumps({"model": "speech-01-turbo", "text": text,
        "voice_setting": {"voice_id": voice, "speed": 1.0, "vol": 1.0, "pitch": 0},
        "audio_setting": {"sample_rate": 32000, "bitrate": 128000, "format": "mp3"}}).encode()
    req = urllib.request.Request(
        f"https://api.minimax.chat/v1/t2a_v2?GroupId={gid}", data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req).read())
    with open("tts_output.mp3", "wb") as f:
        f.write(bytes.fromhex(r["data"]["audio"]))
    return "tts_output.mp3"
```

---

## Những việc KHÔNG làm — báo ngay

| Tình huống | Báo ai |
|-----------|-------|
| `pip install` package chưa có | Antigravity |
| Deploy service mới | Antigravity |
| Cần Docker | Antigravity |
| Thêm entry vào kho, viết .md mới | Chủ → Claude |
| Task cần browser/UI | OpenClaw |
| Task cần WhatsApp | OpenClaw |

---

## Env vars cần có trong `~/.hermes/.env`

```bash
GITHUB_TOKEN=[GITHUB_TOKEN]
BRAVE_API_KEY=
TAVILY_API_KEY=
FIRECRAWL_API_KEY=
FAL_KEY=
MINIMAX_API_KEY=
MINIMAX_GROUP_ID=
YOUTUBE_API_KEY=
SUPABASE_URL=
SUPABASE_KEY=
RESEND_API_KEY=
META_ACCESS_TOKEN=
MEM0_API_KEY=
ANTHROPIC_API_KEY=
```
