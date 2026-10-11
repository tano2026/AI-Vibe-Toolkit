# Claude Dashboards + Claude Motion — vẽ dashboard từ data, làm video hoạt hoạ giải thích (beta 10/2026)

## TL;DR
Ngày 8/10/2026 Anthropic ra hai loại artifact mới trong Claude, đều **beta**. **Dashboards**: hỏi bằng tiếng thường, Claude nối vào kho dữ liệu (Redshift, BigQuery, ClickHouse, Databricks, Snowflake, Salesforce...) rồi dựng dashboard tự cập nhật, bấm vào con số là thấy truy vấn đằng sau. **Motion**: gõ prompt, ra video hoạt hoạ giải thích (ví dụ báo cáo quý thành clip 30 giây), tải MP4. Motion **không phải AI tạo video**: nó viết animation thành code nên sửa được từng chữ, từng số. Điểm cần nhớ: **Motion chỉ có ở gói Team và Enterprise**, Dashboards cho gói trả phí. Đây là công cụ dùng trong app Claude, **chưa thấy API để agent gọi**.

## Mức kiểm dùng trong file
✅ = trang chính thức của Anthropic (tao đọc 11/10/2026) · 📖 = chỉ từ bài tóm tắt bên thứ ba · ❓ = chưa test thật, cần mày thử.
Tweet gốc trên X **không mở được** (site chặn bot). Số liệu bên dưới lấy từ bài Help/Resources của Anthropic và các bài tóm tắt, không phải từ tweet.

## Dùng để làm gì
| | Dashboards | Motion |
|---|---|---|
| Làm gì | Hỏi câu → ra biểu đồ/bảng số, tự refresh khi data đổi ✅ | Prompt → hoạt hoạ giải thích, chỉnh trong editor hoặc nhờ Claude sửa ✅ |
| Nguồn vào | Connector kho dữ liệu + CRM, hoặc file CSV/TSV/JSON đính kèm ✅📖 | Prompt, báo cáo/số liệu mày đưa ✅ |
| Minh bạch | Bấm vào số xem query; mỗi chart có giờ refresh cuối ✅ | Animation là code, sửa từng chữ/số/timing ✅ |
| Ra ngoài | Chia sẻ sang Amplitude, Grafana, Hex, Mixpanel, Omni, Perplexity, PostHog, Sigma; Looker, monday.com, Tableau "sắp có" ✅ | Tải MP4; mở tiếp ở Adobe, Descript, HeyGen, Higgsfield, invideo, Luma AI, Runway; Canva, Captions "sắp có" ✅ |
| Gói | Gói trả phí (bài không nêu tên Pro hay Max) ✅ | **Chỉ Team và Enterprise** ✅ |
| Trạng thái | Beta ✅ | Beta ✅ |

Docs, Slides, Design đã hết beta và có ở mọi gói kể cả Free ✅. Admin Enterprise: Dashboards và Motion **tắt mặc định**, bật ở Organization settings → Artifacts ✅. Bài **không nêu con số giới hạn** nào (số query, dung lượng, số lần xuất) ✅.

## Setup từng bước
1. Vào claude.ai (app web/desktop), kiểm gói của mày. Nếu là Pro/Max cá nhân: thử Dashboards trước, Motion có thể không hiện ❓.
2. Dashboards, cách A (không cần kho dữ liệu): đính kèm CSV/TSV/JSON → nhắn "dựng dashboard từ file này, ... " 📖.
3. Dashboards, cách B: Settings → Connectors → nối nguồn dữ liệu (BigQuery, Snowflake, Salesforce...) → hỏi bằng câu thường ✅.
4. Motion: nhắn "làm video hoạt hoạ 30 giây giải thích ..." → mở editor chỉnh chữ/số → Download MP4 ✅.
5. Muốn đưa sang bước dựng tiếp: dùng nút mở sang HeyGen/Runway/Adobe... trong menu xuất ❓ (tên nút chưa tao thấy tận mắt).
6. Tài khoản tổ chức: nhờ admin bật ở Organization settings → Artifacts ✅.

## Ví dụ thực tế (chưa chạy, chỉ là kịch bản để mày thử ❓)
**1. ABTRIP báo cáo doanh thu tuần.** Xuất báo cáo bán vé tuần từ hệ thống ra CSV (cột: ngày, hãng, kênh, số vé, doanh thu, hoàn/đổi) → đính kèm → prompt: "Dựng dashboard: doanh thu theo hãng và theo kênh, tỷ lệ hoàn/đổi theo ngày, top 5 tuyến. Mỗi số ghi rõ lấy từ cột nào." Cái đáng kiểm là phần "nguồn của từng số": mở thử 3 con số, tự cộng lại bằng Excel xem có khớp không.

