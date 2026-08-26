# Oh My Pi (OMP) — GitHub Repo

## TL;DR
Coding agent chạy trong terminal, fork từ pi-mono nhưng nhồi thêm cả bộ tool đầy đủ — AI commit generator, LSP integration, code review, task automation. Đang trending mạnh trên GitHub (7K+ stars, tăng +2361 chỉ trong 1 tuần lúc peak) vì tự động nhận diện config có sẵn từ Claude Code, Cursor, Windsurf, Gemini, Codex, Cline — không cần setup lại từ đầu.

## Tool này dùng để làm gì
Oh My Pi (viết tắt OMP) là "senior engineer sống trong terminal" — đọc, viết, test, debug, refactor code trực tiếp trong môi trường dev, không cần copy-paste qua lại giữa browser và editor.

Điểm hay nhất: **Universal Configuration Discovery** — lần đầu chạy, OMP tự động kế thừa rule, skill, MCP server đã có sẵn từ `.claude`, `.cursor`, `.windsurf`, `.gemini`, `.codex`, `.cline`, `.github/copilot`, `.vscode`. Không cần script migrate, không cần setup lại config đã có.

Kiến trúc extension là TypeScript module dùng chung tool API, slash-command registry, hotkey table, TUI primitives với các built-in feature — nghĩa là mở rộng OMP dễ như viết thêm 1 module, không phải học API riêng biệt.

**Time Traveling Streamed Rules (TTSR)** — rule chỉ được inject vào context khi có pattern khớp xuất hiện trong output stream của AI, tối ưu context usage, tránh tính toán thừa.

## Setup từng bước

1. Yêu cầu: Bun (JS runtime nhanh hơn Node) + Rust toolchain (cho native addon)
2. Clone repo: `git clone https://github.com/can1357/oh-my-pi`
3. Cài dependency workspace: `bun setup` (build luôn `@oh-my-pi/pi-natives`)
4. Nếu sửa Rust crate: chạy lại `bun run build:native`
5. Nếu dùng Nix: toolchain Bun/Rust đã pin sẵn qua flake, không cần cài tay
6. Chạy lần đầu — OMP tự quét và inherit config từ các tool AI khác đã có trên máy

## Ví dụ thực tế

Tình huống: mày đang có sẵn `.claude/` config trong repo `tano.agency` (rule brand context, skill fetching), muốn thử OMP nhưng không muốn viết lại config từ đầu.

- Clone OMP vào máy, chạy trong thư mục `tano.agency`
- OMP tự phát hiện `.claude/` folder, đọc rule + skill có sẵn, không hỏi lại
- Thiếu tool gì → hỏi OMP viết bổ sung, xong gõ `/reload-plugins`
- Có thể publish extension đó lên npm hoặc giữ local, tuỳ nhu cầu

## Lưu ý / Lỗi thường gặp

- Cần cả Bun **và** Rust — nếu máy chỉ có Node thì build sẽ fail, phải cài thêm Rust toolchain trước
- Fresh clone bắt buộc chạy `bun setup` trước, không skip bước native addon
- Có nhiều repo dùng tên "oh-my-pi" khác nhau trên GitHub (fork, tool phụ trợ như dashboard, vault bảo mật) — bản gốc là `can1357/oh-my-pi`, tránh nhầm với `az9713/oh-my-pi` (fork có thêm enhancement, tương thích ngược nhưng không phải bản chính)
- README nhấn khá nhiều thuật ngữ riêng (TTSR, Universal Config Discovery) — cần đọc kỹ docs trước khi dùng để hiểu đúng khái niệm

## Đánh giá cá nhân

- **Điểm mạnh:** Universal Configuration Discovery cực kỳ thực dụng — không tốn công setup lại nếu đã có config từ tool khác. 40+ LLM provider hỗ trợ, 32 built-in tool là con số ấn tượng so với Cline (~15 tool).
- **Điểm yếu:** Yêu cầu setup phức tạp hơn (cần cả Bun + Rust), không phải "cài 1 dòng lệnh là chạy" như OpenCode. Trending nhanh cũng đồng nghĩa docs/community còn đang đuổi theo tốc độ phát triển.
- **Có nên dùng không:** 7/10 — Hợp nếu mày đã có sẵn nhiều config từ Claude Code/Cursor và muốn 1 agent terminal ăn theo config đó luôn. Không phải lựa chọn đầu tiên nếu chỉ cần 1 coding agent đơn giản, dùng ngay.

## Link
- Repo: https://github.com/can1357/oh-my-pi
- Docs/Context: https://context7.com/can1357/oh-my-pi
- Bài phân tích chi tiết (tiếng Nhật, dịch máy tốt): https://note.com/kudoucraft/n/n991c4bb46fd0?hl=en

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess

def run_omp_task(prompt: str, workdir: str):
    """Gọi Oh My Pi xử lý 1 task coding trong thư mục chỉ định."""
    result = subprocess.run(
        ["omp", "run", prompt],
        cwd=workdir, capture_output=True, text=True, timeout=1800
    )
    return result.stdout, result.stderr
```

### OpenClaw
```bash
# Cài qua Bun nếu OpenClaw cần dispatch task coding cho OMP
bun setup
bun run build:native
omp --version  # verify cài đặt
```

### Antigravity
```bash
# Yêu cầu Rust toolchain trên VPS trước khi deploy
# curl https://sh.rustup.rs -sSf | sh  (nếu chưa có Rust)
# curl -fsSL https://bun.sh/install | bash  (nếu chưa có Bun)
```
> ⚠️ Build native addon cần cả Bun và Rust — kiểm tra RAM/CPU của VPS Tencent Cloud trước khi build, quá trình compile Rust khá nặng.
