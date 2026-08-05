# OpenWorker (Andrew Ng) — GitHub Repo

## TL;DR
Desktop AI coworker mã nguồn mở của Andrew Ng (MIT license, ra mắt tháng 7/2026): giao 1 outcome (không phải 1 prompt), nó tự chia bước, thao tác trên file/terminal/app kết nối, và trả về deliverable hoàn chỉnh — không phải chat trả lời. Điểm đáng chú ý nhất với Tano Agency: hệ thống phân quyền 4 cấp rủi ro (read/write_local/exec/external) gate từng tool call — đúng khoảng trống mà `agents/company/` đang thiếu.

## Repo này dùng để làm gì
Thay vì "hỏi AI 1 câu, tự copy kết quả đi làm tiếp", OpenWorker nhận thẳng 1 yêu cầu kiểu "chuẩn bị brief khách hàng cho cuộc gọi renewal", tự lên kế hoạch từng bước, gọi tool (đọc file, gửi Slack, sửa calendar...), và mỗi hành động có ảnh hưởng thật đều dừng lại xin duyệt trước khi làm — không phải kiểu "để AI làm hết không ai kiểm soát".

## Setup từng bước
1. Tải app cho macOS (Windows đang phát triển, chưa có bản chính thức tại thời điểm viết) hoặc build từ source: `git clone https://github.com/andrewyng/openworker`
2. Kiến trúc: Tauri 2 + React (desktop shell) gọi vào Python FastAPI server chạy local trên `127.0.0.1:8765`, agent runtime dựng trên `aisuite` (thư viện của chính Andrew Ng, thống nhất API cho nhiều LLM provider).
3. Bring-your-own API key — chọn 1 trong 30 model provider hỗ trợ tool-calling, hoặc chạy hoàn toàn local qua Ollama.
4. Kết nối tool: 25+ connector có sẵn (GitHub, Slack, Jira, Notion, Linear, HubSpot, Outlook, monday.com, Gmail, Google Calendar) + hỗ trợ MCP server ngoài.
5. Chọn permission mode: `discuss`/`plan` (chỉ đọc, không hành động) → `interactive` (mặc định, hỏi trước mỗi write/command/external call) → `auto` (tự làm hết, vẫn giới hạn trong path đã cho phép) → `custom` (tự liệt kê tool nào được auto-approve).

## Ví dụ thực tế
Yêu cầu: "Chuẩn bị brief cho cuộc gọi renewal với Northwind." OpenWorker tự đọc lịch sử tương tác, kiểm tra ticket support còn mở, tổng hợp usage Q2, rồi trả về 1 đoạn brief sẵn dùng: "Usage tăng gấp đôi Q2. Cả 2 ticket support đã đóng; góc mở rộng là hướng renewal mạnh nhất." — không phải danh sách gạch đầu dòng để người tự tổng hợp lại.

## Lưu ý / Lỗi thường gặp
- **Chỉ chạy được trên máy có GUI (Tauri desktop app)** — không deploy headless được trên VPS Ubuntu như Tencent Cloud VPS đang dùng. Muốn dùng kiểu tự động 24/7 phải chạy trên máy Windows local có desktop, không phải VPS.
- **Windows chưa chính thức** tại thời điểm viết — nếu team chủ yếu Windows/VPS thì phải chờ hoặc build thủ công.
- Repo còn khá mới (ra mắt vài tuần), tăng sao rất nhanh nhưng chưa có track-record production dài hạn — nên đọc code trước khi tin tưởng chạy `auto` mode với dữ liệu thật.

## Đánh giá cá nhân
- **Điểm mạnh:** Hệ thống phân quyền theo risk-tier (read/write_local/exec/external + 5 permission mode) là thiết kế đáng học nhất trong repo này — đúng pattern Tano cần cho OpenClaw/Hermes khi mở rộng quyền hành động (Gmail/Slack/CRM-write) mà `SKILL_AGENTIC_FACTORY.md` cũng đang khuyến nghị ("agent hành động BẮT BUỘC giữ Validator + tầng confirm").
- **Điểm yếu:** Là desktop app, không chạy headless trên VPS — không dùng trực tiếp được cho Hermes/OpenClaw đang chạy 24/7 trên Tencent Cloud. Giá trị thực tế với Tano nằm ở việc **học kiến trúc phân quyền để tự implement**, không phải cài thẳng vào stack.
- **Có nên dùng không:** 7/10 cho mục đích tham khảo kiến trúc, 3/10 nếu định deploy thẳng vào pipeline VPS hiện tại — không hợp môi trường headless.

## Link
- Repo: https://github.com/andrewyng/openworker
- Docs/Demo: https://openworker.com

---

## 🤖 Agent Integration

### Hermes (Python)
Không cài trực tiếp — nhưng nên tham khảo pattern risk-tier để thêm lớp phân quyền cho Hermes trước khi mở rộng quyền hành động (hiện Hermes gọi API qua urllib thuần, chưa có gate theo risk-class).

```python
# Pattern tham khảo từ OpenWorker — implement risk-tier gate cho Hermes
RISK_TIERS = {
    "read": [],                      # không cần confirm — web_search, get_file
    "write_local": ["push_to_github"],   # cần confirm nếu path ngoài kho AI-Vibe-Toolkit
    "exec": ["run_shell_command"],       # luôn cần confirm trên VPS production
    "external": ["send_telegram", "call_zalo_oa"],  # luôn cần confirm — có side-effect ngoài máy
}

def classify_and_gate(tool_name: str, permission_mode: str = "interactive") -> bool:
    """Trả về True nếu tool được phép chạy ngay, False nếu cần dừng xin duyệt."""
    tier = next((t for t, tools in RISK_TIERS.items() if tool_name in tools), "read")
    if permission_mode == "auto":
        return tier != "external"  # auto vẫn chặn external theo đúng pattern OpenWorker
    if permission_mode == "interactive":
        return tier == "read"
    return False  # discuss/plan mode — không hành động gì
```

### OpenClaw
Không có tích hợp trực tiếp (khác hệ sinh thái) — dùng làm tài liệu tham khảo khi thiết kế lại cơ chế duyệt lệnh Telegram/WhatsApp cho các hành động ghi/gửi.

### Antigravity
Không deploy — đây là desktop app cần GUI, không phù hợp VPS headless Ubuntu 22.04 đang dùng.

> ⚠️ Đừng nhầm "học kiến trúc" với "cài đặt tool". OpenWorker đáng giá nhất ở
> cách thiết kế permission, không phải như 1 service chạy nền trên VPS.
