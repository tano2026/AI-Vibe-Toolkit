---
name: agentic-factory
description: >
  Nhà sản xuất agentic — đưa vào MỘT ý tưởng về agent cần xây ("tao cần 1 agent chuyên về X"),
  trả ra trọn bộ sản phẩm đóng gói: bộ skill files, danh sách MCP/tools, kiến trúc orchestrator,
  file cấu hình project, và checklist deploy. Bung được ra dùng luôn.
  Dùng skill này khi user nói: "xây 1 agent về...", "tao cần 1 agentic chuyên...", "đóng gói agent...",
  "sản xuất agent...", "build cho tao 1 con AI làm...", "factory agent...", "tạo bộ skill cho agent...".
  Trigger mạnh với: "agent", "agentic", "chuyên gia AI", "đóng gói", "bộ skill", "factory", kèm bất kỳ
  mô tả chuyên ngành/công việc nào (research, sales, legal, kế toán, tuyển dụng, vận hành, v.v.).
---

# Agentic Factory — Nhà sản xuất Agentic

Input: một ý tưởng. Output: một bộ sản phẩm agent hoàn chỉnh, đóng gói, deploy được.

Nguyên tắc: KHÔNG hỏi lan man. Đọc ý tưởng → tự suy ra mọi thứ còn thiếu → ra sản phẩm. Chỉ hỏi
lại tối đa 1 câu nếu domain mơ hồ tới mức không chọn được hướng.

---

## Quy trình 5 bước (chạy tuần tự, không bỏ bước)

### Bước 1 — Spec the Agent (Đặc tả)

Từ ý tưởng của user, điền BẢNG SPEC này. Tự suy luận chỗ thiếu, đừng bắt user khai báo:

```
Tên agent:        [đặt tên ngắn, snake_case + tên hiển thị]
Domain:           [chuyên ngành cốt lõi]
Job-to-be-done:   [1 câu: agent này tồn tại để làm gì]
Người dùng:       [ai sẽ ra lệnh cho nó]
Input điển hình:  [3-5 loại yêu cầu nó sẽ nhận]
Output điển hình: [agent giao ra cái gì — report? file? quyết định? data?]
Mức tự chủ:       [tra cứu / phân tích / hành động (gọi API, ghi data)]
Rủi ro cao nhất:  [chỗ agent dễ sai/gây hại nhất → quyết định guardrail]
```

### Bước 2 — Derive the Capability Map (Suy ra năng lực)

Map job-to-be-done sang 3 tầng năng lực. MỌI agent đều cần đủ 3 tầng, nếu thiếu tầng nào là agent què:

```
TẦNG NÃO (Skills):     tư duy nghiệp vụ — cách agent suy nghĩ, đánh giá, quyết định
TẦNG TAY (MCP/Tools):  nguồn data + khả năng hành động ra thế giới ngoài
TẦNG CƠ (Compute):     xử lý thật — code execution, file creation, tính toán
```

Quy tắc chọn cho mỗi tầng ở phần THƯ VIỆN bên dưới.

### Bước 3 — Generate the Package (Sinh sản phẩm)

Đẻ ra trọn bộ file vào thư mục `<tên-agent>/`:

```
<tên-agent>/
├── README.md              ← spec + kiến trúc + hướng dẫn bung
├── ARCHITECTURE.md        ← sơ đồ orchestrator + luồng dữ liệu
├── skills/
│   ├── <skill-1>/SKILL.md ← mỗi năng lực não = 1 skill file đầy đủ
│   ├── <skill-2>/SKILL.md
│   └── ...
├── mcp-setup.md           ← danh sách MCP/connector + lý do + cách bật
├── system-prompt.md       ← prompt gốc định danh + nguyên tắc + guardrail
└── deploy-checklist.md    ← các bước bung ra môi trường thật
```

VIẾT THẬT nội dung từng file — không để placeholder "TODO". Mỗi SKILL.md phải có
trigger tiếng Việt, quy trình rõ ràng, ví dụ cụ thể.

### Bước 4 — Wire the Architecture (Đấu kiến trúc)

Mặc định mọi agent dùng mô hình **Orchestrator + Sub-agents**:

