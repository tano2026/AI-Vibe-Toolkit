# Ghi chú Curation Lô 5 (40 mục: 161–200) — Antigravity

- **Tổng số mục:** 40/40 mục (`curation-todo-398.json` Lô 5, toàn bộ là các repository từ `repos/brand-building-skills` đến `repos/diffusiongemma`).
- **File kết quả:** `work/antigravity/v3/lo-5.json`.

---

## 1. Thống kê tổng quan Lô 5

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục đã đọc và xử lý** | 40 mục | Đủ 40 mục từ mục 161 đến 200 của danh sách todo. |
| **Confidence: Cao** | 25 mục (62.5%) | Evidence trích câu văn hoàn chỉnh nói thẳng năng lực đứng đầu. |
| **Confidence: Vừa** | 15 mục (37.5%) | Evidence là mệnh đề hoặc cụm từ giới thiệu/mô tả chức năng/tài liệu tham khảo. |
| **Confidence: Thấp** | 0 mục (0.0%) | Không có mục nào quá mỏng ở lô này. |
| **skip_if: có điều kiện thật** | 8 mục (20.0%) | Có điều kiện ngoại cảnh thật sự (Xvfb trên VPS headless, thiếu pycairo/ffmpeg, giới hạn ngôn ngữ tiếng Việt của TTS, RAM VPS tối thiểu 2GB, hỗ trợ KVM ảo hoá, thiếu MCP search key, API key DeepSeek trả phí, GPU VRAM 18GB). |
| **skip_if: unknown** | 32 mục (80.0%) | Không có điều kiện ngoại vi; các lưu ý cấu hình, cảnh báo rủi ro pháp lý, rà soát thủ công, biến động thuật toán tìm kiếm được đưa về unknown. |

---

## 2. Các điểm điều chỉnh chính so với nhãn nháp (`nhan_hien_tai`)

1. **Phân định rõ `skip_if` thực sự vs Cảnh báo nội bộ / Hướng dẫn triển khai:**
   - 32 mục được đưa về `skip_if = "unknown"` và `evidence_skip = ""` theo đúng chỉ đạo:
     + Lưu ý rủi ro pháp lý (`claude-for-legal`: khuyến cáo không thay thế luật sư có chứng chỉ).
     + Hướng dẫn cấu hình hạ tầng (`chatwoot`: cấu hình email máy chủ; `deepseek-r1-local`: thao tác cài đặt Ollama; `design-md`: vị trí đặt file ở root).
     + Biến động bên ngoài chung (`claude-seo`: biến động thuật toán tìm kiếm).
     + Đặc tính giao tiếp / hành vi (`caveman`: phong cách nói ngắn gọn kiểu người tiền sử).
   - 8 mục giữ `skip_if` với điều kiện ngoại cảnh xác thực:
     + `browser-use`: Cần display server trên VPS headless (`Bỏ qua nếu máy chủ ảo không có màn hình hiển thị hoặc chưa cài đặt phần mềm Xvfb`).
     + `buildfast-generative-film-skill`: Thiếu thư viện pycairo/ffmpeg (`Bỏ qua nếu môi trường máy tính chưa cài đặt thư viện đồ họa pycairo và công cụ ffmpeg`).
     + `chattts`: Tác giả xác nhận không phù hợp làm voiceover tiếng Việt (`Bỏ qua nếu yêu cầu sản xuất nội dung lồng tiếng chuyên biệt bằng tiếng Việt`).
     + `coolify`: Yêu cầu RAM VPS tối thiểu 2GB (`Bỏ qua nếu máy chủ ảo có dung lượng bộ nhớ dưới hai gigabyte RAM`).
     + `cubesandbox`: Yêu cầu VPS hỗ trợ KVM (`Bỏ qua nếu máy chủ ảo không hỗ trợ tính năng ảo hóa phần cứng lồng nhau KVM`).
     + `deep-research-skills`: Yêu cầu ít nhất 1 key Tavily/Firecrawl/Exa (`Bỏ qua nếu không có ít nhất một khóa dịch vụ tìm kiếm như Tavily, Firecrawl hoặc Exa`).
     + `deepseek-reasonix`: Không có free tier, cần key trả phí (`Bỏ qua nếu chưa đăng ký tài khoản và nạp số dư cho khóa giao diện lập trình DeepSeek`).
     + `diffusiongemma`: Yêu cầu phần cứng GPU VRAM 18GB trở lên (`Bỏ qua nếu máy chủ không có phần cứng GPU chuyên dụng dung lượng VRAM từ mười tám gigabyte trở lên`).

2. **Chuẩn hoá `capability` và `needs`:**
   - `repos/buzz`: Gán đúng `["agent-orchestration-memory", "productivity"]`, `needs: ["docker", "vps"]`.
   - `repos/chattts`: Gán đúng `["voice-tts", "local-llm"]`.
   - `repos/claude-motion-design`: Gán `["video-render", "design-ui"]`.
   - `repos/deepseek-reasonix`: Gán `["agent-framework", "backend"]`, `needs: ["api-key", "tra-phi"]`.
   - `repos/diffusiongemma`: Gán `["local-llm", "reference"]`, `needs: ["gpu"]`.

3. **Phân bố `confidence`:**
   - 25 `cao` / 15 `vua` (đạt tỷ lệ cân bằng thực tế ~62.5% / 37.5%, phản ánh đúng cấu trúc ngữ pháp của câu trích dẫn bằng chứng).

4. **Tên nhóm trùng (`dup_group`):**
   - Tái sử dụng nhất quán các nhóm đã có trong kho: `branding-skills`, `browser-automation-framework`, `auto-video-pipeline`, `security-scanner`, `job-monitoring`, `tts-voiceover`, `crm-connector`, `coding-workflow-frameworks`, `llm-gateway`, `coding-behavior-prompt`, `financial-analysis`, `legal-review`, `awesome-catalog`, `motion-design`, `seo-audit-tools`, `auto-short-video`, `code-review-skills`, `awesome-selfhosted`, `agent-framework-core`, `sandbox-execution`, `deep-research-skill`, `local-llm-deployment`, `coding-agent-cli`, `design-md-reference`, `command-guard`, `llm-training-learning`.

---
*Báo cáo Lô 5 bởi Antigravity — Đã kiểm định dạng và chuỗi con nguyên văn 100%.*
