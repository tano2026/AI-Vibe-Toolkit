"""
web_search.py — DDG search adapter, zero API key, urllib only (Hermes convention).

Trả về list[dict{title, url, snippet}] — đúng contract brain.py cần.
Dùng HTML endpoint html.duckduckgo.com (không cần JS render, ổn định hơn endpoint chính).

LƯU Ý: DDG có thể đổi cấu trúc HTML bất kỳ lúc nào — nếu search() trả về [] liên tục,
kiểm tra lại _RESULT_BLOCK regex trước khi nghi ngờ pipeline brain.py.
"""
import urllib.request
import urllib.parse
import re

_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
       "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

_RESULT_BLOCK = re.compile(
    r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>.*?'
    r'class="result__snippet"[^>]*>(.*?)</a>',
    re.S,
)


def _strip_tags(html_fragment):
    return re.sub(r"<[^>]+>", "", html_fragment or "").strip()


def search(query, max_results=8):
    """query: str -> list[dict{title, url, snippet}]. Không raise — lỗi trả [] để
    ratelimit.throttled_search tự backoff/retry ở tầng trên."""
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query})
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")

    out = []
    for m in _RESULT_BLOCK.finditer(html):
        raw_url, raw_title, raw_snippet = m.groups()
        # DDG redirect link dạng //duckduckgo.com/l/?uddg=<encoded real url>
        real_url = raw_url
        if "uddg=" in raw_url:
            qs = urllib.parse.parse_qs(urllib.parse.urlparse(raw_url).query)
            real_url = qs.get("uddg", [raw_url])[0]
        out.append({
            "title": _strip_tags(raw_title),
            "url": real_url,
            "snippet": _strip_tags(raw_snippet),
        })
        if len(out) >= max_results:
            break
    return out
