# Research Pro — AI Agent

## TL;DR
Agent nghiên cứu đa ngành của Nobitano. Nhận bất kỳ câu hỏi nào về thị trường, ngành nghề, đối thủ, số liệu → trả về báo cáo có data thật, nguồn rõ, khuyến nghị actionable. Không bịa số, không dump data vô nghĩa.

## Agent này dùng để làm gì
Research Pro là analyst cấp cao chạy trong Hermes environment. Khác với chatbot thông thường ở chỗ nó **fetch data thật từ API** thay vì trả lời từ training data.

Làm được:
- Nghiên cứu thị trường bất kỳ ngành nào: hàng không, FMCG, SaaS, BĐS, F&B, tài chính, logistics, giáo dục, y tế, nông nghiệp, digital marketing...
- Phân tích đối thủ: pricing, positioning, weakness, cơ hội
- So sánh giá vé, chính sách đổi/hoàn hãng bay (VNA/VJ/QH/VU)
- Tóm tắt báo cáo, tài liệu phức tạp
- Đưa ra khuyến nghị chiến lược dựa trên data

Không làm được (workaround có):
- YouTube API (cần OAuth) → scrape public HTML thay thế
- Meta Ads API (cần Business token) → user export thủ công
- Brave/Firecrawl MCP (không mount được trong Hermes) → urllib Python thay thế

## Khi nào dùng Research Pro vs Hermes

| Tình huống | Dùng cái nào |
|------------|-------------|
| Đang ngồi máy, cần research ngay | Research Pro trực tiếp |
| Cần back-and-forth, hỏi thêm | Research Pro trực tiếp |
| Trên điện thoại / di chuyển | Hermes qua Telegram |
| Thêm repo vào kho AI Vibe Toolkit | Hermes |
| Chạy nền, không cần ngồi chờ | Hermes |

## Setup từng bước

### 1. Copy system-prompt vào Hermes project
Fetch file này từ kho:
```
agents/research-analytics-pro/system-prompt.md
```
Dán toàn bộ vào Project Instructions của Hermes agent.

### 2. Update MEMORY.md
Fetch file này từ kho:
```
configs/hermes-MEMORY.md
```
Copy vào `~/.hermes/MEMORY.md` (thay `[YOUR_GITHUB_TOKEN]` bằng token thật).

### 3. Đọc domain playbooks (optional nhưng nên có)
Fetch:
```
agents/research-analytics-pro/domain-playbooks.md
```
Hermes đọc file này để biết fetch data từ đâu cho từng ngành.

## Ví dụ thực tế

**Input:** "So sánh giá vé HAN-SGN VNA vs VJ ngày 15/7, hạng phổ thông"
**Output:** Bảng giá thực tế từ searchflights API + phí hành lý + chính sách đổi hoàn từng hãng

**Input:** "Market size thương mại điện tử Việt Nam 2026"
**Output:** Số liệu từ World Bank + GSO + news scrape + triangulate ≥2 nguồn + label Primary/Secondary

**Input:** "Phân tích repo F5-TTS — có nên thêm vào kho không"
**Output:** GitHub metadata (stars, velocity, issues) + HN sentiment + PyPI/npm adoption + đánh giá 1-10

## Tools tích hợp

**Search engines (cần API key miễn phí):**
- Tavily API → search engine tốt nhất cho AI agents (1000 req/month free)
- Exa API → semantic search theo meaning (1000 req/month free)

**File reader (local, không cần internet):**
- MarkItDown → đọc PDF/Excel/Word/PPT/CSV → markdown

**Academic (không cần key):**
- Semantic Scholar, arXiv, PubMed

**Python-native (không cần MCP):**
- urllib.request → fetch bất kỳ URL
- GitHub REST API (có token sẵn)
- HN Algolia, Wikipedia, Reddit JSON, DuckDuckGo
- World Bank API, Exchange Rate API
- Google News RSS, VnExpress scrape
- CafeF.vn, Batdongsan.com.vn scrape

**Flight APIs (qua defaultapi):**
- searchflights, bookflight, getliveflightstatus, getliveairportboard, getaircraftlayout

**Skills từ AI Vibe Toolkit:**
- deep-research-skills (L0-L5)
- marketingskills (43 skills)
- x-research-skill, affiliate-skills, youtube-marketing-skills
- fact-checker, scholar-evaluation

## Lưu ý quan trọng

- Đặt vé thật cho khách: **bắt buộc dùng Playwright trên abtrip.vn** — không dùng test API
- Mô hình mặc định: DeepSeek V4 Flash, tự chuyển R1 khi cần suy luận phức tạp
- Output ưu tiên: bảng Markdown > bullets > prose
- Luôn label nguồn: PRIMARY / SECONDARY / INFERENCE / ESTIMATION

## Đánh giá cá nhân
- **Điểm mạnh:** Domain-agnostic — research được bất kỳ ngành nào. Python-native nên không phụ thuộc MCP external. Có sẵn airline fees 2026 cho VNA/VJ/QH/VU. Fallback chain rõ ràng — không nói "không làm được" mà không thử 3 hướng.
- **Điểm yếu:** Một số nguồn data VN (GSO, CAAV) khó scrape tự động do cấu trúc web phức tạp. YouTube/Meta cần workaround thủ công.
- **Có nên dùng không: 9/10** — Con agent này là backbone cho mọi quyết định data-driven của Nobitano. Đầu tư setup 1 lần, dùng hàng ngày.

## Link
- System prompt v4: `agents/research-analytics-pro/system-prompt.md`
- **Cần set env vars:** TAVILY_API_KEY + EXA_API_KEY (lấy miễn phí)
- **Cài local:** `pip install markitdown pandas matplotlib`
- Domain playbooks: `agents/research-analytics-pro/domain-playbooks.md`
- MEMORY template: `configs/hermes-MEMORY.md`
- Upgrade guide: `agents/research-analytics-pro/RESEARCH-UPGRADE.md`
