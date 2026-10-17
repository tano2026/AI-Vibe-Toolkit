# OPC-ROSTER — Đội hình agent của OPC `trum-san-bay-opc`

> Chọn từ **9 agent thật của ORG v3** (`agents/company/ORG-v2.md`). Không thêm agent thứ 10: nhu cầu mới đi qua
> gói mở rộng (extension pack) nạp vào agent có sẵn. Lõi 9 agent không sửa khi thêm client; sửa lõi là thay đổi công ty, phải qua CEO.
> Mỗi agent dưới đây có đủ bốn thứ JD, KPI, SOP, Escalation; thiếu một thứ là chưa được nhận việc.

## Cấu hình OPC

- **Domain Pack:** `domain-packs/trum-san-bay-opc/PACK.md` (mọi delegation phải có header `[PACK: trum-san-bay-opc]`)
- **Nguồn doanh thu:** affiliate, dich-vu
- **Kênh:** facebook, zalo, instagram
- **Gói mở rộng yêu cầu:** tai-chinh, doi-tac
- **Vessel/runtime:** theo cột "Runtime" bên dưới, lấy từ bảng phân công ORG v3. Hermes là bộ não (agent `ceo`); OpenClaw là tay chân thực thi, không tự quyết, không có kênh nhận lệnh riêng.
- **Tier LLM:** cheap (DeepSeek V3), balanced (Gemini Flash), reasoning (DeepSeek R1), creative (Claude Sonnet, chỉ khi chất lượng chữ quyết định). Nâng tier phải ghi lý do trong brief (mức L1). Ghi chú: ORG v3 không ghi tier cho agent `ceo`; giá trị dưới đây là suy ra của công cụ, CEO xác nhận.

## Bảng đội hình

| Agent | Bật | Runtime | Tier LLM | Package tham chiếu | KPI chính (tuần) |
|---|---|---|---|---|---|
| ceo | Có | Hermes | balanced (suy ra của công cụ; ORG v3 không ghi) | `agents/company/HERMES-SOUL.md`; `agents/company/COORDINATION-v2.md` | Việc chờ duyệt không tồn quá 24 giờ; bản tin sáng gửi đủ (đề xuất của công cụ, ORG v3 không ghi KPI cho ceo) |
| research | Có | ceo (Hermes) | reasoning | `agents/research-analytics-pro/` | Số insight report được agent khác dùng (cited) |
| dev | Có | Cả 3 runtime (Hermes, OpenClaw, Antigravity) | balanced | `agents/infra-ops-agent/`; `agents/HERMES-PLAYBOOK.md`; `agents/OPENCLAW-PLAYBOOK.md`; `agents/ANTIGRAVITY-PLAYBOOK.md` | Uptime 3 runtime + ticket tồn dưới 7 ngày |
| sales | Có | ceo + OpenClaw | balanced (reasoning khi chạm hợp đồng) | `agents/sales-ceo/system-prompt.md` | Số deal chốt + pipeline value + 100% hợp đồng sàng lọc trước ký |
| marketing | Có | ceo + OpenClaw | creative (content) / balanced (SEO, ads) | `agents/digital-marketing-agent/`; `agents/company/roles/marketing.md`; `agents/company/roles/content-creator.md` | Lead/traffic so với target + content sẵn sàng đăng đúng hạn |
| media | Có | OpenClaw | creative (design) / cheap (đăng) | `agents/company/roles/media.md`; `agents/company/roles/designer.md`; `agents/media-pro/`; `agents/designer-pro/` | Số visual đúng spec + số bài đăng đúng lịch |
| operations | Có | ceo (Hermes) | cheap -> balanced (reasoning khi tranh chấp lao động) | `agents/company/roles/ops-finance.md` | Đơn xử lý dưới SLA + % ca trực đủ người |
| support | Có | OpenClaw | cheap | `agents/customer-satisfaction-pro/` | Ticket resolve dưới SLA |
| analytics | Có | ceo (Hermes) | reasoning | `agents/company/roles/ops-finance.md`; `skills/tu-duy-tai-chinh-vi-mo/`; `skills/tu-duy-tai-chinh-phat-trien-ban-than/` | Báo cáo KPI/forecast đúng hạn tuần |

