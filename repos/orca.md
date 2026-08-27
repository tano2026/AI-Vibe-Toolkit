# Orca (stablyai/orca) — GitHub Repo

## TL;DR
Orca là "ADE" (Agent Development Environment) — app desktop/mobile/VPS cho phép chạy nhiều coding agent (Claude Code, Codex, Cursor, OpenClaw, Antigravity, Hermes Agent...) song song, mỗi con trong 1 git worktree riêng, quản lý tập trung 1 chỗ. 53.7k star, MIT license, ship daily.

## Repo này dùng để làm gì
Vấn đề nó giải quyết: khi vibe code, mình hay chạy nhiều agent cùng lúc cho nhiều task khác nhau (hoặc chạy cùng 1 task với nhiều agent để so kết quả) — nhưng quản lý bằng tay (mở nhiều terminal, nhớ agent nào đang làm gì) rất rối. Orca gom hết vào 1 app: mỗi agent chạy trong 1 "worktree" (bản sao code cô lập của Git), Orca theo dõi tiến độ, cho review diff, merge kết quả thắng.

Điểm hay nhất so với các tool orchestrator khác: **không tự có model riêng** — Orca chỉ là lớp điều phối, dùng subscription/CLI có sẵn của mình (Claude Code, Codex...) chứ không tính phí theo token riêng.

## Setup từng bước
1. Tải app desktop: `https://onorca.dev/download` (macOS/Windows/Linux) hoặc build trực tiếp từ GitHub Releases
2. macOS qua Homebrew: `brew install --cask stablyai/orca/orca`
3. Arch Linux (AUR): `yay -S stably-orca-bin`
4. Chạy headless trên VPS: dùng lệnh `orca serve` (có hướng dẫn riêng trong docs/reference/headless-linux-server.md của repo) — đây là cách phù hợp nhất để dùng chung với VPS Tencent Cloud đang chạy Hermes/OpenClaw/Antigravity
5. Kết nối app mobile (iOS App Store / Android APK) để theo dõi/điều khiển agent từ điện thoại
6. Trỏ Orca vào git repo cần làm việc, chọn agent (Claude Code, Codex, OpenClaw, Antigravity, hoặc bất kỳ CLI agent nào), tạo worktree mới

## Ví dụ thực tế
Tình huống: đang sửa 1 bug trong `tano.agency` repo nhưng không chắc cách fix nào tốt hơn.
- Input: 1 prompt fix bug, chạy cùng lúc trên 2 worktree — 1 dùng Claude Code, 1 dùng Codex
- Output: Orca hiển thị song song 2 diff, Design Mode cho phép click vào UI thật để lấy HTML/CSS/screenshot ném thẳng vào prompt agent nếu bug liên quan giao diện, review xong chọn bản thắng để merge — không cần tự tay so sánh 2 branch bằng git diff thủ công

## Lưu ý / Lỗi thường gặp
- Đây là app desktop/Electron — không phải thứ chạy trực tiếp trong Hermes (Python urllib-only), phải dùng qua `orca serve` trên VPS hoặc app riêng, không nhét vào pipeline agent hiện tại của Hermes được
- "Hermes Agent" trong danh sách agent hỗ trợ của Orca là Hermes của Nous Research — KHÁC hoàn toàn với Hermes VPS đang dùng, dễ nhầm khi đọc README
- Mobile companion app cần pair với desktop trước, không hoạt động độc lập
- Repo ship rất nhanh (9000+ commit), API/CLI có thể đổi giữa các bản — theo dõi CHANGELOG trước khi tự động hoá quy trình dựa vào Orca CLI

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng pain point vibe coder chạy nhiều agent song song; dùng subscription sẵn có không tốn thêm token riêng; hỗ trợ SSH remote worktree (chạy agent trên VPS mạnh, sửa/review từ máy yếu); có Orca CLI để agent tự script điều khiển Orca
- Điểm yếu: là 1 app riêng cần cài, không tích hợp thẳng vào workflow Hermes/OpenClaw hiện tại của Nobitano trừ khi chạy `orca serve` song song trên cùng VPS; chưa rõ mức ổn định khi self-host headless trên Ubuntu so với desktop; không phải giải pháp cho việc chạy agent 24/7 tự động (vẫn cần người ngồi review/merge)
- Có nên dùng không: 7/10 — hữu ích khi Nobitano cần so sánh output nhiều agent cho 1 task khó, nhưng không thay thế được pipeline Hermes/OpenClaw đang chạy nền tự động

## Link
- Repo: https://github.com/stablyai/orca
- Docs/Demo: https://onorca.dev

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Orca là app desktop/Electron, không có REST API public để Hermes gọi trực tiếp.
# Cách duy nhất Hermes tương tác được là qua "orca serve" CLI trên VPS (subprocess),
# KHÔNG dùng urllib vì đây không phải HTTP API — dùng subprocess.run thay thế.
import subprocess

def orca_worktree_create(repo_path, agent="claude-code"):
    # Yêu cầu: đã cài Orca CLI trên VPS qua orca serve setup
    result = subprocess.run(
        ["orca", "worktree", "create", "--repo", repo_path, "--agent", agent],
        capture_output=True, text=True
    )
    return result.stdout
```
> ⚠️ Đây là subprocess call, không phải HTTP request — không tương thích với ràng buộc "urllib only, no external packages" nếu Hermes cần chạy hoàn toàn cô lập. Cần Orca binary đã cài sẵn trên VPS.

### OpenClaw
```bash
# OpenClaw có thể trigger Orca CLI qua npx pattern nếu cần kích hoạt worktree mới từ Telegram command
orca worktree create --repo /path/to/repo --agent openclaw --prompt "fix bug X"
```

### Antigravity
```bash
# Cài Orca headless trên VPS Tencent Cloud (Ubuntu)
curl -fsSL https://onorca.dev/install.sh | sh
orca serve --port 4200 --headless
# Sau đó pair từ app mobile hoặc dùng Orca CLI để điều khiển từ xa
```
> ⚠️ Cần test kỹ trên Ubuntu 22.04 hiện có — README chỉ liệt kê macOS/Windows/Linux desktop chính thức, chế độ headless server là tài liệu riêng, có thể có giới hạn tính năng so với bản desktop.
