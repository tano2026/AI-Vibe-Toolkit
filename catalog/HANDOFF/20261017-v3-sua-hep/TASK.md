# TASK — Vòng sửa hẹp cho v3 lô 2–10

Việc: Đọc lại có chủ đích 167 mục trong `worklist.json` (script chỉ lập danh sách chỗ cần xem, KHÔNG quyết nhãn), điền điều kiện loại trừ và yêu cầu còn thiếu.
Đầu vào: `worklist.json` (mỗi mục có `can_xem`: gpu, license, beta, api-key, tra-phi), nhãn hiện tại trong `catalog/curation.json`, entry gốc.
Đầu ra: `work/antigravity/v3/sua-hep.json` — chỉ các mục có đổi, cùng trường như `lo-N.json` + `evidence_skip` + `ly_do_doi`; mục xem rồi không đổi ghi `{"id":..., "giu_nguyen": true}`.
Dừng ở: nộp `sua-hep.json` + `NOTE-sua-hep.md`, chờ Claude kiểm.

Với từng mục, mở entry và đọc đúng phần liên quan, rồi:
- `gpu`: entry có yêu cầu GPU/VRAM thật → thêm `gpu` vào `needs` và nêu trong `skip_if` (kèm `evidence_skip` nguyên văn). Chỉ nhắc GPU như tuỳ chọn thì giữ nguyên.
- `license`: license phi thương mại/AGPL/GPL hay giới hạn thương mại → `skip_if` nêu rõ, `evidence_skip` nguyên văn.
- `beta`: entry nói beta/preview/alpha/chưa public → `adoption` không được là `cai-ngay-duoc`; nêu trong `skip_if`.
- `api-key`, `tra-phi`: entry bắt buộc khoá API hoặc trả phí → thêm vào `needs`, và `skip_if` nếu là điều kiện bỏ qua.
Không thấy căn cứ trong entry thì giữ nguyên, không đoán.

Làm thêm cho cả 358 mục lô 2–10:
- `use_when` giữ nguyên thuật ngữ chuẩn (API, MCP, GPU, token, LLM, RAM, 4K, VRAM) và viết số bằng chữ số. Claude đã thay tự động 56 chuỗi; kiểm lại những mục còn đọc gượng (vd "trợ lý lập trình", "tác nhân").
- Trong `NOTE-sua-hep.md` ghi trung thực: đã đọc kỹ bao nhiêu mục/phần nào, thời gian, mục không chắc. Không ghi "đọc nguyên entry" nếu chỉ đọc một phần.

Kiểm cơ học: enum hợp lệ (capability ∈ bảng 30, adoption ∈ 4 giá trị), `evidence_skip` là chuỗi con nguyên văn ≤120 ký tự, `skip_if` ≤100 ký tự bắt đầu "Bỏ qua nếu ", không "..." hay từ quảng cáo.
Hạn ngân sách: hết ngân sách thì dừng ở mục đã xong và ghi rõ.
