# Twenty CRM — GitHub Repo

## TL;DR
CRM mã nguồn mở, tự host được, kiểu "Notion/Airtable gặp Salesforce": object tuỳ biến, pipeline kéo-thả, API (REST + GraphQL), workflow tự động. ~58K sao, release rất đều (v2.45.0 ngày 05/10/2026). Hợp để thay CRM tự xây tay nếu chỉ dùng nội bộ — nhưng **license không đơn giản** và **2026 có nhiều lỗ hổng bảo mật loại nặng**, nên không được ném thẳng ra internet.

## Repo này dùng để làm gì
Quản lý khách hàng/đối tác/deal: Companies, People, Opportunities, Notes, Tasks có sẵn; thêm object riêng (ví dụ Bookings, Dịch vụ sân bay) bằng giao diện, không cần code. Có API nên Hermes/OpenClaw đọc ghi được.

## Số liệu đã kiểm (07/10/2026)
- Repo: `twentyhq/twenty` — 57.968 sao, push gần nhất 06/10/2026, release mới nhất `twenty/v2.45.0` (05/10/2026)
- GitHub hiển thị license là `NOASSERTION` — đúng, vì repo trộn nhiều license (xem dưới)

## ⚠️ License — đọc kỹ trước khi dùng cho việc nào ngoài nội bộ
File LICENSE của repo chia 3 phần:
1. **AGPLv3** — phần lớn code.
2. **Enterprise (thương mại)** — các file có dòng `/* @license Enterprise */`. Đếm được 477 file, tập trung ở billing (36), usage (20), SSO (12), record-share (7), settings/security (5), event-logs, auth, jwt... Muốn dùng nhóm tính năng này phải mua license thương mại của Twenty.
3. **MIT** — một số package: `twenty-sdk`, `twenty-client-sdk`, `create-twenty-app`, `twenty-shared`, `twenty-ui`, `twenty-apps`.

Hệ quả thực tế:
- **Dùng nội bộ ABTRIP** (chỉ nhân viên truy cập) → AGPL không buộc phải công khai code. Đây là cách hiểu phổ biến của AGPL (nghĩa vụ mở nguồn kích hoạt khi người NGOÀI công ty dùng qua mạng). Tao không phải luật sư — cần xác nhận lại nếu tính bán.
- **Bán/cho khách dùng như dịch vụ** (ví dụ gói TanoOS có Twenty bên trong, khách đăng nhập vào) → rơi vào vùng AGPL kích hoạt + Enterprise. Phải hỏi luật sư hoặc Twenty trước, không tự suy diễn.
- Phần "Twenty Application Exception" (ngoại lệ AGPL §7 cho app mở rộng) tao CHƯA đọc hết — chưa kết luận gì về nó.

## ⚠️ Bảo mật — sự thật cần nhớ trước khi self-host
Phân biệt 2 nhóm, vì trước đây tao từng gộp nhầm:

**A. CVE của thư viện axios (không phải lỗi riêng của Twenty):** CVE-2026-44492 (NO_PROXY bị qua mặt bằng IPv4-mapped IPv6 → SSRF, CVSS 8.6), CVE-2026-44494, CVE-2026-44495. Vá ở axios ≥ 1.16.0 (44495 vá từ ≥ 1.15.2). `twenty-server` trên nhánh main đã ghim `axios ^1.16.0` → bản mới đã vá. Bản cũ thì chưa chắc.

**B. Lỗ hổng riêng của Twenty (2026):** theo trang tổng hợp cve.imfht.com (chưa đối chiếu NVD) có 11 CVE, gồm: command execution 9.9 (CVE-2026-46624, 26/5), SQL injection 9.1 (CVE-2026-73069, 11/8), SSRF 9.1 (CVE-2026-33975), XSS 8.7 (CVE-2026-44729), RCE qua `local-driver.ts` (CVE-2026-26720), SSRF 5.0 (CVE-2026-27023), bypass đọc theo field 7.1 (22/9), và **lộ mật khẩu qua GraphQL 9.6 (CVE-2026-105763, 05/10/2026 — mới 2 ngày)**. Trang GitHub Security Advisories của repo cũng liệt kê SQLi (bản ≤ 1.16.7), XSS, SSRF bypass, IDOR chéo workspace. Chưa xác nhận được bản vá cụ thể cho từng lỗi từ nguồn nào.

