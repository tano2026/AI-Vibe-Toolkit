# super-board (EricTechPro) — GitHub Repo

## TL;DR
Bộ skill cho **Claude Code** (MIT, v3.1.2, commit mới nhất 13/10/2026) biến GitHub Project thành "bảng kanban tự chạy": bạn thả thẻ vào cột `Ready`, các lane **Build → QA → Review** chạy trong worktree riêng, tạo PR nháp, và chỉ merge khi qua cổng kiểm tra. Hợp với việc **sửa/bảo trì code có test sẵn**; không phải công cụ cho nội dung hay marketing. Chưa chạy end-to-end trong phiên này.

> Trùng tên: tìm "super-board" ra nhiều bản fork (vernanng, MDsniper, heverton-dev, Wladefant) và một repo LED scoreboard không liên quan. Entry này nói về bản gốc **`EricTechPro/super-board`**.

## Repo này dùng để làm gì
8 skill (5 bạn gõ, 3 do bảng chạy), 9 lệnh, 6 hook chặn lỗi:
| Nhóm | Thành phần |
|---|---|
| Điều phối | `/super-board` (onboard, lint, status, run, stop) |
| Thu thập việc | `/super-collect` — lấy vấn đề từ Sentry, PostHog, issue, PR rồi tạo thẻ Backlog |
| Ba lane chạy | `/super-build` (worktree, thay đổi nhỏ nhất, test, PR nháp) · `/super-qa` (bằng chứng, ảnh chụp, trả về Build nếu lỗi) · `/super-review` (nhớ phát hiện trước, cổng merge) |
| Phụ trợ | `/ui-refine-loop`, `/visual` (một trang HTML tóm tắt nhánh/kế hoạch), `/git-sync` |
| Hook bảo vệ | chặn đọc `.env`/khoá SSH, chặn ghi API key vào file, chặn `rm` ngoài dự án, tuỳ chọn chặn push thẳng main |

Bộ định tuyến rẻ chấm thẻ dễ/vừa/khó rồi chọn model (mặc định Haiku 4.5 / Sonnet 5.5 / Opus 5.5); có cờ `--low`, `--high`, `--codex`.

## Số liệu đã kiểm (15/10/2026, bản clone nông)
- License MIT (đã mở LICENSE). VERSION 3.1.2. Commit mới nhất 13/10/2026 (`7d848f7`) — đang được bảo trì sát
- Chạy thật 1 bộ test offline: `tests/test-guard-hooks.sh` → **PASS 82 case** (có cảnh báo `push negotiation failed` do sandbox, không ảnh hưởng). `run-safety.sh` chạy quá 2 phút thì ngắt, **chưa có kết quả**
- Chưa cài vào Claude Code thật, chưa chạy `/super-board run` với một GitHub Project thật → chưa biết chất lượng PR
- Số sao: **chưa đo** (API GitHub bị chặn trong phiên này)
- Yêu cầu: Claude Code, `gh`, `jq`, bash 3.2+, Python 3.9+; cài kèm skill của Matt Pocock (`npx skills@latest add mattpocock/skills`) trừ khi dùng `--no-helper-skills`

## Setup
```bash
# Trong thư mục dự án (đọc get.sh trước khi pipe vào bash)
curl -fsSL https://raw.githubusercontent.com/EricTechPro/super-board/main/get.sh | bash
# hoặc plugin (chỉ có skill, hook cài ở bước onboard)
/plugin marketplace add EricTechPro/super-board
/plugin install super-board@super-board
```
Rồi `/super-board onboard` (8 bước, Enter nhận đề xuất), thêm thẻ vào cột `Ready`, chạy `/super-board run <slug>`.

