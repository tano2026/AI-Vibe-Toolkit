# 10 Skill Bắt buộc cho Mọi Dự án Mới — Combo Skill theo Use Case

## TL;DR
Bundle 10 skill/nguyên tắc bắt buộc nạp vào **mọi dự án AI mới** trong hệ sinh thái Tano Agency — trộn giữa cái đã có sẵn trong kho + 3 phát hiện mới (agent-browser, supermemory, sanyuan-skills). Mục tiêu: mọi project mới không phải "tái phát minh" các nguyên tắc cơ bản đã học được từ project trước.

## 10 skill trong bundle

| # | Skill | File | Vai trò | Khi nào áp |
|---|---|---|---|---|
| 1 | Karpathy Coding Guidelines | `agents/KARPATHY-CODING-GUIDELINES.md` | Hành vi nền khi code — nghĩ trước khi code, đơn giản, sửa đúng phạm vi | Mọi task sửa/viết code |
| 2 | sanyuan-skills | `repos/sanyuan-skills.md` | Review code quality — SOLID, hiệu năng, xử lý lỗi, edge case | Trước khi merge/ship code quan trọng |
| 3 | Kiểm tra bảo mật trước deploy | `skills/kiem-tra-bao-mat-truoc-deploy.md` | 7 lỗi toang ngầm — secret, IDOR, payment, AI phá ngầm | Bắt buộc trước MỌI lần deploy |
| 4 | agent-browser | `repos/agent-browser.md` | Tự verify bằng browser thật, không chỉ nói "xong" | Mọi project có UI/web app |
| 5 | supermemory | `repos/supermemory.md` | Nhớ context xuyên session, xuyên project | Setup 1 lần đầu dự án, dùng suốt vòng đời |
| 6 | Write a Skill | `skills/write-a-skill.md` | Đóng gói quy trình đã verify thành SKILL.md tái dùng | Sau khi 1 quy trình dùng thành công ≥2-3 lần |
| 7 | Hand Off | `skills/handoff.md` | Tóm tắt context khi chuyển chat/giao agent khác | Chat dài, chuyển giao giữa Hermes/OpenClaw/Claude |
| 8 | Hallmark hoặc Huashu Design | `repos/hallmark.md` / `repos/huashu-design.md` | Chặn UI/design nhìn rõ là AI làm | Mọi project có giao diện người dùng thấy |
| 9 | Prompt Master + Grill Me | `skills/prompt-master.md` + `skills/grill-me.md` | Làm sạch brief mơ hồ ngay từ đầu | Brief mới từ CEO chưa đủ rõ |
| 10 | awesome-claude-skills (tra cứu) | `repos/awesome-claude-skills.md` | Check trước khi tự viết skill mới cho 1 dịch vụ chưa có | Cần tích hợp dịch vụ/API mới |

## Workflow ghép nối
Bắt đầu dự án mới → nạp **Karpathy Guidelines (1)** làm nền hành vi mặc định →
Brief từ CEO mơ hồ → **Prompt Master + Grill Me (9)** làm rõ →
Trong lúc code → luôn tuân **Karpathy (1)**, review qua **sanyuan-skills (2)** trước mỗi lần merge lớn →
Có UI → chạy qua **Hallmark/Huashu Design (8)** tránh AI slop, verify bằng **agent-browser (4)** →
Setup **supermemory (5)** ngay từ đầu để không mất context qua các session →
Trước khi deploy → bắt buộc qua **checklist bảo mật (3)**, không có ngoại lệ →
Quy trình nào lặp lại nhiều lần → **Write a Skill (6)** đóng gói lại →
Chat dài/chuyển giao agent → **Hand Off (7)** →
Cần tích hợp dịch vụ mới chưa có sẵn → check **awesome-claude-skills (10)** trước khi tự viết.

## Ví dụ thực tế
Dự án mới: thêm tính năng đặt bàn online cho Tano Cafe. Bắt đầu: nạp Karpathy Guidelines cho Claude Code. Brief CEO "làm chức năng đặt bàn" còn mơ hồ → Grill Me hỏi rõ (đặt trước bao lâu, giới hạn bàn/giờ, có cần xác nhận SMS không). Code xong → sanyuan-skills review trước khi merge → agent-browser tự test luồng đặt bàn thật trên browser → Hallmark check UI trang đặt bàn không bị "nhìn rõ AI làm" → trước khi deploy, chạy đủ 7 mục checklist bảo mật (đặc biệt mục IDOR — user A không xem được đơn của user B) → supermemory tự ghi nhớ quyết định "giới hạn 20 bàn/khung giờ" cho lần sau không phải hỏi lại.

## Lưu ý / Lỗi thường gặp
- Không phải dự án nào cũng cần đủ 10 — task nhỏ/nội bộ có thể chỉ cần 1, 2, 3 (Karpathy + review + bảo mật); bundle đầy đủ dành cho dự án có UI/user thật/deploy production.
- Thứ tự không cứng nhắc — vd supermemory nên setup NGAY đầu dự án (một lần), không phải chờ tới cuối.
- 3 phát hiện mới (agent-browser, supermemory, sanyuan-skills) chưa được TEST THẬT trong pipeline Tano Agency — nên thử trên 1 project nhỏ trước khi coi là bắt buộc chính thức cho mọi dự án.

## Đánh giá cá nhân
- Điểm mạnh: gộp đúng những gì đã học được qua nhiều project trước (bảo mật, hành vi AI, review) với 3 công cụ mới lấp đúng khoảng trống (tự verify UI, nhớ context, review code quality riêng biệt).
- Điểm yếu: 10 là con số khá nhiều để nhớ hết — nên có checklist ngắn dán vào mỗi CLAUDE.md project mới thay vì bắt nhớ tay.
- Có nên dùng không: 8.5/10 — đề xuất tạo 1 file `PROJECT-BOOTSTRAP.md` mẫu (checklist 10 mục ngắn gọn) để copy vào mọi dự án mới, thay vì phải tra lại stack này mỗi lần.

## Link
- Nguồn 3 phát hiện mới: mattpocock/skills, awesome-claude-skills, agent-browser, scientific-agent-skills (bỏ qua — sai domain), supermemory, Claude-Code-Game-Studios (bỏ qua — sai domain), sanyuan-skills
- Link tới từng skill: xem bảng "10 skill trong bundle" ở trên


---

> ⚠️ **SUPERSEDED** (25/07/2026) — thay bằng `stacks/20-skill-nen-theo-loai-du-an.md`. Bundle mới có thêm 10 skill + cơ chế tự chọn theo loại dự án (không phải nạp cứng cả 10 như file này). Giữ lại file này chỉ để tham khảo lịch sử.
