#!/usr/bin/env python3
"""Sinh lại TRACKER.md từ file THẬT trong /mcps /repos /skills /stacks.
Chạy:  python3 tools/build_index.py          (ghi TRACKER.md)
       python3 tools/build_index.py --check   (chỉ in chênh lệch, không ghi)
- Dòng đã có trong TRACKER: giữ nguyên Tên/Tóm tắt/Quay video (cột Quay video sửa TAY).
- File mới: lấy tên từ H1, tóm tắt từ mục TL;DR (hoặc description), Agent Integration = Có nếu có mục đó.
- Không tay-append. File TRACKER cũ lưu trong git history.
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = [("MCPs", "mcps"), ("Repos", "repos"), ("Skills", "skills"), ("Stacks", "stacks")]
SKIP = {"README.md", "_template.md", "_template_script.md", "MASTER-INDEX.md"}
ROW = re.compile(r"^\| (.+?) \| (.*) \| `?(/(?:mcps|repos|skills|stacks)/[^`|]+?\.md)`? \| (Có|Không) \| ?(.*?) ?\|$")

def read_header_and_rows():
    txt = open(os.path.join(ROOT, "TRACKER.md"), encoding="utf-8").read().splitlines()
    head = []
    for ln in txt:
        if ln.startswith("## MCPs"): break
        head.append(ln)
    rows = {}
    for ln in txt:
        m = ROW.match(ln)
        if m:
            rows[m.group(3)] = (m.group(1), m.group(2), m.group(4), m.group(5).strip())
    return head, rows

def clean(s, n=320):
    s = re.sub(r"\s+", " ", s.replace("|", "/")).strip()
    return s if len(s) <= n else s[:n].rstrip() + "…"

def from_file(path):
    t = open(path, encoding="utf-8").read()
    h1 = re.search(r"^# (.+)$", t, re.M)
    name = clean(h1.group(1), 120) if h1 else os.path.basename(path)[:-3]
    m = re.search(r"^## TL;DR\s*\n+(.+?)(?:\n\s*\n|\n## )", t, re.M | re.S)
    if m: summ = m.group(1)
    else:
        d = re.search(r"^description:\s*>?\s*\n?(.+?)(?:\n---|\n\w+:)", t, re.M | re.S)
        summ = d.group(1) if d else ""
    ai = "Có" if re.search(r"^#+ .*Agent Integration", t, re.M) else "Không"
    return name, clean(summ), ai, ""

def main():
    check = "--check" in sys.argv
    head, old = read_header_and_rows()
    out, new_files, gone = [], [], []
    seen = set()
    for title, d in SECTIONS:
        files = sorted(f for f in os.listdir(os.path.join(ROOT, d))
                       if f.endswith(".md") and f not in SKIP)
        rows = []
        for f in files:
            key = f"/{d}/{f}"
            seen.add(key)
            if key in old: r = old[key]
            else:
                r = from_file(os.path.join(ROOT, d, f)); new_files.append(key)
            rows.append((r[0].lower(), r[0], r[1], key, r[2], r[3]))
        rows.sort()
        out.append(f"## {title} — {len(rows)} cái\n")
        out.append("| Tên | Tóm tắt (dùng để làm gì) | File | Agent Integration | Quay video |")
        out.append("|-----|---------------------------|------|--------------------|------------|")
        for _, n, s, key, ai, v in rows:
            out.append(f"| {n} | {s} | `{key}` | {ai} | {v} |")
        out.append("")
    gone = [k for k in old if k not in seen]
    print(f"giữ {len(old)-len(gone)} dòng cũ, thêm {len(new_files)} mới, bỏ {len(gone)} (file không còn)")
    for k in new_files: print("  + ", k)
    for k in gone: print("  - ", k)
    if check: return
    open(os.path.join(ROOT, "TRACKER.md"), "w", encoding="utf-8").write("\n".join(head + out).rstrip() + "\n")

main()
