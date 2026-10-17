# CAPABILITY-MAP — OPC `trum-san-bay-opc`

> Mục kho chọn cho từng khả năng (1 chính + 1 dự phòng). Nhãn do model gắn, chưa mục nào được dùng thật. Thủ kho chọn theo nhãn khả năng, không hiểu ngữ cảnh của OPC: có mục chính hoặc dự phòng lệch việc. Người duyệt phải gạt mục không hợp trước khi lập kế hoạch cài. Công cụ không tự ghi `catalog/GAP-LOG.md`; người dán các dòng HỔNG.

- **Não** (luật, cách nghĩ, skill): `kho:agents/shorts-affiliate-system/skills/compliance-gate`, `kho:skills/natural-writing`, `kho:skills/social-media-skills`, `kho:agents/designer-pro/skills/image-prompt-formula-core`, `kho:stacks/video-factory-auto-router`, `kho:stacks/second-brain-obsidian-claude`, `kho:agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline`, `kho:skills/kpi-dashboard-creator`, `kho:agents/anbinh-travel-ops-analyst/skills/aviation-policy-lookup`
- **Tay** (công cụ làm việc với thế giới ngoài): `kho:repos/tencentdb-agent-memory`, `kho:repos/web-research-mcp`, `kho:repos/coolify`, `kho:repos/twenty-crm`, `kho:repos/billionmail`, `kho:mcps/cloud-accounting-mcps`
- **Cơ** (nơi chạy): Hermes, Python (urllib-only), kênh Telegram
- **HỔNG** (chưa có mục): không

#### `agent-orchestration-memory`

- **Chính:** `kho:repos/tencentdb-agent-memory` (TencentDB Agent Memory (Tencent)), lớp Tay
  - Lý do chọn: Dùng khi cần hệ thống bộ nhớ agent bốn tầng chạy cục bộ trên cơ sở dữ liệu SQLite hỗ trợ tìm kiếm kết hợp
  - Bằng chứng trong entry: Hệ thống bộ nhớ dài hạn 4 tầng cho AI agent, chạy local hoàn toàn (SQLite + sqlite-vec, zero dependency ngoài)
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/tencentdb-agent-memory.md`
- **Dự phòng:** `kho:skills/bo-nao-4-file-claude` (Bộ não 4 file cho Claude (AGENTS.md + context.md + memory.md + Skills)), lớp Não
  - Lý do chọn: Dùng khi cần thiết lập cấu trúc 4 tệp bối cảnh vai trò và bộ nhớ để duy trì cách làm việc nhất quán cho agent
  - Bằng chứng trong entry: dựng cho Claude 4 thứ để nó không phải học lại bối cảnh mỗi lần mở chat mới.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `skills/bo-nao-4-file-claude.md`
- **Cảnh báo:** repos/tencentdb-agent-memory: mới đọc phần đầu entry
- **Cảnh báo:** skills/bo-nao-4-file-claude: mới đọc phần đầu entry

#### `web-research`

- **Chính:** `kho:repos/web-research-mcp` (web-research — Token-Efficient Research MCP (99% Ít Token Hơn)), lớp Tay
  - Lý do chọn: Dùng khi cần MCP server hỗ trợ tìm kiếm và tóm tắt thông tin web tiết kiệm lượng token ngữ cảnh
  - Bằng chứng trong entry: Stack: TinyFish (search) + Groq Llama 3.1 8B (summarize) = cheap + fast + clean.
  - Điều kiện cần: api-key; cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: vua / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/web-research-mcp.md`
