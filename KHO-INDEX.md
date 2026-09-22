# KHO-INDEX — AI Vibe Toolkit
> Cập nhật: 21/09/2026 | Version: 4.0
> **Entry point duy nhất cho mọi agent. Fetch file này đầu tiên.**
> ⚠️ Bản v3.0 (21/08/2026) sai số liệu /skills/ (báo 861, không nói rõ đây là tổng cả 2 tầng khác nhau) và không hề nhắc TRACKER.md. Bản này viết lại bằng cách quét full recursive tree qua GitHub API — số liệu chính xác 100% tại thời điểm quét, không suy đoán.

---

## Kho là gì

- **Repo:** https://github.com/tano2026/AI-Vibe-Toolkit
- **Chủ:** Nobitano — Founder Tano Agency, AI Implementation Partner cho SMB Việt Nam
- **Mục đích kép:**
  1. Vận hành thật — luật quyết định + agent chạy việc cho ABTRIP/An Bình/Tano Cafe/Wonder Mart/Trùm Sân Bay
  2. Content factory — mỗi entry curated (theo template chuẩn) = 1 video TikTok/YouTube Shorts

---

## Số liệu thực tế (quét full recursive tree qua GitHub API, 21/09/2026)

| Folder | Số file thật | Ghi chú |
|---|---|---|
| /skills/ | **591** — chia 2 tầng khác hẳn nhau, xem cảnh báo ngay dưới bảng | |
| /content/ | 333 (317 script đánh số, max hiện tại **#320** + 4 script không đánh số + 1 series HyperFrames riêng `airfare-decoded-hyperframes/`) | |
| /repos/ | 238 | GitHub repo đã research |
| /agents/ | 195 (13 file gốc + 14 package con) | Playbook + company/ + 7 Pro agent + 4 instance brand + rio-bot + smb-ai-team |
| /mcps/ | 57 | MCP server |
| /stacks/ | 16 | Combo workflow |
| /configs/ /deploy/ /VAULT/ /domain-packs/ /reports/ /tools/ | 26 (11+7+4+2+1+1) | Hạ tầng/cấu hình |
| Root (`TRACKER.md`, `KHO-INDEX.md`...) | 9 | |
| **Tổng** | **1.466 file** | Giảm so với bản cũ báo 1.731 — do các đợt dọn duplicate đã chạy sau 21/08 |

### ⚠️ CẢNH BÁO QUAN TRỌNG — `/skills/` có 2 tầng khác hẳn nhau, đừng gộp chung

```
Tầng "Template chuẩn" — 26 file nằm PHẲNG (skills/ten-skill.md)
  Đây là entry viết theo đúng quy trình kho: có TL;DR, setup, ví dụ thực tế,
  đánh giá cá nhân, mỗi cái có 1 script video đi kèm trong /content/.
  → Nằm trong TRACKER.md, tra trùng bằng Ctrl+F ở đó là đủ.
  → Ví dụ: skills/ponytail.md, skills/i-have-adhd.md

Tầng 3 "Thư viện thô" — 470 subfolder (skills/<ten>/SKILL.md), 565 file
  Là skill cộng đồng/third-party import hàng loạt, KHÔNG theo template kho,
  đa số CHƯA audit/verify, KHÔNG có script video đi kèm, KHÔNG nằm trong TRACKER.md.
  → Một số đã xác nhận chất lượng cao qua kiểm tra thật: skills/claude-ads/*,
    skills/systematic-debugging, skills/anti-ai-tells, skills/accessibility
  → 21/08/2026 báo 861 file, giờ còn 470 — do đã dọn bớt qua các đợt cleanup.
```

**Hệ quả thật cho việc tra trùng:** trước khi viết 1 entry Skill mới, phải tra CẢ 2 nơi —
TRACKER.md (tầng chuẩn) VÀ liệt kê thư mục `skills/<tên-nghi-ngờ>/` (tầng thô) — vì
Ctrl+F trong TRACKER.md một mình KHÔNG đủ, sẽ bỏ sót 470 skill kia.

---

## TRACKER.md — index tra cứu theo nội dung (MỚI, chưa có trong bản v3.0)

`TRACKER.md` ở root repo — tự sinh (không phải tay-append) từ nội dung thật của `/mcps` `/repos` `/skills` (chỉ tầng phẳng) `/stacks`, có cột Tóm tắt lấy từ TL;DR mỗi file, cột Agent Integration (Có/Không) để lọc tool nào có code gọi được ngay. Viết lại toàn bộ 21/09/2026, thay cho bản cũ (nhật ký lộn xộn qua ~90 batch, số ID bị trùng) — bản cũ lưu nguyên tại `TRACKER-ARCHIVE.md`, chỉ để tham khảo lịch sử, không tra cứu từ đó.

**Cách cập nhật khi thêm entry mới:** chạy lại script quét (build từ full repo tree), không tay-append dòng.

---

## Cấu trúc 3 tầng (v3.2 — sửa lỗi backtick + thêm agent thứ 8, 22/08/2026)

```
TẦNG 0 — LUẬT CỨNG (đọc 1 lần, áp cho mọi việc)
  agents/company/EXPERT-CORE.md — ngưỡng số 8 vai trò (Research/Marketing/
    Sales/Content/Dev/Designer/Media/Customer Satisfaction): fit x intent
    >= 7, forecast 90%/60%, retention 70%/50%, contrast 4.5:1, FCR >=70%,
    no-fabrication...
  agents/company/CORE-META-SKILLS.md — nhóm "Đầu Não" (harness/loop/
    superpowers/humanizer) — CẮT NGANG mọi Pro Agent, kiểm tra trước khi
    viết agent mới (xem Agentic Factory v2, Bước 1)

TẦNG 1 — 8 PRO AGENT (chuẩn hoá đồng đều, có Adapter, tin cậy nhất)
  agents/research-analytics-pro/     (23 file)
  agents/content-pro/                (14 file)
  agents/sales-ceo/                  (12 file)
  agents/infra-ops-agent/            (11 file)
  agents/digital-marketing-agent/    (8 file)
  agents/media-pro/                  (6 file)
  agents/customer-satisfaction-pro/  (6 file) — MỚI, agent thứ 8
  agents/designer-pro/               (5 file)
  -> Mỗi cái tự đủ: README (spec+capability map) + ARCHITECTURE + system-prompt
     + skills/ riêng + HERMES-ADAPTER.md

TẦNG 2 — INSTANCE ĐÃ CÁ NHÂN HOÁ CHO BRAND (chạy thật, CHƯA audit chéo EXPERT-CORE)
  agents/trum-san-bay/              (27 file — nhiều nhất, pipeline chính)
  agents/yt-cashcow/                 (18 file)
  agents/shorts-affiliate-system/    (15 file)
  agents/anbinh-travel-ops-analyst/  (11 file)

TẦNG 3 — THƯ VIỆN SKILL THÔ (591 file trong skills/, sau khi xoá ecc/ 271
  file trùng — số liệu đếm trực tiếp qua API, không suy đoán)

CHƯA HOÀN THIỆN — cần quyết định giữ hay bỏ
  agents/rio-bot/       (8 file, KHÔNG có README/system-prompt)
  agents/smb-ai-team/   (3 file, gần trống)
```

Bản đồ tổng + cách nhân bản cho khách mới: agents/MASTER-TEMPLATE-MANIFEST.md — phân loại CORE (clone thẳng, không sửa) vs TENANT-CONFIG (brand playbook riêng từng khách).

---

## Agent nào đọc file nào tiếp theo

| Agent | Đọc theo thứ tự |
|---|---|
| Hermes | 1. agents/HERMES-GUIDE.md (đọc nhanh) -> 2. agents/HERMES-PLAYBOOK.md (đầy đủ, dán Project Instructions) -> 3. Khi cần làm việc của 1 Pro agent cụ thể: agents/<pro-agent>/HERMES-ADAPTER.md |
| OpenClaw | 1. agents/OPENCLAW-GUIDE.md -> 2. agents/OPENCLAW-PLAYBOOK.md -> 3. agents/OPENCLAW-TOOLKIT.md (tra cứu nhanh, không cần fetch từng file lẻ) |
| Antigravity | 1. agents/ANTIGRAVITY-GUIDE.md -> 2. agents/ANTIGRAVITY-PLAYBOOK.md |
| DeepSeek Harness | Chưa có playbook riêng chính thức — hiện mượn quyết định qua OpenClaw (nền tảng DSH còn breaking changes, xem ghi chú trong lịch sử quyết định) |
| Claude Code | agents/CLAUDE-CODE-BRIDGE.md |
| Claude (Senior Advisor) | Không cần fetch trước — có Project Knowledge riêng. Cần hiểu tổ chức: agents/company/ORG-v2.md + agents/company/SENIOR-ADVISOR.md |
| Mọi agent, trước khi làm việc thuộc 1 trong 7 vai trò | agents/company/EXPERT-CORE.md — luật cứng, không tự hạ chuẩn |
| Mọi agent, khi cần tra "kho có tool gì cho việc X" | TRACKER.md (xem mục ngay trên) |

**"Team Thục Hán"** = biệt danh Nobitano đặt cho bộ 3 Hermes/OpenClaw/DeepSeek Harness khi
gộp chung thành 1 project riêng gọi là **OPC** — giao tiếp nội bộ qua file `tasks/*.md`,
tách biệt runtime với Claude Code (xem agents/CLAUDE-CODE-BRIDGE.md). Không phải hệ thống
khác, chỉ là tên gọi khi 3 agent này hoạt động cùng nhau trong OPC.

Lớp hành vi nền cho MỌI agent làm việc liên quan code: agents/KARPATHY-CODING-GUIDELINES.md.

---

## Cách nạp skill — khuyến nghị (từ v3.0, chưa có cập nhật mới)

Cách cũ (đang tồn tại trong 1 số Hermes Adapter): mỗi agent tự viết dict cứng {"tên-skill": "path"} rồi fetch tay từng cái qua GitHub API. Hoạt động nhưng phải tự maintain danh sách, dễ quên khi thêm skill mới.

Cách khuyến nghị (từ khi research Swarms framework, 21/08/2026): dùng skills_dir — Swarms đọc THẲNG cấu trúc skills/<name>/SKILL.md đang dùng, tự chọn đúng skill theo độ liên quan tác vụ, không cần biết trước tên:

```python
from swarms import Agent
agent = Agent(model_name="claude-sonnet-4-6", skills_dir="./skills")
agent.run("Chấm điểm deal theo fit x intent")
# Tự nạp đúng skill liên quan, không cần dict cứng
```

Chi tiết: repos/swarms.md. Đang ở giai đoạn đề xuất — chưa test thật với Pilot 1 agent, xem ghi chú trong file đó trước khi tin dùng production.

---

## Fetch function chuẩn (Python/Hermes)

```python
import urllib.request, json, base64, os

def fetch(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}",
        headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}",
                 "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode()

# Workflow chuẩn khi nhận task:
# 1. fetch("KHO-INDEX.md")                    -> map toàn bộ kho (file này)
# 2. fetch("agents/company/EXPERT-CORE.md")   -> luật cứng áp dụng
# 3. fetch("agents/HERMES-GUIDE.md")          -> hướng dẫn nhanh
# 4. Cần tra "kho có gì cho việc X" -> fetch("TRACKER.md")
# 5. Việc thuộc 1 trong 7 vai trò Pro Agent -> fetch("agents/<pro-agent>/README.md")
#    rồi HERMES-ADAPTER.md của đúng agent đó
```

**Lưu ý khi list folder qua Contents API (`/contents/<path>`):** API này KHÔNG đệ quy —
với `/skills/` sẽ chỉ trả về 26 file tầng phẳng, bỏ sót toàn bộ 470 subfolder Tầng 3.
Muốn quét đầy đủ, dùng Git Trees API với `?recursive=1`:
```python
req = urllib.request.Request(
    "https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/git/trees/main?recursive=1",
    headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}",
             "Accept": "application/vnd.github.v3+json"})
tree = json.loads(urllib.request.urlopen(req).read())["tree"]
```

Node.js (OpenClaw) và Bash (Antigravity) dùng cùng pattern — xem chi tiết trong HERMES-PLAYBOOK.md (áp dụng chung, chỉ đổi cú pháp HTTP request).

---

## Env vars toàn hệ thống

```bash
# GitHub
GITHUB_TOKEN=

# Search/Scrape
BRAVE_API_KEY=
TAVILY_API_KEY=
FIRECRAWL_API_KEY=

# LLM
ANTHROPIC_API_KEY=

# Media — Google Flow MCP (Nano Banana/Veo, API chính thức — xem mcps/google-flow-mcp.md
# để phân biệt với 4 tool TRÙNG TÊN rủi ro ToS khác)
GOOGLE_API_KEY=

# Decision Engine — Jev (TypeSafe, còn early access/waitlist — xem repos/typesafe-jev.md)
TYPESAFE_API_KEY=

# CRM — Sales-CEO
HUBSPOT_TOKEN=

# Ads — Digital Marketing Agent (cần OAuth thủ công 1 lần, xem HERMES-ADAPTER.md agent đó)
GOOGLE_ADS_REFRESH_TOKEN=

# Media cũ
FAL_KEY=
MINIMAX_API_KEY=
MINIMAX_GROUP_ID=
YOUTUBE_API_KEY=

# Database
SUPABASE_URL=
SUPABASE_KEY=

# Email
RESEND_API_KEY=

# Social
META_ACCESS_TOKEN=
TIKTOK_SESSION=

# Memory
MEM0_API_KEY=
```

---

## Việc tồn đọng thật — không giấu

1. ✅ Số liệu /skills/ đã sửa đúng (591 thật, tách rõ 2 tầng) — bản v3.0 báo 861 gộp chung, gây hiểu lầm là 1 khối đồng nhất.
2. ✅ TRACKER.md đã viết lại 21/09/2026 (tự sinh, không tay-append) — bản cũ lưu tại TRACKER-ARCHIVE.md.
3. ⚠️ **Tra trùng qua TRACKER.md một mình KHÔNG đủ** cho entry loại Skill — phải kiểm cả `skills/<tên>/` (Tầng 3) trước khi viết mới, quy trình dedup hiện tại (Claude, khi Nobitano giao task viết kho) cần cập nhật lại bước này.
4. agents/README.md vẫn lỗi thời như bản v2.1 cũ — chưa viết lại, chỉ mô tả "3 agent trong hệ thống", không nhắc DeepSeek Harness hay 7 Pro Agent.
5. Tier 2 (4 instance brand) chưa audit chéo EXPERT-CORE.
6. Tier 3 (470 skill thô) — đa số chưa được đọc/verify, chỉ vài chục đã xác nhận qua kiểm tra thật.
7. Swarms skills_dir — mới là đề xuất, chưa chạy Pilot thật.
