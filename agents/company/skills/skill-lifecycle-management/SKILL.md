---
name: skill-lifecycle-management
description: >
  Vai trò "HR" đúc kết từ OneManCompany (Talent Market — tuyển/sa thải
  theo hiệu suất) — áp dụng cho việc quản lý vòng đời 590+ skill trong
  kho, hiện chưa ai quản lý định kỳ. Định nghĩa khi nào 1 skill được
  "thăng chức" (verified), khi nào bị "sa thải" (nghỉ hưu/archive).
---

# Skill Lifecycle Management (vai trò "HR")

## TL;DR
590 skill trong kho, phần lớn chưa ai đọc/verify từ ngày thêm vào. Không có ai đóng vai "HR" định kỳ audit chất lượng — skill có thể lỗi thời, trùng lặp (như vụ ecc/ 271 file), hoặc chưa từng dùng mà không ai biết.

## Khi nào dùng
- Audit định kỳ thư viện skill (khuyến nghị: mỗi lần thêm >=20 skill mới, hoặc mỗi quý)
- Trước khi viết skill mới — kiểm tra "tuyển người mới hay đã có sẵn rồi"
- Phát hiện nghi ngờ trùng lặp

## Nội dung skill / prompt

### 4 trạng thái vòng đời (mượn khái niệm hire/fire từ OMC)

```
1. UNG TUYEN (Candidate) — skill mới thêm, CHƯA verify nội dung, chỉ có
   tên + mô tả. Trạng thái mặc định của phần lớn 590 skill hiện tại.

2. DA XAC MINH (Verified) — đã đọc thật, đã dùng thật ít nhất 1 lần,
   không trùng lặp với skill khác. VD: claude-ads/*, systematic-debugging,
   anti-ai-tells (đã qua kiểm tra thật trong phiên trước).

3. NGHI HUU (Retired) — xác nhận trùng lặp/lỗi thời, archive không xoá
   ngay (trừ khi Nobitano xác nhận xoá hẳn — đúng nguyên tắc đã áp cho
   research-pro.md/skills/ecc/).

4. TU CHOI (Rejected) — trong quá trình audit phát hiện skill sai/gây
   hại/không dùng được — archive kèm lý do rõ ràng, không xoá âm thầm.
```

### Quy trình audit định kỳ

```
1. Lấy danh sách skill mới thêm từ lần audit trước (so sánh TRACKER.md)
2. Với mỗi skill: đọc thật nội dung, kiểm tra trùng tên/nội dung với
   skill đã có (đúng cách đã làm với claude-ads, systematic-debugging)
3. Verified → không cần làm gì thêm, giữ nguyên
4. Trùng lặp xác nhận → đề xuất Nobitano cho phép archive (không tự xoá)
5. Cập nhật KHO-INDEX.md nếu số liệu tổng lệch nhiều
```

### Quy trình "tuyển người mới" (trước khi viết skill mới)

```
BẮT BUỘC search rộng trước khi viết — đúng bài học từ vụ trùng lặp
ad-budget-testing-discipline/claude-ads đã xảy ra thật:
  1. Search tên + từ khoá liên quan trong toàn bộ skills/
  2. Đọc nội dung nếu tìm thấy khả nghi (không chỉ tin tên)
  3. Chỉ viết mới nếu xác nhận thật sự chưa có
```

## Setup từng bước
1. Định kỳ (mỗi quý hoặc mỗi 20 skill mới) — chạy audit theo quy trình trên
2. Với mỗi skill mới — xác định trạng thái (Candidate/Verified)
3. Nghi ngờ trùng lặp — verify nội dung thật (không chỉ tên), đề xuất Nobitano quyết định archive
4. Cập nhật số liệu KHO-INDEX.md nếu có thay đổi lớn

## Ví dụ thực tế
Đợt audit tháng 8/2026 phát hiện skills/ecc/ (271 file) trùng 100% nội dung với skill phẳng đã có — đây chính là 1 lần "HR" phát hiện nhân sự trùng lặp, đề xuất Nobitano duyệt archive, không tự ý xoá trước khi hỏi.

## Lưu ý / Lỗi thường gặp
- Tự động xoá skill nghi trùng mà chưa hỏi — vi phạm nguyên tắc đã thống nhất, luôn cần xác nhận trước khi archive/xoá
- Chỉ so tên mà không đọc nội dung — bỏ sót trùng lặp thật (nhiều skill tên khác nhưng nội dung giống, hoặc tên giống nhưng nội dung khác)
- Audit 1 lần rồi bỏ quên — cần định kỳ, kho vẫn tiếp tục phình thêm

## Đánh giá cá nhân
- Điểm mạnh: vá đúng lỗ hổng đã xảy ra thật (vụ ecc/, vụ ad-budget-testing-discipline) — không phải lý thuyết suông, có bằng chứng cụ thể trong lịch sử kho
- Điểm yếu: cần thời gian đọc thật từng skill nghi ngờ — không tự động hoá hoàn toàn được, vẫn cần con người/Claude đọc kỹ
- Có nên dùng: 9/10 — 590 skill không quản lý định kỳ sẽ tiếp tục phình và trùng lặp

## Link
- Nguồn: OneManCompany (Talent Market — hire/fire theo hiệu suất, community-verified)
- Case thật đã xử lý: skills/ecc/ (271 file, đã archive/xoá 21/08/2026), agents/research-pro.md (đã xoá)
