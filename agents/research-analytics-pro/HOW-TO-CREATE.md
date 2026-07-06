# HƯỚNG DẪN TẠO & DEPLOY RESEARCH PRO
> Áp khung Agentic Factory (5 bước) — grounded vào file THẬT đã có trong kho
> `tano2026/AI-Vibe-Toolkit`, không viết lại từ đầu.

---

## Bước 1 — SPEC (đã có, xác nhận lại)

| | |
|--|--|
| **Tên agent** | `research-analytics-pro` |
| **Domain** | Market research · Competitive intel · Tech/tool evaluation · Data analytics |
| **Job-to-be-done** | Nhận câu hỏi → trả báo cáo có nguồn, có công thức, actionable |
| **Người dùng** | Nobitano — qua Claude.ai Project |
| **Mức tự chủ** | Tra cứu + Phân tích (KHÔNG hành động ghi/gửi) |
| **Rủi ro cao nhất** | Bịa số/nguồn → guardrail: tag FACT/ƯỚC TÍNH/GIẢ THUYẾT + blocking rule nếu thiếu input |

---

## Bước 2 — CAPABILITY MAP (đã có 7 + đề xuất thêm 5)

```
TẦNG NÃO (7 skill có sẵn + 5 mới):
  research-synthesis, source-evaluation, market-sizing,
  statistical-analysis, data-storytelling, trend-forecasting,
  competitive-intel
  + data-reality-check      (mới — ép tự tính từ raw data, không chép số)
  + debate-pattern           (mới — 2 phe đối lập cho quyết định rủi ro cao)
  + source-deduplication     (mới — phân biệt nguồn độc lập vs syndicate)
  + report-formatting        (mới — khung 9 khối + bảng tin cậy theo phần)
  + hallucination-detection  (mới — tự nhận diện lúc đang bịa)

TẦNG TAY (MCP/Tools):
  web_search (có sẵn Claude.ai, dùng ngay không cần setup)
  Firecrawl / Brave Search / MarkItDown / Tavily MCP (optional, nếu connect)

TẦNG CƠ (Compute):
  Code execution có sẵn Claude.ai — pandas/thống kê/chart
```

**Lý do KHÔNG thêm domain ticketing/marketing/coding cứng vào đây:** đó là persona
áp dụng khi hỏi TRỰC TIẾP Claude về 3 mảng đó (`userPreferences`) — Research Pro là
agent nghiên cứu ĐA lĩnh vực, dùng `domain-playbooks.md` (đã có) để route đúng ngành
khi cần, không nên bó cứng vào 3 domain cố định.

---

## Bước 3 — PACKAGE (đã tồn tại đủ, không tạo lại)

```
agents/research-analytics-pro/
├── README.md              ✅ có — spec + capability map
├── ARCHITECTURE.md         ✅ có — Orchestrator + Scout/Validator/Analyst/Synthesizer
├── system-prompt.md        ✅ có — v4.2 (đã nâng cấp đủ 3 lần trong session này)
├── domain-playbooks.md     ✅ có — route theo ngành
├── mcp-setup.md            ✅ có — hướng dẫn bật Firecrawl/Brave/MarkItDown
├── deploy-checklist.md     ✅ có — Phase 1 setup + Phase 2 test case
├── skills/                 ⚠️ có 7, THIẾU 5 mới (chưa viết SKILL.md riêng, đang
│                              nằm gộp trong system-prompt.md v4.1 phần "NÂNG CẤP")
└── subagents/
    └── market-research-analyst.md  ✅ có — THAM KHẢO, không chạy được (cần Claude Code CLI)
```

**Còn thiếu duy nhất:** 5 skill mới chưa tách file riêng trong `skills/` — hiện đang
nằm chung trong `system-prompt.md`. Muốn tách hay giữ gộp là quyết định của mày (gộp
tiện đọc 1 lần, tách tiện tái dùng cho agent khác).

---

## Bước 4 — ARCHITECTURE (đã có, không đổi)

```
Research Orchestrator (phân loại L0-L5, chọn pipeline)
├── Scout      — Brave/Firecrawl/Tavily/MarkItDown (thu raw)
├── Validator  — source-evaluation + source-deduplication (chấm tin cậy, khử trùng nguồn)
├── Analyst    — statistical-analysis + data-reality-check (code execution, tự tính)
└── Synthesizer — data-storytelling + report-formatting (insight → khuyến nghị)
```

---

## Bước 5 — GUARDRAIL + DEPLOY THẬT (phần quan trọng nhất — thành thật về hạ tầng)

### Đường deploy DUY NHẤT khả dụng NGAY BÂY GIỜ

**Claude.ai Project riêng** (không phải Hermes — lý do dưới):

1. Tạo Project mới, tên "Research Pro"
2. Copy nội dung `agents/research-analytics-pro/system-prompt.md` (đã bao gồm mọi
   nâng cấp v4.2) → paste vào Project Instructions — hoặc dùng file
   `RESEARCH-PRO-FULL.md` đã gộp sẵn tao đưa mày trước đó
3. Nếu có MCP connect được (Firecrawl/Brave/Tavily) → bật theo `mcp-setup.md`. Không
   có cũng chạy được — `web_search` có sẵn trong Claude.ai đủ dùng cho Scout tầng
4. Chạy đủ 2 test case trong `deploy-checklist.md` Phase 2 trước khi dùng thật

### Đường Hermes — CHƯA khả dụng, đừng thử cho tới khi:

1. Antigravity fix xong ticket `fetch_url` trong `default_api` (xem
   `ANTIGRAVITY-PLAYBOOK.md` mục 🎫 TICKET)
2. Test lại bằng câu hỏi có đáp án biết trước (tránh lặp lại vụ Hermes bịa 6/12 skill)
3. Chỉ sau khi 2 bước trên xong mới nhắn Hermes: *"fetch
   agents/research-analytics-pro/system-prompt.md, áp dụng cho research tiếp theo"*

### Guardrail bắt buộc (đã build sẵn trong system-prompt v4.2)

- Blocking rule: thiếu thị trường/phạm vi địa lý → trả `[CẦN LÀM RÕ]`, không tự đoán
- Mọi claim quan trọng → tag `[FACT]/[ƯỚC TÍNH]/[GIẢ THUYẾT]` + nguồn tại chỗ
- Không có dữ liệu → ghi "KHÔNG CÓ DỮ LIỆU CÔNG KHAI", không bịa
- Domain-age check (RDAP + Wayback) khi đối thủ lạ/mới
- Kết thúc luôn có verdict rõ ràng + bảng tin cậy theo phần + validate list ưu tiên

---

## Việc cần mày quyết ngay để tao làm tiếp

1. Tách 5 skill mới thành file riêng trong `skills/`, hay giữ gộp trong system-prompt?
2. Tạo Claude.ai Project "Research Pro" ngay bây giờ — cần tao push thêm gì vào kho
   trước không, hay đủ rồi bắt đầu dùng thử luôn?
