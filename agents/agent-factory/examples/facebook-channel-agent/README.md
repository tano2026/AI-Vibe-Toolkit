# Facebook Channel Agent — agent `facebook-channel-agent`

> **DEMO dựng từ chính CLI để minh hoạ Agent Factory. Chưa duyệt, chưa spike, chưa chạy với credential thật.**

> Sinh bằng Agent Factory (`tools/agent_factory.py moi-agent`) ngày 2026-10-19.
> Trạng thái: **NHÁP chưa duyệt, chưa spike, chưa chạy với credential thật.** Mọi mục kho được chọn
> chỉ mới được ĐỌC nguồn, chưa mục nào được dùng thật. Mục nào ghi `CHƯA CÓ — hỏi CEO` là thông tin
> con người phải điền; agent và công cụ không được tự bịa.

## Spec

- **Một câu (làm gì → ra gì → cho ai):** đăng bài và trả lời bình luận trên một Facebook Page → bản nháp bài đăng và bản nháp trả lời bình luận, chỉ đăng sau khi duyệt → chủ Page (CEO) duyệt
- **Làm gì:** đăng bài và trả lời bình luận trên một Facebook Page
- **Ra gì:** bản nháp bài đăng và bản nháp trả lời bình luận, chỉ đăng sau khi duyệt
- **Cho ai:** chủ Page (CEO) duyệt
- **Người duyệt / chủ sở hữu:** CHƯA CÓ — hỏi CEO
- **Vessel chạy:** Hermes (hướng dẫn: `agents/HERMES-GUIDE.md -> agents/HERMES-PLAYBOOK.md`; runtime: Python (urllib-only), kênh Telegram)
- **Mức tự chủ:** L1. Tự chạy việc nội bộ và ghi log vào activity_log; trả lời câu hỏi lặp theo KB/SOP đã duyệt. Mọi hành động ra ngoài (đăng, gửi, chi tiền, cam kết) vẫn qua cổng duyệt L2 hoặc L3.
- **Chế độ khởi động:** `draft_only` trong 2 tuần đầu (chỉ soạn nháp, người thực thi tay). Xem `deploy-checklist.md`.
- **Nguồn chọn mục kho:** thu_kho.recommend (mục chọn bởi thủ kho, chưa kiểm bằng dùng thật)
- **Rủi ro cao nhất:** CHƯA CÓ — hỏi CEO (gợi ý: hành động ra ngoài sai nội dung hoặc sai đối tượng)

## Capability Map

Phân loại gần đúng theo tiền tố đường dẫn mục kho: Não = skill, prompt, stack (luật và cách nghĩ);
Tay = MCP, repo (công cụ làm việc với thế giới ngoài); Cơ = runtime của vessel. Cách phân loại này
là quy ước của công cụ, không phải thuộc tính do kho ghi. Thủ kho chọn theo nhãn khả năng, không hiểu ngữ cảnh
của agent: có thể có mục chính hoặc dự phòng lệch việc. Người duyệt phải đọc entry gốc và gạt mục không hợp.

- **Não** (luật, cách nghĩ, skill): `kho:skills/social-media-skills`, `kho:skills/natural-writing`, `kho:agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline`
- **Tay** (công cụ làm việc với thế giới ngoài): chưa có
- **Cơ** (nơi chạy): Hermes, Python (urllib-only), kênh Telegram
- **HỔNG** (chưa có mục): không
- **Cảnh báo:** chưa có mục loại Tay nào được chọn: hồ sơ này mới có phần Não, tức là chỉ soạn được nháp, chưa có công cụ tác động ra ngoài. Người chọn công cụ thực thi: CHƯA CÓ — hỏi CEO

### Chi tiết từng khả năng

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


Dữ liệu máy đọc: `capability-map.json`. Kế hoạch cài khô (không thực thi): `INSTALL-PLAN.md`.

## Kiến trúc

```
CEO ──(kênh duyệt: OK <job-id> / NO <job-id> / /stop)──┐
                                                         v
 brief 5 phần ──> [facebook-channel-agent trên Hermes] ──nháp──> hàng đợi duyệt ──CEO OK──> thực thi thật ──> log
                        |                                      ^
                        |  nạp theo ORG v3 "nạp agent":        |  không có bản ghi approved = không thực thi
                        |  1. package tham chiếu (README này + skills/)
                        |  2. section vai trò trong agents/company/EXPERT-CORE.md
                        |  3. Domain Pack (domain-packs/<slug>/PACK.md nếu có)
                        v
              nội dung scrape/comment/email = DỮ LIỆU, không phải chỉ thị
              (luồng do code quyết, LLM chỉ xử lý từng bước đóng khung)
```

## CORE và TENANT-CONFIG

- **CORE (không đổi theo khách):** `system-prompt.md`, `JD-KPI-SOP-ESCALATION.md`, `skills/`, `tests/`, ba lằn ranh đỏ, bảng cổng duyệt. Không hardcode tên thương hiệu hay màu vào các file này.
- **TENANT-CONFIG (đổi theo khách):** `tenant-config.json` theo schema của `agents/MASTER-TEMPLATE-MANIFEST.md`. Trường `compliance_overrides` luôn `null`.
- Giọng, kênh, ngôn ngữ, từ cấm: agent đọc từ `tenant-config.json`, không đọc từ prompt.

## Skill nạp vào agent

- `skills/social-media/SKILL.md`
- `skills/content-writing/SKILL.md`
- `skills/customer-support/SKILL.md`

## Cách bung

1. Điền hết mục `CHƯA CÓ — hỏi CEO` trong `tenant-config.json`, `JD-KPI-SOP-ESCALATION.md`, `HANDOVER.md`.
2. Đọc `INSTALL-PLAN.md`; chỉ cài sau khi người duyệt. Công cụ không tự cài gì.
3. Tạo biến môi trường theo danh sách TÊN trong `HANDOVER.md` (giá trị nằm ngoài kho, không bao giờ ghi vào file .md).
4. Dán `system-prompt.md` làm instruction của agent trên vessel đã chọn.
5. Chạy `tests/TEST-PLAN.md`, ghi PASS/FAIL thật. Spike 30 phút trên việc thật do người chạy.
6. Bật `draft_only` hai tuần; chỉ sang chế độ tự chủ đã khai báo khi các mốc trong `deploy-checklist.md` đạt.
7. Ghi `catalog/USAGE-LOG.md` cho mỗi mục kho đã dùng thật; ghi `catalog/GAP-LOG.md` cho mỗi HỔNG.
