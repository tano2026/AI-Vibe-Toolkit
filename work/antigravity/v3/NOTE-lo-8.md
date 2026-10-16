# Ghi chú Curation Lô 8 (40 mục: 281–320) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 8, toàn bộ là các repository từ `repos/openhands` đến `repos/stickman-studio`).
- **File kết quả:** `work/antigravity/v3/lo-8.json`.

---

## 1. Thống kê tổng quan Lô 8

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 281 đến 320 của danh sách todo. |
| **Confidence: Cao** | 24 mục (60.0%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 16 mục (40.0%) | Evidence là mệnh đề, cụm giới thiệu hoặc cấu trúc ngữ pháp tương quan/mô tả chức năng. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 6 mục (15.0%) | Có điều kiện ngoại cảnh thật sự (openhands, openshorts, openvoice, pixelrag, sceneworks, skyvern). |
| **skip_if: unknown** | 34 mục (85.0%) | Không có điều kiện ngoại vi; các hướng dẫn sử dụng, cảnh báo bản quyền mã nguồn mở, giới hạn tính năng được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Hướng dẫn triển khai:**
   - 34 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng quy chuẩn:
     + Lưu ý cấu hình giao diện, pipeline hoặc thông số (`openmontage`, `openreel-video`, `pixelle-video`, `paddleocr`).
     + Rào cản tương thích hoặc cảnh báo phong cách/triết lý tối giản (`pi-coding-agent`, `plannotator`, `prime-agent`, `social-media-caption-generator`).
     + Lưu ý giấy phép bản quyền sao chép (`short-video-factory`: AGPL-3.0 là vấn đề pháp lý không phải lỗi hạ tầng).
   - 6 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `repos/openhands`: Bỏ qua nếu máy chủ chưa cài đặt Docker trước khi tải gói môi trường thực thi runtime (Evidence: "# Cài Docker trước, sau đó: docker pull docker.all-hands.dev/all-hands-ai/runtime:0.39-nikol")
     + `repos/openshorts`: Bỏ qua nếu máy chủ thiếu môi trường Docker Compose để tự lưu trữ dịch vụ (Evidence: "Cần Docker (MIT license, self-host qua Docker Compose)")
     + `repos/openvoice`: Bỏ qua nếu máy chủ thiếu phần cứng đồ họa chuyên dụng GPU để xử lý nhân bản giọng nói (Evidence: "- Cần GPU để chạy tốc độ hợp lý — CPU vẫn chạy được nhưng chậm hơn nhiều, không hợp cho batch lớn.")
     + `repos/pixelrag`: Bỏ qua nếu máy chủ thiếu phần cứng đồ họa chuyên dụng GPU để phục vụ mô hình nhúng hình ảnh (Evidence: "serve API tìm kiếm (cần GPU cho model embedding).")
     + `repos/sceneworks`: Bỏ qua nếu máy tính thiếu bộ xử lý đồ họa chuyên dụng GPU hỗ trợ tối thiểu 10GB VRAM để nạp mô hình (Evidence: "Load model Flux.1-schnell (Q8, ~10GB VRAM)")
     + `repos/skyvern`: Bỏ qua nếu máy chủ thiếu môi trường Docker Desktop để triển khai bản tự lưu trữ (Evidence: "Cài Docker Desktop (bản self-host chạy qua Docker).")

2. **Chuẩn hoá `capability` và `needs`:**
   - `repos/openhands`: Gán đúng `["agent-framework", "backend"]`, `needs: ["docker", "api-key"]`.
   - `repos/openmontage`: Gán đúng `["video-generation", "video-render"]`, `needs: ["none"]`.
   - `repos/openreel-video`: Gán đúng `["video-render", "front-end"]`, `needs: ["none"]`.
   - `repos/openshorts`: Gán đúng `["video-render", "video-generation"]`, `needs: ["docker"]`.
   - `repos/openvoice`: Gán đúng `["voice-tts"]`, `needs: ["gpu"]`.
   - `repos/pixelrag`: Gán đúng `["web-research", "agent-orchestration-memory"]`, `needs: ["gpu"]`.
   - `repos/product-film-skill`: Gán đúng `["video-render", "design-ui"]`, `needs: ["none"]`.
   - `repos/sceneworks`: Gán đúng `["image-generation", "video-generation"]`, `needs: ["gpu"]`.
   - `repos/skyvern`: Gán đúng `["browser-automation"]`, `needs: ["docker"]`.

3. **Phân bố `confidence`:**
   - 24 `cao` / 16 `vua` (đạt tỷ lệ cân bằng chuẩn 60% / 40%, phản ánh chính xác cấu trúc ngữ pháp và bằng chứng xác thực).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `coding-agent`, `auto-video-pipeline`, `video-processing-tools`, `tts-voiceover`, `agent-workflow-platform`, `agent-framework-core`, `tracing-telemetry`, `coding-workflow-frameworks`, `doc-to-markdown`, `browser-automation-framework`, `rag-memory`, `coding-workflow-skills`, `design-md-reference`, `motion-graphics`, `awesome-catalog`, `vector-rag`, `html-canvas-video`, `saas-boilerplate`, `higgsfield-fal-genmedia`, `branding-skills`, `content-marketing-stack`.

---
*Báo cáo Lô 8 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
