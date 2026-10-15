# BÁO CÁO PILOT 20 MỤC ĐẦU (BATCH 4) — ANTIGRAVITY

> Ngày thực hiện: 16/10/2026  
> Người thực hiện: Antigravity  
> Đầu ra: `work/antigravity/pilot20.json` (20 mục) & `work/antigravity/PILOT-NOTE.md`

---

## 1. Thời gian thực hiện
- **Tổng thời gian:** ~20 phút.
- Gồm: đọc trọn vẹn 20 file entry gốc (`.md`), trích xuất dữ liệu, gắn nhãn từng trường theo đúng bộ từ vựng chuẩn, trích verbatim `evidence`, và viết script kiểm tra cơ học tự động.

---

## 2. Thống kê sơ bộ 20 mục pilot
- **Số mục hoàn thành:** 20 / 20.
- **Tỉ lệ confidence:**
  - `cao`: 20 / 20 (100% — cả 20 entry đều có nội dung chi tiết, TL;DR, setup hoặc agent integration rõ ràng).
  - `vua`: 0.
  - `thap`: 0.
- **Phân bổ adoption:**
  - `cai-ngay-duoc`: 12 mục (60%)
  - `can-ha-tang`: 5 mục (25% — cần Docker, VPS, DB hoặc môi trường nặng như Crawl4AI, BitFun, DramaClaw, Roomifields, AI-auto-generate-video)
  - `chi-tham-khao`: 3 mục (15% — Awesome-GPT-Image-2, Claude-Code-Skills-List, Continue)

---

## 3. Các mục khó phân loại và giải pháp

1. **`mcps/buffer-mcp` (Lên lịch & đăng bài MXH):**
   - *Khó khăn:* Bảng 29 capabilities cố định không có mục riêng cho `social-media` hay `social-posting`.
   - *Giải pháp:* Chọn `productivity` (tự động hóa đăng bài và quản lý lịch trình), gán `dup_group: social-media-post`.
2. **`mcps/tiktok-mcp` (TikTok Ads/Posting):**
   - *Khó khăn:* TikTok chưa có MCP chính thức dù có thông báo; entry thực chất mô tả 2 dịch vụ bên thứ 3 (Outstand để post, Pipeboard để quản lý Ads).
   - *Giải pháp:* Gắn cả `ads` và `productivity`; trong `skip_if` nêu rõ rủi ro cần tránh hiểu nhầm là official MCP.
3. **`repos/ai-video-generator-claude` (Tên gây hiểu lầm):**
   - *Khó khăn:* Tên repo có chữ "generator" nhưng entry ghi rõ: *"Đây KHÔNG phải tool tự sinh video — là skill viết prompt cho người khác/model khác sinh video"*.
   - *Giải pháp:* Không gán `video-generation` đứng đầu mà gán `prompt-skill-library` đứng đầu, `video-generation` phụ; vessel_fit là `claude-code`, `deepseek-harness`.
4. **`repos/continue` (Repo đã ngưng bảo trì):**
   - *Khó khăn:* Là coding agent tiên phong rất nổi tiếng (33.7k sao), nhưng tháng 6/2026 repo đã chết (discontinued/read-only).
   - *Giải pháp:* Gắn `adoption: chi-tham-khao`, `vessel_fit: []`, gán capability `agent-framework` và `reference`. `use_when` hướng tới học hỏi pattern thiết kế `.continue/` thay vì deploy production.
5. **`repos/awesome-gpt-image-2` (Kho prompt tĩnh):**
   - *Khó khăn:* Là danh sách 2000+ prompt và ảnh preview, không có code chạy hay API.
   - *Giải pháp:* Gắn `prompt-skill-library` + `image-generation` + `reference`, `adoption: chi-tham-khao`, `needs: ["none"]`.

---

## 4. Điểm cần làm rõ về luật (cho Giai đoạn 2)
1. **Quy định trích dẫn `evidence`:**
   - Cần đảm bảo trích **nguyên văn từng ký tự (exact substring)** từ file entry gốc, bao gồm cả markdown formatting (dấu sao `**`, ngoặc kép `"`, backtick). Giới hạn ≤ 120 ký tự là hợp lý, đủ trích 1 mệnh đề chứa năng lực cốt lõi.
2. **Trường `needs` đối với mục `chi-tham-khao`:**
   - Các repo prompt (như `awesome-gpt-image-2` hay `system-prompts`) bản thân file không đòi hỏi API key để đọc, nhưng nếu người dùng muốn chạy prompt đó thì cần API key. Đề xuất thống nhất: đánh giá `needs` theo yêu cầu trực tiếp của tài nguyên đó (`none` cho repo tĩnh).
3. **Phân loại công cụ mạng xã hội:**
   - Các công cụ đăng bài/quản lý social media (Buffer, TikTok posting) hiện đang dùng `productivity`. Nếu Tano Agency làm content/social media nhiều, có thể cân nhắc xem `productivity` đã đủ phản ánh chưa (hay cần kết hợp `content-writing` / `ads`).

---

## 5. Kết quả kiểm tra cơ học tự động (Validation Gate)
Script `work/antigravity/build_pilot.py` đã kiểm tra toàn bộ 20 mục và xác nhận:
- [x] Đủ 20 mục, đúng thứ tự trong `batch4-chua-gan-nhan.json`.
- [x] Tất cả `id` tồn tại và khớp chính xác `catalog/catalog.json`.
- [x] Tất cả `capability` thuộc tập 29 nhãn hợp lệ, số lượng 1–3, năng lực chính đứng đầu.
- [x] Tất cả `use_when` ≤ 140 ký tự, bắt đầu bằng "Dùng khi cần ...", không quảng cáo, không nhắc tên công cụ.
- [x] Tất cả `skip_if` ≤ 100 ký tự, bắt đầu bằng "Bỏ qua nếu ...", lấy từ Lưu ý/Đánh giá.
- [x] Tất cả `adoption`, `vessel_fit`, `needs`, `confidence` tuân thủ enum cho phép.
- [x] Tất cả `evidence` là chuỗi con nguyên văn (exact substring) trong entry gốc và ≤ 120 ký tự.