- **Dự phòng:** `kho:agents/research-analytics-pro/skills/primary-research-design` (Primary Research Design — Thiết kế khảo sát & phỏng vấn), lớp Não
  - Lý do chọn: Dùng khi cần thiết kế bảng câu hỏi khảo sát hoặc hướng dẫn phỏng vấn để thu thập dữ liệu sơ cấp từ khách hàng
  - Bằng chứng trong entry: Thiết kế nghiên cứu sơ cấp (survey, interview guide) khi không có nguồn thứ cấp nào trả lời được câu hỏi
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/research-analytics-pro/skills/primary-research-design/SKILL.md`
- **Cảnh báo:** repos/web-research-mcp: mới đọc phần đầu entry
- **Cảnh báo:** repos/web-research-mcp: cần khoá API -> L3

#### `devops`

- **Chính:** `kho:repos/coolify` (Coolify), lớp Tay
  - Lý do chọn: Dùng khi cần nền tảng tự lưu trữ để triển khai ứng dụng cơ sở dữ liệu và dịch vụ lên máy chủ riêng
  - Bằng chứng trong entry: Self-hosted PaaS thay thế Vercel, Heroku, Netlify — deploy app, database, service lên VPS riêng chỉ cần một click.
  - Điều kiện cần: vps,docker; cách dùng: can-ha-tang
  - Bỏ qua nếu: Bỏ qua nếu máy chủ ảo có dung lượng bộ nhớ dưới 2GB RAM
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/coolify.md`
- **Dự phòng:** `kho:agents/infra-ops-agent/skills/destructive-command-guardrail` (Destructive Command Guardrail), lớp Não
  - Lý do chọn: Dùng khi cần cảnh báo và gắn cờ các câu lệnh có khả năng gây mất mát dữ liệu hoặc dừng dịch vụ VPS
  - Bằng chứng trong entry: Chặn/flag lệnh có tính phá hủy (xóa data, kill process, đổi firewall, ghi đè quyền)
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/infra-ops-agent/skills/destructive-command-guardrail/SKILL.md`
- **Cảnh báo:** repos/coolify: mới đọc phần đầu entry
- **Cảnh báo:** repos/coolify: cần VPS
- **Cảnh báo:** repos/coolify: cần hạ tầng

#### `security-compliance`

- **Chính:** `kho:agents/shorts-affiliate-system/skills/compliance-gate` (Compliance Gate — Chặn Inauthentic Content trước khi render), lớp Não
  - Lý do chọn: Dùng khi cần kiểm tra script và metadata video trước khi render để ngăn ngừa rủi ro vi phạm chính sách nền tảng
  - Bằng chứng trong entry: Node bắt buộc trong pipeline, đứng giữa Script Variation Engine và MoneyPrinterTurbo.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/shorts-affiliate-system/skills/compliance-gate/SKILL.md`
- **Dự phòng:** `kho:repos/codex-security` (Codex Security (OpenAI)), lớp Tay
  - Lý do chọn: Dùng khi cần kiểm tra an toàn bảo mật quét lỗ hổng và rà soát mã độc trước khi triển khai phần mềm
  - Bằng chứng trong entry: CLI + SDK chính thức của OpenAI để tự động tìm/xác minh/vá lỗ hổng bảo mật trong code
  - Điều kiện cần: api-key; cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu không có khóa API để quét mã nguồn qua mô hình phân tích bảo mật
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/codex-security.md`
- **Cảnh báo:** agents/shorts-affiliate-system/skills/compliance-gate: mới đọc phần đầu entry
- **Cảnh báo:** repos/codex-security: mới đọc phần đầu entry
- **Cảnh báo:** repos/codex-security: cần khoá API -> L3

#### `crm-sales`

- **Chính:** `kho:repos/twenty-crm` (Twenty CRM), lớp Tay
  - Lý do chọn: Dùng khi cần hệ thống quản trị quan hệ khách hàng mã nguồn mở tự lưu trữ với quy trình linh hoạt và giao diện trực quan
  - Bằng chứng trong entry: CRM mã nguồn mở, tự host được, kiểu "Notion/Airtable gặp Salesforce": object tuỳ biến, pipeline kéo-thả
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu đóng gói bán lại dạng dịch vụ đóng mã nguồn do ràng buộc bản quyền AGPLv3 và Enterprise
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/twenty-crm.md`
- **Dự phòng:** `kho:agents/sales-ceo/skills/deal-scoring-forecast-discipline` (Deal Scoring & Forecast Discipline (SMB Việt Nam)), lớp Não
  - Lý do chọn: Dùng khi cần chấm điểm cơ hội bán hàng B2B theo thang điểm khách quan và dự báo doanh thu sát thực tế
  - Bằng chứng trong entry: Dùng khi cần chấm điểm lead mới, lên lịch touch, xử lý objection, forecast pipeline, hoặc audit CRM.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/sales-ceo/skills/deal-scoring-forecast-discipline/SKILL.md`
- **Cảnh báo:** repos/twenty-crm: mới đọc phần đầu entry
- **Cảnh báo:** agents/sales-ceo/skills/deal-scoring-forecast-discipline: mới đọc phần đầu entry

#### `email-outreach`

- **Chính:** `kho:repos/billionmail` (BillionMail), lớp Tay
  - Lý do chọn: Dùng khi cần nền tảng thư điện tử tiếp thị tự vận hành trên máy chủ riêng không tốn phí định kỳ hàng tháng
  - Bằng chứng trong entry: Platform email marketing self-hosted hoàn chỉnh: mail server + newsletter + campaign
  - Điều kiện cần: vps,tra-phi; cách dùng: can-ha-tang
  - Bỏ qua nếu: Bỏ qua nếu chưa có máy chủ ảo VPS và ngân sách duy trì hạ tầng gửi thư riêng
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/billionmail.md`
- **Dự phòng:** không có.
- **Cảnh báo:** repos/billionmail: mới đọc phần đầu entry
- **Cảnh báo:** repos/billionmail: tốn tiền -> L2
- **Cảnh báo:** repos/billionmail: cần VPS
- **Cảnh báo:** repos/billionmail: cần hạ tầng

