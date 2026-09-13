# just-scrape (ScrapeGraphAI) — Skill CLI

## TL;DR
CLI scrape/extract/search/crawl/monitor cho AI agent, chạy bằng lệnh tự nhiên qua ScrapeGraphAI backend (LLM-powered extraction). Cài 1 lệnh `npx skills add`, agent tự biết dùng, không cần đọc docs API riêng.

## Tool này dùng để làm gì
`just-scrape` là CLI wrap quanh ScrapeGraphAI (v2 API), cho Claude Code/Cursor gọi trực tiếp mà không cần tự viết code gọi API:
- `scrape` — lấy 1 URL biết trước, trả về markdown/html/screenshot/links/images/summary/branding/JSON có cấu trúc
- `extract` — lấy structured JSON từ 1 URL theo prompt + schema tuỳ chọn
- `search` — search web, chạy extraction luôn trên kết quả
- `crawl` — cào nhiều trang trong 1 khu vực site giới hạn
- `monitor` — hẹn giờ check lại 1 trang, báo qua webhook khi có thay đổi
- `history`, `credits`, `validate` — quản lý vận hành

Khớp đúng Bước 2 (Research) trong Quy trình xử lý input của kho: khi Nobitano quẳng link tool/repo mới, Claude có thể dùng `just-scrape` để cào docs/README/feature list thay vì tự fetch tay.

## Setup từng bước
1. Cài skill:
```bash
npx skills add https://github.com/scrapegraphai/just-scrape --skill just-scrape
```
2. Set API key (bắt buộc, trả phí theo credit):
```bash
export SGAI_API_KEY="sgai-xxxxx"   # lấy tại dashboard ScrapeGraphAI
```
3. Test nhanh:
```bash
just-scrape scrape https://example.com --json
```

## Ví dụ thực tế
Nobitano quẳng 1 tên tool mới chưa có link cụ thể → Claude gọi `just-scrape search "TênTool AI agent skill" --num-results 3 --json` để tìm trang chính thức, rồi `just-scrape smart-scraper <url> -p "Extract setup steps, star count, key features" --json` để lấy dữ liệu có cấu trúc ngay, khỏi phải đọc raw HTML.

## Lưu ý / Lỗi thường gặp
- Không có `SGAI_API_KEY` → lệnh chạy được (skill load OK) nhưng mọi call thật sẽ fail — phải set biến môi trường trước.
- Trả phí theo credit ScrapeGraphAI, không free — cân đối lượng gọi khi research nhiều tool 1 lúc.
- Luôn thêm `--json` khi agent gọi (không cần spinner/banner, đỡ token).
- Có MCP Server thay thế nếu cần tích hợp sâu hơn trong Cursor/Claude Desktop — CLI này hợp hơn cho tác vụ nhanh trong chat.

## Đánh giá cá nhân
- Điểm mạnh: gọn, đúng nhu cầu research của kho (không cần Firecrawl/Crawl4AI nặng hơn cho việc nhanh); output JSON sẵn cho agent xử lý tiếp.
- Điểm yếu: phải trả phí theo credit, không miễn phí như Crawl4AI đã có trong kho; repo còn nhỏ (~40⭐), audit MEDIUM risk.
- Có nên dùng không: 7/10 — dùng cho việc scrape/extract nhanh gọn 1-2 URL khi research tool mới; việc cào lớn/lặp lại vẫn ưu tiên Crawl4AI/Firecrawl đã có sẵn trong kho.

## Link
- Repo: https://github.com/scrapegraphai/just-scrape
- Docs: https://docs.scrapegraphai.com/services/cli/ai-agent-skill

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json, os

def just_scrape_extract(url: str, prompt: str) -> dict:
    """Gọi thẳng just-scrape CLI (đã cài qua npx skills add), không dùng MCP."""
    env = os.environ.copy()
    env["SGAI_API_KEY"] = "[YOUR_SGAI_API_KEY]"
    result = subprocess.run(
        ["just-scrape", "smart-scraper", url, "-p", prompt, "--json"],
        capture_output=True, text=True, env=env, timeout=60
    )
    return json.loads(result.stdout)
```

### OpenClaw
```bash
npx skills add https://github.com/scrapegraphai/just-scrape --skill just-scrape
# gọi trong session: "dùng just-scrape scrape <url> lấy markdown"
```

### Antigravity
```bash
# Không cần deploy service riêng — chỉ cần cài CLI global trên VPS 1 lần
npm install -g @scrapegraphai/just-scrape 2>/dev/null || npx skills add https://github.com/scrapegraphai/just-scrape --skill just-scrape
```
> ⚠️ Set `SGAI_API_KEY` trong `.env` của VPS, không hardcode trong script.
