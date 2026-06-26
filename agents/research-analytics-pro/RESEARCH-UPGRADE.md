# Research Capability Upgrade — Hermes Agent

**Version:** 2.0 | **Date:** 2026-06
**Mục đích:** Nâng cấp research từ "phụ thuộc MCP" sang "Python-native, không cần external services"

---

## Vấn đề v1 (cũ)

Agent v1 thiết kế cho Claude Desktop với MCP servers:
- Brave Search MCP → cần API key + npx process
- Firecrawl MCP → cần API key + npx process
- YouTube API → cần OAuth credentials.json
- Kết quả: chạy trong Hermes/OpenClaw → báo "không làm được"

## Giải pháp v2

Thay toàn bộ MCP dependency bằng **Python code execution thuần**:

| Thay thế | Tool cũ | Tool mới |
|----------|---------|----------|
| Web search | Brave Search MCP | HN Algolia API + scrape Google |
| Web scrape | Firecrawl MCP | urllib.request + regex |
| YouTube | YouTube Data API | Scrape channel HTML + SocialBlade |
| File read | MarkItDown MCP | Python built-in + base64 |
| GitHub | GitHub MCP | GitHub REST API trực tiếp |

## Files đã update

1. `agents/research-analytics-pro/system-prompt.md` → v2 (Python-native)
2. `configs/hermes-MEMORY.md` → v2 (stats đúng + workarounds)

## Free APIs không cần key

```
Wikipedia:     https://en.wikipedia.org/api/rest_v1/page/summary/{topic}
HackerNews:    https://hn.algolia.com/api/v1/search?query={q}&tags=story
Reddit:        https://www.reddit.com/r/{sub}/search.json?q={q}&sort=top
npm:           https://registry.npmjs.org/{package}
PyPI:          https://pypi.org/pypi/{package}/json
GitHub Search: https://api.github.com/search/repositories?q={q}
GitHub Trending: https://github.com/trending (scrape HTML)
```

## Research Quality tăng từ đâu

- **Trước:** Không có search tool → hallucinate hoặc từ chối
- **Sau:** Luôn fetch ≥3 nguồn thật → triangulate → cite URL cụ thể

## Cách apply

1. Copy nội dung `system-prompt.md` (v2) vào Hermes project instructions
2. Copy nội dung `hermes-MEMORY.md` (v2) vào `~/.hermes/MEMORY.md`
3. Test: "Research repo SWivid/F5-TTS cho tao" → phải ra data thật với nguồn