## Chi tiết từng agent (JD / KPI / SOP / Escalation)

KPI mục tiêu bằng số: `CHƯA CÓ — hỏi CEO` cho tới khi có số nền sau hai tuần chạy nháp. Công cụ không đặt số.

### ceo

- **JD:** Nhận lệnh, phân tích, giao việc, theo dõi tiến độ, báo cáo. Là tầng Hermes vận hành, không ngang hàng 8 agent dưới.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Việc chờ duyệt không tồn quá 24 giờ; bản tin sáng gửi đủ (đề xuất của công cụ, ORG v3 không ghi KPI cho ceo). Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP dispatch và bản tin sáng; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Hai agent xung đột kết quả, job kẹt hơn 24 giờ, CEO không phản hồi bản duyệt: tạo escalation lên CEO. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, không có section riêng trong EXPERT-CORE, Domain Pack của OPC

### research

- **JD:** Nghiên cứu thị trường, phân tích ngách, fact-check, đối thủ, xu hướng.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Số insight report được agent khác dùng (cited). Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP kiểm chứng thông tin trước khi lên lô; SOP báo cáo nền đầu tiên của pack; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Nguồn mâu thuẫn hoặc không kiểm được: gắn [CẦN VERIFY], không dùng, escalate. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, EXPERT-CORE mục ① Research & Data Analytics, Domain Pack của OPC

### dev

- **JD:** Code/deploy, fix bug, hạ tầng và healthcheck/monitor/backup, review.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Uptime 3 runtime + ticket tồn dưới 7 ngày. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP healthcheck và xoay token theo lịch; SOP triển khai nội bộ; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Healthcheck fail 3 lần, token/khoá hết hạn, chạm production có khách, đổi credential: escalate. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, EXPERT-CORE mục ⑤ Dev & Automation, Domain Pack của OPC

### sales

- **JD:** Lead-gen, CSKH trước bán, outreach, proposal, pipeline.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Số deal chốt + pipeline value + 100% hợp đồng sàng lọc trước ký. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP phân loại ý định và lập đơn nháp; SOP chuyển ngoại lệ lên G3; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Khách đòi giá ngoài bảng chuẩn, giảm giá, phạm vi ngoài chuẩn, hợp đồng/NDA: chuyển CEO (L3); gửi outreach thật là L2. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, EXPERT-CORE mục ③ Sales, Domain Pack của OPC; gói mở rộng: doi-tac

### marketing

- **JD:** Content đa kênh (viết và chiến lược), SEO, campaign, content calendar, trend.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Lead/traffic so với target + content sẵn sàng đăng đúng hạn. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP lô nội dung tuần (lịch, kiểm chứng, sản xuất, tuân thủ, cổng G1); SOP gắn link và chú thích affiliate; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Bài lệch lịch đã duyệt, đề xuất chi ngân sách, claim không có nguồn: quay lại hỏi, không tự tiếp tục. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, EXPERT-CORE mục ② Marketing và ④ Content Creator, Domain Pack của OPC

### media

- **JD:** Thiết kế, hình ảnh, video, storyboard, format check, brand asset, đăng (guardrail người-tạo khác người-đăng qua approval gate).
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Số visual đúng spec + số bài đăng đúng lịch. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP sản xuất hình/video theo token thương hiệu; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Thiếu design token/bộ nhận diện: hỏi CEO, không tự chốt. Bấm đăng luôn qua cổng duyệt. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, EXPERT-CORE mục ⑥ Designer và ⑦ Media, Domain Pack của OPC

### operations

