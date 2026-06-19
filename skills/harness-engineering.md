# Harness Engineering — Skill / Framework

## TL;DR
Xu hướng AI 2026: sau Prompt Engineering (2022-24) và Context Engineering (2025), Harness Engineering là kỷ nguyên thứ 3 — xây cái "khung" xung quanh AI agent để nó chạy ổn định production, không phải chỉnh prompt mãi.

## Khi nào dùng
Khi mày đang: build AI agent mà demo thì được nhưng chạy thật thì gãy, deploy agent lên production mà unreliable, bị hỏi tại sao agent làm đúng 1 bước rồi sai lung tung từ bước 2 trở đi. Cũng áp dụng khi muốn thiết kế hệ thống Hermes + OpenClaw chạy 24/7 không cần canh.

## Khung tư duy Harness Engineering

### Roadmap tiến hóa AI Engineering
```
Prompt Engineering (2022-2024)
→ Tập trung: viết câu lệnh đẹp, magic words, few-shot
→ Vấn đề: đổi model version là gãy hết

Context Engineering (2025)
→ Tập trung: nhồi đúng thông tin vào context window
→ Vấn đề: task dài → context window đầy → agent "quên"

Harness Engineering (2026)
→ Tập trung: xây toàn bộ hệ thống XUNG QUANH model
→ Công thức: Agent = Model + Harness
→ Tức là: Harness = Agent - Model (mọi thứ ngoài model)
```

### Định nghĩa nhanh
**Analogy:** Model = CPU, Context = RAM, Harness = Hệ điều hành, Agent = Ứng dụng.
Không ai chạy phần mềm trực tiếp trên CPU không có OS. Tương tự, không deploy agent mà không có harness.

Nguyên tắc cốt lõi (Mitchell Hashimoto định nghĩa, Feb 2026):
> "Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."

### 3 trụ cột của Harness Engineering

**Trụ 1 — Context Engineering (quản lý thông tin)**
- Context compression: tóm gọn thông tin cũ mà giữ đủ ý
- Dynamic context injection: load đúng thứ cần, đúng lúc cần — không nhồi hết từ đầu
- Knowledge persistence: lưu tiến độ ra file ngoài (progress.txt, db) để agent đọc lại khi restart
- Priority scoring: thứ gì quan trọng nhất thì sống sót khi context bị cắt

**Trụ 2 — Architectural Constraints (giới hạn phạm vi)**
- Tool access controls: agent được phép dùng tool nào, chỉnh file nào, gọi API nào
- Structural enforcement: linter/CI tự check output agent trước khi commit — không để agent gãy cả codebase
- Scope boundaries: 1 task chỉ được đụng 1 phần nhỏ, không để agent cascade khắp nơi
- Safety guardrails: filter output trước khi ra production

**Trụ 3 — Entropy Management (chống "rỉ sét" dần dần)**
- Agent code càng nhiều thì inconsistency tích lũy càng nhanh (naming drift, dead code, doc lỗi thời)
- Dùng agent chuyên biệt để định kỳ audit, refactor, dọn test, cập nhật docs
- Monitor model drift: phát hiện khi chất lượng output giảm do model bị update phía provider

## Setup / Áp dụng từng bước

### Bước 1 — Xây progress persistence
```
# Tạo file progress.txt để agent tự ghi tiến độ
echo "TASK: [tên task] | STATUS: in_progress | STEP: 1/5 | LAST_ACTION: ..." > progress.txt
# Agent đọc file này mỗi khi start, không phải nhớ từ đầu
```

### Bước 2 — Đặt tool access controls
Trong system prompt của agent, ghi rõ:
```
ALLOWED TOOLS: web_search, bash_tool, create_file (trong /home/claude/ only)
FORBIDDEN: delete files, push to main branch without review, external API calls to payment systems
REQUIRE HUMAN APPROVAL: push production, modify database schema
```

### Bước 3 — Xây verification loop
```
Sau mỗi bước agent làm xong:
→ Chạy linter/test tự động
→ Nếu pass → tiếp tục
→ Nếu fail → agent đọc error, tự fix, retry (max 3 lần)
→ Nếu vẫn fail → escalate human
```

### Bước 4 — Entropy audit định kỳ
Đặt 1 cron job hoặc Hermes task chạy hàng tuần:
```
"Review toàn bộ /repos/ và /mcps/ trong AI Vibe Toolkit,
tìm entry nào đã outdated (repo bị archive, star thay đổi nhiều),
báo cáo list cần update"
```

## Ví dụ thực tế
**Vấn đề:** Hermes agent đang viết file .md cho kho, nhưng mỗi lần restart lại làm lại từ đầu (quên đã viết cái gì rồi).
**Harness fix:** Tạo file `VAULT/session-progress.md` — agent ghi vào đó sau mỗi task xong. Lần sau start lại, agent đọc file này trước, biết bắt đầu từ đâu.

**Vấn đề:** Agent push nhầm file nhạy cảm lên GitHub.
**Harness fix:** Thêm constraint "không push file có keyword: token, api_key, password, secret" — linter chặn trước khi PUT request được gọi.

## Lưu ý / Lỗi thường gặp
- "Harness Engineering" đang là buzzword mạnh trong 2026 — nhiều bài viết làm nó nghe phức tạp hơn thực tế. Core idea đơn giản: xây hệ thống xung quanh AI để nó reliable, không phải cứ chỉnh prompt.
- Constraint không làm agent yếu hơn — ngược lại, agent trong môi trường có giới hạn rõ ràng chạy tự tin hơn vì biết "sai là có người catch", không sợ làm gãy gì quan trọng.
- Áp ngay vào AI Vibe Toolkit: TRACKER.md là 1 dạng harness (progress persistence), token placeholder trong file push lên GitHub là 1 dạng constraint, sequential push thay vì parallel là 1 dạng entropy prevention.
- 88% AI agent project không lên được production vì harness quá fragile (số liệu Deloitte 2026) — lý do không phải model tệ, mà là hệ thống xung quanh không ổn.

## Đánh giá cá nhân
- Điểm mạnh: framework thực sự giải quyết đúng vấn đề mà bất kỳ ai build agent đều gặp — agent reliable trong production. Không phải buzzword thuần tuý.
- Điểm yếu: term còn mới, tài liệu đang rải rác nhiều nguồn, chưa có 1 "canonical book" hay course nào thực sự chuẩn hoá hết.
- Có nên dùng: 9/10 — bắt buộc phải hiểu nếu mày muốn Hermes + OpenClaw của AI Vibe Toolkit chạy production 24/7 không người trông.

## Link
- Bài gốc định nghĩa chính thức (OpenAI, Ryan Lopopolo, Feb 2026): tìm "Harness Engineering: Leveraging Codex in an Agent-First World" trên OpenAI blog
- Bài giải thích dễ hiểu nhất: https://primotech.com/harness-engineering-beyond-prompt-context-engineering/
- Full framework 3 pillars: https://harnessengineering.academy/blog/what-is-harness-engineering-introduction-2026/
- Faros.ai breakdown (5 layers): https://www.faros.ai/blog/harness-engineering
