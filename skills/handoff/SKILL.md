---
name: handoff
description: >
  - "Tạo handoff doc để tao mở chat mới tiếp tục" - "Tóm tắt hết context để chat sau đọc lại"
---

# Hand Off — Skill

## TL;DR
Bước 09 (cuối chuỗi 9 skill) — đóng gói toàn bộ context của phiên làm việc hiện tại thành 1
tài liệu handoff, để mở chat mới (hoặc giao agent khác) tiếp tục mà không mất thông tin.

## Khi nào dùng
- Chat hiện tại sắp dài quá, cần chuyển sang chat mới
- Giao việc đang làm dở cho Hermes/OpenClaw/agent khác tiếp tục
- Kết thúc 1 phiên làm việc dài, muốn lưu lại trạng thái để hôm sau tiếp

## Nội dung skill / prompt
```
Tóm tắt phiên làm việc hiện tại thành handoff doc, cấu trúc:

1. MỤC TIÊU GỐC: 1-2 câu, việc đang làm là gì
2. ĐÃ LÀM: liệt kê ngắn gọn các bước đã hoàn thành, kèm kết quả (không kể lể quá trình, chỉ
   kết quả cuối mỗi bước)
3. QUYẾT ĐỊNH ĐÃ CHỐT: những lựa chọn đã quyết định và LÝ DO (quan trọng — người đọc sau
   không được đoán lại từ đầu vì sao chọn hướng này)
4. ĐANG DỞ: việc chưa xong, đang ở bước nào
5. TIẾP THEO: 2-3 bước cụ thể nên làm tiếp, theo thứ tự ưu tiên
6. RÀNG BUỘC CẦN NHỚ: constraint/rule đặc biệt của task này (vd "không được động vào file X",
   "phải giữ backward-compatible với Y")

Giữ toàn bộ handoff dưới 1 trang — nếu dài hơn, đang tóm tắt sai (giữ lại process thay vì kết
quả). Ưu tiên thứ tự: quyết định đã chốt > việc đang dở > việc đã xong.
```

## Ví dụ thực tế
Đang giữa việc nâng cấp RIO Bot lên v3.0, chat sắp dài → tạo handoff: "Mục tiêu: nâng RIO
thành trùm research. Đã làm: viết rio_bot.py, web_search.py, thêm Drafter-Reviewer loop vào
brain.py. Quyết định chốt: tối đa 2 vòng research, không lặp vô hạn. Đang dở: chưa test thật
trên VPS. Tiếp theo: viết deploy-checklist.md, test 1 lệnh /market thật."

## Đánh giá cá nhân
- Có nên dùng không: 8/10 — đặc biệt quan trọng khi giao việc giữa nhiều agent (Claude → Hermes
  → OpenClaw) hoặc chat rất dài dễ mất context.

## Link
- Thuộc chuỗi: `stacks/chuoi-9-buoc-viet-prompt.md` — bước 09/09 (cuối chuỗi)
