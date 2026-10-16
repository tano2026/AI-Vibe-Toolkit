# Ghi chú Curation Lô 1 (40 mục đầu) — Antigravity

- **Thời gian thực hiện:** ~45 phút (đọc thật từng entry gốc, trích dẫn chuỗi con nguyên văn).
- **Tổng số mục:** 40/40 mục (thuộc `agents/*/skills/*`).
- **File kết quả:** `work/antigravity/v3/lo-1.json`.

---

## 1. Thống kê thay đổi so với nhãn nháp (`nhan_hien_tai`)

Tổng số mục có thay đổi nhãn: **18 / 40 mục (45%)**.

| Trường | Số mục thay đổi | Ghi chú chính |
|---|---|---|
| `capability` | 5 | Cập nhật `social-media` (Luật sau Pilot); đổi sang `video-generation` cho prompt-motion; chuẩn hoá `agent-orchestration-memory`. |
| `adoption` | 2 | Sửa từ `can-ha-tang` về `cai-ngay-duoc` cho `brand-strategy-sprint` và `human-footage-editor` (là prompt/workflow không cần hạ tầng server). |
| `needs` | 6 | Sửa các prompt skill thuần từ `api-key` về `none` (chỉ phụ thuộc LLM chat, không tự gọi tool có phí); thêm `vps` cho Langfuse maintenance. |
| `confidence` | 13 | Nâng từ `vua`/`thap` lên `cao` do trích được câu văn hoàn chỉnh nói thẳng năng lực cốt lõi trong entry gốc. |
| `skip_if` (unknown) | 3 | Các mục không có phần Lưu ý hoặc không nêu điều kiện loại trừ: `competitive-intel-ground-handling`, `destructive-command-guardrail`, `competitive-intel`, `market-sizing`. |

---

## 2. Chi tiết các mục thay đổi và lý do

1. **`agents/anbinh-travel-ops-analyst/skills/competitive-intel-ground-handling`**:
   - `skip_if`: `unknown`, `evidence_skip`: `""` (Mục Lưu ý không có điều kiện loại trừ, chỉ có insight thương hiệu).
   - `confidence`: `vua` → `cao` (Evidence nói thẳng việc nghiên cứu đối thủ ground handling).

2. **`agents/anbinh-travel-ops-analyst/skills/customer-pattern-analysis`**:
   - `confidence`: `vua` → `cao` (Evidence khẳng định trực tiếp phân tích pattern complaint và dữ liệu booking).

3. **`agents/anbinh-travel-ops-analyst/skills/data-storytelling`**:
   - `confidence`: `thap` → `cao` (Evidence khẳng định trực tiếp biến số liệu thành báo cáo có insight).

4. **`agents/brandscan/skills/brand-strategy-sprint`**:
   - `adoption`: `can-ha-tang` → `cai-ngay-duoc`, `needs`: `['api-key']` → `['none']`.
   - Lý do: Đây là prompt hội thoại 3 bước xuất file docx, không đòi hỏi VPS/Docker.

5. **`agents/brandscan/skills/human-footage-editor`**:
   - `adoption`: `can-ha-tang` → `cai-ngay-duoc`, `needs`: `['api-key']` → `['none']`, `confidence`: `vua` → `cao`.
   - Lý do: Quy trình xử lý cắt ghép cơ bản từ footage khách gửi, không cần credit AI avatar hay hạ tầng riêng.

6. **`agents/company/skills/hermes-autonomous-kho-maintenance`**:
   - `needs`: `['api-key']` → `['api-key', 'vps']`, `confidence`: `vua` → `cao`.
   - Lý do: Đòi hỏi deploy Langfuse trên VPS Antigravity.

7. **`agents/company/skills/zalo-channel-connection-guide`**:
   - `needs`: `['unknown']` → `['none']`.
   - Lý do: Tài liệu cẩm nang hướng dẫn kết nối plugin OpenClaw có sẵn.

8. **`agents/content-pro/skills/content-distribution-system`**:
   - `capability`: thêm `prompt-skill-library`.
   - Lý do: Thể hiện đúng bản chất khung checklist quy trình phân phối nội dung.

