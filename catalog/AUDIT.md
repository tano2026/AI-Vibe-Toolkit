# AUDIT — KIỂM TOÁN TỰ ĐỘNG TOÀN KHO

> Sinh tự động bằng `tools/audit_kho.py`. Đừng sửa tay. Dữ liệu đầy đủ: `catalog/audit.json`.
> Chạy lúc 2026-10-17 16:21 UTC, 916 mục, 224 giây, có mạng (chỉ-đọc).

## Đọc trước khi tin

- **Kết quả này KHÔNG chứng minh công cụ chạy đúng.** Kiểm toán chỉ đọc file, parse cú pháp và hỏi mạng chỉ-đọc (GitHub còn sống không, gói có trên npm/PyPI/Docker Hub không). Không mục nào được cài hay chạy: mọi mục đều `chua_chay_that: true`. `cai-duoc-o-day` nghĩa là *điều kiện cần* được đáp ứng (có lệnh cài hợp lệ, gói tồn tại, máy này có công cụ), không nghĩa là công cụ chạy tốt.
- `dung-duoc-ngay` = tài liệu/prompt/skill thuần, tĩnh sạch (không lộ khoá, không file hỏng). Chưa ai kiểm skill đó có hiệu quả.
- Link GitHub trả 404 có thể là repo đổi tên hay chuyển riêng tư, không chắc đã chết hẳn. 403/429/timeout ghi `chua-xac-dinh`.
- Cột lý do có mã: `LO_KHOA`, `FILE_THIEU`... (hong); `GH_LINK_CHET`, `GOI_KHONG_TIM_THAY`, `NHAN_MAU_THUAN_*` (nghi-ngo); `THIEU_*` (thieu-dieu-kien).

## 1. Đếm theo loại và usable

| Loại | dung-duoc-ngay | cai-duoc-o-day | thieu-dieu-kien | nghi-ngo | hong | chua-xac-dinh | Tổng |
|---|---|---|---|---|---|---|---|
| mcp | 0 | 13 | 34 | 7 | 0 | 1 | 55 |
| repo | 39 | 121 | 84 | 22 | 0 | 8 | 274 |
| stack | 8 | 5 | 1 | 0 | 0 | 4 | 18 |
| skill-kho | 19 | 4 | 3 | 1 | 0 | 0 | 27 |
| skill-import | 338 | 26 | 5 | 12 | 0 | 79 | 460 |
| skill-agent | 73 | 0 | 6 | 3 | 0 | 0 | 82 |
| **Tổng** | **477** | **169** | **133** | **45** | **0** | **92** | **916** |

## 2. Theo capability (chỉ mục đã gắn nhãn)

| Capability | dung-duoc-ngay | cai-duoc-o-day | thieu-dieu-kien | nghi-ngo | hong | chua-xac-dinh | Tổng |
|---|---|---|---|---|---|---|---|
| prompt-skill-library | 70 | 26 | 5 | 2 | 0 | 0 | 103 |
| reference | 46 | 12 | 5 | 3 | 0 | 0 | 66 |
| video-generation | 7 | 10 | 31 | 8 | 0 | 2 | 58 |
| agent-framework | 9 | 13 | 24 | 7 | 0 | 0 | 53 |
| productivity | 9 | 20 | 16 | 4 | 0 | 3 | 52 |
| video-render | 3 | 29 | 12 | 2 | 0 | 3 | 49 |
| agent-orchestration-memory | 7 | 19 | 15 | 3 | 0 | 3 | 47 |
| web-research | 16 | 11 | 12 | 2 | 0 | 0 | 41 |
| content-writing | 28 | 6 | 5 | 1 | 0 | 0 | 40 |
| devops | 7 | 7 | 12 | 1 | 0 | 1 | 28 |
| front-end | 1 | 17 | 6 | 0 | 0 | 1 | 25 |
| social-media | 9 | 3 | 9 | 3 | 0 | 0 | 24 |
| design-ui | 9 | 13 | 0 | 1 | 0 | 1 | 24 |
| voice-tts | 0 | 9 | 11 | 1 | 0 | 2 | 23 |
| security-compliance | 9 | 5 | 4 | 1 | 0 | 0 | 19 |
| backend | 2 | 6 | 10 | 0 | 0 | 0 | 18 |
| data-dashboard | 7 | 5 | 4 | 1 | 0 | 0 | 17 |
| document-office | 2 | 8 | 4 | 2 | 0 | 0 | 16 |
| local-llm | 2 | 7 | 6 | 1 | 0 | 0 | 16 |
| image-generation | 4 | 0 | 8 | 3 | 0 | 0 | 15 |
| browser-automation | 0 | 7 | 2 | 3 | 0 | 1 | 13 |
| ads | 5 | 1 | 3 | 0 | 0 | 1 | 10 |
| scraping | 0 | 6 | 4 | 0 | 0 | 0 | 10 |
| crm-sales | 4 | 2 | 1 | 2 | 0 | 1 | 10 |
| customer-support | 6 | 1 | 2 | 1 | 0 | 0 | 10 |
| database | 0 | 3 | 4 | 0 | 0 | 1 | 8 |
| seo | 4 | 2 | 1 | 1 | 0 | 0 | 8 |
| finance-accounting | 0 | 4 | 3 | 0 | 0 | 0 | 7 |
| ticketing-aviation | 6 | 0 | 1 | 0 | 0 | 0 | 7 |
| email-outreach | 0 | 1 | 1 | 0 | 0 | 0 | 2 |

