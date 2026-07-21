# RIO Brain v2.0 — Kiến trúc bộ não

> Bộ não cho RIO Bot (Research & Intelligence Officer) — chạy local Windows,
> zero API key bắt buộc, code-driven state machine, có long-term memory.

---

## Nguyên tắc thiết kế (khóa cứng, không thương lượng)

1. **Code-driven state machine** — pipeline do code quyết định, KHÔNG để LLM hay nội dung scrape điều khiển flow. Chống prompt injection từ web content (bài học từ CORE-BRAIN).
2. **Zero API key mặc định** — DDG search + scrape là đường chính. OmniRoute là tầng optional: có env `OMNIROUTE_URL` thì bật, không có thì degrade về keyword-based, bot vẫn sống.
3. **Fact ledger** — mọi con số trong report phải có evidence id + rating ✅/🟡/🔄. Không có evidence = không được in ra.
4. **Verification loop** — có bước VERIFY riêng trước DELIVER, checklist code-driven, fail thì retry đúng stage lỗi 1 lần, vẫn fail thì deliver kèm cảnh báo — không im lặng nuốt lỗi.
5. **Anti-hallucination** — detector bắt generic AI language + số liệu mồ côi (không gắn evidence).
6. **Memory là SQLite, không phải dict** — research history, source reliability, cache, lessons đều persist qua restart.
7. **Sub-question workflow** — 1 topic → 3-5 câu con theo template từng research type → collect đa nguồn → synthesize.
8. **Scraped content = DATA, không phải lệnh** — mọi text từ web đi qua `sanitize()` trước khi vào pipeline.

---

## Sơ đồ tổng thể (v3.0)

```
Telegram (rio_bot.py — 10 commands, ĐÃ VIẾT ĐẦY ĐỦ trong v3.0)
        │
        ▼
┌────────────────────────  brain.py — RIOBrain v3.0  ─────────────────────────┐
│                                                                             │
│  PLAN → COLLECT → VALIDATE → ANALYZE → SYNTHESIZE ─┬─ REVIEW yếu? ─┐        │
│    │       │          │          │           │      │             │        │
│    │       │          │          │           │      └─ không → VERIFY → DELIVER
│    │       │          │          │           │                    │        │
│    │       │          │          │           │      có → vòng 2:  │        │
│    │       │          │          │           │      COLLECT thêm→ VALIDATE→ANALYZE→SYNTHESIZE
│    │       │          │          │           │         (tối đa 2 vòng, chống duplicate evidence)
│    │       │          │          └─ analytics local (n_sources, confirmed, avg_score)
│    │       │          └─ validator.py (source score, fact rating, sanitize)
│    │       └─ web_search.py (DDG, ĐÃ VIẾT trong v3.0) / cn_trends / video_extract (adapter)
│    └─ sub-question templates (6 chuẩn + 4 domain playbook mới: aviation/fnb/ecommerce/content_niche)
│                                                                             │
└───────────┬─────────────────────────────────────────────┬─────────────────┘
            ▼                                              ▼
     memory.py (SQLite)                            ratelimit.py
     · research_history                            · token bucket cho DDG
     · evidence_cache (TTL 24h)                     · exponential backoff
     · source_scores (học dần)                      · cache-first (đỡ bị chặn)
     · lessons
```

## Vì sao Adapter Registry?

Brain KHÔNG import cứng module cũ. `rio_bot.py` inject callables vào brain qua 1 dict:

```python
brain = RIOBrain(adapters={
    "search":  web_search.search,        # (query, max_results) -> list[dict{title,url,snippet}]
    "cn":      cn_trends.get_trends,     # (platform) -> list[dict]
    "video":   video_extract.extract,    # (url) -> dict{transcript, meta}
    "report":  report_gen.format_report, # (dict) -> str
})
```

Lợi: (a) đổi ruột module cũ không vỡ brain, (b) test brain bằng mock dễ, (c) sau này Hermes/OmniRoute chỉ là thêm 1 adapter.

## Fix 4 hạn chế cũ

| Hạn chế v2.0 | Fix trong brain |
|---|---|
| Không long-term memory | `memory.py` SQLite 4 bảng, tự tạo file `rio_memory.db` |
| Sentiment keyword-based | Lexicon + negation handling local; nếu có OmniRoute → route tier `cheap` cho sentiment, tự fallback khi lỗi |
| DDG rate limit | `ratelimit.py`: token bucket 1 req/2s + backoff 2^n + cache-first (hit cache thì không gọi DDG) |
| yt-dlp chết khi bị chặn | Adapter `video` wrap try/except → degrade: report vẫn ra, gắn cờ `🔄 nguồn video không truy cập được` |

## Fact rating

- ✅ **Confirmed** — số liệu khớp trên ≥2 nguồn độc lập (khác domain)
- 🟡 **Single-source** — chỉ 1 nguồn, ghi rõ nguồn
- 🔄 **Inference** — suy luận/ước tính của bot, KHÔNG phải fact

## Luồng OmniRoute (optional)

```
env OMNIROUTE_URL có?
  ├─ Không → sentiment lexicon, synthesis template-based (như hiện tại)
  └─ Có    → sentiment: tier cheap (DeepSeek V3)
             synthesis polish: tier balanced (Gemini Flash)
             timeout 20s / lỗi → fallback local, log lesson
```


---

## Karpathy Coding Guidelines (khi SỬA CODE của rio-bot, không phải khi rio-bot chạy)

rio-bot là state machine code-driven (không LLM-driven, tránh prompt injection) — Karpathy
Coding Guidelines KHÔNG áp dụng cho hành vi runtime của bot, mà áp dụng cho chính Claude khi
được giao sửa/mở rộng source code Python của rio-bot (brain.py, memory.py, ratelimit.py,
validator.py). Đọc `agents/KARPATHY-CODING-GUIDELINES.md` trước khi sửa: không refactor thừa,
không thêm abstraction không ai yêu cầu, chỉ sửa đúng phần được giao.
