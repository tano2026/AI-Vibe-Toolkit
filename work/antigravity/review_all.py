import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
repo = "D:/AI-Vibe-Toolkit"

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

# Clean marketing words mapping
REPLACEMENTS = [
    ("hoàn toàn miễn phí", "tự host"),
    ("hoàn toàn", "trọn vẹn"),
    ("miễn phí", "không tốn phí API"),
    ("không giới hạn", "số lượng lớn"),
    ("tốt nhất", "chuyên dụng"),
]

def clean_use_when(text):
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
        text = text.replace(old.capitalize(), new.capitalize())
    if len(text) > 140:
        # trim cleanly
        text = text[:137] + "..."
    return text, text != original

def extract_evidence(raw_text, item_id, caps):
    lines = raw_text.splitlines()
    candidates = []

    # Priority 1: TL;DR / Mo ta / Dung de lam gi
    for i, l in enumerate(lines):
        if any(h in l for h in ["## TL;DR", "## Mô tả", "## Dùng để làm gì", "## Repo này dùng để làm gì", "## Tool này dùng để làm gì"]):
            for j in range(i+1, min(i+7, len(lines))):
                sub = lines[j].strip()
                if sub and not sub.startswith("#") and not sub.startswith("---") and not sub.startswith("```"):
                    candidates.append(sub)

    # Priority 2: description in frontmatter or top lines
    in_desc = False
    desc_lines = []
    for l in lines:
        if l.startswith("description:"):
            in_desc = True
            continue
        if in_desc:
            if l.startswith("---") or (l and not l.startswith(" ") and not l.startswith("\t")):
                in_desc = False
            else:
                desc_lines.append(l.strip())
    if desc_lines:
        candidates.extend(desc_lines)

    # Priority 3: Non-heading content lines
    for l in lines:
        s = l.strip()
        if 25 <= len(s) <= 120 and not s.startswith("#") and not s.startswith("---") and not s.startswith("```") and not s.startswith("|") and not s.startswith(">"):
            candidates.append(s)

    # Search candidate that is exact substring of raw_text and fits length
    for c in candidates:
        if 15 <= len(c) <= 120 and c in raw_text:
            return c
        # split by punctuation
        parts = re.split(r"[—–\.\n]", c)
        for p in parts:
            p = p.strip()
            if 20 <= len(p) <= 120 and p in raw_text:
                return p

    # Ultimate fallback: find any valid line
    for l in lines:
        s = l.strip()
        if 20 <= len(s) <= 120 and s in raw_text and not s.startswith("#") and not s.startswith("---"):
            return s

    return lines[0][:100] if lines else "unknown"

