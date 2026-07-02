# Firecrawl — GitHub Repo

## TL;DR
Firecrawl là API biến bất kỳ website nào thành markdown/JSON sạch, sẵn sàng nhét vào LLM — không cần tự viết selector, không cần lo JS render hay chống bot. 141K+ stars, dùng bởi hầu hết agent framework lớn hiện nay.

## Repo này dùng để làm gì
Nói ngắn: mày quăng 1 URL vào, nó trả về markdown sạch (hoặc JSON có cấu trúc), đã lọc bỏ header/footer/ads, không còn HTML rác. So với việc tự viết BeautifulSoup/Playwright rồi maintain selector mỗi khi site đổi UI, Firecrawl xử lý hết phần khó: render JS, bypass chống bot, xoay proxy.

6 khả năng chính:
- **Search** — search web + trả luôn nội dung trang kết quả (khỏi search rồi scrape riêng)
- **Scrape** — 1 URL → markdown/JSON sạch
- **Crawl** — quét đệ quy cả site
- **Map** — liệt kê hết URL trên 1 site (audit site, tìm link)
- **Interact** — tương tác trang động (click, scroll, login, chờ load)
- **Agent** (mới, thay cho /extract cũ) — chỉ cần tả bằng lời "tìm giá plan của Notion", nó tự search + navigate + trả data, không cần biết URL trước

## Setup từng bước
1. Lấy API key tại firecrawl.dev (có free tier)
2. Cài SDK:
```bash
pip install firecrawl-py
```
3. Scrape 1 trang:
```python
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-YOUR_API_KEY")
doc = app.scrape("https://example.com")
print(doc.markdown)
```
4. Muốn tự host (free, không giới hạn request nhưng phải tự lo hạ tầng):
```bash
git clone https://github.com/firecrawl/firecrawl.git
cd firecrawl
docker-compose up -d
# rồi trỏ SDK vào: --api-url http://localhost:3002
```

## Ví dụ thực tế
Research Pro của tao cần bóc data đối thủ ABTRIP (các trang OTA khác) để so giá. Trước đây phải tự viết script requests + BeautifulSoup, gặp trang nào render bằng React là toang. Với Firecrawl:
```python
result = app.scrape("https://competitor-ota.vn/tour-abc")
# result.markdown là text sạch, không còn div/class rác, feed thẳng vào DeepSeek để phân tích giá
```
Hoặc dùng Agent khi không biết URL cụ thể:
```python
result = app.agent(prompt="Tìm giá tour Đà Lạt 3N2Đ trên các web OTA VN")
```

## Lưu ý / Lỗi thường gặp
- **License AGPL-3.0** — nếu tự host và sửa code rồi phân phối lại (SaaS công khai) phải open-source phần sửa. Dùng nội bộ (như Research Pro) thì không vấn đề.
- **Endpoint /extract đã deprecated**, chuyển hết qua /agent — code cũ dùng extract sẽ warning, nên update sớm.
- **Free tier giới hạn credit** — scrape nhiều (crawl cả site) tốn credit nhanh hơn tưởng, cân đối với OmniRoute budget.
- **Self-host cần Docker + Postgres + Redis** — không nhẹ như 1 script Python, nếu chỉ scrape vài chục trang/ngày thì dùng cloud API rẻ hơn công tự host.

## Đánh giá cá nhân
- **Điểm mạnh:** Cover 96% web kể cả site JS-heavy, P95 latency 3.4s, output markdown giảm ~67% token so với HTML thô — tiết kiệm token đáng kể khi feed vào DeepSeek/Claude. MCP server + CLI + skill có sẵn, cắm vào OpenClaw/Hermes gần như plug-and-play.
- **Điểm yếu:** Cloud API tính phí theo request, scale lớn (crawl hàng nghìn trang/ngày) sẽ tốn hơn tự viết scraper thô. Self-host đòi hạ tầng nặng hơn 1 script đơn giản.
- **Có nên dùng không:** 9/10 — đúng thứ Research Pro v4 cần (thay/bổ sung Tavily cho phần scrape có cấu trúc), tiết kiệm thời gian maintain scraper hơn hẳn tự viết.

## Link
- Repo: https://github.com/firecrawl/firecrawl
- Docs: https://docs.firecrawl.dev
- MCP: https://github.com/firecrawl/firecrawl-mcp-server

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

FIRECRAWL_KEY = "fc-YOUR_API_KEY"

def firecrawl_scrape(url):
    req = urllib.request.Request(
        "https://api.firecrawl.dev/v2/scrape",
        data=json.dumps({"url": url, "formats": ["markdown"]}).encode(),
        headers={
            "Authorization": f"Bearer {FIRECRAWL_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

# Dùng trong Research Pro pipeline
data = firecrawl_scrape("https://example.com")
print(data["data"]["markdown"])
```

### OpenClaw
```bash
# Cài MCP server để OpenClaw gọi Firecrawl trực tiếp qua browser automation layer
npx -y firecrawl-mcp
# hoặc /skill install firecrawl (nếu skill registry của OpenClaw có sẵn)
```

### Antigravity
```bash
# Self-host Firecrawl trên VPS Tencent Cloud nếu muốn không giới hạn request
git clone https://github.com/firecrawl/firecrawl.git
cd firecrawl && docker-compose up -d
# Expose port 3002, trỏ Hermes vào http://<vps-ip>:3002
```
> ⚠️ Self-host cần RAM đủ cho Postgres + Redis + Playwright service — kiểm tra RAM VPS trước, tránh lặp lỗi RAM constraint như Chatwoot.
