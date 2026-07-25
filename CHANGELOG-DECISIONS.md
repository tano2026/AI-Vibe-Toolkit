# CHANGELOG-DECISIONS — Nhật ký quyết định từ Claude Project Chat

> Mỗi lần phiên chat với Claude (Senior Advisor) ra quyết định kiến trúc/skill mới, ghi 1 dòng
> tại đây kèm push file thật trong cùng lần. Hermes có thể fetch file này để biết "có gì mới từ
> phiên cố vấn với Nobitano" mà không cần đọc lại toàn bộ lịch sử chat.
>
> Format: `- YYYY-MM-DD — <tóm tắt 1 dòng> → [file liên quan](đường-dẫn-trong-repo)`

---

## 2026-07-25

- Thêm tier **Senior Advisor** (Claude, Project Chat) — cố vấn cấp cao ngoài cấu trúc 9 role
  AI-coordination, thiết kế skill/flow/kiến trúc, không có runtime, chỉ viết file →
  [agents/company/SENIOR-ADVISOR.md](agents/company/SENIOR-ADVISOR.md)
- Quy tắc mới: mọi quyết định kiến trúc/skill trong phiên chat với Claude PHẢI xuống kho
  (push GitHub) trước khi kết thúc phiên, Claude tự đề xuất không đợi nhắc → ghi trong
  `agents/company/SENIOR-ADVISOR.md` mục SOP giai đoạn 1
- Xác định rõ 3 kho tách biệt (Project Knowledge / GitHub repo / `/mnt/skills`) — không có gì
  tự động sync giữa 3 kho, mọi cập nhật đều cần hành động chủ động trong 1 turn cụ thể
- Định hướng giai đoạn 2 (chưa build): Hermes tự gọi Claude API qua `invoke.py` khi gặp
  escalation đủ điều kiện, không cần qua tay Nobitano — chi tiết trong SENIOR-ADVISOR.md
