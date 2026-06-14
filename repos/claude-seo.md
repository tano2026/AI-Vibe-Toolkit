# claude-seo — Plugin Biến Claude Code Thành Đội Audit SEO 18 Chuyên Gia

**GitHub:** https://github.com/AgriciDaniel/claude-seo
**Stars:** 8.8k⭐ | **Forks:** 1.3k | **License:** MIT
**Tác giả:** AgriciDaniel | **Tạo:** 02/2026 | **Version:** v2+
**Website:** claude-seo.md

---

## Đây Là Gì

Plugin open-source cho **Claude Code** — biến Claude thành một đội audit SEO chạy song song.

Cài 2 lệnh → gõ `/seo audit https://site-của-mày.com` → **18 agent chuyên gia chạy đồng thời**, quét toàn bộ website, cho ra action plan ưu tiên trong vài phút.

Không phải dashboard đầy số. Không phải report PDF vô nghĩa. **Mỗi khuyến nghị đều có: lý do tại sao, dependency, và cách kiểm tra xem fix có hiệu quả không.**

---

## 25 Lệnh `/seo` — Làm Được Gì

| Lệnh | Làm gì |
|------|--------|
| `/seo audit <url>` | Full audit toàn site — 18 agent chạy song song |
| `/seo page <url>` | Phân tích sâu 1 trang cụ thể |
| `/seo technical <url>` | Technical SEO — 9 category (speed, crawl, indexing...) |
| `/seo content <url>` | Đánh giá E-E-A-T + chất lượng nội dung |
| `/seo content-brief <topic>` | Viết content brief: từ khóa mục tiêu, outline, internal links |
| `/seo schema <url>` | Detect, validate, generate Schema.org markup |
| `/seo geo <url>` | Tối ưu cho AI Overviews / GEO (xuất hiện trong ChatGPT, Gemini) |
| `/seo local <url>` | Local SEO: Google Business Profile, citations, map pack |
| `/seo maps [command]` | Geo-grid analysis, GBP audit, competitor maps |
| `/seo backlinks <url>` | Phân tích backlink profile (Moz, Bing, Common Crawl) |
| `/seo cluster <keyword>` | Semantic clustering từ SERP thật |
| `/seo google [command]` | Kết nối GSC, PageSpeed, CrUX, GA4, xuất PDF report |
| `/seo ecommerce <url>` | SEO cho e-commerce + marketplace intelligence |
| `/seo competitor-pages <url>` | Tạo trang so sánh với đối thủ |
| `/seo hreflang <url>` | SEO đa ngôn ngữ / quốc tế |
| `/seo drift baseline/compare <url>` | Theo dõi SEO drift qua thời gian (SQLite snapshots) |
| `/seo plan <type>` | Kế hoạch SEO theo loại: saas / local / ecommerce / publisher / agency |
| `/seo programmatic <url>` | Lên kế hoạch programmatic SEO |
| `/seo images <url>` | Tối ưu hình ảnh |
| `/seo sitemap <url/generate>` | Phân tích hoặc tạo XML sitemap |
| `/seo sxo <url>` | Search Experience Optimization — user stories, personas |
| `/seo firecrawl <url>` | Full-site crawling (cần extension Firecrawl) |
| `/seo dataforseo` | Live SEO data (cần extension DataForSEO) |
| `/seo image-gen` | Tạo ảnh SEO assets bằng AI (extension) |
| `/seo flow [stage]` | Framework FLOW — evidence-led workflow |

---

## Tại Sao Khác Tool SEO Bình Thường

**Tool SEO bình thường:** cho mày dashboard → mày tự đọc → mày tự hiểu → mày tự quyết.

**Claude SEO:** 18 agent phân tích song song → tổng hợp → ưu tiên → giải thích lý do → nói rõ cách kiểm tra fix có work không.

3 điểm khác biệt cốt lõi:

**1. AI-search first** — Align theo Google AI Optimization Guide. Check citability cho AI Overviews, llms.txt, IPTC metadata cho ảnh AI-generated. Tool SEO truyền thống chưa có cái này.

