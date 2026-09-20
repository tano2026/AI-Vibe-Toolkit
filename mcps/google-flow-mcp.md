# Google Flow MCP — MCP Server

## ⚠️ CẢNH BÁO TRÙNG TÊN — đọc trước khi cài (phát hiện sau khi đào sâu 21/08/2026)

Có **5 tool khác nhau** cùng tên hoặc tên rất giống "google-flow-mcp". Chỉ **1 cái an toàn** — 4 cái còn lại là browser automation reverse-engineer (đúng loại rủi ro ToS như FlowKit đã cảnh báo):

| Tên/tác giả | Loại | An toàn? |
|---|---|---|
| **`joshuadaniel-8090/google-flow-mcp`** (trên PyPI) | API chính thức Google AI | ✅ **ĐÂY LÀ CÁI ĐANG DÙNG** |
| `roshanarnav25-sloth/google-flow-mcp` | Reverse-engineer tRPC nội bộ Flow, tự nhận "v0.1, uncalibrated" | ❌ |
| `hitjcl/google-flow-mcp` | Browser automation qua Chrome/Edge, 22 tool | ❌ |
| `Mitanshp5/Google-Flow_MCP` | Chrome CDP automation, profile đã đăng nhập | ❌ |
| `TMSSS05/google-flow-browser-mcp` | Playwright + CDP automation | ❌ |

**Cách phân biệt chắc chắn nhất:** cái đúng cài qua `uvx google-flow-mcp` hoặc `pip install google-flow-mcp` (có trên PyPI, không cần Chrome/trình duyệt gì cả). Nếu thấy hướng dẫn nào bắt mở Chrome với `--remote-debugging-port` hoặc yêu cầu đăng nhập Google trong trình duyệt — đó là 1 trong 4 cái rủi ro, KHÔNG PHẢI cái này.

## TL;DR
MCP server cho Claude Desktop/Code truy cập trực tiếp Nano Banana (ảnh) và Veo (video) — dùng API chính thức Google AI, KHÔNG reverse-engineer như FlowKit. An toàn hơn cho việc dùng thật trong kinh doanh, không có rủi ro khoá tài khoản.

## Tool này dùng để làm gì
Cho Claude gọi thẳng model tạo ảnh/video của Google trong lúc chat — Claude tự viết prompt, tự gọi tool, tự chờ kết quả (video mất 1-4 phút, Claude tự đợi). Dùng cho content Trùm Sân Bay: tạo ảnh minh hoạ, video ngắn cinematic có âm thanh, hoặc chuỗi ảnh→video (Nano Banana Pro tạo ảnh trước, Veo animate ảnh đó thành video).

| Capability | Model | Giá |
|---|---|---|
| Tạo/sửa ảnh chất lượng cao | Nano Banana Pro (gemini-3-pro-image) | Free |
| Tạo ảnh nhanh | Nano Banana 2 (gemini-3.1-flash-image) | Free |
| Video cinematic có âm thanh gốc | Veo 3.1 (veo-3.1-generate-preview) | Trả phí |

## 6 tool thật (xác nhận từ PyPI, không đoán)

| Tool | Làm gì |
|---|---|
| `flow_generate_image` | Text → 1-4 ảnh, tới 4K, chọn model |
| `flow_edit_image` | Sửa ảnh bằng lời (inpaint/outpaint/đổi nền) |
| `flow_generate_image_with_references` | Tạo ảnh có tới 14 ảnh tham chiếu dẫn hướng |
| `flow_generate_video` | Text → video cinematic, có thể neo khung hình |
| `flow_extend_video` | Kéo dài clip Veo đã có |
| `flow_image_to_video` | Pipeline đủ: ảnh Nano Banana Pro → video Veo 3.1 |

⚠️ **Development Status: 3 - Alpha** (ghi rõ trên PyPI) — package mới (release 29/6/2026), dùng thận trọng cho việc quan trọng, chưa phải bản ổn định lâu năm.

## Setup từng bước (ĐÃ SỬA — bản cũ hướng dẫn sai, phức tạp hơn cần thiết)
1. Cần Google AI API key — lấy free tại aistudio.google.com/apikey
2. Cài — chỉ 1 dòng, dùng `uv` (khuyến nghị, không cần tự tạo venv):
```bash
uvx google-flow-mcp
# hoặc: pip install google-flow-mcp
```
3. Cấu hình trong Claude Desktop config (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "google-flow": {
      "command": "uvx",
      "args": ["google-flow-mcp"],
      "env": {
        "GOOGLE_API_KEY": "YOUR_GOOGLE_AI_STUDIO_KEY"
      }
    }
  }
}
```
⚠️ Tên biến môi trường đúng là `GOOGLE_API_KEY` (bản trước ghi nhầm `GOOGLE_AI_API_KEY` — đã sửa).

**Vị trí file config theo hệ điều hành:**
| Platform | Đường dẫn |
|---|---|
| Windows Store | `%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json` |
| Windows Direct | `%APPDATA%\Claude\claude_desktop_config.json` |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

4. Restart Claude Desktop — tool xuất hiện, gọi trực tiếp bằng lời (không cần cú pháp riêng)
5. File output mặc định lưu ở `~/google_flow_outputs/` — đổi bằng biến `FLOW_OUTPUT_DIR` nếu muốn chỗ khác

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

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")

def generate_image_nano_banana(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent"
    payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(
        f"{url}?key={GOOGLE_API_KEY}", data=payload,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())
```
> ⚠️ Đây là gọi trực tiếp API, không qua MCP — endpoint/schema cần verify lại theo docs Google AI mới nhất trước khi tin dùng, chưa test thật.

### OpenClaw / Claude Code
```bash
claude mcp add google-flow -- uvx google-flow-mcp
```
Gọi trực tiếp bằng lời trong chat — "tạo ảnh...", "animate ảnh này thành video..." — Claude tự chọn đúng tool trong 6 tool đã liệt kê ở trên.

### Antigravity
```bash
# Cài trên VPS nếu muốn Claude Code chạy trên VPS truy cập được — chỉ cần uv,
# không cần git clone/venv thủ công như trước
curl -LsSf https://astral.sh/uv/install.sh | sh   # cài uv nếu chưa có
uvx google-flow-mcp   # tự tải và chạy, không cần cài thường trực
```
