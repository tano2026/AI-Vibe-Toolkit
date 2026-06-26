# Domain Research Playbooks — Research Pro v3

Mỗi domain có nguồn data riêng + key metrics + sample queries.
Hermes đọc file này để biết fetch gì, từ đâu, đo cái gì.

---

## ✈️ HÀNG KHÔNG & DU LỊCH

**Free data sources:**
- `searchflights` API → giá vé thực tế
- `getliveairportboard` → tình trạng sân bay
- https://www.flightradar24.com/data/statistics → load factor public
- https://www.caav.gov.vn → số liệu CAAV chính thức
- https://vietnamtourism.gov.vn → thống kê du lịch
- VnExpress Du lịch / Travel: https://vnexpress.net/du-lich
- Google News RSS: `q=hàng không Việt Nam`

**Key metrics:**
Load factor (%) | Yield (VND/RPK) | RASK | Booking window | Ancillary % | OTP %

**Sample queries Nobitano hay hỏi:**
- So sánh giá VNA vs VJ vs QH route X-Y ngày Z
- Phí đổi hoàn hãng X hạng vé Y
- Xu hướng giá vé mùa hè/tết
- Load factor thị trường nội địa

---

## 💼 SAAS & AI/TECH

**Free data sources:**
- GitHub API: `https://api.github.com/repos/{owner}/{repo}`
- HN Algolia: `https://hn.algolia.com/api/v1/search?query={q}`
- npm: `https://registry.npmjs.org/{package}`
- PyPI: `https://pypi.org/pypi/{package}/json`
- ProductHunt: scrape `https://www.producthunt.com/posts/{slug}`
- G2: scrape `https://www.g2.com/products/{slug}/reviews`
- Reddit: r/SaaS, r/startups, r/MachineLearning, r/LocalLLaMA

**Key metrics:**
Stars/week velocity | Fork ratio | Issue response time | npm weekly downloads | G2 rating | Pricing tier

---

## 🏪 FMCG, RETAIL & THƯƠNG MẠI ĐIỆN TỬ

**Free data sources:**
- GSO (Tổng cục Thống kê): https://www.gso.gov.vn/px-web-2/
- World Bank VN: `https://api.worldbank.org/v2/country/VN/indicator/NE.TRD.GNFS.ZS`
- Shopee/Lazada public category rankings (scrape)
- VnExpress Kinh doanh: https://vnexpress.net/kinh-doanh
- Google Trends (scrape public)
- Nielsen/Kantar VN: scrape public press releases

**Key metrics:**
Market share (%) | YoY growth | Channel split (MT/GT/Online) | ASP | Category penetration

---

## 💰 TÀI CHÍNH, ĐẦU TƯ & CHỨNG KHOÁN

**Free data sources:**
- CafeF.vn: https://cafef.vn/thi-truong-chung-khoan.chn (scrape)
- VNDIRECT/SSI public research: scrape PDF links
- World Bank: GDP, FDI, CPI, inflation
- Exchange rate: `https://open.er-api.com/v6/latest/USD`
- SBV (Ngân hàng Nhà nước): https://www.sbv.gov.vn/webcenter/portal/vi/menu/rm/tg
- Ministry of Finance: https://mof.gov.vn

**Key metrics:**
PE | PB | ROE | Debt/Equity | EPS growth | Sector allocation | FDI inflow

---

## 🏠 BẤT ĐỘNG SẢN

**Free data sources:**
- Batdongsan.com.vn: scrape listing data (giá/m², inventory)
- Cafeland.vn: https://cafeland.vn
- CBRE VN press releases: https://www.cbre.com/vietnam/press-releases
- Savills VN: https://www.savills.com.vn/research
- GSO housing: https://www.gso.gov.vn
- VnExpress BĐS: https://vnexpress.net/bat-dong-san

**Key metrics:**
Price/m² theo quận | Rental yield | Vacancy rate | Absorption rate | New supply | Pipeline

---

## 🍜 F&B, HOSPITALITY & DU LỊCH

**Free data sources:**
- TCDL (Vietnam Tourism): https://vietnamtourism.gov.vn/thong-ke
- TripAdvisor public: scrape review counts, ratings
- Google Maps public data
- Foody.vn: scrape (restaurant density, pricing)
- AirBnB public listings (scrape)
- STR Global VN: scrape press releases

**Key metrics:**
RevPAR | ADR | Occupancy % | Cover turn | Delivery % revenue | Tourist arrival YoY

---

## 🎓 GIÁO DỤC & EDTECH

**Free data sources:**
- MOET (Bộ GD&ĐT): https://moet.gov.vn/thong-ke
- World Bank Education: `indicator/SE.XPD.TOTL.GD.ZS`
- Coursera/Udemy public course stats (scrape)
- HolonIQ VN reports (scrape press)
- Reddit: r/edtech, r/teaching
- HN: search "edtech Vietnam"

**Key metrics:**
Enrollment rate | Completion rate | ARPU | CAC | LTV | NPS

---

## 🏥 Y TẾ & DƯỢC PHẨM

**Free data sources:**
- MOH (Bộ Y tế): https://moh.gov.vn/thong-ke-y-te
- WHO VN: https://www.who.int/vietnam
- World Bank Health: `indicator/SH.XPD.CHEX.GD.ZS`
- ClinicalTrials.gov (public)
- PubMed search (free API)

**Key metrics:**
Healthcare spending % GDP | Out-of-pocket % | Hospital beds/1000 | Insurance coverage

---

## 🌾 NÔNG NGHIỆP & THỰC PHẨM

**Free data sources:**
- MARD (Bộ NN&PTNT): https://www.mard.gov.vn/Pages/thong-ke.aspx
- FAO VN: https://www.fao.org/vietnam
- UN Comtrade (xuất nhập khẩu nông sản)
- World Bank Agriculture: `indicator/NV.AGR.TOTL.ZS`
- VASEP (thủy sản): https://vasep.com.vn/san-pham-xuat-khau

**Key metrics:**
Export value | Volume | Price index | Yield/hectare | Value chain margin

---

## 📱 DIGITAL MARKETING & SOCIAL MEDIA

**Free data sources:**
- Meta Business Insights public: https://www.facebook.com/business/insights
- TikTok Creative Center: https://ads.tiktok.com/business/creativecenter
- SimilarWeb (scrape public): https://www.similarweb.com
- Sprout Social / HootSuite public benchmarks
- We Are Social VN Digital Report (scrape)
- HN: search "social media Vietnam 2026"

**Key metrics:**
CPM | CPC | CTR | ROAS | CAC | Engagement rate | Reach/Impression ratio

---

## 🚚 LOGISTICS & SUPPLY CHAIN

**Free data sources:**
- VLA (Vietnam Logistics Association): https://vla.com.vn
- World Bank Logistics Performance Index
- VCCI: https://vcci.com.vn
- VnExpress Logistics scrape
- UN Comtrade cho trade flows

**Key metrics:**
Logistics cost % GDP | Warehouse utilization | Last-mile cost | Transit time | Fill rate

