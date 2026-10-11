#!/usr/bin/env python3
"""convert_skills.py: chuyển skills/ của kho thành thư mục skill nạp được bởi Claude Code.

Vấn đề kho đang có (đo 11/10/2026): một số thư mục skill không có frontmatter, một số
chỉ chứa các file .md rời (không có SKILL.md), một số có `name` khác tên thư mục (gây
trùng tên), một số có `description` một dòng chứa dấu ": " chưa đặt trong ngoặc (YAML hỏng).

Script KHÔNG sửa nguồn. Nó đọc `<repo>/skills` và ghi bản đã chuẩn hóa vào thư mục đích.

Dùng:
  py -3 convert_skills.py --dry-run                 # chỉ in kế hoạch, không ghi gì
  py -3 convert_skills.py --dst D:\\path\\skills-out  # ghi thật
  py -3 convert_skills.py --only viral-hooks,anti-ai-tells --dst <project>\\.claude\\skills

Thư mục đích mặc định: ~/.claude/skills-kho (khác ~/.claude/skills). Nếu thư mục đích là
chính nguồn, nằm trong nguồn, hoặc là symlink trỏ vào nguồn thì script từ chối.
Mặc định loại các skill tử vi (tuvi*, bazi-ziwei-skill); đổi bằng --exclude / --no-default-exclude.
Chỉ dùng thư viện chuẩn của Python.
"""
import argparse
import fnmatch
import json
import os
import re
import shutil
import sys
from pathlib import Path

MARK = ".kho-converted.json"
DEFAULT_EXCLUDE = ["tuvi*", "bazi-ziwei-skill"]
NON_SKILL_DIRS = {"README", "_template"}
FM_RE = re.compile(r"^\ufeff?---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", re.S)
SLUG_RE = re.compile(r"[^a-z0-9]+")


def slug(s):
    return SLUG_RE.sub("-", s.lower()).strip("-") or "skill"


def split_fm(text):
    m = FM_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def needs_quote(val):
    v = val.strip()
    if not v or v[0] in "\"'|>[{&*!%@`":
        return False
    return ": " in v or v.endswith(":") or " #" in v


def fix_fm_lines(fm, dirname, want=None):
    """Trả (fm mới, danh sách thay đổi). Chỉ sửa name và description một dòng."""
    changes = []
    lines = fm.split("\n")
    out = []
    has_name = has_desc = False
    for ln in lines:
        m = re.match(r"^(name|description):[ \t]*(.*?)\r?$", ln)
        if m:
            key, val = m.group(1), m.group(2)
            if key == "name":
                has_name = True
                cur = val.strip().strip("\"'")
                target = want or cur
                if cur != target:
                    changes.append(f"name {cur!r} -> {target!r} (trùng tên)")
                    ln = f"name: {target}"
            else:
                has_desc = True
                if needs_quote(val):
                    changes.append("description: thêm ngoặc kép (có dấu ': ')")
                    ln = "description: " + json.dumps(val.strip(), ensure_ascii=False)
        out.append(ln)
    head = []
    if not has_name:
        head.append(f"name: {dirname}")
        changes.append("thêm name")
    new = "\n".join(head + out)
    return new, changes, has_desc


def guess_description(body):
    title = ""
    for ln in body.splitlines():
        s = ln.strip()
        if not s or s.startswith(("```", "|", "<")):
            continue
        if s.startswith("#"):
            if not title:
                title = s.lstrip("#").strip()
            continue
        s = re.sub(r"^[>\-\*\s]+", "", s)
        s = re.sub(r"[*_`]", "", s)
        if len(s) >= 20:
            return (title + ". " if title else "") + s[:240]
    return title or "Skill nhập từ kho AI-Vibe-Toolkit (chưa có mô tả)."


def build_skill_md(text, dirname, want=None):
    """Trả (nội dung SKILL.md mới, ghi chú, trạng thái)."""
    fm, body = split_fm(text)
    if fm is None:
        desc = guess_description(body)
        new_fm = f"name: {dirname}\ndescription: {json.dumps(desc, ensure_ascii=False)}"
        return f"---\n{new_fm}\n---\n\n{body.lstrip()}", ["thêm frontmatter (mô tả suy ra từ nội dung)"], "added-fm"
    new_fm, ch, has_desc = fix_fm_lines(fm, dirname, want)
    if not has_desc:
        desc = guess_description(body)
        new_fm += "\ndescription: " + json.dumps(desc, ensure_ascii=False)
        ch.append("thêm description (suy ra từ nội dung)")
    if not ch:
        return text, [], "ok"
    return f"---\n{new_fm}\n---\n{body if body.startswith(chr(10)) else chr(10) + body}", ch, "fixed"


