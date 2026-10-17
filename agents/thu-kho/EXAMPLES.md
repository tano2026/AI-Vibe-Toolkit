# EXAMPLES — Đầu ra thật của Thủ Kho

> Chạy ngày 2026-10-17 trên `catalog/catalog.json` (916 mục), không có `catalog/audit.json`. Mọi khối trong ``` dưới đây là **đầu ra nguyên văn** của `python tools/thu_kho.py ...` (không chỉnh sửa; các "Khớp:" dài là do công cụ in). Sinh lại bằng cách chạy lại lệnh ghi trên mỗi mục.
> Đây là **tự kiểm của người làm công cụ**, không phải đánh giá độc lập. "Hợp lý" nghĩa là top-3 có mục mà người làm agency sẽ thử mở đọc; **không** nghĩa là mục đó đã chạy được (chưa mục nào được chạy).

## Chấm top-3 của 8 truy vấn

| # | Truy vấn | Top-1 | Nhận xét top-3 |
|---|---|---|---|
| 1 | cào web đối thủ | `mcps/crawl4ai` | **Tốt.** 3 mục đều là công cụ cào web thật (Crawl4AI cần Docker + RAM ≥ 4GB; gpt-crawler; Firecrawl MCP cần khoá API) |
| 2 | đăng bài Facebook có lịch | `mcps/buffer-mcp` | **Khá.** #1 có lịch đăng, #2 Meta Graph API (API gốc của Facebook). #3 là skill đặc thù Trùm Sân Bay, chỉ để tham khảo |
| 3 | giọng đọc tiếng Việt | `repos/capcut-tts-api` | **Khá.** Cả 3 là TTS; chưa có gì kiểm chất lượng giọng Việt. `capcut-tts-api` nên đọc kỹ điều khoản dịch vụ trước |
| 4 | làm video ngắn không GPU | `repos/yasgu` | **Khá.** Đều là máy tạo video ngắn; "không GPU" chỉ loại được mục có nhãn `needs: gpu`, mục không ghi gì vẫn có thể nặng |
| 5 | CRM quản lý khách hàng | `repos/twenty-crm` | **Tốt.** Twenty CRM, HubSpot MCP, Ever Gauzy |
| 6 | chatbot Zalo | `agents/company/skills/zalo-channel-connection-guide` | **Trung bình.** #1 đúng việc; #2 `sentiment-classifier` lệch (phân loại comment, không phải chatbot); `zalo-oa-...playbook` đúng nhưng chưa gắn nhãn nên chỉ nằm ở "Thêm" |
| 7 | báo cáo dashboard | `agents/trum-san-bay/skills/pipeline-dashboard` | **Kém.** Top-1 là dashboard đặc thù Trùm Sân Bay; mục tổng quát hơn (`skills/kpi-dashboard-creator`) chỉ ở #3 |
| 8 | viết email lạnh | `repos/billionmail` | **Kém.** BillionMail là máy chủ gửi mail hàng loạt (cần VPS, tốn tiền); `founder-skills` chỉ chạy trong Claude Code. Mục thật sự đúng (`skills/outbound-engine`, `skills/cold-email`) **chưa gắn nhãn** nên chỉ hiện ở "Thêm". Đây là một GAP thật của kho có nhãn |

## Đầu ra nguyên văn — 8 truy vấn

### 1. `cào web đối thủ`

Lệnh: `python tools/thu_kho.py tim "cào web đối thủ" --top 3`

```
Khả năng phát hiện: scraping (cào web), web-research (đối thủ)
1. mcps/crawl4ai  -  Crawl4AI MCP — Cào Web Free Không Giới Hạn
   điểm 35.0 | da-doc-entry-goc | độ tin cậy nhãn: cao | adoption: can-ha-tang | cần: docker | vessel: hermes,openclaw,antigravity,claude-code
   Khớp: capability scraping (chính), web-research (phụ); từ khoá: cao@ten, web@ten, doi@use_when, scrape@tom_tat, crawl@ten
   Dùng khi: Dùng khi cần cào dữ liệu web tự host và chuyển đổi nội dung thành định dạng Markdown cho AI đọc.
   Bỏ qua nếu: Bỏ qua nếu không thể chạy Docker Desktop nền hoặc máy có RAM trống dưới 4GB.
   Đọc entry gốc: mcps/crawl4ai.md
2. repos/gpt-crawler  -  gpt-crawler
   điểm 31.9 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: claude-code,hermes,openclaw
   Khớp: capability scraping (chính), web-research (phụ); từ khoá: web@use_when, crawl@ten
   Dùng khi: Dùng khi cần thu thập toàn bộ dữ liệu trang web theo liên kết nội bộ xuất ra tệp kiến thức sạch cho hệ thống truy xuất
   Bỏ qua nếu: unknown
   Đọc entry gốc: repos/gpt-crawler.md
