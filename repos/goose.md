# Goose — GitHub Repo

## TL;DR
AI agent tổng quát chạy trên máy mình, viết bằng Rust — có cả desktop app (macOS/Linux/Windows), CLI, và API. Ban đầu là dự án của Block (công ty mẹ Square/Cash App), giờ đã chuyển về Agentic AI Foundation (AAIF) thuộc Linux Foundation. Nối được 70+ extension qua MCP, chạy được với 15+ provider model.

## Repo này dùng để làm gì
Không chỉ để code — Goose dùng được cho research, viết lách, automation, phân tích dữ liệu, hoặc bất kỳ việc gì cần agent tự thực thi (không chỉ gợi ý). Khác biệt với nhiều coding agent khác: không kén provider, dùng API key riêng hoặc tận dụng luôn subscription Claude/ChatGPT/Gemini đang có sẵn qua ACP (Agent Client Protocol).

## Setup từng bước
1. Cài CLI (cách nhanh nhất):
   ```bash
   curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash
   ```
2. Hoặc tải app desktop cho macOS/Linux/Windows từ trang chủ (giao diện Electron, không chỉ CLI).
3. Cấu hình provider model đầu tiên khi khởi động (Anthropic/OpenAI/Google/Ollama/OpenRouter/Azure/Bedrock...).
4. Nối extension qua MCP — Goose hỗ trợ 70+ extension có sẵn (Jira, GitHub, Slack, hạ tầng, data pipeline...), thêm bằng lệnh cấu hình MCP server trong CLI/app.
5. Chạy task, hỏi bằng tiếng thường — Goose tự chạy shell, sửa code, test, lặp lại tới khi xong (không chỉ dừng ở gợi ý).

## Ví dụ thực tế
Giao cho Goose 1 việc tự động hoá không phải code: "tổng hợp file CSV doanh số Wonder Mart thành báo cáo tuần" — Goose tự viết script xử lý, chạy, kiểm tra kết quả, sửa nếu sai, tới khi ra đúng báo cáo, không cần tự tay chạy từng lệnh.

## Lưu ý / Lỗi thường gặp
- Repo đã **chuyển tổ chức**: từ `block/goose` sang `aaif-goose/goose` (Agentic AI Foundation, Linux Foundation) — link cũ vẫn redirect được nhưng nên cập nhật bookmark sang repo mới, tài liệu ghi rõ "một số link vẫn đang trong giai đoạn chuyển đổi".
- Có nhiều bản cũ trùng tên trước khi đổi tổ chức (`adhintz/goose` cài qua `pipx install goose-ai` — đây là bản Python cũ, khác hẳn bản Rust hiện tại) — dễ nhầm 2 dự án "goose" khác nhau hoàn toàn, kiểm tra kỹ link trước khi cài.
- Dùng ACP để tận dụng subscription Claude/ChatGPT/Gemini có sẵn (không cần thêm API key riêng) — nhưng không phải mọi tính năng đều support qua ACP như qua API key trực tiếp, kiểm tra changelog nếu thiếu tính năng.
- Stack chính là Rust (63.8%) + TypeScript (26.2%, phần UI desktop) — muốn tự contribute code cần biết cả 2, không chỉ 1.

## Đánh giá cá nhân
- **Điểm mạnh:** Được Linux Foundation đỡ đầu (AAIF) là tín hiệu về độ ổn định lâu dài hiếm có trong mảng agent open source. Không kén model, không kén use case (không chỉ code), có cả desktop app cho người không quen CLI — hiếm agent open source làm được cả 3 hình thái (desktop/CLI/API) cùng lúc.
- **Điểm yếu:** Vừa đổi tổ chức nên tài liệu/link đang trong giai đoạn cập nhật, dễ nhầm với bản Python cũ (`goose-ai`) đã bị bỏ. Viết bằng Rust nên rào cản contribute cao hơn dự án Python/JS thông thường.
- **Có nên dùng không:** 8/10 — đáng thử làm agent tổng quát trên máy cá nhân, đặc biệt nếu đã có sẵn subscription Claude/ChatGPT/Gemini muốn tận dụng qua ACP thay vì trả thêm API key riêng.

## Link
- Repo: https://github.com/aaif-goose/goose
- Docs/Demo: (xem README repo cho Quick Links tài liệu chính thức, đang cập nhật theo tổ chức mới)

---

## 🤖 Agent Integration

### Hermes (Python)
Không có REST API cố định public để gọi trực tiếp từ ngoài — Goose có "API để nhúng vào bất cứ đâu" nhưng cần tự host/chạy Goose ở chế độ server trước. Nếu Hermes cần dùng, cách đơn giản nhất là subprocess gọi Goose CLI với 1 task cụ thể, đọc kết quả trả về từ output.

### OpenClaw
```bash
# Cài CLI Goose 1 lần, sau đó OpenClaw subprocess gọi để giao task tổng quát
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash
goose run --text "mô tả task cần Goose tự làm"
```
> ⚠️ Cần cấu hình provider model cho Goose từ trước (API key hoặc ACP) — chưa cấu hình thì lệnh chạy sẽ dừng lại hỏi thiết lập, không tự chạy ngầm được.

### Antigravity
```bash
# Cài CLI trên VPS
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash
```
> ⚠️ Trên VPS không có giao diện, chỉ dùng được bản CLI (không phải desktop app) — nhớ cấu hình provider qua biến môi trường/config file, không qua UI như trên máy cá nhân.
