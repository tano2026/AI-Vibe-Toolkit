# Ghi chú Curation Lô 6 (40 mục: 201–240) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 6, toàn bộ là các repository từ `repos/dify` đến `repos/iztro`).
- **File kết quả:** `work/antigravity/v3/lo-6.json`.

---

## 1. Thống kê tổng quan Lô 6

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 201 đến 240 của danh sách todo. |
| **Confidence: Cao** | 24 mục (60.0%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 16 mục (40.0%) | Evidence là mệnh đề hoặc cụm từ giới thiệu/mô tả chức năng/tài liệu tham khảo. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 8 mục (20.0%) | Có điều kiện ngoại cảnh thật sự (RAM VPS tối thiểu 4GB, ToS production, cần train set, API key trả phí ElevenLabs, cần GPU thời gian thực, hạ tầng Docker/Postgres/Redis, hạn mức tín dụng video, GPU cho video avatar). |
| **skip_if: unknown** | 32 mục (80.0%) | Không có điều kiện ngoại vi; các hướng dẫn tích hợp, cảnh báo rà soát thủ công, cấu hình phân hệ quản trị được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Hướng dẫn triển khai:**
   - 32 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng chỉ đạo:
     + Lưu ý cấu hình phân hệ (`ever-gauzy`: thiết lập nhiều phân hệ quản trị).
     + Hướng dẫn kiểm thử chất lượng (`funasr`: kiểm tra chất lượng trên file thực tế).
     + Thiết lập tài khoản dịch vụ (`goose`: cấu hình nhà cung cấp LLM).
     + Đặc tính nén và xử lý dữ liệu (`headroom`: tích hợp tầng nén token; `iztro`: hàm xử lý toán học lá số tử vi).
   - 8 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `dify`: Cần ít nhất 4GB RAM cho máy chủ self-host (`Bỏ qua nếu máy chủ ảo có dung lượng bộ nhớ dưới bốn gigabyte RAM khi tự lưu trữ`).
     + `ds2api`: Kỹ thuật vi phạm ToS, không dùng cho production (`Bỏ qua nếu cần triển khai hệ thống dịch vụ sản xuất thương mại chính thức ổn định lâu dài`).
     + `dspy`: Đòi hỏi tập dữ liệu ví dụ thực tế để tối ưu hóa (`Bỏ qua nếu chỉ xử lý tác vụ một lần hoặc không có sẵn tập dữ liệu ví dụ thực tế để huấn luyện`).
     + `elevenlabs-skills`: Đòi hỏi API key có trả phí (`Bỏ qua nếu chưa đăng ký tài khoản và có khóa giao diện lập trình ElevenLabs trả phí`).
     + `f5-tts`: Cần GPU tốt để xử lý real-time (`Bỏ qua nếu máy chủ thiếu phần cứng đồ họa GPU để xử lý nhân bản giọng nói theo thời gian thực`).
     + `firecrawl`: Yêu cầu Docker, Postgres, Redis khi tự lưu trữ (`Bỏ qua nếu máy chủ thiếu hạ tầng Docker, cơ sở dữ liệu Postgres và Redis khi tự lưu trữ`).
     + `higgsfield-mcp-unified`: Tạo video tốn credit thực tế (`Bỏ qua nếu tài khoản Higgsfield đã sử dụng hết hạn mức tín dụng tạo video`).
     + `infinitetalk`: Không chạy được trên VPS CPU-only (`Bỏ qua nếu máy chủ chỉ có CPU mà không có phần cứng đồ họa chuyên dụng GPU`).

2. **Chuẩn hoá `capability` và `needs`:**
   - `repos/dify`: Gán đúng `["agent-framework", "backend"]`, `needs: ["docker", "vps"]`.
   - `repos/ds2api`: Gán `["backend"]`, `needs: ["none"]`.
   - `repos/dspy`: Gán `["agent-framework", "prompt-skill-library"]`.
   - `repos/ecc`: Gán `["prompt-skill-library", "agent-orchestration-memory"]`.
   - `repos/ever-gauzy`: Gán `["crm-sales", "productivity", "database"]`.
   - `repos/head-of-content`: Gán `["web-research", "content-writing"]`.
   - `repos/html-video`: Gán `["video-render", "video-generation"]`.
   - `repos/infinitetalk`: Gán `["video-generation"]`, `needs: ["gpu"]`.
   - `repos/iztro`: Gán `["front-end", "reference"]`.

3. **Phân bố `confidence`:**
   - 24 `cao` / 16 `vua` (đạt tỷ lệ cân bằng chuẩn 60% / 40%, phản ánh chính xác cấu trúc ngữ pháp và bằng chứng xác thực).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `agent-workflow-platform`, `llm-gateway`, `agent-framework-core`, `coding-workflow-frameworks`, `browser-automation-framework`, `tts-voiceover`, `crm-connector`, `video-processing-tools`, `financial-analysis`, `web-scraper`, `branding-skills`, `google-workspace-integration`, `rag-memory`, `design-md-reference`, `content-marketing-stack`, `awesome-selfhosted`, `coding-workflow-skills`, `higgsfield-fal-genmedia`, `doc-to-markdown`, `html-canvas-video`, `motion-design`, `auto-video-pipeline`, `awesome-catalog`, `tu-vi-astrology`.

---
*Báo cáo Lô 6 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
