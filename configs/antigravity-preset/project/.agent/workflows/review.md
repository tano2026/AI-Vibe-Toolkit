---
description: Tự review diff trước khi commit hoặc merge. Báo PASS/FAIL từng mục kèm bằng chứng, không tự sửa.
---
# /review

Chạy `git diff` (và `git status`). Với mỗi mục ghi PASS/FAIL + bằng chứng (dòng hoặc output lệnh):

1. **Phạm vi:** mỗi dòng diff truy ngược được về yêu cầu. Có thay đổi thừa không?
2. **Test:** chạy lệnh test trong `AGENTS.md`. Bug fix có test tái hiện chưa?
3. **Bảo mật:** có bí mật hardcode, `.env` bị track, lệnh phá huỷ, dependency mới chưa duyệt?
4. **Đơn giản:** có abstraction hay tính năng ngoài yêu cầu không?
5. **UI (nếu có):** đã qua `/ui-check`? Tương phản, focus, alt?
6. **Rollback:** nếu chạm hệ thống thật, rollback plan có chưa?

Kết: danh sách FAIL theo mức nghiêm trọng. Không tự sửa. Không commit.