3. mcps/firecrawl  -  Firecrawl MCP — Cào Web Sạch, AI Đọc Được Ngay
   điểm 35.0 | da-doc-dau-entry | độ tin cậy nhãn: vua | adoption: cai-ngay-duoc | cần: api-key | vessel: claude-code,hermes,openclaw
   Khớp: capability scraping (chính), web-research (phụ); từ khoá: cao@ten, web@ten, doi@use_when, scrape@tom_tat
   Dùng khi: Dùng khi cần cào dữ liệu trang web chuyển đổi thành văn bản định dạng markdown sạch cho trợ lý phân tích
   Bỏ qua nếu: Bỏ qua nếu đã sử dụng hết hạn mức 500 tín dụng cào trang hàng tháng
   Đọc entry gốc: mcps/firecrawl.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/data-scraper-agent  -  Data Scraper Agent  [từ khoá: scrape@ten, scraper@ten]
  - skills/scrapling  -  Scrapling - Adaptive Web Scraping  [từ khoá: web@ten, crawl@tom_tat]
  - skills/site-launch-checklist  -  Site Launch Checklist  [từ khoá: web@tom_tat, crawl@tom_tat]
```

### 2. `đăng bài Facebook có lịch`

Lệnh: `python tools/thu_kho.py tim "đăng bài Facebook có lịch" --top 3`

```
Khả năng phát hiện: social-media (facebook/đăng bài)
1. mcps/buffer-mcp  -  buffer-mcp — Schedule Social Media Posts Qua Claude (Buffer GraphQL)
   điểm 28.0 | da-doc-entry-goc | độ tin cậy nhãn: vua | adoption: cai-ngay-duoc | cần: api-key | vessel: hermes,openclaw,antigravity,claude-code
   Khớp: capability social-media (chính); từ khoá: bai@use_when, facebook@use_when, lich@use_when, post@ten, schedule@ten
   Dùng khi: Dùng khi cần tự động lên lịch và đăng bài viết lên nhiều kênh mạng xã hội như Twitter, LinkedIn, Facebook từ chat hoặc agent.
   Bỏ qua nếu: Bỏ qua nếu không có tài khoản Buffer hoặc không có mã BUFFER_ACCESS_TOKEN.
   Đọc entry gốc: mcps/buffer-mcp.md
2. mcps/meta-social-api  -  Meta Graph API — Facebook, Instagram, Threads
   điểm 24.72 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: api-key | vessel: claude-code,hermes,openclaw
   Khớp: capability social-media (chính); từ khoá: bai@use_when, facebook@ten, post@tom_tat
   Dùng khi: Dùng khi cần kết nối API chính thức của Meta để đăng nội dung bài viết và phân tích số liệu trên Facebook và Instagram
   Bỏ qua nếu: unknown
   Đọc entry gốc: mcps/meta-social-api.md
3. agents/trum-san-bay/skills/social-publisher  -  Social Publisher — Multi-Platform Adapter
   điểm 23.61 | da-doc-dau-entry | độ tin cậy nhãn: vua | adoption: cai-ngay-duoc | cần: api-key | vessel: claude-code,hermes,openclaw
   Khớp: capability social-media (chính); từ khoá: bai@use_when, facebook@use_when, publish@ten
   Dùng khi: Dùng khi cần tự động hóa đăng tải bài viết và video lên các nền tảng mạng xã hội Facebook TikTok Instagram
   Bỏ qua nếu: unknown
   Đọc entry gốc: agents/trum-san-bay/skills/social-publisher/SKILL.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/social-publisher  -  Social Publisher (SocialClaw)  [từ khoá: facebook@tom_tat, post@tom_tat, publish@ten]
  - skills/personal-branding-creator  -  personal-branding-creator — Skill Phát Triển Nhân Hiệu Đa Kênh  [từ khoá: facebook@tom_tat, lich@tom_tat]
```

### 3. `giọng đọc tiếng Việt`

Lệnh: `python tools/thu_kho.py tim "giọng đọc tiếng Việt" --top 3`

```
Khả năng phát hiện: voice-tts (giọng đọc)
1. repos/capcut-tts-api  -  capcut-tts-api
   điểm 28.0 | da-doc-entry-goc | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: hermes,antigravity
   Khớp: capability voice-tts (chính); từ khoá: giong@use_when, doc@use_when, tieng@use_when, viet@use_when, tts@ten, voice@use_when
   Dùng khi: Dùng khi cần tạo voiceover tiếng Việt tự nhiên bằng giọng đọc CapCut (BV074) qua script Python mà không cần mở app.
   Bỏ qua nếu: Bỏ qua nếu cần API chính thức ổn định lâu dài hoặc không có tài khoản CapCut hợp lệ để cấu hình.
   Đọc entry gốc: repos/capcut-tts-api.md
2. repos/vieneu-tts  -  VieNeu-TTS — GitHub/HuggingFace
   điểm 28.0 | da-doc-entry-goc | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: hermes,antigravity
   Khớp: capability voice-tts (chính); từ khoá: giong@use_when, doc@use_when, tieng@use_when, viet@use_when, tts@ten
   Dùng khi: Dùng khi cần tạo giọng đọc tiếng Việt tự nhiên và sao chép giọng nói chạy ngoại tuyến trên máy.
   Bỏ qua nếu: unknown
   Đọc entry gốc: repos/vieneu-tts.md
