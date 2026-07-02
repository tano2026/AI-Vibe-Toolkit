---
name: competitor-research
description: >
  Market research methodology: research competitors in parallel with DDGS
  multi-query or profile customer segments by nationality/region. Validate
  shortlisted players via browser deep-dive and output structured comparison
  (feature matrix, pricing, UX patterns) or customer segment profile
  (spending, behavior, product fit). Use when user asks: "nghiên cứu X thằng",
  "compare [industry] providers", "top [product] trên thế giới",
  "ai là đối thủ chính", "thị trường [domain]", or needs customer segment
  profiling. Not for single-website analysis (use web-search + browser_navigate directly).
---

# Competitor Research

## Overview

Multi-stage competitor research workflow optimized for token cost. Combines
broad parallel search (DDGS via execute_code) with targeted browser deep-dives
on shortlisted players.

**Token cost:** ~500-1,500 tokens for search phase (DDGS in execute_code),
~2,000-8,000 tokens for browser phase (2-3 competitors).

## Workflow

### Phase 1: Parallel DDGS Multi-Query (execute_code)

Run 4-6 queries covering different angles simultaneously via `execute_code`
with `ddgs`. This is **10-20x cheaper** than sequential browser navigation.

```python
from ddgs import DDGS

searches = {
    "vn_players": "sim du lịch Việt Nam uy tín nhất 2025 2026",
    "competitor_A": "gigago.vn sim du lịch eSIM đánh giá",
    "global_overview": "best travel eSIM 2025 2026 comparison",
    "global_pricing": "airalo holafly nomad saily pricing comparison",
    "competitor_X_business": "gigago.com business model how it works",
}

results = {}
with DDGS() as ddgs:
    for key, query in searches.items():
        res = list(ddgs.text(query, max_results=5, region='wt-wt'))
        results[key] = res
```

**Query strategy per search:**
- **Market overview:** "top [product] [country/region] [year]" or "thị trường [domain] [year]"
- **Specific competitor A:** "[name] [product] đánh giá" or "[name].com [product]"
- **Global landscape:** "best [product] 2025 2026 comparison review"
- **Pricing / business model:** "[competitor] pricing OR business model OR how it works"
- **Business model deep-dive:** "[competitor] partnership OR CTV OR reseller program"

### Phase 2: Shortlist & Browser Deep-Dive

From search results, pick the **top 2-3 players** and validate each via
`browser_navigate` on their actual sites. Focus on:

1. **Homepage UX:** Search bar? Country cards? Hero section?
2. **Product page:** How do they display plans? (price, GB, days, network)
3. **Checkout flow:** What happens after you click "buy"?
4. **Partner/CTV program:** Any referral or reseller program?
5. **Pricing range:** From → To price for a typical destination

For each competitor, open 2 pages:
```python
# Homepage for UX overview
browser_navigate("https://competitor.com/")
# Product page for a specific country
browser_navigate("https://competitor.com/vietnam-esim")
```

### Phase 3: Structured Comparison

Output format — **direct, no fluff**:

```markdown
## 🏠 Thị trường VN — Top X

**1. [Name]** — [Position/tagline]
- UX: [Search box + country grid / other pattern]
- Price: từ [min]đ đến [max]đ
- Differentiator: [what makes them stand out]
- Partner program: [Yes/No with link]

## 🌍 Thế giới — Top X

**1. [Name]** — [Tagline (e.g. "Kẻ dẫn đầu 20M+ users")]
- Price: $[min] → $[max]
- Model: [per-GB / unlimited / daily-cap]
- UX: [search → choose plan → checkout]
- Partner: [Yes/No]

## 🔑 Feature Matrix

| Factor | Player A | Player B |
|--------|----------|----------|
| Search + country cards | ✅ | ✅ |
| Plan selector (GB/ngày) | ✅ | ✅ |
| Partner/CTV program | ✅ | ✅ |
| Giá từ ($) | 4 | 5 |

*Note: Telegram has NO table syntax — use bullet lists or labeled key:value pairs instead.*
```

### Phase 4: Insight & Recommendation

End with **1-2 sentence actionable insight** — what the user's opportunity is
based on the research. E.g.:

