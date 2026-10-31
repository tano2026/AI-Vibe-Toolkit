# zalo-agent — GitHub Repo

## TL;DR
Con AI agent tự host (chạy trên máy/VPS của mình) sống ngay trong nick Zalo cá nhân. Quét QR như đăng nhập Zalo Web, cắm API key AI (OpenAI-compatible hoặc Anthropic), bật công tắc là nick Zalo tự trả lời khách. Gồm 15 tool, nối thêm MCP server ngoài, dashboard web, lập lịch, bộ nhớ lâu dài. TypeScript + SQLite, MIT. Tác giả: vuhai2002. Repo còn rất nhỏ (~5 star lúc kiểm tra) nhưng đang được cập nhật đều (release v0.4.0 ngày 24/10).

## Repo này dùng để làm gì
Biến nick Zalo cá nhân thành nhân viên CSKH AI chạy 24/7. Khách nhắn vào nick, agent đọc, trả lời, có thể tra web, đọc/gửi file, hẹn lịch nhắc, nhớ ngữ cảnh khách. Nhiều nick cùng lúc, quản lý qua dashboard web.

Nó đi đường "Zalo cá nhân không chính thức" (dùng thư viện zca-js, nhái giao thức Zalo Web). KHÔNG phải Zalo OA chính thức. Đây là điểm mạnh (không cần duyệt OA, không tốn phí API) và cũng là rủi ro lớn nhất (xem Lưu ý).

## Setup từng bước
Video TikTok nói 3 bước `npm install && npm run dev` + `localhost:3000`. Đối chiếu release notes thì thực tế khác. Dùng bản dưới đây.

**Cách 1 — Docker (khuyên dùng, theo release notes):**
1. `git clone https://github.com/vuhai2002/zalo-agent`
2. Copy file `.env` mẫu, điền `DASHBOARD_PASSWORD` và key AI
3. `bash deploy.sh`
4. Mở dashboard (cổng mặc định 3900 theo fork đang chạy bản này, kiểm tra lại README)

**Cách 2 — chạy thẳng Node (Node 24):**
1. `pnpm install`
2. `pnpm build:web`
3. `pnpm start`
4. Mở `http://127.0.0.1:3900`, đăng nhập bằng `DASHBOARD_PASSWORD`

**Sau khi lên:**
1. Vào Accounts → thêm tài khoản → quét QR bằng app Zalo trên điện thoại
2. Vào Settings, nhập provider/model (OpenAI-compatible hoặc Anthropic)
3. Bật công tắc bot hoạt động, nhắn thử từ nick khác

Lưu ý: bước 1-4 ở trên tao ghép từ release notes v0.4.0 và README của fork, vì README gốc không đọc được lúc research. Chạy thật thì đối chiếu README gốc.

## Ví dụ thực tế
Use case cho ABTRIP: một nick phụ chuyên nhận câu hỏi vé máy bay. Khách hỏi "SGN-HAN ngày 15/11 còn vé không?", agent trả lời mẫu, hẹn nhân viên gọi lại, lưu tên khách vào bộ nhớ. Câu chuyện giá vé thật thì phải nối MCP/tool tra giá (agent này tự không có dữ liệu giá).

Use case Wonder Mart: nick phụ nhận hỏi giờ mở cửa, sản phẩm, gửi ảnh/PDF menu bằng tool gửi file.

Chưa chạy thử, đây là ví dụ thiết kế. Cần test thật trước khi khẳng định.

## Lưu ý / Lỗi thường gặp
- **Rủi ro khóa nick:** zca-js là API không chính thức. Docs OpenClaw cho plugin cùng loại ghi thẳng: tự động hóa không chính thức có thể bị Zalo khóa/cấm. Fork của repo này cũng khuyên chỉ dùng nick phụ. KHÔNG gắn nick Zalo chính của ABTRIP vào.
- **Docs lệch video:** video nói npm + port 3000, thực tế dùng pnpm, build:web, Docker deploy.sh.
- **Nâng cấp v0.4.0:** nếu dùng 9Router phải từ v0.5.109; model vẽ ảnh `cx/gpt-5.5-image` đã ngừng, đổi sang `cx/gpt-image-2.5`. MCP server hơn 128 tool hoặc schema sai sẽ hiện "Cần duyệt lại", duyệt lại một lần là xong.
- **Cookie Zalo nằm trong thư mục data/**: không commit, không đưa lên GitHub.
- **Prompt injection:** bot đọc tin nhắn người lạ. v0.4.0 đã vá một số thứ (làm sạch tên người gửi, chặn SSRF ở web_fetch) nhưng đừng cho agent quyền nguy hiểm (gửi tiền, xóa dữ liệu).
- **Dự án nhỏ:** ít người kiểm chứng, một tác giả chính. Có fork `andyluu98/zalo-agent` thêm "chế độ chỉ đọc" (ghi log chat theo ngày cho AI khác lọc việc), cũng chỉ vài star.

## Đánh giá cá nhân
- Điểm mạnh: cài nhanh, có dashboard, đa nick, nối MCP, provider nào cũng chạy, MIT, release gần đây có sửa bảo mật nghiêm túc (pnpm audit từ 41 xuống 1 cảnh báo).
- Điểm yếu: dựa API Zalo không chính thức nên nick có thể bị khóa bất cứ lúc nào. Repo nhỏ, ít người dùng thật. Docs trên video sai so với thực tế. Chưa có dữ liệu độ ổn định dài hạn.
- Có nên dùng không: **6/10**. Đáng chạy thử trên nick phụ để làm demo/POC, xây content. Không đủ an toàn để làm kênh CSKH chính của ABTRIP. Kênh chính thì đi Zalo OA (đang làm trong dự án Zalo OA ABTRIP).

---

## 🤖 Agent Integration

Chưa xác minh được REST API của repo này (README gốc không đọc được), nên không đưa code gọi API bịa. Phần dưới chỉ gồm thứ đã thấy trong release notes.

### Hermes (Python)
```python
# Không có REST API được xác minh. Nếu cần Hermes nói chuyện qua Zalo,
# dùng plugin đã có: cuongdev/hermes-zalo-plugin (42 star), cùng hướng zca-js.
# Cần dữ liệu từ zalo-agent thì đọc dashboard hoặc DB SQLite trong data/ (chỉ đọc).
```

### OpenClaw
```bash
# OpenClaw có plugin Zalo cá nhân chính chủ (cũng zca-js, cũng rủi ro khóa nick):
openclaw plugins install @openclaw/zalouser
openclaw channels login --channel zalouser
```

### Antigravity
```bash
git clone https://github.com/vuhai2002/zalo-agent
cd zalo-agent
# điền .env (DASHBOARD_PASSWORD, key AI)
bash deploy.sh
# Chạy Node thẳng thay vì Docker:
# pnpm install && pnpm build:web && pnpm start
```
> ⚠️ Chạy trên VPS thì không mở cổng dashboard ra internet. Đặt sau VPN/Tailscale hoặc reverse proxy có auth. Không để lộ thư mục data/ (chứa cookie Zalo).

## Link
- Repo: https://github.com/vuhai2002/zalo-agent
- Release v0.4.0: https://github.com/vuhai2002/zalo-agent/releases/tag/v0.4.0
- Fork read-only: https://github.com/andyluu98/zalo-agent
- Plugin OpenClaw Zalo cá nhân: https://docs.openclaw.ai/plugins/zalouser
- Plugin Hermes Zalo: https://github.com/cuongdev/hermes-zalo-plugin
