# SMOKE-REPORT — kiểm sử dụng kho (2026-10-19)

> Kết quả tổng hợp của ba lớp kiểm. **Không lớp nào là "dùng thật trong dự án"**: `USAGE-LOG` vẫn trống. Đây là kiểm bằng cách mô phỏng và chạy cục bộ với dữ liệu giả, không mạng, không credential. Mã công cụ bên thứ ba **chưa chạy**.

## 1. Skill dạng prompt: mô phỏng sử dụng bằng văn bản (172 mục)
Mỗi skill được đọc nguyên văn, đặt một tình huống thử thật của agency, thực hiện đúng theo skill, rồi chấm. Dữ liệu: `catalog/smoke/skill-a1..a4.json`, tổng hợp `catalog/smoke.json`, cột `kiem_su_dung` trong CATALOG.csv.

| Nhóm | Số mục | pass | partial | fail | không áp dụng |
|---|---|---|---|---|---|
| skill-agent (kho tự viết) | 82 | 29 | 51 | 1 | 1 |
| skill-kho | 27 | 8 | 15 | 2 | 2 |
| skill-import (mẫu phân tầng) | 63 | 26 | 30 | 5 | 2 |
| Tổng | 172 | 63 | 96 | 8 | 5 |

Số liệu theo nhóm lấy từ báo cáo từng lô; tổng khớp `catalog/smoke.json`. Phần lớn là `partial`, nghĩa là dùng được nhưng cần bổ sung. Vấn đề phổ biến:
1. **Gắn cứng thương hiệu** (ABTRIP, Trùm Sân Bay, Tano, Wonder Mart) ở hơn 60 lần: khó tái dùng cho khách khác.
2. **Cần công cụ ngoài mà không nêu cách có** (Airtable, vidIQ, Apify, VPS, ffmpeg...) hơn 60 lần.
3. **Mâu thuẫn nội bộ** (ngưỡng retention 65% so với 70%, ngưỡng scale 20% so với 30%, ví dụ lệch quy trình).
4. **Thiếu guardrail ở việc rủi ro** (đăng, gửi email, chi tiền, tự merge) khoảng 30 lần.
5. **Tham chiếu hỏng** (file kho không tồn tại, lõi skill nằm ngoài kho).
6. **Lệnh nguy hiểm** trong skill nhập hàng loạt (`curl | bash`, `--break-system-packages`, ghi token vào `/etc`): chỉ ghi nhận.

Skill fail: `aviation-knowledge` (sai sự kiện về terminal sân bay do người chấm tự đánh giá, chưa đối chiếu nguồn), `markdown-converter`, `voxstyle-prompt-engine`, `conversion-ops`, `digital-product-factory`, `nanoclaw-repl`, `social-push-multi`, `yuanbao`.

## 2. Mã do kho tự viết: chạy cục bộ (43 nhóm file)
Chi tiết: `catalog/smoke/code.json`, `catalog/smoke/CODE-REPORT.md`. Cú pháp 41 ok, 2 lỗi theo thiết kế (khuôn có `{{...}}`); import 17 ok, 3 lỗi; chạy thử 26 ok, 5 lỗi, 12 không chạy được. Lỗi nặng nhất, tôi đã đối chiếu 4 lỗi trong file gốc:
- `agents/trum-san-bay/agent.py` gọi `llm_call` nhưng **không định nghĩa** hàm đó (chỉ có trong tài liệu skill): `orchestrator.py` không import được, các luồng sinh nội dung chết.
- `publish_post_safe` coi `0 == 0` là xong khi chưa cấu hình platform nào: báo `success`, ghi `POSTED`.
- `skills/ecc` không tồn tại nhưng `configs/sync-to-openclaw.sh` sao chép từ đó và dừng; `deploy/auto-sync.sh` dừng sau khi `git pull` nên lần sau không bao giờ đồng bộ lại.
- `compliance-gate` dùng `history[-5:]`; subagent báo đó là 5 bản ghi cũ nhất nếu lịch sử xếp mới nhất đầu (chưa kiểm thứ tự lưu).
Luồng chạy đúng khi mock: chặn đăng khi chưa `APPROVED`, idempotency, retry backoff, làm mới token, phân loại 4 nhãn bình luận.

## 3. Hành vi agent do nhà máy dựng (45 tình huống, 3 agent)
Chi tiết: `catalog/smoke/behavior.json`, `agents/agent-factory/examples/KET-QUA-HANH-VI.md`. 26 pass, 16 partial, 3 fail; cả 45 giữ ba lằn ranh đỏ **trên giấy** (nút dừng, hàng đợi duyệt, ghi log chưa có mã). Lỗ hổng thiết kế lớn nhất: tài liệu im lặng về **số thẻ, CVV, giấy tờ khách gửi trong tin nhắn**, và theo chữ "ghi nguyên văn" thì dữ liệu này lan sang Telegram, log, Airtable. Còn: `compliance-gate` bị trỏ sai chức năng trong OPC; không có câu xác nhận tạm cho khách khi chuyển CEO; mâu thuẫn L1/L2 ở gói Facebook; thiếu cổng cho tin gửi đối tác; lỗi hệ thống không có đường báo thay thế.

## 4. Công cụ bên thứ ba: bộ chạy cách ly, CHƯA CHẠY
`tools/smoke_sandbox.py` + `catalog/smoke-specs.json` (22 spec: 14 chưa duyệt, 8 cần người đọc kỹ, 0 đã duyệt) + `catalog/SMOKE-RUNBOOK.md`. Mặc định chỉ in kế hoạch. Chạy thật phải do bạn: cần Docker, cờ `--chay-that --toi-da-doc-spec`, và chỉ chạy spec bạn đã duyệt. Khuyên chạy thử 3 mục nhẹ trước (`mcp-use`, `markitdown`, `gsap-skills`).

## 5. Giới hạn trung thực
- Mô phỏng bằng model có thể chấm sai; ranh giới pass và partial là phán đoán. Tôi chỉ kiểm lại vài phát hiện cụ thể trong file gốc, không kiểm hết 172 mục.
- skill-import chỉ kiểm mẫu 63 trong 460 mục; 338 mục `dung-duoc-ngay` của kiểm toán tĩnh chưa mô phỏng hết.
- Chưa mục kho nào có dòng `USAGE-LOG` (dùng thật trong dự án).

## 6. Cập nhật sau khi sửa (2026-10-19)
Hai nhóm lỗi nghiêm trọng ở mục 2 và 3 đã được sửa và có test (mock, mô phỏng): 162 test trong `tools/tests`, 37 test trong `agents/trum-san-bay/tests`; hai ví dụ nhà máy `kiem` PASS với thêm 4 mục kiểm mới. Giới hạn: bằng chứng vẫn là mock và mô phỏng trên giấy; bộ lọc che dữ liệu nhạy cảm, nút dừng, hàng đợi duyệt và chống đăng đôi chưa có mã; Postiz mặc định chỉ tạo bản nháp cho đến khi đặt `POSTIZ_POST_TYPE=now`; chưa chạy với credential thật.
