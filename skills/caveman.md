# Caveman — Prompt Template / System Prompt

## TL;DR
Skill bắt Claude (hoặc bất kỳ coding agent nào) trả lời theo kiểu "người tiền sử" — bỏ từ đệm, lịch sự thừa, chỉ giữ thuật ngữ kỹ thuật chính xác. Kết quả: cắt trung bình ~65% token output (có case tới 87%), giữ nguyên độ chính xác kỹ thuật.

## Khi nào dùng
Dùng khi mày là người xài Claude Code/Claude nặng, hay bị giới hạn token/rate limit trong ngày, hoặc đơn giản là không cần Claude giải thích dài dòng — chỉ cần fix nhanh, review nhanh, commit message gọn. Không nên dùng khi cần văn phong chuẩn mực để gửi cho client hoặc viết nội dung public-facing (giọng "caveman" đọc hơi cộc, không hợp context đó).

## Nội dung skill / prompt
Đây không phải 1 đoạn prompt ngắn copy-paste được mà là 1 SKILL.md đầy đủ (kèm hook tự động cho Claude Code) do tác giả JuliusBrussee maintain. Lấy trực tiếp từ source thay vì copy lại ở đây (tránh lỗi thời khi tác giả update version):

```
npx skills@latest add JuliusBrussee/skills --skill caveman
```

Cơ chế tóm tắt: skill chỉ dạy agent "bỏ filler, giữ substance, dùng câu cụt" — không đụng tới reasoning/thinking token, chỉ ép phần *trả lời ra* (output) ngắn lại. Với Claude Code, có thêm 1 hook ghi file flag mỗi session để agent tự nói kiểu caveman từ tin nhắn đầu, không cần gọi lệnh mỗi lần.

## Setup từng bước
1. Cài 1 dòng lệnh (tự detect agent đang có trên máy — Claude Code, Cursor, Codex, Gemini, Windsurf, Cline, Copilot, 30+ agent khác):
   ```bash
   curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
   ```
   (Windows PowerShell: `irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex`)
2. Yêu cầu Node ≥18, cài xong khoảng 30 giây.
3. Trigger bằng gõ `/caveman` hoặc nói "talk like caveman". Tắt bằng "normal mode".
4. Chọn mức độ nén: `/caveman lite` (chỉ bỏ rào đón), `full` (default), `ultra` (tối giản tối đa), hoặc `wenyan` (phong cách Hán cổ — nén mạnh nhất, vẫn giữ ngôn ngữ gốc mày đang dùng — tiếng Việt vẫn ra tiếng Việt, chỉ nén văn phong).

## Ví dụ thực tế
**Bình thường (69 token):** Claude giải thích dài dòng lý do component React bị re-render — do object reference mới mỗi lần render, đề xuất dùng `useMemo`.

**Caveman mode (19 token):** Cùng nội dung, rút gọn thành 3 câu cụt: nêu nguyên nhân (ref mới mỗi render), nêu cơ chế (prop inline = ref mới = re-render), nêu cách fix (`useMemo`). Mất ~73% chữ, giữ 100% thông tin kỹ thuật.

Benchmark thật từ tác giả (10 task qua Claude API): trung bình giảm 65% token, dao động 22-87% tùy task. Task giải thích càng dài dòng (debug, setup phức tạp) thì giảm càng mạnh.

## Lưu ý / Lỗi thường gặp
- Caveman chỉ cắt **output token** (phần Claude trả lời), không đụng tới **thinking/reasoning token** — đừng kỳ vọng giảm cost ở phần suy nghĩ ngầm.
- Cài lần đầu bị lỗi → mở agent, gõ "Read CLAUDE.md and INSTALL.md, install caveman for me" để agent tự fix.
- Một số agent (Cursor, Windsurf, Cline, Copilot) cần cờ `--with-init` để always-on; mặc định chỉ trigger theo session khi gọi `/caveman`.
- Caveman có cả 1 ecosystem riêng (caveman-code — coding agent full, cavemem — memory, cavekit — spec-driven build) → dễ nhầm cái nào cài cái nào, đọc kỹ README trước khi cài thêm cái khác ngoài skill gốc.
- Có lệnh `/caveman-compress <file>` để nén luôn cả file CLAUDE.md/project notes — tiết kiệm token mỗi session load context, không chỉ tiết kiệm lúc trả lời.

## Đánh giá cá nhân
- Điểm mạnh: hiệu quả giảm token rõ ràng có số liệu benchmark thật (không chỉ quảng cáo), giữ nguyên ngôn ngữ gốc (Việt vẫn ra Việt), hỗ trợ 30+ agent, 74k+ star MIT free, có cả statusline hiện số token đã save.
- Điểm yếu: văn phong "cộc" có thể gây khó đọc nếu mày cần Claude giải thích kỹ cho người mới học; phải nhớ tắt "normal mode" khi cần văn phong chuẩn; ecosystem phụ (caveman-code, cavemem...) dễ gây rối nếu không đọc kỹ cái nào là cái nào.
- Có nên dùng không: 8/10 — cực hợp nếu mày code nhiều, ngại Claude dài dòng, đang lo hết quota trong ngày. Không hợp nếu mục đích chính là viết content/copy cần giọng văn mượt.

## Link
- Repo: https://github.com/JuliusBrussee/caveman
- Docs: https://caveman.so/ , https://github.com/JuliusBrussee/caveman/blob/main/INSTALL.md
- MCP registry: không, đây là skill/plugin cài qua npx skills hoặc /plugin marketplace