**2. Parallel execution** — Full site audit spawn tới 15 agent cùng lúc. Audit xong trong **vài phút thay vì vài giờ**.

**3. Falsifiable** — Mỗi khuyến nghị có: observation cơ sở + dependency relationships + "làm sao biết fix này fail?" + leading indicator để track. Không phải recommendation mơ hồ kiểu "improve your content quality."

---

## Core Web Vitals Check

Claude SEO đo đúng 3 CWV hiện tại (đã update INP thay FID từ 3/2024):
- **LCP** < 2.5s (Largest Contentful Paint)
- **INP** < 200ms (Interaction to Next Paint — thay FID)
- **CLS** < 0.1 (Cumulative Layout Shift)

Field data từ CrUX API, lab data fallback Lighthouse. Mobile + desktop đo riêng. CrUX History 25 tuần included trong tier free.

---

## E-E-A-T Assessment

Đánh giá theo Search Quality Rater Guidelines (update 9/2025):
- **Experience:** Original research, case study, first-hand photos
- **Expertise:** Author credentials, topical depth
- **Authoritativeness:** External citations, brand mentions
- **Trustworthiness** (quan trọng nhất): HTTPS, contact info, date stamps, correction policy

---

## Cài Đặt — 2 Lệnh

```bash
# Cần Claude Code 1.0.33+
# Trong Claude Code, gõ:

/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
```

**Hoặc manual (nếu thích):**
```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

---

## Quick Start

```bash
# Mở Claude Code
claude

# Full audit toàn site
/seo audit https://your-site.com

# Phân tích 1 trang
/seo page https://your-site.com/blog/bai-viet

# Check AI search readiness
/seo geo https://your-site.com

# Schema audit
/seo schema https://your-site.com
```

---

## Extensions (Tùy chọn, Tăng Power)

| Extension | Thêm gì |
|-----------|---------|
| **DataForSEO** | Live SERP data, keyword volume, backlink data thật |
| **Firecrawl** | Full-site crawling sâu hơn |
| **Banana** (image-gen) | Tạo ảnh SEO assets bằng AI |

Base plugin hoạt động free không cần extension — extension chỉ cần khi muốn data live thật.

---

## Ai Nên Dùng

- **SEO agency** chạy 5+ client site → thay quarterly audit bằng weekly automated run, cùng team, 4× cadence
- **In-house SEO** tại SaaS/publisher/ecommerce → second pair of eyes trước executive review
- **Freelance SEO** → audit 15 phút, ra score 0-100, close client trước khi viết proposal
- **Vibe coders** → không cần hiểu SEO sâu, gõ 1 lệnh, đọc action plan, làm theo

---

## Kết Quả Thực Tế

Repo có ảnh Google Search Console của một site mới tạo 23/3/2026, chạy workflow này 3 tháng liên tục → organic traffic tăng steady từ launch đến 6/2026.

---

## Đánh Giá Cá Nhân

8.8k stars trong 4 tháng (tạo 2/2026) — cực nhanh cho một tool SEO chuyên biệt. Có thể thấy repo này đang bùng nổ trong cộng đồng Claude Code.

Điểm tao thấy game-changing nhất: **GEO command** — tối ưu cho AI Overviews và xuất hiện trong ChatGPT/Gemini. Đây là thứ Ahrefs và Semrush chưa có proper workflow. Và cái này nằm trong plugin free MIT.

Điểm trừ: Cần Claude Code — không chạy standalone, không dùng được nếu mày không có Claude Code setup. Và một số commands advanced cần API key DataForSEO (trả phí).

Nhưng nhìn chung: nếu mày đang làm SEO và dùng Claude Code → đây là plugin phải cài ngay. Không bàn.

**Rating: 9/10** — Best SEO tool trong Claude ecosystem hiện tại.

---

*Nguồn: github.com/AgriciDaniel/claude-seo*
*Stars: 8.8k⭐ (tháng 6/2026) | MIT License*
*Cập nhật: tháng 6/2026*
