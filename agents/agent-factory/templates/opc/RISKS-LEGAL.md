# RISKS-LEGAL — Bảng rủi ro và pháp lý cho CEO điền, OPC `{{slug}}`

> **Đây không phải tư vấn pháp lý.** Bảng chỉ liệt kê chỗ thiết kế cần CEO hoặc luật sư/kế toán quyết. Công cụ không biết
> luật hiện hành, không điền văn bản pháp luật, không điền số. Mọi ô `CHƯA CÓ — hỏi CEO` phải do người có thẩm quyền điền trước khi
> bật pha liên quan (xem `PHASES.md`). Thiết kế chỉ chừa chỗ cắm; kho không thay luật sư.

## A. Rủi ro pháp lý và tài chính (CEO và luật sư/kế toán điền)

| # | Chủ đề | Câu hỏi cần trả lời | Liên quan pha/cổng | Người chịu trách nhiệm | Trả lời / quyết định | Ngày |
|---|---|---|---|---|---|---|
{{LEGAL_ROWS}}

## B. Rủi ro kỹ thuật và vận hành (đã có biện pháp trong thiết kế, chưa kiểm thật)

| # | Rủi ro | Biện pháp trong thiết kế | Còn thiếu |
|---|---|---|---|
{{TECH_ROWS}}

## C. Ghi chú

- Chủ thể thu tiền, hoá đơn, hoàn tiền và dữ liệu cá nhân của khách là việc của CEO và chuyên gia. Agent không quyết các việc này (G4, G5, G7).
- Quy định quảng cáo và affiliate khác nhau theo nền tảng và thay đổi theo thời gian: agent luôn gắn `[CẦN VERIFY]`. Bài có link affiliate hoặc tài trợ đi qua bước kiểm chú thích TRƯỚC cổng duyệt, gồm: `kho:agents/shorts-affiliate-system/skills/platform-disclosure-adapter` (bật nhãn nội dung AI theo từng nền tảng), `kho:agents/shorts-affiliate-system/skills/affiliate-disclosure-writer` (viết dòng công bố affiliate) và checklist chú thích do CEO duyệt. **HỔNG:** kho chưa có skill kiểm theo quy định quảng cáo (FTC, quy định quảng cáo Việt Nam); hai skill trên chỉ viết và bật nhãn, không kiểm tuân thủ luật. Chừng nào chưa có, người duyệt (CEO hoặc luật sư) tự kiểm bằng checklist. `compliance-gate` trong kho (`kho:agents/shorts-affiliate-system/skills/compliance-gate`) chỉ chặn lặp cấu trúc script YouTube bằng so dấu vân tay, KHÔNG kiểm chú thích; không được dùng dấu "đã qua compliance-gate" thay cho kiểm chú thích. Việc xác nhận cuối cùng là của người.
- Dữ liệu thanh toán và giấy tờ khách gửi vào chat (thẻ, CVV, OTP, CCCD): thiết kế chỉ chặn việc agent sao chép (GATES Luật vận hành 10); trách nhiệm pháp lý khi dữ liệu đã nằm trên nền tảng chat thuộc về CEO và chuyên gia.
- Bảng này nên được rà lại mỗi quý cùng `GATES.md`.