## 3. Link chết hay gói không tìm thấy (22 dòng chính làm mục thành nghi-ngo, 12 dòng phụ; liệt kê 30 đầu, chính trước)

| Mục | Mã | Chi tiết |
|---|---|---|
| `mcps/google-flow-mcp` | GH_LINK_CHET | repo GitHub chính joshuadaniel-8090/google-flow-mcp trả 404 (link chết/đổi tên/riêng tư) |
| `mcps/google-workspace-mcp` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: @trypear/gws |
| `mcps/hubspot-mcp` | GH_LINK_CHET | repo GitHub chính ZLeventer/hubspot-mcp trả 404 (link chết/đổi tên/riêng tư) |
| `mcps/pollinations-mcp` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: pollinations-mcp |
| `mcps/sequential-thinking` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: @modelcontextprotocol/server-sequentialthinking |
| `mcps/youtube-upload` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: @evolsb/claude-code-google-workspace |
| `repos/chatwoot` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: devlikeapro/waha-plus |
| `repos/hermes-jev-skills` | GH_LINK_CHET | repo GitHub chính maxkilla/hermes-jev-skills trả 404 (link chết/đổi tên/riêng tư) |
| `repos/hermes-jev-skills` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: hermes-jev |
| `repos/open-seo` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: open-seo-mcp |
| `repos/penpot` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: @penpot/mcp-server |
| `repos/prime-agent` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: prime-agent |
| `repos/printfilm-research-notes` | GH_LINK_CHET | repo GitHub chính yuanzhongqiao/printfilm trả 404 (link chết/đổi tên/riêng tư) |
| `repos/sceneworks` | GH_LINK_CHET | repo GitHub chính TiniXXX/SceneWorks trả 404 (link chết/đổi tên/riêng tư) |
| `repos/skillops` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: skops |
| `skills/bumblebee-skill` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: bumblebee-scanner |
| `skills/hyperframes-skill` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: @hyperframes/cli, @heygen/hyperframes |
| `skills/just-scrape` | GOI_KHONG_TIM_THAY | gói cài không có trên registry: @scrapegraphai/just-scrape |
| `skills/last30days-skill` | GH_LINK_CHET | repo GitHub chính last30days/last30days trả 404 (link chết/đổi tên/riêng tư) |
| `skills/marketing-automation-mcp-guide` | GH_LINK_CHET | repo GitHub chính ZLeventer/hubspot-mcp trả 404 (link chết/đổi tên/riêng tư) |
| `skills/recsys-pipeline-architect` | GH_LINK_CHET | repo GitHub chính mturac/recsys-pipeline-architect trả 404 (link chết/đổi tên/riêng tư) |
| `skills/token-budget-advisor` | GH_LINK_CHET | repo GitHub chính Xabilimon1/Token-Budget-Advisor-Claude-Code trả 404 (link chết/đổi tên/riêng tư) |
| `mcps/crawl4ai` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: @unclecode/crawl4ai-mcp (entry còn lệnh cài khác có gói tồn tại) |
| `mcps/markitdown-mcp` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: markitdown-mcp (entry còn lệnh cài khác có gói tồn tại) |
| `mcps/mcp-youtube` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: @modelcontextprotocol/server-youtube (entry còn lệnh cài khác có gói tồn tại) |
| `mcps/minimax-mcp` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: mmx-cli (entry còn lệnh cài khác có gói tồn tại) |
| `repos/billionmail` | GH_LINK_CHET_PHU | repo GitHub phụ nicholasgasior/billionmail trả 404 |
| `repos/higgsfield-mcp-unified` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: higgsfield-mcp (entry còn lệnh cài khác có gói tồn tại) |
| `repos/markitdown` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: markitdown-mcp (entry còn lệnh cài khác có gói tồn tại) |
| `repos/page-agent` | GOI_PHU_KHONG_TIM_THAY | gói phụ không có trên registry: page-agent-mcp (entry còn lệnh cài khác có gói tồn tại) |

