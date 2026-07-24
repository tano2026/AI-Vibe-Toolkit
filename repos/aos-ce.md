# AOS Community Edition (aos-ce) — GitHub Repo

## TL;DR
"Hệ điều hành cho agent" — một CLI/HTTP API viết bằng Rust, quản lý agent như OS quản lý process: capsule (đơn vị năng lực đóng gói, least-privilege), audit, distro, và cơ chế approval cho hành động nhạy cảm. 6.8k+ sao, do Unicity phát triển.

## Repo này dùng để làm gì
Thay vì để agent (Claude/Codex/Grok...) có quyền truy cập tuỳ tiện vào máy, AOS-CE tạo ra một lớp trung gian: mọi năng lực agent dùng được đóng gói thành "capsule" (giống package least-privilege), có audit trail riêng ("Unicity Audit"), và có cơ chế approval cục bộ khi agent muốn làm việc nhạy cảm (AppKit trên macOS, dialog Windows, hoặc Pinentry trên Linux).

Trong core có công cụ tên "Forge" — cho phép 1 agent tự soi hệ thống đang chạy, học cấu trúc capsule, tự phát hiện năng lực còn thiếu, rồi TỰ build + verify 1 capsule mới đúng chuẩn least-privilege. Nói cách khác: agent tự mở rộng năng lực của chính nó một cách có kiểm soát, thay vì Nobitano phải tự code thêm mỗi lần.

`aos mcp serve` là điểm nối MCP dùng chung cho Codex/Claude/Grok — nghĩa là 1 agent (vd Hermes) có thể expose năng lực của nó ra làm MCP server cho các agent khác gọi vào.

## Setup từng bước
1. Cài qua installer chính thức (cài luôn CLI + runtime pinned + 21 capsule Community Edition mặc định):
   ```bash
   curl --proto '=https' --tlsv1.2 -fsSL https://aos.unicity.ai/install.sh | sh
   aos init
   ```
2. Kiểm tra trạng thái hệ thống:
   ```bash
   aos status
   aos status --json
   ```
3. Chạy chẩn đoán / build capsule mới:
   ```bash
   aos doctor
   aos capsule build
   ```
4. Bật MCP server để agent khác (Claude Code, Codex...) gọi vào:
   ```bash
   aos --principal codex-code mcp serve
   ```
5. Nếu cần chạy offline (VPS không có mạng ra ngoài lúc setup): `aos init --offline`.

## Ví dụ thực tế
Áp cho hệ sinh thái hiện tại: thay vì để Hermes/OpenClaw có quyền chạy shell tuỳ tiện trên VPS (rủi ro nếu bị prompt injection từ content research được), có thể bọc từng năng lực Hermes hay dùng (gọi API research, ghi file, gọi Telegram) thành capsule riêng qua AOS-CE — mỗi capsule chỉ có đúng quyền nó cần, và mọi hành động nhạy cảm (vd Hermes muốn tự sửa file cấu hình pm2) phải qua approval gate thay vì chạy thẳng.

## Lưu ý / Lỗi thường gặp
- Viết bằng Rust, chưa thấy license rõ ràng trên repo (khác các repo Python/JS quen thuộc trong kho) — cần double-check license trước khi tích hợp sâu vào production.
- Đây là lớp hạ tầng (infra layer) cho agent, không phải 1 agent cụ thể — cần thời gian học command boundary (`aos` sở hữu root nào, root nào pass-through nguyên vẹn) trước khi wire vào Antigravity.
- Cơ chế approval yêu cầu 1 UI xác nhận cục bộ (AppKit/Windows dialog/Pinentry) — trên VPS headless (Tencent Cloud Ubuntu 22.04 hiện tại) cần xác nhận cơ chế `--interaction` nào chạy được không cần GUI trước khi triển khai thật.

## Đánh giá cá nhân
- Điểm mạnh: đúng hướng với nguyên tắc "state machine phải code-driven, tránh prompt injection" mà kho đã đúc kết — AOS-CE giải bài toán này ở tầng OS thay vì tự vá từng agent; cơ chế capsule least-privilege + audit trail là thứ hệ sinh thái hiện tại (Hermes/OpenClaw) đang thiếu.
- Điểm yếu: còn khá mới, tài liệu tập trung vào command reference hơn là hướng dẫn tích hợp thực tế; approval UI cần GUI local — chưa rõ vận hành tốt trên VPS headless hay không, cần test kỹ trước khi tin tưởng cho production.
- Có nên dùng: 6/10 — đáng thử nghiệm ở môi trường dev trước khi đưa vào VPS production, vì lợi ích bảo mật (capsule least-privilege) lớn nhưng rủi ro tương thích với hạ tầng headless hiện tại chưa kiểm chứng.

## Link
- Repo: https://github.com/unicity-aos/aos-ce
- Docs: repo `docs/` folder (Extending an agent's world on AOS — world model, Forge boundary)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# AOS-CE không có REST endpoint public dạng pip-installable — gọi qua subprocess CLI
import subprocess

def aos_status():
    result = subprocess.run(["aos", "status", "--json"], capture_output=True, text=True)
    return result.stdout
```

### OpenClaw
```bash
# OpenClaw có thể expose chính nó ra làm MCP client gọi aos mcp serve
aos --principal openclaw mcp serve
```

### Antigravity
```bash
curl --proto '=https' --tlsv1.2 -fsSL https://aos.unicity.ai/install.sh | sh
aos init --offline   # nếu VPS hạn chế network ra ngoài lúc cài
```
> ⚠️ Cơ chế approval cần UI cục bộ (Pinentry trên Linux) — Antigravity phải test kỹ chế độ `--interaction` nào chạy được trên VPS headless trước khi bật capsule có quyền hành động nhạy cảm thật.
