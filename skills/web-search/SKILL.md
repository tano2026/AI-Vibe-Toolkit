---
name: web-search
description: This skill should be used when users need to search the web for information, find current content, look up news articles, search for images, or find videos. It uses DuckDuckGo's search API to return results in clean, formatted output (text, markdown, or JSON). Use for research, fact-checking, finding recent information, or gathering web resources. Also covers Firecrawl (cloud + self-host) setup and tool research methodology.
---

# Web Search

## Overview

Search the web using DuckDuckGo's API to find information across web pages, news articles, images, and videos. Returns results in multiple formats (text, markdown, JSON) with filtering options for time range, region, and safe search.

## When to Use This Skill

Use this skill when users request:
- Web searches for information or resources
- Finding current or recent information online
- Looking up news articles about specific topics
- Searching for images by description or topic
- Finding videos on specific subjects
- Researching a new tool/technology/service ("nghiên cứu cái X giúp tao")
- Configuring web extract backend (Firecrawl, Tavily, etc.)

## Prerequisites

Install the required dependency:

```bash
pip install ddgs
```

This library provides a simple Python interface to DuckDuckGo's search API (renamed from `duckduckgo-search`).

## Core Capabilities

### 1. Basic Web Search

Search for web pages and information:

```bash
python scripts/search.py "<query>"
```

**Example:**
```bash
python scripts/search.py "python asyncio tutorial"
```

Returns the top 10 web results with titles, URLs, and descriptions in a clean text format.

### 2. Limiting Results

Control the number of results returned:

```bash
python scripts/search.py "<query>" --max-results <N>
```

**Example:**
```bash
python scripts/search.py "machine learning frameworks" --max-results 20
```

Useful for:
- Getting more comprehensive results (increase limit)
- Quick lookups with fewer results (decrease limit)
- Balancing detail vs. processing time

### 3. Time Range Filtering

Filter results by recency:

```bash
python scripts/search.py "<query>" --time-range <d|w|m|y>
```

**Time range options:**
- `d` - Past day
- `w` - Past week
- `m` - Past month
- `y` - Past year

**Example:**
```bash
python scripts/search.py "artificial intelligence news" --time-range w
```

Great for:
- Finding recent news or updates
- Filtering out outdated content
- Tracking recent developments

### 4. News Search

Search specifically for news articles:

```bash
python scripts/search.py "<query>" --type news
```

**Example:**
```bash
python scripts/search.py "climate change" --type news --time-range w --max-results 15
```

News results include:
- Article title
- Source publication
- Publication date
- URL
- Article summary/description

### 5. Image Search

Search for images:

```bash
python scripts/search.py "<query>" --type images
```

**Example:**
```bash
python scripts/search.py "sunset over mountains" --type images --max-results 20
```

**Image filtering options:**

Size filters:
```bash
python scripts/search.py "landscape photos" --type images --image-size Large
```
Options: `Small`, `Medium`, `Large`, `Wallpaper`

Color filters:
```bash
python scripts/search.py "abstract art" --type images --image-color Blue
```
Options: `color`, `Monochrome`, `Red`, `Orange`, `Yellow`, `Green`, `Blue`, `Purple`, `Pink`, `Brown`, `Black`, `Gray`, `Teal`, `White`

Type filters:
```bash
python scripts/search.py "icons" --type images --image-type transparent
```
Options: `photo`, `clipart`, `gif`, `transparent`, `line`

Layout filters:
```bash
python scripts/search.py "wallpapers" --type images --image-layout Wide
```
Options: `Square`, `Tall`, `Wide`

Image results include:
- Image title
- Image URL (direct link to image)
- Thumbnail URL
- Source website
- Dimensions (width x height)

### 6. Video Search

Search for videos:

```bash
python scripts/search.py "<query>" --type videos
```

**Example:**
```bash
python scripts/search.py "python tutorial" --type videos --max-results 15
```

**Video filtering options:**

Duration filters:
```bash
python scripts/search.py "cooking recipes" --type videos --video-duration short
```
Options: `short`, `medium`, `long`

