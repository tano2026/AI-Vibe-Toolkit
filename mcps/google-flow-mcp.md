# Google Flow MCP — MCP Server

## TL;DR
MCP server cho Claude Desktop/Code truy cập trực tiếp Nano Banana (ảnh) và Veo (video) — dùng API chính thức Google AI, KHÔNG reverse-engineer như FlowKit. An toàn hơn cho việc dùng thật trong kinh doanh, không có rủi ro khoá tài khoản.

## Tool này dùng để làm gì
Cho Claude gọi thẳng model tạo ảnh/video của Google trong lúc chat — Claude tự viết prompt, tự gọi tool, tự chờ kết quả (video mất 1-4 phút, Claude tự đợi). Dùng cho content Trùm Sân Bay: tạo ảnh minh hoạ, video ngắn cinematic có âm thanh, hoặc chuỗi ảnh→video (Nano Banana Pro tạo ảnh trước, Veo animate ảnh đó thành video).

| Capability | Model | Giá |
|---|---|---|
| Tạo/sửa ảnh chất lượng cao | Nano Banana Pro (gemini-3-pro-image) | Free |
| Tạo ảnh nhanh | Nano Banana 2 (gemini-3.1-flash-image) | Free |
| Video cinematic có âm thanh gốc | Veo 3.1 (veo-3.1-generate-preview) | Trả phí |

## Setup từng bước
1. Cần Google AI API key (Google AI Studio) — free tier đủ cho ảnh, cần gói trả phí riêng cho video
2. Clone và cài:
```bash
git clone https://github.com/joshuadaniel-8090/google-flow-mcp
cd google-flow-mcp
pip install -e ".[dev]"
pytest -v   # verify cài đúng
```
3. Cấu hình trong Claude Desktop config (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "google-flow": {
      "command": "python",
      "args": ["-m", "google_flow_mcp"],
      "env": {
        "GOOGLE_AI_API_KEY": "your-key-here",
        "FLOW_OUTPUT_DIR": "/path/to/output/folder"
      }
    }
  }
}
```
4. Restart Claude Desktop — tool xuất hiện, gọi trực tiếp bằng lời (không cần cú pháp riêng)

## Ví dụ thực tế
"Tạo ảnh photo-realistic quầy Fast Track sân bay Nội Bài buổi sáng sớm, ánh sáng ấm" → Nano Banana Pro ra ảnh → "giờ animate thành video 5 giây, camera lia chậm" → Veo 3.1 tạo video có âm thanh môi trường (tiếng động sân bay). Dùng làm B-roll cho content Trùm Sân Bay mà không cần quay thật.

## Lưu ý / Lỗi thường gặp
- Video Veo lưu trên server Google chỉ 2 NGÀY sau khi tạo — phải tải về ngay, không để đó rồi quên
- Mọi video Veo có watermark SynthID (nhúng vào file, không thấy bằng mắt nhưng máy quét được) — Google chính sách bắt buộc, không tắt được
- Video generation cần gói trả phí riêng (không nằm trong free tier như ảnh) — kiểm tra billing trước khi dùng nhiều

## Đánh giá cá nhân
- Điểm mạnh: dùng API chính thức, không rủi ro ToS như FlowKit/gflow-cli (cả 2 đều tự nhận "unofficial, reverse-engineered"); tích hợp thẳng vào Claude Desktop, không cần Chrome extension riêng
- Điểm yếu: video cần trả phí riêng, không rẻ bằng cách "dùng ké" credit Flow cá nhân như FlowKit làm — đây là đánh đổi an toàn lấy chi phí
- Có nên dùng: 9/10 — đây là lựa chọn đúng cho business thật, ưu tiên an toàn tài khoản hơn tiết kiệm vài đồng

## Link
- Repo: https://github.com/joshuadaniel-8090/google-flow-mcp
- PyPI: https://pypi.org/project/google-flow-mcp/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes không chạy MCP trực tiếp (MCP là giao thức cho Claude Desktop/Code) —
# nhưng có thể gọi thẳng Google AI API bằng urllib thuần nếu cần tạo ảnh/video
# ngoài luồng chat, không qua MCP layer:
import urllib.request, json, os

GOOGLE_AI_API_KEY = os.environ.get("GOOGLE_AI_API_KEY", "")

def generate_image_nano_banana(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent"
    payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(
        f"{url}?key={GOOGLE_AI_API_KEY}", data=payload,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())
```
> ⚠️ Đây là gọi trực tiếp API, không qua MCP — endpoint/schema cần verify lại theo docs Google AI mới nhất trước khi tin dùng, chưa test thật.

### OpenClaw / Claude Code
```bash
claude mcp add google-flow -- python -m google_flow_mcp
```
Gọi trực tiếp bằng lời trong chat — "tạo ảnh...", "animate ảnh này thành video..." — Claude tự chọn đúng tool.

### Antigravity
```bash
# Cài trên VPS nếu muốn Claude Code chạy trên VPS truy cập được
git clone https://github.com/joshuadaniel-8090/google-flow-mcp /opt/google-flow-mcp
cd /opt/google-flow-mcp && pip install -e ".[dev]"
```
