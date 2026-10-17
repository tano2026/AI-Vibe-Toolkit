# Trùm Sân Bay OPC — ghi chú thiết kế (NHÁP, đang brainstorm)

> Trạng thái: **nháp chưa duyệt**, dừng sau Phần 2 trên 5 phần. Chưa viết spec, chưa viết kế hoạch triển khai, chưa dựng gì.
> Ngày ghi: 2026-10-17. Người quyết: Nobitano. Làm tiếp **sau khi hoàn thiện kho** (xem mục 7).
> Đọc kèm: `agents/company/ORG-v2.md` (ORG v3, 9 agent), `agents/company/DECISION-MATRIX.md`, `agents/trum-san-bay/README.md`.

## 1. Mục tiêu (đã thống nhất)
Công ty một người quanh thương hiệu Trùm Sân Bay: xây kênh (Facebook chính, kèm IG, TikTok, YouTube) và thương hiệu, rồi bán dịch vụ sân bay và làm affiliate. Nobitano là CEO duyệt việc, các bộ phận do agent chạy.

"90% tự động" được hiểu là **90% khối lượng việc do agent làm, người chỉ duyệt ở các cổng**. Ba lằn ranh đỏ của kho giữ nguyên: AI không tự chi tiền, không tự bấm đăng ngoài lô đã duyệt, không tự cam kết giá hay phạm vi với khách.

## 2. Quyết định đã chốt
| Điểm | Quyết định |
|---|---|
| Doanh thu 6 tháng đầu | Affiliate và bán dịch vụ chạy song song |
| Thực hiện dịch vụ | Đối tác bên thứ ba làm ngoài đời thật |
| Dòng tiền | **Trùm Sân Bay thu tiền của khách rồi trả đối tác** (cần cổng thanh toán, đối soát, hoá đơn, hoàn tiền; phần này luôn có người duyệt) |
| Kiến trúc | Phương án A: mở rộng lõi ORG-v3 bằng Domain Pack Trùm Sân Bay, bật theo pha (C) |
| Kênh khách | Bot Zalo (OA đã xác thực) và các mạng xã hội cho CSKH và bán hàng, một hộp thư chung |
| Marketing | Một agent marketing chuyên nghiệp (Giám đốc Marketing) dựa trên `agents/digital-marketing-agent` |
| Báo giá trong chat | Bot trích **bảng giá chuẩn** do CEO duyệt trước (coi như FAQ, mức L1); giá ngoài bảng, giảm giá, đoàn lớn, hoàn tiền, khiếu nại chuyển cho CEO (L3) |

Chưa quyết, đừng coi là đã quyết: license Remotion (kho ghi công ty từ 4 người trở lên phải mua bản thương mại) và CRM đang dùng. Một báo cáo của DeepSeek Harness ghi "mua khi có agent thứ 4" và "HubSpot", nhưng đó là DSH tự điền, chưa phải quyết định của CEO.

## 3. Bộ phận (dùng 9 agent ORG-v3, thêm 2 gói mở rộng, không thêm agent mới)
| Bộ phận | Agent | Kho đã có | Còn thiếu |
|---|---|---|---|
| Điều phối | `ceo` (Hermes) | `HERMES-SOUL`, `COORDINATION-v2` | Luồng báo cáo riêng |
| Nghiên cứu | `research` | `content-research`, `aviation-knowledge`, `trend-scout` | Danh sách đối thủ, nguồn tin chuẩn |
| Thương hiệu và nội dung | `marketing` (Giám đốc Marketing) | `content-strategy-ideation`, `brand-voice`, `writer-agent-prompt`, `content-pillar-cluster-architecture`, `digital-marketing-orchestrator` | **Bộ nhận diện thương hiệu** |
| Sản xuất hình, video | `media` | `image-prompt-engineer`, `video-renderer`, `brand-design-system`, `social-publisher` | Tự động chèn logo |
| Affiliate | `marketing` | `affiliate-injector`, `affiliate-disclosure-writer`, `platform-disclosure-adapter`, `compliance-gate` | Danh sách chương trình thật (SIM, đổi tiền, phòng chờ) |
| Bán hàng và đối tác | `sales` + **gói Quản lý đối tác** | `sales-ceo`, `legal-compliance` | Gói đối tác, mẫu hợp đồng, CRM lead |
| Đơn hàng và tiền | `operations` + **gói Tài chính và thanh toán** | `ops-finance` (khung) | Cổng thanh toán, quy trình hoàn tiền, hoá đơn |
| Cửa hàng chat (CSKH và bán) | `sales` (trước bán), `support` (sau bán) | `zalo-channel-connection-guide`, `zalo-oa-du-lich-luu-tru-playbook`, `repos/chatwoot`, `sentiment-classifier`, `reply-agent-prompt` | KB riêng, bảng giá chuẩn |
| Phân tích | `analytics` | `media-performance-discipline`, `kpi-dashboard-creator`, `pipeline-dashboard` | Nguồn số liệu thật |
| Hạ tầng, tuân thủ | `dev` | `api-error-handler`, `infra-ops-agent`, `LOOP-TOKEN-GOVERNOR` | Schema Airtable, workflow n8n (README nhắc nhưng file không tồn tại) |

