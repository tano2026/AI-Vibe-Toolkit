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

- Thêm 2 cơ chế quan trọng: LOOP-TOKEN-GOVERNOR.md (wire skill agentic-loop-optimizer có sẵn
  vào 4 tier OmniRoute thật + exit condition theo risk_level L0-L3 + circuit breaker tự phát
  hiện job stuck) và SECURITY-WALL.md (5 lớp, viết ngay từ lỗ hổng thật vừa tìm — .env VPS chứa
  ZALO_ACCESS_TOKEN + DEEPSEEK_API_KEY plaintext, đọc được bằng cat). Cả 2 wire skill có sẵn
  trong kho (destructive-command-guard, security-review) thay vì viết lại, chỉ thêm lớp áp dụng
  cụ thể cho 9 agent thật + tình huống VPS thật

## 2026-08-15

- Council (4-voice: Architect/Skeptic/Pragmatist/Critic) quyết định video engine cho GMSP:
  chọn **OpenMontage** thay vì DramaClaw — use-case khớp voiceover/explainer, DramaClaw tối ưu
  cho narrative/nhân vật (Director World 3GS) không hợp với format GMSP. **ĐIỀU KIỆN BẮT BUỘC:**
  config OpenMontage dùng provider `elevenlabs_tts`, KHÔNG dùng Piper mặc định — Piper tiếng
  Việt (vi_VN) chỉ có voice chất lượng low/medium (xác nhận từ rhasspy/piper VOICES.md), không
  đạt chuẩn phát podcast. Skeptic dissent (đã nhận): nên test 1-2 tập GMSP bằng stack thủ công
  hiện có (ElevenLabs → OBS → CapCut) trước khi đầu tư setup OpenMontage, chỉ scale khi chứng
  minh cần volume đều đặn. Chi phí thật: free tier ElevenLabs chỉ 10k ký tự/tháng (~2-3 phút
  audio) — GMSP làm nhiều tập/tháng sẽ vượt free tier nhanh, cần tính phí ElevenLabs riêng
  ngoài chi phí OpenMontage ($0-1/video nếu dùng cloud API mặc định) →
  [repos/openmontage.md](repos/openmontage.md)

## 2026-08-21

