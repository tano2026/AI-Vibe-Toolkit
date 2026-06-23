---
name: competitive-intel
description: >
  Phân tích đối thủ cạnh tranh: positioning, features, pricing, moat, weakness.
  Trigger với: "phân tích đối thủ", "competitive analysis", "so sánh với competitor",
  "ai đang chơi trong thị trường này", "landscape players", "benchmarking".
---

# Competitive Intel — Phân Tích Đối Thủ

---

## Framework phân tích

### Bước 1 — Map the landscape
```
Thu thập danh sách players qua:
  - Brave Search: "[industry] companies Vietnam/SEA/global 2025"
  - Firecrawl: Scrape trang "Alternatives to [leader]" trên G2/Capterra
  - x-research: Search "[category] players" trên X/Twitter
  - Crunchbase/LinkedIn: funding và headcount

Phân loại:
  Tier 1: Market leaders (>20% share hoặc widely recognized)
  Tier 2: Challengers (growing, có funding, đáng theo dõi)
  Tier 3: Niche players (serve specific segment tốt)
  Tier 4: Legacy (declining, dùng làm baseline comparison)
```

### Bước 2 — Feature matrix
```
| Feature         | Player A | Player B | Player C | Mình |
|-----------------|----------|----------|----------|------|
| Core feature 1  |    ✅    |    ✅    |    ❌    |  ?   |
| Core feature 2  |    ✅    |    ❌    |    ✅    |  ?   |
| Pricing (ARPU)  |  $50/mo  |  $30/mo  |  $80/mo  |  ?   |
| Market          |  Global  |  SEA     |  VN      |  ?   |
| Key strength    |  UX      |  Price   |  Local   |  ?   |
| Key weakness    |  Price   |  Support |  Scale   |  ?   |
```

### Bước 3 — Positioning map (2x2 matrix)
```
Chọn 2 dimensions quan trọng nhất với buyer:
  Ví dụ: Price (Low→High) vs Capability (Basic→Advanced)

Plot từng player → tìm "white space" (góc không có ai)

White space = opportunity (hoặc signal là không ai muốn ở đó — phải investigate)
```

### Bước 4 — Moat analysis
```
Đánh giá mỗi player có "moat" gì (rào cản khó copy):
  Network effect: càng nhiều user → càng valuable (LinkedIn, Marketplace)
  Switching cost: expensive/painful to leave (Salesforce, SAP)
  Data moat: unique proprietary data (Google Search, Amazon)
  Brand: trust accumulated over time (McKinsey, Apple)
  Scale/cost: cheapest at scale (Amazon AWS)

Player không có moat = vulnerable to disruption
```

---

## Output format

```
## Competitive Landscape: [Market]

### Summary (1 paragraph)
[Market structure: fragmented/consolidated, who leads, key dynamics]

### Player Matrix
[Table với top 5 players × key dimensions]

### Positioning Map
[2x2 description hoặc chart]

### Key Insights
1. [Điểm mạnh của leader] — implication for new entrants
2. [Gap trong market không ai đang fill]
3. [Trend về cạnh tranh — đang consolidate hay fragmantate?]

### Recommendation
[Dựa trên competitive landscape, nên position như thế nào?]
```
