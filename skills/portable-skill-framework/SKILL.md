---
name: portable-skill-framework
description: >
  Khung viết skill để dùng chung được trên nhiều harness khác nhau (Hermes,
  Claude Code, Mission Control/Paperclip, DeepSeek Harness...) mà không phải
  viết lại từ đầu mỗi lần đổi công cụ. Tách skill thành 2 lớp: Core (kiến
  thức/logic, không đổi) + Adapter (cách gắn vào từng harness cụ thể, đổi
  theo nơi lắp). Dùng khi viết skill mới cho OMC/OPC hoặc bất kỳ agent nào
  cần chạy đa nền tảng.
---

# Portable Skill Framework — Viết 1 lần, chạy nhiều nơi

## TL;DR
Vấn đề: 4 harness (Hermes, Claude Code, Mission Control/Paperclip, DeepSeek Harness) có format hoàn toàn khác nhau — Python thuần `urllib` vs YAML frontmatter 1 file vs AGENTS.md 4 file rời vs plugin JSON-RPC. Viết riêng skill cho từng harness = 4 lần công, dễ lệch nhau khi update. Giải pháp: tách phần "nghĩ gì" (Core, viết 1 lần) khỏi phần "gọi tool cụ thể ra sao" (Adapter, viết ngắn cho từng harness).

> Hermes và Claude Code là 2 harness đang dùng thật hàng ngày (không phải thử
> nghiệm như DeepSeek Harness) — ưu tiên viết Adapter cho 2 cái này trước khi
> làm Mission Control/DeepSeek Harness nếu phải chọn thứ tự.

## Khi nào dùng
- Viết skill mới cần chạy được trên >1 harness (đúng case OMC/OPC hiện tại)
- Convert skill cũ (đã viết riêng cho 1 harness) sang dùng được đa nền tảng
- Chuẩn hoá cách Content Lead/Nobitano thêm harness mới trong tương lai mà không phải sửa lại toàn bộ skill cũ

## Nội dung skill / prompt

### Nguyên tắc tách lớp

```
CORE (viết 1 lần, không đổi dù chạy đâu):
  - Kiến thức nền, quy trình tư duy, nguyên tắc quyết định
  - Viết bằng ngôn ngữ tự nhiên + pseudocode thuần
  - KHÔNG nhắc tên tool cụ thể của bất kỳ harness nào
    (không viết "WebSearch", không viết "dsh plugin", chỉ viết
    "tìm kiếm web", "đọc file", "gọi API bên ngoài")
  - Đây là phần con người đọc hiểu logic mà không cần biết chạy ở đâu

ADAPTER (viết ngắn, riêng từng harness):
  - Chỉ làm 1 việc: map hành động generic trong Core → đúng cú pháp/tool
    thật của harness đó
  - Không lặp lại logic/kiến thức đã có trong Core
  - Khi Core đổi → Adapter thường KHÔNG cần đổi (trừ khi hành động mới
    xuất hiện mà harness đó chưa có tool tương ứng)
```

### Cấu trúc file skill portable (áp dụng khi viết mới)

```markdown
# [Tên Skill]

## Core
[Toàn bộ TL;DR, nguyên tắc, quy trình quyết định — viết 1 lần bằng ngôn ngữ
tự nhiên/pseudocode. Đây là phần dài nhất, ổn định nhất.]

## Harness Adapters

### → Mission Control / Paperclip
[Core map vào đâu trong 4 file AGENTS.md/SOUL.md/HEARTBEAT.md/TOOLS.md]

### → Claude Code
[Core map vào YAML frontmatter (name/description/tools/model) — dùng làm
Skill (.claude/skills/<name>/SKILL.md) hay Subagent (.claude/agents/<name>.md)]

### → DeepSeek Harness
[Core map vào plugin/procedure của dsh — lưu ý DSH còn breaking changes,
verify trước khi rely]
```

### Bảng dịch hành động generic → tool thật từng harness (dùng khi viết Adapter)

