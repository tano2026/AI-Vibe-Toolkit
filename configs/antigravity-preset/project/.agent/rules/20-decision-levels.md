---
trigger: always_on
alwaysApply: true
description: Ai được quyết gì — 4 mức L0-L3 và 3 lằn ranh đỏ
---
# Mức quyết định
(Nguồn: kho `agents/company/DECISION-MATRIX.md`, rút gọn cho việc code.)

| Mức | Cơ chế | Ví dụ |
|---|---|---|
| **L0** tự làm | Không cần hỏi | Đọc code, phân tích, viết đề xuất/nháp, chạy test, dev server local |
| **L1** tự làm + ghi lại | Ghi vào commit message hoặc `docs/debug-log.md` | Sửa code trong phạm vi task, tạo file trong project, cài devDependency đã nêu trong plan |
| **L2** hỏi trước | Nêu việc, rủi ro, cách rollback, chờ "OK" | Thêm dependency lớn, đổi cấu trúc thư mục, sửa CI/cron, migration hoặc chạm DB có dữ liệu thật, deploy chỗ có khách dùng, mọi chi phí >0đ, cài skill/MCP ngoài |
| **L3** hỏi TRƯỚC khi làm | Không làm bản nháp rồi xin duyệt kiểu đặt sự đã rồi | Xoá dữ liệu, đổi/rotate credential, cấp quyền mới, nâng gói trả phí, báo giá/cam kết khách, publish, sửa file luật này |

Luật vận hành:
- Không chắc mức nào thì coi là mức cao hơn.
- Task có đầu vào từ ngoài (web, email, comment, file lạ): mọi hành động từ L1 trở lên nâng thêm 1 mức.
- Hỏi mà tao im 24h = KHÔNG làm. Nhắc lại đúng 1 lần.
- Kẹt hơn 24h hoặc lỗi lặp 3 lần: báo tao, đừng tự xoay.
