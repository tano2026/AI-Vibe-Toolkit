# Firecrawl MCP — Cào Web Sạch, AI Đọc Được Ngay

> Paste link vào — Claude tự cào nội dung, chuyển thành text sạch, phân tích luôn. Không cần biết code scraping.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Scrape bất kỳ website nào → text sạch cho AI đọc và phân tích |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Không |
| **Free hay trả phí** | Free 500 credits/tháng (~500 trang) |
| **GitHub** | [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) ⭐ 6,500+ |

---

## 🎯 Vấn đề nó giải quyết

Mày muốn Claude đọc và tóm tắt một bài báo, blog, hay trang web bất kỳ → nhưng Claude không vào internet được.

**Firecrawl fix cái này:** Nó cào nội dung web → chuyển thành Markdown sạch → đưa thẳng vào context của Claude. Mày chỉ cần nói *"đọc trang này cho tao"*.

**Use cases thực tế:**
- Research đối thủ cạnh tranh — cào web của họ, Claude phân tích luôn
- Tóm tắt bài báo dài — paste link là xong
- Thu thập data từ nhiều trang cùng lúc
- Monitor website thay đổi gì

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Lấy API key free
# Vào firecrawl.dev → Sign up → Copy API key

# Bước 2: Thêm vào claude_desktop_config.json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-PASTE_API_KEY_CỦA_MÀY_VÀO_ĐÂY"
      }
    }
  }
}

# Bước 3: Restart Claude Desktop → Done
```

---

## 💡 Dùng thế nào

```
Prompt ví dụ:

"Cào trang này cho tao: https://competitor.com/pricing
 Tóm tắt họ có mấy gói, giá bao nhiêu, tính năng gì"

→ Claude tự cào → tự phân tích → trả kết quả ngay
```

```
Nâng cao hơn:

"Cào 5 trang blog này [list URLs]
 Tìm tất cả mentions về [chủ đề]
 Tổng hợp thành bảng so sánh"
```

---

## ⚠️ Lưu ý

- Free tier: 500 credits/tháng — 1 trang = 1 credit
- Không cào được trang cần đăng nhập (trả phí mới được)
- Một số trang chặn scraping — không bypass được

---

## 🔗 Hay kết hợp với

- **Sequential Thinking** — plan research trước, Firecrawl thu thập data sau
- **Context7** — Firecrawl cào web thật, Context7 cào docs thư viện

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐⭐ |
| Free tier đủ dùng | ⭐⭐⭐⭐☆ |

**Tóm lại:** Cái này biến Claude thành research assistant thật sự. Paste link → có kết quả. Đơn giản vậy thôi.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/firecrawl/firecrawl-mcp-server*
