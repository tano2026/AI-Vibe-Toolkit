# Ghi chú Curation Lô 3 (40 mục: 81–120) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 3, toàn bộ là các MCP server từ `mcps/comfyui-mcp` đến `mcps/zapier`).
- **File kết quả:** `work/antigravity/v3/lo-3.json`.

---

## 1. Thống kê tổng quan Lô 3

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 81 đến 120 của danh sách todo. |
| **Confidence: Cao** | 23 mục (57.5%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 17 mục (42.5%) | Evidence là cụm mô tả năng lực hoặc chức năng công cụ. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 12 mục (30.0%) | Có điều kiện ngoại cảnh thật sự (GPU, hạn ngạch credit, giới hạn quota API, Captcha/Cloudflare, Chrome login). |
| **skip_if: unknown** | 28 mục (70.0%) | Không có điều kiện ngoại vi; các lưu ý là hướng dẫn cấu hình hoặc guardrail an toàn. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ:**
   - 28 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` do các ghi chú chỉ là hướng dẫn cài đặt, lưu ý về chi phí pay-per-use, hoặc cơ chế bảo mật (như chia sẻ quyền Notion thủ công, kiểm duyệt app review của Meta/TikTok).
   - 12 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `comfyui-mcp`: Bỏ qua nếu máy không có GPU hoặc chưa chạy ComfyUI server.
     + `firecrawl`: Bỏ qua nếu đã sử dụng hết hạn mức 500 tín dụng cào trang hàng tháng.
     + `google-flow-mcp`: Bỏ qua nếu tài khoản chưa bật thanh toán cho tính năng tạo video trả phí.
     + `kondo`: Bỏ qua nếu không mở sẵn tab tiện ích trình duyệt Kondo hoặc chưa nâng cấp gói Business.
     + `meta-ads-mcp-official`: Bỏ qua nếu tài khoản quảng cáo Meta chưa được kích hoạt quyền truy cập tính năng beta.
     + `notebooklm-mcp-2026`: Bỏ qua nếu chưa đóng hoàn toàn trình duyệt Chrome trước khi thực hiện đăng nhập.
     + `playwright`: Bỏ qua nếu trang đích có hệ thống xác thực người máy Captcha hoặc Cloudflare quá nghiêm ngặt.
     + `sequential-thinking`: Bỏ qua nếu tác vụ quá đơn giản không đòi hỏi nhiều bước tư duy giải quyết.
     + `stable-diffusion-mcp`: Bỏ qua nếu máy tính không có phần cứng đồ họa chuyên dụng GPU hỗ trợ.
     + `wangp-kaggle`: Bỏ qua nếu tài khoản nền tảng điện toán đám mây Kaggle đã sử dụng hết hạn mức thời gian GPU.
     + `youtube-upload`: Bỏ qua nếu đã sử dụng hết hạn mức 10000 đơn vị hoạt động trong ngày của YouTube API.
     + `zapier`: Bỏ qua nếu nhu cầu tự động hóa quy mô lớn vượt quá hạn mức tác vụ hàng tháng.

2. **Chuẩn hoá `capability` và `needs`:**
   - `context7`: Đổi sang `["agent-orchestration-memory", "reference"]` (truy xuất tài liệu mới nhất làm ngữ cảnh cho agent).
   - `taibu-mcp`: Gán đúng `reference` (bộ công cụ tri thức luận giải Á Đông).
   - `meta-social-api` và `tiktok-api`: Gán đúng `social-media` thay vì chỉ reference chung chung.
   - `kondo`: Bổ sung `customer-support` và gắn `needs: ["browser", "tra-phi"]`.

3. **Phân bố `confidence`:**
   - 23 `cao` / 17 `vua`, bảo đảm phân bố thực tế theo chất lượng câu bằng chứng trích xuất được.

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có: `image-gen-local`, `agent-context-retrieval`, `higgsfield-fal-genmedia`, `web-scrape-llm`, `video-processing-tools`, `github-ops`, `google-workspace-integration`, `crm-connector`, `ai-video-gen`, `workflow-builder-mcp`, `doc-to-markdown`, `meta-ads-mcp`, `meta-social-ads`, `social-post-api`, `tts-voiceover`, `notebooklm`, `web-search-api`, `browser-control`, `html-canvas-video`, `tu-vi-astrology`, `tiktok-analytics-api`, `youtube-api`.

---
*Báo cáo Lô 3 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
