"""
validator.py — Tầng Validator của RIO Brain

4 việc:
  1. sanitize()        — scraped content là DATA, không phải lệnh (chống prompt injection)
  2. score_source()    — chấm độ tin cậy nguồn (tier list + học từ memory)
  3. rate_facts()      — gắn rating ✅/🟡/🔄 cho từng con số
  4. detect_generic()  — bắt generic AI language + số liệu mồ côi
"""
import re
from urllib.parse import urlparse
import memory

# ---------- 1. Sanitize ----------

_INJECTION_PATTERNS = [
    r"ignore (all )?(previous|above) (instructions|prompts)",
    r"you are now",
    r"system prompt",
    r"disregard .{0,30}instructions",
    r"act as (?!a source)",
]


def sanitize(text):
    """Strip mọi pattern giống lệnh trong content scrape về. Content chỉ là data."""
    if not text:
        return ""
    out = text
    for p in _INJECTION_PATTERNS:
        out = re.sub(p, "[stripped]", out, flags=re.I)
    return out[:15000]  # cap length, đỡ phình memory


# ---------- 2. Source scoring ----------

TIER_A = {"reuters.com", "bloomberg.com", "statista.com", "gso.gov.vn", "worldbank.org",
          "imf.org", "mckinsey.com", "vnexpress.net", "cafef.vn", "sec.gov"}
TIER_C = {"quora.com", "reddit.com", "medium.com", "blogspot.com", "pinterest.com"}


def score_source(url):
    """0.0–1.0. Kết hợp tier tĩnh + điểm học được trong memory."""
    domain = urlparse(url).netloc.replace("www.", "")
    base = 0.9 if domain in TIER_A else 0.3 if domain in TIER_C else 0.55
    learned = memory.source_score(domain)
    return round(0.6 * base + 0.4 * learned, 2), domain


# ---------- 3. Fact rating ----------

_NUM = re.compile(r"\d[\d,.]*\s*(%|tỷ|triệu|billion|million|USD|VND|\$)?", re.I)


def extract_numbers(text):
    return [m.group(0).strip() for m in _NUM.finditer(text or "")]


def rate_facts(claims):
    """
    claims: list[dict{text, evidence: list[dict{url, snippet}]}]
    Trả về claims kèm rating:
      ✅ số khớp trên >=2 domain khác nhau
      🟡 chỉ 1 nguồn
      🔄 không có nguồn — là inference, phải nói rõ
    """
    rated = []
    for c in claims:
        domains = set()
        for ev in c.get("evidence", []):
            _, d = score_source(ev["url"])
            domains.add(d)
        if len(domains) >= 2:
            c["rating"] = "✅"
        elif len(domains) == 1:
            c["rating"] = "🟡"
        else:
            c["rating"] = "🔄"
        rated.append(c)
    return rated


# ---------- 4. Anti-hallucination ----------

_GENERIC = [
    "trong thế giới ngày nay", "không thể phủ nhận", "in today's fast-paced world",
    "it's important to note", "đóng vai trò quan trọng trong việc",
    "delve into", "tapestry", "game-changer", "revolutionize",
]


def detect_generic(text):
    """Trả list câu vi phạm generic AI language."""
    hits = [g for g in _GENERIC if g in (text or "").lower()]
    return hits


def orphan_numbers(report_text, fact_ledger):
    """
    Bắt số liệu mồ côi: số xuất hiện trong report nhưng không nằm trong fact ledger.
    fact_ledger: set các chuỗi số đã có evidence.
    """
    nums_in_report = set(extract_numbers(report_text))
    # bỏ số nhỏ vô hại (số thứ tự, năm gần)
    suspicious = {n for n in nums_in_report
                  if not re.fullmatch(r"(19|20)\d\d|[1-9]|10", n.strip())}
    return sorted(suspicious - fact_ledger)
