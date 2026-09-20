# gpt-crawler — GitHub Repo

## TL;DR
Crawl nguyên 1 website thành file kiến thức sạch cho agent — nhập 1 URL, ra data sẵn sàng cho AI. 22,4k sao, 2,4k fork.

## Repo này dùng để làm gì
Nhập URL gốc, crawler tự động bóc toàn bộ nội dung site (theo link nội bộ) thành 1 file JSON/text sạch — bỏ menu/quảng cáo/noise, chỉ giữ nội dung chính. Dùng làm nguồn cho RAG/agent tra cứu mà không phải tự viết scraper riêng.

## Setup từng bước
1. Clone: `git clone https://github.com/BuilderIO/gpt-crawler`
2. `npm install`
3. Cấu hình `config.ts`: URL gốc, selector nội dung cần lấy, độ sâu crawl
4. Chạy: `npm start` — output ra file `output.json`

## Ví dụ thực tế
Research Pro cần audit toàn bộ trang giá dịch vụ của đối thủ (VISANA, Hong Ngọc Hà...) — thay vì tự fetch từng trang, dùng gpt-crawler nhập URL gốc, crawl hết các trang con (giá, dịch vụ, giới thiệu), ra 1 file sạch để research-synthesis xử lý luôn.

## Lưu ý / Lỗi thường gặp
- Cần cấu hình selector đúng mới lọc sạch nội dung — mặc định có thể lẫn noise nếu site có cấu trúc lạ
- Crawl sâu (nhiều trang) tốn thời gian và có thể bị site chặn nếu không giới hạn tốc độ request
- Không thay thế được Firecrawl/Brave Search đã có trong Capability Map Research Pro — đây là lựa chọn khi cần crawl TOÀN BỘ 1 site cụ thể, không phải search chung

## Đánh giá cá nhân
- Điểm mạnh: đơn giản, hiệu quả cho việc crawl toàn site cụ thể, output sạch sẵn dùng cho RAG
- Điểm yếu: cần cấu hình thủ công selector, không thông minh tự nhận diện nội dung chính như 1 số tool trả phí
- Có nên dùng: 7/10 — hữu ích khi cần audit toàn bộ 1 website đối thủ cụ thể, không cần cho search chung chung

## Link
- Repo: https://github.com/BuilderIO/gpt-crawler
