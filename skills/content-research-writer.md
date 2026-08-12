# Content Research Writer — Quy trình viết bài có nguồn kiểm chứng được

## TL;DR
Quy trình viết content (blog, báo cáo, newsletter, case study) từ nghiên cứu có nguồn rõ ràng — dùng "source ledger" (bảng ghi nguồn) để tránh bịa số liệu/trích dẫn, đồng thời giữ giọng văn gốc của người viết thay vì bị AI làm phẳng.

## Skill này dùng để làm gì
Quy trình 2 giai đoạn:
**Research:** biến câu hỏi thành các claim cần chứng minh → chọn nguồn ưu tiên (primary source cho số liệu kỹ thuật) → ghi vào bảng ledger (Nguồn | Claim hỗ trợ | Bằng chứng | Giới hạn | Trạng thái) → chỉ đưa nguồn vào reference list nếu đã thực sự mở và dùng → xử lý mâu thuẫn giữa nguồn thay vì tự chọn số thuận tiện.

**Viết:** thesis 1-2 câu → outline gắn từng claim với source ID → draft giữ giọng văn gốc → edit cắt câu mơ hồ → verify lại từng trích dẫn 1 lần nữa trước khi giao.

## Setup từng bước
1. Trước khi viết bài .md mới cho kho hoặc content channel — xác định brief: chủ đề, audience, mục đích, độ dài, giọng văn mẫu (nếu có)
2. Research theo bảng ledger thay vì search rồi viết luôn:
   ```markdown
   | ID | Nguồn | Claim hỗ trợ | Bằng chứng | Giới hạn | Trạng thái |
   |---|---|---|---|---|---|
   | S1 | ... | ... | ... | ... | verified |
   ```
3. Viết outline trước, gắn source ID vào từng mục — không viết thẳng khi chưa rõ claim nào có nguồn, claim nào chưa
4. Verify lần cuối: mở lại từng nguồn, check tên/số/ngày/trích dẫn khớp đúng

## Ví dụ thực tế
**Case:** Viết bài .md research về NDC aggregator cho B2B Travel Platform ABTRIP (so sánh Duffel vs Gotadi) → thay vì viết theo trí nhớ, dựng bảng ledger trước:
| ID | Nguồn | Claim | Bằng chứng |
|---|---|---|---|
| S1 | Duffel docs | Hỗ trợ NDC trực tiếp, không qua BSP | trích API doc |
| S2 | Gotadi.com | Là đối thủ trực tiếp, không có physical presence | trích homepage |

→ Bài viết ra chỉ dùng đúng những gì có trong bảng, không tự thêm số liệu "nghe hợp lý".

## Lưu ý / Lỗi thường gặp
- Với content ngắn (script video 45-60s) áp full quy trình này hơi nặng — chỉ nên dùng cho content dài (báo cáo, bài research .md), không cần cho mọi thứ
- "Giữ giọng văn gốc" đòi hỏi có writing sample trước — nếu không có, Claude sẽ tự chọn giọng mặc định, cần review kỹ hơn
- Không thay thế `natural-writing` skill — 2 cái bổ trợ nhau: cái này lo về structure/nguồn, natural-writing lo về câu chữ

## Đánh giá cá nhân
- Điểm mạnh: bảng source ledger là ý hay, ép tách rõ "đã verify" vs "chưa verify", giảm rủi ro bịa số liệu — quan trọng khi viết case study/báo cáo có tính thuyết phục
- Điểm yếu: hoàn toàn là quy trình/checklist, không có tool hỗ trợ tự động, overhead cao nếu áp cho content ngắn hàng ngày; không có gì đặc biệt so với 1 nhà báo/researcher giỏi vốn đã làm vậy
- Có nên dùng không: 6/10 — dùng chọn lọc cho content dài/quan trọng (case study ABTRIP, báo cáo research), không cần cho script TikTok ngắn

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Prompt-only skill, không cần code thực thi — nhét vào system prompt khi
# task là viết content dài (báo cáo, case study), không áp cho mọi request viết
```

### OpenClaw
> Có thể dùng làm system prompt riêng cho research-agent trong 9-agent pipeline khi task được gắn nhãn "long-form content".

### Antigravity
> Không cần deploy.
