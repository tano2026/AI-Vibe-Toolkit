---
trigger: always_on
alwaysApply: true
description: Kỷ luật code — nghĩ trước, đơn giản, sửa đúng phạm vi, verify bằng bằng chứng
---
# Kỷ luật code
(Nguồn: kho `skills/karpathy-coding-guidelines` + `agents/company/EXPERT-CORE.md` mục Dev. Việc nhỏ và rõ thì được nới bớt thận trọng.)

1. **Nghĩ trước khi code.** Nêu giả định. Có nhiều cách hiểu thì trình bày, không tự chọn rồi lặng lẽ làm. Không rõ thì dừng, gọi tên chỗ mơ hồ, hỏi.
2. **Đơn giản trước.** Code tối thiểu giải quyết đúng vấn đề. Không thêm tính năng ngoài yêu cầu, không abstraction cho code dùng một lần. Viết 200 dòng mà rút được còn 50 thì viết lại.
3. **Sửa đúng phạm vi.** Mỗi dòng diff phải truy ngược về yêu cầu. Không refactor hay chỉnh format phần lân cận. Chỉ dọn phần thừa do chính mình gây ra. Thấy dead code cũ thì nhắc, không tự xoá.
4. **Mục tiêu đo được.** Bug: viết test tái hiện trước, rồi làm cho pass. Việc nhiều bước: ghi `bước → verify: cách kiểm`.
5. **Debug theo trình tự cứng:** tái hiện → cô lập → root cause (không fix triệu chứng) → fix → verify → ghi 5 dòng vào `docs/debug-log.md`. Không tái hiện được lỗi thì đó là đoán mò.
6. **Chạm hệ thống thật** (server, DB, deploy): viết rollback plan trước → ghi lại trạng thái cũ → đổi → verify bằng lệnh cụ thể → log. Deploy xong chưa verify = chưa deploy.
7. **Script chạy lặp phải idempotent**, mọi call ra ngoài có timeout, lỗi thì báo to (không nuốt exception), dependency pin version.
8. **Chống luẩn quẩn:** cùng một lỗi sau 3 lần thử thì DỪNG, báo cái đã thử và đã loại trừ, hỏi hướng. Việc mức L2/L3 không tự loop thử nhiều phương án: soạn 1 bản gọn rồi hỏi sớm.
