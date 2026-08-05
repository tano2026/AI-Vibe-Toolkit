# Zapier — MCP Server

## TL;DR
MCP chính thức của Zapier — mở cửa vào 9,000+ app và 40,000+ action có sẵn trong hệ sinh thái Zapier, qua đúng 1 kết nối MCP. Không cần build riêng từng connector cho từng dịch vụ.

## Tool này dùng để làm gì
Zapier vốn đã là "keo dán" giữa hàng nghìn app (Gmail, Sheets, Airtable, Slack, CRM...). MCP của nó cho Claude gọi thẳng bất kỳ action nào trong kho đó bằng ngôn ngữ tự nhiên, thay vì phải tự viết integration code cho từng dịch vụ riêng lẻ.

## Setup từng bước
1. Có tài khoản Zapier (free tier đủ dùng để thử, giới hạn số action/tháng).
2. Trong Claude: Settings → Connectors → thêm "Zapier" → OAuth qua mcp.zapier.com.
3. Chọn cụ thể app/action nào được expose cho Claude — không bật hết 40,000 action cùng lúc, chỉ bật cái cần dùng để tránh nhiễu tool list.
4. Có sẵn skill hướng dẫn onboarding/audit/demo trong catalog: `zapier:zapier-onboard`, `zapier:zapier-demo`, `zapier:zapier-status`, `zapier:zapier-explore` — dùng các skill này để setup nhanh thay vì tự mò.

## Ví dụ thực tế
Kết nối VietQR/email vào Zapier action, để Claude tự tạo reminder gửi hoá đơn khi có giao dịch mới ở ABTRIP — không cần code riêng cho từng bước, chỉ cần Zap đã cấu hình sẵn và Claude gọi đúng action đó khi cần.

## Lưu ý / Lỗi thường gặp
- **Free tier giới hạn số action/tháng** — automation chạy volume cao (như pipeline content 9-agent) sẽ vượt free tier nhanh, cần tính chi phí gói trả phí.
- Bật quá nhiều action cùng lúc làm tool list Claude phình to, giảm độ chính xác khi chọn tool — chỉ bật đúng cái cần cho từng use case.
- Zapier là lớp trung gian — vẫn phụ thuộc uptime/độ trễ của chính Zapier, không tự chủ hạ tầng bằng cách gọi trực tiếp API của từng dịch vụ.

## Đánh giá cá nhân
- Điểm mạnh: phủ được gần như mọi app phổ biến chỉ với 1 kết nối, tiết kiệm thời gian build integration riêng lẻ.
- Điểm yếu: chi phí tăng theo volume, và là lớp trung gian thêm 1 điểm phụ thuộc ngoài.
- Có nên dùng không: 7/10 — hợp cho automation nhỏ/vừa cần kết nối nhanh nhiều app; với automation lõi (Hermes/OpenClaw gọi GitHub API, Telegram) nên giữ nguyên gọi trực tiếp thay vì qua Zapier để tránh thêm phụ thuộc.

## Link
- Docs: https://mcp.zapier.com
- Skill liên quan trong catalog: `zapier:zapier-onboard`, `zapier:zapier-explore`
