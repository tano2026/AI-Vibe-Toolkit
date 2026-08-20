---
name: portable-skill-framework
description: >
  Khung viết skill để dùng chung được trên nhiều harness khác nhau (Mission
  Control/Paperclip, Claude Code, DeepSeek Harness...) mà không phải viết lại
  từ đầu mỗi lần đổi công cụ. Tách skill thành 2 lớp: Core (kiến thức/logic,
  không đổi) + Adapter (cách gắn vào từng harness cụ thể, đổi theo nơi lắp).
  Dùng khi viết skill mới cho OMC/OPC hoặc bất kỳ agent nào cần chạy đa nền tảng.
---

# Portable Skill Framework — Viết 1 lần, chạy nhiều nơi

## TL;DR
Vấn đề: 3 harness (Mission Control/Paperclip, Claude Code, DeepSeek Harness) có format hoàn toàn khác nhau — AGENTS.md 4 file rời vs YAML frontmatter 1 file vs plugin JSON-RPC. Viết riêng skill cho từng harness = 3 lần công, dễ lệch nhau khi update. Giải pháp: tách phần "nghĩ gì" (Core, viết 1 lần) khỏi phần "gọi tool cụ thể ra sao" (Adapter, viết ngắn cho từng harness).

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

| Hành động generic (viết trong Core) | Mission Control/Paperclip | Claude Code | DeepSeek Harness |
|---|---|---|---|
| Tìm kiếm web | (qua skill/tool đã cấp trong TOOLS.md) | `WebSearch` | plugin web-search (nếu cài) |
| Đọc nội dung trang web | — | `WebFetch` | tool fetch trong plugin |
| Đọc file | Read (nếu Claude Code chạy nền) | `Read` | tool file-read |
| Ghi file | Write (nếu có quyền) | `Write` | tool file-write |
| Tìm file theo pattern | — | `Glob` | — |
| Tìm nội dung trong nhiều file | — | `Grep` | — |
| Chạy lệnh shell | Antigravity (không tự chạy) | `Bash` | subprocess qua CLI |
| Gọi agent khác làm phụ | tạo subtask, gán agent khác | Task/subagent invocation | gọi Claude Code/Codex làm sub-agent (tính năng riêng DSH) |

Ô "—" nghĩa là harness đó chưa có tool tương đương sẵn — Core cần có fallback
("nếu không có tool X, làm Y thay thế") thay vì giả định tool luôn tồn tại.

### Format riêng từng harness (chi tiết kỹ thuật)

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
3. Test trên harness dễ nhất trước (thường Claude Code vì format rõ ràng nhất, ít mơ hồ nhất)
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
- Điểm yếu: thêm 1 lớp trừu tượng nghĩa là viết skill mới tốn thời gian hơn 1 chút ban đầu (phải tách đúng Core/Adapter thay vì viết thẳng 1 mạch); DeepSeek Harness còn quá mới, Adapter cho nó dễ lỗi thời nhanh
- Có nên dùng: 9/10 cho bất kỳ skill nào dự định dùng >1 harness — không cần áp dụng cho skill chỉ chạy 1 nơi duy nhất (over-engineering không cần thiết)

## Link
- Tham chiếu: repos/deepseek-harness.md (triết lý Model + Harness = Agent)
- Tham chiếu: agents/research-analytics-pro/subagents/market-research-analyst.md (ví dụ format Claude Code thật)
