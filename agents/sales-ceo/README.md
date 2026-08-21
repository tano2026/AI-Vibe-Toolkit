# Sales CEO — B2B Sales & Business Strategy Agent

Agent trùm sales B2B: vừa có tư duy CEO (chiến lược, tài chính, rủi ro, pháp lý)
vừa có tay nghề sales xuất sắc (playbook, pipeline, outbound, negotiation),
vừa biết xây hệ thống (pipeline automation, CRM ops) và thực thi (proposal, forecast, deal review).

## Spec

- **Domain:** B2B Sales Strategy + Execution + Business Operations
- **Job-to-be-done:** Nhận 1 bài toán sales/kinh doanh → ra quyết định + kế hoạch thực thi +
  tài liệu bán hàng, có tư duy CEO (rủi ro, tài chính, pháp lý) không chỉ closer thuần
- **Người dùng:** Nobitano (chủ agency, ra lệnh trực tiếp hoặc qua Hermes/OpenClaw)
- **Input điển hình:**
  - "Xây pipeline outbound cho ABTRIP"
  - "Đối thủ X vừa giảm giá, phản ứng sao"
  - "Deal này có nên giảm giá không"
  - "Viết battle card cho Wonder Mart vs đối thủ Y"
  - "Định giá gói dịch vụ mới cho SMB"
  - "Forecast quý này, có đạt target không"
- **Output điển hình:** Playbook/battle card, pipeline automation config, deal recommendation
  kèm rủi ro tài chính, báo cáo market/competitor có trích nguồn, proposal, forecast
- **Mức tự chủ:** Tra cứu + Phân tích + Soạn tài liệu. KHÔNG tự gửi email/tự chốt deal/tự
  update CRM ghi — mọi hành động ghi/gửi phải qua confirm của Nobitano.
- **Rủi ro cao nhất:** Ra quyết định giảm giá/pháp lý/tài chính sai → **guardrail**: mọi
  quyết định tiền/pháp lý phải kèm rủi ro + số liệu cụ thể, không tự thực thi hành động ghi/gửi.

## Capability Map

**Não (Skills):**
| Skill | Vai trò |
|---|---|
| `sales-playbook` (kho có sẵn) | battle card, xử lý objection, script |
| `revenue-intelligence` (kho có sẵn) | phân tích call, trích buying signal |
| `market-research` (kho có sẵn) | market sizing, có trích nguồn |
| `competitor-research` (kho có sẵn) | so sánh đối thủ có cấu trúc |
| `business-guru` (kho có sẵn) | chiến lược tổng, lens CEO |
| `finance-billing-ops` (kho có sẵn) | định giá, rủi ro tiền, evidence-first |
| `council` (kho có sẵn) | quyết định go/no-go mơ hồ, tranh luận 4 voice |
| `negotiation-deal-structuring` (mới viết) | cấu trúc deal, concession ladder, BATNA |
| `ceo-decision-lens` (mới viết) | khung quyết định CEO: risk/return/reversibility |
| `gtm-strategy` (mới viết) | go-to-market cho SMB VN, pricing tier, channel |
| `deal-scoring-forecast-discipline` (mới viết) | vận hành hoá luật scoring/cadence/objection/pricing/forecast/CRM từ EXPERT-CORE.md ③ |

**Tay (MCP/Tools):**
| Tool | Vai trò |
|---|---|
| `hubspot-mcp` (kho có sẵn, 33 tools) | CRM đọc/ghi contacts/deals/pipelines |
| `outbound-engine` + `cold-email` (kho có sẵn) | outreach sequence, personalization |
| `lead-dossier` + `lead-intelligence` (kho có sẵn) | research account, chấm điểm lead |
| Firecrawl/web search (kho có sẵn) | research đối thủ, thị trường |

**Cơ (Compute):**
| Việc | Trang bị |
|---|---|
| Phân tích pipeline/deal data | Code execution (pandas) |
| Forecast, báo cáo | xlsx |
| Proposal, playbook in ấn | docx |

## Kiến trúc

Xem `ARCHITECTURE.md`.

## Cách bung

1. Copy `skills/*` vào skills directory của agent runtime (Hermes/OpenClaw).
2. Bật MCP theo `mcp-setup.md` (hubspot-mcp là bắt buộc, còn lại optional).
3. Dán `system-prompt.md` làm system/project instruction cho agent này.
4. Chạy test case trong `deploy-checklist.md` trước khi giao việc thật.
5. Guardrail bắt buộc: KHÔNG cho agent tool ghi/gửi (Gmail send, HubSpot write) tới khi
   Nobitano confirm workflow ổn — bật read-only trước.
