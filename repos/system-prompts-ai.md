# system-prompts-and-models-of-ai-tools — GitHub Repo

## TL;DR
Kho system prompt bị leak/công bố của 25+ công cụ AI coding thật (Cursor, Windsurf, Devin, Claude Code, v0, Replit Agent, Lovable...) — đọc để học cách các sản phẩm production thật viết system prompt, áp dụng khi tự viết prompt cho agent của Tano Agency.

## Repo này dùng để làm gì
Đây KHÔNG phải tool cài đặt — là thư viện tham khảo thuần text. Tác giả x1xhlol thu thập system prompt của các AI coding tool nổi tiếng (qua leak hoặc công bố chính thức), gom lại theo từng thư mục/tool. 142k+ sao, GPL-3.0.

Dùng để: xem cách Cursor/Devin/v0 định nghĩa tool, ràng buộc hành vi (khi nào hỏi lại user, khi nào tự chạy lệnh), cấu trúc guardrail, cách handle context dài — rồi áp dụng ý tưởng đó vào việc viết `system-prompt.md` cho các agent trong `agents/` của kho (research-analytics-pro, trum-san-bay...).

## Setup từng bước
1. Clone về máy (không cần cài gì, chỉ đọc):
```bash
git clone https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools.git
```
2. Mở thư mục tool muốn tham khảo, vd `Cursor Prompts/` hoặc `Devin AI/`
3. Đọc, rút ý tưởng cấu trúc (không copy nguyên văn — mỗi tool có style riêng, phần lớn nội dung có bản quyền của công ty gốc)

## Ví dụ thực tế
Viết `system-prompt.md` cho agent `sales-ceo` trong kho: mở `Devin AI/prompt.txt` xem Devin xử lý phần "khi nào tự quyết, khi nào hỏi lại user" ra sao, rồi viết lại phần tương tự bằng giọng riêng cho sales-ceo — không copy-paste, chỉ học cấu trúc.

## Lưu ý / Lỗi thường gặp
- Đây là nội dung leak/thu thập — một số phần có thể đã lỗi thời nếu tool gốc đổi prompt sau ngày cập nhật gần nhất (repo cập nhật khá thường xuyên, check ngày trong README)
- Không nên copy nguyên văn prompt của công ty khác vào sản phẩm thương mại — dùng để học pattern, không phải để tái sử dụng trực tiếp
- Repo dạng GPL-3.0 — cân nhắc điều khoản license nếu định dùng lại nội dung theo cách nào đó xa hơn "đọc tham khảo"

## Đánh giá cá nhân
- Điểm mạnh: Nguồn tham khảo hiếm — system prompt production thật của hàng chục sản phẩm tỷ đô, khó tìm ở đâu khác tập trung đầy đủ vậy
- Điểm yếu: Không phải tool dùng trực tiếp được, chỉ đọc — không có Agent Integration kiểu API/code. Giá trị phụ thuộc hoàn toàn vào việc mày có chịu đọc kỹ hay không
- Có nên dùng không: 7/10 — hữu ích khi bí ý tưởng viết system-prompt cho agent mới, không phải thứ dùng hàng ngày

## Link
- Repo: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools

---

## 🤖 Agent Integration

Không áp dụng — đây là tài liệu tham khảo tĩnh (text), không phải service/API. Cách "tích hợp"
duy nhất là clone về và trỏ Claude Code đọc khi cần, qua `agents/CLAUDE-CODE-BRIDGE.md`
(thêm dòng `@` trỏ vào thư mục clone trong CLAUDE.md nếu muốn Claude Code tự biết nguồn này tồn tại).
