# Public APIs — GitHub Repo

## TL;DR
Danh sach tong hop 1500+ API mien phi cho developer — 444K stars, top 5 repo GitHub moi thoi dai. Phan loai theo 90+ danh muc: AI, Finance, Weather, Music, Sports, Travel... Moi lam tinh nang moi cho app thi kiem o day truoc.

## Repo nay dung de lam gi
Thay vi Google "free API for X" va phai sap xep ket qua lung tung — Public APIs la thu vien duoc curate thu cong, kiem tra that su hoat dong:
- **1500+ API** phan loai ro rang
- **Filter:** Free / API Key / OAuth / HTTPS / CORS
- **90+ danh muc:** Animals, Anime, Art, Books, Business, Finance, Food, Games, Health, Music, News, Science, Sports, Travel, Weather...
- **Website:** publicapis.dev — UI tim kiem dep hon README

Vibe coder dung de tim API tra API key nhanh truoc khi code tinh nang moi.

## Setup tung buoc
```bash
# Khong can cai gi — dung web
# publicapis.dev hoac publicapis.io

# Hoac clone de contribute / dung offline
git clone https://github.com/public-apis/public-apis

# Tim API trong file README.md theo danh muc
# Hoac dung GitHub search: site:github.com/public-apis/public-apis "travel"
```

**API hay dung cho du an cua tao:**

Travel/Tourism (ABTRIP):
- Open-Meteo: weather forecast mien phi, khong can key
- REST Countries: thong tin quoc gia, visa, currency
- Amadeus for Developers: flight, hotel (free tier)
- Unsplash API: anh dep mien phi cho landing page

Content Factory:
- YouTube Data API: search video, analytics
- NewsAPI: tin tuc theo keyword
- Wikipedia API: lay content bai viet

## Vi du thuc te
**Tinh nang "Thoi tiet tai diem den" cho ABTRIP — 0 dong:**
```python
import requests

# Open-Meteo — hoan toan mien phi, khong can API key
resp = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 22.8402,   # Ha Giang
        "longitude": 104.9841,
        "daily": "temperature_2m_max,precipitation_sum",
        "forecast_days": 7
    }
)
weather = resp.json()
# Ra thoi tiet 7 ngay, khong ton mot dong tien
```

## Luu y / Loi thuong gap
- Mot so API da chet nhung chua duoc xoa khoi list — test truoc khi dung
- "Free" co the co rate limit nghiem ngat — doc docs ky
- CORS note quan trong neu call tu frontend (browser)
- Website publicapis.dev de dung hon README tren GitHub

## Danh gia ca nhan
- Diem manh: 444K stars = tin tuong duoc; curate tot; update thuong xuyen; website UI dep
- Diem yeu: Mot so API het hoat dong; khong co rating chat luong API; thieu API VN-specific
- Co nen dung khong: **9/10** — Bookmark ngay. Bat ky luc nao can tinh nang moi ma khong muon tu build — mo cai nay tim API truoc.

## Link
- Repo: https://github.com/public-apis/public-apis
- Website: https://publicapis.dev
- Alternative UI: https://publicapis.io