3. mcps/minimax-mcp  -  MiniMax MCP — TTS + Video + Nhạc Trong 1 MCP Server
   điểm 25.29 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: api-key,tra-phi | vessel: claude-code,hermes,openclaw
   Khớp: capability voice-tts (chính); từ khoá: giong@use_when, doc@use_when, tts@ten, voice@tom_tat, speech@tom_tat
   Dùng khi: Dùng khi cần tạo giọng đọc thuyết minh nhân bản giọng nói và tạo video từ mô tả văn bản bằng mô hình MiniMax
   Bỏ qua nếu: Bỏ qua nếu tài khoản MiniMax đã hết hạn mức tín dụng hoặc không muốn chi trả chi phí tạo video
   Đọc entry gốc: mcps/minimax-mcp.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/sherpa-vietnamese-asr  -  Sherpa Vietnamese ASR — Tool  [từ khoá: giong@tom_tat, tieng@tom_tat, viet@ten, vietnamese@ten, vietnam@ten]
  - skills/resona  -  Resona — TTS & Lồng Tiếng Video AI Tiếng Việt  [từ khoá: giong@tom_tat, tieng@ten, viet@ten, tts@ten]
  - skills/voice-profile-builder  -  Voice Profile Builder — Biến Bản Thân Thành Phiên Bản Đỉnh Cao Trong Claude  [từ khoá: viet@tom_tat, voice@ten, vietnamese@tom_tat, vietnam@tom_tat]
```

### 4. `làm video ngắn không GPU`

Lệnh: `python tools/thu_kho.py tim "làm video ngắn không GPU" --top 3`

```
Khả năng phát hiện: video-generation (làm video/video ngắn)
Tự bỏ mục cần: gpu
1. repos/yasgu  -  YASGU — YouTube Automatised Shorts Generator & Uploader
   điểm 28.0 | da-doc-entry-goc | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: api-key | vessel: hermes
   Khớp: capability video-generation (chính); từ khoá: video@use_when, shorts@ten, short@ten
   Dùng khi: Dùng khi cần tự động ráp video YouTube Shorts từ kịch bản gồm giọng đọc, video nền và phụ đề tự sinh.
   Bỏ qua nếu: Bỏ qua nếu máy chưa cài FFmpeg và ImageMagick hoặc không có API key để sinh giọng đọc.
   Đọc entry gốc: repos/yasgu.md
2. mcps/scrptly  -  Scrptly Video Generator
   điểm 25.5 | da-doc-entry-goc | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: api-key,tra-phi | vessel: hermes,openclaw,claude-code,antigravity
   Khớp: capability video-generation (chính); từ khoá: video@ten, ngan@use_when
   Dùng khi: Dùng khi cần tạo video AI từ mô tả văn bản kèm ảnh tham chiếu ngữ cảnh và giới hạn ngân sách chi phí.
   Bỏ qua nếu: Bỏ qua nếu không có API key của Scrptly hoặc cần kết quả đồng bộ tức thì không qua polling.
   Đọc entry gốc: mcps/scrptly.md
3. repos/short-video-factory  -  Short Video Factory (YILS-LIN)
   điểm 28.0 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: claude-code,hermes,openclaw
   Khớp: capability video-generation (chính); từ khoá: video@ten, ngan@use_when, short@ten
   Dùng khi: Dùng khi cần ứng dụng máy tính tự động ghép video ngắn quảng cáo hàng loạt từ tư liệu có sẵn
   Bỏ qua nếu: Bỏ qua nếu dự định đóng gói cung cấp dịch vụ mạng đóng mã nguồn do ràng buộc bản quyền AGPL-3.0
   Đọc entry gốc: repos/short-video-factory.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/short-form-pipeline  -  Short-Form Video Pipeline  [từ khoá: video@ten, shorts@tom_tat, short@ten, reels@tom_tat]
  - skills/viral-hooks  -  Viral Hooks — 100 formulas, 10 psychology triggers  [từ khoá: video@tom_tat, short@tom_tat, reels@tom_tat, generate@tom_tat]
  - skills/viral-hooks-hooks-database  -  Viral Hooks — 100 formulas, 10 psychology triggers  [từ khoá: video@tom_tat, short@tom_tat, reels@tom_tat, generate@tom_tat]
```

### 5. `CRM`

Lệnh: `python tools/thu_kho.py tim "CRM quản lý khách hàng" --top 3`

```
Khả năng phát hiện: crm-sales (crm/quản lý khách hàng)
1. repos/twenty-crm  -  Twenty CRM
   điểm 23.39 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: claude-code,hermes,openclaw
   Khớp: capability crm-sales (chính); từ khoá: crm@ten, quan@use_when, khach@use_when, hang@use_when
   Dùng khi: Dùng khi cần hệ thống quản trị quan hệ khách hàng mã nguồn mở tự lưu trữ với quy trình linh hoạt và giao diện trực quan
   Bỏ qua nếu: Bỏ qua nếu đóng gói bán lại dạng dịch vụ đóng mã nguồn do ràng buộc bản quyền AGPLv3 và Enterprise
   Đọc entry gốc: repos/twenty-crm.md
