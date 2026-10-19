# STARTER-KIT — Bộ đồ nghề khởi đầu (NHÁP để duyệt)

> Ngày soạn: 2026-10-17. Trạng thái: **nháp chờ duyệt**, không phải danh mục đầy đủ. Soạn từ `catalog/CATALOG.csv` (456 mục có nhãn) và `catalog/AGENT-ROUTER.md`. Dữ liệu máy đọc: `catalog/STARTER-KIT-source.json`.

## 1. Cách dùng và cảnh báo

1. Gặp việc lặp lại: tìm dòng tương ứng ở mục 2, dùng mục Chính; Dự phòng chỉ khi Chính không hợp điều kiện của khách.
2. Trước khi chạy: mở entry gốc (đường dẫn ở mục 2b), đọc lại phần Lưu ý và điều kiện cần; bảng này chỉ là bản tóm.
3. Việc không có dòng ở đây thì tra `catalog.json` theo `AGENT-ROUTER.md`; không có ứng viên đủ tốt thì ghi `GAP-LOG.md`, không bịa.
4. Không cài hay chạy gì khi chưa có người duyệt; mọi thứ gửi ra ngoài (đăng bài, gửi email, trả lời khách) phải qua người duyệt.
5. Mục chọn cho khách nào thì dùng khoá, token, tài khoản riêng của khách đó; không dùng chung giữa các khách.

**Cảnh báo trung thực.** Chưa mục nào trong bộ này từng được spike hay dùng thật (`USAGE-LOG.md` và `GAP-LOG.md` đang trống). Mức kiểm duy nhất của mọi mục là **đọc nguồn**: người soạn đã mở entry gốc và đọc phần cài đặt, lưu ý, license, đánh giá, nhưng **chưa chạy** mục nào. Nhãn trong catalog do model gắn, không phải kết luận. Mỗi mục phải qua spike 30 phút trên việc thật, ghi `USAGE-LOG.md` (dùng được / phải sửa / bỏ), rồi mới cam kết cho khách.

**Tiêu chí chọn.** (a) `curation_status`: đọc entry gốc trước, đọc đầu entry sau; (b) `adoption` khác `chi-tham-khao`; (c) độ chắc nhãn `cao` trước; (d) ưu tiên mục viết riêng cho agency trong `agents/*/skills` và `stacks/` trước `repos/`, `mcps/`; (e) tránh mục cần GPU, VPS, trả phí khi có lựa chọn không cần; (f) đã xét `skip_if`, `needs`, `rui_ro`, license; (g) loại mục entry ghi alpha/preview, hoặc license/điều khoản không dùng được thương mại, hoặc gắn cứng một thương hiệu mà không tách được. Mục `chua-gan-nhan` không được chọn vì chỉ có mô tả. Có chỗ lệch tiêu chí (a), xem mục 4.

## 2. Bảng theo việc

`C:` = cần gì. Cột Bỏ qua nếu lấy từ entry; chi tiết và câu trích nguyên văn ở mục 2b.

