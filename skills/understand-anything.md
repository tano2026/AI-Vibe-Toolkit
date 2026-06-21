# Understand Anything — Biến Codebase Thành Knowledge Graph Tương Tác

## TL;DR
Tool 64K+ stars biến bất kỳ codebase, docs hay knowledge base nào thành knowledge graph tương tác — mày có thể explore, tìm kiếm và hỏi trực tiếp. Chạy được với Claude Code, Cursor, Copilot, Gemini CLI.

## Tool này dùng để làm gì
Thay vì đọc code từng file một khi join project mới (hoặc debug codebase khổng lồ), Understand Anything phân tích toàn bộ project bằng multi-agent pipeline rồi tạo ra:

- **Knowledge graph tương tác** — click vào node để xem relationship giữa các module
- **Dashboard có thể search** — tìm function, class, dependency bằng ngôn ngữ tự nhiên
- **Q&A trực tiếp** — hỏi "cái này connect với cái gì?" và nhận câu trả lời có context

Dùng được với: Claude Code, Codex, Cursor, Copilot, Gemini CLI.

## Setup từng bước
```bash
# Clone repo
git clone https://github.com/Egonex-AI/Understand-Anything
cd Understand-Anything

# Install dependencies
pip install -r requirements.txt

# Chạy với codebase của mày
python main.py --path /path/to/your/project

# Mở dashboard
# Tự động mở browser tại localhost:xxxx
```

Với Claude Code:
```bash
# Add như một MCP hoặc skill trong project
# Theo hướng dẫn trong CLAUDE.md của repo
```

## Ví dụ thực tế
**Tình huống:** Join project React 50K dòng code, cần hiểu architecture trong 1 giờ

1. Chạy `python main.py --path ./my-react-project`
2. Tool phân tích tất cả imports, exports, function calls
3. Mở dashboard → thấy ngay: component nào gọi component nào, state flow như thế nào
4. Hỏi: "AuthContext được dùng ở đâu?" → ra ngay list + diagram

Thay vì mất 2 ngày đọc code, mất 2 giờ.

## Lưu ý / Lỗi thường gặp
- Project lớn (>100K dòng) cần thời gian phân tích lâu hơn, có thể 10-15 phút
- Graph đẹp hơn với code có structure rõ ràng (tệ hơn với spaghetti code)
- Cần Python + Node.js environment
- "Graphs that teach > graphs that impress" — focus vào hiểu, không phải visual

## Đánh giá cá nhân
- **Điểm mạnh:** Game changer khi onboard project mới hoặc debug legacy code. Graph tương tác thật sự hữu ích chứ không chỉ đẹp
- **Điểm yếu:** Setup hơi nhiều bước, một số ngôn ngữ support chưa tốt bằng Python/JS
- **Có nên dùng không:** 8/10 — nếu mày thường xuyên đụng codebase lạ hoặc large codebase, đây là must-have

## Link
- Repo: https://github.com/Egonex-AI/Understand-Anything
- Trang chủ: https://egonex.ai
