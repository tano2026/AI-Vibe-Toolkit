# Customer Satisfaction Pro — Support & Retention Agent

> Agent thứ 8 — khoảng trống phát hiện khi so sánh với mô hình "AI Employees" (Mark Fulton): 7 Pro Agent trước không ai phụ trách CSKH/inbox/rủi ro rời bỏ khách. Quét inbox, soạn câu trả lời khó trước, gắn cờ khách có nguy cơ rời đi kèm bằng chứng — không tự động trả lời thay, chỉ chuẩn bị + gắn cờ đúng độ khẩn.

## Spec

| | |
|--|--|
| **Domain** | Customer support/success — inbox, ticket, comment, rủi ro rời bỏ |
| **Job-to-be-done** | Quét kênh hỗ trợ → phân loại đúng độ khẩn → soạn trả lời khó trước → gắn cờ rủi ro rời bỏ kèm bằng chứng |
| **Người dùng** | Nobitano, đội vận hành ABTRIP/Tano Cafe/Wonder Mart |
| **Input điển hình** | "Quét inbox Facebook ABTRIP hôm nay", "khách này có đáng lo không", "báo cáo CSKH tuần này" |
| **Output điển hình** | Draft trả lời (chưa gửi), báo cáo rủi ro rời bỏ kèm bằng chứng, báo cáo SLA median/P90 |
| **Mức tự chủ** | Soạn/phân loại/gắn cờ — KHÔNG tự gửi trả lời khách, KHÔNG tự hoàn tiền/bồi thường (đúng nguyên tắc propose-don't-decide toàn hệ thống) |
| **Rủi ro cao nhất** | Bỏ sót tín hiệu rời bỏ thật (áp nhầm luật "chờ lặp lại 3 lần" cho case cần escalate ngay) → guardrail: churn-risk-escalation-discipline phân loại NGAY từ lần đầu |

## Capability Map

```
TẦNG NÃO (Skills):
  churn-risk-escalation-discipline — SLA theo kênh, FCR, luật escalate
                                      ngay lần đầu cho tín hiệu rời bỏ thật
  critical-path-briefing            — lọc báo cáo chỉ đưa việc cần đúng
                                       quyết định của Nobitano (dùng chung
                                       được cho mọi agent khác)

TẦNG TAY (MCP/Tools):
  Gmail/Zalo OA/Facebook inbox — tuỳ kênh brand đang dùng, chưa có adapter
  cụ thể — cần xác nhận kênh thật trước khi tích hợp sâu

TẦNG CƠ (Compute):
  Không cần code execution phức tạp — chủ yếu đọc/phân loại/soạn text
```

## Cách bung

1. Copy 2 skill vào skills directory
2. Dán system-prompt.md làm Project Instructions
3. Xác nhận kênh inbox thật đang dùng cho từng brand (Facebook/Zalo OA/Email) trước khi tự động hoá quét — hiện CHƯA có Adapter tool cụ thể, agent mới ở dạng khung + luật, chưa nối kênh thật
4. Test đầu tiên: đưa 5-10 tin nhắn/comment cũ, xem agent phân loại đúng "rời bỏ thật" vs "phàn nàn nhỏ" không

## Việc CHƯA làm — nói thẳng

- Chưa nối kênh inbox thật (Facebook/Zalo OA/email) — agent hiện là khung luật + skill, chưa có pipeline đọc tin nhắn tự động
- Chưa test với case thật của ABTRIP/Tano Cafe/Wonder Mart
- Khác 7 Pro Agent kia, đây được xây từ phát hiện khoảng trống (so sánh AI Employees), không phải từ nhu cầu vận hành đã bức thiết — cần Nobitano xác nhận có đáng ưu tiên ngay không
