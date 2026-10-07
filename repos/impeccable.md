# Impeccable — GitHub Repo

## TL;DR
Bộ "ngôn ngữ thiết kế" cho AI viết giao diện: 1 skill + **24 lệnh** (`/impeccable critique`, `polish`, `typeset`...) + **bộ quét 60 lỗi thiết kế kiểu "AI làm"** chạy bằng `npx impeccable detect`, **không cần AI, không cần API key**. Apache-2.0, ~77,8K sao (07/10/2026), tác giả Paul Bakaus. Đã chạy thử bộ quét thật (v4.1.0): bắt đúng 11 lỗi trên file HTML mẫu. **Phần quét dùng được ngay, kể cả trên VPS/Antigravity; phần 24 lệnh cần 1 agent có hỗ trợ.**

> Đính chính bản cũ trong kho: ghi "23 lệnh", "không chạy trên Hermes" và không có số sao/license. Thực tế (README hiện tại): 24 lệnh, Hermes Agent / DeepSeek Harness / Antigravity / Gemini CLI nằm trong danh sách harness được hỗ trợ, Apache-2.0.

## Repo này dùng để làm gì
Chặn giao diện "trông như AI làm" (font Inter/Arial mặc định, gradient tím, viền trái dày, chữ xám trên nền màu, card lồng card, easing nảy…) và cho agent từ vựng thiết kế để sửa. Hai phần tách biệt:
1. **Detector (CLI, quét tất định, 0 chi phí LLM):** quét thư mục, file HTML, hoặc URL đang chạy. Xuất JSON cho CI. Mã thoát: 0 sạch, 2 có lỗi, 1 quét hỏng.
2. **Skill + 24 lệnh (cần agent):** `init` (ghi PRODUCT.md), `craft`, `shape`, `critique`, `audit`, `polish`, `typeset`, `layout`, `colorize`, `bolder`, `quieter`, `distill`, `harden`, `animate`, `clarify`, `adapt`, `optimize`, `onboard`, `delight`, `overdrive`, `document`, `extract`, `live`, `generate`.

## Đã kiểm chứng thật (07/10/2026, trong sandbox của tao)
```bash
npx impeccable --version        # -> 4.1.0
npx impeccable detect t.html    # file mẫu cố tình xấu
```
Kết quả: **11 lỗi** được chỉ đúng chỗ, kèm gợi ý sửa: `side-tab` (viền trái 4px), `gray-on-color`, `low-contrast` (1.7:1 và 3.5:1, cần 4.5:1), `dark-glow` (bóng tím zero-offset), `bounce-easing`, `overused-font` (Inter), `ai-color-palette` (tím/violet). Không cần key nào. Đây là bằng chứng chạy thật của bộ quét; **phần 24 lệnh qua agent thì chưa test**.

## Setup
```bash
# Cách khuyên dùng — cài cho harness đang có:
npx impeccable install
# Rồi trong agent:  /impeccable init     (ghi PRODUCT.md: bối cảnh sản phẩm)
#                   /impeccable hooks on (bật hook tự quét khi sửa file UI — nơi có hỗ trợ hook)

# Chỉ muốn QUÉT, không cài gì vào agent:
npx impeccable detect src/                 # thư mục
npx impeccable detect https://example.com  # URL đang chạy (cần Chrome/Chromium/Edge)
npx impeccable detect --json .             # cho CI/Hermes
```
Cần Node (cho `npx`). Quét URL cần trình duyệt. Chế độ `live` chỉ chạy với bản checkout cục bộ, không bơm vào site production.

## Harness được hỗ trợ (theo README)
Claude Code, Cursor, GitHub Copilot, Codex CLI, Grok Build, DeepSeek Harness, Gemini CLI, Google Antigravity, Hermes Agent, OpenCode, Pi, Kiro, Trae, Rovo Dev, Qoder, Mistral Vibe, Veto. Hook tự động có ở Claude Code, Copilot, Cursor, Codex, Grok Build. Chưa kiểm từng harness.

## Điểm kết nối với kho
- Bổ sung Designer Pro: Designer Pro lo ảnh/poster tĩnh; Impeccable lo **giao diện web/app thật** (TMC Corporate Portal, Smart Booking, trang đích ABTRIP, Twenty tuỳ biến giao diện không phải việc của nó)
- Detector là lưới an toàn rẻ nhất: chạy trước khi demo cho khách B2B/B2G

## Ví dụ thực tế
TMC Corporate Portal đang ở giai đoạn dựng UI: chạy `npx impeccable detect --json <thư mục portal>` trước mỗi lần demo; lỗi nào mã thoát 2 thì sửa hoặc ghi lý do bỏ qua bằng chú thích `impeccable-disable`. Việc này làm được trên VPS qua Antigravity/Hermes mà **không cần Claude Code** (đang bị chặn).

## Lưu ý / Lỗi thường gặp
- Detector bắt dấu hiệu "AI-tell" theo luật cố định — không thay thế mắt nhìn và người dùng thật; có thể báo "lỗi" với lựa chọn thiết kế cố ý (dùng chú thích waiver, ghi lý do)
- Hook cần mình duyệt "trust" theo từng công cụ (Codex, Grok…)
- Đừng cài trùng 2 bản trong cùng workspace
- Mục `optional script impeccable:manual-edit-validate` chạy với quyền người dùng — chỉ bật khi hiểu nó chạy gì
- 24 lệnh qua agent: chưa test

## Đánh giá cá nhân
- Điểm mạnh: Apache-2.0, cộng đồng rất lớn, **phần quét chạy ngay không tốn token/key và đã tự kiểm chứng**, hỗ trợ nhiều harness trong đó có Hermes/Antigravity
- Điểm yếu: tập trung UI code (không phải poster); luật mang gu thẩm mỹ của tác giả; hiệu quả thật của 24 lệnh trên dự án của mình chưa biết
- Có nên dùng: **8/10 cho bộ quét** (làm ngay), 6/10 cho 24 lệnh (đợi có agent chạy được và có UI thật để thử)

## Link
- Repo: https://github.com/pbakaus/impeccable
- Docs: https://impeccable.style
- npm: `impeccable`
- Liên quan: `agents/designer-pro/`, `repos/product-film-skill.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Quét UI tất định, không tốn token. Cần Node trên VPS.
import subprocess, json
r = subprocess.run(["npx", "--yes", "impeccable", "detect", "--json", "/duong/dan/portal"],
                   capture_output=True, text=True, timeout=300)
# r.returncode: 0 sạch, 2 có lỗi, 1 quét hỏng
findings = json.loads(r.stdout) if r.stdout.strip().startswith(("{", "[")) else r.stdout
print(r.returncode, findings)
```

### OpenClaw
```bash
npx impeccable detect --json ./ten-du-an   # chạy trong bước kiểm tra trước demo
```

### Antigravity
```bash
npx impeccable install            # cài skill + lệnh cho harness đang dùng (agy)
npx impeccable detect src/        # hoặc chỉ quét
```
> ⚠️ `--json` in ra cấu trúc có thể đổi theo phiên bản; kiểm tra đầu ra thật trước khi parse tự động.