Điều cần kiểm lại trước khi tin (lấy từ entry kho, chưa mục nào chạy thật):
- Zalo: bot nói chuyện với khách phải dùng **Zalo OA đã xác thực**. Entry ghi gói Nâng cao 99K hoặc Premium 399K một tháng để mở chatbot, duyệt 3–7 ngày; giá cần kiểm lại. Không dùng nick Zalo cá nhân tự động hoá cho khách (có thể bị khoá).
- Chatwoot: MIT, tự host Docker, tối thiểu 4GB RAM, gộp Facebook, Instagram, Telegram, web chat. Zalo chỉ qua kênh API và webhook. AI đầy đủ cần gói trả phí hoặc nối OmniRoute.
- `agents/trum-san-bay` hiện **chưa chạy với credential thật**; TikTok và YouTube publisher còn nợ chưa test.

## 4. Luồng việc và cổng duyệt (Phần 2)
1. **Nội dung, mỗi tuần:** analytics → marketing lập lịch tuần theo trụ cột và phễu TOFU/MOFU/BOFU 60/25/15 → research kiểm chứng thông tin hàng không → media sản xuất → compliance-gate và ghi chú quảng cáo → **[G1] CEO duyệt cả lô tuần** → tự đăng theo lịch → theo dõi. Bài lệch lịch đã duyệt quay lại hỏi CEO. Hai tuần đầu chỉ soạn, CEO đăng tay.
2. **Tin nhắn, thời gian thực:** Zalo OA, Messenger, IG vào hộp thư chung → phân loại ý định và cảm xúc → FAQ và bảng giá chuẩn bot tự trả lời → muốn mua thì `sales` lập đơn nháp → ngoài bảng thì **[G3]** chuyển CEO. Hai tuần đầu bot ở chế độ nháp.
3. **Đơn và tiền:** đơn nháp → khách thanh toán → `operations` xác nhận → gửi đối tác → nhắc lịch → hỏi đánh giá → đối soát cuối tuần → **[G4] CEO duyệt lệnh trả đối tác** → **[G5] hoàn tiền từng ca**. Agent không tự chuyển tiền ra ngoài.
4. **Affiliate:** link theo dõi gắn khi soạn bài, đối soát hoa hồng hằng tuần, analytics đưa lại cho marketing chỉnh lịch.

| Cổng | Việc |
|---|---|
| G1 | Duyệt lô nội dung tuần |
| G2 | Chi tiền mới (ads, công cụ trả phí, thuê ngoài) |
| G3 | Ngoại lệ trong chat |
| G4 | Duyệt trả đối tác |
| G5 | Hoàn tiền |
| G6 | Khủng hoảng, xoá bài |
| G7 | Đổi bảng giá, SOP, credential, hợp đồng đối tác |

Chốt an toàn: `/stop` trên Telegram dừng đăng bài và bot chat; tự khoá khi token Meta hết hạn, khi tỉ lệ chuyển người vượt ngưỡng, hoặc khi chi tiêu chạm mức đặt; mọi hành động vào `activity_log`. Tần suất cổng trong thiết kế là mục tiêu, chưa có số đo.

## 5. Còn lại để brainstorm (Phần 3 đến 5)
- **Phần 3:** hạ tầng và công cụ: VPS, hộp thư chung, cổng thanh toán, kho dữ liệu, theo dõi affiliate, mapping cụ thể mục kho cho từng thứ.
- **Phần 4:** KPI "90%" đo thế nào (tỉ lệ tin nhắn bot xử lý trọn, tỉ lệ bài trong lô không sửa, giờ CEO mỗi tuần), lộ trình pha, mốc đo giữa các pha.
- **Phần 5:** rủi ro và pháp lý: pháp nhân thu tiền khách, hoá đơn, điều khoản hoàn tiền, quy định quảng cáo và affiliate trên từng nền tảng, dữ liệu cá nhân của khách. Đây là việc của CEO và luật sư; thiết kế chỉ chừa chỗ cắm.
- Sau đó: viết spec (`docs/superpowers/specs/`), CEO duyệt spec, rồi mới viết kế hoạch triển khai.

## 6. Câu hỏi mở cho CEO
1. Bảng giá chuẩn và danh sách đối tác đầu tiên (ai, dịch vụ gì, chia hoa hồng bao nhiêu).
2. Pháp nhân nào thu tiền; cổng thanh toán nào.
3. Tên thương hiệu, giọng, bộ nhận diện (kho chưa có).
4. Quyết license Remotion và CRM (hai điểm treo của STARTER-KIT).

## 7. Điều kiện để quay lại làm tiếp
- Kho đã đủ ổn: Trio kiểm chéo xong, nhãn gộp xong, ít nhất vài dòng `USAGE-LOG` thật (hiện vẫn trống).
- Nhắc Claude: đọc file này, chạy lại `catalog/AGENT-ROUTER.md` để kiểm các mục ở mục 3 còn đúng, rồi tiếp tục từ Phần 3.
