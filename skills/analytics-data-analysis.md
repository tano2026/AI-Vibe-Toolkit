# Analytics Data Analysis — Chuẩn viết code phân tích tái lặp lại được

## TL;DR
Chuẩn viết code/notebook phân tích data sao cho người khác (hoặc chính mình 3 tháng sau) chạy lại và audit được — từ inventory data, validate, transform (giữ raw không đổi), phân tích, visualize, đến đóng gói output. Bổ trợ cho `data-analyzer` (skill kia là *cách nghĩ*, skill này là *cách viết code*).

## Skill này dùng để làm gì
7 bước khi giao code/notebook phân tích thay vì chỉ trả lời bằng lời:
1. Inventory: ghi rõ tên nguồn, size, cột, kiểu dữ liệu, row count, key
2. Validate: check missing/range/duplicate-key/referential integrity — tách lỗi nguồn với lọc có chủ đích
3. Transform: **giữ nguyên raw input**, mọi bước clean phải rõ ràng và deterministic (không random ẩn)
4. Analyze: chọn phương pháp thống kê đúng loại biến, báo cáo effect size chứ không chỉ p-value
5. Visualize: chọn chart đúng loại so sánh, ghi rõ unit/time window/filter/sample size trên chart
6. Package: tách config khỏi logic, đặt tên output ổn định
7. Verify: chạy lại từ đầu sạch, đối chiếu tổng số quan trọng với nguồn

Quy tắc code: hàm rõ input/output, không giấu mất data trong except rộng, chỉ dùng random seed khi method cần và phải ghi lại seed.

## Setup từng bước
1. Khi giao task "viết code phân tích" (không phải chỉ trả lời bằng số) — áp chuẩn 7 bước trên
2. Luôn tách raw data ra khỏi transformed data, không ghi đè file gốc trừ khi được yêu cầu rõ
3. Giao kèm: input/scope, quyết định clean/loại trừ, phương pháp, output chính, đã verify gì, giới hạn còn tồn tại

## Ví dụ thực tế
**Case:** Viết script Python phân tích data booking ABTRIP (Fast Track/SIM/đổi tiền) theo tháng để tìm mùa cao điểm → thay vì viết code 1 lần rồi báo kết quả:
```python
# 1. Inventory: ghi rõ file nguồn, 1200 dòng, cột [date, service_type, revenue]
# 2. Validate: check date parse lỗi, service_type có giá trị lạ không
# 3. Transform: giữ file gốc, tạo file mới month_aggregate.csv
# 4. Analyze: group by month, so sánh median (không mean vì có outlier dịp Tết)
# 5. Verify: tổng revenue theo tháng cộng lại phải khớp tổng cả năm
```
→ Nếu 3 tháng sau cần chạy lại với data mới, chỉ cần đổi file input, chạy lại đúng pipeline, không phải làm lại từ đầu.

## Lưu ý / Lỗi thường gặp
- Overlap gần như hoàn toàn với `data-analyzer` — khác biệt chính: `data-analyzer` là quy trình tư duy/report, còn skill này là chuẩn viết code thực thi. Dùng chung với nhau, không thay thế nhau
- Rule "giữ raw không đổi" dễ bị bỏ qua khi làm nhanh — cần nhắc rõ trong prompt

## Đánh giá cá nhân
- Điểm mạnh: chuẩn code sạch, dễ audit, nguyên tắc "giữ raw + transform deterministic" rất đáng áp dụng cho pipeline dữ liệu lặp lại (VD: báo cáo tháng cho ABTRIP/Wonder Mart)
- Điểm yếu: khá overlap với data-analyzer, không có gì mới ngoài "coding best practice" thông thường; cần code execution thật, không dùng được ở tầng Hermes (không có pandas)
- Có nên dùng không: 5/10 — hữu ích cho pipeline phân tích lặp lại định kỳ, không cần cho phân tích 1 lần đơn giản

## Link
- Nguồn gốc skill: adapted từ bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills) (clean-room-original)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Cần pandas/numpy — Hermes hiện không có pip ngoài, nên pipeline phân tích
# nặng nên chạy ở tầng Claude session, Hermes chỉ gọi kết quả cuối qua API
# nếu cần tự động hóa báo cáo định kỳ (VD: gửi Telegram mỗi đầu tháng)
```

### OpenClaw
> Có thể lưu script phân tích chuẩn hóa này trong repo, chạy định kỳ qua cron/PM2 nếu cần báo cáo tháng tự động cho ABTRIP/Wonder Mart.

### Antigravity
```bash
# Nếu cần chạy script phân tích định kỳ trên VPS:
pip install pandas numpy --break-system-packages
# Setup cron job gọi script, output đẩy về qua Telegram/OpenClaw
```