| Hành động generic (viết trong Core) | Hermes (Python, urllib thuần) | Claude Code | Mission Control/Paperclip | DeepSeek Harness |
|---|---|---|---|---|
| Tìm kiếm web | `tavily_search()`/`exa_search()` qua urllib POST (xem system-prompt.md Research Analytics Pro), hoặc fallback DuckDuckGo/HN/Wikipedia free API | `WebSearch` | (qua skill/tool đã cấp trong TOOLS.md) | plugin web-search (nếu cài) |
| Đọc nội dung trang web | `fetch(url)` + `strip_html()` — hàm urllib thuần đã có sẵn | `WebFetch` | — | tool fetch trong plugin |
| Đọc file | `open(path).read()` hoặc `read_file()` (MarkItDown cho PDF/Excel/Word) | `Read` | Read (nếu Claude Code chạy nền) | tool file-read |
| Ghi file | `open(path, 'w').write()` | `Write` | Write (nếu có quyền) | tool file-write |
| Tìm file theo pattern | module `glob` (built-in, không cần pip) | `Glob` | — | — |
| Tìm nội dung trong nhiều file | `os.walk()` + `re` (built-in) | `Grep` | — | — |
| Chạy lệnh shell | KHÔNG tự chạy — báo Antigravity thực thi (giới hạn bảo mật cố ý) | `Bash` | Antigravity (không tự chạy) | subprocess qua CLI |
| Gọi API bên thứ 3 (GitHub, Airtable...) | `urllib.request` thuần, tự build header/JSON | Tool có sẵn hoặc `Bash`+curl | qua MCP đã cấp | plugin tương ứng |
| Cài thêm thư viện | KHÔNG — bắt buộc chỉ `urllib`/stdlib | `pip install`/`npm install` được | tuỳ hạ tầng | `dsh plugin add` |
| Gọi agent khác làm phụ | Không tự spawn — báo OpenClaw điều phối | Task/subagent invocation | tạo subtask, gán agent khác | gọi Claude Code/Codex làm sub-agent (tính năng riêng DSH) |

Ô "—" nghĩa là harness đó chưa có tool tương đương sẵn — Core cần có fallback
("nếu không có tool X, làm Y thay thế") thay vì giả định tool luôn tồn tại.

**Ràng buộc riêng của Hermes — quan trọng nhất khi viết Adapter cho nó:**
Hermes CHỈ được dùng `urllib.request` và các module built-in Python (`json`,
`re`, `glob`, `os`, `time`, `base64`...) — **không được `pip install` bất cứ
gì**. Mọi Adapter viết cho Hermes phải tự implement bằng tay (vd tự POST JSON
qua `urllib` thay vì `import requests`). Đây không phải giới hạn kỹ thuật
tạm thời — là quy tắc cố định của toàn bộ hạ tầng Hermes, viết Adapter vi
phạm quy tắc này sẽ không chạy được trên máy thật.

### Format riêng từng harness (chi tiết kỹ thuật)

**Hermes — Python thuần, không file cấu hình riêng:**
```python
# Core của skill portable → viết thành 1 module Python độc lập, import được
# vào bất kỳ script Hermes nào. Không có "file cấu hình" như 3 harness kia —
# Adapter CHÍNH LÀ code Python thật.

import urllib.request, json, re

def fetch(url, headers=None):
    h = {"User-Agent": "Mozilla/5.0"}
    if headers: h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode('utf-8', errors='ignore')

# Core logic (nguyên tắc/quyết định) viết thành docstring hoặc comment ngay
# trên hàm — để người đọc code vẫn hiểu được "tại sao", không chỉ "làm gì"
def evaluate_source_reliability(url, content):
    """
    Core logic (từ skill source-evaluation):
    - Nguồn chính chủ/chính phủ > báo chí uy tín > blog/community
    - Domain quá mới (<1 năm, check RDAP) → hạ độ tin cậy
    - Không tự bịa số liệu nếu không tìm thấy nguồn
    """
    # ... implement thật ở đây
    pass
```
Nạp vào workflow: Hermes chạy qua lệnh Telegram → gọi script Python có import
module Core này → không cần bước "cài đặt" hay "đăng ký skill" như 3 harness
kia, chỉ cần đúng path file trên máy Windows (agent-core).

**Mission Control/Paperclip — 4 file:**
```
AGENTS.md   → Role/Summary/Expertise & Responsibilities/Priorities/
              Boundaries/Tools & Permissions/Communication/
              Collaboration & Escalation (7 section, xem template
              đã dùng cho Sales & BD Lead trước đó)
SOUL.md     → Identity/Personality/Communication style/Values/Boundaries
HEARTBEAT.md → Quy trình lặp lại mỗi chu kỳ (thứ tự bước)
TOOLS.md    → Danh sách quyền hạn cụ thể
```
Core của skill portable → nội dung chính đưa vào phần "Expertise &
Responsibilities" của AGENTS.md (hoặc gắn qua tab Skills riêng nếu Mission
Control hỗ trợ — CHƯA verify được schema chính xác của tab đó, cần Nobitano
tự kiểm tra khi tạo skill thật trong dashboard).

