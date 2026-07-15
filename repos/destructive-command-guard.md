# Destructive Command Guard (dcg) — GitHub Repo

## TL;DR
Một hook chặn lệnh git/shell nguy hiểm (`rm -rf`, `git reset --hard`, `DROP TABLE`...) trước khi AI agent kịp chạy — bảo vệ code/data khỏi việc agent tự tay phá hoại. Hỗ trợ sẵn Claude Code, Hermes Agent, Cursor, Codex CLI và nhiều tool khác.

## Repo này dùng để làm gì
AI coding agent thỉnh thoảng chạy nhầm lệnh phá hoại — xoá cả folder, reset git mất hết commit chưa lưu, xoá bảng database — vì nó không "hiểu" hậu quả như người. dcg đứng chắn giữa agent và terminal: mọi lệnh trước khi thực thi đều bị nó soi qua bộ rule (50+ pack: database, Kubernetes, Docker, AWS/GCP/Azure, Terraform...), nếu match pattern nguy hiểm thì chặn lại kèm giải thích lý do và gợi ý cách làm an toàn hơn. Tốc độ gần như bằng 0 (SIMD-accelerated), không làm agent chậm đi.

## Setup từng bước
1. Cài nhanh (Linux/macOS/WSL):
   ```bash
   curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/main/install.sh?$(date +%s)" | bash -s -- --easy-mode
   ```
2. Windows (PowerShell native):
   ```powershell
   & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/main/install.ps1"))) -EasyMode -Verify
   ```
3. Script tự detect agent đang cài (Claude Code, Hermes Agent, Cursor, Codex CLI...) và tự cấu hình hook tương ứng — không cần chỉnh tay từng tool.
4. Bật thêm rule pack theo nhu cầu tại `~/.config/dcg/config.toml`:
   ```toml
   [packs]
   enabled = [
       "database.postgresql",
       "kubernetes.kubectl",
       "cloud.aws",
       "containers.docker",
   ]
   ```
5. Test xem hoạt động chưa: `dcg explain "git reset --hard HEAD~5"` — nó in ra lý do sẽ chặn lệnh này.

## Ví dụ thực tế
Agent (Claude Code hoặc Hermes) tự ý chạy `git reset --hard HEAD~5` để "dọn code" — dcg chặn ngay:
```
BLOCKED  dcg
Reason:  git reset --hard destroys uncommitted changes
Command: git reset --hard HEAD~5
Tip: Consider using 'git stash' first to save your changes.
```
Agent nhận output này qua stdout (machine-readable), tự hiểu lệnh bị từ chối và đổi hướng — không cần con người ngồi canh terminal 24/7.

## Lưu ý / Lỗi thường gặp
- `trust_level` trong config chỉ là nhãn ghi log, KHÔNG tự thay đổi rule — muốn nới lỏng thật sự phải chỉnh `disabled_packs`/`additional_allowlist` cụ thể.
- Thiết kế "fail-open" — nếu dcg timeout hay lỗi parse, nó KHÔNG chặn workflow (ưu tiên không làm gián đoạn hơn là an toàn tuyệt đối) → vẫn cần backup/git commit thường xuyên, đừng ỷ lại 100% vào dcg.
- Chưa hỗ trợ native đầy đủ cho một số agent (Aider chỉ có git hook, Continue chỉ detect không chặn).

## Đánh giá cá nhân
- Điểm mạnh: đúng nỗi đau thật khi chạy nhiều agent tự động 24/7 trên VPS (như Hermes/OpenClaw của tao) — 1 lệnh sai là mất data, dcg là lớp bảo hiểm rẻ tiền mà hiệu quả cao, tích hợp sẵn Hermes Agent nên gần như plug-and-play.
- Điểm yếu: fail-open nghĩa là không phải bulletproof, và rule pack mặc định có thể chưa cover hết pattern nguy hiểm đặc thù của stack riêng (vd script Python tự viết xoá file theo path động) — vẫn cần review code agent viết.
- Có nên dùng không: 8/10 — nên cài ngay cho VPS có agent chạy tự động, chi phí cài gần bằng 0, lợi ích phòng ngừa rất lớn.

## Link
- Repo: https://github.com/Dicklesworthstone/destructive_command_guard
- Docs: README trong repo (cùng docs/pi-integration.md cho tool khác)

---

## 🤖 Agent Integration

### Hermes (Python)
```bash
# dcg hỗ trợ NATIVE Hermes Agent - cài 1 lần, tự áp dụng cho mọi lệnh Hermes chạy qua shell
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/main/install.sh?$(date +%s)" | bash -s -- --easy-mode
# Sau khi cài, Hermes tự động bị chặn khi cố chạy rm -rf, git reset --hard, DROP TABLE...
# Kiểm tra: dcg explain "rm -rf /home/hermes/repo"
```

### OpenClaw
```bash
# Cài chung 1 lần trên VPS là áp dụng cho mọi agent shell-based trên máy, gồm cả OpenClaw
# nếu OpenClaw gọi lệnh qua subprocess/shell thông thường (không qua sandbox riêng)
```

### Antigravity
```bash
# Antigravity (vai trò shell/bash access) LÀ agent rủi ro cao nhất cần dcg nhất -
# nó có quyền deploy/install/maintain, dễ chạy nhầm lệnh phá VPS nhất trong 3 agent
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/main/install.sh?$(date +%s)" | bash -s -- --easy-mode
```
> ⚠️ Vẫn giữ backup/snapshot VPS định kỳ — dcg là lớp chặn bổ sung, không thay thế backup vì thiết kế fail-open khi có lỗi.
