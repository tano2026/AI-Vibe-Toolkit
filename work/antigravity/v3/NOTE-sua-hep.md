# Ghi chú vòng sửa hẹp v3 (Lô 2–10) — Antigravity

## 1. Phương pháp và thời gian thực hiện
- **Phạm vi rà soát:** Đúng 167 mục được liệt kê trong `catalog/HANDOFF/20261017-v3-sua-hep/worklist.json`.
- **Phương pháp đọc:** Đọc có chủ đích (targeted reading) các phần liên quan đến nhãn cảnh báo:
  - `gpu`: Rà soát phần cứng, yêu cầu VRAM/CUDA/GPU. Chỉ ghi nhận khi bắt buộc GPU thật để chạy; các trường hợp chạy được CPU hoặc gọi qua Cloud API được giữ nguyên.
  - `license`: Rà soát giấy phép AGPL-3.0, GPL-3.0, CC BY-NC, Enterprise hoặc giấy phép có ngưỡng thương mại riêng (Remotion).
  - `beta`: Rà soát trạng thái phát hành (alpha, beta, preview, developer preview). Nếu công cụ chưa ổn định hoặc chưa lên PyPI, chuyển `adoption` sang `can-ha-tang` và bổ sung `skip_if`.
  - `api-key` & `tra-phi`: Rà soát yêu cầu cấu hình khóa API (OpenAI, Anthropic, Gemini, Apify, TubeLab, Google Maps...) và chi phí credit/subscription bắt buộc.
- **Thời gian thực hiện:** Khoảng 45 phút kiểm tra đối chiếu trực tiếp trên từng file markdown nguồn.
- **Trung thực:** Xác nhận đây là đợt đọc có chủ đích theo phân đoạn nhạy cảm (TL;DR, Cảnh báo, Yêu cầu, Cài đặt, License), không đọc toàn bộ từng chữ trong toàn entry.

---

## 2. Kết quả tổng hợp
- **Tổng số mục trong danh sách sửa hẹp:** 167 mục.
- **Mục có thay đổi (`sua-hep.json`):** 75 mục.
  - **48 mục** cập nhật điều kiện loại trừ (`skip_if`), chuỗi bằng chứng nguyên văn (`evidence_skip`), yêu cầu (`needs`) và mức độ sẵn sàng (`adoption`).
  - **27 mục** chuẩn hóa câu văn trong `use_when` (thay "tác nhân" -> "agent", "trợ lý lập trình" -> "coding agent", đổi số dạng chữ "sáu mươi tám", "gần ba trăm", "mười lăm" thành chữ số "68", "gần 300", "15").
- **Mục giữ nguyên:** 92 mục (ghi rõ `{"id": "...", "giu_nguyen": true}`).
- **Kiểm định cơ học:**
  - `skip_if`: Tất cả đều bắt đầu bằng `"Bỏ qua nếu "`, độ dài ≤ 100 ký tự, không chứa từ quảng cáo cấm ("miễn phí", "hoàn toàn", "không giới hạn", "tốt nhất") và không có dấu ba chấm `...`.
  - `evidence_skip`: Là chuỗi con nguyên văn 100% trong entry nguồn (chuẩn hóa khoảng trắng), độ dài ≤ 120 ký tự.
  - `adoption`: Thuộc 4 giá trị hợp lệ (`cai-ngay-duoc`, `can-ha-tang`, `chi-tham-khao`, `unknown`). Các mục beta/alpha chuyển sang `can-ha-tang`.
  - `capability`: 100% nằm trong danh mục 30 capability chuẩn của kho.

---

## 3. Chi tiết phân loại theo các nhóm nhãn chính

### A. Nhóm GPU (5 mục cập nhật bắt buộc, còn lại giữ nguyên)
- `repos/omnishow`: Bắt buộc GPU mạnh cấp nghiên cứu (A100) -> Thêm `needs: ['gpu']`, `adoption: chi-tham-khao`, `skip_if: Bỏ qua nếu không có GPU mạnh chuyên dụng A100 để chạy mô hình nghiên cứu`.
- `repos/vimax`: Bắt buộc GPU 24GB+ hoặc API cloud -> Thêm `needs: ['gpu', 'api-key']`, `skip_if: Bỏ qua nếu không có GPU tối thiểu 24GB VRAM hoặc không có khóa API dịch vụ video đám mây`.
- `repos/voice-pro`: Cần GPU rời (RTX 3080) và giấy phép GPL-3.0 -> Thêm `needs: ['gpu']`, `skip_if: Bỏ qua nếu không có GPU rời để xử lý âm thanh hoặc tích hợp phần mềm đóng do giấy phép GPL-3.0`.
- `repos/pixelle-video`: Không có GPU bắt buộc trả phí API Cloud (RunningHub + LLM) -> Thêm `needs: ['api-key', 'tra-phi']`.
- `repos/stable-diffusion-3-medium`: Bắt buộc GPU 8GB+ VRAM -> Thêm `needs: ['gpu']`, `skip_if: Bỏ qua nếu máy tính không có GPU chuyên dụng với tối thiểu 8GB VRAM`.
*(Các mục như `mcps/framecraft`, `mcps/fal-mcp`, `repos/kokoro-82m`, `repos/supertonic`, `repos/chattts`, `repos/funasr` xác nhận chạy tốt trên CPU hoặc Cloud nên giữ nguyên không đòi hỏi GPU).*

