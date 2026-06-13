# Script Video #25 — Playwright MCP: Claude Tự Test Web Cho Mày

**Format:** TikTok / YouTube Shorts (~75s)
**Hook type:** "Không cần test tay nữa"
**Style:** Không lộ mặt, demo browser tự chạy

---

## 🎬 SCRIPT

**[0s - 7s] HOOK**
> "Build xong landing page, mày phải ngồi click tay từng button để test. Cài MCP này vào — Claude tự mở browser, tự click, tự báo cái nào broken."

*[Show: browser tự navigate không có bàn tay người]*

**[7s - 20s] PLAYWRIGHT MCP LÀ GÌ**
> "Playwright MCP — by Microsoft, free. Nó cho Claude quyền điều khiển browser thật — không phải headless, browser thật mày thấy được."

> "Khác browser-use ở chỗ: Playwright MCP là tool cho developer kiểm soát chính xác. browser-use là cho AI tự quyết làm gì."

**[20s - 50s] DEMO 3 USE CASES**
> "Use case 1 — Test UI tự động:"

*[Show Claude nhận lệnh → browser mở → click form → submit → report]*

> "'Test form đăng ký, điền dữ liệu test, báo nếu có lỗi' — Claude làm hết."

> "Use case 2 — Scrape web có JavaScript:"
> "Website dùng React, lazy load — fetch thường không lấy được data. Playwright render xong mới lấy."

> "Use case 3 — Screenshot so sánh:"
> "'Chụp màn hình trang này trên mobile và desktop, so sánh layout' — 10 giây."

**[50s - 65s] CÀI**
```bash
npx @playwright/mcp@latest
```
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**[65s - 75s] CTA**
> "Microsoft build cái này để dùng nội bộ rồi open source. Cài 1 lệnh, Claude biết test web ngay."

---

## 📝 CAPTION
```
Test web bằng tay mãi à? Claude tự làm được rồi 🖥️

Playwright MCP — Claude tự mở browser, click, test UI, scrape JS sites, chụp screenshot

Free · By Microsoft · 1 lệnh cài

#playwright #testing #vibecoding #claudeai #mcp #webdev #automation
```

## 🎯 B-ROLL
1. **Hero shot:** Browser tự navigate không có tay người
2. Claude nhận text prompt → browser action xảy ra real-time
3. Screenshot comparison mobile vs desktop
4. Terminal: `npx @playwright/mcp@latest`

---
*Script v1 — tháng 6/2026*
