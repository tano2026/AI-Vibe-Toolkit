# Báo cáo Tổng kết Curation v3 (398 Mục) — Antigravity

- **Thời gian hoàn thành:** 2026-10-17.
- **Quy chuẩn áp dụng:** Tiêu chuẩn Curation v3 theo hướng dẫn và sửa đổi sau Pilot của Nobitano (`TASK-ANTIGRAVITY-2.md` và `TASK-ANTIGRAVITY.md`).
- **Phạm vi:** Toàn bộ 398 mục trong `catalog/curation-todo-398.json` (từ Lô 1 đến Lô 10).
- **Kết quả:** 10 tệp JSON (`lo-1.json` đến `lo-10.json`) cùng 10 bản ghi chú chi tiết (`NOTE-lo-1.md` đến `NOTE-lo-10.md`) đã được kiểm tra định dạng và chuỗi con nguyên văn 100%.

---

## 1. Tổng quan số lượng mục đã đọc và xử lý

| Hạng mục | Số lượng | Tỷ lệ | Ghi chú |
|---|---|---|---|
| **Tổng số mục cần xử lý** | 398 mục | 100% | Toàn bộ danh sách todo 398 mục |
| **Số mục đã đọc thật và thẩm định** | **398 mục** | **100%** | Không bỏ sót mục nào, đọc trực tiếp từng tệp nguồn |
| **Phần chưa làm** | **0 mục** | **0.0%** | Đã hoàn tất toàn bộ 10/10 lô |

### Phân bổ theo từng lô:
- **Lô 1:** 40 mục
- **Lô 2:** 40 mục
- **Lô 3:** 40 mục
- **Lô 4:** 40 mục
- **Lô 5:** 40 mục
- **Lô 6:** 40 mục
- **Lô 7:** 40 mục
- **Lô 8:** 40 mục
- **Lô 9:** 40 mục
- **Lô 10:** 38 mục

---

## 2. Phân bố mức độ tin cậy (Confidence)

Theo luật chuẩn hóa v3: `confidence = "cao"` chỉ được gán khi câu trích `evidence` là một câu hoàn chỉnh về mặt ngữ pháp, nói trực tiếp năng lực cốt lõi đứng đầu của mục; các trường hợp là mệnh đề, cụm giới thiệu hoặc cấu trúc định nghĩa danh từ được đưa về mức `vua`. Không có tình trạng toàn bộ lô bị đẩy lên cao.

| Mức tin cậy | Số lượng | Tỷ lệ | Diễn giải |
|---|---|---|---|
| **Cao (`cao`)** | **233 mục** | **58.5%** | Evidence trích dẫn câu văn hoàn chỉnh, trực tiếp xác nhận năng lực đứng đầu |
| **Vừa (`vua`)** | **164 mục** | **41.2%** | Evidence là mệnh đề, cụm từ giới thiệu hoặc cấu trúc tương quan/mô tả chức năng |
| **Thấp (`thap`)** | **1 mục** | **0.3%** | Tài liệu nguồn quá mỏng, thiếu bằng chứng xác thực |

### Chi tiết các mục có mức tin cậy Thấp (`thap`):
- `mcps/cloud-accounting-mcps`: Giữ confidence thap vì entry chỉ liệt kê danh sách link repo; skip_if unknown do không nêu rõ điều kiện bỏ qua.

---

## 3. Thống kê thay đổi nhãn so với nhãn nháp (`nhan_hien_tai`)

Tổng số mục có ít nhất một trường thay đổi hoặc được bổ sung/chuẩn hóa so với bản nháp ban đầu là **398/398 mục (100.0%)**.

