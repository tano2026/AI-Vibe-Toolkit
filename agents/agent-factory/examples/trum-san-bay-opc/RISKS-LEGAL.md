# RISKS-LEGAL — Bảng rủi ro và pháp lý cho CEO điền, OPC `trum-san-bay-opc`

> **DEMO dựng từ thiết kế NHÁP chưa duyệt (agents/trum-san-bay/OPC-DESIGN-NOTES.md, dừng sau Phần 2 trên 5 phần). Không phải kế hoạch triển khai, chưa chạy gì.**

> **Đây không phải tư vấn pháp lý.** Bảng chỉ liệt kê chỗ thiết kế cần CEO hoặc luật sư/kế toán quyết. Công cụ không biết
> luật hiện hành, không điền văn bản pháp luật, không điền số. Mọi ô `CHƯA CÓ — hỏi CEO` phải do người có thẩm quyền điền trước khi
> bật pha liên quan (xem `PHASES.md`). Thiết kế chỉ chừa chỗ cắm; kho không thay luật sư.

## A. Rủi ro pháp lý và tài chính (CEO và luật sư/kế toán điền)

| # | Chủ đề | Câu hỏi cần trả lời | Liên quan pha/cổng | Người chịu trách nhiệm | Trả lời / quyết định | Ngày |
|---|---|---|---|---|---|---|
| L1 | Pháp nhân thu tiền khách | Pháp nhân/tài khoản nào thu tiền của khách? Có đủ điều kiện kinh doanh dịch vụ này không? | Đơn và tiền; G4, G5 | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L2 | Hoá đơn và thuế | Xuất hoá đơn, kê khai thuế cho tiền thu hộ và hoa hồng như thế nào? | Đơn và tiền | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L3 | Điều khoản hoàn tiền và khiếu nại | Điều kiện hoàn tiền, thời hạn, ai quyết, thông báo cho khách ở đâu? | Chat và bán; G3, G5 | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L4 | Hợp đồng với đối tác thực hiện | Mẫu hợp đồng, chia hoa hồng, trách nhiệm khi đối tác làm sai, bảo mật dữ liệu khách chia sẻ cho đối tác? | Đơn và tiền; G7 | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L5 | Quy định quảng cáo và affiliate | Quy định công bố quan hệ thương mại/quảng cáo trên từng nền tảng và theo luật hiện hành áp dụng cho nội dung của bạn là gì? | Nội dung; G1 | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L6 | Dữ liệu thanh toán và giấy tờ khách gửi vào chat | Khách dán số thẻ, CVV, OTP, CCCD vào chat hay bình luận: có nghĩa vụ gì, ai xoá tin gốc, lưu hay xoá bản đã che ở đâu và bao lâu, thông báo cho khách thế nào? (Thiết kế chỉ chặn agent sao chép; trách nhiệm pháp lý do người có thẩm quyền xác định) | Chat và bán; G9 | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L7 | Dữ liệu cá nhân của khách | Thu thập gì, lưu ở đâu, lưu bao lâu, khách đồng ý bằng cách nào, chia sẻ với đối tác ra sao theo luật bảo vệ dữ liệu cá nhân hiện hành (người có thẩm quyền xác định văn bản áp dụng)? | Chat và bán | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L8 | Điều khoản nền tảng về tự động hoá | Điều khoản của facebook, zalo, instagram cho phép mức tự động đăng/trả lời nào? Tài khoản có thể bị khoá nếu vi phạm không? | Mọi pha có kênh | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L9 | Quyền sử dụng hình, nhạc, nội dung bên thứ ba | Nguồn ảnh/nhạc/video, giấy phép, quyền với nội dung do AI sinh? | Nội dung; G1 | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L10 | Giấy phép của công cụ đã chọn | Các mục kho đã chọn có điều khoản hạn chế dùng thương mại hoặc theo quy mô công ty không (xem cột license trong catalog và entry gốc)? | Mọi pha | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |
| L11 | Giấy phép và ràng buộc ngành | Ngành của bạn có điều kiện kinh doanh, nghĩa vụ công bố thông tin, giới hạn quảng cáo riêng không? | Nền | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |

## B. Rủi ro kỹ thuật và vận hành (đã có biện pháp trong thiết kế, chưa kiểm thật)

