# Scrptly Video Generator — MCP Server

## TL;DR
MCP hosted (remote) từ Scrptly — 1 prompt văn bản + ảnh ngữ cảnh tùy chọn ra video chuyên nghiệp, có cơ chế duyệt ngân sách token trước khi chạy (`approveUpTo`) để tránh tốn quá tay.

## Tool này dùng để làm gì
Chỉ có 2 tool nhưng đơn giản dễ tích hợp:
- `generateAiVideo` — nhận `prompt` (nên mô tả rõ thời lượng, phong cách hình ảnh, cốt truyện), `context` (mảng ảnh tham chiếu kèm mô tả), và `approveUpTo` (giới hạn chi phí token, mặc định 10.000) → trả về `taskId`, `projectId`, `projectUrl`
- `getTaskStatus` — poll theo `taskId`, trả trạng thái (`awaiting`/`processing`/`success`/`failed`) và `resultVideoUrl` khi xong

Điểm khác AITuber ở trên: Scrptly cho phép đưa ảnh ngữ cảnh (context images) để hướng dẫn phong cách video — hợp khi có sẵn ảnh sản phẩm/brand muốn video bám theo.

## Setup từng bước
1. Lấy API key tại dashboard Scrptly.
2. Cấu hình MCP client (ví dụ Claude Code/Cursor qua `mcp-remote`):
```json
{
  "mcpServers": {
    "scrptly-video-generator": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.scrptly.com/", "--header", "Authorization: Bearer [YOUR_SCRPTLY_API_KEY]"]
    }
  }
}
```
3. Gọi `generateAiVideo`, sau đó poll `getTaskStatus` tới khi `status = success`.

## Ví dụ thực tế
Đưa vào `context` 2 ảnh sản phẩm Wonder Mart kèm mô tả ("ly giữ nhiệt màu xanh, chụp studio"), prompt: "video quảng cáo 20 giây, phong cách năng động, sản phẩm xoay 360 độ, nhạc nền upbeat" → nhận `taskId`, poll tới khi có `resultVideoUrl`.

## Lưu ý / Lỗi thường gặp
- Luôn set `approveUpTo` — không set thì mặc định 10.000 token, có thể vượt ngân sách nếu prompt phức tạp.
- Là task bất đồng bộ (async) — phải tự poll `getTaskStatus`, không trả video ngay trong 1 lần gọi.
- Server còn khá mới, tài liệu ít ví dụ thực tế hơn AITuber — cần tự thử để biết giới hạn thật (độ dài video tối đa, tốc độ xử lý).

## Đánh giá cá nhân
- Điểm mạnh: input ảnh ngữ cảnh (context images) là điểm khác biệt hay — hợp giữ đúng hình ảnh sản phẩm/brand trong video thay vì để AI tự bịa; cơ chế `approveUpTo` kiểm soát chi phí tốt hơn nhiều MCP video khác không có giới hạn rõ.
- Điểm yếu: chỉ 2 tool, ít linh hoạt hơn AITuber (không có mẫu viral sẵn, không danh sách giọng để chọn); tài liệu sơ sài, cần tự dò khi gặp lỗi.
- Có nên dùng không: 6.5/10 — thử khi cần video bám sát ảnh sản phẩm có sẵn; nếu cần đa dạng mẫu/giọng đọc thì AITuber ở trên đầy đủ hơn.

## Link
- Trang chủ: https://scrptly.com/api/mcp
- Endpoint: https://mcp.scrptly.com/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import requests, time

def scrptly_generate_video(prompt: str, api_key: str, approve_up_to: int = 10000) -> str:
    headers = {"Authorization": f"Bearer {api_key}"}
    r = requests.post("https://mcp.scrptly.com/tools/generateAiVideo",
                       headers=headers,
                       json={"prompt": prompt, "approveUpTo": approve_up_to})
    task_id = r.json()["taskId"]

    while True:
        status = requests.post("https://mcp.scrptly.com/tools/getTaskStatus",
                                headers=headers, json={"taskId": task_id}).json()
        if status["status"] in ("success", "failed"):
            return status.get("resultVideoUrl", status["statusMessage"])
        time.sleep(5)
```

### OpenClaw
```json
{
  "mcpServers": {
    "scrptly-video-generator": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.scrptly.com/", "--header", "Authorization: Bearer [YOUR_SCRPTLY_API_KEY]"]
    }
  }
}
```

### Antigravity
```bash
echo 'SCRPTLY_API_KEY=[YOUR_SCRPTLY_API_KEY]' >> /etc/hermes.env
```
> ⚠️ Task là async — nếu Hermes tự động hoá, nhớ implement poll loop có timeout, đừng để treo vô hạn khi task fail âm thầm.
