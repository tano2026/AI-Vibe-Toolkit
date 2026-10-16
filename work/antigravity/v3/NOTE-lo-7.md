# Ghi chú Curation Lô 7 (40 mục: 241–280) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 7, toàn bộ là các repository từ `repos/jaeger` đến `repos/opencut`).
- **File kết quả:** `work/antigravity/v3/lo-7.json`.

---

## 1. Thống kê tổng quan Lô 7

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 241 đến 280 của danh sách todo. |
| **Confidence: Cao** | 24 mục (60.0%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 16 mục (40.0%) | Evidence là mệnh đề hoặc cụm từ giới thiệu/mô tả chức năng/tài liệu tham khảo. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 3 mục (7.5%) | Có điều kiện ngoại cảnh thật sự (langfuse, motion-graphics-skills, open-video-gen-models-2026). |
| **skip_if: unknown** | 37 mục (92.5%) | Không có điều kiện ngoại vi; các hướng dẫn tích hợp, cảnh báo bảo mật ứng dụng cục bộ được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Hướng dẫn triển khai:**
   - 37 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng quy chuẩn:
     + Ứng dụng/tiện ích chạy cục bộ không đòi hỏi hạ tầng ngoài (`meetily`, `omnivoice-studio`, `opencut`).
     + Quy trình thiết kế, tham khảo, thư viện mã nguồn (`lucide`, `nanoid`, `nextjs-subscription-payments`).
   - 3 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `repos/langfuse`: Bỏ qua nếu máy chủ thiếu hạ tầng dịch vụ cơ sở dữ liệu Postgres, ClickHouse và MinIO (Evidence: "Self-host full-stack (Postgres + ClickHouse + MinIO) là cách DUY NHẤT được hỗ trợ chính thức")
     + `repos/motion-graphics-skills`: Bỏ qua nếu tài khoản Claude Code không có quyền sử dụng mô hình Claude 3 Opus (Evidence: "README yêu cầu chạy trên **Opus 5.5**")
     + `repos/open-video-gen-models-2026`: Bỏ qua nếu máy tính hoặc máy chủ không có phần cứng đồ họa chuyên dụng GPU rời đủ mạnh (Evidence: "Không hợp chạy trên VPS Tencent Cloud hay máy Windows local hiện có (không có GPU rời đủ mạnh)")

2. **Chuẩn hoá `capability` và `needs`:**
   - `repos/jaeger`: Gán đúng `["security-compliance", "reference"]`, `needs: ["docker"]`.
   - `repos/langfuse`: Gán đúng `["agent-framework", "backend"]`, `needs: ["docker", "database"]`.
   - `repos/litellm`: Gán đúng `["agent-framework", "backend"]`, `needs: ["docker"]`.
   - `repos/lucide`: Gán đúng `["front-end", "design-system"]`, `needs: ["none"]`.
   - `repos/magika`: Gán đúng `["security-compliance", "reference"]`, `needs: ["none"]`.
   - `repos/meetily`: Gán đúng `["productivity"]`, `needs: ["none"]`.
   - `repos/omnivoice-studio`: Gán đúng `["voice-tts", "local-llm"]`, `needs: ["none"]`.
   - `repos/opencut`: Gán đúng `["video-render", "front-end"]`, `needs: ["none"]`.

3. **Phân bố `confidence`:**
   - 24 `cao` / 16 `vua` (đạt tỷ lệ cân bằng chuẩn 60% / 40%, phản ánh chính xác cấu trúc ngữ pháp và bằng chứng xác thực).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `tracing-telemetry`, `vector-rag`, `financial-analysis`, `agent-workflow-platform`, `llm-gateway`, `icon-assets`, `audio-processing`, `security-scanner`, `automation-hub`, `database-tools`, `meeting-recording`, `saas-boilerplate`, `motion-graphics`, `tts-voiceover`, `video-processing-tools`.

---
*Báo cáo Lô 7 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
