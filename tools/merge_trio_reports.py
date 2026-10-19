#!/usr/bin/env python3
"""Gộp báo cáo kiểm chéo của Trio (Hermes / OpenClaw / DeepSeek Harness).

Dùng:  python tools/merge_trio_reports.py REPORT-hermes.md REPORT-openclaw.md REPORT-deepseek.md
In ra: tỉ lệ nhãn đúng theo agent và tổng, trường sai nhiều nhất, danh sách đề xuất sửa,
       mục nên gỡ khỏi cai-ngay-duoc, cảnh báo định dạng. KHÔNG ghi vào curation.json
       hay bất kỳ file nào (chỉ đọc + in ra stdout).
Bảng mong đợi:  | id | nhãn đúng? | sửa đề xuất | căn cứ |  (đúng 20 dòng dữ liệu)
"""
import re
import sys
import unicodedata
from collections import Counter

FIELDS = ["capability", "vessel_fit", "needs", "adoption", "dup_group",
          "confidence", "use_when", "skip_if", "evidence"]
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._\-]*/[A-Za-z0-9._\-/]+$")
EXPECT = 20


def norm(s):
    return unicodedata.normalize("NFC", s).strip()


def split_row(line):
    line = line.strip()
    if not (line.startswith("|") and line.endswith("|")):
        return None
    cells, cur, esc = [], "", False
    for ch in line[1:-1]:
        if esc:
            cur += ch if ch == "|" else "\\" + ch
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == "|":
            cells.append(cur.strip()); cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def agent_name(path):
    m = re.search(r"REPORT-([A-Za-z0-9_]+)", path.replace("\\", "/").split("/")[-1])
    return m.group(1).lower() if m else path


def parse(path):
    text = open(path, encoding="utf-8-sig").read()
    rows, warns = [], []
    for ln in text.splitlines():
        c = split_row(ln)
        if not c or len(c) < 4:
            continue
        iid = c[0].strip("` ")
        if not ID_RE.match(iid):
            continue  # tiêu đề, dòng ngăn cách, bảng phụ không có id
        verdict, fix, basis = norm(c[1]), c[2].strip(), c[3].strip()
        ok = verdict.lower().startswith("đúng") or verdict.lower().startswith("dung")
        bad = [f for f in FIELDS if re.search(rf"\b{f}\b", verdict)] if not ok else []
        if not ok and not bad:
            warns.append(f"{iid}: không nhận ra trường sai trong '{verdict}'")
        rows.append({"id": iid, "ok": ok, "verdict": verdict, "bad": bad, "fix": fix, "basis": basis})
    seen = Counter(r["id"] for r in rows)
    dups = [i for i, n in seen.items() if n > 1]
    if dups:
        warns.append("id lặp: " + ", ".join(dups))
    if len(rows) != EXPECT:
        warns.append(f"có {len(rows)} dòng dữ liệu, cần {EXPECT}")
    for r in rows:
        b = r["basis"].strip('"“”\' ')
        if not b:
            warns.append(f"{r['id']}: thiếu căn cứ")
    concl = {}
    for key, pat in [("ti_le", r"TỈ LỆ ĐÚNG\s*:\s*(.+)"), ("loi", r"LỖI HAY GẶP\s*:\s*(.+)"),
                     ("go", r"NÊN GỠ KHỎI cai-ngay-duoc\s*:\s*(.+)")]:
        m = re.search(pat, text)
        concl[key] = m.group(1).strip() if m else None
        if not m:
            warns.append(f"thiếu dòng kết luận '{pat.split(chr(92))[0]}'")
    return rows, concl, warns


def pct(a, b):
    return f"{a}/{b} ({100 * a / b:.0f}%)" if b else "n/a"


def main(argv):
    if not argv:
        print(__doc__); return 2
    per, allrows, status = {}, [], 0
    for p in argv:
        try:
            rows, concl, warns = parse(p)
        except OSError as e:
            print(f"! không đọc được {p}: {e}"); status = 1; continue
        a = agent_name(p)
        per[a] = (rows, concl, warns)
        allrows += [dict(r, agent=a) for r in rows]
    print("=== TỈ LỆ NHÃN ĐÚNG ===")
    for a, (rows, concl, _) in per.items():
        n_ok = sum(r["ok"] for r in rows)
        self_rep = f"   | agent tự báo: {concl['ti_le']}" if concl.get("ti_le") else ""
        print(f"{a:10s} {pct(n_ok, len(rows))}{self_rep}")
    tot_ok = sum(r["ok"] for r in allrows)
    print(f"{'TỔNG':10s} {pct(tot_ok, len(allrows))}")

    print("\n=== TRƯỜNG SAI NHIỀU NHẤT (đếm số mục sai theo trường) ===")
    fc = Counter(f for r in allrows for f in r["bad"])
    if not fc:
        print("(không có)")
    for f, n in fc.most_common():
        by = Counter(r["agent"] for r in allrows if f in r["bad"])
        print(f"{f:12s} {n:3d}   " + ", ".join(f"{a}:{k}" for a, k in by.items()))

    print("\n=== ĐỀ XUẤT SỬA (mục sai; chưa áp dụng, chỉ để Claude duyệt) ===")
    bad_rows = [r for r in allrows if not r["ok"]]
    for r in sorted(bad_rows, key=lambda r: r["id"]):
        print(f"- {r['id']}  [{r['agent']}]  sai: {', '.join(r['bad']) or r['verdict']}")
        print(f"    sửa: {r['fix']}")
        print(f"    căn cứ: {r['basis']}")
    if not bad_rows:
        print("(không có)")
    ids = Counter(r["id"] for r in allrows)
    conflict = [i for i, n in ids.items() if n > 1]
    if conflict:
        print("\n! id xuất hiện ở nhiều agent (lẽ ra không trùng): " + ", ".join(conflict))

    print("\n=== MỤC NÊN GỠ KHỎI cai-ngay-duoc (theo kết luận của từng agent) ===")
    for a, (_, concl, _) in per.items():
        print(f"{a:10s} {concl.get('go') or '(thiếu)'}")
    print("\n=== LỖI HAY GẶP (agent tự nêu) ===")
    for a, (_, concl, _) in per.items():
        print(f"{a:10s} {concl.get('loi') or '(thiếu)'}")

    kdung = sum(1 for r in allrows if r["basis"].strip('"“”\' ').lower() == "không xác định")
    print(f"\nMục ghi 'không xác định' ở cột căn cứ: {kdung}")
    print("\n=== CẢNH BÁO ĐỊNH DẠNG ===")
    anyw = False
    for a, (_, _, warns) in per.items():
        for w in warns:
            anyw = True; print(f"[{a}] {w}")
    if not anyw:
        print("(không có)")
    print("\nLưu ý: script chỉ in ra, không ghi curation.json; áp dụng sửa là việc của Claude sau khi duyệt.")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