- Audit tổng toàn kho (1.731 file) — phát hiện KHO-INDEX.md lệch nặng (số liệu tháng 6/2026, thiếu hoàn toàn 7 Pro Agent/EXPERT-CORE/DeepSeek Harness/Jev) → [KHO-INDEX.md v3.0](./KHO-INDEX.md)
- Phát hiện file khả nghi cần dọn: research-pro.md (bản cũ của research-analytics-pro/), 3 cụm HERMES-*/OPENCLAW-* chưa rõ thứ tự đọc, "Team Thục Hán" trong CLAUDE-CODE-BRIDGE.md chưa xác nhận được — CHƯA XOÁ, chờ Nobitano xác nhận
- Hoàn thiện 7/7 Pro Agent đồng chuẩn (thêm Designer Pro từ số 0, Hermes Adapter cho Sales-CEO + Digital Marketing) → agents/designer-pro/, agents/sales-ceo/HERMES-ADAPTER.md, agents/digital-marketing-agent/HERMES-ADAPTER.md
- Research Swarms (kyegomez/swarms) — tương thích trực tiếp skills_dir với format SKILL.md đang dùng, đề xuất thay cơ chế load_skill() viết tay → [repos/swarms.md](./repos/swarms.md)
- Xoá `agents/research-pro.md` (xác nhận trùng, đã bị `research-analytics-pro/` thay thế) — Nobitano duyệt
- Xoá `skills/ecc/` (271 file, confirm trùng 100% skill phẳng đã có) — dọn kho trước khi Nobitano symlink toàn bộ skills/ vào Claude Code local
- Xây Customer Satisfaction Pro (agent thứ 8) — phát hiện khoảng trống sau khi so sánh cấu trúc với mô hình "AI Employees" (Mark Fulton, github.com/markfulton/ai-employees) — không Pro Agent nào trong 7 cái trước phụ trách CSKH/rủi ro rời bỏ khách. Thêm EXPERT-CORE.md section 8 (ngưỡng SLA/FCR thật, nguồn SQM Group/HubSpot/Zendesk 2026). Kèm skill critical-path-briefing (dùng chung mọi agent báo cáo, đúc kết từ cơ chế Chief of Staff của AI Employees)
- Viết COMPANY-CHARTER.md — nghiên cứu 2 repo thật (opc_agent/OPC, OneManCompany/OMC 422 sao) để đặt đúng tên cho kiến trúc đã có (Vessel=Hermes/OpenClaw/DSH/Claude Code/Antigravity, Talent=8 Pro Agent) và vá 2 khoảng trống: task-intake-quality-gate (vai EA, gác cổng trước dispatch) và skill-lifecycle-management (vai HR, audit định kỳ 590+ skill — vá đúng loại lỗi đã xảy ra thật với ecc/)
- Viết CLIENT-ONBOARDING-TEMPLATE.md — dịch mô hình FDE + MASTER-TEMPLATE-MANIFEST thành quy trình bán hàng thật cho khách phi kỹ thuật: đổi tên 8 Pro Agent thành "phòng ban AI", intake theo Deepthink (1 câu/lần), giao kết quả cụ thể trước khi bàn hợp đồng dài hạn. Đồng thời chỉ rõ mâu thuẫn giữa "template phục vụ khách" (bán outcome, đúng FDE) và "kho prompt bán riêng" (bán tool, đúng anti-pattern FDE cảnh báo) — 2 việc không nên trộn lẫn nội dung
- Viết production-signal-feedback-loop cho Infra Ops Agent — nối 2 thiết kế riêng lẻ (kiến trúc Jev cascade + vòng khép kín ADLC từ infographic Nobitano chia sẻ) thành 1 skill cụ thể: tín hiệu vận hành tự phân loại qua Jev (Noul/Choice/Score) rồi tự tạo intent.md mới, chỉ hỏi Nobitano khi confidence <50%. Có fallback rule-based khi Jev còn waitlist
- Cập nhật Agentic Factory lên v2 — bản gốc (đầu phiên) viết trước khi có EXPERT-CORE per-role, Vessel/Talent, chuỗi tạo tác ADLC, Jev cascade. v2 thêm 3 bước: (1) grounding bắt buộc vào EXPERT-CORE, (2) Vessel/Talent thay 'Tầng Tay/Não/Cơ' tự đặt, (3) wire vào EA gate/briefing/HR lifecycle — đúc kết từ quy trình THẬT đã dùng xây 8 Pro Agent
- Vá lỗ hổng: nhóm 'Đầu Não' (harness/loop/superpowers/humanizer) đã phát hiện từ trước nhưng CHƯA từng ghi vào tài liệu chính thức, chỉ nằm trong chat -> viết agents/company/CORE-META-SKILLS.md, gắn vào KHO-INDEX.md và agentic-factory Bước 1. Đồng thời phát hiện + sửa 2 lỗi thật trong KHO-INDEX.md: escaped backtick sai cú pháp, và agent thứ 8 (customer-satisfaction-pro) chưa được thêm vào TẦNG 1 dù đã push từ trước
- Chạy skill-lifecycle-management lần đầu — audit các file 'meta' phát hiện 3 file stale nặng: agents/README.md (còn trỏ agents/research-pro.md ĐÃ XOÁ, ghi '3 agents' thiếu DeepSeek Harness/Claude Code/8 Pro Agent), ARCHITECTURE.md gốc (ghi cứng 'tháng 6/2026', số liệu 49 repos/34 MCPs/406 skills lệch xa thật 236/57/591), MASTER-TEMPLATE-MANIFEST.md (thiếu agent thứ 7-8 và CORE-META-SKILLS.md). Cả 3 đã viết lại theo đúng thực tế 22/08/2026
- Viết OPERATING-MODEL.md ở gốc kho — đóng gói toàn bộ mô hình (Lớp Luật/Năng lực/Vessel + luồng task + checklist hành động RIÊNG cho Hermes/OpenClaw 2.0/DeepSeek Harness) thành 1 brief giao việc, không chỉ tài liệu mô tả. Trio đọc file này trước để biết chính xác việc cần làm — DSH có đúng 1 việc ưu tiên (thiết lập kết nối đầu tiên vào kho, hiện là 0)
- Research hermes-jev-skills (bridge Jev có sẵn cho Hermes, thay production-signal-feedback-loop tự viết) + Langfuse (tích hợp chính thức trace Jev). Viết hermes-autonomous-kho-maintenance — nối 3 thứ (Hermes Autonomous GitHub Engineer + hermes-jev-skills shadow mode + Langfuse quan sát) thành 1 chu trình Explore-Plan-Implement-Test-Fix-Verify áp cho bảo trì kho tự động, vá lỗ hổng skill-lifecycle-management chưa ai chạy định kỳ thật (case thật: agents/README.md/ARCHITECTURE.md đều bị lệch mà không ai phát hiện kịp)
- Research giải pháp kết nối Zalo — phát hiện OpenClaw (đã dùng sẵn) có 3 kênh chính thức: zalouser (cá nhân, rủi ro khoá nick, OpenClaw tự cảnh báo), zaloclawbot (trợ lý cá nhân, API chính thức, AN TOÀN, không cần đăng ký OA riêng — khuyến nghị cho nhu cầu 'Zalo Agent' cá nhân Nobitano), Zalo OA Developer chuẩn (bắt buộc cho bot khách hàng ABTRIP/Tano Cafe/Wonder Mart, cần đăng ký OA + phí tháng). Không cần tự xây kết nối Zalo từ đầu
- Research Pydantic AI — framework Tier 1 thật (xếp cùng LangChain/CrewAI/Vercel AI SDK), hỗ trợ Claude trực tiếp, validate output có cấu trúc + tự retry. Giải quyết đúng vấn đề đang chờ Jev (output đáng tin cậy) nhưng dùng NGAY với Claude, không cần waitlist. Cập nhật production-signal-feedback-loop: thay fallback rule-based bằng Pydantic AI
- Quét bản đồ 'Modern AI Ecosystem' (~90 tool, 11 nhóm) — phát hiện ĐÚNG 1 nhóm trống hoàn toàn trong kho: AI Security/Guardrails. Research Presidio (PII, Microsoft)/NeMo Guardrails (tool-execution, NVIDIA) — chọn Presidio làm trọng tâm vì khớp rủi ro thật (data khách hàng ABTRIP/hợp đồng PVN/tài khoản ngân hàng). Phát hiện phụ: LLM Guard (Protect AI) đã bị khai tử 7/2026, loại khỏi cân nhắc
- Viết ffmpeg-media-toolkit vào agents/company/skills/ (dùng chung, không riêng agent nào) — vá lỗ hổng vừa phát hiện: srt-whiteboard-animation/product-film-skill/vox-explainer đều âm thầm cần FFmpeg riêng, không ai gom thành 1 nơi chuẩn. Bộ lệnh chuẩn 8 thao tác + bài học thật (cần ffmpeg-full không phải ffmpeg thường để chèn phụ đề)