2. mcps/hubspot-mcp  -  hubspot-mcp — HubSpot CRM & Marketing Từ Claude (33 Tools)
   điểm 23.2 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: api-key | vessel: claude-code,hermes,openclaw
   Khớp: capability crm-sales (chính); từ khoá: crm@ten, ly@use_when, khach@use_when, hang@use_when
   Dùng khi: Dùng khi cần kết nối trợ lý với hệ thống HubSpot CRM để đọc tạo và cập nhật dữ liệu khách hàng và quy trình tiếp thị
   Bỏ qua nếu: unknown
   Đọc entry gốc: mcps/hubspot-mcp.md
3. repos/ever-gauzy  -  Ever Gauzy
   điểm 22.86 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: can-ha-tang | cần: docker,vps,tra-phi | vessel: claude-code,hermes,openclaw,antigravity
   Khớp: capability crm-sales (chính); từ khoá: crm@tom_tat, quan@use_when, ly@use_when, khach@use_when, hang@use_when
   Dùng khi: Dùng khi cần nền tảng quản trị tổng thể doanh nghiệp mã nguồn mở tích hợp quản lý dự án nhân sự và quan hệ khách hàng
   Bỏ qua nếu: Bỏ qua nếu cần giải pháp mở cho mọi tính năng doanh nghiệp do giấy phép Community Edition phân tầng
   Đọc entry gốc: repos/ever-gauzy.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
```

### 6. `chatbot Zalo`

Lệnh: `python tools/thu_kho.py tim "chatbot Zalo" --top 3`

```
Khả năng phát hiện: customer-support (chatbot), social-media (zalo)
1. agents/company/skills/zalo-channel-connection-guide  -  Zalo Channel Connection Guide
   điểm 23.43 | da-doc-entry-goc | độ tin cậy nhãn: vua | adoption: cai-ngay-duoc | cần: none | vessel: openclaw,hermes
   Khớp: capability customer-support (chính); từ khoá: zalo@ten
   Dùng khi: Dùng khi cần tài liệu hướng dẫn kỹ thuật kết nối kênh Zalo qua nền tảng OpenClaw
   Bỏ qua nếu: unknown
   Đọc entry gốc: agents/company/skills/zalo-channel-connection-guide/SKILL.md
2. agents/trum-san-bay/skills/sentiment-classifier  -  Sentiment Classifier — Comment Triage
   điểm 19.0 | da-doc-entry-goc | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: hermes,openclaw
   Khớp: capability customer-support (chính), social-media (phụ)
   Dùng khi: Dùng khi cần phân loại mức độ ưu tiên và cảm xúc của bình luận mạng xã hội trước khi đưa vào hàng đợi xử lý.
   Bỏ qua nếu: Bỏ qua nếu kênh không có tương tác bình luận mới hoặc đã xử lý thủ công từng phản hồi.
   Đọc entry gốc: agents/trum-san-bay/skills/sentiment-classifier/SKILL.md
3. repos/chatwoot  -  Chatwoot
   điểm 17.71 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: can-ha-tang | cần: docker,vps | vessel: claude-code,hermes,openclaw,antigravity
   Khớp: capability customer-support (chính); từ khoá: zalo@tom_tat
   Dùng khi: Dùng khi cần nền tảng hỗ trợ khách hàng đa kênh tự lưu trữ để tích hợp vào hệ thống trợ lý chăm sóc
   Bỏ qua nếu: unknown
   Đọc entry gốc: repos/chatwoot.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/zalo-oa-du-lich-luu-tru-playbook  -  Zalo OA — Playbook Vận Hành Du Lịch & Lưu Trú Mùa Cao Điểm/Biến Động  [từ khoá: zalo@ten]
```

### 7. `báo cáo dashboard`

Lệnh: `python tools/thu_kho.py tim "báo cáo dashboard" --top 3`

```
Khả năng phát hiện: data-dashboard (dashboard/báo cáo)
1. agents/trum-san-bay/skills/pipeline-dashboard  -  Pipeline Dashboard — Xem Progress Trực Quan
   điểm 23.21 | da-doc-dau-entry | độ tin cậy nhãn: vua | adoption: can-ha-tang | cần: vps | vessel: claude-code,hermes,openclaw,antigravity
   Khớp: capability data-dashboard (chính); từ khoá: bao@use_when, dashboard@ten
   Dùng khi: Dùng khi cần bảng điều khiển giám sát trạng thái quy trình sản xuất nội dung tự động và cảnh báo điểm nghẽn
   Bỏ qua nếu: unknown
   Đọc entry gốc: agents/trum-san-bay/skills/pipeline-dashboard/SKILL.md
2. agents/anbinh-travel-ops-analyst/skills/data-storytelling  -  Data Storytelling
   điểm 20.28 | da-doc-entry-goc | độ tin cậy nhãn: vua | adoption: cai-ngay-duoc | cần: none | vessel: claude-code,hermes,openclaw
   Khớp: capability data-dashboard (chính); từ khoá: bao@use_when, cao@use_when, report@tom_tat
   Dùng khi: Dùng khi cần biến số liệu thô thành báo cáo chứa thông tin cốt lõi và hành động cụ thể
   Bỏ qua nếu: unknown
   Đọc entry gốc: agents/anbinh-travel-ops-analyst/skills/data-storytelling/SKILL.md
