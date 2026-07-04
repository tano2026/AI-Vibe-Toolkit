# Plugin Integration Notes — Sales CEO

File này ghi rõ những plugin/MCP có sẵn trong Claude (không phải trong kho GitHub, vì
Hermes/OpenClaw không đọc được các plugin này — chỉ Claude session mới dùng được) có
thể nâng cấp Sales CEO. Dùng khi Nobitano trực tiếp làm việc với Sales CEO qua Claude,
không áp dụng khi Hermes/OpenClaw tự chạy trên VPS.

## Vì sao tách riêng file này

Kho GitHub (`agents/sales-ceo/mcp-setup.md`) chỉ liệt kê MCP mà Hermes/OpenClaw/
Antigravity đọc và tự cài trên VPS. Plugin Claude bên dưới KHÔNG nằm trong kho, chỉ
tồn tại trong Claude Platform/claude.ai session — Nobitano tự bật khi cần, không phải
việc của Antigravity.

## Plugin sales — thay thế 1 phần outbound-engine/sales-playbook viết tay

| Plugin | Dùng khi | Thay được skill kho nào |
|---|---|---|
| `sales:forecast` | Forecast quý weighted best/likely/worst | Chưa có trong kho — bổ sung, không trùng |
| `sales:pipeline-review` | Audit hygiene pipeline, deal stuck | Bổ trợ `sales-pipeline` (kho) |
| `sales:competitive-intelligence` | Ra HTML battle card nhanh | Bổ trợ `sales-playbook` (kho) khi cần bản nhanh, không thay thế bản chi tiết viết tay |
| `sales:account-research` + `sales:draft-outreach` | Research + viết outreach cá nhân hóa | Bổ trợ `lead-dossier`/`outbound-engine` (kho) |
| `sales:call-prep` | Prep trước cuộc gọi khách | Chưa có trong kho |
| `sales:call-summary` | Trích action item từ note cuộc gọi | Bổ trợ `revenue-intelligence` (kho) |

## Plugin finance — lấp lỗ hổng tài chính/kế toán

| Plugin | Dùng khi |
|---|---|
| `finance:variance-analysis` | Deal ảnh hưởng P&L thế nào — trước khi ceo-decision-lens ra khuyến nghị |
| `finance:financial-statements` | Cần nhìn P&L/balance sheet toàn cảnh trước khi định giá gói mới |
| `finance:journal-entry`, `finance:reconciliation` | Hiểu sổ sách khi cấu trúc deal có payment terms phức tạp |

## Plugin small-business — bộ ops copilot gần trùng skill mới viết

| Plugin | Trùng/bổ trợ skill nào của sales-ceo |
|---|---|
| `small-business:margin-analyzer` | Mạnh hơn phần tính walk-away point trong `negotiation-deal-structuring` vì pull data thật từ PayPal/QuickBooks — DÙNG PLUGIN NÀY thay tính tay nếu Nobitano có kết nối PayPal/QuickBooks |
| `small-business:price-check` | Bổ trợ bước pricing tier trong `gtm-strategy` |
| `small-business:cash-flow-snapshot` | Input cho `ceo-decision-lens` khi cân nhắc quyết định tốn tiền |
| `small-business:crm-maintenance`, `small-business:lead-triage` | Bổ trợ vận hành pipeline khi HubSpot đã kết nối |
| `small-business:monday-brief`/`friday-brief` | Báo cáo tổng hợp nhanh, không cần agent tự tổng hợp |

## MCP đã connect sẵn trong Claude session (không cần cài thêm)

| MCP | Vai trò cho Sales CEO |
|---|---|
| Similarweb | Traffic/market share đối thủ — nâng cấp `competitor-research`/`market-research` (kho) khi cần data traffic thật, không chỉ web search |
| Gmail | Layer gửi outreach thật — **vẫn giữ guardrail**: Sales CEO chỉ soạn nội dung, Nobitano confirm rồi mới gửi qua Gmail, không tự động gửi |
| Google Drive | Lưu proposal/deal docs sau khi Sales CEO soạn |

## Nguyên tắc khi dùng plugin thay/bổ trợ skill trong kho

1. **Data thật ưu tiên hơn ước lượng tay.** Nếu plugin pull được data thật (VD:
   `margin-analyzer` từ QuickBooks) → dùng plugin, không dùng số ước lượng trong skill
   kho.
2. **Guardrail gửi/ghi vẫn áp dụng cho plugin** — `sales:draft-outreach` chỉ soạn,
   Gmail chỉ gửi sau khi Nobitano confirm, giống nguyên tắc trong `system-prompt.md`.
3. **Không trùng lặp công việc** — nếu đã dùng plugin `finance:variance-analysis` cho
   1 câu hỏi, không cần chạy lại `finance-billing-ops` (kho) cho cùng câu hỏi đó.
4. Plugin không nằm trong kho nên **Hermes/OpenClaw không tự dùng được** — nếu muốn
   automation hóa phần nào của quy trình plugin, phải viết lại thành MCP/script trong
   kho để Hermes đọc, không thể chỉ "bật plugin" cho agent VPS.