**2. Wonder Mart đơn hàng.** Export đơn từ Shopify/Woo ra CSV → hỏi "tỷ lệ bỏ giỏ theo sản phẩm, doanh thu theo nguồn quảng cáo". Dashboard hợp để xem nhanh, không thay GA4 hay báo cáo thuế.

**3. Tano content.** Có số liệu kênh (view, follow theo tuần) → Motion: "clip 30 giây: 3 số tăng trưởng tuần này, nền tối, số chạy từ 0 lên". Tải MP4 làm cảnh chèn vào video TikTok.

## Lưu ý / lỗi thường gặp
- **Số trên dashboard là do Claude tính** từ file/query. Với số liên quan tiền (doanh thu, hoàn vé), luôn tự đối chiếu ít nhất 3 số với nguồn gốc trước khi gửi ai.
- File đính kèm có thể bị giới hạn dung lượng (tao thấy loại dashboard này giới hạn khoảng 8MB trong công cụ tao đang dùng) ❓. Data lớn thì nối connector hoặc tổng hợp trước.
- **Không gửi dữ liệu khách (tên, SĐT, số hộ chiếu) lên dashboard** nếu chưa cần. Ẩn cột nhạy cảm trước.
- Motion "không phải AI video": không tạo người, không tạo cảnh quay. Nó hợp làm số liệu chạy, sơ đồ, chữ động; không hợp làm cảnh đời thật.
- Tính năng beta: giao diện và giới hạn có thể đổi trong vài tuần.
- Claude Design bản độc lập vẫn chạy đến 14/12/2026, sau đó chat/bình luận trong bản đó không còn ✅.

## Áp vào hệ thống của mày
| Việc | Nên dùng gì | Vì sao |
|---|---|---|
| Xem nhanh số liệu 1 lần, gửi sếp/đối tác | Dashboards | Không code, có truy vết nguồn của từng số |
| Dashboard chạy hằng ngày, tự động, agent đẩy số | **Không dùng Dashboards** (chưa thấy API). Dùng `skills/kpi-dashboard-creator.md` / `skills/dashboard-builder` + Hermes | Cần script chạy được trên VPS |
| Clip số liệu 1 lần cho video | Motion (nếu có gói) | Ra MP4 nhanh, sửa chữ không cần dựng lại |
| Clip hàng loạt, nhét text vào ra video | `stacks/remotion-template-factory.md` hoặc `skills/hyperframes-skill` | Chạy bằng lệnh, agent gọi được |

Một chi tiết nên thử: trong tài khoản Claude của mày đang có connector **HyperFrames by HeyGen**, và connector này có tool `import-claude-motion-from-url` (đọc từ danh sách tool, tao chưa gọi thử ❓). Nghĩa là có đường **Motion → HyperFrames** để dựng tiếp thành project HeyGen. Nếu chạy được, đây là cầu nối từ "làm tay trong app" sang "render hàng loạt".

## Đánh giá cá nhân
**Điểm cộng:** truy vết từng con số (xem query, giờ refresh) là thứ khiến dashboard AI đáng tin hơn hẳn kiểu "AI đoán rồi vẽ"; Motion viết animation bằng code nên sửa chữ/số rất lẹ, không phải sinh lại cả video như AI video.
**Điểm yếu:** Motion khoá ở Team/Enterprise nên dân cá nhân có thể không dùng được; chưa có API nên không đưa vào pipeline tự động; bài chính thức không công bố giới hạn nào; chưa có ai test độ chính xác số liệu trên data thật.
**Điểm: 6.5/10 cho mày lúc này.** Dashboards đáng thử ngay với CSV của ABTRIP. Motion chỉ đáng quan tâm nếu mày có gói Team, còn không thì Remotion/HyperFrames trong kho làm được việc tương đương và tự động hoá được.

## Link
- Trang chính thức: https://claude.com/ja/resources/articles/dashboards-and-motion
- Tweet gốc (không đọc được): https://x.com/claudeai/status/2108271552991252810
- Liên quan trong kho: `skills/kpi-dashboard-creator.md`, `skills/hyperframes-skill`, `skills/remotion-skill`, `stacks/remotion-template-factory.md`

---

## 🤖 Agent Integration
Không có API/CLI công khai cho Dashboards hay Motion trong nguồn tao đọc, nên **không có code Hermes để gọi trực tiếp**. Đừng viết agent giả định endpoint.

### Hermes (Python)
Cần dashboard/video tự động → dùng đường có API sẵn trong kho: `skills/kpi-dashboard-creator.md` (dashboard từ data) và `stacks/remotion-template-factory.md` (video từ JSON props).

### OpenClaw
Nhận lệnh Telegram kiểu "làm dashboard doanh thu tuần" → trả về checklist cho Nobitano mở Claude làm tay (đính file CSV + prompt mẫu ở mục Ví dụ), không tự gọi.

### Antigravity
Không có gì để deploy.
> ⚠️ Nếu sau này Anthropic công bố API cho hai tính năng này, báo tao để cập nhật mục này.
