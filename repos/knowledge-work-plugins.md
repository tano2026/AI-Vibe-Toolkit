---
name: knowledge-work-plugins
description: >
  Tác giả: Anthropic (chính chủ) License: Apache 2.0 Domain: Bộ 11 plugin cho Claude Cowork/Code
---

# knowledge-work-plugins — bộ plugin chính thức của Anthropic cho dân văn phòng

**GitHub:** https://github.com/anthropics/knowledge-work-plugins
**Tác giả:** Anthropic | **License:** Apache 2.0

---

## TL;DR

11 plugin chính thức Anthropic mở nguồn, mỗi cái biến Claude thành "chuyên gia" cho 1 vai trò cụ thể (sales, data, marketing, productivity, finance, legal, HR, customer-support, product-management, engineering, bio-research). Chạy trên Claude Cowork và tương thích Claude Code.

## Tool này dùng để làm gì

Khác skill đơn lẻ — mỗi plugin là 1 bộ đóng gói gồm: skills + connectors (MCP) + slash commands + sub-agents cho đúng 1 công việc. Ví dụ plugin `sales` có sẵn `/sales:call-prep`, `/sales:pipeline-review`, kết nối CRM luôn chứ không chỉ là prompt suông.

**Quan trọng:** bộ này đang chạy SẴN trong session Claude hiện tại của tao (thấy rõ trong danh sách skill: `sales:*`, `data:*`, `marketing:*`, `engineering:*`, `human-resources:*`, `finance:*`, `customer-support:*`, `product-management:*`, `design:*`, `productivity:*`, `enterprise-search:*`, `bio-research:*`, `cowork-plugin-management:*`) — tức là claude.ai project này đã có 12-13/11+ plugin bật sẵn, không cần cài lại từ đầu.

## Setup từng bước

1. Trên Cowork: cài trực tiếp tại `claude.com/plugins`, chọn plugin cần
2. Trên Claude Code CLI:
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```
3. Sau khi cài, skill tự kích hoạt khi liên quan, slash command dùng ngay trong session

## Ví dụ thực tế

Plugin `sales` áp cho ABTRIP B2B: gõ `/sales:call-prep [tên khách]` → tự research công ty + gợi ý agenda cuộc gọi, không cần tự viết prompt từ đầu mỗi lần.

## Lưu ý / Lỗi thường gặp

- README từng ghi sai cú pháp CLI (`claude plugins add` — số nhiều, không tồn tại) — bản sửa đúng là `claude plugin marketplace add` rồi `claude plugin install tên@marketplace`. Nếu thấy lệnh cũ báo lỗi, đây là lý do.
- Trên Cowork cài qua UI, không có CLI riêng cho Cowork — đừng nhầm lệnh Claude Code CLI sang Cowork
- Có vài fork tùy biến theo ngành (vd fork FashionUnited) — nếu tìm thấy bản fork, kiểm tra kỹ đây có phải bản gốc Anthropic hay bản đã chỉnh riêng

## Đánh giá cá nhân

- **Điểm mạnh:** chính chủ Anthropic nên độ tin cậy và maintain cao hơn skill cộng đồng, đã tích hợp sẵn connector thật (MCP) chứ không chỉ là văn bản hướng dẫn, đang chạy thật trong project này nên biết chắc nó hoạt động
- **Điểm yếu:** một số plugin cần connector ngoài (CRM, calendar...) mới phát huy hết — nếu không kết nối gì thì output chỉ như prompt thường; docs từng có lỗi cú pháp CLI
- **Có nên dùng không:** 8.5/10 — vì đang xài sẵn trong chính project kho này rồi, không cần cân nhắc thêm

## Link
- Repo: https://github.com/anthropics/knowledge-work-plugins

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không có REST API riêng cho plugin — đây là bộ config chạy trong Claude, không phải service ngoài.
# Hermes muốn dùng cùng connector (vd CRM) thì gọi thẳng MCP server tương ứng, không qua plugin này.
```

### OpenClaw
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install productivity@knowledge-work-plugins
```

### Antigravity
```bash
# Không cần tự host — plugin chạy trong môi trường Claude Cowork/Code có sẵn,
# chỉ cần đảm bảo VPS có claude CLI version hỗ trợ lệnh `plugin marketplace`
claude --version   # kiểm tra hỗ trợ plugin marketplace trước khi cài
```
> ⚠️ Đây là bộ đang chạy sẵn trong claude.ai project "Kho Skills" — không cần cài lại, chỉ ghi vào kho để tra cứu khi cần biết plugin nào có sẵn.
