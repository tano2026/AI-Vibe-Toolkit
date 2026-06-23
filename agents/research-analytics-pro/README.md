# Research Analytics Pro — Agentic Specialist

> Trùm nghiên cứu thị trường + data analytics. Nhận 1 câu hỏi → trả về báo cáo có data, insight, khuyến nghị hành động cụ thể.

---

## Spec

| | |
|--|--|
| **Tên agent** | `research-analytics-pro` |
| **Domain** | Market research · Industry analysis · AI/Tech landscape · Data analytics |
| **Job-to-be-done** | Nhận câu hỏi về thị trường / ngành / đối thủ / trend → trả về báo cáo đầy đủ data, insight, khuyến nghị |
| **Người dùng** | Founder, marketer, analyst, vibe coder muốn hiểu ngành |
| **Input điển hình** | "Quy mô thị trường X ở VN?", "Phân tích đối thủ Y", "AI agent landscape 2026", "Trend nào đang nổi trong ngành Z?" |
| **Output điển hình** | Báo cáo structured (docx/md) + data table + biểu đồ + 3-5 khuyến nghị hành động |
| **Mức tự chủ** | Tra cứu + Phân tích (không tự gửi/ghi nếu chưa được confirm) |
| **Rủi ro cao nhất** | Tin nguồn rác, hallucinate số liệu → **guardrail: bắt buộc trích nguồn + chấm độ tin cậy + triangulate ≥2 nguồn trước khi claim số** |

---

## Capability Map

```
TẦNG NÃO (Skills):
  research-synthesis    — tổng hợp đa nguồn, triangulate, phát hiện mâu thuẫn
  source-evaluation     — chấm độ tin cậy nguồn, phân biệt primary/secondary
  market-sizing         — TAM/SAM/SOM, top-down + bottom-up, Fermi estimation
  statistical-analysis  — phân tích số liệu, trend, correlation, significance
  data-storytelling     — insight → so-what → recommendation (không dump data)
  trend-forecasting     — time-series, leading indicators, scenario planning
  competitive-intel     — benchmarking đối thủ, positioning, feature teardown

TẦNG TAY (MCP/Tools):
  Firecrawl MCP         — scrape web có cấu trúc, crawl entire sites
  Brave Search MCP      — web search sạch cho agent
  MarkItDown MCP        — convert PDF/XLSX/DOCX/PPTX → markdown để feed vào LLM
  x-research-skill      — research X/Twitter, nắm pulse thị trường real-time
  Google Sheets MCP     — lưu data, build tracker, share kết quả

TẦNG CƠ (Compute):
  Code execution        — pandas, numpy, scipy, statsmodels, scikit-learn
  Google TimesFM        — time-series forecasting foundation model (từ kho)
  TurboVec              — vector search tốc độ cao cho RAG pipeline nếu build knowledge base
  sc-datav              — dashboard 3D visualization output
  Mem0                  — long-term memory: nhớ context research trước đó
  Output skills         — xlsx, docx, pdf để xuất deliverable
```

---

## Kiến trúc

```
Research Analytics Orchestrator
│
├── 🔍 Scout Agent
│   ├── Brave Search MCP       → tìm kiếm web broad
│   ├── Firecrawl MCP          → scrape deep từng source
│   ├── x-research-skill       → X/Twitter pulse check
│   └── MarkItDown MCP         → đọc PDF/file người dùng upload
│
├── 🧪 Validator Agent
│   ├── source-evaluation      → chấm tin cậy (Primary / Secondary / Tertiary)
│   ├── research-synthesis     → triangulate, flag mâu thuẫn
│   └── Mem0                   → check context research trước, tránh repeat
│
├── 📊 Analyst Agent
│   ├── statistical-analysis   → pandas/statsmodels xử lý số thật
│   ├── market-sizing          → TAM/SAM/SOM model
│   ├── trend-forecasting      → TimesFM cho time-series nếu có historical data
│   └── competitive-intel      → benchmarking, positioning map
│
└── 📝 Synthesizer Agent
    ├── data-storytelling      → insight + so-what + recommendation
    ├── sc-datav / plotly      → visualization output
    └── xlsx / docx / pdf      → deliverable file
```

---

## Cách bung

1. Copy toàn bộ thư mục `skills/` vào `.claude/skills/` của project.
2. Bật MCP theo `mcp-setup.md`.
3. Dán nội dung `system-prompt.md` vào **Project Instructions** của Claude project.
4. Chạy 3 test case trong `deploy-checklist.md` trước khi dùng thật.
5. Optional: cài Mem0 (`pip install mem0ai`) để agent nhớ context qua các session.

---

## Lấy nguyên liệu từ kho AI Vibe Toolkit

Agent này khai thác trực tiếp các entry đã có trong kho:

| Entry | Dùng cho |
|-------|----------|
| `repos/deerflow.md` | Kiến trúc orchestrator reference |
| `repos/tradingagents.md` | Mô hình multi-analyst debate trước khi ra kết luận |
| `repos/turbovec.md` | Vector search nếu build knowledge base internal |
| `repos/mem0.md` | Long-term memory layer |
| `repos/sc-datav.md` | Dashboard visualization output |
| `repos/google-timesfm.md` | Time-series forecasting |
| `repos/markitdown.md` | Đọc file PDF/Excel/PPT upload |
| `skills/deep-research-skills-skill.md` | Research ladder L0→L5 |
| `skills/x-research-skill-skill.md` | X/Twitter research |
| `skills/token-efficient-research.md` | Tối ưu token khi research |
| `mcps/markitdown-mcp.md` | MCP đọc file |
| `mcps/firecrawl.md` | Scrape web |
| `mcps/brave-search.md` | Web search |
