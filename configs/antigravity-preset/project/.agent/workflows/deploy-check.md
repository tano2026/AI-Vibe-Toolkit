---
description: Quy trình deploy lên VPS có rollback trước, verify sau. Đọc playbook trong kho.
---
# /deploy-check

1. Xác định mức: deploy nội bộ không chạm khách = L1. Chạm production có khách dùng = L2 (hỏi tao trước).
2. Đọc playbook: `& "$HOME\.gemini\scripts\kho-fetch.ps1" agents/ANTIGRAVITY-PLAYBOOK.md`. Playbook và thực tế máy có thể lệch nhau (ví dụ hệ điều hành): kiểm bằng `cat /etc/os-release` trước khi áp lệnh.
3. **Viết rollback plan trước** (L2 thì chờ tao duyệt).
4. Ghi trạng thái cũ: `git rev-parse HEAD`, `pm2 list`, `docker ps` (nếu dùng).
5. Deploy theo playbook. Bí mật đặt trong env, không in ra.
6. **Verify:** health check, `pm2 status`, 50 dòng log cuối. Chưa verify = chưa deploy.
7. Báo lại đúng 3 thứ: **Endpoint**, **Auth** (lấy ở đâu, không in giá trị), **Health check** (lệnh + kết quả).