> **Cái thiếu của VN là chưa thằng nào có CTV program tử tế + API tự động hoá cho reseller — đó là chỗ [user's product] ăn được.**

## Pitfalls

1. **Don't over-browser.** 2-3 deep-dives max per session. 4+ = context bloat.
2. **DDGS first, browser second.** Never open a browser before you know which players to shortlist.
3. **Watch for DDGS 0 results.** The old `duckduckgo-search` package returns nothing. Use `ddgs` only (`pip install ddgs`).
4. **Gigago vs Gigasim.** User may say "gigasim" but mean Gigago. Clarify or search both.
5. **No table syntax on Telegram.** Use bullet lists or `| key | value |` in code blocks for the user.
6. **Pricing varies by destination.** Always mention which country the sample price is for (e.g. "for Vietnam").

## YouTube/TikTok Content Creator Analysis

### When to use

User asks to research kênh YouTube/TikTok để tham khảo format, học hỏi cấu trúc nội dung, tìm đối thủ trong lĩnh vực content sáng tạo. Đặc biệt hữu ích khi xây dựng kênh face-hidden, tâm lý học/triết lý/huyền học.

### Workflow

#### Phase 1: Multi-Query Discovery (web_search)

Run 8-15 queries covering different angles. Use **both English and Vietnamese** queries:

```python
queries_en = [
    '"face hidden" psychology philosophy YouTube channel',
    '"dark psychology" YouTube channel face not shown',
    '"stoicism" "animation" YouTube channel face hidden',
    '"life philosophy" YouTube channel voice only',
    'Vietnamese psychology YouTube channel "không lộ mặt"',
    'Chinese philosophy applied daily life YouTube',
    '"learn from" ancient wisdom modern life YouTube channel',
    '"tâm lý học" YouTube Việt Nam face hidden channels',
]
```

**Query strategy by niche:**
- Tâm lý đen / Dark Psychology → `"dark psychology" YouTube face hidden`, `"Machiavellian" philosophy channel`
- Triết lý cổ nhân → `"cổ nhân dạy" YouTube`, `"triết lý cuộc sống" YouTube`, `"lời dạy" kênh YouTube`
- Stoicism phương Đông → `"khắc kỷ" YouTube`, `stoicism Vietnamese channel`
- Tâm lý ứng dụng → `"tâm lý học ứng dụng" TikTok`, `psychology fact TikTok face hidden`
- Quốc tế storytelling → `"philosophy storytelling" YouTube`, `"academy of ideas" similar channels`
- Tử vi / huyền học → `"tử vi" YouTube channel faces`, `Vietnamese astrology YouTube`

#### Phase 2: Direct YouTube About Page Validation (browser_navigate)

For each promising channel found, validate via YouTube About page:

```
browser_navigate("https://www.youtube.com/@ChannelHandle/about")
```

From the about page extract:
- Exact subscriber count
- Video count
- Channel description (their positioning)
- Links section (other platforms, monetization)

#### Phase 3: Structured Analysis Per Channel

For each channel, analyze these dimensions:

| Dimension | What to Look For |
|-----------|-----------------|
| **Sub count** | Growth stage (new <10K, medium 10-100K, established >100K) |
| **Format** | Video length (short 3-8min, medium 10-20min, long 30+min) |
| **Visual style** | Stock footage, animation, AI art, text overlay, talking head |
| **Voice** | Human male/female, AI TTS, tone (warm/academic/dark) |
| **Face hidden?** | Yes (100% no face), Limited (hands/environment only), No |
| **Hook style** | Question, statement, story, quote |
| **Thumbnail style** | Dark/mysterious, bright/simple, text-heavy |
| **Publishing frequency** | Daily, 2-3/week, weekly, monthly |
| **Content depth** | Surface (tâm lý phổ thông), Medium (có phân tích), Deep (học thuật) |
| **Monetization** | Ads, sponsors, merch, books, courses, membership |

#### Phase 4: Comparison & Recommendation

Output format — compact markdown file saved to project's `drafts/research/`:

```markdown
# Nghiên cứu Kênh Tham Khảo — [Dự án]

## Danh sách kênh

### 1. [Tên Kênh] (Platform) — ★ [Label]
| Mục | Chi tiết |
|-----|---------|
| **URL** | https://youtube.com/@... |
| **Sub** | ~X subscribers, Y videos |
| **Chủ đề** | Topic 1, Topic 2, Topic 3 |
| **Format** | Format description |
| **Tần suất** | ~X video/tuần |
| **Điểm mạnh** | Bullet list |
| **Điểm yếu** | Bullet list |
| **Đáng học** | What to copy |
| **Nên tránh** | What NOT to copy |

### 2. ... (repeat for 5-11 channels)

## 📊 Bảng So Sánh Tổng Quan
| # | Tên | Platform | Sub | Ngôn ngữ | Face-hidden | Chủ đề | Format dài |

## 🎯 Khuyến nghị
### Kênh nên học hỏi nhiều nhất (theo mức độ phù hợp):
1. **Kênh A** — Reason
2. **Kênh B** — Reason

### Điểm khác biệt dự án nên có:
| Yếu tố | Đối thủ thiếu | Dự án nên làm |
|--------|--------------|--------------|

### Cấu trúc video đề xuất:
- **Hook**: Câu hỏi / statement gây tò mò
- **Story**: Câu chuyện lịch sử / tình huống
- **Phân tích**: Từ tâm lý học / Kinh Dịch / 36 kế
- **Ứng dụng**: Làm thế nào trong cuộc sống hiện đại
- **Kết luận**: Lời dạy

### Tần suất đề xuất:
- **YouTube**: 2 video/tuần (1 ngắn 8-12 phút, 1 dài 20-30 phút)
- **TikTok**: 1 Short/ngày (30-60s, trích từ video dài)
- **Podcast**: 1/tuần (audio full video dài)
```

#### Phase 5: Copy to VPS workspace

```bash
scp /c/Users/Nguyen\ Ngoc\ Tan/research_*.md hermes@<vps_ip>:/tmp/
ssh hermes@<vps_ip> "sudo cp /tmp/research_*.md /home/ubuntu/workspace/<project>/drafts/research/ && sudo chown ubuntu:ubuntu ..."
```

### Pitfalls

1. **The Hidden Path không tìm thấy** — Có thể kênh đã đổi tên, bị xóa, hoặc tồn tại dưới handle khác. Đừng khẳng định chắc chắn.
2. **Sub counts thay đổi theo thời gian** — Luôn confirm từ YouTube About page, ko dùng search result description.
3. **Phân biệt kênh dùng AI TTS vs giọng người thật** — AI voice thường đều đều, thiếu cảm xúc, nghe metallic. Ghi chú rõ nếu nghi ngờ.
4. **Kênh Việt thường chất lượng sản xuất thấp** — Đừng khuyên copy họ; khuyên *làm khác họ*.
5. **Kênh quốc tế quality cao nhưng tốn kém** — Phân biệt giữa "học format" (free) vs "copy production value" (tốn tiền).
6. **Short-form (TikTok/Shorts) cần chiến lược riêng** — Dùng để growth nhanh, ko phải để truyền tải nội dung sâu.
7. **Ignore Telegram table format** — Nếu output qua Telegram, dùng bullet list, ko dùng bảng markdown.

---

## Customer Segmentation Research

In addition to competitor business analysis, this skill also covers **customer segment profiling** — researching target demographics by nationality/region to understand spending, behavior, and product fit.

### When to use

- Need to understand a target customer group before building product or pricing
- Deciding which market to target first
- Content strategy or localization decisions
- Digital product positioning (eSIM pricing, MMO content, guides)

### Research Dimensions (7 axes)

Cover ALL of these for each segment:

1. **Spending & Trip Profile** — avg spending/trip, avg length of stay, accommodation tier, tour type split
2. **Research & Booking Channels** — primary search engine, social platforms, booking platforms, trust signals
3. **Key Decision Drivers** — what matters most, deal-breakers, language requirements
4. **Digital Product Fit** — willingness to buy eSIM/guides/prompts, preferred payment method
5. **Content Preferences** — itinerary depth, language, format (video/text/image)
6. **English Proficiency** — native/fluent/basic/very low
7. **Competitive Landscape** — existing digital products targeting this audience (Gumroad, Etsy), pricing benchmarks, case studies, positioning gaps

### Execution (same DDGS + browser approach)

Same Phase 1 methodology as competitor research, but with segment-specific queries:

```python
with DDGS() as ddgs:
    results = list(ddgs.text(
        '"Japanese tourists" Vietnam "average spending" 2024',
        max_results=5
    ))
```

Search strategy per segment (3 passes):
1. **Global behavior** — `"[nationality] tourists travel behavior preferences spending 2024 2025"`
2. **Vietnam-specific** — `"[nationality] tourists Vietnam spending habits travel 2024"`
3. **Deep dive** — extract key articles via browser or additional searches

### Digital Product / MMO Competitive Analysis

For each segment, additionally research:
1. **Gumroad product search:** `gumroad.com/discover?query={niche+keywords}` → browser_navigate + browser_vision
2. **Gumroad trends:** `marketsy.ai/tools/gumroad-trends` → search category
3. **Case studies:** `"gumroad" "travel" site:medium.com` or Reddit — real numbers from sellers
4. **Pricing analysis:** Build table of competitor/price/positioning
5. **Differentiation:** Position between generic low-end ($6-7) vs premium ($39+) → target $12-19 with "real expert" positioning

### Output Format

Present as a compact markdown table with rows for:
- Chi tiêu/ngày, Số ngày, Kênh tìm hiểu, Quan tâm nhất
- English level, eSIM readiness, MMO potential, Product phù hợp

End with chiến lược recommendation: which segment to target first for each product type.

### References

See `references/travel-customer-segments-comparison.md` for the full 5-group comparison (Âu Mỹ, Nhật, Hàn, Trung, Gulf).
See `references/travel-digital-product-competitors.md` for Gumroad competitive analysis, case studies, and differentiation strategy.

## Social Media Page Reconnaissance

### When to use

User asks to "nghiên cứu page Facebook này", "xem page ABC có gì", or needs competitive intelligence from a social media page behind a login wall.

### The problem

Facebook blocks all automated access: `curl` → HTTP 400, `browser_navigate` → login wall, `Graph API` → needs app token, `Wayback Machine` → no cache for Facebook.

### Bypass methods (in order)

1. **Facebook Page Plugin (việc được trước)** — `plugins/page.php` works **without any login**:
   ```
   browser_navigate("https://www.facebook.com/plugins/page.php?href=https://www.facebook.com/<page_name>")
   ```
   Returns: page name, follower count (exact number), profile picture, Follow/Share buttons.

2. **Try mbasic.facebook.com** (failed in practice — still redirects to login).

3. **Wayback Machine** (usually empty — Facebook blocks crawlers).

4. **Graph API** — requires Page Access Token (not publicly available).

5. **Browser vision** on the Page Plugin — extract profile picture content for context clues (e.g. aviation theme → airport niche).

### Output format

Present findings as a compact block:

```
**Name** — [page name]
- **Followers:** [exact number]
- **Avatar:** [mô tả ảnh đại diện và chủ đề]
- **Tình trạng:** [very new / small / active / inactive]
- **Nội dung:** [what's visible / not visible due to login]
```

### Realistic growth projections (zero ads)

When user asks "bao giờ đạt X interactions/tháng" for a new page, use this table:

| Period | Followers | Interactions/mo |
|--------|-----------|----------------|
| Month 1 | 50-200 | 200-500 |
| Month 2 | 200-500 | 500-1.000 |
| Month 3 | 500-1.500 | 1.000-2.000 |
| Month 6 | 2.000-5.000 | 2.000-5.000 |

Adjust down for niche pages (aviation, B2B), adjust up for viral-friendly content (Reels, trending topics).

### Alternatives to recommend

If user's goal (e.g. 5k interactions/mo) is unrealistic with zero ads + a 4-follower page, offer:

1. **Accept realistic timeline** — 3-6 months organic build
2. **Pivot to easier platform** — TikTok / YouTube Shorts (algorithm rewards new creators more)
3. **Merge with existing page** — if they have an older page with followers
4. **Seed content from other channels** — Reddit, hội nhóm, website traffic

## Quick Reference

```
Phase 1: execute_code with DDGS (4-6 parallel queries)
Phase 2: browser_navigate on top 2-3 shortlisted sites
Phase 3: Structured comparison (matrix + pricing)
Phase 4: Insight + actionable recommendation
---
Social media recon: plugins/page.php → vision → report
```
