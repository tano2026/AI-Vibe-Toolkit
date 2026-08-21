# HERMES-ADAPTER.md — Content Pro

> Adapter chính thức nối Content Pro vào Hermes. Bản trước (`HERMES-CONTENT-PRO.md`,
> file tải về, chưa push kho) nhét TĨNH nội dung 12 skill chiến thuật vào
> 1 file — dễ lỗi thời khi kho update. Bản này đổi sang fetch ĐỘNG qua
> `github()`, luôn lấy bản mới nhất.

## Vấn đề đã sửa: "gọi skill mù"

Xác nhận qua GitHub API thật (không suy đoán): **toàn bộ 12 skill chiến thuật Content Pro tham chiếu đều tồn tại thật trong kho** — không có skill nào bị thiếu. Vấn đề thật sự không phải "skill không tồn tại", mà là **Hermes không có cơ chế tự động load skill theo tên** như Claude Code — cần code tường minh để lấy đúng nội dung khi cần.

```python
import urllib.request, json, base64, os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "tano2026/AI-Vibe-Toolkit"

def github(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def fetch_skill_from_kho(skill_path):
    data = github(f"repos/{REPO}/contents/{skill_path}")
    return base64.b64decode(data['content']).decode()

# Bảng tra đúng path thật (verify qua API — không suy đoán path) cho 12 skill
# chiến thuật Content Pro hay gọi tới:
TACTICAL_SKILLS = {
    "viral-hooks": "skills/viral-hooks/SKILL.md",
    "brand-voice": "skills/brand-voice/SKILL.md",
    "personal-voice": "skills/personal-voice/SKILL.md",
    "content-engine": "skills/content-engine/SKILL.md",
    "anti-ai-tells": "skills/anti-ai-tells/SKILL.md",
    "fact-checker": "skills/fact-checker/SKILL.md",
    "geo-aeo-content-optimization": "skills/geo-aeo-content-optimization/SKILL.md",
    "content-tiktok-script-writer": "skills/affiliate-skills/content-tiktok-script-writer.md",
    "content-twitter-thread-writer": "skills/affiliate-skills/content-twitter-thread-writer.md",
    "content-viral-post-writer": "skills/affiliate-skills/content-viral-post-writer.md",
    "automation-content-repurposer": "skills/affiliate-skills/automation-content-repurposer.md",
    "research-trending-content-scout": "skills/affiliate-skills/research-trending-content-scout.md",
}

# 4 skill chiến lược do chính Content Pro sở hữu (không đổi, ổn định hơn)
STRATEGIC_SKILLS = {
    "content-pillar-cluster-architecture": "agents/content-pro/skills/content-pillar-cluster-architecture/SKILL.md",
    "editorial-workflow-quality-gates": "agents/content-pro/skills/editorial-workflow-quality-gates/SKILL.md",
    "content-distribution-system": "agents/content-pro/skills/content-distribution-system/SKILL.md",
    "content-strategy-review-gate": "agents/content-pro/skills/content-strategy-review-gate/SKILL.md",
}

def load_skill(name):
    """
    Khi system-prompt Content Pro nói 'gọi skill X' — Hermes chạy hàm này
    thay vì tìm file cục bộ không tồn tại. Luôn lấy bản mới nhất từ kho.
    """
    path = TACTICAL_SKILLS.get(name) or STRATEGIC_SKILLS.get(name)
    if not path:
        return f"❌ Không tìm thấy skill '{name}' trong bảng tra — kiểm tra lại tên hoặc path trong kho."
    try:
        return fetch_skill_from_kho(path)
    except Exception as e:
        return f"❌ Lỗi fetch skill '{name}': {e}"
```

## Tầng Tay còn thiếu trên Hermes (đã note trong mcp-setup.md gốc, nhắc lại rõ ở đây)

Content Pro gốc dựa vào `web_search`/`vidIQ MCP` có sẵn trên Claude.ai — Hermes không có 2 tool này. Dùng hàm đã có trong `HERMES-ADAPTER-research-pro.md` thay thế:

| Content Pro cần | Thay bằng (từ Research Pro adapter) |
|---|---|
| `web_search` (research chủ đề/trend) | `tavily_search()` hoặc `ddg_search()` (free, không cần key) |
| `vidIQ MCP` (phân tích kênh YouTube/TikTok) | Chưa có thay thế free tương đương trên Hermes — cần giữ nguyên qua Claude.ai/Mission Control cho phần này, hoặc để trống, ghi rõ "cần chạy qua kênh khác" |

## Cách dùng thật trên Hermes

```python
# Khi cần viết hook cho 1 content:
hook_skill_content = load_skill("viral-hooks")
# → Hermes đọc nội dung này như instruction, áp dụng công thức trong đó

# Khi bắt đầu content mới cho brand chưa có khung:
pillar_skill = load_skill("content-pillar-cluster-architecture")
review_gate = load_skill("content-strategy-review-gate")
# → chạy 2 bước này TRƯỚC, đúng thứ tự đã quy định trong system-prompt gốc
```

## Vẫn còn 1 giới hạn thật (không giấu)

Cách fetch động này cần Hermes có kết nối mạng ổn định tới GitHub API mỗi lần cần skill — nếu mạng VPS chập chờn, nên cache lại nội dung skill đã fetch trong session (không fetch lại liên tục cùng 1 skill trong 1 lần chạy), nhưng vẫn fetch lại ở lần chạy mới để đảm bảo luôn là bản mới nhất.