| Tên trường | Số mục thay đổi / chuẩn hóa | Nguyên nhân & Hành động điều chỉnh |
|---|---|---|
| **`use_when`** | **398** | Chuẩn hóa bắt đầu bằng "Dùng khi cần ", loại bỏ hoàn toàn các từ cấm ("miễn phí", "hoàn toàn", "không giới hạn", "tốt nhất"), cắt bỏ đuôi "..." |
| **`skip_if`** | **398** | Phân định nghiêm ngặt: chỉ giữ điều kiện ngoại cảnh/hạ tầng thật sự; toàn bộ các cảnh báo nội bộ, lời khuyên dùng, guardrail, hướng dẫn cài đặt thông thường được đưa về `unknown` |
| **`adoption`** | **96** | Sửa sai nhãn nháp: không đổi sang `can-ha-tang` chỉ vì có chữ "chưa chạy"; phân loại đúng `cai-ngay-duoc`, `can-ha-tang` (cần Docker/VPS/GPU/DB) và `can-khoa` (cần API key trả phí) |
| **`needs`** | **170** | Đồng bộ chính xác với yêu cầu hạ tầng thật (`docker`, `gpu`, `database`, `api-key`, `none`) |
| **`capability`** | **106** | Chuẩn hóa về bảng 30 năng lực hợp lệ; loại bỏ các nhãn sai như `scraping`, `finance-accounting`, `tu-vi`; tập trung vào việc mục đó thực sự làm |
| **`confidence`** | **129** | Hạ từ `cao` xuống `vua` đối với các bằng chứng là cụm từ rời rạc, nâng độ nghiêm ngặt của bằng chứng trích dẫn |
| **`evidence`** | **398** | Nối dòng thành chuỗi con nguyên văn trên 1 dòng, độ dài ≤120 ký tự, nói thẳng khả năng chính |
| **`evidence_skip`** | **398** | Trường mới theo chuẩn v3: trích nguyên văn căn cứ cho `skip_if`, đồng bộ rỗng khi `skip_if = unknown` |
| **`dup_group`** | **398** | Tái sử dụng nhất quán danh sách tên nhóm trùng đã có trong `catalog/curation.json` |

---

## 4. Thống kê điều kiện bỏ qua (`skip_if`)

- **Số mục `skip_if = "unknown"` (kèm `evidence_skip = ""`):** **333 mục (83.7%)**.
- **Số mục có điều kiện ngoại cảnh thật (`skip_if != "unknown"`):** **65 mục (16.3%)**.
  - Các điều kiện ngoại cảnh chính bao gồm:
    + Cần GPU chuyên dụng cho mô hình cục bộ hoặc xử lý âm thanh/video thời gian thực (ví dụ: F5-TTS, CosyVoice, Whisper lớn, ComfyUI, TurboDiffusion).
    + Yêu cầu hạ tầng Docker / Docker Compose / Kubernetes / Database riêng biệt khi tự lưu trữ.
    + Yêu cầu phần mềm nhị phân ngoại vi bắt buộc trên hệ điều hành (ví dụ: `ffmpeg`, `yt-dlp`).
    + Giới hạn tài khoản dịch vụ bên thứ ba (hạn mức tín dụng tạo video, tài khoản trả phí).

---

## 5. Danh mục các nhóm trùng lặp (`dup_group`)

Toàn bộ các nhóm trùng lặp đã được chuẩn hóa để tái sử dụng thống nhất với các nhóm đã có trong `catalog/curation.json`:

