# Small Business + Brock Skill Pack — Combo Skills cho Claude Cowork

## TL;DR
2 bộ skill pack cài sẵn cho Claude, biến Claude thành "nhân viên ảo" vận hành business nhỏ hằng ngày: một bộ chính chủ Anthropic (`skills-small-business`, 31 skills) và một bộ bên thứ ba do creator Brock đóng gói (`skills-brock-pack`, 15 skills, bán trên Gumroad). Cài xong là có nguyên bộ automation cho sổ sách, CRM, content, email — không phải tự viết prompt từ đầu.

## Các tool trong stack
1. **`skills-small-business/` (Anthropic chính chủ)** → tầng vận hành lõi: sổ sách (`close-month`, `tax-prep`), dòng tiền (`business-pulse`, `plan-payroll`, `cash-flow-snapshot`), CRM (`crm-cleanup`, `crm-maintenance`, `lead-triage`), khách hàng (`invoice-chase`, `customer-pulse-check`, `ticket-deflector`), tuyển dụng (`job-post-builder`), pháp lý nhẹ (`contract-review`), báo cáo định kỳ (`friday-brief`, `monday-brief`, `quarterly-review`). Đây chính là các skill `small-business:*` đã có sẵn trong danh sách skill của Claude — không cần cài thêm, chỉ cần trigger đúng câu.
2. **`skills-brock-pack/` (bên thứ ba, Gumroad)** → tầng năng suất cá nhân hằng ngày: `morning-briefing` (scan ngành mỗi sáng), `quick-research`, `email-drafter`, `slide-deck-builder`, `budget-dashboard`, `contract-reviewer`, `difficult-conversation-prep`, `learning-path-generator`. Đóng gói thành 1 file `.plugin` duy nhất, kéo thả vào Cowork là cài hết 15 skill cùng lúc.
3. **`connectors/`** → lớp kết nối dữ liệu thật cho cả 2 bộ trên chạy được: QuickBooks, Gmail, Slack, HubSpot. Không có connector thì skill chỉ chạy được ở chế độ "hỏi input tay", mất phần lớn giá trị auto-pull dữ liệu.

## Workflow ghép nối
```
Connector (QuickBooks/Gmail/Slack/HubSpot)
        ↓ cấp dữ liệu thật
skills-small-business/  →  vận hành định kỳ (đóng sổ, nhắc hoá đơn, dọn CRM, brief cuối tuần)
        +
skills-brock-pack/      →  tác vụ hằng ngày (brief sáng, research nhanh, soạn email, làm slide)
        ↓
Owner nhận output: brief/report/email draft, duyệt và cho chạy tiếp (invoice-chase, crm-cleanup có bước confirm trước khi ghi/gửi thật)
```
Nguyên tắc chọn: bộ Anthropic lo phần "business ops lặp lại theo lịch" (tuần/tháng), bộ Brock lo phần "trợ lý cá nhân mỗi ngày" (research, soạn thảo, slide). Hai bộ không chồng lấn nhiều, ghép được vì khác tầng.

## Ví dụ thực tế
Một solo owner (ví dụ áp cho ABTRIP hoặc Wonder Mart) kết nối QuickBooks + Gmail + HubSpot:
- 7h sáng: chạy `morning-briefing` (brock-pack) → biết ngay hôm nay có gì nóng trong ngành travel/e-commerce.
- Đầu tuần: chạy `monday-brief` (small-business) → 1 trang tóm tắt cash, sales, pipeline, top 3 việc cần làm.
- Có khách complain qua email → `ticket-deflector` kéo lịch sử đơn hàng từ HubSpot, soạn draft trả lời đúng giọng, có thể hoàn tiền qua PayPal nếu owner duyệt.
- Cuối tháng → `close-month` đối chiếu QuickBooks vs Stripe/PayPal, viết narrative P&L, xuất file đóng gói cho kế toán.
- Cần slide pitch nhanh cho investor → `slide-deck-builder` (brock-pack) ra deck có chart, không cần mở PowerPoint.

