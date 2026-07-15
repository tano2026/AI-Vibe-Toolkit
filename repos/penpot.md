# Penpot — GitHub Repo

## TL;DR
Design tool mã nguồn mở thay Figma — tự host được, file lưu dạng SVG/CSS/JSON thay vì format độc quyền, không mất phí per-seat. 56K stars, dùng tốt cho team agency làm brand/UI mà không muốn phụ thuộc Figma.

## Repo này dùng để làm gì
Penpot làm gần hết những gì Figma làm: vẽ UI, prototype click-through, component/design system, real-time collab, Dev Mode xuất thẳng CSS/HTML/SVG cho dev copy paste. Điểm khác biệt chính so với Figma:
- Mã nguồn mở (MPL-2.0), tự host bằng Docker được → dữ liệu design nằm trên server của mình, không phụ thuộc Figma
- File lưu dạng SVG/CSS/JSON chuẩn mở, không phải binary độc quyền → đọc/sửa/migrate được ngay cả khi không dùng Penpot nữa
- Có native CSS Grid/Flex layout — dev đọc code layout dễ hơn Auto Layout của Figma
- Có MCP server chính thức → agent AI đọc/sửa file design trực tiếp qua API, hợp xu hướng agent-driven design workflow
- Import được file Figma qua converter (layout/component cơ bản chuyển tốt, Auto Layout phức tạp cần chỉnh tay)

Điểm yếu thật: hiệu năng file lớn còn thua Figma, hệ plugin ít hơn nhiều, không có FigJam-style whiteboard sẵn (phải cài kit riêng), AI feature trong app còn sơ khai hơn Figma.

## Setup từng bước
1. Dùng bản cloud miễn phí (không giới hạn project/file/thành viên ở free tier): vào `design.penpot.app`, tạo tài khoản.
2. Muốn tự host (để giữ data trong nhà, hợp brand An Bình cần bảo mật thông tin khách):
```bash
git clone https://github.com/penpot/penpot.git
cd penpot/docker
docker compose -p penpot -f docker-compose.yaml up -d
```
Mặc định Docker stack chạy ở port 9001, cần Docker + Docker Compose, nên có reverse proxy nếu public ra ngoài.
3. Import file Figma cũ (nếu có) qua Penpot Exporter plugin bên Figma, rồi import ngược vào Penpot.
4. Muốn cho agent AI đọc/sửa file design → cài Penpot MCP server + plugin theo hướng dẫn trong docs.

## Ví dụ thực tế
Đang làm brand An Bình Airport Services (Deep Navy #1B3A6B + Hanoi Gold #B8973A, logomark 2 đường chéo song song) — thay vì trả phí Figma seat cho team nhỏ, dựng brand board + component library (logo variants, color token, type pairing Cormorant Garamond + Inter) trực tiếp trong Penpot, xuất CSS token thẳng cho dev code landing page `fasttracknoibai.com`, không qua bước "dev tự đo lại pixel" như Figma Dev Mode hay bị lệch.

## Lưu ý / Lỗi thường gặp
- Tự host cần biết Docker + DNS + reverse proxy — không phải "click 1 phát xong", cần chút kiến thức ops.
- File phức tạp/nặng (nhiều component lồng nhau) load chậm hơn Figma rõ rệt.
- Plugin ecosystem còn mỏng — mấy plugin quen tay bên Figma (auto-generate content, advanced prototyping) chưa chắc có bản tương đương bên Penpot.
- Không có FigJam built-in — brainstorm/whiteboard phải cài thêm kit riêng hoặc dùng tool khác song song.
- Bản cloud free giới hạn số seat, cần trả phí nếu team lớn dần (dù vẫn rẻ hơn Figma per-seat rất nhiều).

## Đánh giá cá nhân
- Điểm mạnh: free thật (không phải bản dùng thử), tự host được nên chủ động 100% với data brand khách hàng, xuất CSS/SVG chuẩn dev đọc thẳng, có MCP server nên hợp xu hướng để agent tự thao tác file design sau này.
- Điểm yếu: hiệu năng và độ mượt vẫn kém Figma với file lớn, hệ plugin còn thiếu, cần chút công sức nếu muốn tự host thay vì dùng bản cloud có sẵn.
- Có nên dùng không: 7/10 — hợp nếu ưu tiên data ownership + tiết kiệm chi phí seat cho agency nhỏ; chưa hợp nếu team đã quen sâu vào hệ plugin Figma hoặc làm file cực phức tạp cần hiệu năng cao.

## Link
- Repo: https://github.com/penpot/penpot
- Docs: https://design.penpot.app

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Penpot có REST API thật (khác Hallmark) — Hermes gọi được trực tiếp qua urllib
import urllib.request, json

PENPOT_BASE = "https://design.penpot.app/api"  # hoặc domain tự host

def penpot_login(email, password):
    req = urllib.request.Request(
        f"{PENPOT_BASE}/rpc/command/login-with-password",
        data=json.dumps({"email": email, "password": password}).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    resp = urllib.request.urlopen(req)
    return resp.headers.get('Set-Cookie')

# Sau khi có session cookie, gọi tiếp các rpc/command/... để list file, export asset, v.v.
# Docs API đầy đủ: xem OpenAPI spec trong repo /backend/resources/
```

### OpenClaw
```bash
# Nếu muốn agent tự động dựng UI mockup từ code hiện có, cài Penpot MCP server
npx @penpot/mcp-server
# Rồi thêm vào mcp config của OpenClaw như 1 connector bình thường
```

### Antigravity
```bash
# Deploy self-hosted Penpot trên VPS (nếu cần giữ toàn bộ brand asset in-house)
git clone https://github.com/penpot/penpot.git /opt/penpot
cd /opt/penpot/docker && docker compose -p penpot -f docker-compose.yaml up -d
# Nhớ set reverse proxy (nginx) + domain riêng, port mặc định 9001
```
> ⚠️ Bản tự host cần Postgres + Redis đi kèm (đã có trong docker-compose) — đừng chạy chung stack với service khác đang share port 9001.