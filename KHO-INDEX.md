# KHO-INDEX — AI Vibe Toolkit
> Cập nhật: 21/08/2026 | Version: 3.0
> **Entry point duy nhất cho mọi agent. Fetch file này đầu tiên.**
> ⚠️ Bản v2.1 (tháng 6/2026) đã lệch nặng — số liệu, cấu trúc, danh sách agent đều cũ.
> Bản này viết lại toàn bộ sau đợt audit tổng 21/08/2026.

---

## Kho là gì

- **Repo:** https://github.com/tano2026/AI-Vibe-Toolkit
- **Chủ:** Nobitano — Founder Tano Agency, AI Implementation Partner cho SMB Việt Nam
- **Mục đích kép:**
  1. Vận hành thật — luật quyết định + agent chạy việc cho ABTRIP/An Bình/Tano Cafe/Wonder Mart/Trùm Sân Bay
  2. Content factory — mỗi entry đáng chú ý = 1 video TikTok/YouTube Shorts

---

## Số liệu thực tế (đếm lại 21/08/2026 qua GitHub API — KHÔNG dùng số liệu bản cũ)

| Folder | Số file | Ghi chú |
|---|---|---|
| /skills/ | 861 | Thư viện skill rời — chất lượng KHÔNG đều, xem Tier 3 bên dưới |
| /content/ | 330 (318 script, max #320) | Script video |
| /repos/ | 236 | GitHub repo đã research |
| /agents/ | 196 | Playbook + company/ + 7 Pro agent + 4 instance brand |
| /mcps/ | 57 | MCP server |
| /stacks/ | 17 | Combo workflow |
| /configs/, /deploy/, /VAULT/, /domain-packs/ | 24 | Hạ tầng/cấu hình |
| Tổng | 1.731 file | Tăng gần gấp đôi so với lần đếm gần nhất (966) |

---

## Cấu trúc 3 tầng (MỚI — thay hoàn toàn cách hiểu cũ "chỉ là kho tool")

```
TẦNG 0 — LUẬT CỨNG (đọc 1 lần, áp cho mọi việc)
  agents/company/EXPERT-CORE.md — ngưỡng số 7 vai trò (Research/Marketing/
    Sales/Content/Dev/Designer/Media): fit x intent >= 7, forecast 90%/60%,
    retention 70%/50%, contrast 4.5:1, no-fabrication...

TẦNG 1 — 7 PRO AGENT (chuẩn hoá đồng đều, có Adapter, tin cậy nhất)
  agents/research-analytics-pro/  (23 file, 12 skill)
  agents/content-pro/             (14 file, 5 skill)
  agents/sales-ceo/                (12 file, 5 skill)
  agents/infra-ops-agent/          (10 file, 4 skill)
  agents/digital-marketing-agent/  (8 file, 2 skill)
  agents/media-pro/                (6 file, 2 skill)
  agents/designer-pro/             (5 file, 2 skill)
  -> Mỗi cái tự đủ: README (spec+capability map) + ARCHITECTURE + system-prompt
     + skills/ riêng + HERMES-ADAPTER.md

TẦNG 2 — INSTANCE ĐÃ CÁ NHÂN HOÁ CHO BRAND (chạy thật, CHƯA audit chéo EXPERT-CORE)
  agents/trum-san-bay/              (27 file — nhiều nhất, pipeline chính)
  agents/yt-cashcow/                 (18 file)
  agents/shorts-affiliate-system/    (15 file)
  agents/anbinh-travel-ops-analyst/  (11 file)

TẦNG 3 — THƯ VIỆN SKILL RỜI (861 file, dùng chung, chất lượng không đều)
  skills/<ten-skill>/SKILL.md — đa số CHƯA được audit/verify, một số đã xác
  nhận chất lượng cao qua kiểm tra thật: skills/claude-ads/*,
  skills/systematic-debugging, skills/anti-ai-tells, skills/accessibility

CHƯA HOÀN THIỆN — cần quyết định giữ hay bỏ
  agents/rio-bot/       (8 file, KHÔNG có README/system-prompt)
  agents/smb-ai-team/   (3 file, gần trống)
```

Bản đồ tổng + cách nhân bản cho khách mới: agents/MASTER-TEMPLATE-MANIFEST.md — phân loại CORE (clone thẳng, không sửa) vs TENANT-CONFIG (brand playbook riêng từng khách).

---

## File cần dọn — chưa xoá, chỉ ghi nhận (cần Nobitano xác nhận trước khi xoá)

| File | Vấn đề |
|---|---|
| agents/HERMES-PLAYBOOK.md (24.633 ký tự, cập nhật 28/07/2026) vs agents/HERMES-GUIDE.md (5.207 ký tự) vs agents/HERMES-AGENTS.md (3.872 ký tự) | 3 file khác vai trò (PLAYBOOK = đầy đủ dán vào Project Instructions; GUIDE = đọc nhanh trước khi fetch; AGENTS = harness sinh tự động) nhưng KHÔNG ai ghi rõ thứ tự đọc — xem bảng "Agent nào đọc file nào" bên dưới, đã tạm làm rõ |
| agents/OPENCLAW-PLAYBOOK.md vs -GUIDE.md vs -TOOLKIT.md | Tương tự — 3 vai trò khác nhau, đã làm rõ thứ tự bên dưới |
| agents/CLAUDE-CODE-BRIDGE.md nhắc tới "Team Thục Hán" | Tên chưa từng xuất hiện trong toàn bộ audit/xây dựng phiên 21/08/2026 — CHƯA RÕ đây là gì, cần Nobitano xác nhận trước khi đưa vào tài liệu chính thức |
| agents/README.md (909 ký tự) | Chỉ mô tả "3 agents trong hệ thống" — không nhắc DeepSeek Harness hay 7 Pro Agent, cũng đã lỗi thời như KHO-INDEX bản cũ |

---

## Agent nào đọc file nào tiếp theo (ĐÃ LÀM RÕ THỨ TỰ — bản cũ thiếu)

| Agent | Đọc theo thứ tự |
|---|---|
| Hermes | 1. agents/HERMES-GUIDE.md (đọc nhanh) -> 2. agents/HERMES-PLAYBOOK.md (đầy đủ, dán Project Instructions) -> 3. Khi cần làm việc của 1 Pro agent cụ thể: agents/<pro-agent>/HERMES-ADAPTER.md |
| OpenClaw | 1. agents/OPENCLAW-GUIDE.md -> 2. agents/OPENCLAW-PLAYBOOK.md -> 3. agents/OPENCLAW-TOOLKIT.md (tra cứu nhanh, không cần fetch từng file lẻ) |
| Antigravity | 1. agents/ANTIGRAVITY-GUIDE.md -> 2. agents/ANTIGRAVITY-PLAYBOOK.md |
| DeepSeek Harness | Chưa có playbook riêng chính thức — hiện mượn quyết định qua OpenClaw (nền tảng DSH còn breaking changes, xem ghi chú trong lịch sử quyết định) |
| Claude Code | agents/CLAUDE-CODE-BRIDGE.md |
| Claude (Senior Advisor) | Không cần fetch trước — có Project Knowledge riêng. Cần hiểu tổ chức: agents/company/ORG-v2.md + agents/company/SENIOR-ADVISOR.md |
| Mọi agent, trước khi làm việc thuộc 1 trong 7 vai trò | agents/company/EXPERT-CORE.md — luật cứng, không tự hạ chuẩn |

Lớp hành vi nền cho MỌI agent làm việc liên quan code: agents/KARPATHY-CODING-GUIDELINES.md.

---

## Cách nạp skill — khuyến nghị MỚI (thay cách cũ)

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
# 4. Việc thuộc 1 trong 7 vai trò Pro Agent -> fetch("agents/<pro-agent>/README.md")
#    rồi HERMES-ADAPTER.md của đúng agent đó
```

Node.js (OpenClaw) và Bash (Antigravity) dùng cùng pattern — xem chi tiết trong HERMES-PLAYBOOK.md (áp dụng chung, chỉ đổi cú pháp HTTP request).

---

## Env vars toàn hệ thống (đã bổ sung biến mới từ phiên 21/08/2026)

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

# Decision Engine — Jev (TypeSafe, còn early access/waitlist)
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

1. ✅ research-pro.md đã xoá (21/08/2026, xác nhận trùng research-analytics-pro/). 3 cụm HERMES-*/OPENCLAW-* giữ nguyên (không trùng, chỉ khác vai trò — đã làm rõ thứ tự đọc). "Team Thục Hán" vẫn chưa xác nhận, chưa động vào.
2. agents/README.md cũng lỗi thời như KHO-INDEX bản cũ — chưa viết lại
3. Tier 2 (4 instance brand) chưa audit chéo EXPERT-CORE
4. Tier 3 (861 skill rời) — đa số chưa được đọc/verify, chỉ vài chục đã xác nhận qua kiểm tra thật
5. Swarms skills_dir — mới là đề xuất, chưa chạy Pilot thật
