# Ghi chú Curation Lô 4 (40 mục: 121–160) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 4, toàn bộ là các repository từ `repos/500-ai-agents-projects` đến `repos/bmad-method`).
- **File kết quả:** `work/antigravity/v3/lo-4.json`.

---

## 1. Thống kê tổng quan Lô 4

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 121 đến 160 của danh sách todo. |
| **Confidence: Cao** | 22 mục (55.0%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 18 mục (45.0%) | Evidence là cụm từ giới thiệu hoặc mô tả tài liệu/danh mục/kho nguồn. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 3 mục (7.5%) | Có điều kiện ngoại cảnh thật sự (thiếu FFmpeg/Playwright, thiếu tài khoản Google API, phiên bản hệ điều hành macOS 26). |
| **skip_if: unknown** | 37 mục (92.5%) | Không có điều kiện ngoại cảnh; các khuyến cáo đầu tư tài chính, cảnh báo không tự động hoá 100%, bảo mật IAM hay quy chuẩn hành vi được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Khuyến cáo:**
   - 37 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng chỉ đạo:
     + Khuyến cáo không dùng tiền thật / rủi ro tài chính (`ai-berkshire`, `ai-hedge-fund`).
     + Lưu ý về kiến trúc / đặc tính kỹ thuật (ví dụ `Claude` không tự render video trong `awesome-claude-5-5-videos`, `DESIGN.md` chỉ là style tokens trong `awesome-design-md`).
     + Cảnh báo né AI detection không ổn định và giao diện tiếng Trung (`aiwritex`).
     + Khuyến cáo quy trình làm việc (`bmad-method`, `andrej-karpathy-skills`).
   - 3 mục có điều kiện ngoại vi thực sự:
     + `agenttube`: Yêu cầu Node.js 18+, tài khoản Google và YouTube API credentials (`Bỏ qua nếu hệ thống máy tính chưa cài đặt đầy đủ công cụ ffmpeg và các khóa kết nối API`).
     + `ai-shorts-generator-pipeline`: Cần môi trường máy chủ có FFmpeg và Playwright (`Bỏ qua nếu môi trường máy chủ thiếu phần mềm ffmpeg hoặc trình duyệt chạy tự động`).
     + `apple-container`: Cần hệ điều hành macOS 26 (`Bỏ qua nếu máy tính không sử dụng hệ điều hành macOS phiên bản 26 trở lên`).

2. **Chuẩn hoá `capability` và `needs`:**
   - `repos/agency-agents-app`: Gán đúng `["prompt-skill-library", "agent-framework"]`, `vessel_fit: ["claude-code", "hermes", "openclaw"]` (ứng dụng native quản lý persona cho coding tools).
   - `repos/agenttube`: Bổ sung `social-media` bên cạnh `video-generation`.
   - `repos/aiwritex`: Gán `["content-writing", "seo"]`, `needs: ["api-key", "vps"]`.
   - `repos/barty-motion-graphics`: Gán `["design-ui", "video-render"]`.
   - `repos/billionmail`: Gán `["email-outreach", "devops"]`.

3. **Phân bố `confidence`:**
   - 22 `cao` / 18 `vua` (đạt tỷ lệ cân bằng thực tế ~55% / 45%, loại bỏ hoàn toàn việc gắn "cao" tràn lan cho các tiêu đề/cụm từ mô tả).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có: `awesome-catalog`, `llm-gateway`, `persona-prompt-library`, `web-scraper`, `deep-research-skill`, `coding-workflow-skills`, `auto-video-pipeline`, `agent-design-guide`, `trading-agent-framework`, `job-monitoring`, `claude-marketing-skills`, `auto-short-video`, `rag-memory`, `content-marketing-stack`, `coding-behavior-prompt`, `motion-design`, `security-scanner`, `claude-skill-collections`, `design-md-reference`, `awesome-selfhosted`, `email-marketing-self-host`, `coding-workflow-frameworks`.

---
*Báo cáo Lô 4 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
