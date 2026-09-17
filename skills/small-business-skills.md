# Small Business Skills — Claude for Small Business (Anthropic chính chủ)

## TL;DR
Plugin chính thức của Anthropic, cài 1 lần là có nguyên bộ máy vận hành small business trong Claude Cowork/Claude Code: 43 workflow gõ lệnh `/` hoặc nói tiếng thường, ~15 skill nền, router hiểu ngôn ngữ tự nhiên, và 37 connector nối vào tool thật (QuickBooks, HubSpot, Shopify, Gusto...).

## Tool này dùng để làm gì
Đây không phải 1 skill đơn lẻ mà cả 1 bộ skill pack cho chủ doanh nghiệp nhỏ — nói thẳng vấn đề bằng tiếng thường ("lo không đủ tiền trả lương", "khách đang giận") là Claude tự chọn đúng workflow và dẫn dắt từng bước, không cần nhớ lệnh nào làm gì. Mọi workflow bắt buộc dừng lại xin duyệt trước khi gửi/đăng/thanh toán — không có gì tự động chạy ngầm.

Cấu trúc thư mục thật trong repo (`small-business/`):
```
small-business-skills/     ← 31 quy trình đầy đủ (skills-small-business/)
  CLAUDE.md                ← quy tắc vận hành chung
  memory.md                ← bộ nhớ phiên làm việc
  business-pulse/          ← nhịp đập tình hình doanh nghiệp
  invoice-chase/           ← nhắc hoá đơn quá hạn
  friday-brief/            ← bản tin cuối tuần
  close-month/             ← đóng sổ cuối tháng
  tax-prep/                ← chuẩn bị thuế
  job-post-builder/        ← tạo bài đăng tuyển dụng
  contract-review/         ← rà soát hợp đồng
  cocia-onboarding/        ← onboarding khách hàng
  ... (+ nhiều skill khác)
skills-brock-pack/         ← 15 tự động hoá dùng hàng ngày
  morning-briefing/, quick-research/, email-drafter/,
  slide-deck-builder/, budget-dashboard/, contract-reviewer/,
  difficult-conversation-prep/, learning-path-generator/
connectors/                ← app kết nối: QuickBooks, Gmail, Slack, HubSpot...
```

## Setup từng bước
1. Trong Claude Cowork hoặc Claude Code, thêm marketplace 1 lần:
   ```
   /plugin marketplace add anthropics/knowledge-work-plugins
   ```
2. Cài plugin:
   ```
   /plugin install small-business@knowledge-work-plugins
   ```
3. Chạy `/smb-onboard` (hoặc gõ "set me up") — Claude tự hỏi về doanh nghiệp, điểm đau, tool đang dùng để cá nhân hoá router.
4. Nối connector cần thiết (không bắt buộc nối hết) — không có connector nào vẫn chạy được phần lớn workflow bằng cách upload file CSV/spreadsheet/statement.
5. Gọi workflow bằng lệnh `/` (vd `/monday-brief`) hoặc mô tả việc bằng tiếng thường, Claude tự route.

## Ví dụ thực tế
Áp cho **ABTRIP** hoặc **Wonder Mart**: gõ `/monday-brief` → Claude gom tiền mặt, doanh số, pipeline, lịch tuần, và 1 việc quan trọng nhất cần làm — gọn trong 1 trang. Hoặc không nhớ lệnh, cứ gõ thẳng "sắp tới không đủ tiền trả lương" → router tự chọn đúng workflow kiểm tra dòng tiền + nhắc hoá đơn quá hạn để bù, dẫn dắt từng bước tới khi có bản run sheet để duyệt.

## Lưu ý / Lỗi thường gặp
- Đây là plugin cho **Claude Cowork** (và Claude Code), không chạy được trên bản Claude.ai chat thường — cần đúng môi trường mới cài được.
- Số liệu "15 skill nền" trong tài liệu marketing và "31 skill nhỏ" ghi trong ảnh infographic của người dùng khác nhau — do bản plugin cập nhật liên tục (tài liệu chính thức hiện ghi 43 workflow tổng, số skill nền/workflow lẻ tẻ đổi theo từng bản release, đừng chốt cứng con số).
- Không có connector cũng dùng được — nhưng giá trị giảm nhiều, vì phần lớn workflow (đóng sổ, chốt lương, invoice chase) cần dữ liệu thật từ QuickBooks/Gusto/Stripe... để tự động, không thì phải tự upload file tay mỗi lần.
- Plugin nói rõ không thay thế tư vấn tài chính/thuế/pháp lý/HR — output vẫn cần người (hoặc chuyên gia) duyệt lại trước khi dùng thật.

## Đánh giá cá nhân
- **Điểm mạnh:** Chính chủ Anthropic nên chất lượng prompt/workflow đáng tin hơn hàng cộng đồng, router hiểu tiếng thường thật sự giảm rào cản (không cần nhớ 43 lệnh), cơ chế "luôn dừng chờ duyệt trước khi gửi/đăng/pay" là điểm an toàn quan trọng cho dữ liệu tài chính.
- **Điểm yếu:** Phụ thuộc nhiều vào connector để phát huy hết giá trị — công ty VN dùng tool không nằm trong 37 connector (vd phần mềm kế toán nội địa) thì phải tự nối qua Zapier bằng `build-connector`, tốn thêm công đoạn. Số liệu tài liệu (số skill, số workflow) thay đổi liên tục giữa các bản, dễ lạc hậu.
- **Có nên dùng không:** 8/10 cho ai đang vận hành doanh nghiệp nhỏ có sẵn ít nhất 1-2 tool trong danh sách connector (QuickBooks, HubSpot, Shopify...) — với ABTRIP/Wonder Mart cần xem trước có tool VN nào khớp connector sẵn không, không thì giá trị tụt xuống còn ~5/10.

## Link
- Trang chính thức: https://claude.com/plugins/small-business
- Repo GitHub: https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business
- Hướng dẫn cài đầy đủ: https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin

---

## 🤖 Agent Integration

### Hermes (Python)
Không có REST API riêng — plugin này chạy nội bộ trong Claude Cowork/Claude Code qua slash command, không gọi được bằng `urllib.request` như các MCP thường. Nếu Hermes cần dữ liệu tương tự (vd cash flow snapshot), phải tự viết script gọi thẳng API của QuickBooks/Stripe... chứ không thông qua plugin này.

### OpenClaw
```bash
# Nếu OpenClaw chạy trên máy có Claude Code cài sẵn plugin này,
# có thể subprocess gọi Claude Code CLI để trigger 1 workflow cụ thể
claude "/monday-brief"
```
> ⚠️ Cần đã cài plugin + nối connector từ trước trong đúng project/máy đó — không cài sẵn thì lệnh không tồn tại.

### Antigravity
```bash
# Lệnh cài plugin 1 lần trên máy/VPS có Claude Code, cho project cần dùng
claude
# trong Claude Code, chạy:
# /plugin marketplace add anthropics/knowledge-work-plugins
# /plugin install small-business@knowledge-work-plugins
```
> ⚠️ Plugin thuộc hệ Claude Cowork — cần xác nhận VPS đang chạy đúng bản Claude Code hỗ trợ plugin trước khi cài, không phải mọi bản CLI đều có lệnh `/plugin`.
