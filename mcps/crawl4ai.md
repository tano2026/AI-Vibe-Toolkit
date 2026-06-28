# Crawl4AI MCP — Cào Web Free Không Giới Hạn

> Giống Firecrawl nhưng **hoàn toàn free, không giới hạn** — tự host trên máy mày. Dành cho ai cào nhiều mà không muốn trả tiền.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Scrape web không giới hạn, chuyển thành Markdown cho AI đọc |
| **Độ khó setup** | ⭐⭐⭐☆☆ Trung bình (cần cài Docker) |
| **Cần biết code không** | Biết tí (chạy vài lệnh terminal) |
| **Free hay trả phí** | **Free hoàn toàn, không giới hạn** |
| **GitHub** | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) ⭐ 63,000+ |

---

## 🎯 So sánh với Firecrawl

| | Firecrawl | Crawl4AI |
|--|-----------|----------|
| Giá | Free 500/tháng | **Free không giới hạn** |
| Setup | Dễ hơn | Cần Docker |
| Tốc độ | Nhanh | Nhanh |
| Phù hợp | Dùng thỉnh thoảng | Cào nhiều hàng ngày |

**Chọn Crawl4AI khi:** Mày cào web thường xuyên, không muốn lo hết credits.

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Cài Docker Desktop
# Tải tại: docker.com/products/docker-desktop

# Bước 2: Chạy Crawl4AI
docker run -d -p 11235:11235 --name crawl4ai --shm-size=1g unclecode/crawl4ai:latest

# Bước 3: Thêm vào claude_desktop_config.json
{
  "mcpServers": {
    "crawl4ai": {
      "command": "npx",
      "args": ["-y", "mcp-crawl4ai"]
    }
  }
}

# Restart Claude Desktop → Done
```

---

## 💡 Dùng thế nào

```
Prompt ví dụ:

"Cào toàn bộ trang blog này: https://example.com/blog
 Lấy hết bài viết về chủ đề AI
 Tóm tắt top 5 bài hay nhất"

→ Không giới hạn số trang, không tốn credit
```

---

## ⚠️ Lưu ý

- **Cần Docker Desktop chạy nền** — nếu tắt Docker là mất kết nối
- Lần đầu download image hơi lâu (~500MB)
- RAM cần ít nhất 4GB trống

---

## 🔗 Hay kết hợp với

- **Firecrawl** — dùng Crawl4AI cho cào bulk, Firecrawl cho cào nhanh không cần setup
- **Sequential Thinking** — cào data xong bảo AI phân tích có hệ thống

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐☆☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐⭐ |
| Value for money | ⭐⭐⭐⭐⭐ (free!) |

**Tóm lại:** Nếu mày chịu khó setup Docker 1 lần → cào web miễn phí mãi mãi. 63k stars không phải đùa.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/unclecode/crawl4ai*

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
import urllib.request, json

# Option A: Nếu Antigravity đã deploy self-hosted
CRAWL4AI_URL = "http://localhost:11235"

def crawl4ai_scrape(url, server_url=CRAWL4AI_URL):
    payload = json.dumps({"urls": [url], "crawler_params": {
        "headless": True, "verbose": False
    }, "extra": {"word_count_threshold": 10}}).encode()
    req = urllib.request.Request(
        f"{server_url}/crawl", data=payload,
        headers={"Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["results"][0]["markdown"]["raw_markdown"]

# Option B: Python SDK trực tiếp (nếu Antigravity pip install)
# from crawl4ai import AsyncWebCrawler
# async with AsyncWebCrawler() as crawler:
#     result = await crawler.arun(url="https://example.com")
#     print(result.markdown)

# Dùng: markdown = crawl4ai_scrape("https://techcrunch.com/ai")
```

### OpenClaw
```bash
npx -y @unclecode/crawl4ai-mcp
```

### Antigravity
```bash
# Self-host (Docker):
docker pull unclecode/crawl4ai:latest
docker run -d -p 11235:11235 --name crawl4ai unclecode/crawl4ai:latest
# Verify: curl http://localhost:11235/health

# Hoặc pip install:
pip install crawl4ai
crawl4ai-setup
```
> ⚠️ Antigravity deploy Docker → Hermes gọi localhost:11235. Free unlimited.