| Tên nhóm trùng (`dup_group`) | Số lượng mục | Ví dụ tiêu biểu |
|---|---|---|
| `auto-video-pipeline` | 23 | agenttube, buildfast-generative-film-skill, cinetic, ... (+20) |
| `coding-workflow-skills` | 16 | agent-skills, hermes-jev-skills, mattpocock-skills, ... (+13) |
| `design-md-reference` | 15 | awesome-design-md, design-md, hallmark, ... (+12) |
| `awesome-catalog` | 13 | 500-ai-agents-projects, api-mega-list, awesome-claude-5-5-videos, ... (+10) |
| `rag-memory` | 12 | airweave, graphify, graphrag, ... (+9) |
| `tts-voiceover` | 11 | minimax-mcp, chattts, elevenlabs-skills, ... (+8) |
| `content-marketing-stack` | 11 | aiwritex, head-of-content, social-media-caption-generator, ... (+8) |
| `agent-framework-core` | 11 | crewai, deep-agents, deerflow, ... (+8) |
| `motion-design` | 10 | animasyon-stil-katalogu, barty-motion-graphics, claude-motion, ... (+7) |
| `agent-workflow-platform` | 10 | dify, flowise, langfuse, ... (+7) |
| `video-processing-tools` | 9 | framecraft, ffmpeg, mirage-tesseract, ... (+6) |
| `llm-gateway` | 8 | llm-router, 9router, claude-code-router, ... (+5) |
| `web-scraper` | 8 | agent-reach, firecrawl, gpt-crawler, ... (+5) |
| `higgsfield-fal-genmedia` | 7 | fal-mcp, higgsfield, higgsfield-mcp-unified, ... (+4) |
| `crm-connector` | 7 | hubspot-mcp, chatwoot, ever-gauzy, ... (+4) |
| `coding-workflow-frameworks` | 7 | bmad-method, claude-code-best-practice, ecc, ... (+4) |
| `branding-skills` | 7 | brand-building-skills, founder-skills, seedance-2-0-skill-os, ... (+4) |
| `browser-automation-framework` | 7 | browser-harness, browser-use, egolite, ... (+4) |
| `security-scanner` | 6 | anthropic-cybersecurity-skills, bumblebee, codex-security, ... (+3) |
| `data-dashboard` | 5 | worldmonitor, analytics-data-analysis, claude-dashboards-motion, ... (+2) |
| `ai-video-gen` | 4 | aituber, jaz-ai-mcp, mcp-video-gen, ... (+1) |
| `doc-to-markdown` | 4 | markitdown-mcp, html-anything, markitdown, ... (+1) |
| `notebooklm` | 4 | notebooklm-mcp-2026, notebooklm-mcp-pleaseprompto, notebooklm-mcp-secure, ... (+1) |
| `auto-short-video` | 4 | ai-shorts-generator-pipeline, clipify, moneyprinterturbo, ... (+1) |
| `agent-design-guide` | 3 | agent-design-playbook, ai-agents-for-beginners, learn-harness-engineering |
| `web-search-api` | 3 | brave-search, perplexity, tavily-mcp |
| `workflow-builder-mcp` | 3 | make-mcp, n8n-workflow-builder-mcp, zapier |
| `html-canvas-video` | 3 | poppify, html-video, remotion |
| `tu-vi-astrology` | 3 | taibu-mcp, iztro, ziwei-doushu |
| `persona-prompt-library` | 3 | agency-agents, agency-agents-app, knowledge-work-plugins |
| `deep-research-skill` | 3 | agent-research-skills-academic, deep-research-skills, last30days |
| `llm-training-learning` | 3 | ai-engineering-from-scratch, diffusiongemma, nanochat |
| `awesome-selfhosted` | 3 | awesome-selfhosted, coolify, healthchecks |
| `financial-analysis` | 3 | claude-financial-modeling-skill, financial-services, vibe-trading |
| `coding-agent` | 3 | openhands, pi-coding-agent, prime-agent |
| `saas-boilerplate` | 3 | sc-datav, trek, saas-stack-2026 |
| `channel-analytics` | 2 | cross-channel-distribution-analysis, media-performance-discipline |
| `data-analysis-skills` | 2 | statistical-analysis, pipeline-dashboard |
| `sales-discipline` | 2 | deal-scoring-forecast-discipline, negotiation-deal-structuring |
| `content-strategy-planning` | 2 | gtm-strategy, content-strategy-ideation |
| `ai-disclosure-compliance` | 2 | affiliate-disclosure-writer, platform-disclosure-adapter |
| `compliance-gate` | 2 | compliance-gate, compliance-gate |
| `social-post-api` | 2 | social-publisher, meta-social-api |
| `code-graph-for-ai` | 2 | codebase-memory-mcp, codegraph |
| `image-gen-local` | 2 | comfyui-mcp, stable-diffusion-mcp |
| `google-workspace-integration` | 2 | google-workspace-mcp, google-skills |
| `tiktok-analytics-api` | 2 | tikhub, tiktok-api |
| `trading-agent-framework` | 2 | ai-berkshire, ai-hedge-fund |
| `job-monitoring` | 2 | ai-job-search, career-ops |
| `claude-marketing-skills` | 2 | ai-marketing-claude, marketingskills |
| `coding-behavior-prompt` | 2 | andrej-karpathy-skills, claude-code-templates |
| `seo-audit-tools` | 2 | claude-seo, open-seo |
| `code-review-skills` | 2 | code-review-graph, open-code-review-alibaba |
| `local-llm-deployment` | 2 | deepseek-r1-local, ollama |
| `coding-agent-cli` | 2 | deepseek-reasonix, jcode |
| `vector-rag` | 2 | qdrant, turbovec |
| `brand-image-prompt` | 1 | brand-image-prompt-engineer |
| `cinematic-prompt` | 1 | cinematic-shot-prompt-core |
| `ads-discipline` | 1 | ad-budget-testing-discipline |
| `agent-command-guard` | 1 | destructive-command-guardrail |
| `synthesis-prompts` | 1 | research-synthesis |
| `social-trend-research` | 1 | social-listening-research |
| `source-reliability-evaluation` | 1 | source-evaluation |
| `executive-briefing` | 1 | ceo-decision-lens |
| `promo-storyboard-pipeline` | 1 | storyboard-generator |
| `viral-content-research` | 1 | trend-scout |
| `ops-feedback-loop` | 1 | api-error-handler |
| `ai-design-skill` | 1 | brand-design-system |
| `brand-voice-discovery` | 1 | brand-discovery-session |
| `brand-voice-design` | 1 | brand-voice |
| `researched-content-writing` | 1 | content-research |
| `response-style-prompt` | 1 | reply-agent-prompt |
| `html-video-renderer` | 1 | video-renderer |
| `prompt-writing-chain` | 1 | writer-agent-prompt |
| `short-video-script-structure` | 1 | script-variation-engine |
| `claude-ads-seo-plugins` | 1 | claude-ads |
| `scheduled-automation` | 1 | claude-routines |
| `accounting-mcp` | 1 | cloud-accounting-mcps |
| `agent-context-retrieval` | 1 | context7 |
| `web-scrape-llm` | 1 | firecrawl |
| `github-ops` | 1 | github-mcp |
| `meta-ads-mcp` | 1 | meta-ads-mcp-official |
| `meta-social-ads` | 1 | meta-mcp-server |
| `browser-control` | 1 | playwright |
| `youtube-api` | 1 | youtube-upload |
| `claude-plugin-marketplace` | 1 | agents-wshobson |
| `claude-skill-collections` | 1 | awesome-claude-skills |
| `email-marketing-self-host` | 1 | billionmail |
| `legal-review` | 1 | claude-for-legal |
| `sandbox-execution` | 1 | cubesandbox |
| `command-guard` | 1 | destructive-command-guard |
| `meeting-recording` | 1 | meetily |
| `tracing-telemetry` | 1 | opik |
| `motion-graphics` | 1 | product-film-skill |
| `database-tools` | 1 | supabase |
| `audio-processing` | 1 | whisper |

