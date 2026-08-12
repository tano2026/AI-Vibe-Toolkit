# Summarization — Format tóm tắt theo đúng loại nguồn

## TL;DR
Bộ khung chọn format tóm tắt phù hợp theo loại nguồn (báo cáo, cuộc họp, bài nghiên cứu, đa nguồn) thay vì lúc nào cũng tóm tắt kiểu chung chung — kèm quy tắc chống bịa: không gán owner/deadline cho action item nếu nguồn không nói rõ, không giới thiệu kết luận mới không có trong nguồn.

## Skill này dùng để làm gì
5 format tóm tắt khác nhau theo mục đích:
- **Executive Brief** (báo cáo/đề xuất): bottom line → bằng chứng mạnh nhất → rủi ro → quyết định cần → hành động tiếp theo
- **Technical Summary** (spec/kiến trúc/incident): mục đích/scope → hành vi/thiết kế → interface/dependency → quyết định quan trọng → trade-off → breaking change
- **Meeting/Conversation**: quyết định → action item (kèm owner/deadline **chỉ khi** đã nói rõ) → lý do chính → bất đồng → câu hỏi chưa giải quyết
- **Research Digest**: câu hỏi nghiên cứu → phương pháp/mẫu → phát hiện chính → giới hạn → ý nghĩa
- **Multi-Source Synthesis**: đọc hết nguồn trước khi viết → group theo chủ đề → gắn nguồn cho claim gây tranh cãi → nêu rõ mâu thuẫn giữa nguồn, không lặng lẽ chọn 1 cái

3 mức độ nén: Snapshot (vài dòng) / Brief (bottom line + evidence + action) / Detailed (đầy đủ có caveat).

## Setup từng bước
1. Xác định nguồn cần tóm tắt thuộc loại nào trong 5 loại trên
2. Với input thiếu rõ ràng về audience/mục đích/độ dài — tự chọn format hợp lý và ghi rõ 1 dòng "đang tóm tắt ở mức Brief" thay vì hỏi lại
3. Trước khi trả kết quả: audit lại — tên/số/ngày có khớp nguồn không, có tự thêm kết luận nào không có trong nguồn không

## Ví dụ thực tế
**Case:** Tóm tắt buổi research về Zalo OA bot bug (systemd inactive) để báo cáo nhanh → dùng format Meeting/Conversation:
- Quyết định: tạm dùng Zalo OA Manager thủ công cho Trụ 1-2, defer Trụ 3-4
- Action item: rotate `ZALO_ACCESS_TOKEN` — **không gán deadline** vì chưa ai chốt ngày cụ thể
- Chưa giải quyết: nguyên nhân systemd inactive chưa xác định

→ Không tự bịa ra "deadline tuần sau" nếu không ai nói vậy — đây là điểm khác biệt so với tóm tắt tự do thông thường.

## Lưu ý / Lỗi thường gặp
- Rule "không gán owner/deadline chưa được nói rõ" rất dễ bị bỏ qua khi tóm tắt nhanh — cần nhắc lại rõ trong prompt nếu muốn giữ chuẩn này
- Không hợp cho tóm tắt sáng tạo (VD: tóm tắt 1 video content để lấy ý tưởng remix) — skill này thiên về tóm tắt chính xác factual, không phải tóm tắt truyền cảm hứng

## Đánh giá cá nhân
- Điểm mạnh: phân loại format theo mục đích khá thực tế, rule "không bịa owner/deadline" là điểm tốt hay bị AI mặc định làm sai
- Điểm yếu: về cơ bản là best-practice tóm tắt thông thường được viết lại có cấu trúc, không có gì đột phá; Claude vốn đã làm tốt việc này nếu prompt rõ ràng
- Có nên dùng không: 5/10 — tham khảo được, không phải capability mới, giá trị chính là checklist "audit lại trước khi trả kết quả" ở cuối

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Prompt-only — không cần code. Có thể nhét làm default instruction khi
# Hermes trả kết quả research dài về qua Telegram, để tự chọn format ngắn gọn phù hợp
```

### OpenClaw
> Dùng làm chuẩn format khi OpenClaw tổng hợp báo cáo trạng thái agent hàng ngày/tuần.

### Antigravity
> Không cần deploy.
