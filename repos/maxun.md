# Maxun — GitHub Repo

## TL;DR
No-code web scraping platform mã nguồn mở — record thao tác trên browser, nó tự tạo robot scrape. 16K stars. Không cần biết code để scrape bất kỳ website nào.

## Repo này dùng để làm gì
Thay vì viết Playwright/Puppeteer script phức tạp, Maxun cho mày:
- **Record mode:** Mày click trên web → nó học và tạo robot
- **No-code:** Chọn element muốn extract bằng cách click, không viết CSS selector
- **Schedule:** Đặt lịch chạy tự động
- **API:** Output qua REST API hoặc webhook
- **AI-powered:** Dùng AI để handle dynamic page, pagination tự động

Use case: Scrape giá sản phẩm, theo dõi competitor, collect data thị trường, extract lead từ directory.

## Setup từng bước
```bash
# Clone và chạy với Docker Compose
git clone https://github.com/getmaxun/maxun
cd maxun

# Config environment
cp .env.example .env
# Edit .env: thêm DB connection, API keys

docker-compose up -d

# Truy cập: http://localhost:3000

# Tạo robot đầu tiên:
# 1. Click "New Robot"
# 2. Nhập URL muốn scrape
# 3. Click vào elements muốn extract
# 4. Save → chạy ngay hoặc schedule
```

## Ví dụ thực tế
**Track giá tour competitor cho ABTRIP:**
1. Mở Maxun → New Robot → nhập URL trang tour competitor
2. Click vào tên tour, giá, ngày khởi hành
3. Maxun học pattern → tự extract tất cả
4. Schedule chạy hàng ngày 7am → export CSV
5. Google Sheets nhận data → so sánh giá tự động

Không viết một dòng code.

## Lưu ý / Lỗi thường gặp
- Site có Cloudflare/anti-bot mạnh → cần residential proxy
- Login-required pages: Maxun hỗ trợ nhưng phức tạp hơn
- JavaScript-heavy site (SPA) đôi khi record không chính xác — cần test kỹ
- Còn đang active development — một số feature beta

## Đánh giá cá nhân
- Điểm mạnh: No-code thật sự; record UX trực quan; schedule + API out of the box; mã nguồn mở
- Điểm yếu: Còn non so với Apify hay Bright Data; community nhỏ hơn; anti-bot chưa xử lý tốt
- Có nên dùng không: **7.5/10** — Tốt nhất cho non-technical user muốn scrape mà không code. Developer thì dùng Crawl4AI (đã có trong kho) mạnh hơn.

## Link
- Repo: https://github.com/getmaxun/maxun
- Docs: https://docs.maxun.dev
