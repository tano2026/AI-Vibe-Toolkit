# awesome-claude-code-toolkit (rohitg00) — GitHub Repo

## TL;DR
Kho tổng hợp lớn nhất hiện tại cho Claude Code: 135 agent, 176+ plugin, 42 command, 35 skill dựng sẵn (+400.000 skill khác qua marketplace SkillKit), 20 hook, 15 rule, 26 companion app. 2.5K sao, Apache-2.0, cập nhật gần như hàng ngày. Dùng làm **thư mục tra cứu** — không cài trọn bộ, chỉ lấy đúng agent/skill/plugin cần.

## Repo này dùng để làm gì
Đây không phải 1 tool đơn — nó là "index of index", gom mọi mảnh Claude Code ecosystem vào 1 chỗ, chia theo loại rõ ràng:
- **Agents (135)**: chia theo 9 nhóm — Core Development, Language Experts, Infrastructure, QA, Data & AI, Developer Experience, Specialized Domains, **Business & Product** (12 agent: Content Strategist, Growth Engineer, Marketing Analyst, Legal Advisor...), Orchestration, Research & Analysis (11 agent: Market Researcher, Competitive Analyst, Trend Analyst...).
- **Skills (35 curated + hàng chục community skill nổi bật)**: gồm cả mảng dev thuần (TDD, API design, Postgres...) lẫn mảng marketing/content rất hợp với Tano Agency — ví dụ `claude-code-marketing-skills` (SEO Audit, Landing Page Review, Ad Copy Writer), `linkedin-skills` (10 skill LinkedIn: viral hook, humanizer, content planner), `SuperSEO Skills` (11 skill SEO tự fetch trang top-rank đối thủ, không cần export keyword thủ công), `claude-seo`/`claude-ads`/`claude-blog` (bộ 3 của cùng 1 tác giả: SEO suite 30+ skill, ad audit đa nền tảng, blog engine).
- **Cost Optimizer skill** đáng chú ý: `skill-cost-optimizer` (giảm 60-80% chi phí token qua model routing thông minh) và `TokenWise` (tự route Haiku/Sonnet/Opus theo loại task, log ra $ tiết kiệm thật) — hợp để tối ưu OmniRoute gateway đang dùng.
- **Plugin marketplace cơ chế**: cài qua `/plugin marketplace add rohitg00/awesome-claude-code-toolkit` rồi `/plugin install <tên>` — giống mô hình Nobitano có thể tham khảo để tự làm marketplace nội bộ cho các agent package trong kho riêng.

## Setup từng bước
1. Không cài nguyên repo — duyệt README tìm đúng thứ cần trước.
2. Cài qua plugin marketplace (khuyên dùng):
```bash
/plugin marketplace add rohitg00/awesome-claude-code-toolkit
```
3. Hoặc clone thủ công 1 phần cụ thể (agent/skill):
```bash
git clone https://github.com/rohitg00/awesome-claude-code-toolkit.git ~/.claude/plugins/claude-code-toolkit
```
4. Một số skill/agent trong danh sách là link ra repo riêng của tác giả khác — bấm vào link đó, cài theo hướng dẫn riêng (không nằm chung trong repo này).

## Ví dụ thực tế
Cần agent research thị trường cho Tano Agency → tham chiếu thẳng trong CLAUDE.md của agent package:
```markdown
## Agents
- Use `agents/research-analysis/market-researcher.md` cho market sizing, TAM/SAM/SOM
- Use `agents/business-product/content-strategist.md` cho content calendar + topic clustering
```
Muốn tối ưu chi phí OmniRoute → cài thử `TokenWise` để tự động route model rẻ/đắt theo độ khó task, xem log NDJSON ước tính tiết kiệm được bao nhiêu $ trước khi quyết định tích hợp thật vào gateway.

## Lưu ý / Lỗi thường gặp
- README nói 2.5K sao/850+ file nhưng phần lớn "skill/plugin" trong bảng chỉ là LINK trỏ ra repo GitHub của người khác, không phải code nằm sẵn trong repo này — chất lượng/độ maintain khác nhau tùy tác giả, phải tự đánh giá từng cái trước khi dùng.
- SkillKit marketplace (400.000+ skill) là dịch vụ bên thứ 3 (`agenstskills.com`), không phải do rohitg00 kiểm soát — cẩn trọng trước khi cài skill lạ không rõ nguồn qua đó, nên ưu tiên skill có repo GitHub riêng kiểm tra được.
- Trùng ý tưởng với `ComposioHQ/awesome-claude-skills` đã có trong kho — 2 repo bổ sung nhau chứ không thay thế: bên kia mạnh về connector dịch vụ (Slack, Jira...), bên này mạnh về agent + plugin + skill dev/business.

## Đánh giá cá nhân
- Điểm mạnh: phân loại rõ ràng theo vai trò (đặc biệt nhóm Business & Product và Research & Analysis rất sát nhu cầu agency 1 người của Nobitano), có cả cost-optimizer skill thực chiến, cập nhật gần như mỗi ngày.
- Điểm yếu: quá nhiều — dễ bị choáng, và như đã nói phần lớn chỉ là link tổng hợp chứ tác giả gốc không kiểm duyệt chất lượng từng cái, một số item community-added thiếu star/review.
- Có nên dùng không: 7.5/10 — nên dùng làm "bản đồ tra cứu" định kỳ (mỗi tháng lướt 1 lần tìm agent/skill mới hợp cho kho), không nên cài nguyên bộ 1 lần.

## Link
- Repo: https://github.com/rohitg00/awesome-claude-code-toolkit
- Docs/Demo: README.md ngay trong repo (1233 dòng, đầy đủ bảng agent/skill/plugin)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request
# Lấy README để tra cứu agent/skill mới định kỳ
url = "https://raw.githubusercontent.com/rohitg00/awesome-claude-code-toolkit/main/README.md"
readme = urllib.request.urlopen(url).read().decode('utf-8')
# Có thể tự parse bảng markdown tìm agent/skill mới chưa có trong kho
```

### OpenClaw
```bash
git clone https://github.com/rohitg00/awesome-claude-code-toolkit.git ~/.openclaw/reference/claude-code-toolkit
```

### Antigravity
```bash
git clone https://github.com/rohitg00/awesome-claude-code-toolkit.git ~/.antigravity/reference/claude-code-toolkit
```
> ⚠️ Repo này để THAM KHẢO, không cài production trực tiếp qua Antigravity — mỗi agent/skill cần đánh giá riêng trước khi đưa vào kho chính thức.