#### `content-writing`

- **Chính:** `kho:skills/natural-writing` (Natural Writing — Chống văn phong "nghe như AI"), lớp Não
  - Lý do chọn: Dùng khi cần bảng tiêu chí loại bỏ các cấu trúc văn phong rập khuôn sáo rỗng để văn bản tự nhiên hơn
  - Bằng chứng trong entry: Checklist cụ thể để sửa mọi đoạn text (script video, bài .md trong kho, caption, email) khỏi bị "mùi AI"
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `skills/natural-writing.md`
- **Dự phòng:** `kho:skills/content-research-writer` (Content Research Writer — Quy trình viết bài có nguồn kiểm chứng được), lớp Não
  - Lý do chọn: Dùng khi cần quy trình viết bài chuyên sâu từ dữ liệu nghiên cứu có trích dẫn nguồn kiểm chứng rõ ràng.
  - Bằng chứng trong entry: Quy trình viết content (blog, báo cáo, newsletter, case study) từ nghiên cứu có nguồn rõ ràng
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu chỉ cần viết bài đăng ngắn đơn giản không yêu cầu kiểm chứng nguồn tài liệu.
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `skills/content-research-writer.md`
- **Cảnh báo:** skills/natural-writing: mới đọc phần đầu entry

#### `social-media`

- **Chính:** `kho:skills/social-media-skills` (Social Media Skills), lớp Não
  - Lý do chọn: Dùng khi cần bộ kỹ năng toàn diện cho chu trình sáng tạo nội dung mạng xã hội dựa trên phong cách thương hiệu thống nhất
  - Bằng chứng trong entry: Bộ skill mã nguồn mở (charlie947/social-media-skills, mở rộng thành social-media-skills/skills với 106 skill)
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: vua / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `skills/social-media-skills.md`
- **Dự phòng:** `kho:mcps/buffer-mcp` (buffer-mcp — Schedule Social Media Posts Qua Claude (Buffer GraphQL)), lớp Tay
  - Lý do chọn: Dùng khi cần tự động lên lịch và đăng bài viết lên nhiều kênh mạng xã hội như Twitter, LinkedIn, Facebook từ chat hoặc agent.
  - Bằng chứng trong entry: Schedule Social Media Posts Qua Claude (Buffer GraphQL)
  - Điều kiện cần: api-key; cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu không có tài khoản Buffer hoặc không có mã BUFFER_ACCESS_TOKEN.
  - Độ chắc nhãn: vua / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `mcps/buffer-mcp.md`
- **Cảnh báo:** skills/social-media-skills: mới đọc phần đầu entry
- **Cảnh báo:** mcps/buffer-mcp: cần khoá API -> L3

#### `image-generation`

- **Chính:** `kho:agents/designer-pro/skills/image-prompt-formula-core` (Image Prompt Formula (Core — không gắn brand)), lớp Não
  - Lý do chọn: Dùng khi cần công thức 7 phần để viết prompt tạo ảnh không phụ thuộc thương hiệu và tránh lỗi phổ biến
  - Bằng chứng trong entry: 1 công thức duy nhất, dùng được cho mọi brand/dự án — brand không sửa file này, chỉ cung cấp dữ liệu riêng
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/designer-pro/skills/image-prompt-formula-core/SKILL.md`
- **Dự phòng:** `kho:agents/trum-san-bay/skills/image-prompt-engineer` (Image Prompt Engineer — Ảnh Sân Bay), lớp Não
  - Lý do chọn: Dùng khi cần viết câu lệnh (prompt) tạo ảnh thumbnail và bài đăng mạng xã hội theo chuẩn nhận diện thương hiệu.
  - Bằng chứng trong entry: Viết prompt gen ảnh chuẩn cho thumbnail Facebook/Instagram Feed — đúng bối cảnh sân bay Việt Nam
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu yêu cầu tạo video chuyển động hoặc hình ảnh không thuộc chủ đề sân bay du lịch.
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/trum-san-bay/skills/image-prompt-engineer/SKILL.md`

#### `video-render`