3. skills/kpi-dashboard-creator  -  KPI Dashboard Creator — Build dashboard cho quyết định, không phải trang trí
   điểm 20.41 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: cai-ngay-duoc | cần: none | vessel: claude-code,hermes,openclaw
   Khớp: capability data-dashboard (chính); từ khoá: dashboard@ten
   Dùng khi: Dùng khi cần thiết kế bảng điều khiển chỉ số kinh doanh tập trung vào việc ra quyết định hành động
   Bỏ qua nếu: unknown
   Đọc entry gốc: skills/kpi-dashboard-creator.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/revenue-intelligence  -  Revenue Intelligence — Call Insights & Attribution  [từ khoá: report@tom_tat, reporting@tom_tat]
```

### 8. `viết email lạnh`

Lệnh: `python tools/thu_kho.py tim "viết email lạnh" --top 3`

```
Khả năng phát hiện: email-outreach (email lạnh/viết email)
1. repos/billionmail  -  BillionMail
   điểm 14.68 | da-doc-dau-entry | độ tin cậy nhãn: cao | adoption: can-ha-tang | cần: vps,tra-phi | vessel: claude-code,hermes,openclaw,antigravity
   Khớp: capability email-outreach (chính); từ khoá: email@tom_tat
   Dùng khi: Dùng khi cần nền tảng thư điện tử tiếp thị tự vận hành trên máy chủ riêng không tốn phí định kỳ hàng tháng
   Bỏ qua nếu: Bỏ qua nếu chưa có máy chủ ảo VPS và ngân sách duy trì hạ tầng gửi thư riêng
   Đọc entry gốc: repos/billionmail.md
2. repos/founder-skills  -  founder-skills (ognjengt)
   điểm 11.44 | da-doc-dau-entry | độ tin cậy nhãn: vua | adoption: cai-ngay-duoc | cần: claude-code-only | vessel: claude-code
   Khớp: capability email-outreach (phụ); từ khoá: viet@tom_tat, outreach@tom_tat
   Dùng khi: Dùng khi cần bộ mười lăm kỹ năng định dạng câu lệnh chuẩn hỗ trợ người sáng lập khởi nghiệp phát triển thị trường
   Bỏ qua nếu: unknown
   Đọc entry gốc: repos/founder-skills.md

Lưu ý: Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).

Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):
  - skills/outbound-engine  -  Outbound Engine — Cold Email & Outreach  [từ khoá: email@ten, cold@ten, outreach@ten]
  - skills/cold-email  -  MachFive - AI Cold Email Generator  [từ khoá: email@ten, cold@ten, outreach@tom_tat]
  - skills/investor-outreach  -  Investor Outreach  [từ khoá: email@tom_tat, cold@tom_tat, outreach@ten]
```

## Các lệnh khác (đầu ra nguyên văn)

### Gợi ý cho một dự án nhiều việc

Lệnh: `python tools/thu_kho.py goi-y "Làm kênh Facebook cho khách sạn: cào web đối thủ, đăng bài có lịch, làm video ngắn không GPU, báo cáo dashboard hằng tuần" --vessel hermes`

```
Yêu cầu: Làm kênh Facebook cho khách sạn: cào web đối thủ, đăng bài có lịch, làm video ngắn không GPU, báo cáo dashboard hằng tuần
Khả năng phát hiện: social-media, scraping, web-research, video-generation, data-dashboard
Tự bỏ mục cần: gpu

== social-media  (cụm: facebook, đăng bài)
  CHÍNH     : mcps/buffer-mcp - buffer-mcp — Schedule Social Media Posts Qua Claude (Buffer GraphQL) [da-doc-entry-goc/vua, api-key]
              dùng khi: Dùng khi cần tự động lên lịch và đăng bài viết lên nhiều kênh mạng xã hội như Twitter, LinkedIn, Facebook từ chat hoặc agent.
              bỏ qua nếu: Bỏ qua nếu không có tài khoản Buffer hoặc không có mã BUFFER_ACCESS_TOKEN.
  DỰ PHÒNG  : mcps/meta-social-api - Meta Graph API — Facebook, Instagram, Threads [da-doc-dau-entry/cao, api-key]
== scraping  (cụm: cào web)
  CHÍNH     : mcps/crawl4ai - Crawl4AI MCP — Cào Web Free Không Giới Hạn [da-doc-entry-goc/cao, docker]
              dùng khi: Dùng khi cần cào dữ liệu web tự host và chuyển đổi nội dung thành định dạng Markdown cho AI đọc.
              bỏ qua nếu: Bỏ qua nếu không thể chạy Docker Desktop nền hoặc máy có RAM trống dưới 4GB.
  DỰ PHÒNG  : mcps/firecrawl - Firecrawl MCP — Cào Web Sạch, AI Đọc Được Ngay [da-doc-dau-entry/vua, api-key]
