#!/usr/bin/env python3
"""Dựng trang tra cứu kho (một file index.html tĩnh) từ catalog/catalog.json.

    python tools/build_kho_web.py --out /var/www/kho

Trang tự chứa dữ liệu, không gọi server nào, chạy được sau nginx/Caddy/GitHub Pages.
Chạy lại sau mỗi lần `git pull` để trang khớp với catalog mới.
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["id", "loai", "ten", "domain", "xac_minh", "diem", "license", "rui_ro", "nguon", "cap_nhat",
          "duong_dan", "capability", "vessel_fit", "needs", "use_when", "skip_if", "adoption",
          "dup_group", "confidence", "evidence", "curation_status", "tom_tat"]


def build(root=ROOT):
    cat = json.loads((root / "catalog" / "catalog.json").read_text(encoding="utf-8"))
    cat = cat if isinstance(cat, list) else cat["items"]
    items = []
    for r in cat:
        o = {k: r.get(k, "") for k in FIELDS}
        o["tom_tat"] = (o["tom_tat"] or "")[:200]
        items.append(o)
    kit = json.loads((root / "tools" / "kho-web" / "kit.json").read_text(encoding="utf-8"))
    # ngày dữ liệu = ngày commit catalog gần nhất nếu đọc được, không thì ngày build
    import datetime
    data = {"generated": datetime.date.today().isoformat(), "items": items, "kit": kit}
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (root / "tools" / "kho-web" / "template.html").read_text(encoding="utf-8")
    if "@@DATA@@" not in tpl:
        sys.exit("template.html thiếu chỗ đặt @@DATA@@")
    return tpl.replace("@@DATA@@", '<script type="application/json" id="data">' + js + "</script>"), len(items)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="thư mục xuất index.html")
    a = ap.parse_args()
    html, n = build()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    print(f"đã dựng {out / 'index.html'}: {n} mục, {len(html) // 1024} KB")


if __name__ == "__main__":
    main()