- **Chính:** `kho:stacks/video-factory-auto-router` (Video Factory Auto-Router — 1 Topic Vào, Video Ra, Tự Chọn Engine), lớp Não
  - Lý do chọn: Dùng khi cần hệ thống tự động phân loại chủ đề và định tuyến sang công cụ dựng video thích hợp từ dữ liệu đầu vào
  - Bằng chứng trong entry: Biến 2 stack rời (Remotion, Vox Director) thành 1 công thức auto duy nhất.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `stacks/video-factory-auto-router.md`
- **Dự phòng:** `kho:mcps/scrptly` (Scrptly Video Generator), lớp Tay
  - Lý do chọn: Dùng khi cần tạo video AI từ mô tả văn bản kèm ảnh tham chiếu ngữ cảnh và giới hạn ngân sách chi phí.
  - Bằng chứng trong entry: 1 prompt văn bản + ảnh ngữ cảnh tùy chọn ra video chuyên nghiệp, có cơ chế duyệt ngân sách token
  - Điều kiện cần: api-key,tra-phi; cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu không có API key của Scrptly hoặc cần kết quả đồng bộ tức thì không qua polling.
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `mcps/scrptly.md`
- **Cảnh báo:** stacks/video-factory-auto-router: mới đọc phần đầu entry
- **Cảnh báo:** mcps/scrptly: tốn tiền -> L2
- **Cảnh báo:** mcps/scrptly: cần khoá API -> L3

#### `productivity`

- **Chính:** `kho:stacks/second-brain-obsidian-claude` (Second Brain — Obsidian + Claude + Git — Combo Tools theo Use Case), lớp Não
  - Lý do chọn: Dùng khi cần mô hình lưu trữ và tổ chức kiến thức cá nhân lâu dài bằng định dạng Markdown kết hợp trợ lý thông minh
  - Bằng chứng trong entry: Vault Obsidian đóng vai trò "bộ nhớ nháp" trước khi vào kho chính thức.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `stacks/second-brain-obsidian-claude.md`
- **Dự phòng:** `kho:mcps/n8n-workflow-builder-mcp` (mcp-n8n-workflow-builder — Tạo n8n Workflows Bằng Ngôn Ngữ Thường (226⭐)), lớp Tay
  - Lý do chọn: Dùng khi cần xây dựng quản lý và giám sát các luồng tự động hóa n8n bằng ngôn ngữ tự nhiên thông qua trợ lý
  - Bằng chứng trong entry: MCP server để build, manage, monitor n8n workflows **bằng ngôn ngữ tự nhiên qua Claude**.
  - Điều kiện cần: api-key; cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `mcps/n8n-workflow-builder-mcp.md`
- **Cảnh báo:** stacks/second-brain-obsidian-claude: mới đọc phần đầu entry
- **Cảnh báo:** mcps/n8n-workflow-builder-mcp: mới đọc phần đầu entry
- **Cảnh báo:** mcps/n8n-workflow-builder-mcp: cần khoá API -> L3

#### `customer-support`

- **Chính:** `kho:agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline` (Churn Risk & Escalation Discipline), lớp Não
  - Lý do chọn: Dùng khi cần phân loại tín hiệu khách hàng muốn rời bỏ và áp dụng thời gian phản hồi theo cam kết
  - Bằng chứng trong entry: SLA phản hồi theo kênh, FCR, và luật quan trọng nhất: 1 lần phục vụ tệ đã đủ rủi ro rời bỏ, không đợi lặp lại.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline/SKILL.md`
- **Dự phòng:** `kho:repos/chatwoot` (Chatwoot), lớp Tay
  - Lý do chọn: Dùng khi cần nền tảng hỗ trợ khách hàng đa kênh tự lưu trữ để tích hợp vào hệ thống trợ lý chăm sóc
  - Bằng chứng trong entry: Platform cham soc khach hang mo nguon mo — thay the Intercom, Zendesk, Freshdesk.
  - Điều kiện cần: docker,vps; cách dùng: can-ha-tang
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/chatwoot.md`
- **Cảnh báo:** repos/chatwoot: mới đọc phần đầu entry
- **Cảnh báo:** repos/chatwoot: cần VPS
- **Cảnh báo:** repos/chatwoot: cần hạ tầng

#### `data-dashboard`

- **Chính:** `kho:skills/kpi-dashboard-creator` (KPI Dashboard Creator — Build dashboard cho quyết định, không phải trang trí), lớp Não
  - Lý do chọn: Dùng khi cần thiết kế bảng điều khiển chỉ số kinh doanh tập trung vào việc ra quyết định hành động
  - Bằng chứng trong entry: nên làm gì tiếp — thay vì nhồi hết mọi số liệu có sẵn lên màn hình cho đẹp.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: cao / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `skills/kpi-dashboard-creator.md`
