# RIO Brain v2.0 — Deploy Checklist

## Bước 1 — Copy files vào rio-bot

Copy 4 file này vào `D:\MMO Du an\TANO-AGENCY\rio-bot\` (cùng cấp `rio_bot.py`):

```
brain.py
memory.py
validator.py
ratelimit.py
```

Không cần pip install gì mới — toàn stdlib (sqlite3, urllib, re).

## Bước 2 — Wire vào rio_bot.py

Thêm đầu file:

```python
from brain import RIOBrain
import ratelimit
from modules import web_search, cn_trends, video_extract, report_gen

# rate limit guard cho DDG
web_search.search = ratelimit.throttled_search(web_search.search)

brain = RIOBrain(adapters={
    "search": web_search.search,
    "cn":     cn_trends.get_trends,
    "video":  video_extract.extract,
    "report": report_gen.format_report,   # bỏ dòng này nếu signature không khớp — brain tự có template
})
```

Trong `cmd_research`:

```python
for chunk in brain.run(rtype, topic):
    await update.message.reply_text(chunk, parse_mode="Markdown")
```

`/deep` → `brain.run("deep", topic)`. `/trends` giữ nguyên hoặc route qua brain với `cn_platform=...`.

> ⚠️ Nếu tên hàm module cũ khác (vd `web_search.ddg_search`) → chỉ đổi trong dict adapters, KHÔNG sửa brain.py.

## Bước 3 — Test cases (chạy đủ 5 case trước khi dùng thật)

| # | Test | Pass khi |
|---|------|----------|
| 1 | `/research market fast track Nội Bài` | Report có rating ✅/🟡, có domain nguồn, không crash |
| 2 | Chạy lại đúng lệnh trên trong 24h | Nhanh hơn rõ rệt (cache hit, không gọi DDG) |
| 3 | Rút mạng giữa chừng | Report vẫn ra kèm warning 🔄, bot không chết |
| 4 | `/video <link YouTube bị chặn>` | Warning "nguồn video không truy cập được", pipeline chạy tiếp |
| 5 | Kiểm tra file `rio_memory.db` xuất hiện | `sqlite3 rio_memory.db "select count(*) from research_history"` > 0 |

## Bước 4 — Optional: bật OmniRoute

Chưa wire trong code v2.0 này (giữ zero-dependency). Khi muốn bật:
- Thêm adapter `"llm": omniroute_call` vào dict
- Brain sẽ dùng cho sentiment + polish synthesis ở version sau
- Env: `OMNIROUTE_URL` — không có thì bot vẫn chạy full local

## Bước 5 — Vận hành

- `rio_memory.db` là tài sản — backup tuần 1 lần
- `retrieve_lessons()` xem bot đang vấp gì: `python -c "import memory; print(memory.retrieve_lessons())"`
- Source scores tự học dần — sau ~2 tuần chạy, bot tự ưu tiên nguồn ngon