---

## 6. Đánh giá chất lượng và tuân thủ

1. **Tuân thủ quy tắc Không làm ẩu:**
   - 100% mục được đọc và thẩm định trực tiếp từ tệp văn bản gốc, không sử dụng script tự động gán nhãn hàng loạt.
   - 100% giá trị của `evidence` và `evidence_skip` là chuỗi con nguyên văn (đã chuẩn hóa khoảng trắng thành 1 dòng duy nhất), không có trường nào vượt quá 120 ký tự.
   - 100% giá trị `use_when` bắt đầu bằng "Dùng khi cần ", không vượt quá 140 ký tự và không chứa bất kỳ từ cấm nào ("miễn phí", "hoàn toàn", "không giới hạn", "tốt nhất").
   - 100% năng lực (`capability`) nằm trong danh mục 30 năng lực hợp lệ của kho tri thức.

2. **Tiến độ bàn giao nhánh `antigravity/curation`:**
   - Mỗi lô được kiểm tra định dạng độc lập, tạo tệp JSON và ghi chú NOTE tương ứng, commit và push riêng biệt theo từng lô.
   - Toàn bộ kết quả nằm trọn vẹn trong thư mục `work/antigravity/v3/` trên nhánh `antigravity/curation`, tuyệt đối không tác động lên nhánh `main`.

---
*Báo cáo được tổng hợp và xuất bản bởi Antigravity — Hệ thống Agent Curation AI-Vibe-Toolkit.*