- **Dự phòng:** `kho:repos/sc-datav` (sc-datav — Dashboard 3D Trực Quan Hóa Dữ Liệu Kiểu Màn Hình Lớn), lớp Tay
  - Lý do chọn: Dùng khi cần mẫu bảng điều khiển trực quan hóa dữ liệu không gian ba chiều sử dụng thư viện Three.js và Vue
  - Bằng chứng trong entry: Three.js + Vue3 — tạo dashboard "màn hình lớn" 3D cực đẹp như trong phim khoa học viễn tưởng.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: vua / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/sc-datav.md`
- **Cảnh báo:** skills/kpi-dashboard-creator: mới đọc phần đầu entry
- **Cảnh báo:** repos/sc-datav: mới đọc phần đầu entry

#### `finance-accounting`

- **Chính:** `kho:mcps/cloud-accounting-mcps` (Cloud Accounting MCPs — Xero + Wave + FreshBooks + Stripe), lớp Tay
  - Lý do chọn: Dùng khi cần kết nối trợ lý AI với các nền tảng kế toán đám mây như Xero Wave FreshBooks Stripe
  - Bằng chứng trong entry: Kết nối Claude với phần mềm kế toán cloud
  - Điều kiện cần: api-key; cách dùng: can-ha-tang
  - Bỏ qua nếu: catalog chưa ghi; điều này KHÔNG có nghĩa là không có điều kiện loại trừ, phải đọc mục Lưu ý của entry gốc
  - Độ chắc nhãn: thap / da-doc-dau-entry (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `mcps/cloud-accounting-mcps.md`
- **Dự phòng:** `kho:repos/tradingagents` (TradingAgents — Phòng Giao Dịch AI Đa-Agent (86k⭐)), lớp Tay
  - Lý do chọn: Dùng khi cần mô phỏng phòng phân tích tài chính đa agent để đánh giá dữ liệu cổ phiếu và tiền số.
  - Bằng chứng trong entry: Framework đa-agent mô phỏng phòng giao dịch thật
  - Điều kiện cần: api-key; cách dùng: can-ha-tang
  - Bỏ qua nếu: Bỏ qua nếu không có API key tài chính hoặc không muốn trả chi phí gọi nhiều mô hình cùng lúc.
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `repos/tradingagents.md`
- **Cảnh báo:** mcps/cloud-accounting-mcps: mới đọc phần đầu entry
- **Cảnh báo:** mcps/cloud-accounting-mcps: cần khoá API -> L3
- **Cảnh báo:** mcps/cloud-accounting-mcps: cần hạ tầng
- **Cảnh báo:** repos/tradingagents: cần khoá API -> L3
- **Cảnh báo:** repos/tradingagents: cần hạ tầng

#### `ticketing-aviation`

- **Chính:** `kho:agents/anbinh-travel-ops-analyst/skills/aviation-policy-lookup` (Aviation Policy Lookup), lớp Não
  - Lý do chọn: Dùng khi cần tra cứu quy định hàng không, thủ tục sân bay, hành lý hoặc chính sách nhập cảnh
  - Bằng chứng trong entry: Tra cứu quy định hàng không, nhập cảnh, hành lý, an ninh sân bay để trả lời câu hỏi của khách hoặc staff An Bình/ABTRIP.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu cần thay thế hệ thống tra cứu chuẩn Timatic của đại lý vé máy bay
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/anbinh-travel-ops-analyst/skills/aviation-policy-lookup/SKILL.md`
- **Dự phòng:** `kho:agents/anbinh-travel-ops-analyst/skills/source-evaluation` (Source Evaluation), lớp Não
  - Lý do chọn: Dùng khi cần kiểm tra và đánh giá độ tin cậy của nguồn dữ liệu trước khi trích dẫn chính sách và quy định.
  - Bằng chứng trong entry: Chấm độ tin cậy nguồn trước khi dùng bất kỳ thông tin nào để trả lời.
  - Điều kiện cần: không cần gì thêm (needs = none); cách dùng: cai-ngay-duoc
  - Bỏ qua nếu: Bỏ qua nếu câu hỏi thuộc dạng kiến thức phổ thông cố định không có khả năng bị thay đổi chính sách.
  - Độ chắc nhãn: cao / da-doc-entry-goc (nhãn do model gắn, chưa kiểm bằng dùng thật)
  - Đọc entry gốc: `agents/anbinh-travel-ops-analyst/skills/source-evaluation/SKILL.md`