**Claude Code — YAML frontmatter:**
```yaml
---
name: <tên-skill-kebab-case>
description: <mô tả, bao gồm rõ trigger — khi nào Claude Code nên tự gọi skill này>
tools: WebSearch, WebFetch, Read, Write, Glob, Grep    # chỉ liệt kê tool thật cần
model: inherit    # hoặc chỉ định model cụ thể
---
```
Đặt tại `.claude/skills/<name>/SKILL.md` (dùng như skill bị động, Claude tự
trigger theo description) hoặc `.claude/agents/<name>.md` (dùng như subagent
được gọi tường minh qua Task tool).

**DeepSeek Harness — plugin/procedure:**
```bash
dsh plugin --profile <profile> add <package-hoặc-git-spec>
```
Core → viết thành system-prompt/procedure gắn vào profile đó. DSH còn ở bản
`0.1.0-rc.5` (xem `repos/deepseek-harness.md`), API có thể đổi — luôn kiểm
tra lại cú pháp mới nhất trước khi deploy thật, đừng copy nguyên cú pháp cũ
nếu đã lâu không cập nhật.

## Setup từng bước
1. Viết Core trước — thử tự hỏi "nếu bỏ hết tên tool cụ thể, phần này còn hiểu được không?" Nếu không → đang lẫn Adapter vào Core, tách lại.
2. Với mỗi harness cần chạy, viết Adapter riêng theo bảng dịch hành động ở trên
3. Test trên harness đang dùng thật hàng ngày trước — Hermes hoặc Claude Code (format Claude Code rõ ràng nhất để verify logic đúng chưa; Hermes cần verify thêm vì bị giới hạn urllib-only, dễ lộ ra chỗ Core lỡ giả định có thư viện ngoài)
4. Verify Core không bị "ăn gian" — nếu Adapter phải giải thích thêm logic mà Core chưa có, quay lại bổ sung Core, không vá trực tiếp vào Adapter (Adapter phình to = dấu hiệu tách lớp sai)

## Ví dụ thực tế
Áp thử với skill `source-evaluation` đã có trong Research Analytics Pro (Claude Code format sẵn, dùng Read/Write/WebSearch...). Core của nó (nguyên tắc chấm độ tin cậy nguồn: Primary/Secondary/Tertiary, ưu tiên nguồn nào hơn nguồn nào) hoàn toàn không nhắc tool cụ thể — có thể copy y nguyên sang Mission Control (nhét vào AGENTS.md của agent research) hoặc DeepSeek Harness mà không cần viết lại 1 chữ nào trong phần logic, chỉ cần thêm đúng 3-5 dòng Adapter cho mỗi nơi.

## Lưu ý / Lỗi thường gặp
- Sai lầm phổ biến nhất: viết Core mà vẫn lẫn tên tool cụ thể ("dùng WebSearch để tìm...") — làm vậy thì Core không portable nữa, phải sửa cả phần logic khi đổi harness
- Đừng cố làm Adapter "thông minh" — Adapter chỉ dịch cú pháp, mọi quyết định/logic phải nằm trong Core
- Harness mới xuất hiện (case DeepSeek Harness) → chỉ cần viết thêm 1 Adapter mới, không đụng vào Core đã ổn định của các skill cũ
- Không phải mọi skill đều portable tốt — skill phụ thuộc sâu vào 1 tính năng đặc thù của 1 harness (vd tính năng gọi Claude Code làm sub-agent chỉ DeepSeek Harness có) thì chấp nhận không portable 100%, ghi rõ giới hạn thay vì cố ép

## Đánh giá cá nhân
- Điểm mạnh: giảm công viết lại khi mở rộng harness mới (đúng nhu cầu OMC/OPC hiện tại), dễ maintain vì sửa Core 1 chỗ áp dụng mọi nơi, khớp tự nhiên với triết lý "Model + Harness = Agent" đã thấy ở DeepSeek Harness
- Điểm yếu: thêm 1 lớp trừu tượng nghĩa là viết skill mới tốn thời gian hơn 1 chút ban đầu (phải tách đúng Core/Adapter thay vì viết thẳng 1 mạch); DeepSeek Harness còn quá mới, Adapter cho nó dễ lỗi thời nhanh; Hermes bị giới hạn urllib-only nên Adapter cho Hermes thường dài hơn hẳn 3 harness kia (phải tự implement thay vì gọi thư viện có sẵn)
- Có nên dùng: 9/10 cho bất kỳ skill nào dự định dùng >1 harness — không cần áp dụng cho skill chỉ chạy 1 nơi duy nhất (over-engineering không cần thiết)

## Link
- Tham chiếu: repos/deepseek-harness.md (triết lý Model + Harness = Agent)
- Tham chiếu: agents/research-analytics-pro/subagents/market-research-analyst.md (ví dụ format Claude Code thật)
