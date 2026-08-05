# Digital Marketing Agent — Agentic Specialist

Agent điều phối toàn bộ việc marketing: chiến lược, performance ads, SEO/content,
social, automation/CRM. **Không viết lại skill nào đã có** — package này là lớp
điều phối (orchestrator) ghép các skill/MCP đã có sẵn trong kho lại thành 1 quy
trình dùng được ngay, kèm 1 skill mới (routing logic) mà kho chưa có.

## Spec
- **Domain:** Digital marketing đa kênh (ads, SEO, social, automation, CRM)
- **Job-to-be-done:** Nhận 1 yêu cầu marketing (brand mới cần chiến lược, campaign ads
  cần tối ưu, kênh social cần lịch đăng, lead cần outbound...) → route đúng skill,
  gọi đúng MCP, ra output hành động được ngay
- **Người dùng:** Nobitano (dùng cho ABTRIP, Tano, Wonder Mart, Tano Cafe)
- **Input điển hình:** "lên chiến lược marketing cho Wonder Mart Q3", "Meta Ads CTR
  thấp cho ABTRIP, sửa sao", "audit SEO cho trang ABTRIP", "lên lịch đăng social tuần
  này cho Trùm Sân Bay"
- **Output điển hình:** Chiến lược/kế hoạch có metric đo được, campaign đã audit kèm
  đề xuất cụ thể, content/lịch đăng sẵn sàng publish, báo cáo hiệu suất
- **Mức tự chủ:** Phân tích + đề xuất + tạo nội dung — **hành động ghi/gửi thật** (đăng
  ads, gửi email, publish social) luôn cần confirm trước khi thực thi
- **Rủi ro cao nhất:** Đăng/chi tiền ads mà không confirm, gửi email outbound hàng loạt
  sai đối tượng, đề xuất dựa trên số liệu bịa — guardrail ở `system-prompt.md`

## Capability Map

**Não (skill có sẵn trong kho, không copy vào đây — đọc thẳng từ path gốc):**
| Skill | Path trong kho |
|---|---|
| Persona gốc | `skills/expert-digital-marketing/SKILL.md` |
| Performance ads (9 lệnh) | `skills/claude-ads/` |
| SEO | `skills/claude-seo-commands/SKILL.md`, `skills/ai-seo/SKILL.md`, `skills/seo-plan/SKILL.md` |
| Content & brand voice | `skills/content-strategy/SKILL.md`, `skills/copywriting/SKILL.md`, `skills/brand-voice/SKILL.md` |
| Social | `skills/social-media-stack/SKILL.md`, `skills/social-publisher/SKILL.md`, `skills/crosspost/SKILL.md` |
| Campaign & automation | `skills/marketing-campaign/SKILL.md`, `skills/marketing-automation-mcp-guide/SKILL.md` |
| Research | `skills/competitor-research/SKILL.md`, `skills/market-research/SKILL.md` |
| CRO/funnel | `skills/conversion-ops/SKILL.md`, `skills/click-path-audit/SKILL.md` |
| Outbound B2B | `skills/cold-email/SKILL.md`, `skills/outbound-engine/SKILL.md`, `skills/lead-intelligence/SKILL.md` |
| Affiliate (nếu campaign có) | `skills/affiliate-skills/SKILL.md` |

**Não (skill MỚI, viết trong package này):**
| Skill | Vai trò |
|---|---|
| `skills/digital-marketing-orchestrator/SKILL.md` | Route yêu cầu vào đúng skill ở trên, quyết định thứ tự gọi, gộp output |

**Tay (MCP — xem chi tiết `mcp-setup.md`):** claude-ads, meta-ads-mcp-official,
buffer-mcp, meta-social-api/meta-mcp-server, tiktok-api/tiktok-mcp, mcp-youtube,
youtube-upload, hubspot-mcp, firecrawl/crawl4ai/tavily/brave-search, n8n-workflow-builder-mcp/
make-mcp/zapier, google-workspace-mcp

**Cơ:** Không cần code execution nặng — chủ yếu là research + viết + gọi API, dùng
compute cơ bản để tổng hợp báo cáo/dashboard nếu cần.

## Kiến trúc
```
Input request → Orchestrator (phân loại nhu cầu) → gọi đúng skill chuyên môn
→ [nếu cần data thật] gọi MCP → [nếu là hành động ghi/gửi] CONFIRM với Nobitano
→ Execute → Log kết quả
```
Sơ đồ đầy đủ xem `ARCHITECTURE.md`.

## Cách bung
1. Không cần copy skill nào — Hermes/OpenClaw đọc thẳng từ path gốc trong kho
   (`skills/expert-digital-marketing/`, `skills/claude-ads/`...).
2. Copy riêng `skills/digital-marketing-orchestrator/SKILL.md` (file mới) vào skill
   directory của agent.
3. Setup MCP theo `mcp-setup.md` — phần lớn cần API key/OAuth thật, set env trước.
4. Dán `system-prompt.md` làm project instruction / identity cho agent này.
5. Chạy checklist trong `deploy-checklist.md` trước khi cho agent tự hành động thật
   (đăng ads, gửi email, publish social).

## Việc CHƯA giải quyết
- API key/OAuth thật cho Google Ads, Meta Business, HubSpot, TikTok Business — chưa
  có trong kho, Nobitano cần cung cấp trước khi agent dùng MCP thật.
- Xác nhận n8n có đang chạy trên VPS hay dùng Make cloud — `marketing-automation-mcp-guide`
  giả định có 1 trong 2 cái đã sẵn sàng.
- Ngưỡng auto-approve cho hành động ghi/gửi (đăng ads dưới bao nhiêu tiền thì không
  cần confirm tay) — do Nobitano quyết định, mặc định hiện tại là confirm 100%.