== web-research  (cụm: đối thủ)
  CHÍNH     : mcps/crawl4ai - Crawl4AI MCP — Cào Web Free Không Giới Hạn [da-doc-entry-goc/cao, docker]
              dùng khi: Dùng khi cần cào dữ liệu web tự host và chuyển đổi nội dung thành định dạng Markdown cho AI đọc.
              bỏ qua nếu: Bỏ qua nếu không thể chạy Docker Desktop nền hoặc máy có RAM trống dưới 4GB.
  DỰ PHÒNG  : mcps/firecrawl - Firecrawl MCP — Cào Web Sạch, AI Đọc Được Ngay [da-doc-dau-entry/vua, api-key]
== video-generation  (cụm: làm video, video ngắn, video)
  CHÍNH     : repos/yasgu - YASGU — YouTube Automatised Shorts Generator & Uploader [da-doc-entry-goc/cao, api-key]
              dùng khi: Dùng khi cần tự động ráp video YouTube Shorts từ kịch bản gồm giọng đọc, video nền và phụ đề tự sinh.
              bỏ qua nếu: Bỏ qua nếu máy chưa cài FFmpeg và ImageMagick hoặc không có API key để sinh giọng đọc.
  DỰ PHÒNG  : mcps/scrptly - Scrptly Video Generator [da-doc-entry-goc/cao, api-key,tra-phi]
== data-dashboard  (cụm: dashboard, báo cáo)
  CHÍNH     : agents/anbinh-travel-ops-analyst/skills/data-storytelling - Data Storytelling [da-doc-entry-goc/vua, none]
              dùng khi: Dùng khi cần biến số liệu thô thành báo cáo chứa thông tin cốt lõi và hành động cụ thể
              bỏ qua nếu: unknown
  DỰ PHÒNG  : skills/kpi-dashboard-creator - KPI Dashboard Creator — Build dashboard cho quyết định, không phải trang trí [da-doc-dau-entry/cao, none]

! mcps/buffer-mcp: cần khoá API -> L3
! mcps/meta-social-api: mới đọc phần đầu entry
! mcps/meta-social-api: cần khoá API -> L3
! mcps/crawl4ai: cần hạ tầng
! mcps/firecrawl: mới đọc phần đầu entry
! mcps/firecrawl: cần khoá API -> L3
! repos/yasgu: cần khoá API -> L3
! mcps/scrptly: tốn tiền -> L2
! mcps/scrptly: cần khoá API -> L3
! skills/kpi-dashboard-creator: mới đọc phần đầu entry
! Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
! Mở entry gốc đọc skip_if + mục Lưu ý trước khi dùng; không cài khi chưa có người duyệt.
```

### Yêu cầu vô lý, phải ra HỔNG

Lệnh: `python tools/thu_kho.py goi-y "lập trình robot hút bụi"`

```
Yêu cầu: lập trình robot hút bụi
Khả năng phát hiện: (không)

HỔNG: yêu cầu - lập trình robot hút bụi
      -> Ghi catalog/GAP-LOG.md (gap_line), không bịa ứng viên.

! Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
! Mở entry gốc đọc skip_if + mục Lưu ý trước khi dùng; không cài khi chưa có người duyệt.
```

### Kế hoạch cài (không chạy gì): mcps/buffer-mcp

Lệnh: `python tools/thu_kho.py ke-hoach-cai mcps/buffer-mcp`

```
======================================================================
CHƯA CHẠY THẬT - đây chỉ là kế hoạch đọc từ entry. Không có lệnh nào được thực thi. Cần người duyệt trước khi cài.
======================================================================
Mục: mcps/buffer-mcp - buffer-mcp — Schedule Social Media Posts Qua Claude (Buffer GraphQL)
Entry gốc: mcps/buffer-mcp.md (đã đọc)
Mức duyệt cần: L3
   - cài tool nội bộ/dự án: L1 (ghi log)
   - chạm khoá/credential (đặt/đổi khoá, cấp quyền) -> L3: hỏi CEO TRƯỚC khi làm
Điều kiện tiên quyết: cần git, pip, python | THIẾU: không
Biến môi trường/khoá (chỉ tên): BUFFER_ACCESS_TOKEN[chưa đặt]
Cờ rủi ro:
   [khoa-api] Cần khoá/token API - tạo, đặt, đổi khoá là việc L3 (CEO).
Các bước (CHƯA CHẠY):
  1. [chep-file] git clone https://github.com/jakemeany523/buffer-mcp
  2. [dieu-huong] cd buffer-mcp
  3. [cai-goi] pip install mcp httpx pydantic
  4. [dat-bien-moi-truong] export BUFFER_ACCESS_TOKEN="<GIA_TRI_KHOA>"
  5. [lenh-khac] python3 server.py
  6. [sua-cau-hinh] {
         "mcpServers": {
           "buffer": {
             "command": "python3",
             "args": ["/path/to/buffer-mcp/server.py"],
             "env": { "BUFFER_ACCESS_TOKEN": "<GIA_TRI_KHOA>" }
           }
         }
       }
  7. [lenh-dung-thu] "Schedule post lên X/Twitter lúc 9am sáng mai:
  8. [lenh-dung-thu] 'Vừa khám phá agent-skills của @addyosmani —
  9. [lenh-dung-thu] 24 skills senior engineer distilled thành Claude Code plugin.
  10. [lenh-dung-thu] Link trong bio #vibecoding #claudecode'"
  11. [lenh-dung-thu] "Schedule video announcement cho tất cả channels lúc 7pm:
  12. [lenh-dung-thu] Facebook: [caption dài, formal]
  13. [lenh-dung-thu] Instagram: [caption ngắn + hashtags]
  14. [lenh-dung-thu] X: [thread 3 tweets]
  15. [lenh-dung-thu] LinkedIn: [professional angle]"
  16. [lenh-dung-thu] "Lấy content calendar tuần này từ Airtable/Notion →
  17. [lenh-dung-thu] schedule tất cả posts lên Buffer theo đúng time"
  18. [lenh-dung-thu] "Get top 5 posts performance tuần trước trên từng platform"
  19. [lenh-dung-thu] "Platform nào có engagement rate cao nhất tháng này?"
