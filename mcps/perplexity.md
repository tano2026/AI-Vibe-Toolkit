# Perplexity — MCP Server

## TL;DR
MCP chính thức của Perplexity — cho Claude gọi công cụ search real-time của Perplexity (khác với web_search built-in của Claude) khi cần kết quả có phong cách tổng hợp/trích dẫn kiểu Perplexity, hoặc khi build agent ngoài Claude cần khả năng search tương đương.

## Tool này dùng để làm gì
Perplexity nổi tiếng về search có trích dẫn nguồn rõ ràng, tối ưu cho câu hỏi dạng nghiên cứu. MCP này expose khả năng đó ra ngoài Perplexity.ai, cho agent/Claude gọi trực tiếp thay vì phải tự động web_search rồi tổng hợp.

## Setup từng bước
1. Cần API key Perplexity (Perplexity API, riêng biệt với gói Pro consumer).
2. Với Claude: nếu đã có web_search built-in, MCP Perplexity chủ yếu hữu ích khi build agent ngoài (Hermes) cần khả năng search riêng, không phụ thuộc Claude's web_search.
3. Cấu hình MCP server (nhiều bản community trên GitHub, ví dụ `perplexity-mcp` dạng Python/Node) với `PERPLEXITY_API_KEY` trong biến môi trường.
4. Test bằng 1 câu hỏi cần thông tin mới để so sánh chất lượng trích dẫn với web_search sẵn có.

## Ví dụ thực tế
Cho Hermes khi cần research nhanh 1 tool mới trước khi viết entry vào kho (thay vì chỉ dựa vào GitHub API, dùng thêm Perplexity để có góc nhìn tổng hợp đa nguồn với trích dẫn rõ ràng) — dù hiện tại workflow đã dùng web search sẵn có trong Claude, có thể không cần thêm lớp này trừ khi Hermes chạy độc lập ngoài Claude session.

## Lưu ý / Lỗi thường gặp
- **Trùng lặp chức năng với web_search có sẵn trong Claude** — nếu đang dùng Claude trực tiếp (như trong session này), thêm Perplexity MCP không mang lại giá trị mới rõ ràng, chỉ hữu ích khi build agent độc lập ngoài Claude.
- Cần API key trả phí riêng — thêm chi phí vận hành nếu chỉ dùng thay thế cho tính năng đã có sẵn miễn phí.
- Chất lượng trích dẫn tốt nhưng độ trễ có thể cao hơn search trực tiếp tuỳ tải hệ thống.

## Đánh giá cá nhân
- Điểm mạnh: chất lượng trích dẫn nguồn tốt, hữu ích khi build agent search độc lập ngoài hệ sinh thái Claude.
- Điểm yếu: với Tano hiện tại (Hermes routing qua OmniRoute, Claude session đã có web_search), giá trị gia tăng thấp — dễ thành chi phí trùng lặp không cần thiết.
- Có nên dùng không: 4/10 cho tình trạng hiện tại của Tano — không ưu tiên trừ khi Hermes cần chạy search độc lập hoàn toàn ngoài phiên Claude.

## Link
- Docs: https://docs.perplexity.ai (phần API/MCP)
- MCP registry: có trong danh mục connector Claude chính thức