def plan_entries(src, include, exclude):
    """Sinh danh sách {out_name, kind, files:{relpath: sourcepath}, skill_md_src, notes}."""
    entries = []
    skipped = []
    for d in sorted(os.listdir(src)):
        p = src / d
        if not p.is_dir():
            skipped.append((d, "file phẳng, không phải skill"))
            continue
        if d in NON_SKILL_DIRS:
            skipped.append((d, "không phải skill"))
            continue
        if any(fnmatch.fnmatch(d, pat) for pat in exclude):
            skipped.append((d, "bị loại (--exclude)"))
            continue
        if include and d not in include:
            continue
        if (p / "SKILL.md").is_file():
            entries.append({"out": d, "src_dir": p, "skill_md": p / "SKILL.md", "kind": "dir"})
            continue
        # không có SKILL.md: gom .md rời thành skill riêng
        got = False
        for f in sorted(p.glob("*.md")):
            if f.name.lower() == "readme.md":
                continue
            entries.append({"out": f"{d}-{slug(f.stem)}", "src_dir": None, "skill_md": f, "kind": "loose", "parent": d})
            got = True
        for sub in sorted(x for x in p.iterdir() if x.is_dir()):
            if (sub / "SKILL.md").is_file():
                if any(fnmatch.fnmatch(sub.name, pat) for pat in exclude):
                    skipped.append((f"{d}/{sub.name}", "bị loại (--exclude)"))
                    continue
                entries.append({"out": f"{d}-{slug(sub.name)}", "src_dir": sub, "skill_md": sub / "SKILL.md", "kind": "nested", "parent": d})
                got = True
        if not got:
            skipped.append((d, "không có SKILL.md hay file .md để chuyển"))
    return entries, skipped


def safe_dst(src, dst):
    s, d = src.resolve(), dst.resolve()
    if d == s or s in d.parents or d in s.parents:
        return f"thư mục đích ({d}) trùng/nằm trong/chứa nguồn ({s}). Chọn --dst khác."
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    root = Path(__file__).resolve().parent
    ap.add_argument("--src", default=str(root / "skills"))
    ap.add_argument("--dst", default=str(Path.home() / ".claude" / "skills-kho"))
    ap.add_argument("--dry-run", action="store_true", help="chỉ in kế hoạch, không ghi file")
    ap.add_argument("--only", default="", help="danh sách tên thư mục, cách nhau dấu phẩy")
    ap.add_argument("--exclude", default="", help="mẫu loại thêm, cách nhau dấu phẩy (fnmatch)")
    ap.add_argument("--no-default-exclude", action="store_true")
    ap.add_argument("--report", default="", help="ghi báo cáo JSON ra file này")
    a = ap.parse_args()

    src, dst = Path(a.src), Path(a.dst).expanduser()
    if not src.is_dir():
        print(f"Không thấy nguồn: {src}")
        return 2
    err = safe_dst(src, dst)
    if err:
        print("TỪ CHỐI:", err)
        return 2
    include = {x.strip() for x in a.only.split(",") if x.strip()}
    exclude = ([] if a.no_default_exclude else list(DEFAULT_EXCLUDE)) + [x.strip() for x in a.exclude.split(",") if x.strip()]

    entries, skipped = plan_entries(src, include, exclude)
    names = {}
    results = []
    orig, seen_names = {}, {}
    for e in entries:
        fm, _ = split_fm(e["skill_md"].read_text(encoding="utf-8", errors="replace"))
        m = re.search(r"^name:[ \t]*(.+?)\r?$", fm or "", re.M)
        orig[e["out"]] = m.group(1).strip().strip("\"'") if m else e["out"]
        seen_names[orig[e["out"]]] = seen_names.get(orig[e["out"]], 0) + 1
    for e in entries:
        text = e["skill_md"].read_text(encoding="utf-8", errors="replace")
        want = e["out"] if seen_names[orig[e["out"]]] > 1 else None
        new, notes, status = build_skill_md(text, e["out"], want)
        if e["out"] in names:
            status, notes = "conflict", [f"trùng tên với {names[e['out']]}"]
        names[e["out"]] = str(e["skill_md"].relative_to(src))
        results.append({**e, "new": new, "notes": notes, "status": status})

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"Nguồn: {src}\nĐích : {dst}  ({'DRY-RUN, không ghi gì' if a.dry_run else 'GHI THẬT'})")
    print(f"Skill: {len(results)} | " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) + f" | bỏ qua={len(skipped)}\n")
    for r in results:
        if r["status"] != "ok":
            print(f"  [{r['status']:9}] {r['out']}  <- {names[r['out']] if r['status'] != 'conflict' else ''}  {'; '.join(r['notes'])}")
    print("\nBỏ qua:")
    for n, why in skipped:
        print(f"  {n}: {why}")

    if a.report:
        Path(a.report).write_text(json.dumps({
            "counts": counts,
            "skills": [{"out": r["out"], "status": r["status"], "notes": r["notes"]} for r in results],
            "skipped": skipped}, ensure_ascii=False, indent=2), encoding="utf-8")

    if a.dry_run:
        print("\n(dry-run) Chưa ghi gì. Bỏ --dry-run để ghi.")
        return 0

    dst.mkdir(parents=True, exist_ok=True)
    mf_path = dst / MARK
    manifest = json.loads(mf_path.read_text(encoding="utf-8")) if mf_path.exists() else {"generated": []}
    mine = set(manifest["generated"])
    wrote, refused = [], []
    for r in results:
        if r["status"] == "conflict":
            refused.append((r["out"], "trùng tên"))
            continue
        target = dst / r["out"]
        if target.exists() and r["out"] not in mine:
            refused.append((r["out"], "đã có trong đích mà không do script này tạo, không ghi đè"))
            continue
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        if r["src_dir"] is not None:
            for f in r["src_dir"].rglob("*"):
                if f.is_file() and ".git" not in f.parts and f.name != "SKILL.md":
                    t = target / f.relative_to(r["src_dir"])
                    t.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, t)
        (target / "SKILL.md").write_text(r["new"], encoding="utf-8", newline="\n")
        wrote.append(r["out"])
    manifest["generated"] = sorted(mine | set(wrote))
    mf_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nĐã ghi {len(wrote)} skill vào {dst}")
    for n, why in refused:
        print(f"  KHÔNG ghi {n}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