| Việc | Chính | Dự phòng | Cần gì | Bỏ qua nếu |
|---|---|---|---|---|
| Nghiên cứu đối thủ / thị trường (`web-research`) | `agents/research-analytics-pro/skills/competitive-intel` | `mcps/tavily-mcp` | Chính: Không cần cài; bản thân là prompt. Entry nhắc dùng Brave Search, Firecrawl, x-research và Crunchbase/LinkedIn để lấy dữ liệu nhưng không ghi vào phần điều kiện (catalog ghi needs=none) nên phải có sẵn công cụ tìm web. Dự phòng: Khoá API Tavily (đăng ký tavily.com); gói miễn phí 1.000 credit/tháng theo entry; chạy qua npx. | Chính: Entry không có mục Lưu ý hay điều kiện loại trừ. Dự phòng: Entry tự đánh giá chỉ nên dùng làm nguồn tìm thứ hai, không thay công cụ khác, và ghi chất lượng kém với truy vấn kỹ thuật/ngách. |
| Khung chủ đề nội dung và SEO (`seo`) | `agents/content-pro/skills/content-pillar-cluster-architecture` | `repos/claude-seo` | Chính: Không cần cài; prompt thuần. Cần có thông tin thật về khách (chuyên môn, câu hỏi khách hàng hay hỏi) và nơi lưu khung (Airtable/Sheet). Dự phòng: Claude Code 1.0.33 trở lên (cài bằng /plugin). Lệnh nâng cao cần DataForSEO (trả phí) hoặc Firecrawl; bản gốc dùng được không cần các tiện ích này. | Chính: Không dùng cho nội dung cần gấp trong ngày hoặc nội dung thời sự một lần. Dự phòng: Không dùng nếu agent không chạy trong Claude Code. |
| Viết caption mạng xã hội và bài dài (`content-writing`) | `repos/social-media-caption-generator` | `skills/content-research-writer` | Chính: Claude Code (clone vào ~/.claude/skills rồi gọi /social-captions); không cần khoá API. Licence MIT theo entry. Dự phòng: Không cần cài; prompt thuần. Cần mẫu giọng văn của khách nếu muốn giữ giọng gốc. | Chính: Không dùng khi đầu vào chỉ là mô tả mơ hồ, và không thay được giọng văn riêng của khách. Dự phòng: Không áp cho nội dung ngắn hằng ngày vì quá nặng. |
| Video ngắn (`video-render`) | `repos/hyperframes` | `stacks/remotion-template-factory` | Chính: Claude Code, Node.js 22+, FFmpeg (catalog ghi thêm cần trình duyệt Chromium); không cần khoá API. Dự phòng: Node.js, Remotion, biết React cơ bản để viết template đầu tiên; render cần tải Chrome Headless Shell (khoảng 300MB). Tuỳ chọn LLM để sinh dữ liệu đầu vào. | Chính: Không dùng nếu máy thiếu FFmpeg/Chromium hoặc không chạy trong Claude Code. Dự phòng: Không dùng cho video cần chỉnh tay nhiều theo cảnh quay thô, và phải xét giấy phép thương mại của Remotion. |
| Ảnh và prompt ảnh (`image-generation`) | `agents/designer-pro/skills/image-prompt-formula-core` | `mcps/pollinations-mcp` | Chính: Không cần cài; prompt thuần, cần một công cụ tạo ảnh bên ngoài chạy prompt. Code mẫu gọi Claude API qua ANTHROPIC_API_KEY (tuỳ chọn). Dự phòng: npx pollinations-mcp, không cần khoá API; license ISC cho gói MCP. | Chính: Entry không nêu điều kiện loại trừ; chỉ là công thức nên không tự tạo ảnh. Dự phòng: Không dùng cho sản phẩm cuối của khách cần chất lượng cao. |
| Giọng đọc tiếng Việt (`voice-tts`) | `repos/vieneu-tts` | `repos/elevenlabs-skills` | Chính: pip install vieneu; chạy trên máy, không khoá API. Catalog ghi cần GPU, nhưng entry nói có thể chạy CPU với precision int8 và chỉ cần máy đủ mạnh. Dự phòng: Khoá API ElevenLabs và gói trả phí; npx skills add elevenlabs/skills. Tiêu tiền theo ký tự nên đặt hạn mức trong dashboard. | Chính: Không dùng nếu máy yếu hoặc cần dịch vụ API đám mây sẵn. Dự phòng: Không dùng nếu chưa có tài khoản và khoá API trả phí. |
| Đăng mạng xã hội (`social-media`) | `mcps/meta-social-api` | `mcps/buffer-mcp` | Chính: Tài khoản nhà phát triển Meta, ứng dụng loại Business, Facebook Page, tài khoản Instagram Business/Creator liên kết, token (nên dùng System User cho môi trường chạy thật); video Reels cần URL công khai. Dự phòng: Tài khoản Buffer và BUFFER_ACCESS_TOKEN; Python với mcp, httpx, pydantic. | Chính: Không dùng nếu khách không có Page/Instagram Business hoặc không muốn quản lý token. Dự phòng: Không dùng nếu không có tài khoản Buffer hoặc không có token. |
| CRM (khách, deal, nhắc việc) (`crm-sales`) | `mcps/hubspot-mcp` | `repos/twenty-crm` | Chính: Tài khoản HubSpot và Private App token (HUBSPOT_ACCESS_TOKEN); Node.js; clone và build từ GitHub. Dự phòng: Docker, khoảng 2GB RAM trống, Postgres, đặt sau VPN; license trộn AGPL, Enterprise và MIT. | Chính: Entry không có mục Lưu ý; chỉ có cảnh báo dùng token Private App, không dùng khoá API cũ. Dự phòng: Chỉ dùng nội bộ sau VPN; chưa nên đóng gói cho khách dùng như dịch vụ khi chưa có ý kiến pháp lý. |
| Chăm sóc khách và xử lý bình luận (`customer-support`) | `agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline` | `agents/trum-san-bay/skills/sentiment-classifier` | Chính: Không cần cài; prompt thuần. Cần dữ liệu lịch sử khách để gắn cờ chính xác; ngưỡng SLA trong entry (chat 40 giây, email 4 giờ, mạng xã hội 60 phút) là mặc định, phải đối chiếu hợp đồng từng khách. Dự phòng: Prompt trong code gắn cứng một fanpage cụ thể và mẫu trả lời cụ thể nên phải viết lại cho từng khách; cần hàm đẩy hàng đợi (Airtable) và báo (Telegram), khoá API Claude. | Chính: Entry không nêu điều kiện loại trừ. Dự phòng: Không dùng nếu kênh không có bình luận mới hoặc đã xử lý tay từng phản hồi. |
| Báo cáo và dashboard (`data-dashboard`) | `agents/research-analytics-pro/skills/data-storytelling` | `skills/kpi-dashboard-creator` | Chính: Không cần cài; prompt thuần. Cần số liệu đã phân tích xong làm đầu vào. Entry nhắc EXPERT-CORE.md và sc-datav của kho nội bộ. Dự phòng: Không cần cài; hướng dẫn thiết kế, người/agent tự viết giao diện (React/Tailwind). Ví dụ trong entry gắn với dashboard nội bộ của kho. | Chính: Không dùng khi khách chỉ cần bảng số liệu thô; dùng sau khi phân tích xong. Dự phòng: Entry tự đánh giá chỉ 5/10 vì không có gì đặc thù kỹ thuật. |
| Đọc và chuyển tài liệu khách gửi (`document-office`) | `repos/markitdown` | `repos/stirling-pdf` | Chính: pip install markitdown (hoặc markitdown[all]); không cần khoá API để đổi văn bản; mô tả ảnh bằng AI cần khoá API. Dự phòng: Docker; khoảng 2GB bộ nhớ Java cho file lớn; thêm gói ngôn ngữ vie cho OCR tiếng Việt. | Chính: Entry không nêu điều kiện loại trừ; bảng định dạng chỉ ghi PDF là trích văn bản và bố cục cơ bản. Dự phòng: Không dùng nếu không chạy được Docker hoặc chỉ xử lý vài file đơn giản. |
| Cào dữ liệu web và điều khiển trình duyệt (`scraping`, `browser-automation`) | `mcps/crawl4ai` | `repos/agent-browser` | Chính: Docker Desktop chạy nền, RAM trống từ 4GB, tải image khoảng 500MB; MCP chạy qua npx mcp-crawl4ai. Dự phòng: npm install -g agent-browser rồi agent-browser install (tải Chrome for Testing); Node.js 24+ chỉ khi build từ nguồn; dùng trong Claude Code hoặc OpenClaw. | Chính: Không dùng nếu không chạy được Docker hoặc máy ít RAM. Dự phòng: Không dùng khi cần mô phỏng mạng, nhiều tab phức tạp hoặc xuất PDF. |

