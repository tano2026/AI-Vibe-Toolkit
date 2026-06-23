# ARCHITECTURE — Research Analytics Pro

## Tổng quan

Mô hình **Orchestrator + 4 Sub-agents** — lấy cảm hứng từ DeerFlow (ByteDance, 71k⭐)
và TradingAgents (multi-analyst debate pattern, 86k⭐) có trong kho AI Vibe Toolkit.

---

## Luồng xử lý

```
User Request
     │
     ▼
┌─────────────────────────────────────────┐
│        RESEARCH ORCHESTRATOR            │
│  Phân loại L0-L5, quyết định pipeline  │
└────────────────┬────────────────────────┘
                 │
     ┌───────────┼────────────┬─────────────┐
     ▼           ▼            ▼             ▼
 [SCOUT]    [VALIDATOR]   [ANALYST]   [SYNTHESIZER]
```

---

## Chi tiết từng tầng

### 🔍 Scout Agent — Thu thập raw data

```
Inputs:  User query
Outputs: Raw data từ multiple sources

Tools:
  Brave Search MCP    → Broad discovery search (tìm landscape, top players)
  Firecrawl MCP       → Deep scrape (industry reports, company pages, academic papers)
  x-research-skill    → X/Twitter search (real-time pulse, practitioner opinions)
  MarkItDown MCP      → Đọc file upload (PDF báo cáo, Excel data, PPT slide)

Logic:
  1. Phân tích query → xác định: cần loại data gì, nguồn nào ưu tiên
  2. Chạy parallel search (không sequential) → tiết kiệm time + token
  3. Dừng khi có đủ ≥2 independent sources cho mỗi claim chính
  4. Tag từng piece of data với: [Nguồn, URL, Ngày, Loại nguồn]
```

### 🧪 Validator Agent — Kiểm chứng & lọc

```
Inputs:  Raw data từ Scout
Outputs: Validated data + Reliability score + Conflict flags

Skills:
  source-evaluation   → Chấm điểm từng nguồn (1-5 sao)
  research-synthesis  → Triangulate, phát hiện mâu thuẫn
  Mem0 check          → Tao đã research chủ đề này chưa? Có context cũ nào hữu ích không?

Reliability scoring:
  ⭐⭐⭐⭐⭐ Primary source: báo cáo chính thức, academic paper, số liệu công ty gốc
  ⭐⭐⭐⭐   Secondary: báo chí uy tín, industry analyst report (Gartner, IDC, McKinsey)
  ⭐⭐⭐     Tertiary: blog chuyên ngành, social media expert opinion
  ⭐⭐      Questionable: anonymous sources, viral claims chưa verify
  ⭐        Unreliable: no source, mâu thuẫn với nhiều nguồn khác

Conflict handling:
  - Phát hiện 2 nguồn mâu thuẫn → KHÔNG chọn 1 mà bỏ 1 → report cả 2 + giải thích
  - Số liệu chênh >20% giữa các nguồn → flag "Disputed Data" trong output
```

### 📊 Analyst Agent — Xử lý & Phân tích

```
Inputs:  Validated data
Outputs: Analysis, models, charts, forecasts

Skills + Tools:
  statistical-analysis  → pandas, numpy, scipy, statsmodels (xử lý số thật)
  market-sizing         → TAM/SAM/SOM model (top-down + bottom-up crosscheck)
  trend-forecasting     → Google TimesFM (nếu có historical time-series)
                          statsmodels ARIMA (fallback nếu dataset nhỏ)
  competitive-intel     → Positioning matrix, feature comparison, price teardown
  TurboVec              → Nếu build knowledge base → vector search tốc độ cao

Analysis patterns (học từ TradingAgents multi-analyst):
  → Market Analyst:      quy mô, growth rate, market dynamics
  → Competitive Analyst: players, positioning, moat, weakness
  → Trend Analyst:       leading indicators, weak signals, scenario planning
  → Risk Analyst:        downside cases, missing data, confidence levels

  Các tầng này DEBATE với nhau → kết luận phải survive cross-examination
  (Không phải 1 model đưa ra → 4 góc nhìn độc lập → synthesizer mới tổng hợp)
```

### 📝 Synthesizer Agent — Ra output cuối

```
Inputs:  Analysis từ Analyst
Outputs: Report + Visualization + Deliverable file

Skills + Tools:
  data-storytelling   → Biến số liệu thành narrative (What → So What → Now What)
  sc-datav / plotly   → Charts, visualization
  xlsx skill          → Export data table, model
  docx skill          → Export full report
  Mem0 save           → Lưu key findings vào long-term memory cho research tiếp theo

Output structure:
  Executive Summary (3 câu)
  → Data & Findings (có nguồn)
  → Analysis & Insight (so-what)
  → Khuyến nghị hành động (cụ thể, ai làm gì)
  → Phụ lục nguồn
```

---

## Token Budget theo tier

```
L0 — Quick Answer:    ~500 tokens     | <1 phút   | 1-2 tools
L1 — Basic Research:  ~2,000 tokens   | ~5 phút   | 3-5 sources
L2 — Deep Research:   ~8,000 tokens   | ~15 phút  | 8-12 sources
L3 — Full Report:     ~20,000 tokens  | ~30 phút  | 15+ sources + code
L4 — Expert Analysis: ~40,000 tokens  | ~60 phút  | code + model + forecast + file output
```

---

## Memory Layer (Mem0)

```
Lưu vào memory sau mỗi research session:
  - Chủ đề đã research + key findings tóm tắt
  - Nguồn chất lượng cao đã dùng (để reuse)
  - Gaps/limitations phát hiện được (để avoid repeat)
  - User's context: ngành của họ, loại câu hỏi họ hay hỏi

Không lưu:
  - File nội bộ nhạy cảm user upload
  - Số liệu tài chính cụ thể của cá nhân
```

---

## Dependency Graph (từ kho AI Vibe Toolkit)

```
research-analytics-pro
├── mcps/firecrawl.md          (Scrape)
├── mcps/brave-search.md       (Search)
├── mcps/markitdown-mcp.md     (Read files)
├── skills/x-research-skill-skill.md    (Twitter research)
├── skills/deep-research-skills-skill.md (Research ladder L0-L5)
├── skills/token-efficient-research.md  (Token optimization)
├── repos/mem0.md              (Long-term memory)
├── repos/google-timesfm.md    (Time-series forecast)
├── repos/turbovec.md          (Vector search)
├── repos/sc-datav.md          (3D Dashboard output)
└── repos/tradingagents.md     (Multi-analyst pattern reference)
```