Kiểm PASS/FAIL: PASS nếu lệnh kiểm chạy xong không lỗi VÀ đầu ra khớp ví dụ trong entry; FAIL nếu lỗi, thiếu công cụ, hoặc kết quả khác ví dụ (ghi lý do, bỏ mục đó).
   Ví dụ trong entry: ```bash # Schedule 1 post "Schedule post lên X/Twitter lúc 9am sáng mai: 'Vừa khám phá agent-skills của @addyosmani — 24 skills senior engineer distilled thành Claude Code plugin. Link trong bio #vibecoding #claudecode'" # Cross-platform scheduling "Schedule video announcement cho tất cả channels lúc 7pm: Facebook: [caption dài, formal] Instagram: [caption ngắn + hashtags] X: [thread 3 tweets] LinkedIn: [professional angle]" # Content calendar "Lấy content calendar tuần này từ Airtable/Notion → 
   Lệnh kiểm gợi ý: git --version
Gỡ cài (gợi ý, người tự làm):
   - khôi phục file cấu hình từ bản sao lưu (sao lưu trước khi sửa)
   - bỏ biến môi trường 'BUFFER_ACCESS_TOKEN' (xoá khỏi .env/profile)
   - pip uninstall mcp
   - xoá thư mục 'buffer-mcp' (người tự làm, kiểm kỹ đường dẫn trước khi xoá)
! Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
! Bỏ qua nếu: Bỏ qua nếu không có tài khoản Buffer hoặc không có mã BUFFER_ACCESS_TOKEN.
Lằn ranh đỏ: AI không tự chi tiền; AI không tự publish public content; AI không tự cam kết với khách
CHƯA CHẠY THẬT. Chờ người duyệt (L3) rồi mới cài.
```

### Kế hoạch cài: mcps/crawl4ai

Lệnh: `python tools/thu_kho.py ke-hoach-cai mcps/crawl4ai`

```
======================================================================
CHƯA CHẠY THẬT - đây chỉ là kế hoạch đọc từ entry. Không có lệnh nào được thực thi. Cần người duyệt trước khi cài.
======================================================================
Mục: mcps/crawl4ai - Crawl4AI MCP — Cào Web Free Không Giới Hạn
Entry gốc: mcps/crawl4ai.md (đã đọc)
Mức duyệt cần: L1
   - cài tool nội bộ/dự án: L1 (ghi log)
Điều kiện tiên quyết: cần docker, node | THIẾU: không
Cờ rủi ro:
   [license] License chưa ghi trong kho - kiểm trước khi dùng cho khách.
   [ha-tang] adoption = can-ha-tang (VPS/docker/DB/nhiều bước).
Các bước (CHƯA CHẠY):
  1. [chay-docker] docker run -d -p 11235:11235 --name crawl4ai --shm-size=1g unclecode/crawl4ai:latest
  2. [sua-cau-hinh] {
         "mcpServers": {
           "crawl4ai": {
             "command": "npx",
             "args": ["-y", "mcp-crawl4ai"]
           }
         }
       }
Kiểm PASS/FAIL: PASS nếu lệnh kiểm chạy xong không lỗi VÀ đầu ra khớp ví dụ trong entry; FAIL nếu lỗi, thiếu công cụ, hoặc kết quả khác ví dụ (ghi lý do, bỏ mục đó).
   Lệnh kiểm gợi ý: docker --version
Gỡ cài (gợi ý, người tự làm):
   - khôi phục file cấu hình từ bản sao lưu (sao lưu trước khi sửa)
   - docker stop + docker rm container đã tạo (người tự làm)
! Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
! Bỏ qua nếu: Bỏ qua nếu không thể chạy Docker Desktop nền hoặc máy có RAM trống dưới 4GB.
Lằn ranh đỏ: AI không tự chi tiền; AI không tự publish public content; AI không tự cam kết với khách
CHƯA CHẠY THẬT. Chờ người duyệt (L1) rồi mới cài.
```

### Dòng GAP-LOG sinh ra (chưa ghi vào file)

Lệnh: `python tools/thu_kho.py ghi-gap "viết email lạnh tiếng Việt" --du-an "Khách sạn A" --ghi-chu "nhãn chỉ có billionmail (máy chủ gửi mail), không có công cụ soạn email lạnh"`