## Ví dụ thực tế
Bối cảnh: một web app khách hàng của agency có 10 lỗi nhỏ trong Backlog, repo đã có test và CI.
```text
/super-collect --since 30d        # lọc lỗi từ Sentry/issue thành thẻ Backlog có tiêu chí nghiệm thu
/super-board lint                 # báo thẻ nào tiêu chí mơ hồ
/super-board run client-app --low # rẻ nhất: Haiku cho thẻ dễ
```
Kỳ vọng theo README: PR nháp + bằng chứng QA cho từng thẻ, merge khi `verify_commands` của dự án pass. **Chưa chạy thử — đây là mô tả từ tài liệu, không phải kết quả đo.**

## Lưu ý / Lỗi thường gặp
- **Chỉ có giá trị khi repo có test/lệnh verify.** Cổng merge dừng nếu `verify_commands` rỗng → dự án không test thì không tự merge được
- **Tốn token**: chạy nhiều lane Opus trên thẻ khó; dùng `--low` và giới hạn số thẻ trước khi thả cả bảng
- Phụ thuộc skill bên thứ ba (Matt Pocock, ponytail, impeccable, humanizer); thiếu skill thì dừng trước khi nhận việc
- `get.sh | bash` tải và cài hook vào dự án — đọc `get.sh`/`install.sh` rồi mới chạy, thử trên bản sao
- Cho phép merge tự động: chỉ bật `merge_policy` sau khi đã xem vài PR đầu; đừng dùng trên repo sản xuất của khách khi chưa duyệt tay
- Bản tiếng Anh, giả định quy trình GitHub Projects; không liên quan nội dung/marketing
- Hook đọc `.env` bị chặn là điểm cộng, nhưng skill vẫn đi qua `gh` với quyền token của bạn → dùng token tối thiểu quyền

## Đánh giá cá nhân
- Điểm mạnh: MIT, bảo trì sát (commit 2 ngày trước), có hook chặn thật (82 case test pass), có bộ eval và test offline, quy trình Build/QA/Review tách lane rõ, có cổng merge theo commit đã review
- Điểm yếu: chưa chạy end-to-end, phức tạp (28 script, nhiều phụ thuộc), chỉ cho việc code, lệch với việc chính hằng ngày của agency (nội dung/marketing/sales)
- Có nên dùng: **6/10** cho agency. Không đưa vào luồng hằng ngày. Đáng thử **1 spike 30 phút** khi có dự án code của khách đã có test; khi đó thử trên repo bản sao với 2–3 thẻ dễ. Mượn ý nên làm: cổng merge theo `verify_commands`, hook chặn `.env`, lane QA trả thẻ về Build
- Gần nhất trong kho: `repos/superpowers.md` (kỷ luật quy trình, không có bảng tự chạy)

## Link
- Repo: https://github.com/EricTechPro/super-board
- Trang giới thiệu: https://erictechpro.github.io/super-board/
- Video của tác giả: https://youtu.be/aggJvNZxfKA
- Liên quan trong kho: `repos/superpowers.md`, `agents/` (Pro Agent kỹ thuật)

---

## 🤖 Agent Integration

### Hermes (Python)
Không có REST API. Hermes chỉ cần **đọc** repo để lấy khung/script; việc chạy cần Claude Code hoặc Codex trên máy có `gh`.
```python
import subprocess
# kiểm môi trường trước khi Claude Code chạy bảng (không cài gì)
for t in ("gh", "jq", "python3", "claude"):
    print(t, subprocess.run(["which", t], capture_output=True, text=True).stdout.strip() or "THIẾU")
```

### OpenClaw
```bash
# Chỉ chạy trong Claude Code / Codex. Từ OpenClaw: giao việc cho phiên Claude Code trên VPS
/plugin marketplace add EricTechPro/super-board
```

### Antigravity
```bash
# Cài trong thư mục dự án trên VPS (sau khi người duyệt đã đọc get.sh)
git clone --depth 1 https://github.com/EricTechPro/super-board /opt/kho/super-board
gh auth status   # cần đăng nhập gh bằng token tối thiểu quyền
```
> ⚠️ Đây là công cụ tự merge PR. Không bật `merge_policy` tự động và không dùng trên repo khách khi chưa có người duyệt. Chưa chạy thử trên Project thật.