Resolution filters:
```bash
python scripts/search.py "documentary" --type videos --video-resolution high
```
Options: `high`, `standard`

Video results include:
- Video title
- Publisher/channel
- Duration
- Publication date
- Video URL
- Description

### 7. Region-Specific Search

Search with region-specific results:

```bash
python scripts/search.py "<query>" --region <region-code>
```

**Common region codes:**
- `us-en` - United States (English)
- `uk-en` - United Kingdom (English)
- `ca-en` - Canada (English)
- `au-en` - Australia (English)
- `de-de` - Germany (German)
- `fr-fr` - France (French)
- `wt-wt` - Worldwide (default)

**Example:**
```bash
python scripts/search.py "local news" --region us-en --type news
```

### 8. Safe Search Control

Control safe search filtering:

```bash
python scripts/search.py "<query>" --safe-search <on|moderate|off>
```

**Options:**
- `on` - Strict filtering
- `moderate` - Balanced filtering (default)
- `off` - No filtering

**Example:**
```bash
python scripts/search.py "medical information" --safe-search on
```

### 9. Output Formats

Choose how results are formatted:

**Text format (default):**
```bash
python scripts/search.py "quantum computing"
```

Clean, readable plain text with numbered results.

**Markdown format:**
```bash
python scripts/search.py "quantum computing" --format markdown
```

Formatted markdown with headers, bold text, and links.

**JSON format:**
```bash
python scripts/search.py "quantum computing" --format json
```

Structured JSON data for programmatic processing.

### 10. Saving Results to File

Save search results to a file:

```bash
python scripts/search.py "<query>" --output <file-path>
```

**Example:**
```bash
python scripts/search.py "artificial intelligence" --output ai_results.txt
python scripts/search.py "AI news" --type news --format markdown --output ai_news.md
python scripts/search.py "AI research" --format json --output ai_data.json
```

The file format is determined by the `--format` flag, not the file extension.

## Output Format Examples

### Text Format
```
1. Page Title Here
   URL: https://example.com/page
   Brief description of the page content...

2. Another Result
   URL: https://example.com/another
   Another description...
```

### Markdown Format
```markdown
## 1. Page Title Here

**URL:** https://example.com/page

Brief description of the page content...

## 2. Another Result

**URL:** https://example.com/another

Another description...
```

### JSON Format
```json
[
  {
    "title": "Page Title Here",
    "href": "https://example.com/page",
    "body": "Brief description of the page content..."
  },
  {
    "title": "Another Result",
    "href": "https://example.com/another",
    "body": "Another description..."
  }
]
```

## Common Usage Patterns

### Research on a Topic

Gather comprehensive information about a subject:

```bash
# Get overview from web
python scripts/search.py "machine learning basics" --max-results 15 --output ml_web.txt

# Get recent news
python scripts/search.py "machine learning" --type news --time-range m --output ml_news.txt

# Find tutorial videos
python scripts/search.py "machine learning tutorial" --type videos --max-results 10 --output ml_videos.txt
```

### Current Events Monitoring

Track news on specific topics:

```bash
python scripts/search.py "climate summit" --type news --time-range d --format markdown --output daily_climate_news.md
```

### Finding Visual Resources

Search for images with specific criteria:

```bash
python scripts/search.py "data visualization examples" --type images --image-type photo --image-size Large --max-results 25 --output viz_images.txt
```

### Fact-Checking

Verify information with recent sources:

```bash
python scripts/search.py "specific claim to verify" --time-range w --max-results 20
```

### Academic Research

Find resources on scholarly topics:

```bash
python scripts/search.py "quantum entanglement research" --time-range y --max-results 30 --output quantum_research.txt
```

### Market Research

Gather information about products or companies:

```bash
python scripts/search.py "electric vehicle market 2025" --max-results 20 --format markdown --output ev_market.md
python scripts/search.py "EV news" --type news --time-range m --output ev_news.txt
```

## Preferred Method: execute_code with ddgs (In-session)

For token cost-sensitive environments (Nobitano), use `execute_code` with `ddgs` directly — no subprocess overhead.

