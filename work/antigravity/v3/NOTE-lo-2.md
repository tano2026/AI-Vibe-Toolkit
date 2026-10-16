# Ghi chú Curation Lô 2 (40 mục: 41–80) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 2, gồm các skill của `research-analytics-pro`, `sales-ceo`, `shorts-affiliate-system`, `trum-san-bay`, `yt-cashcow` và 8 MCP).
- **File kết quả:** `work/antigravity/v3/lo-2.json`.

---

## 1. Thống kê tổng quan Lô 2

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 41 đến 80 của danh sách todo. |
| **Confidence: Cao** | 21 mục (52.5%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 18 mục (45.0%) | Evidence là cụm mô tả năng lực hoặc hướng dẫn phương pháp. |
| **Confidence: Thấp** | 1 mục (2.5%) | `mcps/cloud-accounting-mcps` (entry quá mỏng, chỉ gồm link danh sách repo). |
| **skip_if: có điều kiện thật** | 6 mục (15.0%) | Có điều kiện ngoại cảnh thật sự (thiếu link affiliate, thiếu ffmpeg, hết credit/quota, dữ liệu nhạy cảm, codebase nhỏ). |
| **skip_if: unknown** | 34 mục (85.0%) | Không có điều kiện ngoại vi; các lưu ý là guardrail/kinh nghiệm nội bộ. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ:**
   - 34 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` vì các mục lưu ý trong file chỉ nêu quy tắc biên tập, hướng dẫn viết prompt, hoặc guardrail an toàn nội bộ (ví dụ: không spam link, không tranh cãi với khách, circuit breaker, tuổi thọ dữ liệu 18 tháng).
   - 6 mục giữ `skip_if` có điều kiện rõ ràng:
     + `affiliate-disclosure-writer`: Bỏ qua nếu video không có liên kết tiếp thị liên kết (`evidence_skip`: "Nếu video không có affiliate → bỏ qua toàn bộ skill này, không tạo description rác.").
     + `video-renderer`: Bỏ qua nếu hệ thống máy chủ chưa được cài đặt công cụ xử lý đồ họa ffmpeg (`evidence_skip`: "Yêu cầu: Node.js 22+, ffmpeg").
     + `aituber`: Bỏ qua nếu tài khoản dịch vụ đám mây AITuber đã hết số dư tín dụng để tạo video (`evidence_skip`: "Trả phí theo credit (tài khoản AITuber riêng) — check credit trước khi giao task lớn.").
     + `brave-search`: Bỏ qua nếu đã vượt quá hạn mức 2000 lượt tìm kiếm trong tháng của gói sử dụng (`evidence_skip`: "Free tier: 2,000 searches/tháng — đủ dùng cho cá nhân").
     + `claude-routines`: Bỏ qua nếu xử lý dữ liệu nhạy cảm hoặc tài khoản không đủ quyền chạy tự động (`evidence_skip`: "Không dùng cho sensitive data.").
     + `codegraph`: Bỏ qua nếu quy mô mã nguồn dự án nhỏ dưới vài trăm tệp tin (`evidence_skip`: "Chỉ đáng gắn với codebase đủ lớn (vài trăm file trở lên)").

2. **Chuẩn hoá `capability` và `needs`:**
   - `social-listening-research`: Chuyển `capability` chính thành `web-research` (lắng nghe và nghiên cứu thị trường qua mạng xã hội).
   - `content-strategy-ideation`: Đổi capability sang `["content-writing", "prompt-skill-library"]`.
   - `platform-disclosure-adapter`: Bổ sung `social-media` bên cạnh `security-compliance`.
   - `codegraph` và `codebase-memory-mcp`: Gán đúng bản chất là `agent-orchestration-memory` và `productivity`.
   - Sửa `needs` của các kỹ năng prompt thuần từ `api-key` về `none` (`compliance-gate`, `storyboard-generator`, `trend-scout`, `content-research`, `api-error-handler`).

3. **Phân bố `confidence`:**
   - Hạ từ `cao` xuống `vua` cho các mục có evidence là cụm mô tả hoặc cẩm nang phương pháp (`ceo-decision-lens`, `forward-deployed-engineer-model`, `gtm-strategy`, `negotiation-deal-structuring`, `affiliate-injector`, `brand-design-system`, `brand-discovery-session`, `brand-voice`, `media-performance-discipline`, `reply-agent-prompt`, `writer-agent-prompt`).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `synthesis-prompts`, `social-trend-research`, `source-reliability-evaluation`, `data-analysis-skills`, `sales-discipline`, `ai-disclosure-compliance`, `compliance-gate`, `promo-storyboard-pipeline`, `viral-content-research`, `brand-voice-discovery`, `brand-voice-design`, `content-strategy-planning`, `llm-gateway`, `channel-analytics`, `html-video-renderer`, `prompt-writing-chain`, `ai-video-gen`, `web-search-api`, `claude-ads-seo-plugins`, `scheduled-automation`, `accounting-mcp`, `code-graph-for-ai`.

---
*Báo cáo Lô 2 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
