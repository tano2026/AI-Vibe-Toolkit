# Playwright MCP — Cho AI Xem Và Điều Khiển Browser

> Thay vì mày test web bằng tay, cài cái này vào — Claude tự mở browser, click, check kết quả, báo lại cho mày.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | AI tự điều khiển browser để test UI, scrape web, tự động hóa thao tác |
| **Độ khó setup** | ⭐⭐⭐☆☆ Trung bình |
| **Cần biết code không** | Biết tí (hiểu khái niệm DOM là đủ) |
| **Free hay trả phí** | Free hoàn toàn |
| **GitHub** | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — by Microsoft |

---

## 🎯 Vấn đề nó giải quyết

Mày build xong landing page, muốn test xem button có hoạt động không → phải mở browser, click tay, check từng thứ. Tốn thời gian.

**Playwright MCP fix cái này:** Claude tự mở browser thật, tự navigate, tự click, tự báo cáo *"button này bị lỗi vì..."* → mày ngồi nhìn thôi.

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Thêm vào claude_desktop_config.json:
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}

# Bước 2: Restart Claude Desktop

# Bước 3: Test thử — bảo Claude:
# "Mở localhost:3000 và check xem form login có hoạt động không"
```

---

## 💡 Dùng thế nào

```
Prompt ví dụ:

"Vào localhost:3000, đăng nhập với email test@test.com 
 password 123456, check xem có vào được dashboard không.
 Nếu lỗi thì báo lỗi gì."

→ Claude tự làm hết, báo kết quả lại cho mày
```

**Use cases thực tế:**
- Test form submit có hoạt động không
- Check responsive trên mobile size
- Tự động điền form lặp đi lặp lại
- Scrape data từ web không có API

---

## ⚠️ Lưu ý

- Lần đầu cần download Chromium (~150MB)
- Chạy chậm hơn test bằng tay (nhưng mày không cần làm gì)
- Không bypass được Captcha hay Cloudflare chặt

---

## 🔗 Hay kết hợp với

- **Sequential Thinking** — plan test cases trước, Playwright thực thi sau
- **GitHub MCP** — phát hiện bug → tạo issue ngay trên GitHub

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐☆☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐⭐ |
| Wow factor | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Nhìn AI tự điều khiển browser lần đầu là thấy magic. Cực kỳ hữu ích cho vibe coders không muốn test bằng tay.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/microsoft/playwright-mcp*
