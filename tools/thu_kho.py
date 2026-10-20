#!/usr/bin/env python3
"""THU KHO - tra kho AI-Vibe-Toolkit, goi y va lap KE HOACH cai dat.

Chi dung thu vien chuan. Vua la CLI vua import duoc:

    from tools.thu_kho import load_catalog, search, card, install_plan, \
        machine_profile, gap_line, usage_line, recommend

LUAT CUNG TRONG CODE
  1. KHONG BAO GIO chay lenh lay tu entry cua kho. install_plan chi DOC va TRINH BAY.
     Lenh duy nhat duoc phep chay: shutil.which(...) va "<cong cu> --version"
     (trong machine_profile) de biet may co gi.
  2. KHONG in gia tri khoa/token; chi ten bien va co/khong.
  3. Moi ke hoach in ro "CHUA CHAY THAT".
  4. Nhan trong kho la nhan do model gan, khong phai ket luan; chua muc nao
     co bang chung dung that (catalog/USAGE-LOG.md).
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------- hang so

STATUS_RANK = {"da-doc-entry-goc": 0, "da-doc-dau-entry": 1, "nhap-tu-tom-tat": 2, "chua-gan-nhan": 3}
CONF_RANK = {"cao": 0, "vua": 1, "thap": 2, "": 3}
KET_QUA_HOP_LE = {"dung duoc": "dùng được", "phai sua": "phải sửa", "bo": "bỏ"}

CANH_BAO_CHUNG = (
    "Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng "
    "dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md)."
)

# bang dong nghia: capability -> cac cum tu (co dau hoac khong, tieng Viet va Anh)
CAPABILITY_SYNONYMS = {
    "web-research": [
        "nghiên cứu thị trường", "nghiên cứu", "research", "deep research", "market research",
        "tìm kiếm web", "web search", "tìm hiểu", "tra cứu", "phân tích đối thủ", "đối thủ",
        "competitor", "competitive", "xu hướng", "trend", "khảo sát", "fact check", "kiểm chứng",
        "tìm tin", "tổng hợp thông tin"],
    "scraping": [
        "cào web", "cào dữ liệu", "cào trang", "crawl", "crawler", "crawling", "scrape", "scraper",
        "scraping", "thu thập dữ liệu", "lấy dữ liệu web", "trích xuất dữ liệu web", "firecrawl",
        "apify", "parse html", "web data"],
    "content-writing": [
        "viết bài", "viết content", "content", "nội dung", "copywriting", "copywriter", "caption",
        "blog", "bài viết", "viết kịch bản", "kịch bản", "storytelling", "biên tập",
        "viết lách", "writing", "article"],
    "seo": [
        "seo", "từ khóa", "từ khoá", "keyword", "xếp hạng google", "tối ưu tìm kiếm", "backlink",
        "serp", "sitemap", "on-page", "onpage", "organic"],
    "ads": [
        "quảng cáo", "ads", "facebook ads", "google ads", "chạy ads", "ppc", "meta ads",
        "tối ưu chiến dịch", "roas", "advertising", "tiktok ads", "remarketing", "affiliate", "tiếp thị liên kết", "link affiliate"],
    "social-media": [
        "mạng xã hội", "social media", "social", "facebook", "fanpage", "đăng bài", "đăng bài facebook",
        "instagram", "tiktok", "youtube", "lên lịch đăng", "lịch đăng", "schedule post", "linkedin",
        "threads", "zalo", "zalo oa", "đăng facebook", "bài đăng", "reels", "shorts", "pinterest", "x.com", "twitter"],
    "email-outreach": [
        "email lạnh", "cold email", "gửi email", "email marketing", "outreach", "newsletter",
        "chiến dịch email", "mail merge", "email sequence", "email sequences", "gmail", "sendgrid",
        "mailchimp", "cold outreach", "thư chào hàng", "viết email", "email"],
    "crm-sales": [
        "crm", "khách hàng tiềm năng", "lead", "leads", "bán hàng", "pipeline", "sales", "chốt deal",
        "quản lý khách hàng", "báo giá", "proposal", "upsell", "deal", "hubspot", "salesforce"],
    "customer-support": [
        "chăm sóc khách hàng", "cskh", "hỗ trợ khách", "chatbot", "chat bot", "trả lời khách",
        "helpdesk", "faq", "live chat", "tổng đài", "bot trả lời", "customer support", "support",
        "trợ lý ảo", "hỏi đáp", "tin nhắn tự động", "chăm sóc khách", "trả lời bình luận",
        "trả lời comment", "reply comment", "rep comment", "rep bình luận", "phản hồi bình luận",
        "trả lời inbox", "zalo oa", "zalo"],
    "video-generation": [
        "làm video", "tạo video", "video ngắn", "video ai", "text to video", "sinh video",
        "clip", "video quảng cáo", "ai video", "video generation", "video", "short video",
        "video có giọng", "video giới thiệu", "video marketing"],
    "video-render": [
        "render video", "dựng video", "dựng phim", "ffmpeg", "remotion", "motion graphics",
        "edit video", "cắt video", "ghép video", "phụ đề", "subtitle", "hyperframes",
        "xuất video", "video code", "video lập trình"],
    "image-generation": [
        "tạo ảnh", "sinh ảnh", "ảnh ai", "vẽ ảnh", "midjourney", "stable diffusion", "text to image",
        "ảnh sản phẩm", "hình ảnh ai", "image generation", "flux", "dall-e", "dalle", "gen ảnh",
        "minh họa", "illustration"],
    "voice-tts": [
        "giọng đọc", "đọc văn bản", "tts", "text to speech", "giọng nói", "lồng tiếng", "voiceover",
        "voice over", "thuyết minh", "giọng ai", "voice clone", "clone giọng", "speech", "đọc truyện",
        "giọng việt", "tiếng việt giọng", "stt", "speech to text", "transcribe", "chuyển giọng nói"],
    "design-ui": [
        "thiết kế", "ui", "ux", "giao diện", "figma", "logo", "branding", "thương hiệu",
        "design system", "mockup", "banner", "poster", "canva", "design", "bộ nhận diện", "wireframe"],
    "front-end": [
        "front end", "front-end", "frontend", "react", "nextjs", "next.js", "landing page",
        "website", "trang web", "html css", "tailwind", "vue", "web app", "giao diện web", "svelte"],
    "backend": [
        "backend", "back end", "back-end", "api", "server", "nodejs", "fastapi", "django",
        "microservice", "webhook", "rest api", "flask", "express"],
    "database": [
        "database", "cơ sở dữ liệu", "sql", "postgres", "postgresql", "mysql", "supabase",
        "mongodb", "lưu trữ dữ liệu", "vector db", "vector database", "redis", "sqlite", "airtable"],
    "devops": [
        "devops", "deploy", "triển khai", "docker", "ci cd", "ci/cd", "vps", "kubernetes",
        "hosting", "nginx", "giám sát hạ tầng", "monitoring", "hạ tầng", "server linux", "cài đặt server"],
    "agent-framework": [
        "agent framework", "framework agent", "langchain", "langgraph", "crewai", "autogen",
        "xây agent", "tạo agent", "ai agent", "agent", "agents", "agentic", "mcp server",
        "xây dựng agent", "agent sdk"],
    "agent-orchestration-memory": [
        "orchestration", "điều phối agent", "bộ nhớ agent", "memory", "multi agent", "multi-agent",
        "workflow agent", "tự động hóa", "tự động hoá", "automation", "workflow", "n8n", "lập lịch",
        "scheduled", "định kỳ", "bộ nhớ dài hạn", "nhiều agent", "cron"],
    "prompt-skill-library": [
        "prompt", "prompts", "thư viện skill", "skill", "skills", "prompt library", "slash command",
        "claude skill", "bộ prompt", "system prompt", "prompt engineering"],
    "browser-automation": [
        "tự động hóa trình duyệt", "tự động hoá trình duyệt", "browser automation", "playwright",
        "puppeteer", "selenium", "điều khiển trình duyệt", "browser use", "chrome automation",
        "trình duyệt", "tự động điền form", "headless"],
    "document-office": [
        "tài liệu", "word", "docx", "excel", "xlsx", "pdf", "powerpoint", "pptx", "slide",
        "slides", "bảng tính", "văn phòng", "google docs", "google sheets", "sheets", "biên bản",
        "hợp đồng", "office", "spreadsheet", "bản trình bày", "thuyết trình"],
    "data-dashboard": [
        "dashboard", "báo cáo", "biểu đồ", "trực quan hóa dữ liệu", "trực quan hoá", "bi",
        "metabase", "superset", "grafana", "kpi", "phân tích dữ liệu", "analytics", "report",
        "reporting", "data visualization", "looker", "chart", "bảng điều khiển", "power bi"],
    "finance-accounting": [
        "kế toán", "tài chính", "hóa đơn", "hoá đơn", "invoice", "thuế", "báo cáo tài chính",
        "thu chi", "ngân sách", "accounting", "bookkeeping", "finance", "budget", "lương", "payroll"],
    "ticketing-aviation": [
        "vé máy bay", "hàng không", "sân bay", "đặt vé", "gds", "amadeus", "sabre", "ticketing",
        "fast track", "hành lý", "airline", "aviation", "flight", "chuyến bay"],
    "security-compliance": [
        "bảo mật", "security", "tuân thủ", "compliance", "pentest", "lỗ hổng", "gdpr",
        "audit bảo mật", "kiểm tra an ninh", "secret scan", "vulnerability", "quyền riêng tư",
        "privacy", "an toàn thông tin", "mã hóa"],
    "local-llm": [
        "llm local", "chạy model local", "ollama", "llama.cpp", "llamacpp", "vllm", "mô hình cục bộ",
        "local ai", "gguf", "self host llm", "chạy llm", "model cục bộ", "lm studio", "local llm"],
    "productivity": [
        "năng suất", "to do", "todo", "ghi chú", "lịch", "quản lý công việc", "notion", "obsidian",
        "task", "nhắc việc", "họp", "tóm tắt cuộc họp", "productivity", "calendar", "second brain",
        "ghi chép", "meeting"],
    "reference": [
        "tài liệu tham khảo", "hướng dẫn", "awesome list", "awesome", "danh sách", "cheatsheet",
        "tham khảo", "tutorial", "học", "khóa học", "tổng hợp", "cẩm nang", "guide", "reference"],
}

# cum chung chung: chi tinh la tin hieu yeu (khong tu khoi dong mot "kha nang")
_YEU = {"ui", "ux", "bi", "task", "học", "hoc", "design", "support", "content", "email", "lead", "deal",
        "report", "word", "slide", "server", "api", "agent", "agents", "skill", "skills", "prompt",
        "prompts", "tài liệu", "nội dung", "reference", "guide", "danh sách", "tổng hợp", "tham khảo",
        "hướng dẫn", "lịch", "họp", "video", "clip", "x.com", "twitter", "research", "trend", "xu hướng",
        "nghiên cứu", "automation", "workflow", "memory", "định kỳ", "scheduled", "speech", "sales",
        "finance", "budget", "security", "privacy", "ads", "social", "chart", "meeting"}

STOPWORDS = set("""
cho va cua can lam toi muon mot cac nhung de voi la nao duoc the nhu trong tren ra vao hay hoac o tai
giup tao khong ko co nhan tu den khi thi bang ve se dang da cung rat hon nhat theo nua con dua tinh nang
mot may viec cong cu dung tim kiem thu goi y
a an the to for and of with in on my i we want need how do make build create use using by from or is are
""".split())

# ---------------------------------------------------------------- chuan hoa chu

def bo_dau(s):
    """Chuan hoa: bo dau tieng Viet, d->d, thuong hoa."""
    if s is None:
        return ""
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "d").lower()


def _tu(s):
    return re.findall(r"[a-z0-9]+(?:[.\-][a-z0-9]+)*", bo_dau(s))


def _tu_goc(s):
    """Cac tu giu nguyen dau (NFC, thuong) - de kiem tra khop co dau."""
    return set(re.findall(r"\w+", unicodedata.normalize("NFC", str(s or "")).lower()))


def _tach(s):
    """Tach thanh tu; giu ca dang gach noi/cham va dang tach roi (next.js -> next, js)."""
    out = []
    for w in _tu(s):
        out.append(w)
        if "-" in w or "." in w:
            out.extend(p for p in re.split(r"[.\-]", w) if p)
    return out


def _chuan_cum(phrase):
    return tuple(_tach(phrase))


_SYN_NORM = {}
for _cap, _ps in CAPABILITY_SYNONYMS.items():
    _SYN_NORM[_cap] = [(p, _chuan_cum(p), p in _YEU) for p in _ps]

# ---------------------------------------------------------------- nap catalog

_CACHE = {}


def _repo(repo_root=None):
    if repo_root is not None:
        return Path(repo_root)
    return Path(__file__).resolve().parents[1]


def _doc_audit(root):
    p = root / "catalog" / "audit.json"
    if not p.is_file():
        return {}
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}
    if isinstance(d, dict) and isinstance(d.get("items"), (dict, list)):
        d = d["items"]
    if isinstance(d, list):
        d = {r.get("id"): r for r in d if isinstance(r, dict) and r.get("id")}
    return d if isinstance(d, dict) else {}


def load_catalog(repo_root=None):
    """Doc catalog/catalog.json (+ audit.json neu co). Tra dict id -> muc (them truong `audit`)."""
    root = _repo(repo_root)
    cat = root / "catalog" / "catalog.json"
    if not cat.is_file():
        raise FileNotFoundError("Không thấy %s - chạy tools/build_catalog.py hoặc đồng bộ git." % cat)
    data = json.loads(cat.read_text(encoding="utf-8"))
    items = data["items"] if isinstance(data, dict) else data
    audit = _doc_audit(root)
    out = {}
    for r in items:
        r = dict(r)
        a = audit.get(r["id"])
        r["audit"] = a if isinstance(a, dict) else None
        out[r["id"]] = r
    return out


def _caps(r):
    return [c.strip() for c in (r.get("capability") or "").split(",") if c.strip()]


def _csv(v):
    return [c.strip() for c in (v or "").split(",") if c.strip()]


def _audit_usable(r):
    a = r.get("audit")
    if isinstance(a, dict) and "usable" in a:
        return a["usable"]
    return None


def _index(repo_root=None):
    root = _repo(repo_root)
    key = str(root.resolve())
    if key in _CACHE:
        return _CACHE[key]
    cat = load_catalog(root)
    ids = list(cat)
    fields = []
    raws = []
    for i in ids:
        r = cat[i]
        f = {
            "ten": set(_tach(r.get("ten"))),
            "id": set(_tach(r.get("id", "") + " " + r.get("duong_dan", ""))),
            "use_when": set(_tach(r.get("use_when"))),
            "tom_tat": set(_tach(r.get("tom_tat"))),
            "evidence": set(_tach(r.get("evidence"))),
            "domain": set(_tach(r.get("domain"))),
        }
        fields.append(f)
        raws.append({
            "ten": _tu_goc(r.get("ten")), "id": _tu_goc(r.get("id", "")),
            "use_when": _tu_goc(r.get("use_when")), "tom_tat": _tu_goc(r.get("tom_tat")),
            "evidence": _tu_goc(r.get("evidence")), "domain": _tu_goc(r.get("domain")),
        })
    idx = {"cat": cat, "ids": ids, "fields": fields, "raws": raws, "tokcache": {}, "N": len(ids)}
    _CACHE[key] = idx
    return idx


FIELD_W = {"ten": 2.0, "id": 1.5, "use_when": 1.5, "tom_tat": 1.0, "evidence": 0.7, "domain": 0.5}


def _khop_token(idx, tok):
    """tok -> {chi_so_muc: (trong_so_truong_tot_nhat, ten_truong)}; khop dung hoac theo dau tu."""
    c = idx["tokcache"].get(tok)
    if c is not None:
        return c
    res = {}
    pref = len(tok) >= 4
    for n, f in enumerate(idx["fields"]):
        best = None
        for fname, words in f.items():
            hit = tok in words
            if not hit and pref:
                hit = any(w.startswith(tok) for w in words)
            if hit:
                w = FIELD_W[fname]
                if best is None or w > best[0]:
                    best = (w, fname)
        if best:
            res[n] = best
    idx["tokcache"][tok] = res
    return res


def _idf(idx, tok):
    df = len(_khop_token(idx, tok))
    return math.log((idx["N"] + 1) / (df + 1)) + 0.5

# ---------------------------------------------------------------- phan tich truy van

_NEG_RE = re.compile(
    r"\b(?:khong|ko|k|no|without|tranh)\s+(?:can\s+|dung\s+|co\s+|ton\s+|mat\s+|yeu cau\s+|bat buoc\s+)?"
    r"(gpu|vps|docker|browser|trinh duyet|api key|api-key|apikey|tra phi|ton phi|mat phi)\b")
_FREE_RE = re.compile(r"\b(mien phi|free)\b")
_NEG_MAP = {"gpu": "gpu", "vps": "vps", "docker": "docker", "browser": "browser", "trinh duyet": "browser",
            "api key": "api-key", "api-key": "api-key", "apikey": "api-key", "tra phi": "tra-phi",
            "ton phi": "tra-phi", "mat phi": "tra-phi"}


def _cum_trong(toks, phrase_toks):
    n = len(phrase_toks)
    if n == 0:
        return False
    for i in range(len(toks) - n + 1):
        if tuple(toks[i:i + n]) == phrase_toks:
            return True
    return False


# mo rong cau hoi tieng Viet sang tu khoa Anh (entry trong kho phan lon viet tieng Anh/ten rieng)
EXPAND = {
    "email lạnh": ["cold", "email", "outreach"], "cào web": ["scrape", "scraper", "crawl"],
    "cào dữ liệu": ["scrape", "crawl"], "giọng đọc": ["tts", "voice", "speech"],
    "đăng bài": ["post", "publish", "schedule"], "lên lịch": ["schedule", "scheduler"],
    "lịch đăng": ["schedule", "scheduler"], "video ngắn": ["shorts", "short", "reels"],
    "khách hàng": ["customer", "client"], "trả lời bình luận": ["reply", "comment"], "affiliate": ["affiliate"], "đối thủ": ["competitor"], "báo cáo": ["report", "reporting"],
    "tiếng việt": ["vietnamese", "vietnam"], "chăm sóc khách hàng": ["support", "customer"],
    "quảng cáo": ["ads", "advertising"], "thiết kế": ["design"], "trình duyệt": ["browser"],
    "tạo ảnh": ["image", "generate"], "làm video": ["video", "generate"], "viết bài": ["write", "writing"],
}
EXPAND_NORM = [(_chuan_cum(k), v) for k, v in EXPAND.items()]


def phan_tich_truy_van(query):
    """Phan tich 1 cau truy van: kha nang phat hien (kem cum khop), bo-can ngam hieu, tu khoa."""
    norm = bo_dau(query)
    neg = []
    for m in _NEG_RE.finditer(norm):
        v = _NEG_MAP.get(m.group(1))
        if v and v not in neg:
            neg.append(v)
    norm_clean = _NEG_RE.sub(" ", norm)
    free = bool(_FREE_RE.search(norm_clean))
    if free and "tra-phi" not in neg:
        neg.append("tra-phi")
    norm_clean = _FREE_RE.sub(" ", norm_clean)
    toks = _tach(norm_clean)
    caps = {}
    for cap, lst in _SYN_NORM.items():
        hits = []
        for raw, pt, yeu in lst:
            if _cum_trong(toks, pt):
                hits.append((raw, yeu))
        if hits:
            caps[cap] = hits
    # vi tri xuat hien dau tien de sap thu tu
    def vitri(cap):
        best = 10 ** 6
        for raw, pt, _ in _SYN_NORM[cap]:
            n = len(pt)
            for i in range(len(toks) - n + 1):
                if tuple(toks[i:i + n]) == pt:
                    best = min(best, i)
                    break
        return best
    order = sorted(caps, key=vitri)
    # "khai nang" manh = co it nhat 1 cum khong thuoc nhom yeu
    cap_info = []
    for c in order:
        manh = [h for h, y in caps[c] if not y]
        cap_info.append({"capability": c, "cum_khop": [h for h, _ in caps[c]], "manh": bool(manh)})
    if any(c["manh"] for c in cap_info):
        # cum chung chung (vd "lich", "video") chi la tin hieu yeu: bo khi da co kha nang manh
        cap_info = [c for c in cap_info if c["manh"]]
    # tu nam trong cum nhieu tu da khop capability da duoc tinh qua capability: van dung lam
    # tu khoa nhung trong so thap (tranh nhieu kieu "cao" = cao trong tieng Viet khong dau)
    da_dung = set()
    for cap in caps:
        for raw, pt, _ in _SYN_NORM[cap]:
            if len(pt) > 1 and _cum_trong(toks, pt):
                da_dung.update(pt)
    keywords = [t for t in toks if t not in STOPWORDS and len(t) > 1]
    mo_rong = []
    for pt, ex in EXPAND_NORM:
        if _cum_trong(toks, pt):
            mo_rong.extend(x for x in ex if x not in mo_rong)
    dau = {}
    for w in re.findall(r"\w+", unicodedata.normalize("NFC", str(query)).lower()):
        u = bo_dau(w)
        if u != w:
            dau.setdefault(u, set()).add(w)
    return {"query": query, "capabilities": cap_info, "exclude_needs_ngam": neg, "tu_khoa": keywords,
            "tu_khoa_yeu": sorted(da_dung), "tu_khoa_mo_rong": mo_rong, "dau": {k: sorted(v) for k, v in dau.items()}}

# ---------------------------------------------------------------- search

def _score_items(idx, pq, forced_cap=None):
    """Tinh diem cho moi muc. Tra dict chi_so -> info.
    Tu khoa: tu thuong (trong so 1.0), tu nam trong cum capability (0.6), tu mo rong sang tieng Anh (0.6,
    chi cong vao tu so, khong vao mau cua coverage)."""
    kw = []
    seen = set()
    yeu = set(pq.get("tu_khoa_yeu", ()))
    for t in pq["tu_khoa"]:
        if t not in seen:
            seen.add(t)
            kw.append(t)
    mrong = [t for t in pq.get("tu_khoa_mo_rong", ()) if t not in seen]
    wmul = {t: (0.6 if t in yeu else 1.0) for t in kw}
    for t in kw:
        if t in PLATFORMS:
            wmul[t] = 2.5  # ten rieng (facebook, zalo...) la tin hieu manh hon tu thuong
    dau = pq.get("dau", {})
    for t in mrong:
        wmul[t] = 0.6
    idfs = {t: _idf(idx, t) * wmul[t] for t in kw + mrong}
    tot_idf = sum(idfs[t] for t in kw) or 1.0
    caps = [c["capability"] for c in pq["capabilities"]]
    if forced_cap and forced_cap not in caps:
        caps = caps + [forced_cap]
    matches = {t: _khop_token(idx, t) for t in kw + mrong}
    out = {}
    for n, rid in enumerate(idx["ids"]):
        r = idx["cat"][rid]
        rc = _caps(r)
        cap_score = 0.0
        cap_hit = []
        for c in caps:
            if c in rc:
                pos = rc.index(c)
                cap_score += 12.0 if pos == 0 else 7.0
                cap_hit.append((c, pos == 0))
        text_num = 0.0
        matched = []
        cov_num = 0.0
        for t in kw + mrong:
            m = matches[t].get(n)
            if m:
                f = 1.0  # co dau va khong dau cho cung ket qua (khong phat khop sai dau)
                text_num += idfs[t] * m[0] * f
                cov_num += idfs[t] * f
                matched.append((t, m[1]))
        coverage = min(1.0, cov_num / tot_idf)
        text_score = min(16.0, 16.0 * text_num / (tot_idf * 2.0))
        out[n] = {"cap_score": cap_score, "cap_hit": cap_hit, "text_score": text_score,
                  "coverage": coverage, "matched": matched}
    return out


def _brief_item(r, score, info, ghi_chu, tier=0):
    return {
        "id": r["id"],
        "ten": r.get("ten"),
        "loai": r.get("loai"),
        "score": round(score, 2),
        "bac_khop": tier,
        "ly_do_khop": info,
        "capability": r.get("capability", ""),
        "adoption": r.get("adoption", ""),
        "needs": r.get("needs", ""),
        "vessel_fit": r.get("vessel_fit", ""),
        "curation_status": r.get("curation_status", ""),
        "confidence": r.get("confidence", ""),
        "dup_group": r.get("dup_group", ""),
        "use_when": r.get("use_when", ""),
        "skip_if": r.get("skip_if", ""),
        "evidence": r.get("evidence", ""),
        "rui_ro": r.get("rui_ro", ""),
        "audit_usable": _audit_usable(r),
        "duong_dan": r.get("duong_dan", ""),
        "ghi_chu": ghi_chu,
    }


PLATFORMS = {"facebook", "fanpage", "instagram", "tiktok", "youtube", "zalo", "linkedin", "twitter", "threads",
             "gmail", "hubspot", "salesforce", "figma", "canva", "notion", "obsidian", "supabase", "postgres",
             "mysql", "mongodb", "redis", "ollama", "n8n", "playwright", "puppeteer", "selenium", "ffmpeg",
             "remotion", "firecrawl", "apify", "midjourney", "langchain", "langgraph", "airtable", "shopify",
             "telegram", "whatsapp", "slack", "discord", "wordpress", "pinterest", "mailchimp", "sendgrid"}

_GANH_NANG = ("tra-phi", "gpu", "vps", "docker", "claude-code-only", "browser", "api-key")


def _search_core(idx, query, *, vessel, excl, mode, adoption_not, capability, top):
    """mode: 'khong' (bo muc chua gan nhan) | 'gom' (gom ca) | 'chi' (chi muc chua gan nhan)."""
    pq = phan_tich_truy_van(query)
    excl = set(excl or ()) | set(pq["exclude_needs_ngam"])
    sc = _score_items(idx, pq, forced_cap=capability)
    has_cap = bool(pq["capabilities"]) or bool(capability)
    cands = []
    for n, rid in enumerate(idx["ids"]):
        r = idx["cat"][rid]
        s = sc[n]
        chua = r.get("curation_status") == "chua-gan-nhan"
        if capability and capability not in _caps(r):
            continue
        if mode == "khong" and chua:
            continue
        if mode == "chi" and not chua:
            continue
        if r.get("adoption") in adoption_not:
            continue
        needs = _csv(r.get("needs"))
        if excl and any(x in excl for x in needs):
            continue
        vf = _csv(r.get("vessel_fit"))
        ghi_chu = []
        if vessel:
            if vf and vessel not in vf:
                continue
            if not vf and not chua:
                ghi_chu.append("vessel_fit rỗng = chưa rõ có chạy trên '%s' không" % vessel)
        if chua:
            # muc chua gan nhan khong co capability: chi xet theo van ban, nguong chat hon
            if s["coverage"] < 0.68:
                continue
        elif has_cap:
            if s["cap_score"] <= 0 and s["coverage"] < 0.6:
                continue
        else:
            if s["coverage"] < 0.34:
                continue
        total = s["cap_score"] + s["text_score"]
        if total <= 0:
            continue
        parts = []
        if s["cap_hit"]:
            parts.append("capability " + ", ".join(
                "%s (%s)" % (c, "chính" if p else "phụ") for c, p in s["cap_hit"]))
        if s["matched"]:
            parts.append("từ khoá: " + ", ".join("%s@%s" % (t, f) for t, f in s["matched"][:6]))
        if chua:
            ghi_chu.append("chưa gắn nhãn - chỉ có mô tả, không có use_when/skip_if/needs; đọc entry trước khi tin")
        if not vf and vessel and chua:
            ghi_chu.append("vessel_fit rỗng = chưa rõ")
        ca = _audit_usable(r)
        if ca is False:
            a = r.get("audit") or {}
            ghi_chu.append("audit tự động: không dùng được (%s)" % (a.get("ly_do") or a.get("reason") or "xem audit.json"))
        cands.append((n, r, total, "; ".join(parts) or "khớp văn bản", ghi_chu))
    if not cands:
        return []
    best = max(c[2] for c in cands)
    res = []
    for n, r, total, ly, gc in cands:
        rel = total / best if best else 0
        if rel >= 0.88:
            tier = 0
        elif rel >= 0.7:
            tier = 1
        elif rel >= 0.45:
            tier = 2
        elif rel >= 0.25:
            tier = 3
        else:
            continue
        res.append((tier, n, r, total, ly, gc))

    def key(x):
        tier, n, r, total, _, _ = x
        bad = 1 if _audit_usable(r) is False else 0
        burden = sum(1 for v in _csv(r.get("needs")) if v in _GANH_NANG)
        rc = _caps(r)
        # do khop capability: so capability cua truy van ma muc nay co o vi tri CHINH (dau danh sach)
        chinh = sum(1 for c in qcaps if rc and rc[0] == c)
        # ten rieng (zalo, facebook...) cua truy van nam ngay o ten/id muc = muc DANH RIENG cho nen tang do,
        # nen xep truoc muc chi trung capability chung (vd customer-support) dù confidence cao hon
        rieng = sum(1 for t, f in sc[n]["matched"] if t in PLATFORMS and f in ("ten", "id"))
        return (bad, tier, -min(rieng, 1), -chinh, CONF_RANK.get(r.get("confidence", ""), 3),
                STATUS_RANK.get(r.get("curation_status"), 3), -round(total), burden, -total)

    qcaps = set(c["capability"] for c in pq["capabilities"]) | ({capability} if capability else set())
    res.sort(key=key)
    return [_brief_item(r, total, ly, gc, tier) for tier, n, r, total, ly, gc in res[:max(1, int(top))]]


def search(query, *, vessel=None, exclude_needs=(), include_unlabeled=False,
           adoption_not=("chi-tham-khao",), capability=None, top=5, repo_root=None):
    """Tim muc trong kho. Xep hang theo AGENT-ROUTER:
    bac khop -> do khop capability chinh -> confidence (cao truoc) -> curation_status (goc truoc dau-entry)
    -> diem khop -> it dieu kien ganh nang.
    'bac khop' chi tach cac muc khop yeu hon han muc tot nhat (bang tong diem capability + tu khoa), de
    thu tu confidence/curation_status chi quyet dinh giua cac muc khop NGANG NHAU. Muc vessel_fit rong
    van hien (kem ghi chu 'chua ro'). Muc chua gan nhan chi hien khi include_unlabeled=True."""
    idx = _index(repo_root)
    return _search_core(idx, query, vessel=vessel, excl=exclude_needs,
                        mode="gom" if include_unlabeled else "khong",
                        adoption_not=adoption_not, capability=capability, top=top)


def goi_y_chua_nhan(query, *, vessel=None, exclude_needs=(), top=3, repo_root=None):
    """Cac muc CHUA GAN NHAN khop van ban chat che voi truy van (de nguoi dung biet kho con co gi nua)."""
    idx = _index(repo_root)
    return _search_core(idx, query, vessel=vessel, excl=exclude_needs, mode="chi",
                        adoption_not=(), capability=None, top=top)[:top]

# ---------------------------------------------------------------- the chi tiet

def _tim_muc(idx, id_):
    cat = idx["cat"]
    if id_ in cat:
        return cat[id_]
    s = str(id_).strip().replace("\\", "/")
    for r in cat.values():
        if r.get("duong_dan") == s or r.get("duong_dan") == s + ".md":
            return r
    low = [r for r in cat.values() if r["id"].lower() == s.lower() or r["id"].split("/")[-1].lower() == s.lower()]
    if len(low) == 1:
        return low[0]
    if len(low) > 1:
        raise KeyError("id '%s' mơ hồ, khớp %d mục: %s" % (id_, len(low), ", ".join(x["id"] for x in low[:6])))
    raise KeyError("Không có mục '%s' trong kho." % id_)


def card(id, repo_root=None):
    """The chi tiet cua 1 muc: nhan, evidence, dieu kien, rui ro, audit, nguon."""
    idx = _index(repo_root)
    r = _tim_muc(idx, id)
    root = _repo(repo_root)
    p = root / r.get("duong_dan", "")
    canh_bao = []
    st = r.get("curation_status")
    if st == "da-doc-dau-entry":
        canh_bao.append("Nhãn mới dựa trên phần đầu entry; phần Lưu ý chưa dò hết - đọc entry gốc.")
    elif st == "chua-gan-nhan":
        canh_bao.append("Chưa gắn nhãn: chỉ có mô tả ngắn; không có use_when/skip_if/needs.")
    elif st == "da-doc-entry-goc":
        canh_bao.append("Đã đọc nguyên entry (Claude kiểm mẫu), nhưng vẫn là đọc, chưa phải chạy.")
    needs = _csv(r.get("needs"))
    if "claude-code-only" in needs:
        canh_bao.append("Chỉ chạy trong Claude Code.")
    if r.get("skip_if") in ("", "unknown", None):
        canh_bao.append("skip_if = unknown: chưa có nghĩa là không có điều kiện loại trừ.")
    ca = _audit_usable(r)
    if ca is False:
        canh_bao.append("Audit tự động đánh dấu KHÔNG dùng được.")
    canh_bao.append(CANH_BAO_CHUNG)
    return {
        "id": r["id"], "ten": r.get("ten"), "loai": r.get("loai"),
        "tom_tat": r.get("tom_tat"), "capability": r.get("capability"),
        "use_when": r.get("use_when"), "skip_if": r.get("skip_if"),
        "adoption": r.get("adoption"), "needs": r.get("needs"), "vessel_fit": r.get("vessel_fit"),
        "dup_group": r.get("dup_group"), "confidence": r.get("confidence"),
        "curation_status": r.get("curation_status"), "evidence": r.get("evidence"),
        "rui_ro": r.get("rui_ro"), "license": r.get("license"), "diem": r.get("diem"),
        "xac_minh": r.get("xac_minh"), "domain": r.get("domain"), "cap_nhat": r.get("cap_nhat"),
        "co_agent_integration": r.get("co_agent_integration"),
        "audit": r.get("audit"), "audit_usable": ca,
        "duong_dan": r.get("duong_dan"), "entry_ton_tai": p.is_file(),
        "duong_dan_tuyet_doi": str(p),
        "canh_bao": canh_bao,
    }

# ---------------------------------------------------------------- may

TOOLS = [("git", ["git"]), ("node", ["node"]), ("npm", ["npm"]), ("python", ["python", "python3", "py"]),
         ("pip", ["pip", "pip3"]), ("docker", ["docker"]), ("ffmpeg", ["ffmpeg"])]
KEY_ENV_BIET_TRUOC = [
    "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY", "DEEPSEEK_API_KEY",
    "OPENROUTER_API_KEY", "AIRTABLE_API_KEY", "AIRTABLE_TOKEN", "TELEGRAM_BOT_TOKEN", "APIFY_TOKEN",
    "ELEVENLABS_API_KEY", "FIRECRAWL_API_KEY", "FACEBOOK_PAGE_TOKEN", "META_ACCESS_TOKEN",
    "YOUTUBE_API_KEY", "GITHUB_TOKEN", "REPLICATE_API_TOKEN", "FAL_KEY", "HF_TOKEN",
]
_KEY_NAME_RE = re.compile(r"(API[_-]?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|PRIVATE[_-]?KEY|_KEY$)", re.I)


def _lay_phien_ban(path):
    try:
        p = subprocess.run([path, "--version"], capture_output=True, text=True, timeout=8)
        out = (p.stdout or p.stderr or "").strip().splitlines()
        return out[0][:120] if out else ""
    except Exception:
        return ""


def machine_profile(lay_phien_ban=True):
    """Ho so may: he dieu hanh, cong cu co/khong (+ phien ban qua '--version'), TEN bien khoa co dat hay khong.
    KHONG doc gia tri bien moi truong ngoai viec kiem tra co/khong rong."""
    tools = {}
    for name, cands in TOOLS:
        found = None
        for c in cands:
            p = shutil.which(c)
            if p:
                found = p
                break
        info = {"co": bool(found)}
        if found and lay_phien_ban:
            info["phien_ban"] = _lay_phien_ban(found)
        tools[name] = info
    dat = sorted(k for k, v in os.environ.items() if _KEY_NAME_RE.search(k) and v)
    return {
        "he_dieu_hanh": "%s %s" % (platform.system(), platform.release()),
        "kien_truc": platform.machine(),
        "python": platform.python_version(),
        "cong_cu": tools,
        "bien_khoa_biet_truoc": {k: bool(os.environ.get(k)) for k in KEY_ENV_BIET_TRUOC},
        "bien_khoa_dang_dat": dat,
        "ghi_chu": "Chỉ ghi tên biến và có/không; không đọc hay in giá trị.",
    }

# ---------------------------------------------------------------- ke hoach cai

_FENCE_RE = re.compile(r"^```[ \t]*([\w+-]*)[^\n]*\n(.*?)^```[ \t]*$", re.S | re.M)
_H2_RE = re.compile(r"^##\s+(.*)$", re.M)

DANGER_RED = [
    (re.compile(r"(?:curl|wget|iwr|irm|invoke-webrequest|invoke-restmethod)\b[^\n|]*\|\s*(?:sudo\s+)?(?:ba|z|da|k)?sh\b", re.I),
     "curl|sh: chạy thẳng mã tải từ mạng, chưa đọc"),
    (re.compile(r"\|\s*(?:iex|invoke-expression)\b", re.I), "tải rồi chạy luôn (| iex)"),
    (re.compile(r"(?:curl|wget)\b[^\n|]*\|\s*(?:python3?|node|perl|ruby)\b", re.I), "tải rồi chạy luôn qua trình thông dịch"),
    (re.compile(r"\bsudo\b", re.I), "dùng sudo (quyền root)"),
    (re.compile(r"\brm\s+-[a-z]*r[a-z]*f|\brm\s+-[a-z]*f[a-z]*r|remove-item\b[^\n]*-recurse[^\n]*-force|rmdir\s+/s\s+/q|\bdel\s+/f\s+/s", re.I),
     "xoá đệ quy cưỡng bức (rm -rf)"),
    (re.compile(r"\bchmod\s+(?:-R\s+)?0?777\b", re.I), "chmod 777"),
    (re.compile(r"setenforce\s+0|ufw\s+disable|set-executionpolicy\s+(?:unrestricted|bypass)|NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*0|"
                r"--insecure\b|--no-check-certificate|--dangerously-skip-permissions|--privileged\b|--disable-web-security|"
                r"DisableRealtimeMonitoring|add-mppreference[^\n]*exclusion|--no-verify\b|pip\s+install[^\n]*--break-system-packages", re.I),
     "tắt/giảm bảo mật"),
    (re.compile(r"\bcurl\b[^\n]*\s-[a-z]*k[a-z]*\b(?!\w)", re.I), "curl -k (bỏ kiểm chứng chứng chỉ)"),
    (re.compile(r"(?:>>?|\btee(?:\s+-a)?|\bcp\b|\bmv\b|\bmkdir(?:\s+-p)?|\bln\s+-s\w*|\binstall\b|\bcopy\b)\s+[^\n]*?"
                r"(?:(?<![\w.])/(?:etc|usr|opt|var|bin|root|home)(?:/|\b)|~/|\$HOME\b|%USERPROFILE%|\$env:USERPROFILE|"
                r"[A-Za-z]:\\(?:Windows|Program Files))", re.I),
     "ghi ra ngoài thư mục dự án (hệ thống/thư mục người dùng)"),
]
DANGER_YELLOW = [
    (re.compile(r"\bnpm\s+(?:i|install)\s+[^\n]*(?:-g\b|--global)|\byarn\s+global\b|\bpnpm\s+(?:add|i)\s+[^\n]*-g\b", re.I),
     "cài toàn cục (-g), nằm ngoài dự án"),
    (re.compile(r"\bdocker\s+run\b[^\n]*\s-v\s+/(?!\w)|docker[^\n]*/var/run/docker\.sock", re.I), "gắn thư mục gốc hoặc docker.sock vào container"),
    (re.compile(r"\b(?:curl|wget)\b", re.I), "tải nội dung từ mạng"),
    (re.compile(r"\beval\b|\bsh\s+-c\b|\bbash\s+-c\b", re.I), "chạy chuỗi lệnh động"),
    (re.compile(r"--force\b|\s-f\s+origin|--hard\b", re.I), "cờ cưỡng bức (--force/--hard)"),
]

_SECRET_VAL_RE = re.compile(r"((?:api[_-]?key|token|secret|password|passwd|authorization|bearer)\"?\s*[:=]\s*\"?)(?!<)((?:Bearer\s+)?[^\s\",}]+)", re.I)


def _che(s):
    """Che gia tri nhay cam (khong in khoa)."""
    s = _SECRET_VAL_RE.sub(lambda m: m.group(1) + "<GIA_TRI_KHOA>", s)
    s = re.sub(r"\b(sk|ak|pk|ghp|gho|xox[bap]|AIza|hf)[_-][A-Za-z0-9_\-]{8,}", "<GIA_TRI_KHOA>", s)
    s = re.sub(r"Bearer\s+[A-Za-z0-9._\-]{8,}", "Bearer <GIA_TRI_KHOA>", s)
    return s


def _tach_json_nhung(code):
    """Tach cac khoi {...} (cat ngang nhieu dong) nam xen trong khoi shell. -> (code_con_lai, [json_text])."""
    out, js, cur, depth = [], [], [], 0
    for line in code.splitlines():
        s = line.strip()
        if depth == 0 and s.startswith("{"):
            cur, depth = [line], line.count("{") - line.count("}")
            if depth <= 0:
                js.append("\n".join(cur))
                cur, depth = [], 0
            continue
        if depth > 0:
            cur.append(line)
            depth += line.count("{") - line.count("}")
            if depth <= 0:
                js.append("\n".join(cur))
                cur, depth = [], 0
            continue
        out.append(line)
    return "\n".join(out), js


def _chia_muc(text):
    """-> list (tieu_de, noi_dung)."""
    ms = list(_H2_RE.finditer(text))
    out = []
    if not ms:
        return [("", text)]
    out.append(("", text[:ms[0].start()]))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.append((m.group(1).strip(), text[m.end():end]))
    return out


def _la_muc_setup(h):
    n = bo_dau(h)
    return any(k in n for k in ("setup", "cai dat", "cai tung buoc", "install", "bat dau nhanh", "quick start", "cach dung"))


def _la_muc_vi_du(h):
    n = bo_dau(h)
    return any(k in n for k in ("vi du", "example", "dung thu", "chay thu", "dung ngay", "su dung", "usage", "demo"))


_LENH_QUEN = {"git", "npm", "npx", "pnpm", "yarn", "bun", "bunx", "pip", "pip3", "pipx", "python", "python3", "py", "node",
              "docker", "docker-compose", "podman", "curl", "wget", "claude", "uv", "uvx", "cd", "export", "set", "setx",
              "cp", "mv", "mkdir", "brew", "apt", "apt-get", "sudo", "bash", "sh", "make", "go", "cargo", "openclaw",
              "hermes", "ollama", "ffmpeg", "powershell", "pwsh", "code", "unzip", "tar", "chmod", "ln", "rm", "copy",
              "winget", "choco", "scoop", "iwr", "irm", "iex", "gemini", "cat", "echo", "source", "pm2", "systemctl"}


def _la_muc_agent_int(h):
    return "agent integration" in bo_dau(h)


def _gop_dong(code):
    lines = []
    cur = ""
    for raw in code.splitlines():
        l = raw.rstrip()
        if not l.strip():
            if cur:
                lines.append(cur)
                cur = ""
            continue
        s = l.strip()
        if s.startswith("#") and not s.startswith("#!"):
            continue
        if s.startswith("//"):
            continue
        s = re.sub(r"^(?:\$|PS>|PS [^>]*>|>)\s+", "", s)
        if s.endswith("\\") or s.endswith("`") and not s.endswith("``"):
            cur += s[:-1].strip() + " "
            continue
        cur += s
        lines.append(cur)
        cur = ""
    if cur:
        lines.append(cur)
    return lines


_ENV_SET_RE = re.compile(
    r"^(?:export\s+|set\s+|setx\s+|\$env:)([A-Za-z_][A-Za-z0-9_]*)\s*[= ]\s*")
_ENV_PREFIX_RE = re.compile(r"^([A-Z][A-Z0-9_]{2,})=\S*\s+\S+")
_DOTENV_RE = re.compile(r"^([A-Z][A-Z0-9_]{2,})\s*=")


def _phan_loai(cmd):
    c = cmd.strip()
    low = c.lower()
    low = re.sub(r"^sudo\s+", "", low)
    if _ENV_SET_RE.match(c):
        return "dat-bien-moi-truong"
    if re.match(r"^(?:git\s+clone|cp\b|copy\b|mv\b|move\b|mkdir\b|xcopy\b|robocopy\b|unzip\b|tar\b|ln\b|new-item\b|wget\b|curl\b[^\n|]*\s-[a-z]*o\b|git\s+submodule|git\s+pull)", low):
        return "chep-file"
    if re.match(r"^(?:pip3?\s+install|python3?\s+-m\s+pip\s+install|py\s+-m\s+pip|pipx\s+install|uv\s+(?:pip|tool|add|sync)|uvx\b|"
                r"npm\s+(?:i|install|ci)\b|npx\b|pnpm\s+(?:add|i|install|dlx)|yarn\s+(?:add|install|dlx)?|bun\s+(?:add|install|x)|bunx\b|"
                r"cargo\s+install|go\s+install|brew\s+install|apt(?:-get)?\s+install|winget\s+install|choco\s+install|scoop\s+install|gem\s+install|"
                r"poetry\s+(?:add|install)|conda\s+install)", low):
        return "cai-goi"
    if re.match(r"^(?:docker|docker-compose|podman)\b", low):
        return "chay-docker"
    if re.match(r"^(?:claude\s+mcp\s+add|claude\s+plugin|code\s+--add-mcp|openclaw\b|hermes\b|gemini\s+mcp)", low):
        return "sua-cau-hinh"
    if _ENV_PREFIX_RE.match(c):
        return "dat-bien-moi-truong"
    if re.match(r"^cd\b", low):
        return "dieu-huong"
    return "lenh-khac"


def _ten_bien(cmd):
    m = _ENV_SET_RE.match(cmd.strip())
    if m:
        return m.group(1)
    m = _ENV_PREFIX_RE.match(cmd.strip())
    if m:
        return m.group(1)
    return None


def _cong_cu_can(cmd, loai):
    low = re.sub(r"^sudo\s+", "", cmd.strip().lower())
    out = []
    first = low.split()[0] if low.split() else ""
    if loai == "dat-bien-moi-truong":
        return out
    mp = {"git": "git", "npm": "npm", "npx": "node", "node": "node", "pnpm": "node", "yarn": "node", "bun": "node",
          "pip": "pip", "pip3": "pip", "pipx": "pip", "python": "python", "python3": "python", "py": "python",
          "docker": "docker", "docker-compose": "docker", "podman": "docker", "ffmpeg": "ffmpeg", "uv": "python", "uvx": "python"}
    if first in mp:
        out.append(mp[first])
    if first in ("npm", "npx", "pnpm", "yarn") and "node" not in out:
        out.append("node")
    if re.search(r"\bffmpeg\b", low) and "ffmpeg" not in out:
        out.append("ffmpeg")
    return out


def _quet_nguy_hiem(text):
    do, vang = [], []
    for rx, mota in DANGER_RED:
        if rx.search(text):
            do.append(mota)
    for rx, mota in DANGER_YELLOW:
        if rx.search(text):
            if mota == "tải nội dung từ mạng" and do:
                continue
            vang.append(mota)
    return do, vang


def _buoc_tu_json(code, nguon_muc):
    """Khoi json -> buoc 'sua-cau-hinh' neu la cau hinh MCP / env. Tra (buoc|None, ten_bien)."""
    names = []
    txt = code.strip()
    try:
        obj = json.loads(re.sub(r"(?m)^[ \t]*//.*$", "", txt))
    except Exception:
        obj = None
    flat = txt
    if obj is not None:
        def walk(o, path=""):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "env" and isinstance(v, dict):
                        names.extend(str(x) for x in v.keys())
                    if k == "headers" and isinstance(v, dict):
                        for hk in v:
                            if re.search(r"auth|key|token", hk, re.I):
                                names.append("header:" + hk)
                    walk(v, path + "/" + str(k))
            elif isinstance(o, list):
                for v in o:
                    walk(v, path)
        walk(obj)
        is_mcp = isinstance(obj, dict) and any(k in obj for k in ("mcpServers", "servers", "mcp"))
        if not is_mcp and not names:
            return None, []
    else:
        is_mcp = "mcpServers" in txt
        if not is_mcp:
            return None, []
        names.extend(re.findall(r"\"([A-Z][A-Z0-9_]{2,})\"\s*:", txt))
    hien = _che(txt)
    return {"loai": "sua-cau-hinh", "lenh": hien, "kieu": "json", "nguon_muc": nguon_muc,
            "mo_ta": "Thêm khối cấu hình MCP vào file cấu hình của vessel (sửa file cấu hình)."}, names


def _doan_ten_goi(cmd):
    toks = cmd.split()
    skip = {"install", "i", "add", "-y", "--yes", "-g", "--global", "-U", "--upgrade", "-r", "-e", "npx", "npm", "pip", "pip3",
            "python", "python3", "-m", "pnpm", "yarn", "uv", "uvx", "pipx", "dlx", "x", "bunx", "bun", "sudo", "py"}
    for t in toks:
        if t.startswith("-") or t in skip:
            continue
        return t
    return None


def _go_cai(buoc):
    """Goi y go cai tu 1 buoc. Chi la van ban, KHONG chay."""
    c = buoc.get("lenh", "")
    low = c.lower()
    l = buoc["loai"]
    if l == "cai-goi":
        pkg = _doan_ten_goi(c)
        if re.search(r"\bpip3?\b|\bpipx\b|\buv\s+pip", low) and pkg:
            return "pip uninstall %s" % pkg
        if re.search(r"\bnpm\b|\bpnpm\b|\byarn\b", low) and pkg and "npx" not in low:
            return "npm uninstall %s" % pkg
        if low.startswith("npx") or low.startswith("uvx"):
            return "npx/uvx chạy tạm, không cài lâu dài; xoá cache nếu cần (người tự làm)"
        return "gỡ gói '%s' bằng trình quản lý gói tương ứng" % (pkg or "?")
    if l == "chep-file":
        if low.startswith("git clone"):
            m = re.findall(r"\S+", c)
            d = m[-1] if len(m) > 3 and not m[-1].startswith("http") else (m[2].rstrip("/").split("/")[-1].replace(".git", "") if len(m) > 2 else "?")
            return "xoá thư mục '%s' (người tự làm, kiểm kỹ đường dẫn trước khi xoá)" % d
        return "xoá/khôi phục file đã chép (người tự làm, sao lưu trước)"
    if l == "chay-docker":
        if "compose" in low or "docker-compose" in low:
            return "docker compose down (thêm -v nếu muốn xoá cả dữ liệu - cần người duyệt)"
        return "docker stop + docker rm container đã tạo (người tự làm)"
    if l == "sua-cau-hinh":
        m = re.search(r"claude\s+mcp\s+add\s+(?:--\S+\s+\S+\s+)*([\w\-]+)", c)
        if m:
            return "claude mcp remove %s" % m.group(1)
        return "khôi phục file cấu hình từ bản sao lưu (sao lưu trước khi sửa)"
    if l == "dat-bien-moi-truong":
        return "bỏ biến môi trường '%s' (xoá khỏi .env/profile)" % (_ten_bien(c) or "?")
    return None


def _vi_du_entry(text):
    for h, body in _chia_muc(text):
        if _la_muc_vi_du(h):
            b = body.strip()
            if b:
                return re.sub(r"\s+", " ", b)[:500]
    return None


def install_plan(id, *, machine=None, repo_root=None):
    """KE HOACH cai - KHONG BAO GIO thuc thi gi. Doc entry goc, trich lenh, kiem may, gan co rui ro."""
    idx = _index(repo_root)
    r = _tim_muc(idx, id)
    root = _repo(repo_root)
    if machine is None:
        machine = machine_profile()
    p = root / r.get("duong_dan", "")
    plan = {
        "id": r["id"], "ten": r.get("ten"), "loai_muc": r.get("loai"),
        "chua_chay_that": True,
        "thong_bao": "CHƯA CHẠY THẬT - đây chỉ là kế hoạch đọc từ entry. Không có lệnh nào được thực thi. "
                     "Cần người duyệt trước khi cài.",
        "nguon": r.get("duong_dan"), "doc_entry_goc": p.is_file(),
        "buoc": [], "dieu_kien_tien_quyet": {}, "bien_moi_truong": [], "co_rui_ro": [], "co_do": [],
        "muc_duyet": {}, "kiem_tra": {}, "go_cai_dat": [], "canh_bao": [],
        "lan_ranh_do": ["AI không tự chi tiền", "AI không tự publish public content", "AI không tự cam kết với khách"],
    }
    text = ""
    if p.is_file():
        text = p.read_text(encoding="utf-8", errors="replace")
    else:
        plan["canh_bao"].append("Không tìm thấy entry gốc (%s) - không lập được bước cài." % r.get("duong_dan"))

    buoc = []
    ten_bien = []
    cong_cu = []

    def them_buoc(loai, lenh, nguon_muc, kieu="shell", mo_ta=None, bien=None):
        do, vang = _quet_nguy_hiem(lenh)
        b = {"loai": loai, "lenh": _che(lenh), "kieu": kieu, "nguon_muc": nguon_muc,
             "co_do": do, "canh_bao_vang": vang, "can_nguoi_doc_ky": bool(do), "chua_chay": True}
        if mo_ta:
            b["mo_ta"] = mo_ta
        buoc.append(b)
        return b

    if text:
        sections = _chia_muc(text)
        has_setup = any(_la_muc_setup(h) and _FENCE_RE.search(b) for h, b in sections)
        for h, body in sections:
            if _la_muc_agent_int(h):
                continue
            setup = _la_muc_setup(h)
            vidu = _la_muc_vi_du(h)
            if has_setup and not (setup or vidu):
                continue
            if not has_setup and not (setup or vidu) and h and not re.search(r"(luu y|loi thuong|canh bao|license|bao mat)", bo_dau(h)):
                pass
            for m in _FENCE_RE.finditer(body):
                lang = (m.group(1) or "").lower()
                code = m.group(2)
                nm = h or "(đầu file)"
                def xu_ly_json(jtxt, nm=nm, setup=setup, vidu=vidu):
                    b, names = _buoc_tu_json(jtxt, nm)
                    if b:
                        do, vang = _quet_nguy_hiem(b["lenh"])
                        b.update({"co_do": do, "canh_bao_vang": vang, "can_nguoi_doc_ky": bool(do), "chua_chay": True})
                        if vidu and not setup:
                            b["kieu"] = "json (ví dụ)"
                        buoc.append(b)
                        ten_bien.extend(names)
                        mm = re.search(r"\"command\"\s*:\s*\"(\w+)\"", jtxt)
                        if mm and mm.group(1) in ("npx", "node", "python", "python3", "uvx", "docker"):
                            cong_cu.append({"npx": "node", "uvx": "python", "python3": "python"}.get(mm.group(1), mm.group(1)))

                if lang in ("json", "jsonc", "json5") or code.lstrip()[:1] in ("{", "["):
                    xu_ly_json(code)
                    continue
                json_nhung = []
                if lang in ("bash", "sh", "shell", "zsh", "console", "terminal", ""):
                    code, json_nhung = _tach_json_nhung(code)
                if lang in ("bash", "sh", "shell", "zsh", "console", "powershell", "ps1", "pwsh", "cmd", "bat", "batch", "terminal", "env", "dotenv", ""):
                    if lang in ("env", "dotenv"):
                        for l in _gop_dong(code):
                            mm = _DOTENV_RE.match(l)
                            if mm:
                                ten_bien.append(mm.group(1))
                                buoc.append({"loai": "dat-bien-moi-truong", "lenh": "%s=<GIA_TRI_KHOA>" % mm.group(1), "kieu": "env",
                                             "nguon_muc": nm, "co_do": [], "canh_bao_vang": [], "can_nguoi_doc_ky": False, "chua_chay": True})
                        continue
                    lines = _gop_dong(code)
                    # khoi chi co 1 URL => gia tri cau hinh, khong phai lenh
                    if len(lines) == 1 and re.match(r"^https?://\S+$", lines[0]):
                        buoc.append({"loai": "sua-cau-hinh", "lenh": lines[0], "kieu": "url", "nguon_muc": nm,
                                     "mo_ta": "Giá trị URL cần dán vào giao diện/cấu hình (không phải lệnh).",
                                     "co_do": [], "canh_bao_vang": [], "can_nguoi_doc_ky": False, "chua_chay": True})
                        lines = []
                    for l in lines:
                        if lang == "":
                            # khoi khong gan ngon ngu: chi nhan dong bat dau bang lenh quen thuoc (tranh nhan nham cau mau)
                            w0 = l.split()[0].lower() if l.split() else ""
                            if not (w0 in _LENH_QUEN or w0.startswith("./") or _ENV_SET_RE.match(l) or _ENV_PREFIX_RE.match(l)):
                                continue
                        loai = _phan_loai(l)
                        if vidu and not setup and loai in ("lenh-khac", "dieu-huong"):
                            kieu = "dung-thu"
                        else:
                            kieu = "shell"
                        nb = _ten_bien(l)
                        if nb:
                            ten_bien.append(nb)
                        for t in _cong_cu_can(l, loai):
                            cong_cu.append(t)
                        b = them_buoc(loai, l, nm, kieu=kieu)
                        if loai == "lenh-khac" and kieu == "dung-thu":
                            b["loai"] = "lenh-dung-thu"
                    for j in json_nhung:
                        xu_ly_json(j)
                elif lang in ("python", "py", "javascript", "js", "typescript", "ts", "yaml", "yml", "toml") and (setup or vidu):
                    # ma vi du: ghi nhan, khong coi la lenh cai
                    do, vang = _quet_nguy_hiem(code)
                    buoc.append({"loai": "ma-vi-du", "lenh": _che(code.strip())[:400], "kieu": lang, "nguon_muc": nm,
                                 "mo_ta": "Mã ví dụ (đọc, không phải lệnh cài).", "co_do": do, "canh_bao_vang": vang,
                                 "can_nguoi_doc_ky": bool(do), "chua_chay": True})
        # bien moi truong ten thuong gap trong van ban (bo ten mau YOUR_...)
        for v in re.findall(r"\b([A-Z][A-Z0-9]+(?:_[A-Z0-9]+)*_(?:API_KEY|TOKEN|SECRET|KEY))\b", text):
            if not v.startswith(("YOUR_", "EXAMPLE_", "MY_")):
                ten_bien.append(v)

    # skill thuan van ban: buoc chep file
    loai = r.get("loai", "")
    if loai.startswith("skill") and p.is_file():
        folder = str(Path(r["duong_dan"]).parent).replace("\\", "/")
        src = folder if r["duong_dan"].endswith("SKILL.md") else r["duong_dan"]
        buoc.insert(0, {"loai": "chep-file", "lenh": "(sao chép) %s -> thư mục skills của vessel (xem agents/*-GUIDE.md của vessel)" % src,
                        "kieu": "mo-ta", "nguon_muc": "suy ra từ loại muc", "co_do": [], "canh_bao_vang": [],
                        "can_nguoi_doc_ky": False, "chua_chay": True,
                        "mo_ta": "Skill là file Markdown: chép thư mục skill vào nơi vessel đọc skill. Chưa kiểm cách vessel nạp."})
    if text and not [b for b in buoc if b["loai"] not in ("ma-vi-du",)]:
        plan["canh_bao"].append("Không trích được lệnh cài từ entry (không có khối lệnh trong mục Setup/Ví dụ); đọc entry gốc.")
    elif text and not any(_la_muc_setup(h) and _FENCE_RE.search(b) for h, b in _chia_muc(text)):
        plan["canh_bao"].append("Entry không có mục Setup/Cài đặt chứa khối lệnh; lệnh lấy từ mục Ví dụ - cần người đọc kỹ.")

    # danh so
    for i, b in enumerate(buoc, 1):
        b["so"] = i
    plan["buoc"] = buoc

    # dieu kien tien quyet
    can = []
    for t in cong_cu:
        if t and t not in can:
            can.append(t)
    needs = _csv(r.get("needs"))
    if "docker" in needs and "docker" not in can:
        can.append("docker")
    if re.search(r"\bffmpeg\b", text, re.I) and "ffmpeg" not in can and ("ffmpeg" in bo_dau(r.get("tom_tat", "")) or "ffmpeg" in bo_dau(r.get("use_when", "")) or "video-render" in _caps(r)):
        can.append("ffmpeg")
    tools_may = (machine or {}).get("cong_cu", {})
    thieu = [t for t in can if not (tools_may.get(t) or {}).get("co")]
    plan["dieu_kien_tien_quyet"] = {
        "can": can, "thieu": thieu,
        "co": {t: bool((tools_may.get(t) or {}).get("co")) for t in can},
        "can_khac": [x for x in ("vps", "gpu", "docker", "browser", "claude-code-only") if x in needs and x != "docker"],
    }
    if "gpu" in needs:
        plan["dieu_kien_tien_quyet"]["thieu"].append("gpu (không kiểm được tự động)")
    # bien khoa
    seen = []
    for n in ten_bien:
        if n not in seen:
            seen.append(n)
    dang_dat = set((machine or {}).get("bien_khoa_dang_dat") or [])
    plan["bien_moi_truong"] = [{"ten": n, "da_dat": (n in dang_dat) or (n in os.environ if not n.startswith("header:") else False)} for n in seen]

    # co rui ro
    rr = []
    lic = (r.get("license") or "").strip()
    if not lic or lic.lower() in ("unknown", "?"):
        rr.append({"loai": "license", "noi_dung": "License chưa ghi trong kho - kiểm trước khi dùng cho khách."})
    elif re.search(r"agpl|gpl|non-?commercial|cc-by-nc|sspl|busl|proprietary|custom|elastic", lic, re.I):
        rr.append({"loai": "license", "noi_dung": "License hạn chế (%s) - đọc điều khoản trước khi dùng thương mại." % lic})
    if "tra-phi" in needs or re.search(r"tốn tiền|ton tien", (r.get("rui_ro") or ""), re.I):
        rr.append({"loai": "ton-tien", "noi_dung": "Có thể phát sinh chi phí (dịch vụ trả phí/credit)."})
    blob = bo_dau(" ".join([text, r.get("rui_ro", ""), r.get("skip_if", "")]))
    if re.search(r"\btos\b|terms of service|dieu khoan|vi pham.*(dieu khoan|chinh sach)|unofficial|khong chinh thuc|ban tai khoan|bi khoa tai khoan|rate limit|robots\.txt", blob):
        rr.append({"loai": "tos", "noi_dung": "Entry nhắc điều khoản dịch vụ/giới hạn/không chính thức - kiểm ToS của nền tảng đích."})
    if re.search(r"bao mat|security|credential|ro ri|lo khoa|prompt injection|quyen rong|toan quyen|full access", blob) or "bảo mật" in (r.get("rui_ro") or "").lower():
        rr.append({"loai": "bao-mat", "noi_dung": "Entry/nhãn nhắc đến bảo mật, quyền truy cập hoặc khoá - đọc phần Lưu ý."})
    if re.search(r"\b(alpha|beta|preview|experimental|early access|pre-?release)\b|thu nghiem|ban thu", blob + " " + bo_dau(r.get("ten", ""))):
        rr.append({"loai": "preview", "noi_dung": "Nhắc bản alpha/beta/preview/thử nghiệm - API có thể đổi."})
    if "api-key" in needs:
        rr.append({"loai": "khoa-api", "noi_dung": "Cần khoá/token API - tạo, đặt, đổi khoá là việc L3 (CEO)."})
    if "vps" in needs:
        rr.append({"loai": "vps", "noi_dung": "Cần VPS/máy chủ."})
    if "gpu" in needs:
        rr.append({"loai": "gpu", "noi_dung": "Cần GPU."})
    if "claude-code-only" in needs:
        rr.append({"loai": "pham-vi", "noi_dung": "Chỉ chạy trong Claude Code."})
    if r.get("adoption") == "can-ha-tang":
        rr.append({"loai": "ha-tang", "noi_dung": "adoption = can-ha-tang (VPS/docker/DB/nhiều bước)."})
    if r.get("curation_status") != "da-doc-entry-goc":
        rr.append({"loai": "nhan", "noi_dung": "Nhãn chưa dựa trên đọc nguyên entry (%s)." % r.get("curation_status")})
    if _audit_usable(r) is False:
        rr.append({"loai": "audit", "noi_dung": "Audit tự động: không dùng được."})
    plan["co_rui_ro"] = rr

    co_do = []
    for b in buoc:
        for d in b["co_do"]:
            co_do.append({"buoc": b["so"], "ly_do": d, "lenh": b["lenh"], "can_nguoi_doc_ky": True})
    plan["co_do"] = co_do

    # muc duyet theo DECISION-MATRIX
    level, why = 1, ["cài tool nội bộ/dự án: L1 (ghi log)"]
    if "tra-phi" in needs or any(x["loai"] == "ton-tien" for x in rr):
        level = max(level, 2)
        why.append("có chi tiền > 0đ (trả phí/credit) -> L2 (DECISION-MATRIX, trục Tiền)")
    if (machine or {}).get("vps_co_khach") or (isinstance(machine, dict) and machine.get("dich") == "vps-co-khach"):
        level = max(level, 2)
        why.append("cài trên VPS có khách -> L2 (chạm production)")
    elif "vps" in needs:
        why.append("cần VPS: nếu VPS đang có khách dùng thì tối thiểu L2")
    if co_do:
        level = max(level, 2)
        why.append("có lệnh nguy hiểm cờ đỏ -> tối thiểu L2 và người phải đọc kỹ")
    if "api-key" in needs or plan["bien_moi_truong"]:
        level = max(level, 3)
        why.append("chạm khoá/credential (đặt/đổi khoá, cấp quyền) -> L3: hỏi CEO TRƯỚC khi làm")
    if r.get("curation_status") != "da-doc-entry-goc" and level < 2:
        level = 2
        why.append("nhãn chưa chắc (không phải đã-đọc-entry-gốc) -> nâng lên L2 (không chắc thì coi là mức cao hơn)")
    plan["muc_duyet"] = {"muc": "L%d" % level, "ly_do": why,
                         "ghi_chu": "Không chắc mức nào thì coi là mức cao hơn. Mọi hành động đăng bài/gửi tin/chi tiền sau khi cài vẫn đi qua lằn ranh đỏ."}

    # kiem tra PASS/FAIL
    kt = {"tieu_chi": "PASS nếu lệnh kiểm chạy xong không lỗi VÀ đầu ra khớp ví dụ trong entry; FAIL nếu lỗi, thiếu công cụ, hoặc kết quả khác ví dụ (ghi lý do, bỏ mục đó).",
          "vi_du_trong_entry": _vi_du_entry(text) if text else None, "lenh_goi_y": []}
    goi_y = []
    for b in buoc:
        l = b["loai"]
        c = b["lenh"]
        low = c.lower()
        if l == "cai-goi" and not goi_y:
            pkg = _doan_ten_goi(c)
            if re.search(r"\bpip3?\b|\bpipx\b|uv\s+pip", low) and pkg:
                goi_y.append("pip show %s" % pkg)
            elif low.startswith("npx") and pkg:
                goi_y.append("npx -y %s --help" % pkg)
            elif re.search(r"\bnpm\b", low) and pkg:
                goi_y.append("npm ls %s" % pkg)
        if l == "chay-docker" and not goi_y:
            goi_y.append("docker --version")
        if l == "sua-cau-hinh" and "claude mcp add" in low and not goi_y:
            goi_y.append("claude mcp list")
        if l == "chep-file" and low.startswith("git clone") and not goi_y:
            goi_y.append("git --version")
    if not goi_y and can:
        goi_y.append("%s --version" % can[0])
    kt["lenh_goi_y"] = goi_y
    plan["kiem_tra"] = kt

    go = []
    for b in reversed(buoc):
        g = _go_cai(b)
        if g and g not in go:
            go.append(g)
    if loai.startswith("skill") and not go:
        go.append("xoá thư mục skill đã chép khỏi thư mục skills của vessel")
    plan["go_cai_dat"] = go
    plan["canh_bao"].append(CANH_BAO_CHUNG)
    if r.get("skip_if") and r.get("skip_if") != "unknown":
        plan["canh_bao"].append("Bỏ qua nếu: " + r["skip_if"])
    return plan

# ---------------------------------------------------------------- so (gap/usage)

def _o(s):
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "/").strip()


def gap_line(query, du_an="", ghi_chu="", repo_root=None):
    """1 dong bang Markdown cho catalog/GAP-LOG.md.
    Cot: Ngay | Kha nang can | Du an/khach | Da tra | Vi sao chua du | Trang thai."""
    pq = phan_tich_truy_van(query)
    caps = ", ".join(c["capability"] for c in pq["capabilities"]) or "(không khớp capability nào)"
    kw = " ".join(pq["tu_khoa"][:8])
    da_tra = "thu_kho tim; capability: %s; từ khoá: %s" % (caps, kw)
    vi_sao = _o(ghi_chu) or "(chưa ghi lý do - điền tay)"
    return "| %s | %s | %s | %s | %s | mở |" % (
        datetime.date.today().isoformat(), _o(query), _o(du_an) or "-", _o(da_tra), vi_sao)


def usage_line(id, du_an, ket_qua, tiet_kiem, ghi_chu, repo_root=None):
    """1 dong bang Markdown cho catalog/USAGE-LOG.md. ket_qua chi nhan dung duoc/phai sua/bo.
    Cot: Ngay | Muc (duong dan) | Du an/khach | Ket qua | Tiet kiem duoc gi | Ghi chu."""
    k = bo_dau(ket_qua).strip()
    if k not in KET_QUA_HOP_LE:
        raise ValueError("ket_qua '%s' không hợp lệ: chỉ nhận 'dùng được' / 'phải sửa' / 'bỏ'." % ket_qua)
    idx = _index(repo_root)
    r = _tim_muc(idx, id)
    kq = KET_QUA_HOP_LE[k]
    if kq == "dùng được" and not _o(tiet_kiem):
        raise ValueError("Cột 'Tiết kiệm được gì' phải ghi bằng giờ hoặc việc cụ thể khi kết quả là 'dùng được'.")
    if not _o(du_an):
        raise ValueError("Phải ghi dự án/khách thật; kho không nhận dòng dùng thử cho biết.")
    return "| %s | %s | %s | %s | %s | %s |" % (
        datetime.date.today().isoformat(), r["duong_dan"], _o(du_an), kq, _o(tiet_kiem) or "-", _o(ghi_chu) or "-")

# ---------------------------------------------------------------- recommend

def _canh_bao_muc(it):
    w = []
    if it["curation_status"] == "da-doc-dau-entry":
        w.append("mới đọc phần đầu entry")
    if it["curation_status"] == "chua-gan-nhan":
        w.append("chưa gắn nhãn")
    needs = _csv(it["needs"])
    vf = _csv(it["vessel_fit"])
    if "claude-code-only" in needs or vf == ["claude-code"]:
        w.append("chỉ chạy trong Claude Code")
    if "tra-phi" in needs:
        w.append("tốn tiền -> L2")
    if "api-key" in needs:
        w.append("cần khoá API -> L3")
    if "gpu" in needs:
        w.append("cần GPU")
    if "vps" in needs:
        w.append("cần VPS")
    if it["adoption"] == "can-ha-tang":
        w.append("cần hạ tầng")
    return w


def recommend(brief, *, vessel=None, exclude_needs=(), per_need=1, repo_root=None):
    """Goi y cho 1 yeu cau dai: tach thanh kha nang, moi kha nang 1 chinh + 1 du phong (khac dup_group), HONG neu thieu."""
    idx = _index(repo_root)
    pq = phan_tich_truy_van(brief)
    excl = tuple(set(exclude_needs or ()) | set(pq["exclude_needs_ngam"]))
    kha_nang, hong, canh_bao = [], [], []
    # tach yeu cau dai thanh cac doan; moi kha nang chi tra cuu bang cac doan nhac toi no
    # (tranh tu khoa cua kha nang nay lam nhieu viec xep hang kha nang khac)
    doan_theo_cap = {}
    for seg in re.split(r"[,;:\n.•]+|\s[-–]\s|\bvà\b|\band\b|\bvới\b", brief):
        seg = seg.strip()
        if len(seg) < 3:
            continue
        for c in phan_tich_truy_van(seg)["capabilities"]:
            doan_theo_cap.setdefault(c["capability"], []).append(seg)
    nhom_cap = [c for c in pq["capabilities"] if c["manh"]]
    if not nhom_cap:
        nhom_cap = pq["capabilities"] if pq["capabilities"] else []
    if not nhom_cap:
        # khong co capability: thu khop van ban chat che
        res = search(brief, vessel=vessel, exclude_needs=excl, top=3, repo_root=repo_root)
        chat = [x for x in res if x["bac_khop"] == 0]
        # can phu >= 50% trong so tu khoa: tinh lai
        sc = _score_items(idx, pq)
        ok = []
        for x in chat:
            n = idx["ids"].index(x["id"])
            if sc[n]["coverage"] >= 0.6:
                ok.append(x)
        if ok:
            kha_nang.append({"capability": None, "ly_do_phat_hien": "khớp văn bản (không có capability rõ)",
                             "chinh": ok[:per_need], "du_phong": ok[per_need] if len(ok) > per_need else None})
        else:
            hong.append({"mo_ta": brief.strip(), "ly_do": "Không khớp capability nào và không có mục nào khớp văn bản đủ chặt",
                         "hanh_dong": "Ghi catalog/GAP-LOG.md (gap_line), không bịa ứng viên."})
    for c in nhom_cap[:8]:
        cap = c["capability"]
        q_cap = " ; ".join(doan_theo_cap.get(cap) or [brief])
        res = search(q_cap, vessel=vessel, exclude_needs=excl, capability=cap, top=12, repo_root=repo_root)
        if not res:
            hong.append({"capability": cap, "mo_ta": "Có nhu cầu '%s' nhưng kho không có ứng viên (đã lọc vessel/needs/adoption)." % cap,
                         "hanh_dong": "Ghi catalog/GAP-LOG.md, không bịa."})
            continue
        chinh = res[:max(1, per_need)]
        used = {x["dup_group"] for x in chinh if x["dup_group"]}
        du = None
        for x in res[len(chinh):]:
            if not x["dup_group"] or x["dup_group"] not in used:
                du = x
                break
        kha_nang.append({"capability": cap, "ly_do_phat_hien": "cụm: " + ", ".join(c["cum_khop"][:4]),
                         "chinh": chinh, "du_phong": du})
    for k in kha_nang:
        for it in list(k["chinh"]) + ([k["du_phong"]] if k["du_phong"] else []):
            for w in _canh_bao_muc(it):
                s = "%s: %s" % (it["id"], w)
                if s not in canh_bao:
                    canh_bao.append(s)
    canh_bao.append(CANH_BAO_CHUNG)
    canh_bao.append("Mở entry gốc đọc skip_if + mục Lưu ý trước khi dùng; không cài khi chưa có người duyệt.")
    them = goi_y_chua_nhan(brief, vessel=vessel, exclude_needs=excl, top=3, repo_root=repo_root)
    return {"brief": brief, "vessel": vessel, "exclude_needs": list(excl), "kha_nang": kha_nang, "hong": hong,
            "them_chua_gan_nhan": them,
            "canh_bao": canh_bao, "phat_hien": [c["capability"] for c in pq["capabilities"]]}

# ---------------------------------------------------------------- CLI

def _in(s=""):
    print(s)


def _in_ket_qua(items, pq=None):
    if pq:
        caps = ", ".join("%s (%s)" % (c["capability"], "/".join(c["cum_khop"][:2])) for c in pq["capabilities"]) or "(không phát hiện)"
        _in("Khả năng phát hiện: " + caps)
        if pq["exclude_needs_ngam"]:
            _in("Tự bỏ mục cần: " + ", ".join(pq["exclude_needs_ngam"]))
    if not items:
        _in("Không có ứng viên đủ tốt. Ghi vào catalog/GAP-LOG.md (python tools/thu_kho.py ghi-gap ...), đừng bịa.")
        return
    for i, it in enumerate(items, 1):
        _in("%d. %s  -  %s" % (i, it["id"], it["ten"]))
        _in("   điểm %s | %s | độ tin cậy nhãn: %s | adoption: %s | cần: %s | vessel: %s" % (
            it["score"], it["curation_status"], it["confidence"] or "-", it["adoption"] or "-", it["needs"] or "-", it["vessel_fit"] or "(rỗng=chưa rõ)"))
        _in("   Khớp: " + it["ly_do_khop"])
        if it["use_when"]:
            _in("   Dùng khi: " + it["use_when"])
        if it["skip_if"]:
            _in("   Bỏ qua nếu: " + it["skip_if"])
        for g in it["ghi_chu"]:
            _in("   * " + g)
        _in("   Đọc entry gốc: " + it["duong_dan"])
    _in("")
    _in("Lưu ý: " + CANH_BAO_CHUNG)


def _in_card(c):
    _in("%s  -  %s" % (c["id"], c["ten"]))
    for k in ("loai", "capability", "adoption", "needs", "vessel_fit", "curation_status", "confidence", "dup_group",
              "license", "rui_ro", "diem", "xac_minh", "cap_nhat"):
        _in("  %-16s %s" % (k, c.get(k) if c.get(k) not in (None, "") else "-"))
    for k in ("tom_tat", "use_when", "skip_if", "evidence"):
        _in("  %s: %s" % (k, c.get(k) or "-"))
    _in("  audit: " + (json.dumps(c["audit"], ensure_ascii=False) if c["audit"] else "(không có audit.json)"))
    _in("  nguồn: %s (%s)" % (c["duong_dan"], "tồn tại" if c["entry_ton_tai"] else "KHÔNG THẤY FILE"))
    for w in c["canh_bao"]:
        _in("  ! " + w)


def _in_plan(p):
    _in("=" * 70)
    _in(p["thong_bao"])
    _in("=" * 70)
    _in("Mục: %s - %s" % (p["id"], p["ten"]))
    _in("Entry gốc: %s (%s)" % (p["nguon"], "đã đọc" if p["doc_entry_goc"] else "KHÔNG THẤY"))
    _in("Mức duyệt cần: %s" % p["muc_duyet"]["muc"])
    for w in p["muc_duyet"]["ly_do"]:
        _in("   - " + w)
    dk = p["dieu_kien_tien_quyet"]
    _in("Điều kiện tiên quyết: cần %s | THIẾU: %s" % (", ".join(dk["can"]) or "-", ", ".join(dk["thieu"]) or "không" ))
    if dk.get("can_khac"):
        _in("   Yêu cầu khác (nhãn): " + ", ".join(dk["can_khac"]))
    if p["bien_moi_truong"]:
        _in("Biến môi trường/khoá (chỉ tên): " + ", ".join("%s[%s]" % (b["ten"], "đã đặt" if b["da_dat"] else "chưa đặt") for b in p["bien_moi_truong"]))
    _in("Cờ rủi ro:")
    for x in p["co_rui_ro"] or [{"loai": "-", "noi_dung": "không có cờ nào được phát hiện (không có nghĩa là an toàn)"}]:
        _in("   [%s] %s" % (x["loai"], x["noi_dung"]))
    if p["co_do"]:
        _in("CỜ ĐỎ - CẦN NGƯỜI ĐỌC KỸ:")
        for x in p["co_do"]:
            _in("   bước %d: %s -> %s" % (x["buoc"], x["ly_do"], x["lenh"]))
    _in("Các bước (CHƯA CHẠY):")
    for b in p["buoc"]:
        flag = "  <== CẦN NGƯỜI ĐỌC KỸ" if b["can_nguoi_doc_ky"] else ""
        _in("  %d. [%s] %s%s" % (b["so"], b["loai"], b["lenh"].replace("\n", "\n       "), flag))
        for v in b["canh_bao_vang"]:
            _in("       (lưu ý: %s)" % v)
    if not p["buoc"]:
        _in("  (không trích được bước nào - đọc entry gốc)")
    _in("Kiểm PASS/FAIL: " + p["kiem_tra"]["tieu_chi"])
    if p["kiem_tra"]["vi_du_trong_entry"]:
        _in("   Ví dụ trong entry: " + p["kiem_tra"]["vi_du_trong_entry"])
    for c in p["kiem_tra"]["lenh_goi_y"]:
        _in("   Lệnh kiểm gợi ý: " + c)
    if p["go_cai_dat"]:
        _in("Gỡ cài (gợi ý, người tự làm):")
        for g in p["go_cai_dat"]:
            _in("   - " + g)
    for w in p["canh_bao"]:
        _in("! " + w)
    _in("Lằn ranh đỏ: " + "; ".join(p["lan_ranh_do"]))
    _in("CHƯA CHẠY THẬT. Chờ người duyệt (%s) rồi mới cài." % p["muc_duyet"]["muc"])


def _in_may(m):
    _in("Máy: %s (%s), Python %s" % (m["he_dieu_hanh"], m["kien_truc"], m["python"]))
    for k, v in m["cong_cu"].items():
        _in("  %-8s %s" % (k, ("có  " + v.get("phien_ban", "")) if v["co"] else "KHÔNG CÓ"))
    _in("Biến khoá biết trước (chỉ có/không):")
    for k, v in m["bien_khoa_biet_truoc"].items():
        _in("  %-24s %s" % (k, "đã đặt" if v else "chưa"))
    if m["bien_khoa_dang_dat"]:
        _in("Biến giống khoá đang đặt (chỉ tên): " + ", ".join(m["bien_khoa_dang_dat"]))
    _in(m["ghi_chu"])


def _in_goi_y(g):
    _in("Yêu cầu: " + g["brief"])
    _in("Khả năng phát hiện: " + (", ".join(c for c in g["phat_hien"]) or "(không)"))
    if g["exclude_needs"]:
        _in("Tự bỏ mục cần: " + ", ".join(g["exclude_needs"]))
    _in()
    for k in g["kha_nang"]:
        _in("== %s  (%s)" % (k["capability"] or "khớp văn bản", k["ly_do_phat_hien"]))
        for it in k["chinh"]:
            _in("  CHÍNH     : %s - %s [%s/%s, %s]" % (it["id"], it["ten"], it["curation_status"], it["confidence"] or "-", it["needs"] or "-"))
            if it["use_when"]:
                _in("              dùng khi: " + it["use_when"])
            if it["skip_if"]:
                _in("              bỏ qua nếu: " + it["skip_if"])
        d = k["du_phong"]
        if d:
            _in("  DỰ PHÒNG  : %s - %s [%s/%s, %s]" % (d["id"], d["ten"], d["curation_status"], d["confidence"] or "-", d["needs"] or "-"))
        else:
            _in("  DỰ PHÒNG  : (không có mục khác nhóm dup_group)")
    for h in g["hong"]:
        _in("HỔNG: %s - %s" % (h.get("capability") or "yêu cầu", h["mo_ta"]))
        _in("      -> " + h["hanh_dong"])
    if g.get("them_chua_gan_nhan"):
        _in("Thêm (CHƯA GẮN NHÃN, chỉ khớp từ khoá):")
        for it in g["them_chua_gan_nhan"]:
            _in("  - %s - %s" % (it["id"], it["ten"]))
    _in()
    for w in g["canh_bao"]:
        _in("! " + w)


def _main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(prog="thu_kho", description="THỦ KHO - tra kho, gợi ý, lập kế hoạch cài (không bao giờ chạy lệnh).")
    ap.add_argument("--repo", default=None, help="gốc repo (mặc định: cha của tools/)")
    sub = ap.add_subparsers(dest="lenh")
    t = sub.add_parser("tim", help="tìm mục theo câu truy vấn")
    t.add_argument("query")
    t.add_argument("--vessel")
    t.add_argument("--bo-can", default="", help="loại mục cần: gpu,vps,docker,api-key,tra-phi...")
    t.add_argument("--top", type=int, default=5)
    t.add_argument("--capability")
    t.add_argument("--ca-chua-nhan", action="store_true", help="gồm cả mục chưa gắn nhãn")
    t.add_argument("--ca-tham-khao", action="store_true", help="gồm cả mục chỉ-tham-khảo")
    t.add_argument("--json", action="store_true")
    c = sub.add_parser("chi-tiet", help="thẻ chi tiết 1 mục")
    c.add_argument("id")
    c.add_argument("--json", action="store_true")
    k = sub.add_parser("ke-hoach-cai", help="kế hoạch cài (CHƯA CHẠY)")
    k.add_argument("id")
    k.add_argument("--vps-co-khach", action="store_true", help="cài trên VPS đang có khách (L2)")
    k.add_argument("--json", action="store_true")
    g = sub.add_parser("goi-y", help="gợi ý cho 1 mô tả dự án")
    g.add_argument("brief")
    g.add_argument("--vessel")
    g.add_argument("--bo-can", default="")
    g.add_argument("--json", action="store_true")
    gg = sub.add_parser("ghi-gap", help="tạo dòng GAP-LOG")
    gg.add_argument("query")
    gg.add_argument("--du-an", default="")
    gg.add_argument("--ghi-chu", default="")
    gg.add_argument("--ghi", action="store_true", help="nối vào catalog/GAP-LOG.md (mặc định chỉ in)")
    gu = sub.add_parser("ghi-usage", help="tạo dòng USAGE-LOG")
    gu.add_argument("id")
    gu.add_argument("--du-an", required=True)
    gu.add_argument("--ket-qua", required=True, help="dung duoc | phai sua | bo")
    gu.add_argument("--tiet-kiem", default="")
    gu.add_argument("--ghi-chu", default="")
    gu.add_argument("--ghi", action="store_true", help="nối vào catalog/USAGE-LOG.md (mặc định chỉ in)")
    m = sub.add_parser("may", help="hồ sơ máy")
    m.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if not a.lenh:
        ap.print_help()
        return 2
    root = a.repo
    try:
        if a.lenh == "tim":
            bo = [x.strip() for x in a.bo_can.split(",") if x.strip()]
            adopt_not = () if a.ca_tham_khao else ("chi-tham-khao",)
            res = search(a.query, vessel=a.vessel, exclude_needs=bo, include_unlabeled=a.ca_chua_nhan,
                         adoption_not=adopt_not, capability=a.capability, top=a.top, repo_root=root)
            them = [] if a.ca_chua_nhan else goi_y_chua_nhan(a.query, vessel=a.vessel, exclude_needs=bo, repo_root=root)
            if a.json:
                print(json.dumps({"ket_qua": res, "them_chua_gan_nhan": them}, ensure_ascii=False, indent=2))
            else:
                _in_ket_qua(res, phan_tich_truy_van(a.query))
                if them:
                    _in("")
                    _in("Thêm (CHƯA GẮN NHÃN, chỉ có mô tả - khớp từ khoá, không rõ use_when/skip_if/needs):")
                    for it in them:
                        _in("  - %s  -  %s  [%s]" % (it["id"], it["ten"], it["ly_do_khop"]))
        elif a.lenh == "chi-tiet":
            c_ = card(a.id, repo_root=root)
            print(json.dumps(c_, ensure_ascii=False, indent=2)) if a.json else _in_card(c_)
        elif a.lenh == "ke-hoach-cai":
            mp = machine_profile()
            if a.vps_co_khach:
                mp["vps_co_khach"] = True
            p_ = install_plan(a.id, machine=mp, repo_root=root)
            print(json.dumps(p_, ensure_ascii=False, indent=2)) if a.json else _in_plan(p_)
        elif a.lenh == "goi-y":
            bo = [x.strip() for x in a.bo_can.split(",") if x.strip()]
            g_ = recommend(a.brief, vessel=a.vessel, exclude_needs=bo, repo_root=root)
            print(json.dumps(g_, ensure_ascii=False, indent=2)) if a.json else _in_goi_y(g_)
        elif a.lenh == "ghi-gap":
            line = gap_line(a.query, a.du_an, a.ghi_chu, repo_root=root)
            print(line)
            if a.ghi:
                _noi(_repo(root) / "catalog" / "GAP-LOG.md", line)
        elif a.lenh == "ghi-usage":
            line = usage_line(a.id, a.du_an, a.ket_qua, a.tiet_kiem, a.ghi_chu, repo_root=root)
            print(line)
            if a.ghi:
                _noi(_repo(root) / "catalog" / "USAGE-LOG.md", line)
        elif a.lenh == "may":
            mp = machine_profile()
            print(json.dumps(mp, ensure_ascii=False, indent=2)) if a.json else _in_may(mp)
    except (KeyError, ValueError, FileNotFoundError) as e:
        print("Lỗi: %s" % (e.args[0] if e.args else e), file=sys.stderr)
        return 1
    return 0


def _noi(path, line):
    """Noi them 1 dong vao cuoi bang (chi them cuoi, theo luat cua log)."""
    txt = path.read_text(encoding="utf-8")
    if not txt.endswith("\n"):
        txt += "\n"
    path.write_text(txt + line + "\n", encoding="utf-8")
    print("(đã nối vào %s)" % path.name, file=sys.stderr)


if __name__ == "__main__":
    sys.exit(_main())
