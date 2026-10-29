# PIPELINE — 7 bước từ nhu cầu thô đến tool chạy

Mỗi bước có đầu ra, cổng PASS/FAIL và người duyệt. FAIL thì không sang bước sau. Không "sửa mong đợi cho qua".

## Phân mức trước khi làm (Claude chọn, nói rõ lý do một câu)

| Mức | Là gì | Đường đi |
|---|---|---|
| **A** | Việc nhỏ, dùng một lần hoặc vài lần, chủ dùng một mình, không dữ liệu nhạy cảm | Bỏ DSH. `TOOL-SPEC` rút gọn (đầu vào/ra + 3 ca kiểm). Antigravity hoặc Gemini Spark làm một mình, Claude đọc nhanh trước khi chủ dùng |
| **B** | Công cụ nội bộ lặp lại, nhân viên dùng | Đủ 7 bước |
| **C** | Mầm sản phẩm, có thể bán hoặc nhân bản cho khách | 7 bước + tách cấu hình theo khách + soát bảo mật kỹ hơn (QA-GATE mục C) |

Không chắc B hay C thì coi là C. Chưa rõ A hay B thì coi là B.

## Bước 0. Tiếp nhận

- **Đầu vào:** nhu cầu thô của chủ (một câu, ảnh chụp, đoạn text dán, hoặc một framework dài).
- **Làm:** Claude trả lời được 5 câu: vấn đề thật là gì; đầu vào/ra ở dạng gì; ai dùng; mức A/B/C; có dữ liệu nhạy cảm không. Thiếu thông tin mà có thể làm hỏng kết quả: **hỏi tối đa 3 câu**. Thiếu nhỏ: tự chọn mặc định, ghi giả định, làm tiếp.
- **Cổng PASS:** viết được một câu **"làm gì → ra gì → cho ai"**. FAIL nếu không viết được: chưa sẵn sàng.
- **Người duyệt:** chủ (đọc một câu xác nhận).

## Bước 1. TOOL-SPEC

- **Đầu ra:** `tasks/<id>/TOOL-SPEC.md` theo `templates/TOOL-SPEC.md`: câu ba vế, mức A/B/C, đầu vào/ra, **hợp đồng giao diện JSON** (tên trường, kiểu, ví dụ), công thức viết bằng chữ thường chép được vào Excel, ngưỡng đánh dấu "đề xuất, chỉnh được", ít nhất **3 ca kiểm với dữ liệu mẫu và kết quả mong đợi**, các giả định, thứ tool **không** làm.
- **Cổng PASS:** mỗi ngưỡng số có nguồn hoặc nhãn `[CẦN VERIFY]`; mỗi công thức thiếu trọng số được đề xuất giá trị mặc định và ghi là giả định; mọi ca kiểm tính được bằng tay; hợp đồng JSON đủ để hai tay làm song song không cần hỏi nhau.
- **Người duyệt:** chủ đọc nhanh, nói OK hoặc sửa.

## Bước 2. Giao việc

- Claude tạo `tasks/<id>/` và giao hai tay kèm brief (`briefs/`) và `TOOL-SPEC.md`. Mức A bỏ phần DSH.
- **Cổng PASS:** mỗi tay xác nhận hiểu hợp đồng JSON và vùng sở hữu (TEAM-CHARTER mục 4).

## Bước 3a. Logic (DSH)

- **Đầu ra:** `logic/` + test + `BUILD-REPORT-logic.md`. Báo cáo ghi: test nào PASS/FAIL thật (kèm lệnh chạy), gói đã dùng, phần chưa làm, giả định.
- **Cổng PASS:** mọi ca kiểm trong spec chạy được và đúng; không hardcode khoá; không phụ thuộc gói ngoài danh sách. **FAIL** nếu báo "xong" mà không có kết quả chạy.

## Bước 3b. Giao diện (Antigravity), chạy song song với 3a

- **Đầu ra:** `ui/` một file HTML chạy trên điện thoại, nối vào hợp đồng JSON, ô nhập có dữ liệu mẫu bấm là chạy; `BUILD-REPORT-ui.md`.
- **Cổng PASS:** giao diện chạy với dữ liệu mẫu giả (mock theo hợp đồng) trước khi logic xong; thông báo lỗi tiếng Việt dễ hiểu; ngưỡng và trọng số đọc từ `config.json`.

## Bước 4. Cổng QA (Claude)

- Làm theo `QA-GATE.md`: chạy lại ca kiểm, nối UI với logic thật, đọc code, soát bảo mật, soát công thức với spec.
- **Đầu ra:** `QA-VERDICT.md` ghi **ĐẠT** hoặc **KHÔNG ĐẠT**, từng mục PASS/FAIL, ai phải sửa gì, số vòng.
- **KHÔNG ĐẠT:** trả đúng tay có lỗi. Lỗi lặp 3 vòng thì escalation.

## Bước 5. Deploy (Antigravity, sau OK của chủ)

- Claude xin chủ OK, nêu rõ: tool nào, deploy ở đâu, mở cổng nào, dữ liệu lưu ở đâu. Chủ nói OK mới làm (L2).
- **Đầu ra:** link chạy được, `BUILD-REPORT-deploy.md` (lệnh đã chạy, cách khởi động lại, cách gỡ).
- **Cổng PASS:** mở link thấy tool chạy với dữ liệu mẫu; log không chứa khoá hoặc dữ liệu khách; có cách gỡ.

## Bước 6. Ghi sổ

- Claude cập nhật `TOOL-LOG.md` (tool, mức, ngày, vòng QA, link, ghi chú) và chạy lại kiểm khi chủ báo lỗi. Tool đáng nhân bản: đề xuất entry vào kho và một dòng `CHANGELOG-DECISIONS.md` (chủ duyệt).
- **Cổng PASS:** có dòng log thật sau tuần đầu dùng; **FAIL (cảnh báo)** nếu hai tuần liền không ai dùng và không ai báo.

## Tiêu chí gỡ

Tool 6 tháng không ai mở: đề xuất gỡ (tắt, lưu mã, ghi lý do, cập nhật log). Chủ quyết.
