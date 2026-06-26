# Hermes Agent — MEMORY.md v3 (Research Pro Universal)

**Copy vào:** `~/.hermes/MEMORY.md`
**Cập nhật:** 2026-06-26

---

```markdown
# Long-term Memory — Research Pro

## Chủ nhân
Nobitano (Nguyễn Ngọc Tân) — content creator AI, vibe coder, digital marketer
Brands: ABTRIP, Tano, Wonder Mart
Đặt vé thực tế: dùng Playwright trên abtrip.vn, KHÔNG dùng test environment

## Kho AI Vibe Toolkit
- GitHub: https://github.com/tano2026/AI-Vibe-Toolkit
- Token: [YOUR_GITHUB_TOKEN]
- Stats: Repos: 74 | MCPs: 37 | Skills: 82 | Scripts: 102
- Duplicate check: Fetch TRACKER.md trước khi thêm entry mới
- Script tiếp theo: đếm /content/ folder → hiện đến 102 → tiếp là 103

## Skills Đang Có (AI-Vibe-Toolkit)
- agentic-factory
- deep-research-skills-skill (L0-L5)
- agent-research-skills-academic-skill
- token-efficient-research
- marketingskills-skill (43 skills)
- x-research-skill-skill
- affiliate-skills (52 skills)
- youtube-marketing-skills (21 lệnh)
- fact-checker
- scholar-evaluation

## Tools Hàng không
- searchflights / bookflight / getliveflightstatus / getliveairportboard / getaircraftlayout

## Airline Fees 2026
- VNA: đổi 600k-1.2M + fare diff | hoàn 600k-2M | hành lý 20-23kg
- VJ: đổi 0-860k + fare diff | SkyBoss refundable | thêm hành lý từ 100k
- QH: đổi 550k-1.1M + fare diff | hoàn 550k-1.6M | 20kg included
- VU: đổi từ 300k + fare diff | tùy điều kiện vé | 20kg included

## Environment — Tools

### ✅ HOẠT ĐỘNG
- Python urllib.request → fetch URL bất kỳ
- GitHub REST API (token sẵn)
- Free APIs: Wikipedia, HN Algolia, Reddit JSON, DDG, npm, PyPI, World Bank, Exchange Rate
- Flight APIs (defaultapi): searchflights, bookflight, getliveflightstatus...
- Code execution: pandas, numpy, matplotlib, json, re

### ❌ KHÔNG DÙNG ĐƯỢC
- Brave Search MCP / Firecrawl MCP (cần npx external)
- YouTube Data API (cần OAuth)
- Meta Ads API (cần Business token)
- Google Analytics (cần OAuth)

### 🔄 WORKAROUND
- Thay web search → HN Algolia + DDG API + Google News RSS + scrape thẳng
- Thay YouTube API → scrape channel HTML public + SocialBlade
- Thay Meta Ads → user export thủ công rồi paste
- Thay Firecrawl → urllib + regex strip_html

## Push GitHub Pattern
```python
import urllib.request, json, base64
TOKEN = "[YOUR_GITHUB_TOKEN]"
REPO = "tano2026/AI-Vibe-Toolkit"

def push_file(path, content, msg):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
    req = urllib.request.Request(url, headers={"Authorization": f"token {TOKEN}"})
    sha = None
    try:
        with urllib.request.urlopen(req) as r:
            sha = json.loads(r.read()).get('sha')
    except: pass
    data = {"message": msg, "content": base64.b64encode(content.encode()).decode()}
    if sha: data["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="PUT")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())['commit']['sha'][:7]
```

## Quy Tắc Quan Trọng
1. KHÔNG bịa số — luôn fetch thật
2. KHÔNG nói "không làm được" trước khi thử ≥3 approach
3. Luôn update TRACKER.md sau push
4. time.sleep(0.7) giữa GitHub API calls
5. Batch 3+ repos song song khi thêm vào kho
6. Output ưu tiên: bảng Markdown > bullets > prose
7. Đặt vé thật: Playwright trên abtrip.vn — không dùng test API
```
