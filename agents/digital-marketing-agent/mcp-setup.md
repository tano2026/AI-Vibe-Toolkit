# MCP Setup — Digital Marketing Agent

Toàn bộ MCP dưới đây đã có file mô tả trong kho (`/mcps/`). File này chỉ tổng hợp
việc cần làm để wiring thật cho agent digital marketing, không lặp lại nội dung
từng MCP (đọc trực tiếp file gốc nếu cần chi tiết).

## Bắt buộc setup trước khi dùng tính năng ads/CRM thật

| MCP | Path trong kho | Env cần | Dùng cho |
|---|---|---|---|
| Claude Ads | `mcps/claude-ads.md` | Google Ads API key, Meta Business token | `claude-ads/*` skill |
| Meta Ads Official | `mcps/meta-ads-mcp-official.md` | Meta Business API token | Audit/tạo campaign Meta thật |
| HubSpot | `mcps/hubspot-mcp.md` | `HUBSPOT_API_KEY` | Outbound, lead tracking |
| Buffer | `mcps/buffer-mcp.md` | Buffer API key | Schedule social đa nền tảng |
| Meta Social API | `mcps/meta-social-api.md` / `mcps/meta-mcp-server.md` | Meta token | Publish FB/IG trực tiếp |
| TikTok | `mcps/tiktok-api.md` / `mcps/tiktok-mcp.md` | TikTok Business token | Ads + publish TikTok |
| YouTube | `mcps/mcp-youtube.md` / `mcps/youtube-upload.md` | `GITHUB` không liên quan — cần Google OAuth | Ads YouTube + upload video |
| Google Workspace | `mcps/google-workspace-mcp.md` | Google OAuth | GA4 data, Sheets báo cáo, Gmail outbound |

## Không bắt buộc key riêng (dùng ngay được)

| MCP | Dùng cho |
|---|---|
| `mcps/firecrawl.md`, `mcps/crawl4ai.md` | Crawl website đối thủ/thị trường cho research |
| `mcps/tavily-mcp.md`, `mcps/brave-search.md` | Web search cho trend/chính sách ads mới |

## Automation glue — chọn 1 trong các option sau

| Option | Path | Ghi chú |
|---|---|---|
| n8n | `mcps/n8n-workflow-builder-mcp.md` | Nếu đã có n8n chạy trên VPS Tencent Cloud |
| Make | `mcps/make-mcp.md` | Nếu dùng Make cloud thay vì tự host |
| Zapier | `mcps/zapier.md` | Phương án thứ 3, ít khuyến nghị hơn vì đắt hơn ở scale |

**Cần xác nhận với Nobitano:** hiện đang dùng option nào trong 3 cái trên, hay chưa
có cái nào — `marketing-automation-mcp-guide` giả định đã có 1 cái sẵn sàng.

## Checklist trước khi bật hành động thật

```bash
# Kiểm tra từng MCP đã connect chưa (chạy trong OpenClaw/Hermes)
echo "Kiểm tra kết nối MCP marketing..."
# Test call nhẹ tới từng MCP, verify trả về không lỗi auth trước khi cho agent
# tự động gọi trong luồng thật
```

Không bật auto-publish/auto-send khi chưa test connection thật — nếu MCP báo lỗi
auth giữa luồng, agent phải dừng và báo Nobitano, không thử lại vô hạn.
