# Claude Code Router (CCR) — GitHub Repo

## TL;DR
Proxy chạy local, chặn request Claude Code lại rồi route sang model khác (DeepSeek, OpenRouter, Kimi, Gemini, Ollama...) — dùng giao diện Claude Code quen thuộc nhưng trả tiền/miễn phí theo model mày chọn, không bắt buộc phải dùng Claude cho mọi task.

## Repo này dùng để làm gì
Claude Code mặc định chỉ nói chuyện với model Anthropic. CCR (musistudio/claude-code-router) chèn 1 lớp gateway local (`http://127.0.0.1:3456`) ở giữa — Claude Code gửi request tới CCR, CCR đọc rule routing rồi tự quyết định chuyển tới model nào: việc nền dùng model rẻ (DeepSeek), việc cần suy luận sâu dùng model xịn, việc context dài dùng model context window to.

31,952 sao. Hỗ trợ 8+ provider: OpenRouter, DeepSeek, Ollama, Gemini, VolcEngine, SiliconFlow, ModelScope, DashScope, Kimi (built-in preset).

## Setup từng bước
1. Cài Claude Code (nếu chưa có) + CCR:
```bash
npm install -g @anthropic-ai/claude-code
npm install -g @musistudio/claude-code-router
```
2. Tạo file config:
   - Mac/Linux: `~/.claude-code-router/config.json`
   - Windows: `%APPDATA%\Claude Code Router\config.json`
```json
{
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat",
    "think": "deepseek,deepseek-reasoner"
  }
}
```
3. Khởi động router: `ccr start`
4. Mở Claude Code qua router (thay vì gõ `claude` như bình thường): `ccr code`
5. Trong session, đổi model giữa chừng bằng `/model provider,model_name`

## Ví dụ thực tế
Chạy `claude` bình thường: mọi request — kể cả task nền lặt vặt như đọc file, format code — đều tốn quota Claude.

Chạy `ccr code` với router set `"background": "deepseek,deepseek-chat"`: task nền tự động rẻ hơn Sonnet/Opus 10-20 lần, chỉ giữ model Claude cho task cần lý luận sâu.

## Lưu ý / Lỗi thường gặp
- `ccr code` báo "Timeout" → chạy tay `ccr start` rồi `ccr code` lại
- Status "Not Running" → có process ma chiếm port 3456, `lsof -i :3456` rồi kill PID đó
- Kiểm tra base URL đúng chưa bằng lệnh `/status` ngay trong Claude Code — phải thấy `127.0.0.1:3456`
- Model không hỗ trợ tool-calling (một số model free trên OpenRouter) sẽ lỗi khi Claude Code cố gọi tool — cần chọn model có function calling

## Đánh giá cá nhân
- Điểm mạnh: Đúng ý tưởng "model.default rẻ, không cài model Pro đắt tiền làm mặc định" mà project_starter_rules của Tano Agency đã đặt ra — CCR là cách thực thi tự động cái rule đó ở tầng hạ tầng thay vì tự nhớ đổi model tay
- Điểm yếu: Là 1 lớp proxy thêm — nếu nó lỗi/đứng thì Claude Code cũng đứng theo, thêm 1 điểm fail có thể xảy ra. Test kỹ trước khi phụ thuộc hoàn toàn
- Có nên dùng không: 8/10 — đáng cân nhắc thay thế 1 phần vai trò OmniRoute nếu Nobitano muốn Claude Code cụ thể cũng route đa provider giống các agent khác, nhưng 2 hệ thống này overlap chức năng, không nên chạy song song không mục đích

## Link
- Repo: https://github.com/musistudio/claude-code-router
- Docs: https://musistudio.github.io/claude-code-router/

---

## 🤖 Agent Integration

### Hermes (Python)
> Không áp dụng trực tiếp — CCR là proxy cho Claude Code CLI, Hermes không chạy qua Claude Code nên không cần setup này.

### OpenClaw
```bash
# Nếu OpenClaw muốn dùng chung gateway routing với Claude Code, trỏ HTTP request
# vào endpoint local của CCR thay vì gọi thẳng Anthropic API
curl http://127.0.0.1:3456/v1/messages -H "Content-Type: application/json" -d '...'
```

### Antigravity
```bash
# Cài trên máy chạy Claude Code (Windows local D:\, KHÔNG phải VPS)
npm install -g @musistudio/claude-code-router
```
> ⚠️ CCR chạy local trên máy Windows đang chạy Claude Code, không phải trên VPS — xem
> `agents/CLAUDE-CODE-BRIDGE.md` để biết đúng môi trường.
