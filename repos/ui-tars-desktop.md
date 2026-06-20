# UI-TARS-desktop (Agent TARS) — GitHub Repo

## TL;DR
Hai dự án trong một repo của ByteDance: **Agent TARS** (AI agent duyệt web qua terminal/web UI) và **UI-TARS-desktop** (app desktop điều khiển GUI máy tính). 37K+ sao. Không bị lock vào một model duy nhất.

## Repo này dùng để làm gì

### Agent TARS
AI agent đa phương thức chạy từ terminal hoặc web UI. Mày đưa task, nó tự:
- Duyệt web, tìm kiếm, đọc nội dung
- Điền form, click, navigate
- Kết nối với MCP tools
- Hỗ trợ local + cloud deployment

Về cơ bản giống browser-use hay Playwright automation nhưng có UI đẹp hơn và multi-modal (hiểu cả ảnh).

### UI-TARS-desktop
Desktop app (Mac/Win/Linux) dùng model UI-TARS để điều khiển giao diện đồ họa. Mày nói "mở Excel, điền dữ liệu này vào cột A" — nó tự làm. Không cần viết script.

Điểm khác biệt: **không lock vào model** — dùng được Claude, GPT, Gemini, hay model local.

## Setup từng bước

### Agent TARS (CLI)
```bash
# Cài qua npm
npm install -g @agent-tars/cli

# Chạy với Claude
ANTHROPIC_API_KEY=your_key agent-tars

# Hoặc chạy web UI
agent-tars --ui
```

### UI-TARS-desktop
```bash
# Download từ Releases
# https://github.com/bytedance/UI-TARS-desktop/releases

# Hoặc build từ source
git clone https://github.com/bytedance/UI-TARS-desktop.git
cd UI-TARS-desktop
npm install
npm run build
```

Sau khi mở app: config model (local Ollama hoặc API key), rồi gõ task vào là chạy.

## Ví dụ thực tế
**Agent TARS**: "Research top 10 AI tools launched this week và tóm tắt lại" → agent tự mở browser, search, đọc các trang, trả về summary.

**UI-TARS-desktop**: "Mở Figma, tạo frame 1920x1080, thêm text Hello World vào giữa" → app tự điều khiển Figma như người dùng thật.

## Lưu ý / Lỗi thường gặp
- UI-TARS-desktop cần model mạnh (GPT-4o hoặc Claude Sonnet trở lên) để điều khiển GUI chính xác
- Agent TARS còn đang develop mạnh, API có thể thay đổi
- Computer use / GUI control tốn nhiều token hơn text tasks
- Chạy local model cần GPU đủ mạnh

## Đánh giá cá nhân
- Điểm mạnh: ByteDance build nên có resource mạnh, không vendor lock-in, hỗ trợ MCP, cả hai tool trong một repo
- Điểm yếu: Còn non, documentation chưa đầy đủ, GUI agent vẫn còn lỗi khi gặp UI phức tạp
- Có nên dùng không: **7/10** — Agent TARS đáng thử ngay. UI-TARS-desktop thú vị nhưng chờ thêm vài tháng cho stable hơn.

## Link
- Repo: https://github.com/bytedance/UI-TARS-desktop
- Docs Agent TARS: https://agent-tars.com
- Quick Start: https://github.com/bytedance/UI-TARS-desktop/blob/main/docs/quick-start.md
