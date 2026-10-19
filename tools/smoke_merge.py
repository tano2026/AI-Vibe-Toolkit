#!/usr/bin/env python3
"""Gộp kết quả kiểm sử dụng (mô phỏng văn bản) trong catalog/smoke/skill-*.json thành catalog/smoke.json.

Chạy:  python3 tools/smoke_merge.py
Ra:    catalog/smoke.json  {"tong_ket": {...}, "items": {id: {verdict, ma_van_de, tinh_huong_thu, goi_y_sua, lo}}}
build_catalog.py đọc file này để thêm 2 cột kiem_su_dung và kiem_su_dung_ly_do.

Quy ước trung thực: kết quả là MÔ PHỎNG BẰNG VĂN BẢN do model làm (không chạy mã), không phải dùng thật
trong dự án. Mục không có trong smoke.json = chưa kiểm sử dụng.
"""
import glob, json, os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OK = {"pass", "partial", "fail", "khong-ap-dung"}

def merge(root=ROOT):
    cat = {r["id"] for r in json.load(open(os.path.join(root, "catalog/catalog.json"), encoding="utf-8"))["items"]}
    items, errors = {}, []
    for f in sorted(glob.glob(os.path.join(root, "catalog/smoke/skill-*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for r in d.get("ket_qua", []):
            i, v = r.get("id"), r.get("verdict")
            if i not in cat:
                errors.append(f"{os.path.basename(f)}: id không có trong catalog: {i}")
                continue
            if v not in OK:
                errors.append(f"{os.path.basename(f)}: verdict lạ cho {i}: {v}")
                continue
            if i in items:
                errors.append(f"id trùng giữa các lô: {i}")
                continue
            items[i] = {"verdict": v, "ma_van_de": sorted({x.get("ma", "KHAC") for x in r.get("van_de", [])}),
                        "tinh_huong_thu": r.get("tinh_huong_thu", ""), "goi_y_sua": r.get("goi_y_sua", ""),
                        "do_chac": r.get("do_chac_cua_tester", ""), "lo": d.get("lo", "")}
    ma = Counter(m for v in items.values() for m in v["ma_van_de"])
    tong = {"phuong_phap": "mo-phong-van-ban", "so_muc": len(items), "verdict": dict(Counter(v["verdict"] for v in items.values())),
            "ma_van_de_pho_bien": dict(ma.most_common(12))}
    return {"tong_ket": tong, "items": items}, errors

def main():
    out, errors = merge()
    for e in errors:
        print("LỖI:", e, file=sys.stderr)
    json.dump(out, open(os.path.join(ROOT, "catalog/smoke.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("smoke.json:", out["tong_ket"]["so_muc"], "mục;", out["tong_ket"]["verdict"])
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
