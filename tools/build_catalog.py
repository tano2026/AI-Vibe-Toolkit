#!/usr/bin/env python3
"""Sinh DANH MỤC TRA CỨU toàn kho từ file thật (không gõ tay).

Chạy:  python3 tools/build_catalog.py
Ra:    catalog/CATALOG.csv   (import thẳng vào Notion / Google Sheets / Airtable)
       catalog/catalog.json  (cho trang tra cứu + agent)
       catalog/BY-DOMAIN.md  (bản đọc nhanh: mục nào đáng thử trước, theo lĩnh vực)

Quy ước trung thực (đọc trước khi tin các cột):
- domain  = gán TỰ ĐỘNG bằng từ khoá trên tên + tóm tắt -> có thể sai, dùng để LỌC, không phải sự thật.
- xac_minh= suy ra từ chữ trong file: "có ghi đã chạy" / "một phần" / "chưa chạy" / "đọc nguồn" / "chưa đánh giá".
            "có ghi đã chạy" = file CÓ CÂU nói đã chạy (có thể do người khác chạy). KHÔNG có nghĩa Tano Agency đã
            dùng trong dự án thật. Cột dùng thật nằm ở USAGE-LOG.md. Điểm x/10 phần lớn là điểm sau khi ĐỌC, không phải sau khi DÙNG.
- score   = chỉ lấy khi file có ghi "x/10"; không có thì để trống (KHÔNG tự chấm hộ).
- Skill dạng skills/<tên>/SKILL.md nhập hàng loạt (origin: ECC...) chỉ có mô tả ngắn, chưa ai đánh giá.
"""
import csv, json, os, re, subprocess, sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SKIP_NAMES = {"README.md", "_template.md", "_template_script.md"}

# ---------- nguồn ----------
def collect():
    items = []
    def add(path, kind):
        items.append((path, kind))
    for d, kind in (("mcps", "mcp"), ("repos", "repo"), ("stacks", "stack")):
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and f not in SKIP_NAMES:
                add(f"{d}/{f}", kind)
    for f in sorted(os.listdir("skills")):
        p = f"skills/{f}"
        if os.path.isfile(p) and f.endswith(".md") and f not in SKIP_NAMES:
            add(p, "skill-kho")
        elif os.path.isdir(p):
            sk = f"{p}/SKILL.md"
            if os.path.exists(sk) and f not in ("MASTER-INDEX", "README", "_template"):
                add(sk, "skill-import")
    for dp, dn, fn in os.walk("agents"):
        dn.sort()  # thứ tự cố định, không phụ thuộc hệ điều hành
        if "SKILL.md" in fn:
            add(os.path.join(dp, "SKILL.md").replace(os.sep, "/"), "skill-agent")
    return items

