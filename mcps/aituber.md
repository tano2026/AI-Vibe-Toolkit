# AI Video by AITuber — MCP Server

## TL;DR
MCP hosted (remote, không cần cài local) — mô tả video bằng ngôn ngữ tự nhiên, nhận về MP4 có voiceover + phụ đề, có sẵn 1300+ giọng đọc. Hỗ trợ chính thức cả Claude, ChatGPT, Cursor, Notion AI, OpenClaw, Hermes (đúng tên 2 agent nội bộ Tano — trùng tên ngẫu nhiên, không liên quan).

## Tool này dùng để làm gì
Server host sẵn tại `https://mcp.aituber.app`, không cần npx/cài gì trên máy. Đăng nhập tài khoản AITuber (hoặc dùng API key cho môi trường không có UI như VPS/CI), Claude tự có công cụ:
- Viết kịch bản + tạo video hoàn chỉnh từ mô tả ("video 60 giây về 5 sự thật đại dương, giọng nữ Anh")
- Duyệt/chọn giọng đọc trong hơn 1300 giọng
- Tạo clip AI điện ảnh 6 giây (ví dụ cảnh sóng vỗ slow-motion)
- Dùng cảnh quay stock thật tự khớp với lời thuyết minh (hợp video tin tức/giáo dục/tài liệu)
- Mẫu "X-ray" viral ("điều gì xảy ra nếu ăn 100 quả chuối") và mẫu nhân vật nhất quán qua nhiều video
- Check số credit còn lại trước khi tạo

## Setup từng bước
1. Claude Desktop/claude.ai: **Settings → Connectors → Add custom connector**, dán URL:
```
https://mcp.aituber.app
```
2. Claude Code (tự động xuất hiện sau bước 1, hoặc thêm riêng qua terminal):
```bash
claude mcp add --transport http aituber https://mcp.aituber.app
```
3. Không có UI để đăng nhập (VPS/CI, dùng cho Hermes/OpenClaw) — tạo API key tại `app.aituber.app/dashboard/api-keys`, gắn header:
```json
{
  "mcpServers": {
    "aituber": {
      "url": "https://mcp.aituber.app",
      "headers": { "Authorization": "Bearer ak_your_key" }
    }
  }
}
```

## Ví dụ thực tế
"Tạo video 45 giây giới thiệu Fast Track An Bình tại Nội Bài, giọng nam Việt, phong cách tài liệu, dùng cảnh quay sân bay thật khớp lời thuyết minh" — MCP tự viết kịch bản, chọn giọng, khớp stock footage, xuất MP4 kèm phụ đề, trả link tải.

## Lưu ý / Lỗi thường gặp
- Trả phí theo credit (tài khoản AITuber riêng) — check credit trước khi giao task lớn.
- MCP chỉ thao tác trong phạm vi tài khoản AITuber của mình, không đọc được file/trình duyệt khác trên máy — nhưng vẫn cần approve trước khi client thực hiện hành động (theo cơ chế MCP chuẩn).
- Vì hosted remote, không có gì để tự update — server luôn chạy bản mới nhất, giọng/mẫu mới tự xuất hiện.

## Đánh giá cá nhân
- Điểm mạnh: setup cực nhanh (dán 1 URL, không npx/không docker), hỗ trợ chính thức OpenClaw/Hermes ngay trong docs — rất tiện cho agent 24/7 trên VPS; kết hợp viết kịch bản + TTS + stock footage + clip AI trong 1 chỗ.
- Điểm yếu: phụ thuộc hoàn toàn vào dịch vụ ngoài (không tự host được), trả phí theo credit, chưa rõ chất lượng voice tiếng Việt thế nào (cần test thật trước khi dùng cho content ABTRIP/An Bình).
- Có nên dùng không: 7/10 — đáng thử cho video giải thích/dạng "X-ray" viral tiếng Anh; cần test kỹ giọng Việt trước khi đưa vào pipeline chính.

## Link
- Trang chủ: https://aituber.app/mcp
- Setup Claude: https://aituber.app/claude/
- Setup OpenClaw: https://aituber.app/openclaw/
- Setup Hermes: https://aituber.app/hermes/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import requests

def aituber_create_video(prompt: str, api_key: str) -> dict:
    """Gọi thẳng REST/MCP endpoint của AITuber qua HTTP — không cần MCP client lib."""
    resp = requests.post(
        "https://mcp.aituber.app/tools/create_video",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"prompt": prompt}
    )
    return resp.json()
```

### OpenClaw
```json
{
  "mcpServers": {
    "aituber": {
      "url": "https://mcp.aituber.app",
      "headers": { "Authorization": "Bearer [YOUR_AITUBER_API_KEY]" }
    }
  }
}
```
> Docs chính thức có hướng dẫn riêng cho OpenClaw: https://aituber.app/openclaw/

### Antigravity
```bash
# Không cần deploy gì — server đã hosted sẵn. Chỉ cần lưu API key vào .env của VPS.
echo 'AITUBER_API_KEY=[YOUR_AITUBER_API_KEY]' >> /etc/hermes.env
```
> ⚠️ Test giọng tiếng Việt trước khi cho Hermes tự động tạo video publish thật.
