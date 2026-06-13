# last30days — AI Tìm Signal Từ Người Thật, Không Phải Google Biên Tập

> 34k stars, #1 GitHub Trending. Slash command cho Claude Code: `/last30days [topic]` → AI search Reddit, X, YouTube, HackerNews, Polymarket cùng lúc → tổng hợp signal thật từ người dùng thật.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) ⭐ 34,000+ |
| **Tác giả** | Matt Van Horn |
| **Version** | v3.3.0 (June 2026) |
| **Search trên** | Reddit, X, YouTube, HN, TikTok, GitHub, Polymarket, Bluesky |
| **Free** | ✅ MIT (một số platforms cần API key) |

---

## 🎯 Vấn đề nó giải quyết

**Google** → kết quả từ biên tập viên, SEO, ads
**ChatGPT** → không search được X, Reddit bị giới hạn
**Claude** → knowledge cutoff, không có social signals

**last30days fix:** Search 10+ platforms song song, rank theo engagement thật (upvotes, comments, likes) → mày thấy được **người thật đang nói gì** về bất kỳ chủ đề nào trong 30 ngày qua.

---

## ⚡ Cài và dùng

```bash
# Cài skill
npx skills@latest add mvanhorn/last30days-skill

# Trong Claude Code, dùng:
/last30days MCP servers đang trending

/last30days vibe coding tools tốt nhất hiện tại

/last30days OpenClaw vs n8n-claw so sánh thực tế
```

---

## 💡 Use cases thực tế cho kênh

```
/last30days "top AI tools vibe coders đang dùng tháng này"
→ Reddit threads, X posts, YouTube comments
→ Tools nào được khen nhiều nhất
→ Pain points nào hay gặp nhất
→ Tao lấy đó làm content ideas

/last30days "Context7 MCP review"
→ Xem người dùng thật nói gì về tool tao vừa review
→ Có điểm nào tao bỏ sót không
```

---

## 📊 Sources nó search

| Platform | Lấy gì |
|----------|--------|
| Reddit | Discussions, upvotes, comments |
| X/Twitter | Posts từ high-signal accounts |
| YouTube | Comments, views |
| Hacker News | Technical discussions |
| Polymarket | Prediction markets (real money signals) |
| GitHub | Stars, issues, discussions |
| TikTok/Instagram | Social signals |
| Web | Blogs, articles |

---

## ⚠️ Lưu ý

- Cần **Claude Code** để dùng slash command
- Một số platforms (X, Polymarket) cần API key riêng
- v3 engine: 1,012 tests passing — khá stable

---

## 🔗 Hay kết hợp với

- **Auto Research Trending skill** trong kho — last30days là data source cực tốt
- **Firecrawl** — last30days tìm links → Firecrawl đọc nội dung chi tiết
- **Content Creator skill** — research xong → tạo content ngay

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Unique value | ⭐⭐⭐⭐⭐ |
| Dễ dùng | ⭐⭐⭐⭐☆ |
| Phù hợp research content | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Đây chính xác là tool tao cần để tự động research trending cho kênh. Google không có, ChatGPT không có — chỉ last30days mới tổng hợp được signal thật từ cộng đồng.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/mvanhorn/last30days-skill*
