---
name: hermes-autonomous-kho-maintenance
description: >
  Nâng cấp Hermes thành "Autonomous GitHub Engineer" (Explore→Plan→
  Implement→Test→Fix→Verify) áp dụng CHO CHÍNH kho AI-Vibe-Toolkit —
  tự chạy audit skill-lifecycle-management định kỳ thay vì chờ Claude
  làm tay. Dùng hermes-jev-skills (shadow mode) cho quyết định nhanh,
  Langfuse quan sát mọi bước. Vá lỗ hổng: skill-lifecycle-management
  có thiết kế nhưng chưa ai thật sự CHẠY định kỳ.
---

# Hermes Autonomous Kho Maintenance

## TL;DR
`skill-lifecycle-management` (vai "HR") đã thiết kế xong nhưng vẫn phải Claude tự chạy tay mỗi lần nhớ ra. Skill này biến nó thành việc Hermes TỰ LÀM định kỳ — đúng năng lực "Autonomous GitHub Engineer" (Explore→Plan→Implement→Test→Fix→Verify) áp cho việc bảo trì kho, không phải viết code sản phẩm.

## Khi nào dùng
- Chạy định kỳ (cron qua Antigravity) — không cần Claude nhớ tự chạy
- Sau mỗi đợt thêm ≥10 skill/agent mới vào kho

## Nội dung skill / prompt

### Chu trình Explore→Plan→Implement→Test→Fix→Verify áp cho bảo trì kho

```
EXPLORE — Hermes fetch toàn bộ TRACKER.md + danh sách file thật qua
  GitHub API, so sánh 2 cái tìm chênh lệch (file có trong repo nhưng
  không có trong TRACKER, hoặc ngược lại)

PLAN — Với mỗi chênh lệch, gọi Jev (qua hermes-jev-skills, SHADOW MODE
  trước) phân loại: "Đây có phải file cần audit không?" (Boolean),
  "Mức độ nghiêm trọng?" (Score) — GHI LOG qua Langfuse, CHƯA tự sửa

IMPLEMENT — Chỉ với việc CONFIDENCE CAO (đã xem log Langfuse đủ tin) —
  Hermes tự sửa các lỗi ĐƠN GIẢN, RÕ RÀNG (số liệu sai, link chết) —
  KHÔNG tự xoá file, KHÔNG tự quyết định trùng lặp (đúng nguyên tắc
  skill-lifecycle-management: archive cần xác nhận Nobitano)

TEST — Verify file sau khi sửa vẫn parse đúng frontmatter, link không
  chết (dùng lại logic đã dùng cho claude plugin validate)

FIX — Nếu TEST fail, tự rollback (dùng git revert qua Git Data API),
  KHÔNG để lỗi tồn tại im lặng

VERIFY — Tổng hợp báo cáo qua critical-path-briefing — CHỈ đưa Nobitano
  việc cần xác nhận (nghi trùng lặp, cần archive), KHÔNG liệt kê mọi
  file đã tự sửa nhỏ
```

### Ranh giới rõ ràng — Hermes được làm gì, KHÔNG được làm gì

```
ĐƯỢC tự làm (confidence cao, việc nhỏ, rõ ràng):
  - Sửa số liệu thống kê sai trong file "meta" (đúng kiểu lỗi
    KHO-INDEX.md/ARCHITECTURE.md đã tìm thấy)
  - Sửa lỗi cú pháp rõ ràng (backtick escape sai, markdown lỗi)
  - Thêm dòng vào TRACKER.md cho skill mới chưa được đăng ký

TUYỆT ĐỐI KHÔNG tự làm (luôn cần Nobitano xác nhận):
  - Xoá file (kể cả nghi trùng lặp rõ ràng — đúng bài học ecc/)
  - Sửa nội dung EXPERT-CORE.md (ngưỡng số luật)
  - Gộp/archive 2 skill nghi trùng nhau
```

## Setup từng bước
1. Cài `hermes-jev-skills` (xem repos/hermes-jev-skills.md), bắt đầu `/jev routing shadow`
2. Deploy Langfuse (xem repos/langfuse.md) trên cùng VPS Antigravity
3. Viết cron job Antigravity gọi Hermes chạy chu trình 6 bước, tần suất khuyến nghị: hàng tuần
4. Theo dõi Langfuse dashboard 2-3 tuần trước khi cho Hermes tự IMPLEMENT (giai đoạn đầu chỉ EXPLORE+PLAN, ghi log)
5. Sau khi tin tưởng — bật IMPLEMENT cho việc "được tự làm" ở trên

## Ví dụ thực tế
Đúng case đã xảy ra thật: `agents/README.md` trỏ tới `research-pro.md` đã xoá, số liệu `ARCHITECTURE.md` lệch xa thật. Nếu chu trình này đã chạy định kỳ, Hermes tự phát hiện link chết + số liệu lệch trong lần EXPLORE hàng tuần, tự sửa (thuộc nhóm "được làm"), báo Nobitano 1 dòng trong critical-path-briefing thay vì để tồn tại nhiều tháng tới khi Nobitano tình cờ hỏi.

## Lưu ý / Lỗi thường gặp
- Bật IMPLEMENT ngay từ đầu, chưa qua giai đoạn shadow mode đủ lâu — rủi ro Hermes tự sửa sai mà không ai biết
- Để Hermes tự xoá/archive — vi phạm ranh giới đã định, đúng nguyên tắc "cần xác nhận trước khi xoá" đã áp dụng nhất quán từ đầu
- Chạy quá thường xuyên (hàng ngày) khi kho chưa thay đổi nhiều — tốn tài nguyên không cần thiết, hàng tuần là đủ

## Đánh giá cá nhân
- Điểm mạnh: nối đúng 3 công cụ vừa tìm ra (hermes-jev-skills/Langfuse/Autonomous GitHub Engineer pattern) vào 1 vấn đề thật đã xác nhận (KHO-INDEX/ARCHITECTURE/MASTER-TEMPLATE-MANIFEST đều từng bị lệch mà không ai phát hiện kịp)
- Điểm yếu: phụ thuộc 2 công cụ mới (hermes-jev-skills, Langfuse) đều chưa test thật trong hệ thống này — rủi ro cộng dồn nếu cả 2 đều có vấn đề
- Có nên dùng: 8/10 — đáng làm, nhưng PHẢI qua giai đoạn shadow mode đủ lâu trước khi tin tưởng IMPLEMENT tự động

## Link
- Nguồn: phát hiện "Hermes Agent" là framework GitHub-native thật (research 22/08/2026), hermes-jev-skills, Langfuse
- Vá lỗ hổng: skill-lifecycle-management (thiết kế nhưng chưa ai chạy định kỳ thật)
- Case đã xảy ra: agents/README.md trỏ file đã xoá, ARCHITECTURE.md số liệu lệch (cả 2 đã tự sửa tay 22/08/2026)
