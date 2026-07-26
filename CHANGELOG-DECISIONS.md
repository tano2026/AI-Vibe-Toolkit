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

- Gộp cấu trúc "6-module Research Director" (từ TikTok Structure Webworks) vào
  `research-analytics-pro` hiện có, không tạo agent mới → skill mới
  [local-gap-finder](agents/research-analytics-pro/skills/local-gap-finder/SKILL.md) +
  domain playbook Local Business Intel, áp dụng ngay cho ABTRIP/An Bình + Tano Cafe
- Thêm cơ chế **Focus Mode** — khoá research vào 1 pack, tích luỹ state qua tuần, so sánh
  delta gap tuần-qua-tuần, wire vào lịch xoay vòng daily scan đã có trong
  `OPERATING-RHYTHM.md` (không tạo cadence song song) →
  [FOCUS-MODE.md](agents/research-analytics-pro/FOCUS-MODE.md)
- Tạo folder `/reports/` — lưu weekly snapshot theo pack, mặc định bật cho
  abtrip/an-binh/tano-cafe

- Review kế hoạch "3 bước" OpenClaw tự đề xuất (dọn workspace + build 8 agent worker + Claude
  Advisor) — phát hiện lệch ORG-v2.md: gộp sai marketing/content, media/designer (phá guardrail
  người tạo ≠ người đăng), nhầm ops/support với dev+ops-finance thật, thiếu HR&Admin, và đặt
  Claude thành worker nhận task qua queue (sai thiết kế SENIOR-ADVISOR.md). Đã viết bản sửa →
  [OPENCLAW-WORKER-STRUCTURE.md](agents/company/OPENCLAW-WORKER-STRUCTURE.md)
- Câu hỏi mở chưa trả lời: "ECC" (Skills ECC, 459 skills) là nguồn gì — không có định nghĩa
  trong kho, cần Nobitano xác nhận trước khi Hermes/OpenClaw build cơ chế auto-sync

- Xác định "ECC" = kho skill plugin chính thức Anthropic (~360-459 plugin, cùng nguồn Claude
  trong Project Chat có quyền đọc), không phải kho riêng của Nobitano. Trong đó ~66/407 skill
  có khả năng hành động thật (gửi/ghi/tiền) → quy tắc: Claude Advisor chỉ báo cáo skill mới,
  KHÔNG tự sync; skill hành động thật bắt buộc CEO duyệt (L2), skill tham khảo duyệt 1 lần rồi
  tự import (L1). Đã update trong OPENCLAW-WORKER-STRUCTURE.md

- Phát hiện gốc rễ mâu thuẫn: HERMES-PLAYBOOK.md ghi sai "Hermes chạy VPS" trong khi thực tế
  (Claude Code audit TANO-AGENCY local) là Hermes chạy Local Windows với Telegram bot riêng —
  2 bot, 2 taskboard (hq.db vs Airtable design vs n8n), 2 skill dir song song không đồng bộ.
  Thiết kế lại thành 1 kiến trúc: 1 CEO Bot (VPS, 24/7) → 1 Taskboard (Airtable) → dispatch
  theo LOẠI VIỆC (không theo "của Hermes/OpenClaw") → Local (nghiệp vụ nặng) hoặc VPS (24/7,
  nhẹ, public-facing). OpenClaw cũ triệt thoái, thay VPS Agent mỏng chỉ thực thi không tự quyết.
  → [UNIFIED-ARCHITECTURE.md](agents/company/UNIFIED-ARCHITECTURE.md) — STATUS: DRAFT, chờ xác
  nhận VPS đã reboot chưa + tên 8 phòng ban thật trong agent-core/spec.py trước khi thực thi

- UNIFIED-ARCHITECTURE.md → v2, dựa trên audit thật (Claude Code đọc trực tiếp agent-core):
  OpenClaw KHÔNG có code sống trong repo, chỉ còn archive/docs — "2 não đá nhau" hoá ra là 1 hệ
  thống sống (agent-core Local, 9 agent thật: ceo/research/dev/sales/marketing/media/operations/
  support/analytics) + 1 khái niệm gần chết (OpenClaw). Quyết định: khai tử OpenClaw (không phải
  migrate), giữ nguyên cách chia agent thật (không ép theo 9-role lý thuyết ORG-v2 cũ — 4 điểm
  lệch đã note rõ, ORG-v2.md cần viết lại theo thực tế). Gap thật: không có HR&Admin agent —
  tạm gộp vào operations, tách riêng khi khối lượng tăng. Còn 1 việc chờ: Nobitano tự reboot VPS
  (AI không có quyền SSH/provider console), sau đó SSH check pm2/opt-openclaw để xác nhận nốt