# ---------- đọc file ----------
def read(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()

def frontmatter(txt):
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    fm = {}
    if not m:
        return fm, txt
    body = txt[m.end():]
    cur = None
    for line in m.group(1).split("\n"):
        k = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if k:
            cur = k.group(1)
            v = k.group(2).strip()
            fm[cur] = "" if v in (">", "|", ">-", "|-") else v.strip("\"'")
        elif cur and line.startswith((" ", "\t")):
            fm[cur] = (fm[cur] + " " + line.strip()).strip()
    return fm, body

def clean(s):
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_>#]+", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def first_para(block):
    for para in re.split(r"\n\s*\n", block.strip()):
        t = clean(para.replace("\n", " "))
        if len(t) > 25 and not t.startswith(("|", "```", "---")):
            return t
    return ""

def summary_of(fm, body):
    m = re.search(r"^##\s*(?:📌\s*)?TL;DR[^\n]*\n(.*?)(?=\n##\s|\Z)", body, re.S | re.M)
    if m:
        s = first_para(m.group(1))
        if s:
            return s
    if fm.get("description"):
        return clean(fm["description"])
    m = re.search(r"^#\s+.*?\n(.*?)(?=\n##\s|\Z)", body, re.S | re.M)
    got = first_para(m.group(1)) if m else ""
    if got:
        return got
    # dự phòng: đoạn văn đầu tiên bất kỳ trong file (bỏ dòng tiêu đề, bảng)
    no_heads = re.sub(r"^#+ .*$", "", body, flags=re.M)
    return first_para(no_heads)

def name_of(fm, body, path):
    h1 = re.search(r"^#\s+(.+)$", body, re.M)
    base = os.path.basename(os.path.dirname(path)) if path.endswith("SKILL.md") else os.path.basename(path)[:-3]
    if h1:
        t = clean(h1.group(1))
        t = re.sub(r"\s+[—–-]\s+(GitHub Repo|MCP Server|Prompt Template.*|Skill)$", "", t)
        return t[:80] or base
    return fm.get("name") or base

# ---------- suy luận ----------
DOMAINS = [
    ("ticketing-hang-khong", r"\b(amadeus|gds|pnr|iata|airline|aviation|flight|sân bay|vé máy bay|timatic|bsp|ticketing|fast ?track|ground handling)\b"),
    ("research", r"\b(research|nghiên cứu|crawl|scrape|scraper|firecrawl|web search|tra cứu|competitive intel|osint|rag\b|second brain|market research)\b"),
    ("content", r"\b(content|viết bài|copywrit|blog|caption|script|kịch bản|tiktok|youtube|shorts|podcast|newsletter|storytelling|writer|writing)\b"),
    ("marketing", r"\b(marketing|seo\b|ads\b|quảng cáo|campaign|funnel|cro\b|landing|lead\b|affiliate|growth|brand|social media|email marketing|ppc)\b"),
    ("sales-crm", r"\b(sales|crm\b|outreach|cold email|pipeline|bán hàng|proposal|báo giá|deal\b)\b"),
    ("media-video-audio", r"\b(video|remotion|hyperframes|ffmpeg|tts\b|voiceover|giọng|nhạc|music|animation|motion|elevenlabs|capcut)\b"),
    ("design-ui", r"\b(design|thiết kế|ui\b|ux\b|figma|css|tailwind|poster|thumbnail|image prompt|logo|accessib|wcag|frontend)\b"),
    ("customer-support", r"\b(customer (support|service|satisfaction)|chăm sóc khách|helpdesk|chatwoot|zalo oa|chatbot|csat)\b"),
    ("data-analytics", r"\b(analytics|dashboard|kpi|báo cáo|chart|spreadsheet|excel|csv|ga4|metrics)\b"),
    ("finance-accounting", r"\b(accounting|kế toán|invoice|hóa đơn|tax\b|thuế|finance|payroll|bookkeeping)\b"),
    ("productivity", r"\b(productivity|notion|obsidian|automation|zapier|n8n|adhd)\b"),
    ("dev-infra", r"\b(docker|vps|deploy|devops|ci/cd|github actions|kubernetes|nginx|postgres|database|backend|mcp server|homelab|self-host)\b"),
    ("dev-code", r"\b(kotlin|swift|java\b|golang|\bgo\b|rust|django|laravel|spring|react|next\.?js|flutter|android|ios\b|c\+\+|php|perl|ktor|typescript|python|testing|test-driven|refactor|code review|compose multiplatform|jetpack)\b"),
    ("agent-llm", r"\b(multi-agent|agent framework|orchestrat|harness|claude code|llm\b|hermes|openclaw|antigravity|deepseek|mcp\b|prompt engineering|agent eval)\b"),
]

# Bảng capability cố định (nguồn: catalog/curation-draft/PROMPT-GAN-NHAN.md). social-media thêm sau pilot 16/10/2026.
CAPABILITIES = (
    "web-research scraping content-writing seo ads email-outreach crm-sales customer-support video-generation "
    "video-render image-generation voice-tts design-ui front-end backend database devops agent-framework "
    "agent-orchestration-memory prompt-skill-library browser-automation document-office data-dashboard "
    "finance-accounting ticketing-aviation security-compliance local-llm productivity reference social-media"
).split()

def domains_of(text):
    low = text.lower()
    out = [d for d, rx in DOMAINS if re.search(rx, low)]
    if not out:
        return ["agent-llm"] if re.search(r"\b(ai\b|claude|mcp|agent|gpt|gemini|prompt)\b", low) else ["khác"]
    return out[:3]

CORE = {"ticketing-hang-khong", "research", "content", "marketing", "sales-crm", "media-video-audio",
        "design-ui", "customer-support", "data-analytics", "finance-accounting", "productivity"}
def priority_of(domains):
    ds = set(domains.split(","))
    if ds & CORE:
        return "cao"
    if ds & {"dev-infra", "agent-llm"}:
        return "vừa"
    return "thấp"   # chỉ lập trình ngôn ngữ/framework hoặc chưa phân loại: không phục vụ việc agency hằng ngày

NOT_RUN = re.compile(r"chưa (chạy|test|cài|kiểm chứng|verify)|0 lần cài|chưa thử|untested|not (yet )?tested", re.I)
RAN = re.compile(r"ĐÃ CHẠY THẬT|(?<!chưa )đã chạy (thật|thử)|(?<!chưa )đã test thật|đã cài và chạy")

def verify_of(kind, txt, score=""):
    if kind == "skill-import" and score == "":
        return "chưa đánh giá"
    ran = bool(RAN.search(txt)) and not re.search(r"(chưa|không)\s+(có\s+)?(đã\s+)?chạy thật", txt, re.I)
    not_run = bool(NOT_RUN.search(txt))
    if ran and not_run:
        return "một phần"
    if ran:
        return "có ghi đã chạy"
    if not_run:
        return "chưa chạy"
    return "đọc nguồn"

def score_of(txt):
    m = re.search(r"(?:Có nên dùng|nên dùng)[^\n]{0,40}?(\d+(?:[.,]\d)?)\s*/\s*10", txt, re.I)
    if not m:
        m = re.search(r"Đánh giá[^\n]{0,60}?(\d+(?:[.,]\d)?)\s*/\s*10", txt, re.I)
    if m:
        try:
            v = float(m.group(1).replace(",", "."))
            return v if 0 <= v <= 10 else ""
        except ValueError:
            return ""
    return ""

LIC = re.compile(r"\b(MIT|Apache[- ]?2(?:\.0)?|AGPL[- ]?v?3?|GPL[- ]?v?3?|LGPL|BSD(?:-\d)?|MPL|ISC|Unlicense|CC0)\b")
def license_of(txt):
    m = re.search(r"licen[sc]e[^\n]{0,30}?" + LIC.pattern, txt, re.I) or re.search(LIC, txt[:3000])
    if not m:
        return ""
    g = [x for x in m.groups() if x]
    return g[0] if g else ""

def risks_of(txt):
    r = []
    if re.search(r"AGPL|license (thương mại|riêng)|Enterprise\)", txt, re.I): r.append("license")
    if re.search(r"CVE-\d{4}|lỗ hổng|bảo mật nghiêm|prompt injection", txt, re.I): r.append("bảo mật")
    if re.search(r"dữ liệu nhạy cảm|quyền riêng tư|đọc lịch sử|token đăng nhập|ToS|vi phạm điều khoản", txt, re.I): r.append("dữ liệu/ToS")
    if re.search(r"trả phí|\bpaid\b|tính phí|credit|\$\d", txt, re.I): r.append("tốn tiền")
    return ",".join(r)

def has_ai(txt):
    return "có" if re.search(r"Agent Integration", txt) else ""

def git_dates():
    out = subprocess.run(["git", "log", "--name-only", "--format=@@%cs"], capture_output=True, text=True).stdout
    dates, cur = {}, None
    for line in out.splitlines():
        if line.startswith("@@"):
            cur = line[2:]
        elif line.strip() and line not in dates:
            dates[line] = cur
    return dates

def main():
    dates = git_dates()
    rows = []
    for path, kind in collect():
        txt = read(path)
        fm, body = frontmatter(txt)
        summ = summary_of(fm, body)
        name = name_of(fm, body, path)
        rows.append({
            "id": re.sub(r"\.md$", "", path).replace("/SKILL", ""),
            "loai": kind,
            "ten": name,
            "tom_tat": summ[:230],
            "domain": ",".join(domains_of(name + " " + summ + " " + path)),
            "uu_tien_agency": "",
            "xac_minh": verify_of(kind, txt, score_of(txt)),
            "diem": score_of(txt),
            "license": license_of(txt),
            "rui_ro": risks_of(txt),
            "co_agent_integration": has_ai(txt),
            "nguon": fm.get("origin", ""),
            "cap_nhat": dates.get(path, ""),
            "duong_dan": path,
        })
    for r in rows:
        r["uu_tien_agency"] = priority_of(r["domain"])
    # Nhãn tra cứu đã tuyển chọn (catalog/curation.json). Không có thì để trống / "chua-gan-nhan".
    cur = {}
    if os.path.exists("catalog/curation.json"):
        cur = json.load(open("catalog/curation.json", encoding="utf-8")).get("items", {})
    for r in rows:
        c = cur.get(r["id"])
        for k in ("capability", "vessel_fit", "needs"):
            r[k] = ",".join(c[k]) if c else ""
        for k in ("use_when", "skip_if", "adoption", "dup_group", "confidence", "evidence"):
            r[k] = c.get(k, "") if c else ""
        r["curation_status"] = c["curation_status"] if c else "chua-gan-nhan"
    bad = sorted({v for c in cur.values() for v in c["capability"]} - set(CAPABILITIES))
    if bad:
        sys.exit(f"curation.json có capability ngoài bảng 30 giá trị: {bad}")
    os.makedirs("catalog", exist_ok=True)
    cols = list(rows[0].keys())
    with open("catalog/CATALOG.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    with open("catalog/catalog.json", "w", encoding="utf-8") as fh:
        json.dump({"generated": datetime.now().strftime("%Y-%m-%d"), "count": len(rows), "items": rows}, fh, ensure_ascii=False)
    write_by_domain(rows)
    print(f"catalog: {len(rows)} mục")
    from collections import Counter
    print("loại:", dict(Counter(r["loai"] for r in rows)))
    print("xác minh:", dict(Counter(r["xac_minh"] for r in rows)))
    print("ưu tiên:", dict(Counter(r["uu_tien_agency"] for r in rows)))
    print("domain:", dict(Counter(d for r in rows for d in r["domain"].split(","))))

def write_by_domain(rows):
    """Bản đọc nhanh: mỗi lĩnh vực chỉ liệt kê mục có điểm >= 7 hoặc đã chạy thật."""
    by = {}
    for r in rows:
        for d in r["domain"].split(","):
            by.setdefault(d, []).append(r)
    lines = ["# CATALOG — BY DOMAIN", "",
             "> Sinh tự động bằng `tools/build_catalog.py`. Đừng sửa tay.",
             "> Domain gán bằng từ khoá nên có thể sai — dùng để lọc. Đầy đủ: `catalog/CATALOG.csv`.",
             "> Mục ở đây = điểm ≥ 7 hoặc đã chạy thật. Chưa có điểm ≠ dở; chỉ là chưa ai chấm.", ""]
    for d in sorted(by, key=lambda k: -len(by[k])):
        sel = [r for r in by[d] if (r["diem"] != "" and r["diem"] >= 7) or r["xac_minh"] in ("có ghi đã chạy", "một phần")]
        sel.sort(key=lambda r: (-(r["diem"] if r["diem"] != "" else 0)))
        lines.append(f"## {d} ({len(by[d])} mục, {len(sel)} nổi bật)")
        lines.append("")
        if not sel:
            lines += ["_Chưa có mục nào đạt ngưỡng._", ""]
            continue
        lines += ["| Tên | Loại | Điểm | Xác minh | Rủi ro | File |", "|---|---|---|---|---|---|"]
        for r in sel[:40]:
            lines.append(f"| {r['ten'][:50]} | {r['loai']} | {r['diem']} | {r['xac_minh']} | {r['rui_ro']} | `{r['duong_dan']}` |")
        lines.append("")
    with open("catalog/BY-DOMAIN.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

if __name__ == "__main__":
    main()
