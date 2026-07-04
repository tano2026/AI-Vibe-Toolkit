# MCP Setup — Sales CEO

## Bắt buộc

### hubspot-mcp (kho: `/mcps/hubspot-mcp.md`)
- 33 tools: Contacts, Companies, Deals, Pipelines, Lists, Marketing Emails, Forms, Workflows.
- Cài: `git clone https://github.com/ZLeventer/hubspot-mcp && cd hubspot-mcp && npm install && npm run build`
- Lấy API key: HubSpot → Settings → Integrations → Private Apps.
- **Mode ban đầu: READ-ONLY.** Chỉ bật scope write sau khi Nobitano test kỹ workflow —
  agent không tự update deal/contact khi chưa confirm.

## Nên bật (đã có sẵn trong kho, tận dụng luôn)

| MCP | Vai trò | File kho |
|---|---|---|
| Firecrawl | Scrape trang đối thủ/landing page để research | `/mcps/firecrawl.md` |
| Brave Search | Search nhanh tin tức/đối thủ | `/mcps/brave-search.md` |
| Context7 | Tránh bịa API khi viết code tự động hóa outbound | `/mcps/context7.md` |

## Optional — nếu scale lên

| MCP | Vai trò |
|---|---|
| Google Workspace MCP (`/mcps/google-workspace-mcp.md`) | Sheets track deal, Docs proposal |
| Playwright (`/mcps/playwright.md`) | Tự động hóa research đối thủ sâu (đăng nhập, scroll) |

## KHÔNG bật ở giai đoạn đầu

- Bất kỳ MCP gửi email thật (Gmail send, outbound send) — để Nobitano/Hermes làm bước gửi
  cuối, agent chỉ soạn nội dung.
- HubSpot write scope — chỉ bật khi đã review output agent 1-2 tuần thấy ổn.
