"""
ratelimit.py — Guard cho DDG search (và mọi nguồn free khác)

Chiến lược 3 lớp:
  1. Cache-first  — hit memory.evidence_cache thì KHÔNG gọi mạng
  2. Token bucket — tối đa 1 request / MIN_INTERVAL giây
  3. Backoff      — lỗi/bị chặn → chờ 2^n giây, tối đa 3 lần rồi bỏ cuộc có kiểm soát
"""
import time, functools
import memory

MIN_INTERVAL = 2.0   # giây giữa 2 request DDG
MAX_RETRIES = 3

_last_call = {"t": 0.0}


def throttled_search(search_fn):
    """
    Decorator wrap hàm search bất kỳ: search_fn(query, **kw) -> list
    Dùng: web_search.search = throttled_search(web_search.search)
    """
    @functools.wraps(search_fn)
    def wrapper(query, **kw):
        # Lớp 1 — cache
        cached = memory.cache_get(query)
        if cached is not None:
            return cached

        # Lớp 2 — token bucket
        wait = MIN_INTERVAL - (time.time() - _last_call["t"])
        if wait > 0:
            time.sleep(wait)

        # Lớp 3 — backoff
        last_err = None
        for attempt in range(MAX_RETRIES):
            try:
                _last_call["t"] = time.time()
                results = search_fn(query, **kw)
                if results:
                    memory.cache_set(query, results)
                return results or []
            except Exception as e:
                last_err = e
                time.sleep(2 ** (attempt + 1))  # 2s, 4s, 8s

        # Bỏ cuộc có kiểm soát — không crash pipeline
        memory.log_lesson("ddg_ratelimit", f"Search fail sau {MAX_RETRIES} lần: {query} | {last_err}")
        return []
    return wrapper
