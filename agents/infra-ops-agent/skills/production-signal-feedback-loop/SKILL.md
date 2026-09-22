---
name: production-signal-feedback-loop
description: >
  Vòng lặp khép kín — đúc kết từ infographic ADLC (Agentic Development
  Lifecycle): tín hiệu vận hành (lỗi/sự cố/hiệu suất kém) TỰ ĐỘNG tạo
  intent mới, không chờ Nobitano tự nhận ra vấn đề rồi mới giao việc.
  Dùng Jev (TypeSafe) làm tầng phân loại nhanh trước khi tạo intent —
  đúng kiến trúc cascade đã thiết kế cho "3 CLI". Dùng cho Infra Ops
  Agent, có thể mở rộng sang Media Pro/Customer Satisfaction Pro.
---

# Production Signal Feedback Loop

## TL;DR
Báo cáo 1 chiều (đo xong → báo Nobitano → Nobitano tự quyết) khác vòng lặp khép kín (đo xong → tự phân loại → tự tạo việc mới vào hàng đợi → chỉ hỏi Nobitano khi không chắc). Skill này biến dev-automation-discipline/media-performance-discipline từ "báo lỗi" thành "tự khép vòng".

## Khi nào dùng
- Sau deploy-review-gate phát hiện sự cố/lỗi sau deploy
- Hiệu suất giảm bất thường (dùng chung được với media-performance-discipline phân loại (c) fail thật)
- Bất kỳ tín hiệu vận hành nào cần quyết định "có đáng tạo việc mới không"

## Nội dung skill / prompt

### Chuỗi tạo tác (đúng ADLC — mỗi bước vừa là output vừa là input có ngữ cảnh cho bước sau)

```
production signal -> [PHAN LOAI QUA JEV] -> intent.md mới (nếu đáng) ->
spec.md -> plan.md -> code+tests -> review record -> production signal
(vòng lặp tiếp, không dừng ở review record)
```

### Tầng phân loại — Jev làm trước, Claude chỉ vào khi không chắc

```
Production signal vào -> gọi Jev qua Antigravity Bridge (đã thiết kế
trong repos/swarms.md pattern — service nội bộ, KHÔNG cần Hermes tự
cài SDK):

  Câu hỏi 1 (Noul — có/không): "Tín hiệu này có đáng tạo intent mới
  không, hay chỉ nhiễu/dao động bình thường?"

  Câu hỏi 2 (Choice): "Loại vấn đề gì — bug/hiệu suất/bảo mật/thiếu
  tính năng?"

  Câu hỏi 3 (Score 0-5): "Mức độ khẩn cấp?"

  Câu hỏi 4 (Choice, so với danh sách intent đang mở): "Có trùng
  intent nào đang xử lý không, hay là vấn đề mới?"

Áp đúng ngưỡng confidence đã thiết kế trong kiến trúc cascade:
  confidence >=80%  -> tự tạo intent.md mới, xếp hàng theo độ khẩn
  confidence 50-80% -> tạo intent NHƯNG gắn nhãn "cần Nobitano xác
                       nhận trước khi Infra Ops bắt đầu code"
  confidence <50%    -> KHÔNG tự tạo, đưa thẳng cho Nobitano qua
                       critical-path-briefing (đây là việc "chỉ
                       Nobitano gỡ được" — quyết định có đáng làm không)
```

### Fallback khi Jev chưa có (còn waitlist)

```
Chưa có TYPESAFE_API_KEY -> dùng luật đơn giản thay thế (tạm thời):
  - Signal lặp lại >=3 lần trong <24h -> coi như đáng tạo intent
  - Signal xuất hiện 1 lần -> mặc định gửi Nobitano xác nhận trước
    (an toàn hơn bỏ sót, chấp nhận làm phiền hơn 1 chút)
Đây CHỈ là fallback tạm — khi Jev có access thật, chuyển sang dùng
Jev ngay, không giữ luật đơn giản làm chính.
```

### Định dạng intent.md tự động tạo

```markdown
# Intent — [ngày tự động tạo]

**Nguồn:** production signal tự động (không phải Nobitano khởi tạo)
**Phân loại Jev:** [loại vấn đề] | confidence [%]
**Độ khẩn:** [điểm 0-5]
**Trùng lặp:** [không / trùng với intent #X]

## Mô tả
[Tín hiệu gốc — log lỗi/số liệu hiệu suất, nguyên văn không diễn giải lại]

## Trạng thái
Chờ xử lý — [tự động xếp hàng / chờ Nobitano xác nhận]
```

## Setup từng bước
1. Production signal xuất hiện (lỗi log, cảnh báo hiệu suất)
2. Gọi Jev Bridge (Antigravity) với 4 câu hỏi trên
3. Áp ngưỡng confidence -> tạo intent.md hoặc đưa thẳng Nobitano
4. Intent mới xếp vào hàng đợi theo độ khẩn (Score câu 3)
5. Infra Ops Agent tiếp tục theo chuỗi ecc-orch-* đã có (spec->plan->code+tests->review)

## Ví dụ thực tế
VPS chạy Antigravity báo lỗi timeout lặp lại 4 lần trong 2 giờ — Jev phân loại: Noul=có đáng tạo intent (confidence 91%), Choice=hiệu suất, Score=4/5 (khẩn), không trùng intent nào đang mở → tự động tạo intent.md mới, xếp đầu hàng đợi vì độ khẩn cao, Infra Ops Agent bắt đầu viết spec.md ngay mà không cần đợi Nobitano tự phát hiện qua log.

## Lưu ý / Lỗi thường gặp
- Để confidence thấp mà vẫn tự tạo intent — vi phạm đúng nguyên tắc cascade đã thiết kế, dễ tạo nhiễu (nhiều intent giả tạo từ tín hiệu không chắc chắn)
- Fallback rule-based dùng lâu dài thay vì chuyển sang Jev khi có access — mất giá trị chính của skill này
- Không gắn nhãn nguồn "tự động tạo" trong intent.md — Nobitano không phân biệt được việc nào do mình giao, việc nào hệ thống tự phát hiện

## Đánh giá cá nhân
- Điểm mạnh: nối đúng 2 thứ đã thiết kế riêng lẻ (kiến trúc cascade Jev + vòng khép kín ADLC) thành 1 use case cụ thể, có fallback an toàn khi Jev chưa access được
- Điểm yếu: phụ thuộc Jev Bridge (Antigravity) đã thiết kế nhưng CHƯA triển khai thật — toàn bộ phần Jev trong skill này chưa test được cho tới khi có key thật
- Có nên dùng: 8/10 về thiết kế, nhưng thực thi thật phải chờ Jev qua waitlist — dùng fallback rule-based trước

## Link
- Nguồn ADLC: infographic "Từ SDLC đến ADLC" (Nobitano chia sẻ)
- Kiến trúc Jev cascade: repos/typesafe-jev.md, thiết kế Antigravity Bridge đã bàn trước đó
- Dùng cùng: dev-automation-discipline, deploy-review-gate, critical-path-briefing (khi confidence thấp)