**Text search (3 lines):**
```python
from ddgs import DDGS
with DDGS() as ddgs:
    results = list(ddgs.text("query", max_results=5))
```

**Full example with output:**
```python
from ddgs import DDGS
with DDGS() as ddgs:
    results = list(ddgs.text("your query", max_results=5))
    for r in results:
        print(f"{r.get('title')}  {r.get('href')}  {r.get('body','')[:150]}")
```

**Search types:** `ddgs.text(...)`, `ddgs.news(...)`, `ddgs.images(...)`, `ddgs.videos(...)`

**Common params:** `keywords`, `region` (`'wt-wt'` default), `safesearch`, `max_results`, `timelimit` (`'d'|'w'|'m'|'y'`)

**Token cost:** Near-zero — only result text enters context. 5-10x cheaper than browser.

**Alternative (terminal):** `python scripts/search.py "query" -n 5`

## MCP vs DDG Decision

For Nobitano's use case, MCP research servers are overkill:
- **DDG (ddgs):** Free, 0 setup, ~1s, use for all general searches
- **MCP Fetch/Exa/Tavily:** Need npm install + API keys, protocol overhead, slower
- **Rule:** DDG first. Fallback to Firecrawl/curl/web_extract on specific URLs. MCP only if both fail.

## Tool Research Methodology (Nobitano's "nghiên cứu giúp tao" pattern)

Khi user nói "nghiên cứu cái X đi", follow pattern sau:

1. **Evaluate core features** — công cụ làm được gì, architecture (stack, license, stars)
2. **Pricing analysis** — free tier, giới hạn, self-host được không
3. **Trade-off framework** — so sánh các option (cloud vs self-host, free vs paid)
4. **Relevance mapping** — giải quyết nhu cầu cụ thể gì của user
5. **Phased recommendation** — Phase 1: rẻ nhất, 0 setup; Phase 2: scale
6. **Implementation path** — đăng ký/config thế nào, tích hợp ra sao

Output format: bảng trade-off + recommendation ngắn gọn, có thể hành động ngay.

## GitHub Repo Research & Curation ("nghiên cứu repo GitHub" pattern)

Khi user bảo "trên GitHub có cái X, nghiên cứu giúp tao" hoặc "tìm trên GitHub mấy cái Y, chắt lọc về cho tao":

### Phase 1: Discovery — Tìm repo

```bash
curl -s "https://api.github.com/search/repositories?q=<query>&sort=stars&order=desc&per_page=10"
```

**Cách search hiệu quả:**
- `q=ace-step+music&sort=stars` — keyword + sort
- `q=awesome+skills` — keyword đơn giản  
- `q=topic:awesome+topic:skills` — filter by topics
- Thêm `in:name`, `in:description`, `in:readme` nếu cần narrow

**Đánh giá nhanh từ search results:**
- ⭐ Stars + 📝 Description + 🏷️ Topics + 📅 Last updated
- **Signal cao:** 20K+ stars, topics agent/skills cụ thể, updated gần đây
- **Signal thấp:** <1K stars, no description, không updated >1 năm

### Phase 2: Evaluate — Đọc thông tin chi tiết repo

```bash
curl -s "https://api.github.com/repos/<owner>/<repo>" | python -c ...
curl -s "https://api.github.com/repos/<owner>/<repo>/readme" | python -c ...
```

**Checklist đánh giá:**
- README có content thực chất hay chỉ banner + link signup? → Xác định chất lượng
- Cấu trúc thư mục: skills/ riêng hay các folder skill ở root?
- Có content thật (SKILL.md, hướng dẫn chi tiết) hay chỉ danh sách link?
- Là collection curated hay AI-generated bulk?

### Phase 3: Explore — Đào sâu cấu trúc

```bash
curl -s "https://api.github.com/repos/<owner>/<repo>/contents/"
```

**Patterns thường gặp:**
- `skills/` directory với từng skill folder → Antigravity-style
- Skill folders ở root level → Composio-style
- README chỉ listing link đến platform khác → VoltAgent-style (skills host ở officialskills.sh)

