# Ever Gauzy — GitHub Repo

## TL;DR
Nền tảng quản lý doanh nghiệp mã nguồn mở (ERP/CRM/HRM/ATS/PM) all-in-one của Ever Co. — 4.4k star, tự host được hoàn toàn, gộp luôn cả chấm công/time-tracking kiểu Upwork/Hubstaff vào cùng 1 hệ thống.

## Repo này dùng để làm gì
Ever Gauzy giống như gộp chung QuickBooks + HubSpot CRM + BambooHR + Toggl time-tracking + Trello vào 1 nền tảng duy nhất, tự host trên server của mình chứ không phải SaaS trả phí tháng. Có sẵn: quản lý nhân sự, chấm công/theo dõi hoạt động màn hình nhân viên (giống Hubstaff), pipeline bán hàng, kế toán/hoá đơn, quản lý dự án, tuyển dụng (ATS), quản lý kho/tồn kho. Có cả app Desktop Timer riêng để nhân viên chấm công kèm chụp màn hình.

## Setup từng bước
1. Cách nhanh nhất để thử — dùng bản demo online có sẵn, không cần cài gì: https://demo.gauzy.co (đăng nhập `admin@ever.co` / mật khẩu `admin`)
2. Muốn tự host — clone repo, cần Docker Compose bản >= v2.20:
   ```bash
   git clone https://github.com/ever-co/ever-gauzy.git
   cd ever-gauzy
   docker-compose -f docker-compose.demo.yml up
   ```
3. Mở `http://localhost:4200`, đăng nhập `admin@ever.co` / `admin` (super admin) hoặc `employee@ever.co` / `12345678` (nhân viên, để test chấm công).
4. Muốn build thủ công từ source (không qua Docker): cần Node.js LTS 22.x/24.x + Yarn 1.22.x:
   ```bash
   yarn bootstrap
   yarn start
   ```
5. Chạy production thật — **bắt buộc** sửa file `.env.compose`, đổi 4 secret (`JWT_SECRET`, `JWT_REFRESH_TOKEN_SECRET`, `JWT_VERIFICATION_TOKEN_SECRET`, `EXPRESS_SESSION_SECRET`) sang giá trị ngẫu nhiên mạnh (`openssl rand -hex 64`) — API sẽ từ chối khởi động nếu để mặc định, vì bất kỳ ai cũng giả mạo được token đăng nhập nếu dùng secret mẫu.

## Ví dụ thực tế
Nếu dùng cho **Wonder Mart** hay **Tano Cafe**: dựng 1 instance riêng để quản lý ca làm + chấm công nhân viên bán hàng (qua Desktop Timer, có chụp màn hình xác nhận đang làm việc), kèm module quản lý tồn kho (Inventory) và kế toán/hoá đơn (Accounting/Invoicing) — thay vì phải mua rời từng phần mềm chấm công + kế toán + quản lý kho như hiện tại.

## Lưu ý / Lỗi thường gặp
- License **không hề đơn giản**: mặc định repo dùng "Community Edition License" (không phải MIT/AGPL thuần tuý cho mọi tính năng) — có 3 tier license riêng (Community / Small Business / Enterprise), một số tính năng nâng cao chỉ mở khi có license Enterprise/Small Business trả phí. Đọc kỹ `LICENSE.md` trước khi dùng thương mại.
- Bản SaaS chính chủ `app.gauzy.co` đang ở **Alpha/testing** — Anthropic/Ever Co. tự cảnh báo "dùng cẩn thận", không nên đẩy dữ liệu thật vào bản SaaS này.
- Stack khá nặng: Angular + NestJS + Nx monorepo + TypeORM/MikroORM, kèm hạ tầng đi cùng khi chạy production đầy đủ (PostgreSQL, Redis, OpenSearch, MinIO, Jitsu, Cube, Zipkin...) — không phải kiểu "1 file docker-compose nhẹ nhàng", cần server đủ mạnh nếu bật hết.
- Build từ source lần đầu (`docker-compose.build.yml`) rất lâu vì build lại toàn bộ platform tại chỗ — nên ưu tiên bản demo/prebuilt image nếu chỉ cần thử nhanh.

## Đánh giá cá nhân
- **Điểm mạnh:** Hiếm có tool mã nguồn mở nào gộp đủ ERP+CRM+HRM+time-tracking+ATS trong 1 hệ thống mà vẫn tự host được — tiết kiệm đáng kể so với mua rời nhiều SaaS. Cộng đồng khá lớn (4.4k star, 878 fork, 27k+ commit), cập nhật đều tay.
- **Điểm yếu:** License phân tầng phức tạp dễ gây nhầm "mã nguồn mở = free hoàn toàn" trong khi 1 số tính năng cần trả phí license. Stack nặng, không hợp để "cài thử cho vui" trên máy yếu — cần đầu tư hạ tầng nếu muốn chạy production thật. Tài liệu chính thức (`docs.gauzy.co`) vẫn đang WIP theo README.
- **Có nên dùng không:** 6/10 cho việc dùng ngay lập tức — rất đáng thử bản demo trước để đánh giá UI/UX có hợp quy trình ABTRIP/Wonder Mart không, nhưng đừng vội tự host production khi chưa đọc kỹ license và tính toán hạ tầng cần thiết.

## Link
- Repo: https://github.com/ever-co/ever-gauzy
- Docs/Demo: https://demo.gauzy.co · https://docs.gauzy.co · https://gauzy.co

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

# Ever Gauzy expose Headless API (REST) tại https://api.gauzy.co/docs khi dùng bản SaaS,
# hoặc http://127.0.0.1:3000/api khi tự host. Cần login lấy JWT token trước.
API_BASE = "http://127.0.0.1:3000/api"  # đổi sang domain tự host thật

def gauzy_login(email, password):
    req = urllib.request.Request(
        f"{API_BASE}/auth/login",
        data=json.dumps({"email": email, "password": password}).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    return json.loads(urllib.request.urlopen(req).read())  # trả về access token
```
> ⚠️ Chỉ dùng được sau khi đã tự host (hoặc có tài khoản SaaS Alpha). Đọc kỹ tài liệu API ở `/docs` của chính instance đang chạy vì endpoint có thể đổi theo version.

### OpenClaw
Không áp dụng trực tiếp — nếu cần đồng bộ dữ liệu (vd đẩy giờ công nhân viên vào Gauzy), gọi qua REST API ở trên bằng HTTP request thường trong Node.js, không có MCP/connector sẵn cho tool này.

### Antigravity
```bash
# Deploy nhanh bằng Docker Compose (bản demo, dùng prebuilt image)
git clone https://github.com/ever-co/ever-gauzy.git
cd ever-gauzy
docker-compose -f docker-compose.demo.yml up -d
```
> ⚠️ Trước khi deploy production thật, bắt buộc sửa `.env.compose`: đổi 4 secret (JWT_SECRET, JWT_REFRESH_TOKEN_SECRET, JWT_VERIFICATION_TOKEN_SECRET, EXPRESS_SESSION_SECRET) sang giá trị ngẫu nhiên mạnh — API tự chối khởi động nếu để mặc định.