- **JD:** Đơn/booking/lịch (fulfillment), ca trực/nhân sự cơ bản (qua gói mở rộng HR&Admin), tự động hoá. Healthcheck hạ tầng thuộc dev.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Đơn xử lý dưới SLA + % ca trực đủ người. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP vòng đời đơn; SOP nhắc lịch và đối soát; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Đơn kẹt quá SLA, lệch số tiền, tranh chấp: escalate; mọi lệnh chi tiền là L2. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, không có section riêng trong EXPERT-CORE, Domain Pack của OPC; gói mở rộng: tai-chinh

### support

- **JD:** CSKH 24/7 sau bán, KB/FAQ, ticket, escalate.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Ticket resolve dưới SLA. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP trả lời theo KB/FAQ; SOP chuyển khiếu nại (L3); soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Khách phàn nàn, đòi hoàn tiền, khủng hoảng: không tự trả lời, chuyển nguyên văn cho CEO (L3). Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, EXPERT-CORE mục ⑧ Customer Satisfaction, Domain Pack của OPC
- **Ghi chú:** ORG v3 ghi support chưa có role pack riêng; kho có agents/customer-satisfaction-pro/. Công cụ đề xuất dùng, CEO xác nhận.

### analytics

- **JD:** Doanh thu, KPI, dashboard, trend/anomaly, forecast, SWOT; nơi nạp 3 skill tư duy tài chính.
- **Ranh giới (không làm):** không chi tiền, không tự publish, không tự cam kết; không làm việc ngoài JD; không đọc/in giá trị khoá.
- **KPI:** Báo cáo KPI/forecast đúng hạn tuần. Mục tiêu bằng số: CHƯA CÓ — hỏi CEO
- **SOP:** SOP báo cáo KPI tuần; SOP đối soát doanh thu/hoa hồng; soạn bản nháp trong bảng `sops`, bước chi tiết CHƯA CÓ — hỏi CEO
- **Escalation:** Số liệu bất thường (anomaly), thiếu nguồn số thật, KPI lệch dưới 70% target: ghi giải thích và escalate. Kẹt hơn 24 giờ hoặc lỗi lặp 3 lần thì tạo bản ghi `escalations`.
- **Nạp theo ORG v3:** package tham chiếu ở bảng trên, không có section riêng trong EXPERT-CORE, Domain Pack của OPC


## Gói mở rộng

| Gói | Nạp vào agent | Role pack trong kho | Trạng thái |
|---|---|---|---|
| tai-chinh (Tài chính và thanh toán) | operations | CHƯA CÓ trong kho | ĐỀ XUẤT mới từ thiết kế nháp. Tham khảo: agents/company/roles/ops-finance.md (khung, chưa có cổng thanh toán, hoàn tiền, hoá đơn). Ghi `catalog/GAP-LOG.md` và soạn role pack trước khi bật. |
| doi-tac (Quản lý đối tác) | sales | CHƯA CÓ trong kho | ĐỀ XUẤT mới từ thiết kế nháp. Tham khảo: agents/company/roles/legal-compliance.md (khung hợp đồng); chưa có mẫu hợp đồng đối tác, CRM đối tác. Ghi `catalog/GAP-LOG.md` và soạn role pack trước khi bật. |

Gói mở rộng nạp THÊM vào agent chủ khi task khớp, không nạp mặc định, và không phải agent thứ 10.

## Cách nạp agent (ORG v3, không đổi)

`ceo` (Hermes) lấy ba thứ rồi nhúng vào tin giao việc: (1) package tham chiếu của agent, (2) section tương ứng trong
`agents/company/EXPERT-CORE.md`, (3) Domain Pack `domain-packs/trum-san-bay-opc/PACK.md`. Gói mở rộng nạp THÊM khi task khớp, không nạp mặc định.
Job đầu tiên luôn là `[PACK: trum-san-bay-opc] agent=research`: quét thị trường, đối thủ, kênh. Không agent nào chạy trước khi `research` nộp báo cáo nền.