```
| 2026-10-17 | viết email lạnh tiếng Việt | Khách sạn A | thu_kho tim; capability: email-outreach; từ khoá: viet email lanh tieng viet | nhãn chỉ có billionmail (máy chủ gửi mail), không có công cụ soạn email lạnh | mở |
```

## Truy vấn trả kết quả kém và đã sửa gì (nhật ký thật khi tự kiểm)

Các lỗi dưới đây thấy khi chạy vòng đầu của 8 truy vấn; mỗi dòng ghi cái đã đổi trong `tools/thu_kho.py`:

| Triệu chứng thấy được | Nguyên nhân | Đã sửa |
|---|---|---|
| "báo cáo dashboard" kích hoạt thêm khả năng `scraping` | Cụm đồng nghĩa "cào" đơn lẻ, khi bỏ dấu thành "cao", trùng với "báo cáo" | Bỏ "cào" đơn khỏi bảng; chỉ giữ "cào web", "cào dữ liệu", "cào trang" |
| Từ "cao" (của "cào") khớp rác vào "độ tin cậy cao..." | Từ nằm trong cụm nhiều từ đã khớp capability vẫn được tính như từ khoá thường | Từ trong cụm capability có trọng số 0.6 thay vì 1.0 |
| "cào web đối thủ" đưa `repos/researchtikpy` (TikTok Research API) lên đầu | Xếp hạng theo `curation_status` trước, mục `da-doc-entry-goc` thắng dù chỉ khớp capability, không khớp chữ | Thêm "bậc khớp" (so với mục khớp nhất): thứ tự AGENT-ROUTER chỉ phân xử giữa các mục khớp ngang nhau; tăng trọng số khớp chữ |
| "đăng bài Facebook có lịch" đưa `tiktok-mcp` lên trên `meta-social-api` | Như trên, và "facebook" chỉ là từ thường | Tên nền tảng (facebook, zalo, tiktok, hubspot, n8n...) có trọng số 2.5 |
| "chatbot Zalo" đưa `sentiment-classifier` lên đầu | Như trên | Cùng bản sửa (tên nền tảng); `zalo-channel-connection-guide` lên đầu |
| Yêu cầu dài ("kênh Facebook: cào web..., đăng bài..., video ngắn...") ra cùng một mục (`researchtikpy`) cho mọi khả năng | Dùng cả câu làm từ khoá cho từng khả năng, từ khoá của việc này chọn nhầm việc kia | `recommend` tách yêu cầu theo dấu phẩy/chấm phẩy/"và", mỗi khả năng chỉ tra bằng đoạn nhắc tới nó |
| "lập trình robot hút bụi" ra `repos/maxun` thay vì HỔNG | Khớp theo đầu từ 3 ký tự: "bui" ⊂ "build" | Khớp theo đầu từ chỉ từ 4 ký tự; ngưỡng bao phủ từ khoá cho truy vấn không có capability là 0.6 |
| Có dấu và không dấu ra danh sách khác nhau | Lúc đầu có phạt khi gõ có dấu mà mục chỉ khớp sau khi bỏ dấu | Bỏ phạt; có test so sánh cho 4 truy vấn |
| "viết email lạnh" không thấy mục tiếng Anh `cold-email` | Entry viết tiếng Anh ("cold email"), truy vấn tiếng Việt | Thêm bảng mở rộng Việt→Anh (email lạnh → cold, outreach...); thêm phần "Thêm (chưa gắn nhãn)" vì 460 skill chưa nhãn bị ẩn mặc định |
| "Thêm (chưa gắn nhãn)" lòi mục không liên quan (vd "CRM" ra mục compliance) | Ngưỡng bao phủ cho mục chưa nhãn quá lỏng (0.6) | Nâng lên 0.68 |

## Điểm yếu còn lại (không sửa được trong phạm vi này)

1. **Truy vấn 7 và 8 vẫn kém.** Nguyên nhân ở dữ liệu nhãn, không phải ở công cụ: chỉ có 2 mục gắn `email-outreach`; `data-dashboard` gồm cả skill đặc thù dự án (Trùm Sân Bay) cạnh công cụ tổng quát và công cụ không có tín hiệu để phân biệt hai loại. Cần người duy trì gắn nhãn thêm (đặc biệt 460 skill chưa nhãn), hoặc thêm cột "phạm vi" (tổng quát / đặc thù dự án) vào catalog.
2. **Chỉ lọc được điều kiện đã có trong nhãn.** "Không GPU" loại mục `needs: gpu`, không loại mục không khai báo gì.
3. **Bộ khớp là heuristic.** Từ lạ, viết tắt, tiếng lóng sẽ trượt. Không có tìm kiếm ngữ nghĩa/embedding.
4. **Không có tín hiệu dùng thật** (USAGE-LOG trống), nên xếp hạng chỉ phản ánh độ chắc của nhãn đọc, không phản ánh chất lượng công cụ.
5. **`vessel_fit` rỗng** (5 mục có nhãn + 460 chưa nhãn) hiện kèm ghi chú "chưa rõ" nhưng vẫn lọt vào kết quả khi lọc vessel.
