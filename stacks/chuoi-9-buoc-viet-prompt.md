# Chuỗi 9 bước viết Prompt — Combo Skill theo Use Case

## TL;DR
Ý tưởng lộn xộn trong đầu → prompt hoàn chỉnh sẵn dùng (rõ mục tiêu, đủ context, đúng giọng
văn) — 9 skill nối tiếp nhau, mỗi skill xử lý đúng 1 việc. Nguồn cảm hứng: infographic
"9 Claude Skills that write your prompts for you" (@amplified23). Không bắt buộc chạy đủ cả 9
bước — chọn bước cần theo tình huống.

## Các skill trong chuỗi
1. **Prompt Maker** (`skills/prompt-master.md` — đã có) → brain dump thô → task spec sạch
2. **Grill Me** (`skills/grill-me.md` — đã có) → hỏi liên tục tới khi hết mơ hồ
3. **How To** (`skills/how-to.md` — mới) → vạch bước cụ thể cho mục tiêu chưa biết cách làm
4. **Optimizer** (`skills/prompt-optimizer.md` — đã có, tương đương "Optimizer 4.8") → polish
   prompt cho model task-execution chuẩn
5. **Fable Prompter** (`skills/fable-prompter.md` — mới) → polish riêng cho model thiên sáng tạo
6. **Personal Voice** (`skills/personal-voice.md` — mới) → chỉnh đúng giọng văn người dùng
7. **Anti-AI** (`skills/anti-ai-tells.md` — mới) → xoá dấu vết AI khỏi bản draft
8. **Write a Skill** (`skills/write-a-skill.md` — mới) → đóng gói thành SKILL.md tái sử dụng
9. **Hand Off** (`skills/handoff.md` — mới) → tóm tắt context để chat mới/agent khác tiếp tục

## Workflow ghép nối
Ý tưởng lộn xộn → **Prompt Maker** (1) làm sạch task spec →
Nếu còn mơ hồ: **Grill Me** (2) hỏi tới khi rõ → Nếu rõ nhưng chưa biết cách làm: **How To** (3)
vạch bước →
Chọn nhánh theo loại model đích: **Optimizer** (4) cho task-execution HOẶC **Fable Prompter**
(5) cho model sáng tạo →
**Personal Voice** (6) chỉnh giọng văn →
Chạy prompt, có draft → **Anti-AI** (7) xoá dấu vết AI khỏi kết quả →
Nếu quy trình này sẽ dùng lại nhiều lần: **Write a Skill** (8) đóng gói →
Cuối phiên làm việc hoặc chuyển giao: **Hand Off** (9) tóm tắt context

Không phải lúc nào cũng chạy đủ 9 bước — vd task đơn giản chỉ cần bước 1 rồi chạy luôn; task
phức tạp cần lộ trình nhiều bước.

## Ví dụ thực tế
Brief mơ hồ từ CEO: "làm cái gì đó cho content GMSP về tâm lý học" → **Prompt Maker** làm sạch
thành "viết script GMSP giải thích 1 framework tâm lý học liên quan chủ đề số phận" → còn thiếu
info nào cụ thể? **Grill Me** hỏi: framework nào, độ dài bao nhiêu → CEO chọn Locus of Control →
**Optimizer** polish prompt rõ ràng → **Personal Voice** chỉnh giọng kể chuyện đúng tông GMSP →
chạy ra script → **Anti-AI** xoá cụm sáo rỗng → xong, không cần bước 8/9 vì đây là task 1 lần.

## Lưu ý / Lỗi thường gặp
- 6/9 skill mới viết dựa trên mô tả từ infographic (chưa có bản gốc thật của tác giả) — coi là
  bản diễn giải theo tinh thần, không phải copy nguyên văn skill gốc.
- Đừng chạy máy móc đủ 9 bước cho mọi task — phần lớn task đơn giản chỉ cần bước 1, thêm bước
  làm task nhỏ trở nên rườm rà không cần thiết.
- Bước 4 vs 5 (Optimizer vs Fable Prompter) chọn 1 trong 2, không chạy cả hai — tuỳ model đích.

## Đánh giá cá nhân
- Điểm mạnh: chia nhỏ đúng từng việc trong quy trình viết prompt tốt, dễ nhớ, dễ áp dụng từng
  phần riêng lẻ không cần theo đủ chuỗi; khớp trực tiếp với cách kho AI-Vibe-Toolkit vận hành
  (research → viết → đóng gói skill → push).
- Điểm yếu: 9 bước có thể overkill cho task đơn giản; 1 số bước (Fable Prompter) ít khi cần thiết
  trong thực tế công việc hàng ngày của Tano Agency.
- Có nên dùng không: 8/10 — hữu ích nhất là bước 1-2 (Prompt Maker + Grill Me, đã có sẵn) và
  bước 8-9 (Write a Skill + Hand Off) — 2 cặp này dùng thường xuyên nhất trong thực tế.

## Link
- Nguồn cảm hứng: infographic TikTok @amplified23 "9 Claude Skills that write your prompts for you"
- Link tới từng skill: xem mục "Các skill trong chuỗi" ở trên
