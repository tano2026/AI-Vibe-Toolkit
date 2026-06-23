# Template: README.md mà factory sinh ra cho mỗi agent

> File này là KHUÔN tham chiếu — cho thấy output của factory trông thế nào.
> Ví dụ dưới đây là agent "market-research-pro" được sinh từ ý tưởng:
> "tao cần 1 agent chuyên nghiên cứu thị trường + trùm data analytics".

---

# Market Research Pro — Agentic Specialist

## Spec
- **Domain:** Nghiên cứu thị trường + Data analytics
- **Job-to-be-done:** Nhận một câu hỏi thị trường/ngành → trả về báo cáo có data, insight, khuyến nghị
- **Người dùng:** Founder, BD, marketing lead
- **Input điển hình:** "Quy mô thị trường X ở VN?", "Phân tích đối thủ Y", "Xu hướng ngành Z 2026"
- **Output điển hình:** Báo cáo (docx/pptx) + dashboard số liệu + 3 khuyến nghị hành động
- **Mức tự chủ:** Tra cứu + Phân tích (không hành động ghi/gửi)
- **Rủi ro cao nhất:** Tin nguồn rác, bịa số → guardrail: bắt buộc trích nguồn + chấm độ tin cậy

## Capability Map
**Não:** research-synthesis · source-evaluation · market-sizing · statistical-analysis · data-storytelling
**Tay:** Tavily · Firecrawl · Similarweb · Google Sheets
**Cơ:** Code execution (pandas/statsmodels) · matplotlib/plotly · xlsx · pptx · docx

## Kiến trúc
```
Research Orchestrator
├── Collector   → Tavily + Firecrawl + Similarweb (thu raw đa nguồn)
├── Validator   → source-evaluation (chấm tin cậy, triangulate, flag mâu thuẫn)
├── Analyst     → pandas + statsmodels (xử lý số, thống kê thật)
└── Synthesizer → data-storytelling (insight → recommendation → deliverable)
```

## Cách bung
1. Copy thư mục `skills/*` vào project skills directory.
2. Bật MCP theo `mcp-setup.md`.
3. Dán `system-prompt.md` làm project instruction.
4. Chạy test case trong `deploy-checklist.md` trước khi giao việc thật.