### Phase 4: Curate — Chắt lọc

**Selection criteria (ưu tiên từ cao→thấp):**
1. Skills từ official team (Anthropic, Vercel, Stripe, Google, etc.) → **giá trị nhất**
2. Skills có mô tả rõ ràng, use case cụ thể
3. Skills thuộc domain user quan tâm (dev, business, marketing, automation)
4. Skills generic reusable (code review, architecture, SEO, testing)
5. Loại bỏ: quảng cáo platform, AI-slop, skill quá narrow

### Phase 5: Present — Trình bày so sánh

Output format — structured with: repo overview → category breakdown → best skills → recommendation

```markdown
## 📊 Tổng quan [N] repo

| | Repo A | Repo B | Repo C |
|---|---|---|---|
| ⭐ | X | Y | Z |
| Skills | N | M | K |
| Chất lượng | Cao/Trung bình/Thấp | ... | ... |
| Điểm mạnh | ... | ... | ... |

## 🥇 [Tên] — Kho đáng dùng nhất

**[Team/Company] skills:**
- `team/skill-name` — Mô tả ngắn

**[Category] skills:**
- `skill-name` — Mô tả

## 📌 Kết luận

Khuyến nghị + lý do ngắn gọn.
```

### Pitfalls

1. **API rate limit:** GitHub unauthenticated = 60 req/h. Nếu rate-limit, dùng `curl -u "token:''"` với token cá nhân.
2. **Branch name:** Không phải repo nào cũng dùng `main` — thử `master` nếu 404.
3. **Không đọc được README từ API:** Thử `raw.githubusercontent.com/<owner>/<repo>/main/README.md`
4. **Repo có thể đổi tên:** Nếu 404, search lại bằng tên gốc từ kết quả search.
5. **Skills quantity ≠ quality:** Repo 1,500 skills có thể 90% là AI-slop. Ưu tiên curated (official team) hơn số lượng.
6. **Telegram format:** Ko có table — dùng bullet list hoặc | key: value | dạng code block.

## 🔧 Fallback: GitHub API Search (khi web_search/web_extract không config)

Khi Hermes chưa có web_search provider (hoặc bị rate-limit), dùng **curl + GitHub API** để tìm repo, đọc README.

### Tìm repo trên GitHub

```bash
curl -s "https://api.github.com/search/repositories?q=<query>&sort=stars&order=desc&per_page=10" | python -c "
import json, sys
d = json.load(sys.stdin)
for r in d.get('items', [])[:10]:
    print(f'⭐ {r[\"stargazers_count\"]:>5} | {r[\"full_name\"]:40s} | {r[\"description\"][:100] if r[\"description\"] else \"(no desc)\"}')
"
```

**Cách search hiệu quả:**
- `q=awesome+skills` — keyword đơn giản
- `q=ace-step+music&sort=stars` — thêm sort để ưu tiên sao
- Thêm `in:name` hoặc `in:description` nếu cần filter

### Lấy thông tin repo

```bash
curl -s "https://api.github.com/repos/<owner>/<repo>" | python -c "
import json, sys
d = json.load(sys.stdin)
print(f'⭐ {d[\"stargazers_count\"]} | {d[\"full_name\"]}')
print(f'📝 {d[\"description\"]}')
print(f'🏷️ {d.get(\"topics\", [])}')
print(f'📅 Updated: {d[\"updated_at\"][:10]}')
print(f'👁️ Watchers: {d[\"subscribers_count\"]}, Forks: {d[\"forks_count\"]}')
print(f'🔗 {d[\"html_url\"]}')
"
```

### Đọc README.md

```bash
curl -s "https://api.github.com/repos/<owner>/<repo>/readme" | python -c "
import json, sys, base64
d = json.load(sys.stdin)
content = base64.b64decode(d['content']).decode('utf-8')
print(content[:2000])
"
```

**Khi nào dùng:**
- web_search tool chưa config (Hermes mới setup)
- Cần thông tin GitHub chi tiết (sao, topics, description)
- Rate-limit: GitHub API unauthenticated = 60 req/h — đủ cho research nhẹ
- Giới hạn: không search được web tổng quát, chỉ GitHub