**Quy tắc cho ABTRIP (dữ liệu khách + PNR là dữ liệu thật):**
- Luôn dùng bản release mới nhất, đọc GitHub Security Advisories TRƯỚC khi deploy và định kỳ sau đó
- KHÔNG mở cổng ra internet công khai — đặt sau VPN/Tailscale hoặc whitelist IP văn phòng
- Không lưu số hộ chiếu/thẻ thanh toán trong CRM; PNR thì chỉ lưu mã, không lưu nội dung SR DOCS
- API key tạo riêng cho từng agent, quyền tối thiểu

## Setup từng bước (self-host, Docker)
```bash
# Theo docs chính thức twenty.com/developers (kiểm lại lệnh mới nhất trước khi chạy)
git clone --depth 1 https://github.com/twentyhq/twenty
cd twenty/packages/twenty-docker
cp .env.example .env     # đặt APP_SECRET + mật khẩu Postgres mạnh, ngẫu nhiên
docker compose up -d
# mở http://localhost:3000, tạo workspace đầu tiên
```
Cần: Docker, ~2GB RAM trống trở lên, domain/HTTPS nếu truy cập từ ngoài văn phòng (qua VPN).

## Ví dụ thực tế (use case ABTRIP)
- Companies: PVN và các cơ quan đặt vé số lượng lớn; People: đầu mối liên hệ
- Opportunity: "Gia hạn phụ lục hợp đồng PVN" chạy qua stage Tiếp cận → Báo giá → Đàm phán hợp đồng → Ký/Gia hạn → Đang phục vụ
- Object riêng: Bookings (PNR, hành trình, ngày xuất vé), Dịch vụ Fast Track/Meet & Assist
- Chi tiết thiết kế: `stacks/twenty-crm-abtrip-internal.md`

## Lưu ý / Lỗi thường gặp
- **Chưa chạy thử thật** — toàn bộ nội dung trên là từ nghiên cứu, 0 lần cài. Không coi là đã verify
- Object/field tuỳ biến dễ làm rối nếu thiết kế vội — chốt schema trên giấy trước
- Bản self-host tự lo backup Postgres, tự lo cập nhật bản vá (xem mục bảo mật)
- Đang có CRM tự xây tay (ABTrip CRM, 9 module) — chạy song song 2 hệ thống sẽ phân mảnh dữ liệu; phải quyết 1 trong 2

## Đánh giá cá nhân
- Điểm mạnh: giao diện hiện đại, tuỳ biến object không cần code, API đầy đủ, cộng đồng và nhịp release dày
- Điểm yếu: license trộn (AGPL + Enterprise + MIT) làm khó việc đóng gói bán lại; lỗ hổng bảo mật 2026 nhiều và nặng → tự host phải kỷ luật cập nhật; chưa kiểm hỗ trợ tiếng Việt/định dạng tiền VND/ngày dd/mm
- Có nên dùng: 7/10 cho nội bộ ABTRIP (đặt sau VPN). Với TanoOS bán cho khách: chưa nên, đến khi có ý kiến pháp lý về license

## Link
- Repo: https://github.com/twentyhq/twenty
- Security advisories: https://github.com/twentyhq/twenty/security/advisories
- Axios issue tham chiếu: twentyhq/twenty#21071
- Liên quan: `stacks/twenty-crm-abtrip-internal.md`, `repos/microsoft-presidio.md` (nếu đưa dữ liệu khách qua log/LLM)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# REST API của Twenty — đổi HOST và API key (tạo trong Settings → APIs & Webhooks).
# Kiểm lại đường dẫn endpoint trong docs bản đang chạy trước khi dùng.
import urllib.request, json

HOST = "https://crm.noi-bo.abtrip.example"   # sau VPN
KEY = "[TWENTY_API_KEY]"                      # lấy từ biến môi trường, không ghi vào file

def twenty_get(path):
    req = urllib.request.Request(
        f"{HOST}/rest/{path}",
        headers={"Authorization": f"Bearer {KEY}"})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

# vd: danh sách People
print(twenty_get("people?limit=5"))
```

### OpenClaw
```bash
# Dùng qua HTTP/webhook của Twenty hoặc MCP của nó nếu bản đang chạy có bật
# (chưa kiểm tra MCP của Twenty trong đợt research này).
```

### Antigravity
```bash
# Deploy: docker compose như mục Setup; đặt sau VPN/Tailscale, KHÔNG publish cổng ra internet.
# Backup: pg_dump hằng ngày ra ổ khác.
```
> ⚠️ Chỉ dùng nội bộ. Chưa kiểm chứng chạy thật. Đọc mục Bảo mật trước khi bật.
