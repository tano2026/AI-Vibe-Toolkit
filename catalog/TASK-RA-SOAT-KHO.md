# NHIỆM VỤ RÀ SOÁT KHO — tổng quan

> **Antigravity làm chính** theo `catalog/TASK-ANTIGRAVITY.md` (có giai đoạn chạy thử 20 mục, chờ duyệt). Phần B dưới đây (Trio kiểm chéo mẫu) chỉ chạy **sau** khi Antigravity xong. Phần A trong file này đã được thay bằng file Antigravity.

> Người giao: Nobitano. Người nhận báo cáo và là người DUY NHẤT ghi lên kho: Claude.
> Agent **không push `main`**, không sửa TRACKER tay, không để token trong file. Chỉ ghi file kết quả riêng (tên bên dưới) rồi gửi cho Nobitano chuyển Claude.
> Mục tiêu: để agent tra kho nhận ra đúng mục theo **khả năng cần**, không phải theo tên.

## Bối cảnh (đọc 2 phút)
- Kho có 915 mục tra cứu; 455 mục do kho viết (repo/mcp/stack/skill-kho/skill-agent), 460 skill nhập hàng loạt (chỉ mô tả ngắn, không rà ở đợt này).
- Đã có bản gắn nhãn **nháp** do model phân loại tự động: `catalog/curation-draft/out{1,2,3,5,6,7,8}.json` = **398 mục**. **Chưa ai kiểm.**
- Còn **57 mục chưa gắn nhãn**: `catalog/curation-draft/batch4-chua-gan-nhan.json` (đã có digest sẵn).
- Luật gắn nhãn, bảng khả năng và các trường: `catalog/curation-draft/PROMPT-GAN-NHAN.md` (nguồn sự thật, không tự đặt giá trị mới).
- Sơ đồ lược: mỗi mục có `capability` (1–3 giá trị cố định), `use_when`, `skip_if`, `adoption`, `vessel_fit`, `needs`, `dup_group`, `confidence`.

## Phần A — Antigravity (chạy máy, không cần đọc sâu)
Đầu ra: `REPORT-antigravity.md` + (nếu có) `out4.json`.

1. **Gắn nhãn 57 mục còn thiếu** theo `PROMPT-GAN-NHAN.md` → `out4.json` (JSON list, đủ 57, cùng thứ tự). Chỉ dùng digest trong file, không bịa.
2. **Kiểm cơ học cả 455 mục** (script, không phán đoán): mỗi `id` có đúng 1 dòng; `capability` chỉ thuộc bảng 29 giá trị; `use_when` ≤140, `skip_if` ≤100 ký tự; `adoption`/`needs`/`vessel_fit` đúng giá trị cho phép; `id` tồn tại thật trong `catalog/catalog.json`. Báo số lỗi + danh sách id lỗi.
3. **Dò trùng nhóm**: gom theo `dup_group` + `capability` chính, xuất bảng "nhóm ≥3 mục cùng việc" (id, loại, điểm trong catalog). Không tự xoá/gộp.
4. **Báo cáo thiếu**: với mỗi `capability`, đếm số mục `adoption = cai-ngay-duoc` và `confidence ≠ thap`. Liệt kê khả năng có <3 mục (đây là chỗ hổng của kho).

## Phần B — Trio kiểm chứng mẫu (cần đọc entry thật)
Mỗi agent nhận một lát, kiểm **20 mục** (lấy theo `id` chia đều, bỏ mục `confidence = cao` ở lượt đầu trừ khi thiếu). Với mỗi mục: mở file entry gốc (`duong_dan` trong `catalog.json`), đối chiếu nhãn nháp.

| Agent | Lát kiểm | Việc thêm |
|---|---|---|
| Hermes | mục có `vessel_fit` chứa `hermes` (20 mục) | chạy thử `tra_kho()` trong `catalog/PLAYBOOK-DUNG-KHO.md` trên CSV, báo lỗi nếu có |
| OpenClaw | mục có `vessel_fit` chứa `openclaw` (20 mục) | thử đọc `catalog/catalog.json` từ VPS, báo có lấy được qua git clone hay không |
| DeepSeek Harness | mục `adoption = chi-tham-khao` hoặc `confidence = thap` (20 mục) | xem nhãn dựa chỉ vào digest có đủ không; nhờ OpenClaw lấy file nếu không đọc trực tiếp |

Với mỗi mục ghi một dòng: `id | nhãn đúng? (đúng / sai trường nào) | sửa đề xuất | căn cứ (trích 1 câu trong entry)`.
**Quy tắc:** không có căn cứ trong entry thì ghi "không xác định", không đoán. Tuyệt đối không cài hay chạy công cụ trong entry chỉ để kiểm nhãn.

Đầu ra: `REPORT-hermes.md`, `REPORT-openclaw.md`, `REPORT-deepseek.md`, mỗi file có bảng 20 dòng + 3 dòng kết luận: tỉ lệ nhãn đúng, lỗi hay gặp nhất, mục nào nên gỡ khỏi diện "cai-ngay-duoc".

## Phần C — Việc không được làm
- Không viết lại entry, không đổi điểm, không xoá file. Xoá cần Nobitano xác nhận.
- Không chấm điểm chất lượng; đây là phân loại.
- Không đưa token vào báo cáo; dùng `[GITHUB_TOKEN]`.
- Không phỏng đoán số sao, số người dùng.

## Báo cáo gửi lại (một khối, tối đa 1 trang)
```
TỔNG: kiểm <n> mục, nhãn đúng <n> (<%>)
LỖI HAY GẶP: ...
KHẢ NĂNG THIẾU MỤC: ...
NHÓM TRÙNG: ...
ĐỀ XUẤT CHO CLAUDE: (tối đa 5 dòng)
```
Claude sẽ gộp, sửa theo báo cáo, cập nhật `tools/build_catalog.py` + trang tra cứu rồi mới push. **Cho đến lúc đó, nhãn trong `curation-draft/` là NHÁP, không dùng làm quyết định.**
