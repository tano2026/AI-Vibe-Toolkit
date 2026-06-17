# Claude-Mem — Prompt Template / System Prompt

## TL;DR
Plugin cho Claude Code tạo "trí nhớ dài hạn" — tự động ghi lại những gì Claude làm trong session (tool dùng, quyết định, kết quả), nén lại bằng AI, lưu vào database local, rồi tự nạp lại đúng phần context liên quan vào session mới. Mở Claude Code lên là Claude "nhớ" luôn dự án hôm trước, không cần giải thích lại từ đầu.

## Khi nào dùng
Dùng khi mày làm 1 project dài hơi qua nhiều session (debug kéo dài nhiều ngày, refactor lớn, dự án doanh nghiệp có nhiều ngữ cảnh riêng) và chán cảnh mỗi lần mở Claude Code mới phải copy-paste lại bối cảnh. Không cần dùng cho task ngắn 1 lần là xong — overhead setup không đáng.

## Nội dung skill / prompt
Đây là 1 plugin có hook + worker service, không phải 1 đoạn system prompt đơn giản. Lấy nguyên bộ trực tiếp từ source để luôn đúng version mới nhất:

```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

Cơ chế tóm tắt (không quote nguyên văn, diễn giải lại):
- 5 lifecycle hook (SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd) tự bắt mọi hành động Claude làm trong session.
- 1 worker service chạy local (port 37777) quản lý bằng Bun, có web viewer xem trực tiếp những gì đã ghi nhớ.
- Lưu vào SQLite (session, observation, summary) + Chroma vector DB để search ngữ nghĩa kết hợp keyword.
- Skill riêng tên `mem-search` cho phép Claude tự query lại trí nhớ cũ bằng ngôn ngữ tự nhiên, theo 3 lớp tăng dần độ chi tiết để tiết kiệm token: tìm index gọn trước → xem context xung quanh → mới lấy full detail cho đúng ID cần.

## Setup từng bước
1. Cách nhanh nhất — 1 lệnh duy nhất (yêu cầu Node ≥20):
   ```bash
   npx claude-mem install
   ```
2. Hoặc cài qua plugin marketplace ngay trong Claude Code (lệnh ở phần "Nội dung" trên).
3. Restart Claude Code — từ session sau, context cũ tự xuất hiện, không cần làm gì thêm.
4. Muốn dùng cho Gemini CLI hay OpenCode: thêm cờ `--ide gemini-cli` hoặc `--ide opencode` vào lệnh install.
5. Xem trực tiếp những gì đã lưu: mở `http://localhost:37777` trên browser sau khi worker chạy.

## Ví dụ thực tế
Tình huống: ngày 1 mày debug 1 bug auth middleware với Claude Code, xong việc đóng máy. Ngày 2 mở Claude Code lại trong cùng project — không cần nói lại "hôm qua tao fix bug gì", Claude tự biết vì observation đã được nén và nạp lại vào context session mới. Muốn tìm cụ thể lại quyết định nào đó → hỏi thẳng bằng câu tự nhiên kiểu "lúc trước tao fix bug auth thế nào", Claude dùng mem-search tự tra database trả lời, không cần mày tự lục lại log.

## Lưu ý / Lỗi thường gặp
- `npm install -g claude-mem` **chỉ cài SDK/library**, KHÔNG đăng ký hook và worker — bắt buộc phải dùng `npx claude-mem install` hoặc lệnh `/plugin` ở trên, nếu không sẽ tưởng đã cài mà không chạy.
- Cần thêm Bun (runtime) và uv (Python package manager cho vector search) — plugin tự cài nếu máy chưa có, nhưng lần đầu setup sẽ lâu hơn caveman/humanizer khá nhiều.
- Đổi mode/ngôn ngữ ghi nhớ (English/Chinese/Japanese...) qua file `~/.claude-mem/settings.json`, đổi xong phải restart Claude Code mới áp dụng.
- ⚠️ Lưu ý riêng: README chính thức có mục nói về 1 token crypto tên "CMEM" — token này do bên thứ 3 tạo, tác giả chỉ "công khai đồng tình" chứ không phải tự phát hành để kiếm tiền từ plugin. Plugin bản thân hoàn toàn free, không cần mua token gì để dùng — coi chừng nhầm lẫn hoặc bị dẫn dụ mua token nếu thấy quảng cáo CMEM ở đâu đó.

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng pain point thật (Claude quên hết giữa các session), 83k+ star, support nhiều agent không chỉ riêng Claude Code (Gemini CLI, OpenCode, Codex...), có web UI xem trực quan, pattern search 3 lớp tiết kiệm token rất hợp lý.
- Điểm yếu: setup nặng hơn nhiều so với 1 skill thuần text (cần Bun, uv, 1 worker service chạy ngầm chiếm port riêng) — không hợp nếu máy yếu hoặc chỉ cần thử nhanh; phần "CMEM token" trong README dễ gây hiểu lầm/cảnh giác không cần thiết với người mới.
- Có nên dùng không: 8/10 cho ai code dự án dài hơi nhiều ngày liên tục với Claude Code. Nếu chỉ code task ngắn lặt vặt thì không cần, 6/10 vì overhead không đáng.

## Link
- Repo: https://github.com/thedotmack/claude-mem
- Docs: https://docs.claude-mem.ai/
- MCP registry: không trực tiếp, nhưng có cung cấp 4 MCP tool riêng (search, timeline, get_observations) để các agent khác query trí nhớ