## ⚠️ Researching Blocked Websites (Cloudflare / CAPTCHA bypass)

Khi target site bị Cloudflare, CAPTCHA, hoặc các anti-bot khác chặn direct access:

### Phương pháp 1: Wayback Machine (ưu tiên)
1. **Truy cập archive:** `https://web.archive.org/web/*/https://target.com`
2. **Calendar view:** Chọn ngày gần nhất có snapshot (vòng tròn xanh trên calendar)
3. **Click snapshot:** Click vòng tròn trên calendar → load archived page
4. **Direct URL:** Nếu biết timestamp: `https://web.archive.org/web/20260514000000/https://target.com/pricing`
5. **CDX API (nhanh hơn):** `http://web.archive.org/cdx/search/cdx?url=target.com&output=text&limit=10&fl=timestamp,original&filter=statuscode:200`

### Phương pháp 2: Alternative sources
- **Google cache:** `https://webcache.googleusercontent.com/search?q=cache:https://target.com`
- **Textise dot iitty:** Thay `.com` bằng `.com.textise dot iitty` (bypass một số block)
- **textise dot iitty proxy:** `https://r.jina.ai/http://target.com`

### Khi nào dùng
- Site context.dev, producthunt.com, các site dùng Cloudflare
- Cần lấy pricing, feature list từ SaaS product
- API documentation behind auth wall

## Firecrawl — Web Search & Scrape Backend

**Firecrawl** (github.com/firecrawl/firecrawl, 127k⭐) là API search + scrape + crawl toàn diện, MIT License. Chi tiết setup xem `references/firecrawl-setup.md`.

**Hai mode:**
- **Cloud Free Tier** ($0/th, 1k pages) — dùng ngay, 0 setup, chỉ cần API key
- **Self-Host Docker** (free, unlimited) — khi cần scale

**Dùng Firecrawl khi:**
- Cần crawl sâu toàn bộ site đối thủ (eSIM pricing, airline routes)
- Cần extract structured data (LLM-powered)
- web_extract backend chưa configure — Firecrawl thay thế được cả search lẫn extract
- Cần Markdown sạch từ URL (output tốt hơn curl/web_extract mặc định)

**Khi nào vẫn dùng DDGS:**
- Search nhanh 5-10 kết quả, 0 setup, lightweight
- Research nhẹ, token-cost sensitive

**Config Hermes Agent:**
```yaml
web:
  backend: firecrawl           # shared fallback
  search_backend: firecrawl    # explicit per-capability
  extract_backend: firecrawl   # explicit per-capability
  use_gateway: false
```

**Cloud mode:** Chỉ cần env var `FIRECRAWL_API_KEY=fc-xxxx...` trong `.env`
**Self-host mode:** Thêm `web.firecrawl.api_url: http://localhost:3002` trong config

## Implementation Approach

When users request web searches:

1. **Identify search intent**:
   - What type of content (web, news, images, videos)?
   - How recent should results be?
   - How many results are needed?
   - Any filtering requirements?

2. **Configure search parameters**:
   - Choose appropriate search type (`--type`)
   - Set time range if currency matters (`--time-range`)
   - Adjust result count (`--max-results`)
   - Apply filters (image size, video duration, etc.)

3. **Select output format**:
   - Text for quick reading
   - Markdown for documentation
   - JSON for further processing

4. **Execute search**:
   - Run the search command
   - Save to file if results need to be preserved
   - Print to stdout for immediate review

5. **Process results**:
   - Read saved files if needed
   - Extract URLs or specific information
   - Combine results from multiple searches

## Quick Reference

**Command structure:**
```bash
python scripts/search.py "<query>" [options]
```

**Essential options:**
- `-t, --type` - Search type (web, news, images, videos)
- `-n, --max-results` - Maximum results (default: 10)
- `--time-range` - Time filter (d, w, m, y)
- `-r, --region` - Region code (e.g., us-en, uk-en)
- `--safe-search` - Safe search level (on, moderate, off)
- `-f, --format` - Output format (text, markdown, json)
- `-o, --output` - Save to file