### 2b. Chi tiết từng mục (mức đã kiểm: **đọc nguồn**, chưa chạy)

#### 1. Nghiên cứu đối thủ / thị trường

- **Chính: `agents/research-analytics-pro/skills/competitive-intel`** (đường dẫn `agents/research-analytics-pro/skills/competitive-intel/SKILL.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Khung 4 bước (liệt kê người chơi, ma trận tính năng/giá, bản đồ định vị, rào cản) kèm mẫu báo cáo, viết riêng cho agent của agency và không cần cài gì.
  - Điều kiện cần: Không cần cài; bản thân là prompt. Entry nhắc dùng Brave Search, Firecrawl, x-research và Crunchbase/LinkedIn để lấy dữ liệu nhưng không ghi vào phần điều kiện (catalog ghi needs=none) nên phải có sẵn công cụ tìm web.
  - Nên bỏ qua nếu: Entry không có mục Lưu ý hay điều kiện loại trừ. Trích entry về công cụ bên ngoài: "Firecrawl: Scrape trang"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `mcps/tavily-mcp`** (đường dẫn `mcps/tavily-mcp.md`; đọc đầu entry, độ chắc nhãn cao; license: không nêu; needs catalog: api-key)
  - Vì sao chọn: Nguồn tìm web thứ hai để đối chiếu chéo khi cần kiểm số liệu đối thủ; có gói miễn phí.
  - Điều kiện cần: Khoá API Tavily (đăng ký tavily.com); gói miễn phí 1.000 credit/tháng theo entry; chạy qua npx.
  - Nên bỏ qua nếu: Entry tự đánh giá chỉ nên dùng làm nguồn tìm thứ hai, không thay công cụ khác, và ghi chất lượng kém với truy vấn kỹ thuật/ngách. Trích entry: "Không phải phải-có, chỉ là nice-to-have nếu cần thêm 1 nguồn search độc lập để đối chiếu chéo"
  - Mức đã kiểm: đọc nguồn.

#### 2. Khung chủ đề nội dung và SEO

- **Chính: `agents/content-pro/skills/content-pillar-cluster-architecture`** (đường dẫn `agents/content-pro/skills/content-pillar-cluster-architecture/SKILL.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Dựng khung pillar/cluster và kế hoạch liên kết nội bộ trước khi viết bài, có bảng kiểm để không chọn chủ đề thiếu thẩm quyền.
  - Điều kiện cần: Không cần cài; prompt thuần. Cần có thông tin thật về khách (chuyên môn, câu hỏi khách hàng hay hỏi) và nơi lưu khung (Airtable/Sheet).
  - Nên bỏ qua nếu: Không dùng cho nội dung cần gấp trong ngày hoặc nội dung thời sự một lần. Trích entry: "không hợp cho case cần content gấp trong ngày"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `repos/claude-seo`** (đường dẫn `repos/claude-seo.md`; đọc đầu entry, độ chắc nhãn cao; license: MIT; needs catalog: claude-code-only)
  - Vì sao chọn: Khi cần kiểm tra SEO một site thật (audit, schema, content brief, cluster từ kết quả tìm kiếm) bằng một plugin MIT thay vì tự viết quy trình.
  - Điều kiện cần: Claude Code 1.0.33 trở lên (cài bằng /plugin). Lệnh nâng cao cần DataForSEO (trả phí) hoặc Firecrawl; bản gốc dùng được không cần các tiện ích này.
  - Nên bỏ qua nếu: Không dùng nếu agent không chạy trong Claude Code. Trích entry: "Cần Claude Code — không chạy standalone, không dùng được nếu mày không có Claude Code setup."
  - Mức đã kiểm: đọc nguồn.

#### 3. Viết caption mạng xã hội và bài dài

- **Chính: `repos/social-media-caption-generator`** (đường dẫn `repos/social-media-caption-generator.md`; đọc đầu entry, độ chắc nhãn cao; license: MIT; needs catalog: none)
  - Vì sao chọn: Từ một đầu vào ra caption riêng cho từng nền tảng (Reels, TikTok, Threads, Facebook, Shorts) kèm lý do công thức, khớp việc lặp hằng tuần.
  - Điều kiện cần: Claude Code (clone vào ~/.claude/skills rồi gọi /social-captions); không cần khoá API. Licence MIT theo entry.
  - Nên bỏ qua nếu: Không dùng khi đầu vào chỉ là mô tả mơ hồ, và không thay được giọng văn riêng của khách. Trích entry: "Input tốt nhất là script/text/screenshot có nội dung rõ ràng — mô tả mơ hồ ra caption chung chung."
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `skills/content-research-writer`** (đường dẫn `skills/content-research-writer.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Cho bài dài/báo cáo/case study: bảng ghi nguồn (source ledger) để không bịa số liệu, rồi mới viết.
  - Điều kiện cần: Không cần cài; prompt thuần. Cần mẫu giọng văn của khách nếu muốn giữ giọng gốc.
  - Nên bỏ qua nếu: Không áp cho nội dung ngắn hằng ngày vì quá nặng. Trích entry (phạm vi dùng): "chỉ nên dùng cho content dài (báo cáo, bài research .md)"
  - Mức đã kiểm: đọc nguồn.

#### 4. Video ngắn

- **Chính: `repos/hyperframes`** (đường dẫn `repos/hyperframes.md`; đọc entry gốc, độ chắc nhãn cao; license: Apache 2.0; needs catalog: browser)
  - Vì sao chọn: Claude Code viết HTML rồi render ra MP4 từ kịch bản; Apache 2.0, không tính phí theo lần render, nên không vướng giấy phép thương mại.
  - Điều kiện cần: Claude Code, Node.js 22+, FFmpeg (catalog ghi thêm cần trình duyệt Chromium); không cần khoá API.
  - Nên bỏ qua nếu: Không dùng nếu máy thiếu FFmpeg/Chromium hoặc không chạy trong Claude Code. Trích entry: "Đang active development — update liên tục"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `stacks/remotion-template-factory`** (đường dẫn `stacks/remotion-template-factory.md`; đọc đầu entry, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Dựng template React một lần rồi nhét văn bản/số liệu để render hàng loạt cùng một định dạng (thẻ số liệu, intro/outro).
  - Điều kiện cần: Node.js, Remotion, biết React cơ bản để viết template đầu tiên; render cần tải Chrome Headless Shell (khoảng 300MB). Tuỳ chọn LLM để sinh dữ liệu đầu vào.
  - Nên bỏ qua nếu: Không dùng cho video cần chỉnh tay nhiều theo cảnh quay thô, và phải xét giấy phép thương mại của Remotion. Trích entry: "công ty 4+ người phải mua commercial license"
  - Mức đã kiểm: đọc nguồn.

#### 5. Ảnh và prompt ảnh

- **Chính: `agents/designer-pro/skills/image-prompt-formula-core`** (đường dẫn `agents/designer-pro/skills/image-prompt-formula-core/SKILL.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Công thức prompt 7 phần và bảng lỗi ảnh AI hay gặp (chữ méo, mặt lỗi, thiếu chỗ chèn chữ), viết trung lập thương hiệu: mỗi khách có file brand-context riêng.
  - Điều kiện cần: Không cần cài; prompt thuần, cần một công cụ tạo ảnh bên ngoài chạy prompt. Code mẫu gọi Claude API qua ANTHROPIC_API_KEY (tuỳ chọn).
  - Nên bỏ qua nếu: Entry không nêu điều kiện loại trừ; chỉ là công thức nên không tự tạo ảnh. Trích entry (điểm yếu): "bản core này trừu tượng hơn, cần đọc kèm ví dụ brand thật để hiểu đầy đủ"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `mcps/pollinations-mcp`** (đường dẫn `mcps/pollinations-mcp.md`; đọc đầu entry, độ chắc nhãn vua; license: ISC; needs catalog: none)
  - Vì sao chọn: Công cụ tạo ảnh không cần khoá API để chạy bản nháp và thumbnail thử, ghép với công thức ở trên.
  - Điều kiện cần: npx pollinations-mcp, không cần khoá API; license ISC cho gói MCP.
  - Nên bỏ qua nếu: Không dùng cho sản phẩm cuối của khách cần chất lượng cao. Trích entry: "chất lượng thấp hơn Fal.ai/Stable Diffusion, chỉ hợp draft nhanh"
  - Mức đã kiểm: đọc nguồn.

#### 6. Giọng đọc tiếng Việt

- **Chính: `repos/vieneu-tts`** (đường dẫn `repos/vieneu-tts.md`; đọc entry gốc, độ chắc nhãn cao; license: Apache-2.0; needs catalog: gpu)
  - Vì sao chọn: TTS tiếng Việt chạy offline, Apache-2.0, hỗ trợ trộn Việt-Anh và nhân bản giọng từ 3-5 giây mẫu, không tốn phí theo ký tự.
  - Điều kiện cần: pip install vieneu; chạy trên máy, không khoá API. Catalog ghi cần GPU, nhưng entry nói có thể chạy CPU với precision int8 và chỉ cần máy đủ mạnh.
  - Nên bỏ qua nếu: Không dùng nếu máy yếu hoặc cần dịch vụ API đám mây sẵn. Trích entry: "cần máy đủ mạnh để chạy mượt (dù nhẹ hơn nhiều so với tạo nhạc/video)"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `repos/elevenlabs-skills`** (đường dẫn `repos/elevenlabs-skills.md`; đọc đầu entry, độ chắc nhãn cao; license: MIT; needs catalog: api-key,tra-phi)
  - Vì sao chọn: Chính chủ ElevenLabs, một nơi lo cả đọc, phiên âm, hiệu ứng âm thanh; entry ghi có 15 giọng tiếng Việt.
  - Điều kiện cần: Khoá API ElevenLabs và gói trả phí; npx skills add elevenlabs/skills. Tiêu tiền theo ký tự nên đặt hạn mức trong dashboard.
  - Nên bỏ qua nếu: Không dùng nếu chưa có tài khoản và khoá API trả phí. Trích entry: "Code MIT không có nghĩa là audio sinh ra được dùng thương mại miễn phí."
  - Mức đã kiểm: đọc nguồn.

#### 7. Đăng mạng xã hội

- **Chính: `mcps/meta-social-api`** (đường dẫn `mcps/meta-social-api.md`; đọc đầu entry, độ chắc nhãn cao; license: không nêu; needs catalog: api-key)
  - Vì sao chọn: API chính thức của Meta: một token đăng Facebook/Instagram/Threads, lấy insight, quản lý bình luận, không qua dịch vụ trung gian.
  - Điều kiện cần: Tài khoản nhà phát triển Meta, ứng dụng loại Business, Facebook Page, tài khoản Instagram Business/Creator liên kết, token (nên dùng System User cho môi trường chạy thật); video Reels cần URL công khai.
  - Nên bỏ qua nếu: Không dùng nếu khách không có Page/Instagram Business hoặc không muốn quản lý token. Trích entry (điểm yếu): "Điểm yếu: Token management phức tạp, hay thay đổi permissions policy"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `mcps/buffer-mcp`** (đường dẫn `mcps/buffer-mcp.md`; đọc entry gốc, độ chắc nhãn vua; license: MIT; needs catalog: api-key)
  - Vì sao chọn: Lên lịch đăng nhiều nền tảng (X, LinkedIn, Facebook, Instagram, TikTok...) qua một tài khoản Buffer, đỡ tự xử lý từng API.
  - Điều kiện cần: Tài khoản Buffer và BUFFER_ACCESS_TOKEN; Python với mcp, httpx, pydantic.
  - Nên bỏ qua nếu: Không dùng nếu không có tài khoản Buffer hoặc không có token. Trích entry (điều kiện cần): "Lấy token tại buffer.com → Settings → Apps and Integrations → Create App."
  - Mức đã kiểm: đọc nguồn.

#### 8. CRM (khách, deal, nhắc việc)

- **Chính: `mcps/hubspot-mcp`** (đường dẫn `mcps/hubspot-mcp.md`; đọc đầu entry, độ chắc nhãn cao; license: MIT; needs catalog: api-key)
  - Vì sao chọn: Cho agent đọc/tạo/cập nhật contact, company, deal, danh sách và email marketing trong HubSpot mà không mở giao diện; chỉ có ý nghĩa khi khách (hoặc agency) đã dùng HubSpot.
  - Điều kiện cần: Tài khoản HubSpot và Private App token (HUBSPOT_ACCESS_TOKEN); Node.js; clone và build từ GitHub.
  - Nên bỏ qua nếu: Entry không có mục Lưu ý; chỉ có cảnh báo dùng token Private App, không dùng khoá API cũ. Trích entry (cảnh báo): "Dùng Private App Token (HubSpot Settings → Integrations → Private Apps), không dùng API key cũ đã deprecated."
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `repos/twenty-crm`** (đường dẫn `repos/twenty-crm.md`; đọc đầu entry, độ chắc nhãn cao; license: AGPL; needs catalog: none)
  - Vì sao chọn: Nếu agency cần CRM riêng thay vì thuê dịch vụ: nguồn mở, tự host, có API cho agent đọc ghi.
  - Điều kiện cần: Docker, khoảng 2GB RAM trống, Postgres, đặt sau VPN; license trộn AGPL, Enterprise và MIT.
  - Nên bỏ qua nếu: Chỉ dùng nội bộ sau VPN; chưa nên đóng gói cho khách dùng như dịch vụ khi chưa có ý kiến pháp lý. Trích entry: "KHÔNG mở cổng ra internet công khai — đặt sau VPN/Tailscale hoặc whitelist IP văn phòng"
  - Mức đã kiểm: đọc nguồn.

#### 9. Chăm sóc khách và xử lý bình luận

- **Chính: `agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline`** (đường dẫn `agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline/SKILL.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Phân biệt tín hiệu khách sắp rời bỏ (báo ngay lần đầu) với phàn nàn nhỏ, kèm ngưỡng thời gian trả lời theo kênh và cách báo cáo bằng median/P90.
  - Điều kiện cần: Không cần cài; prompt thuần. Cần dữ liệu lịch sử khách để gắn cờ chính xác; ngưỡng SLA trong entry (chat 40 giây, email 4 giờ, mạng xã hội 60 phút) là mặc định, phải đối chiếu hợp đồng từng khách.
  - Nên bỏ qua nếu: Entry không nêu điều kiện loại trừ. Trích entry: "cần data lịch sử khách (VIP/mới) để gắn cờ chính xác"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `agents/trum-san-bay/skills/sentiment-classifier`** (đường dẫn `agents/trum-san-bay/skills/sentiment-classifier/SKILL.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Phân loại bình luận mới thành khiếu nại gấp, câu hỏi, ý định mua, spam để xếp hàng xử lý; dùng làm khung nhãn.
  - Điều kiện cần: Prompt trong code gắn cứng một fanpage cụ thể và mẫu trả lời cụ thể nên phải viết lại cho từng khách; cần hàm đẩy hàng đợi (Airtable) và báo (Telegram), khoá API Claude.
  - Nên bỏ qua nếu: Không dùng nếu kênh không có bình luận mới hoặc đã xử lý tay từng phản hồi. Trích entry (quy tắc): "thà báo nhầm còn hơn bỏ sót"
  - Mức đã kiểm: đọc nguồn.

#### 10. Báo cáo và dashboard

- **Chính: `agents/research-analytics-pro/skills/data-storytelling`** (đường dẫn `agents/research-analytics-pro/skills/data-storytelling/SKILL.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Khung 'Gì - Vì sao quan trọng - Làm gì' và bố cục tóm tắt 5 phần (tối đa 3 khuyến nghị) để báo cáo cho khách có kết luận, không chỉ bảng số.
  - Điều kiện cần: Không cần cài; prompt thuần. Cần số liệu đã phân tích xong làm đầu vào. Entry nhắc EXPERT-CORE.md và sc-datav của kho nội bộ.
  - Nên bỏ qua nếu: Không dùng khi khách chỉ cần bảng số liệu thô; dùng sau khi phân tích xong. Trích entry (thời điểm dùng): "Dùng sau khi có analysis xong, trước khi present output cho user."
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `skills/kpi-dashboard-creator`** (đường dẫn `skills/kpi-dashboard-creator.md`; đọc đầu entry, độ chắc nhãn cao; license: không nêu; needs catalog: none)
  - Vì sao chọn: Khi cần dựng dashboard: quy tắc định nghĩa từng chỉ số (nguồn, tần suất, mốc so sánh) trước khi vẽ giao diện.
  - Điều kiện cần: Không cần cài; hướng dẫn thiết kế, người/agent tự viết giao diện (React/Tailwind). Ví dụ trong entry gắn với dashboard nội bộ của kho.
  - Nên bỏ qua nếu: Entry tự đánh giá chỉ 5/10 vì không có gì đặc thù kỹ thuật. Trích entry (đánh giá): "nhưng không phải capability mới"
  - Mức đã kiểm: đọc nguồn.

#### 11. Đọc và chuyển tài liệu khách gửi

- **Chính: `repos/markitdown`** (đường dẫn `repos/markitdown.md`; đọc đầu entry, độ chắc nhãn cao; license: MIT; needs catalog: none)
  - Vì sao chọn: Công cụ của Microsoft đổi PDF, Word, Excel, PowerPoint, HTML sang Markdown để agent đọc, MIT, không cần Docker.
  - Điều kiện cần: pip install markitdown (hoặc markitdown[all]); không cần khoá API để đổi văn bản; mô tả ảnh bằng AI cần khoá API.
  - Nên bỏ qua nếu: Entry không nêu điều kiện loại trừ; bảng định dạng chỉ ghi PDF là trích văn bản và bố cục cơ bản. Trích entry (phần cần khoá API): "OCR + AI description (cần API key)"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `repos/stirling-pdf`** (đường dẫn `repos/stirling-pdf.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: docker)
  - Vì sao chọn: Khi cần thao tác lên chính file PDF (gộp, tách, nén, OCR tiếng Việt, đóng dấu) mà không tải lên dịch vụ ngoài.
  - Điều kiện cần: Docker; khoảng 2GB bộ nhớ Java cho file lớn; thêm gói ngôn ngữ vie cho OCR tiếng Việt.
  - Nên bỏ qua nếu: Không dùng nếu không chạy được Docker hoặc chỉ xử lý vài file đơn giản. Trích entry: "Điểm yếu: Cần Docker để self-host; UI không đẹp bằng ILovePDF; OCR chậm với file lớn"
  - Mức đã kiểm: đọc nguồn.

#### 12. Cào dữ liệu web và điều khiển trình duyệt

- **Chính: `mcps/crawl4ai`** (đường dẫn `mcps/crawl4ai.md`; đọc entry gốc, độ chắc nhãn cao; license: không nêu; needs catalog: docker)
  - Vì sao chọn: Cào nhiều trang web rồi đổi sang Markdown cho agent đọc, tự host nên không giới hạn số trang và không tốn credit.
  - Điều kiện cần: Docker Desktop chạy nền, RAM trống từ 4GB, tải image khoảng 500MB; MCP chạy qua npx mcp-crawl4ai.
  - Nên bỏ qua nếu: Không dùng nếu không chạy được Docker hoặc máy ít RAM. Trích entry: "RAM cần ít nhất 4GB trống"
  - Mức đã kiểm: đọc nguồn.
- **Dự phòng: `repos/agent-browser`** (đường dẫn `repos/agent-browser.md`; đọc entry gốc, độ chắc nhãn cao; license: Apache-2.0; needs catalog: browser)
  - Vì sao chọn: Điều khiển trình duyệt thật bằng CLI nhẹ (Apache-2.0) để click, điền form, chụp màn hình; dùng khi cần kiểm tra trang đích của khách hoặc trang cần thao tác.
  - Điều kiện cần: npm install -g agent-browser rồi agent-browser install (tải Chrome for Testing); Node.js 24+ chỉ khi build từ nguồn; dùng trong Claude Code hoặc OpenClaw.
  - Nên bỏ qua nếu: Không dùng khi cần mô phỏng mạng, nhiều tab phức tạp hoặc xuất PDF. Trích entry: "là CLI mới của Vercel, cần theo dõi độ ổn định lâu dài"
  - Mức đã kiểm: đọc nguồn.

## 3. HỔNG (theo định dạng dòng `GAP-LOG.md`)

Chưa ghi vào `GAP-LOG.md` thật; chép các dòng dưới vào đó nếu duyệt.

| Ngày | Khả năng cần | Dự án / khách | Đã tra (domain + từ khoá) | Vì sao chưa đủ | Trạng thái (mở / đã có entry: đường dẫn) |
|---|---|---|---|---|---|
| 2026-10-17 | HỔNG: email-outreach: viết và gửi chuỗi email lạnh cho khách của agency | Bộ khởi đầu (chưa gắn dự án) | capability email-outreach, adoption khác chi-tham-khao; từ khoá cold email, outreach, newsletter | Chỉ có 2 mục được gắn nhãn: repos/billionmail cần VPS và trả phí, repos/founder-skills (outreach-specialist) tự chấm 5/10, thiên thị trường Mỹ, entry nói không cài thành bộ cho agent. Hai skill nhập hàng loạt chưa gắn nhãn (skills/cold-email cần khoá MachFive, skills/outbound-engine trỏ đường dẫn máy cục bộ) chưa được đọc kỹ nên không chọn. | mở |
| 2026-10-17 | HỔNG: document-office: soạn tài liệu giao khách (đề xuất, báo giá, slide) dạng .docx/.pptx | Bộ khởi đầu (chưa gắn dự án) | capability document-office, adoption khác chi-tham-khao; từ khoá docx, pptx, proposal | repos/genoffice ghi rõ bản alpha, qua hạ tầng bên thứ ba và chỉ nên dùng nội bộ; repos/markitdown và repos/stirling-pdf chỉ đọc/xử lý file, không soạn tài liệu mới. Chưa thấy mục nào đủ tốt để giao cho khách. | mở |
| 2026-10-17 | HỔNG: data-dashboard: dựng dashboard báo cáo cho khách từ dữ liệu quảng cáo/mạng xã hội | Bộ khởi đầu (chưa gắn dự án) | capability data-dashboard, adoption khác chi-tham-khao | Các mục đã đọc đều là khung tư duy/quy trình: skills/data-analyzer (6/10), skills/analytics-data-analysis (chuẩn viết code phân tích), skills/kpi-dashboard-creator (5/10). Chưa có mục nối trực tiếp dữ liệu quảng cáo/mạng xã hội của khách ra báo cáo hoặc dashboard định kỳ. Bộ đã chọn chỉ lo phần viết báo cáo. | mở |

## 4. Chọn nhưng còn nghi ngờ

Những mục dưới đây nằm trong bảng vì chưa có lựa chọn tốt hơn, nhưng nên spike kỹ hoặc hỏi chủ agency trước.

- `agents/research-analytics-pro/skills/competitive-intel` (Chính, nghiên cứu đối thủ / thị trường): Entry không nêu rõ cách lấy dữ liệu khi thiếu công cụ tìm web; số liệu đối thủ phải tự kiểm.
- `mcps/tavily-mcp` (Dự phòng, nghiên cứu đối thủ / thị trường): Entry ghi rate limit gói miễn phí hay chạm trần và chuyện Nebius mua lại chưa chốt, có thể đổi giá/chính sách.
- `repos/claude-seo` (Dự phòng, khung chủ đề nội dung và seo): Entry viết giọng quảng bá (chấm 9/10, 'không bàn'), số sao/kết quả lấy từ README, chưa ai trong kho chạy. Catalog gắn rủi ro dữ liệu/ToS và tốn tiền nhưng entry không giải thích vì sao.
- `repos/social-media-caption-generator` (Chính, viết caption mạng xã hội và bài dài): Entry phần lớn trích lời tác giả repo (tài khoản 280K follower, tiết kiệm 30 phút/bài), chưa có kết quả độc lập; caption tiếng Việt chưa được kiểm.
- `repos/hyperframes` (Chính, video ngắn): Catalog gắn rủi ro 'tốn tiền' nhưng entry ghi miễn phí, Apache 2.0, không tính phí per-render; cần xem lại khi spike. Chưa có bằng chứng chất lượng video thực tế.
- `stacks/remotion-template-factory` (Dự phòng, video ngắn): Giấy phép: agency từ 4 người trở lên phải mua license thương mại của Remotion theo chính entry; cần chủ agency quyết trước khi chọn. Ví dụ trong entry gắn thương hiệu cụ thể nhưng kỹ thuật dùng chung được.
- `mcps/pollinations-mcp` (Dự phòng, ảnh và prompt ảnh): Entry không nói điều khoản dùng ảnh sinh ra cho mục đích thương mại; mâu thuẫn nội bộ (mục đầu 'không giới hạn', mục sau 'chỉ hợp draft'). Chưa chọn được công cụ tạo ảnh chất lượng cao: google-flow-mcp bị loại vì Alpha, fal-mcp cần trả phí và chưa được xét.
- `repos/vieneu-tts` (Chính, giọng đọc tiếng việt): Catalog ghi needs=gpu còn entry cho thấy chạy CPU được, cần đo thực tế. Nhân bản giọng cần có sự đồng ý của người có giọng: entry không nhắc, đây là lưu ý của người soạn bộ này.
- `repos/elevenlabs-skills` (Dự phòng, giọng đọc tiếng việt): Entry ghi gói miễn phí bị khoá khi người kiểm đi qua proxy và chưa nghe được chất lượng giọng Việt; quyền thương mại theo gói chưa kiểm.
- `mcps/meta-social-api` (Chính, đăng mạng xã hội): Code mẫu dùng Graph API v19.0, cần đối chiếu tài liệu hiện hành. Entry ghi Threads API còn hạn chế. Mỗi khách một token riêng: không dùng chung.
- `mcps/buffer-mcp` (Dự phòng, đăng mạng xã hội): Entry mỏng, không có mục Lưu ý và không nói giá/giới hạn của Buffer; mô tả là GraphQL nhưng đoạn code mẫu gọi đường dẫn kiểu REST, cần đối chiếu. Mã nguồn bên thứ ba.
- `mcps/hubspot-mcp` (Chính, crm (khách, deal, nhắc việc)): Mã nguồn bên thứ ba (không phải của HubSpot), entry mỏng, không nêu chi phí HubSpot. Công cụ có thể lên lịch gửi email marketing: đặt quy tắc phải có người duyệt trước khi gửi.
- `repos/twenty-crm` (Dự phòng, crm (khách, deal, nhắc việc)): Entry ghi nhiều lỗ hổng bảo mật 2026 và chính nó nói chưa chạy thử thật. Ví dụ trong entry gắn thương hiệu cụ thể nhưng sản phẩm dùng chung.
- `agents/trum-san-bay/skills/sentiment-classifier` (Dự phòng, chăm sóc khách và xử lý bình luận): Mục vốn gắn thương hiệu (viết cho một fanpage): chỉ mượn khung nhãn và ngưỡng, không dùng nguyên văn. Không tự trả lời bình luận khi chưa có người duyệt.
- `skills/kpi-dashboard-creator` (Dự phòng, báo cáo và dashboard): Chủ yếu là tư duy thiết kế chung, không đưa ra công cụ dashboard cho khách; xem mục HỔNG.
- `repos/markitdown` (Chính, đọc và chuyển tài liệu khách gửi): Số sao và xếp hạng trong entry là lời quảng bá, chưa kiểm chất lượng với tài liệu tiếng Việt hay PDF quét.
- `repos/stirling-pdf` (Dự phòng, đọc và chuyển tài liệu khách gửi): Entry không ghi license (catalog cũng để trống); cần xem LICENSE trước khi dùng cho việc của khách. Tag image trong entry cần kiểm lại.
- `mcps/crawl4ai` (Chính, cào dữ liệu web và điều khiển trình duyệt): Catalog gắn rủi ro 'tốn tiền' nhưng entry ghi miễn phí, cần xem lại khi spike. Entry không nói gì về điều khoản trang đích hay robots.txt; cào dữ liệu đối thủ/khách phải tự cân nhắc.
- `repos/agent-browser` (Dự phòng, cào dữ liệu web và điều khiển trình duyệt): Entry chỉ nói về kiểm thử giao diện của chính ứng dụng; dùng để cào hoặc thao tác trên site người khác là suy luận của người soạn, entry không đề cập. Phương án khác cùng nhóm: mcps/playwright.

**Chỗ lệch tiêu chí hoặc phải phán đoán.**

- `repos/social-media-caption-generator` (đọc đầu entry) được chọn làm Chính thay cho `skills/content-research-writer` (đọc entry gốc), vì mục sau tự nói không dùng cho nội dung ngắn hằng ngày.
- `mcps/meta-social-api` (đọc đầu entry) làm Chính thay cho `mcps/buffer-mcp` (đọc entry gốc) vì entry Buffer mỏng, không có phần lưu ý, không nói giá hay giới hạn.
- `repos/markitdown` (đọc đầu entry, không cần Docker) làm Chính thay cho `repos/stirling-pdf` (đọc entry gốc, cần Docker) theo tiêu chí tránh hạ tầng.
- `agents/content-pro/skills/content-pillar-cluster-architecture` làm Chính cho SEO thay cho `repos/claude-seo` vì nằm trong `agents/*/skills`, đọc entry gốc, không phụ thuộc Claude Code; `claude-seo` giữ làm dự phòng khi cần audit site thật.
- Việc CRM chỉ có nghĩa nếu có CRM đã chọn; entry không cho biết agency hoặc khách đang dùng gì, nên cả hai mục đều có điều kiện.

**Đã đọc và loại** (không đưa vào bộ):

- `repos/genoffice`: Bản alpha, nội dung đi qua hạ tầng bên thứ ba, entry chỉ cho dùng nội bộ. Trích entry: "bản alpha do đúng 1 kỹ sư build trong 1 tuần"
- `mcps/google-flow-mcp`: Entry ghi trạng thái Alpha trên PyPI; ngoài ra cần trả phí cho video. Trích entry: "Development Status: 3 - Alpha"
- `repos/capcut-tts-api`: API không chính thức (dịch ngược), có thể ngừng hoạt động và vướng điều khoản của CapCut; license chưa rõ. Trích entry: "Khong phai API chinh thuc"
- `repos/kokoro-82m`: Không hỗ trợ tiếng Việt. Trích entry: "Tiếng Việt không hỗ trợ"
- `repos/founder-skills`: Entry tự đánh giá 5/10 và khuyên không cài thành bộ cho agent (thiên thị trường Mỹ, 5 tháng không cập nhật). Trích entry: "Không cài thành bộ cho agent"

**Lệch giữa catalog và entry** (cần sửa nhãn nếu spike xác nhận): `repos/vieneu-tts` catalog ghi `gpu` nhưng entry cho thấy chạy CPU được; `repos/hyperframes` và `mcps/crawl4ai` catalog ghi rủi ro `tốn tiền` nhưng entry ghi miễn phí. Chưa sửa `curation.json`.

## 5. Quy trình cập nhật

1. Spike 30 phút trên một việc thật cho một mục, ghi `USAGE-LOG.md` với kết quả `dùng được` / `phải sửa` / `bỏ` và số giờ tiết kiệm cụ thể. Chỉ chép dòng cũ vào đây sau khi có dòng log.
2. Mục `bỏ` hoặc `phải sửa` nặng: chuyển Dự phòng lên Chính, hoặc ghi dòng HỔNG nếu không còn ứng viên.
3. Việc mới lặp lại từ 3 lần trở lên mà chưa có dòng: tra theo `AGENT-ROUTER.md`, đọc entry gốc, rồi thêm dòng mới cùng lúc vào bảng này và `STARTER-KIT-source.json`.
4. Mỗi dòng HỔNG có entry mới thì sửa cột trạng thái ở `GAP-LOG.md` và bỏ khỏi mục 3.
5. Mỗi khi `catalog.json` sinh lại, kiểm các id trong bộ này còn tồn tại và nhãn (`needs`, `skip_if`, `adoption`) chưa đổi; mỗi quý rà lại các mục chưa có dòng log.