| # | Rủi ro | Biện pháp trong thiết kế | Còn thiếu |
|---|---|---|---|
| R1 | Nội dung ngoài điều khiển agent (prompt injection) | Luồng do code quyết; nội dung ngoài là dữ liệu; mọi hành động từ L1 tự nâng một mức | Chưa kiểm bằng thử nghiệm thật (test OT04) |
| R2 | Agent bịa thông tin | Gắn [CẦN VERIFY]; research kiểm chứng trước khi lên lô; cổng duyệt | Chưa đo tỉ lệ bịa thật |
| R3 | Lộ khoá/token | Chỉ ghi TÊN biến; tách .env theo phạm vi, chmod 600 theo `agents/company/SECURITY-WALL.md`; ghi log mỗi lần đọc file chứa khoá | Chưa thực thi trên máy thật |
| R4 | Token nền tảng hết hạn | Tự khoá kênh khi token hết hạn hoặc bị từ chối; cảnh báo sớm | Chưa có mã; ngưỡng cảnh báo sớm CHƯA CÓ — hỏi CEO |
| R5 | Bot Zalo cho khách | Dùng Zalo OA đã xác thực, không dùng nick cá nhân tự động hoá (theo ghi chú thiết kế; entry kho nói OA gói trả phí và thời gian duyệt, cần kiểm lại giá và điều kiện) | Chưa kiểm điều kiện hiện hành |
| R6 | Khách hoặc nhân viên dán thẻ, CVV, OTP, giấy tờ vào chat | GATES Luật vận hành 10: che trước khi lưu, cột `message_masked`, mẫu trả lời nhắc kênh thanh toán chính thức, đề xuất người xoá tin gốc (G9) | Bộ lọc ở lớp nhận tin chưa có mã (test OT11) |
| R7 | Khách bị chuyển CEO nhưng im lặng nhiều giờ | GATES Luật vận hành 11: MỘT câu xác nhận tạm đã duyệt, SLA người duyệt, nhắc một lần | Câu xác nhận tạm và SLA do CEO điền (PACK mục 7) |
| R8 | Airtable, kênh duyệt hoặc cờ paused không đọc được | GATES Luật vận hành 12 và workflow 3.1: fail-closed, nhật ký tạm cục bộ, báo Telegram trực tiếp, chống đăng đôi | Chưa có mã (test OT13); đường báo thay thế phụ thuộc Telegram |
| R9 | Hạ tầng một điểm hỏng | UNIFIED-ARCHITECTURE ghi ngày 25/07/2026 VPS đang DOWN và hệ thống chạy 100% Local Windows; kiểm lại hiện trạng trước khi bật kênh cần 24/7 | Hiện trạng hạ tầng chưa kiểm lại trong khung này |
| R10 | Sai lệch đối soát tiền | Đối soát hằng tuần; G4/G5 duyệt từng lệnh; agent không chuyển tiền | Cổng thanh toán và quy trình hoàn tiền chưa có trong kho |

## C. Ghi chú

- Chủ thể thu tiền, hoá đơn, hoàn tiền và dữ liệu cá nhân của khách là việc của CEO và chuyên gia. Agent không quyết các việc này (G4, G5, G7).
- Quy định quảng cáo và affiliate khác nhau theo nền tảng và thay đổi theo thời gian: agent luôn gắn `[CẦN VERIFY]`. Bài có link affiliate hoặc tài trợ đi qua bước kiểm chú thích TRƯỚC cổng duyệt, gồm: `kho:agents/shorts-affiliate-system/skills/platform-disclosure-adapter` (bật nhãn nội dung AI theo từng nền tảng), `kho:agents/shorts-affiliate-system/skills/affiliate-disclosure-writer` (viết dòng công bố affiliate) và checklist chú thích do CEO duyệt. **HỔNG:** kho chưa có skill kiểm theo quy định quảng cáo (FTC, quy định quảng cáo Việt Nam); hai skill trên chỉ viết và bật nhãn, không kiểm tuân thủ luật. Chừng nào chưa có, người duyệt (CEO hoặc luật sư) tự kiểm bằng checklist. `compliance-gate` trong kho (`kho:agents/shorts-affiliate-system/skills/compliance-gate`) chỉ chặn lặp cấu trúc script YouTube bằng so dấu vân tay, KHÔNG kiểm chú thích; không được dùng dấu "đã qua compliance-gate" thay cho kiểm chú thích. Việc xác nhận cuối cùng là của người.
- Dữ liệu thanh toán và giấy tờ khách gửi vào chat (thẻ, CVV, OTP, CCCD): thiết kế chỉ chặn việc agent sao chép (GATES Luật vận hành 10); trách nhiệm pháp lý khi dữ liệu đã nằm trên nền tảng chat thuộc về CEO và chuyên gia.
- Bảng này nên được rà lại mỗi quý cùng `GATES.md`.
