# Ghi chú Curation Lô 9 (40 mục: 321–360) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 9, gồm 39 repository từ `repos/stitch-skills` đến `repos/ziwei-doushu` và 1 skill `skills/4-nguon-y-tuong-content`).
- **File kết quả:** `work/antigravity/v3/lo-9.json`.

---

## 1. Thống kê tổng quan Lô 9

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 321 đến 360 của danh sách todo. |
| **Confidence: Cao** | 24 mục (60.0%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 16 mục (40.0%) | Evidence là mệnh đề, cụm giới thiệu hoặc cấu trúc ngữ pháp tương quan/mô tả chức năng. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 2 mục (5.0%) | Có điều kiện ngoại cảnh thật sự (turbodiffusion, whisper). |
| **skip_if: unknown** | 38 mục (95.0%) | Không có điều kiện ngoại vi; các hướng dẫn bảo mật dữ liệu khách hàng, bản quyền AGPL/thương mại, cấu hình token được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Hướng dẫn triển khai:**
   - 38 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng quy chuẩn:
     + Lưu ý bảo mật dữ liệu khách hàng hoặc điều khoản thương mại (`stitch-skills`, `tencentdb-agent-memory`, `twenty-crm`).
     + Rào cản tương thích hoặc kinh nghiệm vận hành (`tiktokautouploader`: khuyên dùng tài khoản có lịch sử; `video-autopilot-kit`: độ nhạy phiên bản CapCut).
     + Hướng dẫn thiết lập token / API key có sẵn (`vectcutapi`, `video-use`).
   - 2 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `repos/turbodiffusion`: Bỏ qua nếu máy chủ thiếu phần cứng đồ họa chuyên dụng GPU như RTX 5090 để tăng tốc tạo video (Evidence: "video 5 giây trên RTX 5090 ra nhanh gấp 100-200 lần so với chạy Wan2.1 gốc.")
     + `repos/whisper`: Bỏ qua nếu máy tính chưa cài đặt phần mềm xử lý âm thanh ffmpeg trên hệ thống (Evidence: "Cài một lệnh `pip install -U openai-whisper`, nhưng **bắt buộc có ffmpeg**.")

2. **Chuẩn hoá `capability` và `needs`:**
   - `repos/stitch-skills`: Gán đúng `["design-ui", "front-end"]`, `needs: ["none"]`.
   - `repos/ui-tars-desktop`: Gán đúng `["computer-use", "browser-automation"]`, `needs: ["none"]`.
   - `repos/turbodiffusion`: Gán đúng `["video-generation", "video-render"]`, `needs: ["gpu"]`.
   - `repos/vibe-trading`: Chuẩn hóa gán `["productivity", "agent-framework"]` (loại bỏ nhãn không hợp lệ `finance-accounting`).
   - `repos/x-research-skill`: Chuẩn hóa gán `["web-research", "social-media"]` (loại bỏ nhãn không hợp lệ `scraping`).
   - `repos/yt-dlp`: Chuẩn hóa gán `["web-research", "productivity"]` (loại bỏ nhãn không hợp lệ `scraping`).
   - `repos/whisper`: Gán đúng `["voice-tts"]`, `needs: ["none"]`.
   - `repos/yue2-studio`: Gán đúng `["local-llm", "audio-music"]`, `needs: ["gpu"]`.

3. **Phân bố `confidence`:**
   - 24 `cao` / 16 `vua` (đạt tỷ lệ cân bằng chuẩn 60% / 40%, phản ánh chính xác cấu trúc ngữ pháp và bằng chứng xác thực).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `design-md-reference`, `security-scanner`, `database-tools`, `rag-memory`, `coding-workflow-skills`, `tts-voiceover`, `agent-workflow-platform`, `branding-skills`, `browser-automation-framework`, `auto-video-pipeline`, `saas-boilerplate`, `awesome-catalog`, `video-processing-tools`, `vector-rag`, `crm-connector`, `agent-framework-core`, `coding-workflow-frameworks`, `financial-analysis`, `web-scraper`, `audio-processing`, `data-dashboard`, `content-marketing-stack`, `tu-vi-astrology`.

---
*Báo cáo Lô 9 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
