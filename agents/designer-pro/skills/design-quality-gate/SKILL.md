---
name: design-quality-gate
description: >
  Tách từ Self-QA checklist đã có sẵn trong agents/company/roles/designer.md
  thành 1 skill review độc lập — chạy TRƯỚC KHI giao bất kỳ visual nào.
  Đúng ngưỡng số EXPERT-CORE.md ⑥ (contrast, safe zone, font/hierarchy,
  license). Dùng như gate cuối cùng, không phải gợi ý.
---

# Design Quality Gate

## TL;DR
8 mục kiểm tra bắt buộc trước khi giao bất kỳ visual nào — lệch 1 mục là chưa xong, không phải "gần xong".

## Khi nào dùng
- Ngay trước khi giao file visual cho Sales/Marketing/Media
- Review lại visual cũ khi nghi ngờ có lệch chuẩn
- Onboard người mới vào Designer role — dùng làm checklist học chuẩn

## Nội dung skill / prompt

### 8 mục kiểm tra (theo đúng thứ tự, không bỏ qua mục nào)

```
□ 1. Màu/font khớp 100% design-tokens của ĐÚNG PACK đang làm (không dùng
     "quen tay" token project khác)
□ 2. Đủ mọi size kênh đích yêu cầu — text nằm trong safe zone ≥10% mọi
     cạnh, ở TẤT CẢ tỷ lệ (1:1, 4:5, 9:16, 16:9)
□ 3. Contrast text ≥4.5:1 (≥7:1 nếu social/mobile ngoài trời) — đo bằng
     công cụ, không đoán bằng mắt
□ 4. Thu nhỏ về 20% kích thước — vẫn đọc được chữ chính + nhận ra chủ thể
     → pass. Fail = làm lại từ bố cục, không phải chỉnh nhỏ
□ 5. Tối đa 2 font, không quá 3 cấp hierarchy trên 1 visual
□ 6. Mọi asset có nguồn + license ghi rõ trong spec (gốc PACK / AI
     generate / license có link) — không có nguồn = KHÔNG dùng, không
     có ngoại lệ "tạm dùng trước"
□ 7. Chữ trên visual khớp NGUYÊN VĂN copy đã duyệt của Content — không tự
     sửa chữ dù thấy "hay hơn"
□ 8. Có file design-spec-<slug>-<topic>.md đi kèm, đầu spec ghi rõ
     "Đang làm việc trên PACK: <slug>"
```

### Verdict

```
Cả 8 mục PASS → giao được
≥1 mục FAIL → KHÔNG giao, sửa đúng mục fail, chạy lại đủ 8 mục (không
              chỉ check lại mục vừa sửa — 1 thay đổi có thể ảnh hưởng
              mục khác, vd đổi màu chữ ảnh hưởng lại contrast)
```

## Setup từng bước
1. Visual đã dựng xong, trước khi giao → chạy đủ 8 mục
2. Mục 3 (contrast) và mục 4 (thumbnail test) cần công cụ đo thật (contrast checker, thu nhỏ preview thật) — không tự đánh giá bằng cảm quan
3. Fail bất kỳ mục nào → note rõ lý do fail, sửa, chạy lại từ đầu
4. Pass đủ 8 → giao kèm file spec

## Ví dụ thực tế
Visual pitch deck cho khách SMB — pass mục 1-2-5-6-7-8, nhưng mục 3 fail (chữ trắng trên nền vàng nhạt, contrast chỉ 3.2:1, dưới ngưỡng 4.5:1 bắt buộc) → không giao, đổi nền đậm hơn hoặc chữ tối hơn, đo lại contrast đạt 5.1:1 mới giao.

## Lưu ý / Lỗi thường gặp
- Mục 4 (thumbnail test) hay bị bỏ qua nhất — visual đẹp ở full-size không có nghĩa đọc được ở kích thước thumbnail thật trên feed
- Đo contrast bằng mắt không đáng tin — luôn dùng công cụ đo thật (contrast checker online hoặc tool thiết kế có sẵn tính năng này)
- Sửa 1 mục rồi chỉ check lại đúng mục đó — sai, phải chạy lại đủ 8 mục vì các mục liên quan nhau

## Đánh giá cá nhân
- Điểm mạnh: ngưỡng số rõ ràng, không phụ thuộc cảm tính, đã có sẵn trong EXPERT-CORE nên không phải bịa
- Điểm yếu: cần công cụ đo thật (contrast checker) mới chạy được mục 3, không phải lúc nào cũng có sẵn
- Có nên dùng: 10/10 — đây là gate bắt buộc, không phải optional

## Link
- Nguồn gốc: agents/company/roles/designer.md (Self-QA checklist gốc) + agents/company/EXPERT-CORE.md ⑥
