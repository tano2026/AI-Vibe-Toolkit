# OpenSEO — GitHub Repo

## TL;DR
Alternative mã nguồn mở của Semrush và Ahrefs — kết nối được với Claude Code, Hermes, OpenClaw. Pay-as-you-go, không tốn $100+/tháng subscription. 2.5K stars và growing.

## Repo này dùng để làm gì
SEO tools xịn (Semrush, Ahrefs) quá đắt cho vibe coder và indie maker. OpenSEO giải quyết bằng cách:
- Keyword research: tìm từ khóa, volume, difficulty
- Backlink analysis: check ai đang link về site mày
- Site audit: crawl và báo lỗi SEO
- Google Search Console MCP: kết nối thẳng data thật từ GSC

Quan trọng: có pre-built skills tương thích với Claude Code, OpenClaw, Hermes — AI agent của mày có thể dùng trực tiếp.

## Setup từng bước
```bash
# 1. Clone repo
git clone https://github.com/every-app/open-seo
cd open-seo

# 2. Install
npm install

# 3. Config API (pay-as-you-go — không phải subscription)
cp .env.example .env
# Thêm API key DataForSEO hoặc similar provider

# 4. Chạy audit site
npm run audit -- --url https://yoursite.com

# 5. Keyword research
npm run keywords -- --seed "vibe coding" --country VN

# 6. Kết nối Google Search Console
# Thêm MCP config vào Claude Code project
```

**Kết nối với Claude Code:**
```json
{
  "mcpServers": {
    "open-seo": {
      "command": "npx",
      "args": ["open-seo-mcp"]
    }
  }
}
```

## Ví dụ thực tế
**Prompt với Claude Code sau khi bật OpenSEO MCP:**
"Audit SEO site abtrip.vn và cho tao biết 5 vấn đề nghiêm trọng nhất"

**Output:**
- Missing meta description: 23 trang
- Duplicate title tags: 8 trang
- Broken internal links: 12 link
- Page speed issues: LCP > 4s trên mobile
- Missing alt text: 67 ảnh

## Lưu ý / Lỗi thường gặp
- Cần API key từ data provider (DataForSEO khuyến nghị — giá theo usage, không phải subscription cố định)
- GSC MCP cần Google OAuth setup — phức tạp hơn một chút lần đầu
- Không có UI đẹp như Semrush — tool này cho developer/AI agent, không phải cho marketer không code
- Backlink data ít hơn Ahrefs (database nhỏ hơn)

## Đánh giá cá nhân
- Điểm mạnh: Miễn phí base, pay-as-you-go; tích hợp native với AI agent; mã nguồn mở tự customize
- Điểm yếu: Database nhỏ hơn Semrush/Ahrefs; cần code để dùng tốt; không phải cho marketer truyền thống
- Có nên dùng không: **8/10** — Perfect cho vibe coder làm SEO tích hợp AI agent. Không thay thế hoàn toàn Ahrefs nhưng cho use case AI-driven SEO thì đỉnh.

## Link
- Repo: https://github.com/every-app/open-seo
- Topics: seo, mcp, keyword-research, backlink-analysis, google-search-console-mcp