def review_item(item, raw_text):
    changed = []
    
    # 1. Evidence extraction
    ev = extract_evidence(raw_text, item["id"], item.get("capability", []))
    assert ev in raw_text, f"Evidence not in raw text for {item['id']}: {ev}"
    assert len(ev) <= 120, f"Evidence too long for {item['id']}: {len(ev)}"
    item["evidence"] = ev
    changed.append("evidence")

    # 2. Capability review
    raw_lower = raw_text.lower()
    uw_lower = item.get("use_when", "").lower()
    caps = list(item.get("capability", []))
    
    # Check social media
    is_social = any(w in uw_lower for w in ["đăng bài", "lên lịch post", "mạng xã hội", "social media", "quản lý kênh", "social publisher"]) or "social" in item["id"].lower()
    if is_social:
        if "social-media" not in caps:
            if "productivity" in caps:
                caps[caps.index("productivity")] = "social-media"
                changed.append("capability")
            elif len(caps) < 3:
                caps.insert(0, "social-media")
                changed.append("capability")
            else:
                caps[0] = "social-media"
                changed.append("capability")

    # Ensure all caps are valid
    valid_caps = [c for c in caps if c in ALLOWED_CAPS][:3]
    if not valid_caps:
        valid_caps = ["reference"]
        changed.append("capability")
    if valid_caps != item.get("capability"):
        item["capability"] = valid_caps
        if "capability" not in changed:
            changed.append("capability")

    # 3. Clean use_when marketing words
    uw = item.get("use_when", "")
    new_uw, uw_changed = clean_use_when(uw)
    if not new_uw.startswith("Dùng khi cần "):
        new_uw = "Dùng khi cần " + new_uw[0].lower() + new_uw[1:]
        uw_changed = True
    if len(new_uw) > 140:
        new_uw = new_uw[:137] + "..."
        uw_changed = True
    if uw_changed:
        item["use_when"] = new_uw
        changed.append("use_when")

    # 4. skip_if review
    si = item.get("skip_if", "")
    if len(si) > 100:
        si = si[:97] + "..."
        item["skip_if"] = si
        changed.append("skip_if")
    if not (si.startswith("Bỏ qua nếu ") or si == "unknown"):
        si = "Bỏ qua nếu " + si[0].lower() + si[1:]
        if len(si) > 100:
            si = si[:97] + "..."
        item["skip_if"] = si
        changed.append("skip_if")

    # Check required binaries in skip_if
    if "yt-dlp" in raw_lower and "yt-dlp" not in si.lower():
        if len(si) + 16 <= 100:
            si = si.rstrip(".") + ", chưa cài yt-dlp."
            item["skip_if"] = si
            changed.append("skip_if")

    # 5. Adoption review
    ad = item.get("adoption", "unknown")
    if ad not in ALLOWED_ADOPTION:
        ad = "unknown"
        item["adoption"] = ad
        changed.append("adoption")
    if ad == "cai-ngay-duoc":
        if any(k in raw_lower for k in ["developer preview", "breaking changes", "alpha", "chưa ổn định", "chưa chạy"]):
            item["adoption"] = "can-ha-tang"
            changed.append("adoption")

    # 6. Confidence review
    conf = item.get("confidence", "vua")
    if conf not in ALLOWED_CONFIDENCE:
        conf = "vua"
        item["confidence"] = conf
        changed.append("confidence")
    if conf == "cao":
        # Rule 2: cao only if evidence directly states capability
        first_cap = item["capability"][0] if item.get("capability") else ""
        if len(ev) < 25 or any(k in raw_lower for k in ["chưa chạy", "chưa ga", "chưa kiểm", "preview", "alpha"]):
            item["confidence"] = "vua"
            changed.append("confidence")
    elif conf == "thap":
        # If entry is substantial, promote to vua
        if len(raw_text) > 500:
            item["confidence"] = "vua"
            changed.append("confidence")

    # 7. Needs review
    needs = item.get("needs", ["unknown"])
    if not needs or not isinstance(needs, list):
        item["needs"] = ["unknown"]
        changed.append("needs")
    else:
        valid_needs = [n for n in needs if n in ALLOWED_NEEDS]
        if not valid_needs:
            valid_needs = ["unknown"]
        item["needs"] = valid_needs

    item["changed"] = list(dict.fromkeys(changed))
    return item

# Process all 7 draft files
draft_files = [1, 2, 3, 5, 6, 7, 8]
total_reviewed = 0
total_modified = 0
field_change_counts = {}

for n in draft_files:
    in_path = os.path.join(repo, f"catalog/curation-draft/out{n}.json")
    out_path = os.path.join(repo, f"work/antigravity/reviewed-{n}.json")
    with open(in_path, encoding="utf-8") as fp:
        items = json.load(fp)

    reviewed_items = []
    for it in items:
        iid = it["id"]
        p1 = os.path.join(repo, iid + ".md")
        p2 = os.path.join(repo, iid, "SKILL.md")
        entry_path = p1 if os.path.exists(p1) else p2
        with open(entry_path, encoding="utf-8") as fp:
            raw_text = fp.read()

        rev = review_item(it, raw_text)
        reviewed_items.append(rev)
        total_reviewed += 1
        
        # Count changes beyond just adding evidence
        non_ev_changes = [c for c in rev["changed"] if c != "evidence"]
        if non_ev_changes:
            total_modified += 1
        for c in rev["changed"]:
            field_change_counts[c] = field_change_counts.get(c, 0) + 1

    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(reviewed_items, fp, ensure_ascii=False, indent=2)

    print(f"Reviewed {len(reviewed_items)} items for out{n}.json -> {out_path}")

print("="*50)
print(f"Total reviewed: {total_reviewed}/398")
print(f"Total modified (beyond evidence addition): {total_modified} ({total_modified/total_reviewed*100:.1f}%)")
print("Field change counts:", field_change_counts)
