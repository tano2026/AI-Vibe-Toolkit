# TikHub — MCP Server

## TL;DR
Một API key duy nhất để lấy data real-time từ 16+ mạng xã hội (TikTok, Douyin, Instagram, YouTube, Twitter/X, Xiaohongshu, Threads, Reddit...) — 1000+ endpoints REST + 990+ MCP tools cho AI agent. Trả tiền theo request, không gói tháng.

## Tool này dùng để làm gì
Bình thường muốn lấy data TikTok/Instagram thì phải tự viết scraper, lo bị block, lo captcha, lo maintain khi platform đổi giao diện. TikHub gánh hết phần đó — mày chỉ gọi 1 REST API là có ngay: chi tiết video, profile user, comments, kết quả search, trending, live stream, thậm chí data e-commerce (TikTok Shop).

Điểm ăn tiền với dân AI agent: họ có sẵn **MCP server hosted** (mcp.tikhub.io) — cắm thẳng vào Claude Desktop/Claude Code là agent tự query data social bằng ngôn ngữ tự nhiên, không cần viết glue code.

Nền tảng hỗ trợ: TikTok, Douyin, Instagram, YouTube, Twitter/X, Xiaohongshu (Red Note), Bilibili, Weibo, Threads, LinkedIn, Reddit, Kuaishou, WeChat, Lemon8, Zhihu + captcha solver và temp mail.

Billing kiểu pay-as-you-go: nạp tiền → trừ theo từng request, không có threshold tháng. Đăng ký được tặng $0.05 credit test thử (ít, nhưng đủ bắn vài chục request xem data shape).

## Setup từng bước

**Cách 1 — REST API (cho script/agent Python):**
1. Đăng ký tại https://user.tikhub.io/login, verify email
2. Vào User Center → API Token → tạo token
3. Gọi API với header `Authorization: Bearer YOUR_API_KEY`

```python
import requests

url = "https://api.tikhub.io/api/v1/tiktok/app/v3/fetch_one_video"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
params = {"aweme_id": "7350810998023949599"}
data = requests.get(url, headers=headers, params=params).json()
print(data["data"]["desc"], data["data"]["statistics"]["play_count"])
```

**Cách 2 — Python SDK chính chủ:**
```bash
pip install tikhub
```
```python
from tikhub import TikHub
client = TikHub(api_key="YOUR_API_KEY")
video = client.douyin_web.fetch_one_video(aweme_id="72512...")
print(video.aweme_detail.desc)
```
SDK map 1:1 với OpenAPI spec — tên method = đoạn cuối của API path, đọc docs là biết dùng SDK.

**Cách 3 — MCP cho Claude Desktop:**
```json
{
  "mcpServers": {
    "tikhub-tiktok": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.tikhub.io/tiktok/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}
```
Mỗi platform một endpoint MCP riêng (`/tiktok/mcp`, `/instagram/mcp`...) — chỉ bật platform cần dùng, đỡ ngập tool.

## Ví dụ thực tế
Use case cho kênh Tano: research content viral để làm faceless video.

Input: keyword "AI agent" trên TikTok
```python
url = "https://api.tikhub.io/api/v1/tiktok/web/fetch_search_video"
params = {"keyword": "AI agent", "count": 20}
```
Output: 20 video kèm play_count, digg_count, share_count, desc, author → sort theo play_count → lọc ra 5 hook đang viral → dựa vào đó viết script video mới. Toàn bộ pipeline chạy tự động qua Hermes, không mở TikTok tay lần nào.

## Lưu ý / Lỗi thường gặp
- **401/403** → token sai hoặc chưa activate; token dán vào Swagger UI thì KHÔNG kèm chữ "Bearer", còn gọi API thẳng thì PHẢI có "Bearer "
- **402** → hết credit; free credit $0.05 chỉ đủ test, dùng thật phải nạp (Stripe/PayPal/crypto)
- **429** → bắn quá nhanh, thêm sleep giữa các request
- Nhiều endpoint cũ bị deprecated (Douyin V1/V2, TikTok V2) → luôn dùng version mới nhất trong docs, đừng copy code mẫu cũ trên mạng
- User ở Trung Quốc đại lục dùng `api.tikhub.dev`, còn lại dùng `api.tikhub.io` — đừng nhầm domain kẻo chậm
- Data lấy về là public data, nhưng dùng để spam/fake interaction là vi phạm ToS của họ (và của platform)

## Đánh giá cá nhân
- Điểm mạnh: coverage khủng (16 platform, 1000+ endpoints, đặc biệt mạnh mảng China apps — Douyin, Xiaohongshu, Kuaishou mà ít đối thủ nào có); MCP hosted sẵn không cần self-host; pay-per-use không ép gói tháng; SDK Python/Java/TS chính chủ + n8n community node
- Điểm yếu: phụ thuộc hoàn toàn vào bên thứ ba scrape — platform siết là endpoint có thể chết hoặc đổi; free credit quá bèo để đánh giá nghiêm túc; pricing theo request nên dùng batch lớn phải tính kỹ chi phí; không có Facebook (điểm trừ cho customer research FB Pages — vẫn cần Bright Data cho mảng đó)
- Có nên dùng không: **8/10** — đáng tiền nhất cho content research đa nền tảng (nhất là TikTok/Douyin/Xiaohongshu), rẻ hơn nhiều so với tự build scraper. Không thay thế được Bright Data cho Facebook.

## Link
- Website: https://tikhub.io
- Docs: https://docs.tikhub.io
- MCP docs: https://mcp.tikhub.io
- Python SDK: https://github.com/TikHub/TikHub-API-Python-SDK
- PyPI: https://pypi.org/project/tikhub/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Gọi thẳng REST API bằng urllib — không cần MCP, không cần pip install
import urllib.request, urllib.parse, json, os

API_KEY = os.environ["TIKHUB_API_KEY"]

def tikhub_get(path, **params):
    url = f"https://api.tikhub.io{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {API_KEY}"
    })
    return json.loads(urllib.request.urlopen(req).read())

# Ví dụ: search video TikTok theo keyword
data = tikhub_get("/api/v1/tiktok/web/fetch_search_video",
                  keyword="AI agent", count=20)
for v in data["data"]["item_list"][:5]:
    print(v["desc"], v["statistics"]["play_count"])
```

### OpenClaw
```bash
# Cắm MCP remote — mỗi platform 1 endpoint riêng
npx mcp-remote https://mcp.tikhub.io/tiktok/mcp \
  --header "Authorization: Bearer $TIKHUB_API_KEY"
```

### Antigravity
```bash
# SaaS hosted — không cần deploy gì trên VPS
# Chỉ cần set env cho Hermes:
echo 'export TIKHUB_API_KEY="your_key_here"' >> /opt/env/hermes.env
```
> ⚠️ Pay-per-request — Hermes chạy batch lớn phải có giới hạn số request/run, kẻo cháy credit. Set env `TIKHUB_API_KEY`, không hardcode key vào script.