## 2026-10-07
- ĐÍNH CHÍNH NGÀY: các dòng nhật ký nằm dưới mục "2026-08-21" từ dòng ~140 trở đi thực ra viết trong khoảng 22/09–06/10/2026 (đối chiếu lịch sử commit), không phải tháng 8. Các mốc "22/08/2026" trong OPERATING-MODEL, ARCHITECTURE, KHO-INDEX, agents/README, COMPANY-CHARTER, CORE-META-SKILLS, CLIENT-ONBOARDING-TEMPLATE, MASTER-TEMPLATE-MANIFEST, hermes-autonomous-kho-maintenance đã sửa thành 22/09/2026.
- Thêm repos/twenty-crm.md: sửa lại phân tích trước — CVE-2026-44492/44494/44495 là lỗi thư viện axios (twenty-server main đã ghim axios ≥1.16.0), KHÔNG phải lỗi riêng của Twenty. Lỗ hổng riêng của Twenty 2026 (command execution 9.9, SQLi 9.1, lộ mật khẩu qua GraphQL 9.6 ngày 05/10/2026...) lấy từ trang tổng hợp, chưa đối chiếu NVD, chưa xác nhận bản vá từng lỗi → quy tắc: chỉ nội bộ, sau VPN, luôn dùng bản mới nhất. License trộn AGPLv3 + file Enterprise (477 file) + package MIT; chưa kết luận về Twenty Application Exception.
- Thêm stacks/twenty-crm-abtrip-internal.md (spec ABTRIP nội bộ). Sửa so với bản nháp: bỏ câu khẳng định "AGPL không bị kích hoạt", bỏ framing CVE sai, thêm mục 0 (quyết định giữ hay bỏ ABTrip CRM tự xây) và mục 7 (test PASS/FAIL trước mọi thiết kế thêm). Chưa triển khai.
- Thêm repos/claude-code-templates.md (aitmpl.com, MIT, ~32K sao). Rủi ro chuỗi cung ứng (thành phần cộng đồng) + bị chặn bởi Claude Code chưa chạy. Ghi chú SKILL.md là chuẩn mở (~32 công cụ) = CHƯA kiểm chứng.
- Ai-auto-generate-video: KHÔNG viết mới — kho đã có repos/ai-auto-generate-video.md và script #134.
- TRACKER.md: sinh lại bằng tools/build_index.py (mới thêm vào kho). Gỡ các dòng ID #342–#377 từng tay-append (sai schema, lẫn vào bảng Stacks); các mục agents/… vẫn tra ở CHANGELOG và KHO-INDEX. Thêm đủ dòng cho các repo mới (gồm awesome-claude-5-5-videos từng thiếu). Quy tắc từ nay: KHÔNG tay-append TRACKER; chạy `python3 tools/build_index.py`. (Project Instructions cũ còn ghi "append-only" — lỗi thời, cần sửa ở phía Nobitano.)
- KHO-INDEX.md làm mới số liệu: 1.528 file (skills 590, agents 219, repos 253, mcps 57, stacks 19, content 335, max script #322).
- QUYẾT ĐỊNH (Nobitano, 07/10/2026): chuyển CRM sang Twenty; ABTrip CRM tự xây đóng băng, KHÔNG xoá, giữ chỉ-đọc ≥30 ngày. Thêm deploy/twenty-abtrip/ (install-twenty.sh, backup-twenty.sh, test-twenty-api.py, HUONG-DAN-TRIEN-KHAI.md) viết từ docker-compose.yml + .env.example chính thức (đã kiểm `docker compose config` hợp lệ; ghim v2.45.0; cổng 3000 chỉ nghe localhost; truy cập qua Tailscale). CHƯA chạy trên VPS thật. Điều kiện chính thức chuyển: PASS test API + backup đã thử khôi phục.
- Thêm repos/higgsfield-mcp-unified.md (Hikhakk, MIT, 4 sao, alpha v0.1.0). Đối chiếu với mcps/higgsfield.md (bản chính thức). Cloud backend suy ngược, tác giả tự ghi "probably against ToS" → khuyến nghị KHÔNG bật trên tài khoản thật; ưu tiên bản chính thức.
- "Cinematic techniques": chưa xác định được nguồn (có ≥3 ứng viên: fal-ai-community/skills cinematography, SamuraiGPT muapi-cinema-director, OSideMedia/higgsfield-ai-prompt-skill) — chờ Nobitano chỉ đúng nguồn, chưa viết.
- Sửa repos/impeccable.md (bản cũ sai: 23 lệnh, "không chạy trên Hermes", thiếu số sao/license). README hiện tại: 24 lệnh, ~77,8K sao, Apache-2.0, Hermes/DeepSeek Harness/Antigravity/Gemini CLI trong danh sách hỗ trợ. ĐÃ CHẠY THẬT `npx impeccable detect` (v4.1.0) trên HTML mẫu xấu → 11 lỗi, không cần key. 24 lệnh qua agent: chưa test.
- Thêm stacks/cinematic-techniques-ai-video.md (so sánh fal cinematography / muapi-cinema-director / higgsfield-camera — nội dung từ trang tổng hợp claudeskills.info, chưa đọc repo gốc, chưa cài thử) + agents/designer-pro/skills/cinematic-shot-prompt-core/SKILL.md (công thức 6 phần SCLCAM thuần, chưa test trên generator).

## 2026-10-08
- Agency-agents: ĐÃ CÓ trong kho (repos/agency-agents.md, repos/agency-agents-app.md, skills/agency-agents-skill, script #128 và #181) → không tạo entry mới. Đối chiếu repo thật (commit f99f6aa, 08/10): ~280 persona (bản cũ ghi 232/220), MIT, có script cài cho Hermes (plugin lazy-router, 4 tool), OpenClaw, DeepSeek Harness (dsh), Antigravity — bản cũ thiếu Hermes + DSH và gọi nhầm OpenClaw là "Hermes ecosystem". Viết lại repos/agency-agents.md, hạ điểm 9,5 → 7/10 (persona prompt ≠ kỷ luật Pro Agent; chưa cài thử). repos/agency-agents-app.md còn ghi 232 — chưa sửa.
- Thêm repos/prompt-motion.md (prompt-motion.com — tên người dùng gõ "promt-motion.com" là sai chính tả). Thư viện ~230 video motion bằng Opus 5.5 kèm prompt/skill, @p4nthera_ tuyển chọn. robots.txt: ai-train=no, use=reference, ~35 crawler AI bị chặn → quy tắc: tra tay từng mục, không cào/mirror/train, kho chỉ lưu con trỏ + ghi chú + nguồn. Nghiên cứu từ trang chủ + 5 mục (4 Skill) — không đọc hết. Sandbox không vào trực tiếp được trang (proxy 403) nên code Hermes chưa test. Thêm agents/designer-pro/skills/prompt-motion-reference/SKILL.md. 3 skill mới thấy chưa có entry: Leonxlnx/cinetic, heygen-com/hyperframes-community-skills (session-story), buildfastwithai/buildfast-skills (generative-film-skill) — chờ Nobitano chỉ cái nào cần đào sâu; product-film-skill đã có sẵn.
- Thêm 3 entry cho 3 skill thấy trên prompt-motion.com (đọc từ bản clone nông của repo gốc, 08/10/2026): `repos/cinetic.md` (MIT, v1.0.0, 7/10 — đắt ~95 phút/626K token/phim theo tác giả; Remotion cần license công ty ≥4 người, nên dùng engine HyperFrames; chỉ `pick.py` đã chạy thật offline), `repos/hyperframes-session-story.md` (3/10 — đọc lịch sử Claude Code/Codex cục bộ = dữ liệu nhạy cảm; `snapshot` phải có `--describe false`; không chạy trên phiên ABTRIP), `repos/buildfast-generative-film-skill.md` (MIT, 6/10 — nhẹ nhất, chỉ Python+ffmpeg; sandbox thiếu pycairo nên CHƯA render; font tiếng Việt có dấu chưa kiểm). Số sao chưa đo (API GitHub bị chặn). Cập nhật bảng trong `repos/prompt-motion.md`. Không viết script video riêng (chưa render được phim nào để quay). Số file KHO-INDEX: 1.540.
- Quy ước kho (Nobitano nhắc 08/10/2026): kho thuộc Tano Agency, KHÔNG gắn một thương hiệu cố định. Sửa 3 entry mới (cinetic, session-story, generative-film-skill) thành trung lập brand: ví dụ dùng [placeholder], brand cụ thể chỉ làm minh hoạ. Rà tương tự khi viết entry mới.
- Quy ước (Nobitano chốt 08/10/2026): kho phục vụ Tano Agency, trung lập brand. Brand cụ thể (ABTRIP, Tano Cafe, Wonder Mart, TanoOS…) chỉ là ví dụ minh hoạ, TRỪ skill/entry/deploy làm riêng cho brand đó (vd stacks/twenty-crm-abtrip-internal.md, deploy/twenty-abtrip/) thì giữ nguyên. Đã trung lập hoá các entry viết trong đợt này: twenty-crm, higgsfield-mcp-unified, impeccable, agency-agents, prompt-motion, cinematic-shot-prompt-core, cinetic, session-story, generative-film-skill. ~85 file repos/ cũ còn nhắc brand — CHƯA rà, rà dần khi đụng tới.
- Thêm agents/GEMINI-LIBRARIAN.md: instruction để Gemini (Gem / GEMINI.md / Antigravity rules) làm thủ thư kho giống Claude — research, viết entry theo khung, Agent Integration. Quy tắc đa-người-viết: Gemini làm trên nhánh gemini/<slug>, không đẩy main, không sửa tay TRACKER (chạy build_index.py), không chứa token. Chưa thử trên Gemini thật.
