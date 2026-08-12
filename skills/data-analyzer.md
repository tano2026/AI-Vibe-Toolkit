# Data Analyzer — Phân tích dữ liệu ưu tiên ít kết luận đáng tin hơn nhiều kết luận yếu

## TL;DR
Khung phân tích data (CSV/spreadsheet/JSON) đi từ câu hỏi rõ ràng → kiểm tra chất lượng data → thống kê đáng tin → điều tra pattern → diễn giải có phân biệt fact/inference → verify lại số liệu trước khi báo cáo. Nguyên tắc cốt lõi: thà ít finding chắc chắn còn hơn nhiều finding yếu.

## Skill này dùng để làm gì
6 bước:
1. Làm rõ câu hỏi/quyết định cần data trả lời trước khi phân tích
2. Kiểm tra data: số dòng, kiểu dữ liệu, missing value, duplicate, giá trị vô lý — ghi rõ phần nào bị loại và vì sao
3. Thống kê đáng tin: dùng median/quantile khi có outlier thay vì trung bình gây lệch
4. Điều tra: so sánh giai đoạn/nhóm, kiểm tra xu hướng/seasonality/concentration, thử giải thích thay thế trước khi kết luận 1 pattern là quan trọng
5. Diễn giải: tách rõ quan sát thực tế vs suy luận, nêu magnitude + denominator (không chỉ % thay đổi suông), không claim nhân quả nếu thiết kế không hỗ trợ
6. Verify: tính lại tổng số quan trọng độc lập, check filter/join/unit có khớp scope đã nêu không

Output chuẩn: Scope → Data Quality → Findings (kèm value/comparison/denominator/vì sao quan trọng) → Recommended Actions → Methods (để tái tạo lại được).

## Setup từng bước
1. Trước khi phân tích data (VD: data view TikTok Trùm Sân Bay, data booking ABTRIP) — viết rõ câu hỏi cụ thể, đừng phân tích chung chung "xem có gì hay không"
2. Chạy code execution thật (pandas/numpy) để tính, không tự bịa số — nguyên tắc "verify lại tổng số độc lập" bắt buộc phải chạy code, không đoán bằng mắt
3. Output theo đúng format Scope/Data Quality/Findings/Actions/Methods để dễ audit lại sau

## Ví dụ thực tế
**Case:** Phân tích data view 230+ script video Trùm Sân Bay xem loại nội dung nào hiệu quả nhất → thay vì kết luận cảm tính "video về Fast Track hay nhất", chạy đúng quy trình:
- Data quality: có bao nhiêu video thiếu số liệu view (chưa đăng hoặc mất data)
- Finding: "Video về SIM du lịch có view trung bình cao hơn Fast Track 40% (n=12 vs n=18, median thay vì mean vì có 1 video viral gây lệch)"
- Method: ghi rõ cách tính để lần sau kiểm tra lại được

## Lưu ý / Lỗi thường gặp
- Đòi hỏi code execution thật (pandas/numpy) — không dùng được nếu chỉ prompt suông không có compute, dễ bị lười và tự bịa số nếu không ép chạy code
- Rule "không claim nhân quả" rất dễ bị bỏ qua trong lúc viết báo cáo nhanh — cần nhắc lại rõ

## Đánh giá cá nhân
- Điểm mạnh: nguyên tắc "ít finding chắc còn hơn nhiều finding yếu" rất đáng học, format output chuẩn hóa tốt, dễ audit lại
- Điểm yếu: không có gì đặc biệt so với cách 1 data analyst giỏi vốn đã làm; giá trị phụ thuộc hoàn toàn vào việc thật sự chạy code, nếu chỉ đọc số bằng mắt thì skill này vô nghĩa
- Có nên dùng không: 6/10 — dùng làm chuẩn khi phân tích data thật (channel analytics, booking data), overlap nhiều với analytics-data-analysis bên dưới nên có thể gộp chung 1 chuẩn dùng cả 2

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Prompt-only + cần code execution thật (pandas). Hermes hiện dùng urllib.request
# thuần, không có pandas sẵn — nếu cần phân tích data nặng, nên đẩy task này
# cho Claude session (có code execution) thay vì Hermes tự làm
```

### OpenClaw
> Dùng khi cần báo cáo phân tích channel analytics định kỳ — format Scope/Findings/Actions dễ đưa vào Telegram digest.

### Antigravity
> Không cần deploy — chỉ cần đảm bảo pandas/numpy có sẵn ở môi trường Claude chạy phân tích, không phải VPS Hermes.