**Image-specific options:**
- `--image-size` - Size filter (Small, Medium, Large, Wallpaper)
- `--image-color` - Color filter
- `--image-type` - Type filter (photo, clipart, gif, transparent, line)
- `--image-layout` - Layout filter (Square, Tall, Wide)

**Video-specific options:**
- `--video-duration` - Duration filter (short, medium, long)
- `--video-resolution` - Resolution filter (high, standard)

**Get full help:**
```bash
python scripts/search.py --help
```

## Best Practices

1. **Be specific** - Use clear, specific search queries for better results
2. **Use time filters** - Apply `--time-range` for current information
3. **Adjust result count** - Start with 10-20 results, increase if needed
4. **Save important searches** - Use `--output` to preserve results
5. **Choose appropriate type** - Use news search for current events, web for general info
6. **Use JSON for automation** - JSON format is easiest to parse programmatically
8. **When user says "nghiên cứu cái X"** — follow Tool Research Methodology, produce trade-off table + recommendation

## Troubleshooting

**Common issues:**

- **"Missing required dependency"**: Run `pip install ddgs`
- **No results found / 0 results**: The old `duckduckgo-search` package has been deprecated and frequently returns 0 results. Install the renamed `ddgs` library instead (`pip install ddgs`), which our scripts and tools support natively.
- **No results found**: Try broader search terms or remove time filters
- **Timeout errors**: The search service may be temporarily unavailable; retry after a moment
- **Rate limiting**: Space out searches if making many requests
- **Unexpected results**: DuckDuckGo's results may differ from Google; try refining the query
- **Firecrawl cloud không hoạt động**: Check `FIRECRAWL_API_KEY` trong `.env`. Lưu ý: file `.env` trên Windows được credential-protected — không thể dùng agent tools để sửa, phải dùng `echo 'KEY=val' >> ~/.hermes/.env` trong terminal. Sau khi thêm, cần `/new` (session mới) để env var có hiệu lực. Provider built-in (Hermes Agent 0.14+), không cần plugin.

**Limitations:**

- Results quality depends on DuckDuckGo's index and algorithms
- No advanced search operators (unlike Google's site:, filetype:, etc.)
- Image and video searches may have fewer results than web search
- No control over result ranking or relevance scoring
- Some specialized searches may work better on dedicated search engines

## Advanced Use Cases

### Combining Multiple Searches

Gather comprehensive information by combining search types:

```bash
# Web overview
python scripts/search.py "topic" --max-results 15 --output topic_web.txt

# Recent news
python scripts/search.py "topic" --type news --time-range w --output topic_news.txt

# Images
python scripts/search.py "topic" --type images --max-results 20 --output topic_images.txt
```

### Programmatic Processing

Use JSON output for automated processing:

```bash
python scripts/search.py "research topic" --format json --output results.json
# Then process with another script
python analyze_results.py results.json
```

### Building a Knowledge Base

Create searchable documentation from web results:

```bash
# Search multiple related topics
python scripts/search.py "topic1" --format markdown --output kb/topic1.md
python scripts/search.py "topic2" --format markdown --output kb/topic2.md
python scripts/search.py "topic3" --format markdown --output kb/topic3.md
```

## Linked Resources

- `references/firecrawl-setup.md` — Full setup guide for Firecrawl (cloud + self-host), SDK usage, Hermes Agent config, pricing, trade-off decision framework
- `references/context-dev.md` — Context.dev reference: competitor web scraping + brand data API, pricing, features, comparison vs Firecrawl
- `references/mcp-research-servers.md` — MCP research server comparison and setup notes
- `references/astrology-tuv-vi-tools.md` — Astrology / Tử Vi tool map (iztro, ziwei-doushu, MCP servers, build options) — research date 2026-06-02
- `scripts/search.py` — Main search tool implementing DuckDuckGo search functionality. Supports all search types, filtering, output formats, and file saving.