- SỬA quyết định trước: OpenClaw KHÔNG khai tử — Nobitano xác nhận mô hình 3 tầng
  Hermes(não, quyết định) → OpenClaw(tay chân, chỉ thực thi) → Claude(cố vấn, ngoài runtime).
  OpenClaw build LẠI TỪ ĐẦU (không hồi sinh code cũ có Telegram bot riêng — đó là nguồn gốc
  "2 não đá nhau"). Luật bất biến: OpenClaw không có kênh nhận lệnh riêng, chỉ pull task từ
  Taskboard Hermes ghi, không có quyền tự quyết DECISION-MATRIX.md mức nào. Đã update
  UNIFIED-ARCHITECTURE.md

- Thêm kênh HỎI trực tiếp OpenClaw (`/oc status`, `/oc log`, `/oc health`) — vẫn 1 Telegram bot
  duy nhất (không mở bot thứ 2), nhưng route thẳng câu hỏi TRẠNG THÁI tới OpenClaw, bỏ qua
  Hermes phân tích. Phân định rõ: "báo cáo về chính nó" luôn trực tiếp được, "hành động/quyết
  định mới" luôn phải qua Hermes + Taskboard — không phá luật 1 bộ não

- Thêm HERMES-SOUL.md — file bản sắc/nguyên tắc cốt lõi cho Hermes, đúc kết trực tiếp từ bài
  học vụ OpenClaw thật ra vẫn sống (7 ngày uptime, Zalo OA thật) trong khi audit Local kết luận
  nhầm "không có gì". 4 nguyên tắc chính: (1) không kết luận khi chưa nhìn tận nơi — thiếu quyền
  truy cập ≠ không tồn tại, (2) verify trước khi tin kể cả tự báo cáo của mình (vụ hallucinate
  sanyuan-skills), (3) chạm production/khách hàng thật luôn dừng hỏi dù có vẻ rõ đường đi, (4)
  assumption cũ là tạm, phải tự hỏi lại trước khi dùng làm nền quyết định mới

- Sửa xong 2 việc tồn đọng:
  1. sanyuan-skills.md — KHÔNG phải hallucinate hoàn toàn như đã báo trước (đính chính): repo
     có thật (sanyuan0704/sanyuan-skills, 3.6K sao, nội dung mô tả khớp 100%), chỉ URL bị để
     placeholder <org>. Đã sửa URL + cách cài đúng (npx skills add, không phải git clone)
  2. supermemory.md — sửa claim sai "có plugin cho Hermes": chỉ OpenClaw có plugin thật
     (openclaw-supermemory), Hermes dùng qua MCP chung không có plugin riêng. Lý do lỗi: nhầm
     "Hermes agent" (NousResearch/hermes-agent, model LLM khác tên) với Hermes của Tano Agency

- Thêm mục "Án lệ" vào HERMES-SOUL.md — 6 case study thật (không phải lý thuyết) đúc kết từ
  phiên làm việc hôm nay: (1) audit Local nhầm kết luận OpenClaw chết trong khi nó sống + phục
  vụ Zalo OA thật, (2) URL placeholder bị viết như đã verify, (2b) NGƯỢC LẠI — gán nhãn
  "hallucinate" cũng sai vì chưa tự verify lại (sanyuan-skills hoá ra là thật), (3) quyết định
  kiến trúc phân mảnh qua nhiều phiên chat riêng biệt (role 10, Paperclip bị quên), (4) cùng 1
  dạng lỗi "2 hệ thống làm trùng việc" lặp lại ở tầng khác (2 não / 2 lớp governance), (5) quy
  trình chậm mà chắc đã cứu 2 lần thật (publish gate, classify_task routing)

- Nâng cấp bundle 10→20 skill nền cho dự án mới — thêm 10 skill mới (database-migrations,
  fact-checker, anti-ai-tells, personal-voice, architecture-decision-records, api-design,
  production-code-audit, git-workflow, token-budget-advisor, duplicate-checker). Đổi cơ chế:
  không còn "nạp cứng cả 10/20" — gắn tag ALWAYS/CODE/UI/DATA/CONTENT/DEPLOY/RESEARCH, mỗi dự án
  tự lọc theo 6 câu hỏi đặc điểm (có code/UI/DB/content/deploy thật/research không). Bundle 10
  cũ đánh dấu SUPERSEDED, giữ lại tham khảo lịch sử →
  [stacks/20-skill-nen-theo-loai-du-an.md](stacks/20-skill-nen-theo-loai-du-an.md)