## 4. Mục nghi lộ khoá bí mật (0)

Chỉ ghi loại và dòng; giá trị đã che. Cần mở file đối chiếu bằng mắt (có thể là khoá mẫu trong tài liệu).

_Không phát hiện._

## 5. Mục nhãn mâu thuẫn với entry (17; mỗi mục 1 căn cứ)

| Mục | Mâu thuẫn |
|---|---|
| `agents/company/skills/hermes-autonomous-kho-maintenance` | nhãn needs=api-key; căn cứ: entry không nhắc khoá/token/đăng nhập |
| `agents/media-pro/skills/cross-channel-distribution-analysis` | nhãn needs=api-key; căn cứ: entry không nhắc khoá/token/đăng nhập |
| `agents/trum-san-bay/skills/social-publisher` | nhãn needs=api-key; căn cứ: entry không nhắc khoá/token/đăng nhập |
| `mcps/notebooklm-mcp-secure` | nhãn needs=api-key; căn cứ: entry không nhắc khoá/token/đăng nhập |
| `repos/ai-shorts-generator-pipeline` | nhãn needs=vps; căn cứ: entry không nhắc VPS/máy chủ/deploy |
| `repos/deepseek-r1-local` | nhãn needs=none; căn cứ: entry ghi “mạnh nhất chạy nổi trên máy cá nhân (32B/70B) vẫn cần GPU cao cấp (RTX 4090/dual-GPU) — máy văn phòng thườn” |
| `repos/funasr` | nhãn needs=none; căn cứ: entry ghi “ua kiểm. - Model flagship `Fun-ASR-Nano` bắt buộc cần GPU — trên VPS Tencent Cloud hiện tại (theo cấu hình” |
| `repos/langflow` | nhãn needs=api-key; căn cứ: entry không nhắc khoá/token/đăng nhập |
| `repos/markitdown` | nhãn needs=none; căn cứ: entry ghi “ext, links / / **Images** / OCR + AI description (cần API key) / / **Audio** / Transcription (Whisper) / / **CS” |
| `repos/mem0` | nhãn needs=none; căn cứ: entry ghi “tier có giới hạn. Self-host free unlimited nhưng cần OpenAI key.” |
| `repos/odysseus` | nhãn needs=docker; căn cứ: entry không hề nhắc docker/container |
| `repos/openclaw` | nhãn needs=none; căn cứ: entry ghi “Skills chạy trên máy mày → review trước khi cài - Cần API key của LLM (Claude/OpenAI/v.v.) - Windows: dùng Wind” |
| `repos/pi-coding-agent` | nhãn needs=none; căn cứ: entry ghi “ro/Max hoặc ChatGPT Plus/Pro qua `/login` thay vì bắt buộc API key. ## Setup từng bước 1. Cài global: ```bash npm” |
| `repos/seedance-2-5` | nhãn needs=api-key; căn cứ: entry không nhắc khoá/token/đăng nhập |
| `repos/srt-whiteboard-animation` | nhãn needs=none; căn cứ: entry ghi “o AI thật vào giữa các cảnh vẽ tay. Phức tạp hơn, cần GPU/SAM 3 nếu bật segmentation. ## Setup từng bước (” |
| `repos/ui-tars-desktop` | nhãn needs=none; căn cứ: entry ghi “tốn nhiều token hơn text tasks - Chạy local model cần GPU đủ mạnh ## Đánh giá cá nhân - Điểm mạnh: ByteDan” |
| `repos/videofy-minimal` | nhãn needs=tra-phi; căn cứ: entry không nhắc phí/giá/credit |

## 6. Dùng ngay / cài được ở đây, tốt nhất theo capability

Xếp theo: điểm trong entry (nếu có), độ tin cậy nhãn, `cai-ngay-duoc`. Điểm là điểm sau khi ĐỌC, không phải sau khi DÙNG.

| Capability | Mục | Usable | Điểm | Cách cài |
|---|---|---|---|---|
| ads | `agents/digital-marketing-agent/skills/ad-budget-testing-discipline` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| ads | `skills/ai-marketing-adoption-map` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| ads | `agents/digital-marketing-agent/skills/digital-marketing-orchestrator` | dung-duoc-ngay |  | chep-file/prompt-thuan |
| agent-framework | `repos/pydantic-ai` | cai-duoc-o-day | 9.0 | pip |
| agent-framework | `repos/swarms` | cai-duoc-o-day | 9.0 | tai-ma-nguon, pip, can-api-key |
| agent-framework | `repos/yc-qm` | cai-duoc-o-day | 8.5 | npx-mot-lenh |
| agent-orchestration-memory | `mcps/codebase-memory-mcp` | cai-duoc-o-day | 9.0 | tai-ma-nguon, npm |
| agent-orchestration-memory | `repos/gstack` | cai-duoc-o-day | 9.0 | tai-ma-nguon, npm |
| agent-orchestration-memory | `repos/swarms` | cai-duoc-o-day | 9.0 | tai-ma-nguon, pip, can-api-key |
| backend | `repos/supabase` | cai-duoc-o-day | 9.0 | tai-ma-nguon, can-docker, npm |
| backend | `repos/pydantic-ai` | cai-duoc-o-day | 9.0 | pip |
| backend | `repos/system-design-primer` | dung-duoc-ngay | 8.0 | tai-ma-nguon |
| browser-automation | `repos/agent-browser` | cai-duoc-o-day | 9.0 | npm, npx-mot-lenh, can-browser |
| browser-automation | `repos/page-agent` | cai-duoc-o-day | 8.0 | npm, npx-mot-lenh |
| browser-automation | `repos/tiktokautouploader` | cai-duoc-o-day | 7.0 | pip |
| content-writing | `agents/content-pro/skills/content-pillar-cluster-architecture` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| content-writing | `agents/content-pro/skills/content-strategy-review-gate` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| content-writing | `agents/content-pro/skills/contrarian-insight-structure` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| crm-sales | `agents/sales-ceo/skills/deal-scoring-forecast-discipline` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| crm-sales | `repos/knowledge-work-plugins` | cai-duoc-o-day | 8.5 | claude-mcp-add |
| crm-sales | `skills/small-business-skills` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| customer-support | `agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| customer-support | `agents/company/skills/zalo-channel-connection-guide` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| customer-support | `agents/customer-satisfaction-pro/skills/critical-path-briefing` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| data-dashboard | `repos/google-timesfm` | cai-duoc-o-day | 8.0 | pip |
| data-dashboard | `repos/gods-eye-view` | cai-duoc-o-day | 8.0 | can-build, tai-ma-nguon, can-browser |
| data-dashboard | `repos/claude-household-cfo` | cai-duoc-o-day | 7.5 | tai-ma-nguon |
| database | `repos/supabase` | cai-duoc-o-day | 9.0 | tai-ma-nguon, can-docker, npm |
| database | `repos/qdrant` | cai-duoc-o-day | 8.5 | can-docker, pip |
| database | `repos/turbovec` | cai-duoc-o-day |  | can-docker, pip |
| design-ui | `agents/designer-pro/skills/design-quality-gate` | dung-duoc-ngay | 10.0 | chep-file/prompt-thuan |
| design-ui | `agents/designer-pro/skills/sales-marketing-collateral-production` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| design-ui | `agents/designer-pro/skills/visual-template-formula-core` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| devops | `agents/infra-ops-agent/skills/dev-automation-discipline` | dung-duoc-ngay | 10.0 | chep-file/prompt-thuan |
| devops | `agents/infra-ops-agent/skills/destructive-command-guardrail` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| devops | `agents/infra-ops-agent/skills/production-signal-feedback-loop` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| document-office | `repos/paddleocr` | cai-duoc-o-day | 9.0 | pip |
| document-office | `repos/stirling-pdf` | cai-duoc-o-day | 9.0 | can-docker |
| document-office | `repos/claude-financial-modeling-skill` | cai-duoc-o-day | 8.0 | tai-ma-nguon |
| email-outreach | `repos/founder-skills` | cai-duoc-o-day | 5.0 | tai-ma-nguon, npx-mot-lenh |
| finance-accounting | `repos/claude-financial-modeling-skill` | cai-duoc-o-day | 8.0 | tai-ma-nguon |
| finance-accounting | `repos/claude-household-cfo` | cai-duoc-o-day | 7.5 | tai-ma-nguon |
| finance-accounting | `repos/ai-berkshire` | cai-duoc-o-day | 7.0 | can-build, tai-ma-nguon, can-api-key |
| front-end | `repos/archify` | cai-duoc-o-day | 8.0 | npx-mot-lenh |
| front-end | `repos/iztro` | cai-duoc-o-day | 8.0 | npm |
| front-end | `repos/hallmark` | cai-duoc-o-day | 8.0 | tai-ma-nguon |
| image-generation | `agents/designer-pro/skills/image-prompt-formula-core` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| image-generation | `agents/designer-pro/skills/brand-image-prompt-engineer` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| image-generation | `repos/awesome-gpt-image-2` | dung-duoc-ngay | 7.0 | tai-ma-nguon |
| local-llm | `repos/chattts` | cai-duoc-o-day | 8.0 | can-build, tai-ma-nguon |
| local-llm | `repos/claude-code-router` | cai-duoc-o-day | 8.0 | npm |
| local-llm | `repos/google-timesfm` | cai-duoc-o-day | 8.0 | pip |
| productivity | `repos/yt-dlp` | cai-duoc-o-day | 10.0 | pip |
| productivity | `agents/company/skills/skill-lifecycle-management` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| productivity | `mcps/codebase-memory-mcp` | cai-duoc-o-day | 9.0 | tai-ma-nguon, npm |
| prompt-skill-library | `agents/designer-pro/skills/design-quality-gate` | dung-duoc-ngay | 10.0 | chep-file/prompt-thuan |
| prompt-skill-library | `agents/company/skills/skill-lifecycle-management` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| prompt-skill-library | `agents/content-pro/skills/content-strategy-review-gate` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| reference | `agents/company/skills/zalo-channel-connection-guide` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| reference | `agents/sales-ceo/skills/ceo-decision-lens` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| reference | `agents/sales-ceo/skills/forward-deployed-engineer-model` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| scraping | `repos/agent-reach` | cai-duoc-o-day | 8.5 | pip |
| scraping | `repos/mediacrawler` | cai-duoc-o-day | 8.0 | can-build, tai-ma-nguon |
| scraping | `repos/maxun` | cai-duoc-o-day | 7.5 | tai-ma-nguon, can-docker, can-browser |
| security-compliance | `agents/shorts-affiliate-system/skills/compliance-gate` | dung-duoc-ngay | 10.0 | chep-file/prompt-thuan |
| security-compliance | `agents/infra-ops-agent/skills/dev-automation-discipline` | dung-duoc-ngay | 10.0 | chep-file/prompt-thuan |
| security-compliance | `agents/infra-ops-agent/skills/destructive-command-guardrail` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| seo | `agents/content-pro/skills/content-pillar-cluster-architecture` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| seo | `agents/yt-cashcow/skills/trend-scout` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| seo | `agents/digital-marketing-agent/skills/digital-marketing-orchestrator` | dung-duoc-ngay |  | chep-file/prompt-thuan |
| social-media | `agents/shorts-affiliate-system/skills/platform-disclosure-adapter` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| social-media | `agents/yt-cashcow/skills/platform-disclosure-adapter` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| social-media | `agents/media-pro/skills/media-performance-discipline` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| ticketing-aviation | `repos/ai-travel-agent-templates` | dung-duoc-ngay | 8.0 | can-build, tai-ma-nguon |
| ticketing-aviation | `agents/anbinh-travel-ops-analyst/skills/aviation-policy-lookup` | dung-duoc-ngay |  | chep-file/prompt-thuan |
| ticketing-aviation | `agents/anbinh-travel-ops-analyst/skills/ota-content-strategy` | dung-duoc-ngay |  | chep-file/prompt-thuan |
| video-generation | `agents/content-pro/skills/video-narrative-structure` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| video-generation | `repos/claude-video` | cai-duoc-o-day | 8.0 | tai-ma-nguon, pip |
| video-generation | `repos/seedance-2-0-skill-os` | dung-duoc-ngay | 8.0 |  |
| video-render | `agents/brandscan/skills/human-footage-editor` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| video-render | `agents/company/skills/ffmpeg-media-toolkit` | dung-duoc-ngay | 8.0 | chep-file/prompt-thuan |
| video-render | `repos/product-film-skill` | cai-duoc-o-day | 8.0 | tai-ma-nguon |
| voice-tts | `repos/vieneu-tts` | cai-duoc-o-day | 9.0 | pip |
| voice-tts | `repos/chattts` | cai-duoc-o-day | 8.0 | can-build, tai-ma-nguon |
| voice-tts | `repos/kokoro-82m` | cai-duoc-o-day | 8.0 | pip |
| web-research | `repos/yt-dlp` | cai-duoc-o-day | 10.0 | pip |
| web-research | `agents/research-analytics-pro/skills/ceo-stress-test-and-roadmap` | dung-duoc-ngay | 9.0 | chep-file/prompt-thuan |
| web-research | `repos/agent-reach` | cai-duoc-o-day | 8.5 | pip |

## 7. Hồ sơ máy đã dùng để kết luận

| Công cụ | Có | Phiên bản |
|---|---|---|
| git | có | git version 2.54.0.windows.1 |
| node | có | v24.15.0 |
| npm | có | 11.12.1 |
| npx | có | 11.12.1 |
| python | có | Python 3.14.4 |
| pip | có | pip 26.2.1 from C:\Users\Nguyen Ngoc Tan\AppData\Roaming\Python\Python314\site-p |
| docker | có | Docker version 29.6.2, build dfc4efb |
| ffmpeg | có | ffmpeg version 8.1.2-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the F |
| gh | không |  |
| bash | có | GNU bash, version 5.3.9(1)-release (x86_64-pc-cygwin) |
| uv | có | uv 0.11.32 (3010295ae 2026-07-23 x86_64-pc-windows-msvc) |
| uvx | có | uvx 0.11.32 (3010295ae 2026-07-23 x86_64-pc-windows-msvc) |
| pipx | không |  |
| go | không |  |
| cargo | không |  |
| make | không |  |
| cmake | không |  |
| claude | có | 2.1.288 (Claude Code) |
| nvidia-smi | không |  |
| jq | không |  |
| curl | có | curl 8.19.0 (x86_64-w64-mingw32) libcurl/8.19.0 Schannel zlib/1.3.2 brotli/1.2.0 |
| bun | có | 1.3.14 |
| pnpm | có | 11.15.0 |
| pandoc | không |  |
| java | không |  |

- Docker daemon trả lời: False; GPU NVIDIA: False; trình duyệt: True; là VPS: False; Claude Code: True.
- Khoá API có trong biến môi trường (chỉ tên): ANTHROPIC_API_KEY, OPENAI_API_KEY, OPENROUTER_API_KEY.

## 8. Chạy lại

```bash
python tools/audit_kho.py                       # cả hai tầng, có mạng (≈ vài phút)
python tools/audit_kho.py --offline             # chỉ tầng 0 tĩnh
python tools/audit_kho.py --only repos/         # chỉ id bắt đầu bằng tiền tố
python tools/audit_kho.py --cache .audit-cache.json   # dùng lại kết quả mạng đã chắc chắn
python tools/audit_kho.py --md-only             # chỉ sinh lại AUDIT.md từ audit.json
python tools/build_catalog.py                   # đưa kiem_tu_dong / kiem_ly_do vào CATALOG.csv + catalog.json
python -m unittest discover -s tools/tests      # test công cụ (không cần mạng)
```