```
<Domain> Orchestrator (điều phối, quyết định gọi sub-agent nào)
├── Collector   — thu thập raw (web search, MCP, file đọc)
├── Validator   — lọc nguồn, chấm độ tin cậy, flag mâu thuẫn
├── Processor   — xử lý thật (code, tính toán, transform)
└── Synthesizer — ra output cuối (insight + recommendation + deliverable)
```

Với agent đơn giản (chỉ tra cứu) có thể gộp còn Collector→Synthesizer.
Với agent hành động (ghi data, gọi API) BẮT BUỘC giữ Validator + thêm tầng confirm.

### Bước 5 — Guardrail + Deploy

Mỗi agent ra lò phải kèm:
- **Guardrail** đúng theo "Rủi ro cao nhất" ở Bước 1 (vd: agent kế toán không tự chuyển tiền;
  agent research phải trích nguồn; agent sales không spam).
- **Deploy checklist**: bật MCP nào, set env nào, test case gì trước khi giao việc thật.

---

## THƯ VIỆN năng lực (chọn theo domain)

### Tầng Não — Skill bank (mix & match theo job)

| Nếu agent cần... | Trang bị skill |
|---|---|
| Nghiên cứu/tổng hợp | `research-synthesis`, `source-evaluation`, `market-sizing` |
| Phân tích số liệu | `data-cleaning`, `statistical-analysis`, `data-storytelling` |
| Cạnh tranh/thị trường | `competitive-intel`, `trend-forecasting` |
| Viết/nội dung | `copywriting`, `brand-voice`, `content-strategy` |
| Bán hàng | `account-research`, `outreach-drafting`, `objection-handling` |
| Vận hành/quy trình | `sop-builder`, `task-decomposition`, `checklist-runner` |
| Pháp lý/tuân thủ | `compliance-check`, `clause-review`, `risk-flagging` |
| Quyết định | `decision-framework`, `tradeoff-analysis` |

Skill nền BẮT BUỘC cho mọi research-type agent: `source-evaluation` (để agent không tin
mù mọi thứ search trả về) + `data-storytelling` (để ra "so what" chứ không dump data).

### Tầng Tay — MCP/Tool bank (chọn theo nguồn data agent cần)

| Loại data/hành động | MCP/Tool |
|---|---|
| Web sạch cho agent | Tavily, Exa, Firecrawl (scrape có cấu trúc) |
| Web traffic/market share | Similarweb |
| Dataset công khai | DataHub, Hugging Face |
| Tài chính công ty | Financial Modeling Prep, Alpha Vantage, SEC EDGAR |
| Lưu trữ/cộng tác | Google Drive/Sheets, Notion, Airtable |
| CRM/sales | HubSpot, Salesforce connector |
| Giao tiếp ra ngoài | Gmail, Slack (chỉ khi agent được phép hành động) |

Quy tắc: agent CHỈ TRA CỨU thì không cần connector ghi/gửi. Agent HÀNH ĐỘNG mới bật
Gmail/Slack/CRM-write, và phải kèm tầng confirm trong kiến trúc.

### Tầng Cơ — Compute bank (gần như luôn cần)

| Việc | Trang bị |
|---|---|
| Phân tích data thật | Code execution + pandas, numpy, scipy, statsmodels, scikit-learn |
| Biểu đồ | matplotlib, plotly, hoặc xuất Chart.js/D3 |
| Deliverable file | skill `xlsx`, `pdf`, `docx`, `pptx` |

Không có code execution = agent chỉ "kể chuyện về data" chứ không phân tích được. Với mọi
agent dính tới số, BẮT BUỘC bật tầng này.

---

## Output format khi chạy factory

1. In ra BẢNG SPEC (Bước 1) để user xác nhận hướng — gọn, không hỏi lại trừ khi mơ hồ.
2. In CAPABILITY MAP (Bước 2): liệt kê skill + MCP + compute đã chọn, kèm lý do 1 dòng mỗi cái.
3. Sinh trọn bộ file (Bước 3) — tạo thật bằng create_file, đặt trong `<tên-agent>/`.
4. Vẽ sơ đồ kiến trúc (Bước 4).
5. Present files + 3 bước tiếp theo để bung.

Phong cách: đi thẳng, một khuyến nghị rõ ràng cho mỗi lựa chọn (không liệt kê 5 option bắt
user tự chọn). Nếu một MCP chưa có sẵn, nói rõ user cần bật ở đâu.
