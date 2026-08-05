---
name: digital-marketing-orchestrator
description: >
  Router cho mọi yêu cầu digital marketing — phân loại request vào đúng skill
  chuyên môn (ads/SEO/social/content/outbound/CRO) đã có sẵn trong kho, quyết định
  có cần gọi MCP không, và có cần confirm trước khi hành động thật không.
  Dùng skill này ĐẦU TIÊN khi nhận bất kỳ yêu cầu marketing nào, trước khi gọi
  thẳng 1 skill chuyên môn cụ thể.
  Trigger: bất kỳ yêu cầu nào về chiến lược marketing, ads, SEO, social, outbound,
  CRO, campaign, brand cho ABTRIP/Tano/Wonder Mart/Tano Cafe.
---

# Digital Marketing Orchestrator

Đây là lớp điều phối, KHÔNG tự làm chuyên môn marketing — việc đó để các skill
chuyên môn đã có sẵn trong kho lo (`expert-digital-marketing`, `claude-ads/*`,
`claude-seo-commands`, `social-media-stack`...). Vai trò của skill này là quyết
định: gọi cái nào, theo thứ tự gì, có cần data MCP thật không, có cần confirm không.

## Quy trình

### Bước 1 — Phân loại request
Đọc yêu cầu, xếp vào 1 hoặc nhiều nhóm:
```
STRATEGY   — chiến lược, định vị thương hiệu, market research
ADS        — tạo/tối ưu/audit ads (Google/Meta/TikTok/YouTube)
SEO        — technical SEO, content SEO, AI-search visibility
CONTENT    — viết copy, content strategy, brand voice
SOCIAL     — lịch đăng, publish, cross-post đa nền tảng
AUTOMATION — campaign automation, email sequence, CRM
CRO        — funnel, conversion, click-path
OUTBOUND   — cold email, lead intelligence (B2B, hợp ABTRIP)
AFFILIATE  — campaign có gắn affiliate link
```
1 request có thể rơi vào nhiều nhóm cùng lúc — xử lý hết, không chỉ chọn 1.

### Bước 2 — Map nhóm sang skill + MCP thật (bảng đầy đủ ở `../../ARCHITECTURE.md`)
Ví dụ nhanh:
- STRATEGY → `skills/expert-digital-marketing` + `skills/market-research` +
  `skills/competitor-research`, cần MCP firecrawl/tavily nếu cần data thị trường thật.
- ADS → `skills/claude-ads/ads-audit.md` (chẩn đoán) trước, rồi mới tới
  `ads-creative.md`/`ads-budget.md` (đề xuất sửa) — không nhảy thẳng vào đề xuất khi
  chưa chẩn đoán.

### Bước 3 — Xác định output có cần confirm không
```
CHỈ phân tích/đề xuất/report → trả kết quả thẳng, không cần confirm
HÀNH ĐỘNG ghi/gửi/chi tiền thật (đăng ads, gửi email hàng loạt, publish social)
  → LUÔN dừng lại, trình bày rõ sẽ làm gì, chờ Nobitano confirm
```

### Bước 4 — Nếu thiếu MCP/data thật
Không bịa số liệu thay cho data thật. Nói rõ: "Chưa có kết nối [MCP tên] để lấy số
liệu thật, đây là ước tính dựa trên [nguồn khác] — cần setup [MCP đó] để có số chính
xác." Xem `../../mcp-setup.md` để biết MCP nào cần key gì.

## Ví dụ thực tế

**Input:** "Meta Ads cho ABTRIP CTR thấp quá, sửa sao?"

**Xử lý:**
1. Phân loại: nhóm ADS.
2. Gọi `skills/claude-ads/ads-audit.md` trước — cần data thật từ `meta-ads-mcp-official`.
   Nếu MCP chưa setup → báo rõ, dùng thông tin Nobitano tự cung cấp thay thế.
3. Audit xong, chẩn đoán theo checklist (creative fatigue → audience sai → placement
   sai → landing page mismatch) — đây là nội dung có sẵn trong `expert-digital-marketing`.
4. Đề xuất sửa cụ thể, gọi thêm `ads-creative.md` nếu cần creative mới.
5. Đây là ĐỀ XUẤT, không phải hành động — trả kết quả thẳng, không cần confirm.
6. Nếu Nobitano duyệt và nói "tạo campaign mới với đề xuất này" → CHUYỂN sang hành
   động ghi thật, lúc này mới cần confirm trước khi gọi MCP tạo campaign.

## Guardrail
- Không tự chọn 1 skill rồi bỏ qua các skill liên quan khác nếu request thực ra cần
  nhiều góc (vd chỉ audit mà bỏ qua bước đề xuất sửa cụ thể là làm nửa vời).
- Ranh giới confirm/không-confirm là CỨNG — không nới lỏng dù agent "tự tin" đề xuất
  đúng, hành động ghi/gửi/chi tiền luôn cần người duyệt.
