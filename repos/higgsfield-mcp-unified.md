# higgsfield-mcp-unified — GitHub Repo

## TL;DR
MCP server chạy trên máy mình (Python, MIT, alpha v0.1.0) gom Higgsfield vào 1 giao diện: gọi được model qua API chính thức, và tuỳ chọn thêm "cloud backend" để dùng model mới (Sora 2, Veo 3.x, Kling 3.0, Seedance 2.0...). Có thêm vài thứ bản chính thức không nhấn mạnh: liệt kê model không tốn credit, kiểm tra auth trước khi tạo, xem số dư. **Rất nhỏ (4 sao, 3 fork), cloud backend dễ hỏng và có thể vi phạm điều khoản. Dùng bản chính thức trước.**

## Repo này dùng để làm gì
Cho Claude/agent tạo ảnh và video AI qua Higgsfield bằng tool gọi có cấu trúc: `list_models`, `generate_image`, `generate_video`, `generate_speech_video` (talking-head), `get_status`/`subscribe` (chờ kết quả), `upload_image`, `create_character` (train nhân vật Soul), `preflight_check`, `get_balance`, `cancel_job`. Tác giả: Hikhakk. Repo: `Hikhakk/higgsfield-mcp-unified`.

## So với bản chính thức (đã có trong kho: `mcps/higgsfield.md`)
| | Bản chính thức `mcp.higgsfield.ai/mcp` | `higgsfield-mcp-unified` |
|---|---|---|
| Chạy ở đâu | Dịch vụ của Higgsfield, OAuth (không cần API key riêng) | Trên máy/VPS mình |
| Auth | Đăng nhập OAuth | `HIGGSFIELD_API_KEY` + `HIGGSFIELD_SECRET` |
| Credit | Luôn trừ credit theo giá chuẩn, không dùng được "unlimited" của web | Theo API chính thức: cũng trừ credit |
| Model | Danh mục của Higgsfield | API chính thức: Soul, FLUX.1, Seedream v4, DOP, Seedance v1 Pro, Kling v2.1. Cloud backend (opt-in): Sora 2, Veo 3.x, Kling 3.0, Seedance 2.0, Wan, Nano Banana... |
| Độ ổn định | Sản phẩm chính thức | Alpha; cloud backend tự tác giả cảnh báo sẽ hỏng |
| Điểm riêng | Đơn giản, không cài gì | Output có cấu trúc, liệt kê model/preflight không tốn credit, chạy được từ agent trên VPS (Hermes) |

## ⚠️ Cảnh báo quan trọng
Cloud backend dùng cách gọi suy ngược từ web của Higgsfield, cần token đăng nhập (Clerk, sống khoảng 7 ngày), hay bị chặn bot, endpoint đổi không báo. Chính tác giả ghi "probably against ToS". Dùng nó có thể làm **tài khoản Higgsfield của mày bị khoá**. Khuyến nghị: KHÔNG bật `HIGGSFIELD_ENABLE_WEB_BACKEND` cho tài khoản thật của Tano Agency hay của khách.

## Setup
```bash
# Cần uv (https://docs.astral.sh/uv/)
git clone https://github.com/Hikhakk/higgsfield-mcp-unified
cd higgsfield-mcp-unified
uv sync
export HIGGSFIELD_API_KEY="..."      # từ platform.higgsfield.ai (API chính thức)
export HIGGSFIELD_SECRET="..."
uv run higgsfield-mcp
```
Một nguồn khác ghi cài bằng `uvx higgsfield-mcp` hoặc `pipx install higgsfield-mcp-unified`; chưa xác nhận tên package có trên PyPI — dùng cách clone ở trên cho chắc.

## Ví dụ thực tế
Tạo cảnh mở đầu video giới thiệu một dịch vụ/sản phẩm của brand bất kỳ (ví dụ: Fast Track Nội Bài của ABTRIP): `preflight_check` → `get_balance` (biết còn bao nhiêu credit) → `generate_video` với model đã xác nhận có trong `list_models` → `subscribe` chờ xong → tải về ghép bằng `ffmpeg-media-toolkit`.

## Lưu ý / Lỗi thường gặp
- Chưa chạy thử lần nào; mọi chi tiết lấy từ README/trang tổng hợp
- Số model "43" là tác giả tự nêu, gồm cả mục thử nghiệm — chỉ nhóm "official verified" mới nên tin
- Tạo video tốn credit thật. Luôn `get_balance` + `list_models` (miễn phí) trước khi bấm tạo
- Tạo khuôn mặt/nhân vật thật của người khác cần có quyền; Soul character chỉ dùng ảnh mình có quyền sử dụng

## Đánh giá cá nhân
- Điểm mạnh: MIT, output có cấu trúc, preflight/balance tiện cho agent chạy tự động, chạy local
- Điểm yếu: 4 sao, alpha, 1 người bảo trì; cloud backend rủi ro tài khoản; trùng chức năng lõi với bản chính thức
- Có nên dùng: 4/10 lúc này. Dùng bản chính thức (`mcps/higgsfield.md`) trước. Chỉ cân nhắc bản này khi cần Hermes tự động gọi API chính thức trên VPS, và chỉ với backend chính thức

## Link
- Repo: https://github.com/Hikhakk/higgsfield-mcp-unified
- Bản chính thức: https://mcp.higgsfield.ai/mcp (docs: higgsfield.ai/creator-hub/help-center/mcp-cli/what-is-higgsfield-mcp)
- Liên quan trong kho: `mcps/higgsfield.md`, `mcps/fal-mcp.md`, `agents/company/skills/ffmpeg-media-toolkit/SKILL.md`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Chạy server MCP local rồi để Hermes gọi qua client MCP của nó.
# Biến môi trường lấy từ .env của VPS, KHÔNG ghi vào file trong kho:
#   HIGGSFIELD_API_KEY=[HIGGSFIELD_API_KEY]
#   HIGGSFIELD_SECRET=[HIGGSFIELD_SECRET]
# Thứ tự gọi an toàn cho credit: preflight_check -> get_balance -> list_models -> generate_video -> subscribe
```

### OpenClaw
```bash
# Thêm vào cấu hình MCP của OpenClaw (command: uv, args: run higgsfield-mcp, cwd: thư mục repo).
# Chưa kiểm chứng cú pháp cấu hình cụ thể — xem docs OpenClaw bản đang chạy.
```

### Antigravity
```bash
git clone https://github.com/Hikhakk/higgsfield-mcp-unified && cd higgsfield-mcp-unified && uv sync
```
> ⚠️ Không bật HIGGSFIELD_ENABLE_WEB_BACKEND trên tài khoản thật. Tạo video tốn credit thật.
