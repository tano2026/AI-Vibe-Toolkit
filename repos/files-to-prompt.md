# files-to-prompt — GitHub Repo

## TL;DR
Gộp nguyên 1 codebase thành 1 prompt duy nhất, chỉ bằng 1 lệnh. 2,8k sao, tool nhỏ nhưng thiết thực.

## Repo này dùng để làm gì
Duyệt cả thư mục project, nối toàn bộ file lại thành 1 prompt để đưa cho LLM — hữu ích khi cần hỏi Claude/GPT về toàn bộ codebase mà không muốn copy-paste tay từng file.

## Setup từng bước
1. Cài: `pip install files-to-prompt`
2. Dùng ngay:
```bash
files-to-prompt ./my-project > prompt.txt
files-to-prompt ./my-project -e py -e js  # chỉ lấy file .py và .js
```
3. Copy nội dung `prompt.txt` dán vào Claude/ChatGPT, hoặc pipe thẳng

## Ví dụ thực tế
Cần review toàn bộ code `jev_bridge.py` + config liên quan trước khi giao Antigravity deploy — thay vì mở từng file copy tay, chạy `files-to-prompt ./jev-bridge -e py -e env` ra 1 file gộp, dán thẳng cho Claude review tổng thể 1 lần.

## Lưu ý / Lỗi thường gặp
- Codebase lớn sẽ vượt context window model — cần lọc bằng flag `-e` (extension) hoặc `--ignore` để tránh gộp file không cần thiết
- Không tự động lọc file nhạy cảm (`.env` có key thật) — cần tự loại trừ, không để lộ secret khi paste cho AI
- Là tool nhỏ, không có tính năng phức tạp — đúng 1 việc, làm tốt việc đó

## Đánh giá cá nhân
- Điểm mạnh: đơn giản, nhanh, giải quyết đúng vấn đề "phải copy tay nhiều file" khi hỏi AI về code
- Điểm yếu: không lọc thông minh, dễ vượt context nếu không cẩn thận filter
- Có nên dùng: 7/10 — tiện cho review code nhanh, nhớ tự loại file chứa secret trước khi dùng

## Link
- Repo: https://github.com/simonw/files-to-prompt
