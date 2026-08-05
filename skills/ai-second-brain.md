# AI Second Brain — Prompt Template / System Prompt

## TL;DR
Skill biến lịch sử trò chuyện với Claude/ChatGPT thành 1 wiki cá nhân có tổ chức, dạng đồ thị tri thức liên kết (theo pattern LLM Wiki của Andrej Karpathy) — lưu dưới Markdown thuần trong Obsidian, không khoá vào 1 nền tảng riêng.

## Khi nào dùng
- Sau nhiều tháng làm việc với Claude, có hàng trăm cuộc hội thoại chứa quyết định/kiến thức quan trọng nhưng không tìm lại được — dùng skill này để gom thành wiki tra cứu được.
- Cần 1 "bộ nhớ ngoài" bền vững hơn memory system của Claude (memory system có recency bias, không giữ toàn bộ lịch sử) — second brain lưu file thật, tự quản lý được.
- Không dùng khi: chỉ cần nhớ vài fact đơn giản — memory system built-in của Claude đã đủ, không cần thêm hệ thống riêng.

## Nội dung skill / prompt
Không phải 1 prompt đơn — là 1 Claude Code skill (`.claude/skills/ai-second-brain/`) hoạt động theo cơ chế: nhận nguồn bất kỳ (đoạn chat, note, research) → Claude đọc, phân loại, liên kết vào đồ thị tri thức hiện có → ghi ra file Markdown trong Obsidian vault, có wikilink nối các khái niệm liên quan.

## Setup từng bước
1. Cần Obsidian đã cài (vault local) + Claude Code.
2. Clone/cài skill: `git clone https://github.com/charlie947/ai-second-brain` (hoặc bản tương tự theo Karpathy-pattern trên GitHub topic `ai-second-brain`).
3. Trỏ skill vào đường dẫn Obsidian vault đang dùng.
4. Feed nguồn định kỳ: dán đoạn hội thoại quan trọng, note họp, hoặc kết quả research vào Claude Code, gọi skill để tự phân loại và ghi vào vault.
5. Vault tự lớn dần theo thời gian dùng — không cần cấu trúc trước, Claude tự tổ chức link khi thêm nội dung mới.

## Ví dụ thực tế
Sau vài tháng research tool cho kho AI-Vibe-Toolkit, feed lại các quyết định kiến trúc quan trọng (vd lý do chọn OmniRoute thay vì gọi trực tiếp từng LLM provider) vào second brain — sau này hỏi lại "tại sao chọn OmniRoute" ra ngay câu trả lời có link tới các ghi chú liên quan, thay vì phải lục lại conversation cũ hoặc dựa vào trí nhớ.

## Lưu ý / Lỗi thường gặp
- **Chỉ chạy trong Claude Code, không dùng được trực tiếp trong claude.ai web/app** — cần môi trường có filesystem thật (Obsidian vault local), không hợp nếu Tano chủ yếu làm việc qua Claude web/mobile.
- Trùng chức năng một phần với memory system built-in của Claude — cần xác định rõ ranh giới: memory system nhớ theo phiên tự động, second brain là chủ động feed + có file thật kiểm soát được.
- Vault càng lớn, càng cần dọn dẹp định kỳ — không tự làm sạch link chết hay note trùng lặp nếu không chủ động maintain.

## Đánh giá cá nhân
- Điểm mạnh: dữ liệu là file Markdown thật, tự sở hữu hoàn toàn, không phụ thuộc hệ thống memory của bất kỳ AI provider nào — khớp nguyên tắc tự chủ hạ tầng Tano đang theo.
- Điểm yếu: cần môi trường Claude Code + Obsidian, không dùng được nếu chỉ thao tác qua claude.ai; cần công feed liên tục để vault có giá trị, không tự động hoá hoàn toàn.
- Có nên dùng không: 6/10 — đáng thử làm bổ sung cho CHANGELOG-DECISIONS.md hiện có trong `agents/company/`, nhưng không thay thế được git-based tracking đang dùng cho kho chính.

## Link
- Repo: https://github.com/charlie947/ai-second-brain
- Chủ đề liên quan: https://github.com/topics/ai-second-brain
