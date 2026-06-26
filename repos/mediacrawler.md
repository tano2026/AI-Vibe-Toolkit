# MediaCrawler — GitHub Repo

## TL;DR
Crawler mạng xã hội Trung Quốc mã nguồn mở — scrape Xiaohongshu (Red Note), Douyin, Kuaishou, Bilibili, Weibo, Zhihu. 52.7K stars, 1 trong những tool scraping popular nhất GitHub. Cực thiết thực cho marketer nghiên cứu trend Trung Quốc.

## Repo này dùng để làm gì
Content creator và digital marketer VN hay theo trend Trung Quốc (XHS, Douyin) trước khi trend đó vào TikTok VN. MediaCrawler cho phép:
- Scrape posts, comments, likes từ Xiaohongshu (trend beauty, lifestyle)
- Crawl video + comments từ Douyin
- Lấy data từ Bilibili (tech, gaming content)
- Export ra CSV/JSON để phân tích
- Chạy automation search theo keyword

Hay nhất: không cần API chính thức — dùng playwright simulate real browser.

## Setup từng bước
```bash
# 1. Clone
git clone https://github.com/NanmiCoder/MediaCrawler
cd MediaCrawler

# 2. Cài Python dependencies
pip install -r requirements.txt

# 3. Cài Playwright browsers
playwright install chromium

# 4. Config platform muốn crawl
cp config/base_config.py.example config/base_config.py
# Edit: chọn platform, login cookies, output format

# 5. Chạy crawler Xiaohongshu
python main.py --platform xhs --lt qrcode --type search --keywords "skincare routine"

# 6. Crawl Douyin theo keyword
python main.py --platform douyin --lt qrcode --type search --keywords "AI tools 2026"
```

**Login bằng QR Code (lần đầu):**
- Chạy lệnh → hiện QR code trong terminal
- Quét bằng app mobile → authenticated
- Cookie tự lưu cho lần sau

**Output formats:** CSV, JSON, database SQLite

## Ví dụ thực tế
**Use case:** Research trend skincare đang hot ở XHS trước khi push content TikTok VN

```bash
python main.py --platform xhs --type search --keywords "dưỡng da tối giản" --max-count 200
```

**Output CSV:**
| post_id | title | likes | comments | shares | date | author |
|---------|-------|-------|----------|--------|------|--------|
| xxx | "3 bước skincare..." | 45K | 2.3K | 890 | 2026-06 | @beauty_user |

Phân tích 200 posts → biết ngay format nào đang viral, hashtag nào trending, pain point user hay comment nhất.

## Lưu ý / Lỗi thường gặp
- Platform detect bot và ban IP — dùng residential proxy nếu crawl nhiều
- Login session expire sau vài ngày → cần re-authenticate
- Xiaohongshu hay update anti-bot → có thể cần update code theo
- Chỉ dùng cho research cá nhân/nghiên cứu — không spam, không vi phạm ToS nặng
- Cần Python 3.10+ và Playwright mới nhất

## Đánh giá cá nhân
- Điểm mạnh: Support nhiều platform; output sạch; community active maintain; 52K stars = ổn định
- Điểm yếu: Platform hay update anti-bot (cần maintain); cần residential proxy cho crawl lớn; UI terminal only
- Có nên dùng không: **8/10** — Essential cho marketer theo trend Trung Quốc. Nếu mày làm content beauty, lifestyle, tech mà muốn bắt trend sớm — đây là tool số 1.

## Link
- Repo: https://github.com/NanmiCoder/MediaCrawler
- Docs: Xem README với hướng dẫn chi tiết từng platform