## Lưu ý / Lỗi thường gặp
- **`skills-brock-pack` KHÔNG phải chính chủ Anthropic** — là sản phẩm bán trên Gumroad của creator cá nhân (kênh dạy Claude Cowork), chất lượng phụ thuộc creator, không có SLA hay update cam kết như skill chính chủ. Tin vào review trước khi mua.
- 31 skill của Anthropic đã có sẵn trong Claude, **không cần cài .plugin** — chỉ cần biết đúng trigger phrase (vd nói "đóng sổ tháng này" tự động gọi `close-month`). Brock-pack thì phải cài file `.plugin` thủ công vào Cowork.
- Không kết nối connector nào (QuickBooks/Gmail/HubSpot) thì gần hết giá trị auto-pull mất, phải tự dán số liệu tay — mất phần lớn lý do dùng skill.
- Vài skill tên gần giống nhau giữa 2 bộ (`contract-review` vs `contract-reviewer`) dễ gây nhầm khi nói chuyện — nên biết rõ skill nào thuộc bộ nào để tránh gọi sai.
- Tác vụ có hành động thật (gửi email, hoàn tiền, ghi CRM) đều có bước confirm — đừng approve ẩu khi thấy "sẵn sàng gửi", đọc kỹ nội dung trước khi duyệt.

## Đánh giá cá nhân
- Điểm mạnh: bộ Anthropic cover gần hết vòng đời vận hành 1 SMB (cash, CRM, hoá đơn, tuyển dụng, báo cáo) mà không cần build agent riêng; brock-pack bù đúng phần năng suất cá nhân hằng ngày mà bộ chính chủ không có (research nhanh, slide, briefing sáng). Ghép 2 bộ = gần đủ bộ "trợ lý ảo" cho 1 người vận hành nhiều việc.
- Điểm yếu: brock-pack là third-party, rủi ro về maintenance/update dài hạn không rõ ràng; cả 2 bộ đều phụ thuộc nặng vào việc đã bật đúng connector, nếu thiếu connector thì giá trị giảm mạnh; không có agent state machine đứng sau (khác với pattern Harness Engineering — LLM tự quyết luồng theo skill trigger, dễ non-deterministic hơn agent tự build).
- Có nên dùng không: 7/10 — dùng tốt cho việc dựng nhanh 1 "văn phòng ảo" cho SMB không cần code, nhưng nếu đã có hệ agent riêng (như Hermes/OpenClaw) thì nên coi đây là tham khảo pattern hơn là thay thế, vì thiếu tầng guardrail/state machine cứng.

## Link
- Bộ small-business (chính chủ Anthropic): có sẵn trong Claude Skills, không cần link cài đặt riêng
- Brock's 15 Claude Cowork Skills (Gumroad): https://brockster6202.gumroad.com/l/15claudeskills
- Link nội bộ liên quan trong kho: [/skills/agentic-loop-optimizer] (Harness Engineering pattern để so sánh)

---

## 🤖 Agent Integration

### Hermes (Python)
> ⚠️ Skill pack này chạy trong Claude Cowork (context Claude, không phải REST API độc lập) — Hermes không gọi trực tiếp được. Nếu cần automation tương tự trên VPS, dùng làm **reference spec** để build sub-agent riêng theo pattern `agentic-factory` (xem `SKILL_AGENTIC_FACTORY.md`), map từng skill sang 1 hàm Python cụ thể thay vì phụ thuộc Claude Skills trigger.

### OpenClaw
```bash
# Không cài trực tiếp qua npx — đây là Claude-side skill, không phải MCP server hay npm package.
# Nếu muốn OpenClaw orchestrate luồng tương tự, gọi Claude API kèm system prompt mô phỏng
# đúng logic của skill (vd copy quy trình trong close-month/friday-brief) thay vì cài plugin.
```

### Antigravity
```bash
# Không cần deploy service riêng cho skill pack này — nó chạy trong Claude Cowork, không self-host được.
```
