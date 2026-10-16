# Ghi chú Curation Lô 1 (40 mục đầu) — Antigravity (Bản sửa đổi theo góp ý Claude)

- **Thời gian thực hiện:** Hoàn thiện và cập nhật theo 5 tiêu chí phản hồi từ đợt kiểm mẫu của Claude.
- **Tổng số mục:** 40/40 mục (thuộc `agents/*/skills/*`).
- **File kết quả:** `work/antigravity/v3/lo-1.json`.

---

## 1. Các điểm sửa đổi cốt lõi theo phản hồi kiểm mẫu

1. **Phân bố `confidence` thực tế (23 cao / 17 vừa):**
   - Không để 40/40 `cao`. Chỉ gắn `confidence = "cao"` khi `evidence` là một câu trọn vẹn ngữ pháp nói thẳng năng lực đứng đầu.
   - Các mục có evidence là cụm danh từ mô tả hoặc năng lực suy luận từ tài liệu được chuyển xuống `vua` (ví dụ: `customer-pattern-analysis`, `ota-content-strategy`, `agent-design-playbook`, `brand-visual-template-system`, `dev-automation-discipline`, `sales-marketing-collateral-production`).
   - Phân bố cụ thể: **23 `cao`**, **17 `vua`**, **0 `thap`**.

2. **Chuẩn hoá định dạng `evidence` và `evidence_skip`:**
   - Nối toàn bộ các chỗ xuống dòng (`\n`) trong `evidence` và `evidence_skip` thành một dòng duy nhất bằng khoảng trắng đơn.
   - Đảm bảo 100% `evidence` và `evidence_skip` là chuỗi con nguyên văn (substring) của văn bản gốc (sau khi chuẩn hoá khoảng trắng) và độ dài ≤ 120 ký tự.

3. **Phân định rõ `skip_if` thực sự vs Cảnh báo / Guardrail:**
   - `skip_if` chỉ nêu điều kiện ngoại cảnh hoặc tiền đề khiến ta phải bỏ qua skill (cần phần cứng/GPU, thiếu binary, quy mô kênh chưa đủ, ngoài phạm vi thị trường).
   - Lời cảnh báo cách dùng, quy tắc an toàn hoặc guardrail của chính skill (ví dụ: không scale theo trung bình, không tự tiện chi tiền, phải verify lệnh thật trước khi khẳng định) **không phải là `skip_if`**.
   - Các mục không có điều kiện loại trừ ngoại cảnh thật sự được đưa về `skip_if = "unknown"` và `evidence_skip = ""` (ví dụ: `digital-marketing-orchestrator`, `tencent-vps-capacity-cost`, `data-storytelling`, `destructive-command-guardrail`, `dev-automation-discipline`).
   - **Tổng số mục `skip_if = "unknown"`:** **26 / 40 mục** (14 mục có điều kiện bỏ qua thực sự).

4. **Điều chỉnh capability chính cho 2 mục đặc thù:**
   - `zalo-channel-connection-guide`: Đổi capability thành `["agent-orchestration-memory", "reference"]` (năng lực chính là tích hợp kênh chat cho agent OpenClaw điều phối hội thoại, thay vì chỉ là reference thuần túy).
   - `human-footage-editor`: Đổi capability thành `["content-writing", "video-render"]` (năng lực chính là viết kịch bản A/B roll, hook và hướng dẫn cắt dựng video ngắn, thay vì công cụ render video tự động).

5. **Làm sạch tài liệu:**
   - Đếm chính xác số lượng mục `skip_if = unknown`.
   - Loại bỏ hoàn toàn các nhắc đến "Luật 17" (không tồn tại trong hệ thống quy chuẩn).

---

## 2. Bảng phân bố thống kê chi tiết

| Chỉ số | Số lượng / Tỷ lệ | Diễn giải |
|---|---|---|
| **Tổng số mục** | 40 mục | Đủ 40 mục theo `curation-todo-398.json` (Lô 1). |
| **Confidence: Cao** | 23 mục (57.5%) | Evidence trích câu văn trọn vẹn khẳng định trực tiếp năng lực. |
| **Confidence: Vừa** | 17 mục (42.5%) | Evidence là cụm mô tả hoặc năng lực mang tính phương pháp/hướng dẫn. |
| **skip_if: có điều kiện** | 14 mục (35.0%) | Có điều kiện loại trừ ngoại vi thật sự (kênh < 5 video, không có footage, v.v.). |
| **skip_if: unknown** | 26 mục (65.0%) | Không có điều kiện loại trừ thật sự; chỉ có guardrail hoặc lời khuyên. |
| **Needs: none** | 35 mục | Kỹ năng prompt / quy trình nghiệp vụ thuần túy. |
| **Needs: api-key / vps** | 5 mục | Cần API key ngoài hoặc hạ tầng hosting VPS riêng. |

---

## 3. Danh sách 14 mục có điều kiện `skip_if` thật sự

1. `visa-transit-timatic-expert`: Bỏ qua nếu cần thay thế hệ thống tra cứu chuẩn Timatic của đại lý vé máy bay.
2. `brand-visual-template-system`: Bỏ qua nếu thương hiệu theo định hướng faceless hoặc không có footage người thật.
3. `human-footage-editor`: Bỏ qua nếu không có footage người thật từ khách hàng hoặc tự quay.
4. `ota-content-strategy`: Bỏ qua nếu là phòng khách sạn thông thường hoặc không có view bối cảnh đặc trưng.
5. `zalo-oa-booking-flow`: Bỏ qua nếu khách hàng chỉ mua vé máy bay thông thường không cần tư vấn hành trình.
6. `hermes-autonomous-kho-maintenance`: Bỏ qua nếu hệ thống Langfuse chưa được thiết lập trên máy chủ VPS Antigravity.
7. `cross-channel-distribution-analysis`: Bỏ qua nếu kênh mới có ít hơn 5 nội dung cùng thể loại chưa đủ dữ liệu tìm quy luật.
8. `content-repurpose-playbook`: Bỏ qua nếu chưa có nội dung gốc đạt hiệu quả hoặc cần sản xuất nội dung mới từ đầu.
9. `video-title-hook-generator`: Bỏ qua nếu nội dung dạng bài viết blog dài không cần yếu tố thu hút của video ngắn.
10. `agent-design-playbook`: Bỏ qua nếu tác vụ có quy trình xử lý cố định có thể giải quyết bằng kịch bản hoặc workflow thường.
11. `deploy-review-gate`: Bỏ qua nếu chỉ là lệnh đơn lẻ đơn giản đã có guardrail riêng xử lý.
12. `ceo-stress-test-and-roadmap`: Bỏ qua nếu báo cáo chỉ mang tính cập nhật thông tin không dẫn đến quyết định đầu tư nguồn lực.
13. `local-gap-finder`: Bỏ qua nếu nghiên cứu phạm vi vĩ mô đa ngành hoặc lĩnh vực không cạnh tranh theo địa lý.
14. `research-independent-review-gate`: Bỏ qua nếu là báo cáo nội bộ nhỏ hoặc nghiên cứu thăm dò không dẫn tới quyết định đầu tư lớn.

---
*Báo cáo bởi Antigravity — Lô 1 đã được chuẩn hoá 100% theo các tiêu chí phản biện.*
