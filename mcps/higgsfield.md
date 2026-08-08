# Higgsfield — MCP Server

> ⚠️ **Lưu ý trùng tên:** Tài liệu chính thức của Higgsfield MCP nhắc tới việc
> tương thích với "OpenClaw" và "Hermes Agent" như tên framework agent phổ
> biến ngoài cộng đồng. Đây là trùng tên ngẫu nhiên với 2 agent nội bộ của Tano
> (OpenClaw = orchestrator VPS, Hermes = executor Python) — không phải cùng 1
> hệ thống, không liên quan gì tới nhau.

## TL;DR
MCP chính thức của Higgsfield — mở khoá 30+ model tạo ảnh/video cinematic (Veo 3.1, Kling 3.0, Sora 2, Seedance, Soul, Cinema Studio) ngay trong chat, không cần API key, không cần vào từng web riêng của mỗi model.

## Tool này dùng để làm gì
Claude nhận mô tả cảnh quay bằng ngôn ngữ tự nhiên, tự chọn model phù hợp (hoặc theo tên model chỉ định), viết prompt đúng format riêng của model đó, gọi generate, và trả kết quả ảnh/video thẳng vào chat.

## Setup từng bước
1. Trong Claude web/desktop: Settings → Connectors → thêm "Higgsfield" → xác thực OAuth qua tài khoản Higgsfield (không cần API key thủ công).
2. Có 5 tool chính: `generate_image`, `generate_video`, train character (giữ nhân vật nhất quán qua nhiều cảnh), browse lịch sử tạo, và style preset.
3. Test: "tạo ảnh sản phẩm [tên] đặt trên mặt bàn đá cẩm thạch, ánh sáng buổi sáng ấm" — kiểm tra output trước khi dùng cho việc thật.
4. Muốn dùng ngoài Claude (Hermes/OpenClaw thật của Tano): cần server MCP riêng qua FastMCP wrapper (vd `geopopos/higgsfield_ai_mcp` trên GitHub) với `HF_API_KEY`/`HF_SECRET` — bản này cần API key, khác bản hosted không cần key.

## Ví dụ thực tế
Cho kênh **AI review (TikTok/Shorts)**: mô tả "cảnh mở đầu điện thoại rơi chậm xuống bàn, slow motion cinematic, ánh sáng neon" — Higgsfield tự chọn model video phù hợp (kiểu Cinema Studio) và trả clip 5-10 giây dùng làm B-roll, không cần quay dựng thật.

## Lưu ý / Lỗi thường gặp
- Bản hosted (không cần key) tiện nhưng gắn với tài khoản Higgsfield — chi phí theo credit của họ, cần kiểm tra hạn mức trước khi dùng batch lớn.
- Chất lượng video phụ thuộc model được chọn tự động — với brief phức tạp nên chỉ định rõ tên model muốn dùng thay vì để tự chọn.
- Đừng nhầm tên "OpenClaw"/"Hermes Agent" trong tài liệu Higgsfield với agent thật của Tano — 2 hệ thống hoàn toàn khác nhau dù trùng tên.

## Đánh giá cá nhân
- Điểm mạnh: gom 30+ model vào 1 kết nối, không cần học prompt riêng từng model, tiết kiệm thời gian brainstorm B-roll cho content video.
- Điểm yếu: phụ thuộc credit/tài khoản Higgsfield, chưa rõ chi phí dài hạn nếu dùng volume cao cho nhiều kênh cùng lúc.
- Có nên dùng không: 7/10 — đáng thử cho B-roll/thumbnail động của Trùm Sân Bay và AI review channel, cần theo dõi chi phí trước khi đưa vào pipeline chính thức.

## Link
- MCP hosted: https://mcp.higgsfield.ai
- Repo self-host (cần API key): https://github.com/geopopos/higgsfield_ai_mcp
- Docs: https://higgsfield.ai/mcp

---

## 🤖 Agent Integration

### Hermes (Python)
Bản hosted MCP (mcp.higgsfield.ai) yêu cầu OAuth qua Claude connector, KHÔNG gọi thẳng
được từ script Python thuần bằng urllib. Muốn Hermes tự động hoá (không qua Claude chat),
dùng REST wrapper tự host `geopopos/higgsfield_ai_mcp` (cần HF_API_KEY/HF_SECRET lấy từ
tài khoản Higgsfield → Settings → API):

```python
import urllib.request, json, os

HF_API_KEY = os.environ.get("HF_API_KEY")
HF_SECRET = os.environ.get("HF_SECRET")

def higgsfield_generate_image(prompt, model="soul"):
    url = "https://api.higgsfield.ai/v1/image/generate"  # endpoint theo doc repo wrapper
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "X-HF-Secret": HF_SECRET,
        "Content-Type": "application/json"
    }
    payload = json.dumps({"prompt": prompt, "model": model}).encode()
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    return json.loads(urllib.request.urlopen(req).read())

# vd: tạo ảnh sản phẩm ABTRIP cho content Trùm Sân Bay
# result = higgsfield_generate_image("SIM 4G đặt trên bàn đá cẩm thạch, ánh sáng buổi sáng ấm")
```
> ⚠️ Endpoint REST thật cần verify lại trong docs repo `geopopos/higgsfield_ai_mcp` trước
> khi chạy — repo là wrapper cộng đồng, không phải API chính chủ Higgsfield.

### OpenClaw
Add MCP server hosted vào config OpenClaw (không cần API key, auth OAuth 1 lần qua tài khoản):

```bash
# trong OpenClaw MCP config (vd mcp-servers.json hoặc tương đương)
# thêm entry:
# {
#   "name": "higgsfield",
#   "url": "https://mcp.higgsfield.ai",
#   "auth": "oauth"
# }
# Sau đó chạy lệnh xác thực (nếu OpenClaw hỗ trợ CLI auth flow):
npx @higgsfield/cli auth login
```
> Cách chắc ăn nhất vẫn là add qua Claude web/desktop Connectors trước để xác nhận
> account hoạt động, sau đó mới trỏ OpenClaw vào cùng MCP URL.

### Antigravity
Không cần deploy service riêng nếu dùng bản hosted (mcp.higgsfield.ai). Chỉ cần deploy
khi muốn self-host wrapper `geopopos/higgsfield_ai_mcp` để Hermes gọi thẳng REST:

```bash
# trên VPS (Tencent Cloud), nếu chọn self-host wrapper:
git clone https://github.com/geopopos/higgsfield_ai_mcp.git
cd higgsfield_ai_mcp
npm install
# set env HF_API_KEY, HF_SECRET trong .env hoặc pm2 ecosystem file
pm2 start index.js --name higgsfield-wrapper
```
> ⚠️ Chỉ làm bước này nếu Hermes THỰC SỰ cần gọi Higgsfield ngoài phiên Claude chat.
> Nếu chỉ dùng qua Claude (web/Cowork/Code) thì bản hosted qua Connectors là đủ,
> không cần deploy gì thêm.
