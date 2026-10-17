# Ghi chú Curation Lô 10 (38 mục: 361–398) — Antigravity

- **Tổng số mục:** 38/38 mục (`curation-todo-398.json` Lô 10, gồm 22 skill từ `skills/ai-second-brain` đến `skills/voxstyle-prompt-engine` và 16 stack từ `stacks/10-buoc-thiet-ke-agentic-ai` đến `stacks/video-factory-auto-router`).
- **File kết quả:** `work/antigravity/v3/lo-10.json`.

---

## 1. Thống kê tổng quan Lô 10

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 38 mục | Đủ 38 mục từ mục 361 đến 398 của danh sách todo (lô cuối cùng). |
| **Confidence: Cao** | 23 mục (60.5%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 15 mục (39.5%) | Evidence là mệnh đề, cụm giới thiệu hoặc cấu trúc ngữ pháp tương quan/mô tả chức năng. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 3 mục (7.9%) | Có điều kiện ngoại cảnh thật sự (claude-dashboards-motion, genmedia-labs-runcomfy, just-scrape). |
| **skip_if: unknown** | 35 mục (92.1%) | Không có điều kiện ngoại vi; các hướng dẫn sử dụng, chốt xin duyệt an toàn, bối cảnh chạy máy cá nhân được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Hướng dẫn triển khai:**
   - 35 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng quy chuẩn:
     + Lưu ý cài đặt Obsidian local hoặc các gói phụ trợ phổ biến (`ai-second-brain`, `second-brain-obsidian-claude`).
     + Chốt an toàn xin duyệt trước khi gửi thao tác thật (`small-business-skills`, `day-chuyen-4-agent-claude-code`).
     + Ngữ cảnh chạy máy cá nhân thay vì VPS 24/7 (`antigravity-mirage-remotion-combo`).
     + Rào cản định dạng khuôn mẫu hoặc kịch bản 6 cảnh (`stickman-video-director`).
   - 3 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `skills/claude-dashboards-motion`: Bỏ qua nếu tài khoản Claude chưa đăng ký gói trả phí Team hoặc Enterprise để mở tính năng Motion (Evidence: "Điểm cần nhớ: **Motion chỉ có ở gói Team và Enterprise**, Dashboards cho gói trả phí.")
     + `skills/genmedia-labs-runcomfy`: Bỏ qua nếu chưa có tài khoản RunComfy có số dư tín dụng để chi trả theo lượt yêu cầu (Evidence: "Cần tài khoản RunComfy + trả phí theo request (không free).")
     + `skills/just-scrape`: Bỏ qua nếu tài khoản ScrapeGraphAI không còn hạn mức tín dụng để thực hiện trích xuất dữ liệu (Evidence: "Trả phí theo credit ScrapeGraphAI, không free — cân đối lượng gọi khi research nhiều tool 1 lúc.")

2. **Chuẩn hoá `capability` và `needs`:**
   - `skills/brand-identity-factory`: Gán đúng `["content-writing", "design-ui"]`, `needs: ["none"]`.
   - `skills/claude-dashboards-motion`: Gán đúng `["data-dashboard", "video-generation"]`, `needs: ["api-key"]`.
   - `skills/just-scrape`: Chuẩn hóa gán `["web-research", "browser-automation"]` (loại bỏ nhãn không hợp lệ `scraping`).
   - `stacks/antigravity-mirage-remotion-combo`: Gán đúng `["video-render", "video-generation"]`, `needs: ["none"]`.
   - `stacks/saas-stack-2026`: Gán đúng `["reference", "backend"]`, `needs: ["none"]`.
   - `stacks/video-factory-auto-router`: Gán đúng `["video-generation", "video-render"]`, `needs: ["none"]`.

3. **Phân bố `confidence`:**
   - 23 `cao` / 15 `vua` (đạt tỷ lệ cân bằng chuẩn 60.5% / 39.5%, phản ánh chính xác cấu trúc ngữ pháp và bằng chứng xác thực).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `rag-memory`, `data-dashboard`, `coding-workflow-skills`, `branding-skills`, `content-marketing-stack`, `higgsfield-fal-genmedia`, `web-scraper`, `crm-connector`, `auto-video-pipeline`, `design-md-reference`, `coding-workflow-frameworks`, `saas-boilerplate`.

---
*Báo cáo Lô 10 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
