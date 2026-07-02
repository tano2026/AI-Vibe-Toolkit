# Tavily — MCP Server

## TL;DR
Search API build riêng cho AI agent chứ không phải cho người — query vào, ra thẳng JSON sạch (summary, content, citation) sẵn sàng nhét vào prompt, không phải tự bóc HTML như search thường. Free 1,000 credit/tháng.

## Tool này dùng để làm gì
Search engine bình thường (Google, Bing) trả về cho con người: 10 cái link, tự bấm vào đọc. Tavily trả thẳng nội dung đã tóm — mỗi kết quả có sẵn content snippet, có thể bật thêm `include_answer` để nó tự tổng hợp 1 câu trả lời từ nhiều nguồn luôn, khỏi cần agent tự synthesize.

4 tool chính trong MCP server:
- `tavily-search` — search web, chọn depth basic/advanced, filter theo topic (general/news), time range, domain include/exclude
- `tavily-extract` — quăng list URL vào, nó rút content sạch ra markdown (giống Firecrawl nhưng đơn giản hơn, không có JS rendering sâu)
- `tavily-crawl` — crawl đệ quy từ 1 URL gốc, nhận instruction tiếng tự nhiên kiểu "chỉ crawl trang docs"
- `tavily-map` — chỉ lấy sitemap/cấu trúc URL, không lấy content

## Setup từng bước
1. Đăng ký tài khoản tại tavily.com, lấy API key (free tier 1,000 credit/tháng, không cần thẻ)
2. Cài MCP server (remote hoặc local, tùy client):
```bash
npx -y tavily-mcp
```
3. Set biến môi trường:
```bash
export TAVILY_API_KEY="tvly-xxxxxxxx"
```
4. Add vào MCP config (Claude Desktop / Cursor / OpenClaw) trỏ tới server trên, hoặc dùng bản remote nếu client hỗ trợ

## Ví dụ thực tế
Research Pro cần trả lời "AI content automation tool nào mới nổi tháng này cho TikTok VN" — gọi `tavily-search` với `topic="news"`, `search_depth="advanced"`, `include_answer=true`. Trả về: 5-8 kết quả đã rank theo relevance, mỗi cái có content snippet tóm tắt sẵn ~200-400 từ, cộng thêm 1 câu answer tổng hợp AI-generated ở đầu. So với Brave Search (đã có trong kho) trả raw link + meta description ngắn — Tavily tiết kiệm hẳn 1 bước fetch+parse từng trang.

## Lưu ý / Lỗi thường gặp
- **Đã có Firecrawl trong kho làm việc tương tự** — đây là điểm cần cân nhắc thật kỹ trước khi bật thêm. Benchmark độc lập (AIMultiple, 100 query thật) xếp Firecrawl hạng #2, Tavily hạng #5 trong nhóm search API cho AI agent. Cộng đồng r/mcp gần đây cũng nhiều người report chất lượng search của Tavily "ổn với query chung chung, nhưng ra rác với query kỹ thuật/niche" và hit rate limit free tier khá nhanh.
- Rate limit thấp: 100 RPM cho hầu hết endpoint ở dev key, riêng endpoint `research` chỉ 20 RPM
- Nebius mua lại Tavily (thoả thuận 275-400 triệu USD công bố tháng 2/2026), tới giờ vẫn chưa có thông báo chính thức đóng deal — theo dõi thêm vì có thể ảnh hưởng chính sách API/giá sau này
- Search chỉ trong phạm vi web thường — không đụng được SEC filings, PubMed, academic paper trả phí
- Chất lượng mô tả tool (`extract`, `crawl`, `map`) trong MCP server bị chấm D-grade ở 1 audit độc lập — mô tả sơ sài, agent có thể chọn nhầm tool nếu prompt không rõ

## Đánh giá cá nhân
- **Điểm mạnh:** setup nhanh, JSON output sạch không cần hậu xử lý, `include_answer` tiện cho quick lookup, tích hợp sẵn với LangChain/CrewAI nếu sau này mở rộng framework
- **Điểm yếu:** overlap khá nhiều với Firecrawl đã có sẵn trong kho — Firecrawl mạnh hơn ở phần extract/scrape trang JS-heavy, Tavily chỉ nhỉnh hơn ở phần search discovery (tìm URL mới) nhờ ranking tối ưu cho AI. Không phải phải-có, chỉ là nice-to-have nếu cần thêm 1 nguồn search độc lập để đối chiếu chéo (tránh single point of failure khi Brave Search hoặc Firecrawl bị rate limit)
- **Có nên dùng không:** 6/10 — không nên thay thế Firecrawl, chỉ nên bật thêm cho Research Pro như 1 nguồn search THỨ 2 để cross-check (đúng tinh thần "không tin 1 nguồn duy nhất" ở Lớp 1 của Research Pro), free tier đủ dùng cho tần suất research vài lần/ngày

## Link
- Docs: https://docs.tavily.com
- Pricing: https://www.tavily.com/pricing
- MCP registry: npm package `tavily-mcp`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json, os

TAVILY_KEY = os.environ.get("TAVILY_API_KEY", "tvly-xxxxxxxx")

def tavily_search(query, depth="basic", topic="general", include_answer=True):
    payload = {
        "api_key": TAVILY_KEY,
        "query": query,
        "search_depth": depth,       # "basic" hoặc "advanced"
        "topic": topic,               # "general" hoặc "news"
        "include_answer": include_answer,
        "max_results": 8
    }
    req = urllib.request.Request(
        "https://api.tavily.com/search",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

# vi du dung trong Research Pro cross-check
result = tavily_search("AI content automation TikTok VN 2026", depth="advanced", topic="news")
print(result.get("answer"))
for r in result["results"]:
    print(r["title"], "-", r["url"])
```

### OpenClaw
```bash
npx -y tavily-mcp
# set env truoc: export TAVILY_API_KEY="tvly-xxxxxxxx"
# them vao openclaw MCP config, alias "tavily"
```

### Antigravity
```bash
# khong can self-host - la managed API, chi can set env tren VPS
echo 'export TAVILY_API_KEY="tvly-xxxxxxxx"' >> ~/.bashrc
```
> ⚠️ Đừng gọi Tavily làm nguồn search DUY NHẤT — dùng song song với Brave Search/Firecrawl đã có, đúng nguyên tắc "đối chiếu chéo" của Research Pro. Free tier 1,000 credit/tháng cạn nhanh nếu để agent tự động chạy research theo lịch (schedule).
