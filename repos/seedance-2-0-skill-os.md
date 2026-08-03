# Seedance 2.0 Skill OS (Emily2040) — "Đạo diễn mã nguồn mở" — GitHub Repo

## TL;DR
Bộ 23 skill module hóa dạy AI agent viết prompt cho Seedance 2.0 (model video AI của ByteDance, đã có `seedance-2-5.md` trong kho) **như 1 đạo diễn thật** — đọc kịch bản trước khi viết prompt, giữ nhất quán 1 "giọng đạo diễn" xuyên suốt nhiều clip trong 1 câu chuyện dài. 6K sao, MIT, 33 ví dụ đầy đủ (sản phẩm, MV, kinh dị, anime, hành động, tài liệu...). Khác `seedance-2-5.md` đã có (nói về bản thân model), đây là **lớp kỹ năng viết prompt** để dùng model đó cho ra kết quả điện ảnh thay vì "prompt phẳng".

## Repo này dùng để làm gì
Vấn đề cốt lõi bộ này giải quyết: hầu hết người dùng viết prompt video AI kiểu liệt kê tính từ ("cinematic, dramatic, 4K") — ra kết quả chung chung. Bộ skill này ép agent phải **đọc chức năng kịch tính của cảnh trước khi viết** (đây là cảnh "reveal", "arrival", "quyết định", "biến hình"...) rồi mới chọn camera/ánh sáng/diễn xuất/âm thanh phục vụ đúng 1 ý đồ đó — không dùng công thức chung cho mọi cảnh.

**23 sub-skill độc lập**, agent chỉ load đúng cái cần (zero token waste):
- `seedance-interview` / `seedance-interview-short` — phỏng vấn đạo diễn khi ý tưởng còn mơ hồ, có "Quick Mode" cho ai đã có reference rõ
- `seedance-prompt` — viết prompt chuẩn production (30-100 từ), theo "công thức đạo diễn": xác định 1 khoảnh khắc hình ảnh duy nhất → gán vai trò cho từng reference asset → viết theo thứ tự camera-ánh sáng-diễn xuất-âm thanh
- `seedance-camera`, `seedance-motion`, `seedance-lighting`, `seedance-characters`, `seedance-style`, `seedance-vfx` — từng mảng kỹ thuật riêng
- `seedance-pipeline` — quy trình sản xuất chuyên nghiệp đầy đủ (treatment, shot list, continuity ledger, review loop, hậu kỳ, delivery/QC)
- `seedance-copyright` — **bắt buộc chạy trước mỗi lần generate** (xem mục cảnh báo dưới)
- `seedance-troubleshoot` — cây chẩn đoán 5 bước khi kết quả generate ra lỗi

Hỗ trợ 4 chế độ input: T2V (text), I2V (ảnh), V2V (video), R2V (reference-to-video), cùng
first/last-frame workflow (khoá điểm đầu-cuối clip). Có sẵn hướng dẫn tiếng Trung/Nhật/Hàn cho
người dùng không phải tiếng Anh gốc.

## Setup từng bước
```bash
# Claude Code / Antigravity / Gemini CLI đều cài được qua URL trực tiếp
antigravity skills install https://github.com/Emily2040/seedance-2.0
# hoặc Codex: copy vào $CODEX_HOME/skills/seedance-20 (hoặc ~/.codex/skills/seedance-20)
```
Trigger tự nhiên: mô tả ý tưởng video mơ hồ → agent tự vào `seedance-interview` hỏi lại đúng
câu cần thiết (chủ thể, hành động, reference asset, cảm giác camera, độ dài) → ra prompt chuẩn.

## Ví dụ thực tế
Cần B-roll cho "Airfare Decoded" — cảnh máy bay cất cánh cảm giác hùng vĩ — thay vì tự viết
prompt "cinematic airplane takeoff, dramatic, 4K" (ra kết quả chung chung), dùng
`seedance-interview-short`: agent hỏi lại "khoảnh khắc hình ảnh cụ thể là gì — máy bay tách khỏi
đường băng, hay góc nhìn từ cửa sổ hành khách?" → chốt 1 ý đồ rõ ràng → `seedance-prompt` viết
ra prompt 30-100 từ đúng công thức đạo diễn, không lan man.

## Lưu ý / Lỗi thường gặp
- **Cảnh báo bản quyền quan trọng (cập nhật 02/08/2026):** Global launch đã diễn ra 15/4/2026
  nhưng **trừ thị trường Mỹ** — 2 Thượng nghị sĩ Mỹ yêu cầu đóng cửa sau khi Disney/Paramount/
  Warner Bros/Netflix/SAG-AFTRA gửi cảnh báo pháp lý vì nghi ngờ train trên dữ liệu có bản quyền.
  ByteDance đã thêm safeguard (chặn tạo mặt người thật/nhân vật IP thương hiệu) nhưng **tranh
  chấp pháp lý với các studio CHƯA giải quyết xong ở tòa** — vẫn đang lơ lửng, chưa yên ổn hẳn.
  **Bắt buộc chạy `seedance-copyright` trước mỗi lần generate** — bỏ qua bước này dễ dính vi
  phạm bản quyền khi dùng nhân vật/IP không phải của mình.
- Có bản fork/tương tự `zhishu51/seedance-2.0-director` (dịch/đóng gói lại cho Codex) — nội
  dung cùng gốc, chỉ khác cách cài đặt.
- Đây là skill viết PROMPT, không tự sinh video — vẫn cần tài khoản Seedance 2.0/Dreamina/
  Jimeng hoặc API BytePlus/Volcengine để chạy ra clip thật (có phí theo nền tảng đó).
- 33 ví dụ có sẵn cho nhiều thể loại (sản phẩm, MV, kinh dị, tài liệu...) — nên xem qua trước
  khi viết ý tưởng riêng để hiểu đúng "công thức đạo diễn" bộ này áp dụng.

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng vấn đề "prompt phẳng ra kết quả chung chung" bằng cách ép tư duy
  đạo diễn thật (ý đồ cảnh trước, kỹ thuật sau); modular 23 skill tiết kiệm token; giữ nhất
  quán giọng kể xuyên suốt clip dài — rất hợp làm B-roll/motion cho nội dung nhiều tập.
- Điểm yếu: phụ thuộc Seedance 2.0 đang bị siết bởi vấn đề bản quyền (tính tới thời điểm ghi
  nhận gần nhất), cần luôn chạy bước copyright-check; chỉ là lớp prompt, vẫn cần trả phí nền
  tảng chạy model thật.
- Có nên dùng không: 8/10 — đáng dùng cho content cần B-roll/motion chất lượng cao (Airfare
  Decoded, kênh AI review) thay vì tự viết prompt tay; luôn nhớ bước copyright-check trước khi
  generate.

## Link
- Repo: https://github.com/Emily2040/seedance-2.0
- Bản liên quan (fork/đóng gói Codex): https://github.com/zhishu51/seedance-2.0-director
