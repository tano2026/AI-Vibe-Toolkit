import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
repo = "D:/AI-Vibe-Toolkit"

# Load catalog.json
with open(os.path.join(repo, "catalog/catalog.json"), encoding="utf-8") as fp:
    catalog_raw = json.load(fp)
catalog_items = catalog_raw.get("items", [])
catalog_dict = {x["id"]: x for x in catalog_items}
print(f"Catalog items loaded: {len(catalog_items)}")

# Load all 455 items
all_files = [
    "work/antigravity/pilot20-v2.json",
    "work/antigravity/out4.json",
    "work/antigravity/reviewed-1.json",
    "work/antigravity/reviewed-2.json",
    "work/antigravity/reviewed-3.json",
    "work/antigravity/reviewed-5.json",
    "work/antigravity/reviewed-6.json",
    "work/antigravity/reviewed-7.json",
    "work/antigravity/reviewed-8.json",
]

all_items = []
file_breakdown = {}
for rel_path in all_files:
    fpath = os.path.join(repo, rel_path)
    with open(fpath, encoding="utf-8") as fp:
        items = json.load(fp)
    file_breakdown[rel_path] = len(items)
    all_items.extend(items)

print(f"Total items gathered: {len(all_items)}")
for k, v in file_breakdown.items():
    print(f"  {k}: {v}")

# Mechanical checks
ALLOWED_CAPS = {
    "web-research", "scraping", "content-writing", "seo", "ads",
    "email-outreach", "crm-sales", "customer-support", "video-generation",
    "video-render", "image-generation", "voice-tts", "design-ui",
    "front-end", "backend", "database", "devops", "agent-framework",
    "agent-orchestration-memory", "prompt-skill-library",
    "browser-automation", "document-office", "data-dashboard",
    "finance-accounting", "ticketing-aviation", "security-compliance",
    "local-llm", "productivity", "reference", "social-media"
}

ALLOWED_ADOPTION = {"cai-ngay-duoc", "can-ha-tang", "chi-tham-khao", "unknown"}
ALLOWED_VESSELS = {"hermes", "openclaw", "deepseek-harness", "antigravity", "claude-code"}
ALLOWED_NEEDS = {"api-key", "tra-phi", "vps", "gpu", "docker", "claude-code-only", "browser", "none", "unknown"}
ALLOWED_CONFIDENCE = {"cao", "vua", "thap"}

seen_ids = set()
duplicate_ids = []
missing_in_catalog = []
validation_errors = []

for idx, it in enumerate(all_items):
    iid = it.get("id", f"UNKNOWN_INDEX_{idx}")
    
    # 1. Unique id
    if iid in seen_ids:
        duplicate_ids.append(iid)
    seen_ids.add(iid)
    
    # 2. Exists in catalog.json
    if iid not in catalog_dict:
        missing_in_catalog.append(iid)
        
    # 3. File exists on disk and evidence check
    p1 = os.path.join(repo, iid + ".md")
    p2 = os.path.join(repo, iid, "SKILL.md")
    p = p1 if os.path.exists(p1) else (p2 if os.path.exists(p2) else None)
    if not p:
        validation_errors.append(f"[{iid}] Entry file missing on disk")
    else:
        with open(p, encoding="utf-8") as fp:
            raw_text = fp.read()
        ev = it.get("evidence", "")
        if not ev:
            validation_errors.append(f"[{iid}] Missing evidence")
        elif len(ev) > 120:
            validation_errors.append(f"[{iid}] Evidence > 120 chars: {len(ev)}")
        elif ev not in raw_text:
            validation_errors.append(f"[{iid}] Evidence not exact substring in {p}")
            
    # 4. Capabilities check
    caps = it.get("capability", [])
    if not isinstance(caps, list) or not (1 <= len(caps) <= 3):
        validation_errors.append(f"[{iid}] Invalid capability count: {len(caps)}")
    for c in caps:
        if c not in ALLOWED_CAPS:
            validation_errors.append(f"[{iid}] Disallowed capability: {c}")
            
    # 5. use_when check
    uw = it.get("use_when", "")
    if len(uw) > 140:
        validation_errors.append(f"[{iid}] use_when > 140 chars: {len(uw)}")
    if not uw.startswith("Dùng khi cần "):
        validation_errors.append(f"[{iid}] use_when does not start with 'Dùng khi cần '")
        
    # 6. skip_if check
    si = it.get("skip_if", "")
    if len(si) > 100:
        validation_errors.append(f"[{iid}] skip_if > 100 chars: {len(si)}")
    if not (si.startswith("Bỏ qua nếu ") or si == "unknown"):
        validation_errors.append(f"[{iid}] skip_if does not start with 'Bỏ qua nếu '")
        
    # 7. Enum checks
    if it.get("adoption") not in ALLOWED_ADOPTION:
        validation_errors.append(f"[{iid}] Disallowed adoption: {it.get('adoption')}")
    for v in it.get("vessel_fit", []):
        if v not in ALLOWED_VESSELS:
            validation_errors.append(f"[{iid}] Disallowed vessel: {v}")
    for n in it.get("needs", []):
        if n not in ALLOWED_NEEDS:
            validation_errors.append(f"[{iid}] Disallowed need: {n}")
    if it.get("confidence") not in ALLOWED_CONFIDENCE:
        validation_errors.append(f"[{iid}] Disallowed confidence: {it.get('confidence')}")

print("="*50)
print("MECHANICAL AUDIT RESULTS:")
print(f"Total checked: {len(all_items)}")
print(f"Duplicate IDs: {len(duplicate_ids)} ({duplicate_ids})")
print(f"Missing in catalog.json: {len(missing_in_catalog)} ({missing_in_catalog})")
print(f"Validation errors: {len(validation_errors)}")
if validation_errors:
    for e in validation_errors[:20]:
        print("  -", e)

# PART D: Duplicate group detection (nhóm >= 3 mục cùng việc)
dup_groups = {}
for it in all_items:
    dg = it.get("dup_group", "").strip()
    if dg:
        dup_groups.setdefault(dg, []).append(it)

large_groups = {k: v for k, v in dup_groups.items() if len(v) >= 3}
print("="*50)
print(f"PART D: Groups with >= 3 items ({len(large_groups)} groups):")
for gname, items in sorted(large_groups.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"\nNhóm '{gname}' ({len(items)} mục):")
    for it in items:
        cid = it["id"]
        cat_info = catalog_dict.get(cid, {})
        loai = cat_info.get("loai", "unknown")
        diem = cat_info.get("diem", "chưa chấm")
        print(f"  - {cid:45} | loại: {loai:12} | điểm: {diem}")

# PART E: Báo cáo chỗ hổng (capabilities with < 3 cai-ngay-duoc & confidence != thap)
cap_counts = {c: 0 for c in sorted(ALLOWED_CAPS)}
for it in all_items:
    ad = it.get("adoption")
    conf = it.get("confidence")
    if ad == "cai-ngay-duoc" and conf != "thap":
        for c in it.get("capability", []):
            cap_counts[c] = cap_counts.get(c, 0) + 1

print("="*50)
print("PART E: Capability coverage (cai-ngay-duoc & confidence != thap):")
sparse_caps = []
for c, cnt in sorted(cap_counts.items(), key=lambda x: x[1]):
    print(f"  {c:30}: {cnt} mục")
    if cnt < 3:
        sparse_caps.append((c, cnt))

print(f"\nCapabilities with < 3 ready-to-use items: {len(sparse_caps)}")
for c, cnt in sparse_caps:
    print(f"  * {c}: {cnt}")
