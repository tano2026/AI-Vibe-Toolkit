# Kiến trúc — Digital Marketing Agent

## Sơ đồ điều phối tổng

```
┌──────────────────────────────────────────────────────────────────────┐
│ 1. INPUT — yêu cầu marketing bất kỳ (chiến lược/ads/SEO/social/outbound)│
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 2. ORCHESTRATOR (skills/digital-marketing-orchestrator/SKILL.md)      │
│    Phân loại request → 1 trong 6 nhóm (xem bảng routing bên dưới)    │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
        ┌───────────────┬───────────────┬───────────────┬──────────────┐
        ▼               ▼               ▼               ▼              ▼
   ┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐   ┌──────────┐
   │STRATEGY │    │   ADS    │    │   SEO    │    │  SOCIAL  │   │ OUTBOUND │
   │(brand/  │    │(claude-  │    │(claude-  │    │(social-  │   │(cold-    │
   │ market  │    │ ads/*)   │    │ seo/ai-  │    │ media-   │   │ email/   │
   │ research)│    │          │    │ seo)     │    │ stack)   │   │ outbound)│
   └────┬────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘   └────┬─────┘
        │              │               │               │              │
        ▼              ▼               ▼               ▼              ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 3. Skill chuyên môn thực thi — gọi MCP nếu cần data/hành động thật    │
│    (firecrawl/tavily cho research, meta-ads-mcp cho ads thật...)      │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 4. PHÂN LOẠI OUTPUT                                                   │
│    - Chỉ phân tích/đề xuất (report, audit, chiến lược) → trả kết quả │
│      thẳng, KHÔNG cần confirm                                        │
│    - Hành động GHI/GỬI thật (đăng ads, gửi email, publish social)    │
│      → BẮT BUỘC confirm với Nobitano trước khi thực thi              │
└───────────────────────────────┬──────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 5. EXECUTE (nếu đã confirm) → LOG kết quả                             │
└──────────────────────────────────────────────────────────────────────┘
```

## Bảng routing (Orchestrator dùng để phân loại request)

| Loại request | Route tới skill | Có cần MCP không |
|---|---|---|
| "Lên chiến lược/định vị thương hiệu" | `expert-digital-marketing` + `market-research` + `competitor-research` | Có — firecrawl/tavily để lấy data thị trường thật |
| "Tối ưu/audit ads Google/Meta/TikTok" | `claude-ads/ads-audit`, `ads-budget`, `ads-competitor`, `ads-creative` | Có — MCP ads tương ứng để lấy số liệu thật |
| "Tạo campaign ads mới" | `claude-ads/ads-create` + `ads-google`/`ads-meta`/`ads-tiktok`/`ads-youtube` | Có — **luôn confirm trước khi tạo/chi tiền** |
| "SEO cho website/content" | `claude-seo-commands` + `ai-seo` + `seo-plan` | Có — firecrawl để crawl site thật |
| "Viết content/copy" | `content-strategy` + `copywriting` + `brand-voice` | Không bắt buộc |
| "Lịch đăng/publish social" | `social-media-stack` + `social-publisher` + `crosspost` | Có — buffer-mcp/meta-social-api/tiktok-mcp, **confirm trước khi publish thật** |
| "Campaign automation/email" | `marketing-campaign` + `marketing-automation-mcp-guide` | Có — n8n-workflow-builder-mcp/make-mcp |
| "Funnel/conversion không tốt" | `conversion-ops` + `click-path-audit` | Có — google-workspace-mcp (GA4 data) |
| "Outbound B2B (hợp ABTRIP)" | `cold-email` + `outbound-engine` + `lead-intelligence` + `hubspot-mcp` | Có — **confirm trước khi gửi hàng loạt** |
| "Campaign có affiliate" | `affiliate-skills` (đã dùng ở shorts-affiliate-system) | Có |

## Nguyên tắc điều phối

1. **1 request có thể cần nhiều skill** — vd "audit CTR thấp Meta Ads" cần cả
   `ads-audit` (chẩn đoán) lẫn `ads-creative` (đề xuất creative mới), Orchestrator
   gọi tuần tự, không dừng ở skill đầu tiên nếu request cần nhiều góc.
2. **Phân tích/đề xuất không cần confirm, hành động ghi/gửi luôn cần confirm** —
   ranh giới này là cứng, không du di theo mức độ "tự tin" của agent.
3. **Không bịa số liệu khi không có MCP data thật** — nếu MCP chưa setup (thiếu
   API key), agent phải nói rõ "chưa có data thật, đây là ước tính" thay vì trả lời
   như đã verify.
