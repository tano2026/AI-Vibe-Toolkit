# Mission Control Agent Roster (từ rohitg00/awesome-claude-code-toolkit) — Stack

## TL;DR
6 agent prompt (Content Strategist, Growth Engineer, Marketing Analyst, Market Researcher, Competitive Analyst, và bộ 3 Orchestration) lấy từ repo `rohitg00/awesome-claude-code-toolkit`, ghép vào Mission Control để bổ sung năng lực cho 3 sub-agent hiện có (Sales & BD Lead, Content & Delivery Lead, Automation & Ops Lead) và cho CEO Agent điều phối.

## Các tool trong stack
1. **content-strategist.md** → viết editorial calendar theo topic cluster + keyword research, gắn được vào Content & Delivery Lead
2. **growth-engineer.md** → A/B test framework, funnel tracking, feature flag — gắn vào Automation & Ops Lead cho ABTRIP landing page
3. **marketing-analyst.md** → multi-touch attribution, CAC/LTV, marketing mix model — gắn vào Sales & BD Lead để đo ROI campaign Trùm Sân Bay
4. **market-researcher.md** → TAM/SAM/SOM top-down + bottom-up, thiết kế survey — dùng cho B2B Travel Platform đang deferred, cần số liệu trước khi resume
5. **competitive-analyst.md** → feature matrix, pricing comparison, positioning map — so ABTRIP với đối thủ Fast Track khác
6. **task-coordinator.md + workflow-director.md + multi-agent-coordinator.md** → 3 agent điều phối, đúng vai trò còn thiếu của CEO Agent "Nobitano" trong Mission Control (hiện SOUL.md/HEARTBEAT.md/TOOLS.md có nhưng chưa có logic phân rã task + quản lý dependency rõ ràng)

## Workflow ghép nối
CEO Agent (Mission Control) nhận task từ Nobitano → gọi **task-coordinator** phân rã thành các unit độc lập (vd: "launch campaign ABTRIP tháng sau" → tách ra market-researcher chạy trước, competitive-analyst chạy song song, content-strategist chờ 2 cái trên xong mới chạy) → **workflow-director** theo dõi checkpoint, cho phép resume nếu bị đứt giữa chừng (đặc biệt hữu ích vì Mission Control chạy trên VPS 24/7, có thể bị restart) → **multi-agent-coordinator** merge output của Sales/Content/Ops Lead lại thành báo cáo cuối cho Nobitano.

3 agent research/marketing (content-strategist, growth-engineer, marketing-analyst, market-researcher, competitive-analyst) đóng vai "chuyên gia" được task-coordinator gọi tới khi cần, không chạy thường trực.

## Ví dụ thực tế
Input: "Chuẩn bị launch Trụ 3 (auto-reply Zalo OA) sau khi rotate token xong."
→ task-coordinator tách: (1) competitive-analyst xem đối thủ đang auto-reply Zalo kiểu gì, (2) content-strategist viết kịch bản trả lời mẫu theo TONE.md ABTRIP, (3) growth-engineer thiết kế A/B test 2 kịch bản trả lời xem cái nào giữ khách hỏi tiếp nhiều hơn.
→ workflow-director track: nếu VPS restart giữa chừng lúc đang chạy (2), tự resume từ đó chứ không chạy lại từ đầu.
→ multi-agent-coordinator gộp kết quả 3 nhánh thành 1 báo cáo, báo Nobitano qua Telegram.

## Lưu ý / Lỗi thường gặp
- Cả 6 agent đều set `model: opus` mặc định trong frontmatter — hơi tốn với tần suất chạy 24/7 trên Mission Control, nên route qua OmniRoute gateway tag `reasoning`/`balanced` tùy việc thay vì mặc định Opus cho mọi call.
- Agent chỉ là prompt/process (file .md thuần), không có code thực thi kèm theo — phần nào cần số liệu thật (TAM/SAM, CAC/LTV) vẫn phải tự nối API/nguồn dữ liệu, agent chỉ định hướng phương pháp.
- `market-researcher` đề cập nguồn trả phí (Gartner, IDC, Statista) — với ABTRIP/Wonder Mart quy mô nhỏ, thay bằng nguồn miễn phí (báo cáo ngành hàng không VN, số liệu Cục Hàng không, khảo sát tự làm) rồi áp cùng phương pháp luận.

## Đánh giá cá nhân
- Điểm mạnh: đúng lỗ hổng Mission Control đang thiếu — có SOUL/HEARTBEAT/TOOLS nhưng chưa có logic điều phối DAG rõ ràng, 3 agent orchestration lấp đúng chỗ đó. Quy trình 9 bước mỗi agent research/marketing khá bài bản, không hời hợt.
- Điểm yếu: toàn bộ hướng tới sản phẩm SaaS/tech company chuẩn Mỹ (viết bằng tiếng Anh, ví dụ Gartner/IDC, GA4/Mixpanel) — phải tự dịch + Việt hóa số liệu/nguồn khi áp cho ABTRIP, Wonder Mart, Tano Cafe.
- Có nên dùng không: 7/10 — 3 agent orchestration đáng gắn ngay vào Mission Control, 5 agent còn lại dùng như checklist/quy trình tham khảo hơn là chạy nguyên si.

## Link
- Link tới từng file gốc trong repo:
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/business-product/content-strategist.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/business-product/growth-engineer.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/business-product/marketing-analyst.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/research-analysis/market-researcher.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/research-analysis/competitive-analyst.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/orchestration/task-coordinator.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/orchestration/workflow-director.md
  - https://github.com/rohitg00/awesome-claude-code-toolkit/blob/main/agents/orchestration/multi-agent-coordinator.md
- Repo gốc đã có trong kho: repos/awesome-claude-code-toolkit.md