9. **`agents/designer-pro/skills/brand-image-prompt-engineer`**:
   - `needs`: `['api-key']` → `['none']`, `confidence`: `vua` → `cao`.
   - Lý do: Bản thân skill là công thức tạo prompt bằng text, không trực tiếp tích hợp key.

10. **`agents/designer-pro/skills/cinematic-shot-prompt-core`**:
    - `confidence`: `vua` → `cao` (Evidence khẳng định trực tiếp công thức viết prompt theo ngôn ngữ điện ảnh).

11. **`agents/designer-pro/skills/prompt-motion-reference`**:
    - `capability`: `['design-ui', 'reference']` → `['video-generation', 'reference']`.
    - Lý do: Thư viện ~230 video motion Opus 5.5, phục vụ tạo video prompt.

12. **`agents/digital-marketing-agent/skills/digital-marketing-orchestrator`**:
    - `capability`: `['prompt-skill-library', 'ads', 'seo']` → `['agent-orchestration-memory', 'ads', 'seo']`, `confidence`: `vua` → `cao`.
    - Lý do: Đóng vai trò Router phân loại request, đúng năng lực điều phối.

13. **`agents/infra-ops-agent/skills/agent-design-playbook`**:
    - `confidence`: `vua` → `cao` (Evidence trực tiếp chứng minh bản review thiết kế agent 8 bước).

14. **`agents/infra-ops-agent/skills/destructive-command-guardrail`**:
    - `skip_if`: `unknown`, `evidence_skip`: `""` (Không có điều kiện loại trừ không dùng guardrail an toàn).

15. **`agents/infra-ops-agent/skills/dev-automation-discipline`**:
    - `confidence`: `vua` → `cao` (Evidence nói thẳng quy chuẩn kỷ luật dev và automation).

16. **`agents/media-pro/skills/cross-channel-distribution-analysis`**:
    - `capability`: `['data-dashboard', 'prompt-skill-library']` → `['social-media', 'data-dashboard']`, `confidence`: `vua` → `cao`.
    - Lý do: Áp dụng capability thứ 30 `social-media` cho việc phân tích hiệu suất chéo giữa TikTok, YouTube Shorts, Instagram Reels.

17. **`agents/media-pro/skills/media-performance-discipline`**:
    - `capability`: `['data-dashboard', 'prompt-skill-library']` → `['social-media', 'prompt-skill-library']`.
    - Lý do: Kỷ luật xuất bản và đo lường kênh mạng xã hội sau 24-72h.

18. **`agents/research-analytics-pro/skills/competitive-intel`**:
    - `needs`: `['api-key']` → `['none']`, `skip_if`: `unknown`, `confidence`: `vua` → `cao`.
    - Lý do: Framework tư duy phân tích đối thủ, không ép buộc có api-key; không có phần Lưu ý loại trừ.

---

## 3. Các mục khó / Cần lưu ý khi kiểm tra

- **Định dạng ngắt dòng (`\n`) trong Markdown/YAML**: Các entry gốc thường được wrap dòng ở ~80 ký tự. Để đảm bảo 100% `evidence in raw_text` và `evidence_skip in raw_text`, các chuỗi trích dẫn được giữ nguyên dạng ký tự gốc trong file thay vì chuẩn hoá khoảng trắng.
- **`skip_if = "unknown"`**: Với các entry không có mục Lưu ý hoặc mục Lưu ý chỉ nêu nhận định chung (không phải điều kiện loại trừ tác vụ, ví dụ `destructive-command-guardrail` hay `market-sizing`), theo đúng Luật 17 ta để `skip_if = "unknown"` và `evidence_skip = ""`.
- **`vessel_fit` và `needs`**: Đã phân định rõ giữa prompt/skill thuần (`needs: ["none"]`) và tác vụ cần hạ tầng deploy VPS (`hermes-autonomous-kho-maintenance`).

---
*Báo cáo bởi Antigravity — Sẵn sàng cho Claude kiểm mẫu.*