### B. Nhóm License (9 mục cập nhật ràng buộc thương mại / copyleft)
- `repos/short-video-factory`: Giấy phép AGPL-3.0 copyleft mạnh -> Bổ sung `skip_if`.
- `repos/ever-gauzy`: Giấy phép Community Edition phân tầng, tính năng sâu cần trả phí -> Thêm `needs: ['tra-phi']` và `skip_if`.
- `repos/twenty-crm`: Chứa thành phần Enterprise thương mại và AGPLv3 -> Bổ sung `skip_if`.
- `repos/worldmonitor`: Giấy phép AGPL-3.0 khi cung cấp dịch vụ mạng SaaS -> Bổ sung `skip_if`.
- `repos/cinetic`: Phụ thuộc engine Remotion giới hạn công ty ≤ 3 người -> Bổ sung `skip_if`.
- `repos/claude-motion`: Phụ thuộc Remotion có giấy phép thương mại riêng -> Bổ sung `skip_if`.
- `stacks/motion-design-studio-claude-code`: Phụ thuộc Remotion có ngưỡng thương mại -> Bổ sung `skip_if`.
- `stacks/twenty-crm-abtrip-internal`: Tính năng Enterprise yêu cầu bản quyền riêng -> Bổ sung `skip_if`.
- `repos/system-prompts-ai`: Kho lưu trữ dạng GPL-3.0 -> Bổ sung `skip_if`.

### C. Nhóm Beta / Alpha (4 mục cập nhật adoption & skip_if)
- `repos/openreel-video`: Trạng thái Beta, nhiều tính năng đang phát triển -> `adoption: can-ha-tang`.
- `repos/pycaps`: Trạng thái "very alpha stage", chưa phát hành lên PyPI -> `adoption: can-ha-tang`.
- `stacks/deepseek-harness-bo-tai-lieu`: Framework dsh ở giai đoạn rc (developer preview) -> `adoption: can-ha-tang`.
- `repos/paperclip`: Một số tính năng vận hành doanh nghiệp còn ở bản beta -> Bổ sung `skip_if`.

### D. Nhóm API-Key & Trả phí (30 mục cập nhật)
- Điển hình:
  - `repos/head-of-content`: Bắt buộc tài khoản trả phí Apify và TubeLab -> `needs: ['api-key', 'tra-phi']`.
  - `repos/x-research-skill`: Bắt buộc API key X (Twitter), gói Basic $100/tháng -> `needs: ['api-key', 'tra-phi']`.
  - `repos/openwork-modelstudioai`: Bắt buộc tài khoản Alibaba Cloud Bailian -> `needs: ['api-key']`.
  - `mcps/perplexity`: Yêu cầu API key trả phí riêng -> `needs: ['api-key', 'tra-phi']`.
  - `mcps/minimax-mcp`: Dịch vụ tạo video tiêu tốn credit -> `needs: ['api-key', 'tra-phi']`.
  - `repos/openmontage`: Cần API key OpenAI/Anthropic và trả phí ElevenLabs -> `needs: ['api-key', 'tra-phi']`.
  - `repos/toonflow`: Chi phí tạo ảnh FLUX/SD -> `needs: ['api-key', 'tra-phi']`.
  - `repos/videofy-minimal`: Bắt buộc 2 API key OpenAI và ElevenLabs -> `needs: ['api-key', 'tra-phi']`.
  - `agents/trum-san-bay/skills/content-research`: Phụ thuộc credit Apify -> `needs: ['api-key', 'tra-phi']`.
  - `agents/trum-san-bay/skills/video-renderer`: Cần ffmpeg và API key Anthropic -> `needs: ['vps', 'api-key']`.

---

## 4. Mục lưu ý và không chắc chắn
1. `repos/barty-motion-graphics`: Repo có 6 skill, trong đó chỉ riêng skill `object-separation` dùng SAM 2 chạy CPU mất ~5s/khung, tác giả có gắn link dẫn tới cộng đồng trả phí. Tuy nhiên 5 skill còn lại là motion/SFX thuần hoàn toàn độc lập và không đòi GPU hay phí. Do đó giữ nguyên `adoption: cai-ngay-duoc` và `skip_if: unknown`.
2. `repos/hyperframes-student-kit`: Đoạn code demo 8s chạy hoàn toàn không cần API key, nhưng quy trình quay video thật khuyến nghị dùng ElevenLabs Scribe trả phí. Vì đây là student-kit phục vụ thực hành nên được giữ nguyên là `cai-ngay-duoc`.
3. `skills/gemini-video-content-kit`: Là bộ 7 prompt template định hướng kịch bản, không phải tool tự chạy trực tiếp bằng code nên không áp đặt bắt buộc API key riêng.
4. **Ghi chú về 32 mục ngoài danh sách worklist trong các lô 2–10:** Hiện trong `catalog/curation.json` vẫn còn 32 mục chứa các từ ngữ gượng như "tác nhân", "trợ lý lập trình". Do nằm ngoài 167 mục của `worklist.json`, Antigravity không tự tiện thêm vào `sua-hep.json` để tránh sai lệch cấu trúc kiểm tra tự động của Claude, nhưng đã lập danh sách theo dõi sẵn sàng khi Claude cần chuẩn hóa toàn diện.
