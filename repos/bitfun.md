# BitFun — GitHub Repo

## TL;DR
Desktop app AI agent viết bằng Rust + Tauri, đóng gói sẵn 4 agent khác nhau (Code Agent, Cowork Agent, Computer Use, Personal Assistant) trong 1 app — có memory, personality, và khả năng "tiến hoá" theo thời gian. Điều khiển được từ điện thoại qua Telegram/WeChat.

## Repo này dùng để làm gì
BitFun là runtime agent cấp desktop kết hợp với bộ app agent dùng ngay được. Khác với các coding agent chỉ chạy trong terminal, BitFun vào thẳng "workspace thật" — trình duyệt, app desktop, terminal, hoặc môi trường remote — khi task cần.

Điểm khác biệt lớn nhất là **Agentic Mini Apps**: thay vì mọi task đều đẩy qua 1 ô chat, BitFun tự dựng giao diện riêng cho task (biểu đồ, board, form, panel) và gắn conversation với trạng thái sống của giao diện đó — hỏi thẳng về cái đang hiện trên màn hình thay vì phải mô tả lại từ đầu. Cộng đồng đã build dashboard thị trường, tool chuyên ngành khác nhau dựa trên tính năng này.

Có **self-hosted multi-device control** — đăng nhập account, đồng bộ session/settings đa thiết bị, điều khiển 1 máy từ máy khác qua relay tự deploy (zero-knowledge: client tự tạo key ở local, server chỉ giữ hash Argon2id + material mã hoá AES-GCM). Không phụ thuộc cloud của vendor nào — điểm quan trọng nếu cần chạy trong mạng nội bộ công ty.

Kiến trúc mở rộng theo 4 tầng liên tục: custom Agent → MCP/Skill/Codex-compatible Hook → Mini App → sửa source code trực tiếp.

## Setup từng bước

1. Yêu cầu: Node.js 22.12+ (LTS), pnpm 10.15.0 qua Corepack, Rust toolchain, Tauri prerequisites
2. Mở BitFun → tab Welcome → nhấn Open → chọn thư mục project
3. Vào More options (…) → Settings → Models → Create First Configuration
4. Chọn provider, nhập API key, chọn model, nhấn Save — BitFun tự test kết nối và đặt model đầu tiên làm primary
5. Quay lại tab Session, gõ task cụ thể, nhấn Enter hoặc Send

## Ví dụ thực tế

Tình huống: cần 1 agent xử lý cả việc code (sửa `tano.agency`) lẫn việc văn phòng (đọc research report, viết thành docx cho client), và muốn điều khiển từ điện thoại khi đang di chuyển.

- Mở BitFun trên VPS/desktop, config model Claude Sonnet 5
- Dùng Code Agent để refactor `server/kho-client.ts`
- Chuyển sang Cowork Agent để đọc research-analytics-pro output, biến thành file docx
- Setup relay tự host, đăng nhập từ điện thoại qua Telegram bot đã liên kết → giám sát/điều khiển từ xa

## Lưu ý / Lỗi thường gặp

- README nặng về ngôn ngữ marketing, thiếu chi tiết kiến trúc cụ thể và benchmark hiệu năng định lượng (claim "flashgrep" chưa có số liệu kèm theo)
- Không có thông tin rõ model nào đã test/khuyến nghị — phải tự thử nghiệm
- Project ghi rõ là "spare-time research, không phải sản phẩm thương mại" — thiếu độ chín về vận hành, đừng kỳ vọng ổn định như tool doanh nghiệp
- Bản README có cả tiếng Anh và tiếng Trung (README.zh-CN.md) — coi cả 2 nếu cần chi tiết đầy đủ

## Đánh giá cá nhân

- **Điểm mạnh:** Gộp 4 loại agent trong 1 app desktop là ý tưởng thực dụng, không cần chuyển qua lại nhiều tool riêng biệt. Multi-device control self-hosted (zero-knowledge relay) rất hợp nếu Nobitano muốn giám sát VPS agent từ điện thoại mà không tin tưởng cloud của ai khác.
- **Điểm yếu:** Docs sơ sài, thiếu benchmark, project tự nhận là "nghiên cứu tay trái" không phải production-ready. Rủi ro breaking change cao vì đang phát triển nhanh.
- **Có nên dùng không:** 6/10 — Đáng thử nếu cần 1 desktop agent đa năng và thích tự host, nhưng đừng đặt cược production vào nó lúc này. Theo dõi thêm vài tháng để xem độ chín có tăng không.

## Link
- Repo: https://github.com/GCWing/BitFun
- README tiếng Trung: https://github.com/GCWing/BitFun/blob/main/README.zh-CN.md
- Đánh giá độc lập (OSS AI Hub): https://ossaihub.com/tool/gcwing-bitfun/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# BitFun chủ yếu là desktop app, không có REST API công khai rõ ràng trong docs hiện tại
# Nếu cần điều khiển từ Hermes, kiểm tra relay self-hosted (ControlHub) trong docs trước
import subprocess

def check_bitfun_relay(relay_url: str):
    """Kiểm tra relay BitFun đang chạy — cần setup relay trước theo docs."""
    # Placeholder: BitFun dùng self-hosted relay, cần đọc thêm docs ControlHub
    pass
```

### OpenClaw
```bash
# BitFun là app desktop (Tauri), không phải CLI thuần — cài qua installer từ GitHub Releases
# Không phù hợp để OpenClaw dispatch trực tiếp trừ khi dùng relay/remote control API
```

### Antigravity
```bash
# Deploy trên VPS cần chạy được Tauri desktop app — thường cần headless display (Xvfb)
# hoặc chỉ deploy relay server (ControlHub) nếu chỉ cần multi-device control, không cần full app
```
> ⚠️ Đây là desktop app trước tiên, không phải service headless thuần — cân nhắc kỹ trước khi cố deploy trên VPS không có GUI. Ưu tiên dùng trên máy cá nhân, chỉ deploy relay trên VPS nếu cần remote control.
