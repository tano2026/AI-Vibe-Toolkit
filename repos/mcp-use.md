# mcp-use — GitHub Repo

## TL;DR
Thư viện Python (kèm bản TypeScript) gói gọn "full stack MCP" — vừa làm MCP Client (nối tới MCP server có sẵn), vừa build MCP Agent (agent tự dùng tool qua nhiều bước), vừa tạo/test/deploy MCP Server, tất cả trong 1 package. Của Pietro Zullo, thuộc tổ chức `mcp-use`.

## Repo này dùng để làm gì
Bình thường muốn nối 1 LLM với nhiều MCP server cùng lúc phải tự viết code quản lý connection, xử lý reconnect, list tool. mcp-use gói sẵn: `MCPClient` để nối trực tiếp và gọi tool theo cách lập trình (không cần LLM), `MCPAgent` để dựng agent LLM tự suy luận và chọn tool qua nhiều bước (có adapter sẵn cho LangChain), và phần server để tự tạo/test MCP server riêng.

## Setup từng bước
1. Cài:
   ```bash
   pip install mcp-use
   ```
2. Dùng MCP Client (gọi tool trực tiếp, không qua LLM):
   ```python
   from mcp_use import MCPClient

   client = MCPClient.from_config_file("mcp_config.json")  # config nhiều MCP server cùng lúc
   tools = await client.list_tools()
   ```
3. Dùng MCP Agent (để LLM tự suy luận + gọi tool):
   ```python
   from mcp_use import MCPAgent

   agent = MCPAgent(
       llm=your_llm,        # model LangChain bất kỳ (OpenAI, Anthropic...)
       client=client,
       verbose=True,        # chỉ hiện bước suy luận của agent, không log rác
   )
   result = await agent.run("Tìm chuyến bay rẻ nhất tuần sau")
   ```
4. Yêu cầu: Python 3.11+, đã có implementation MCP thật (vd Playwright MCP) và thư viện model tương ứng (OpenAI/Anthropic...) cài kèm.

## Ví dụ thực tế
Cho Hermes: dùng `MCPClient` nối tới nhiều MCP server cùng lúc (vd 1 MCP tra giá vé, 1 MCP đọc email ABTRIP) qua 1 file config duy nhất, rồi bọc bằng `MCPAgent` để agent tự quyết định gọi tool nào theo yêu cầu tiếng thường, không cần Hermes tự viết logic routing giữa các MCP server.

## Lưu ý / Lỗi thường gặp
- Đừng nhầm với `mcp` (Python SDK chính thức của Model Context Protocol, `modelcontextprotocol/python-sdk`) — `mcp-use` là thư viện cộng đồng xây trên nền đó, thêm lớp Agent + quản lý nhiều server, không phải SDK gốc.
- `verbose=True` chỉ hiện log bước suy luận của agent, không phải log chi tiết toàn hệ thống — đọc kỹ docs nếu cần debug sâu hơn tầng dưới (connection, transport).
- Cần model LangChain tương thích để dùng `MCPAgent` — nếu chỉ cần gọi tool trực tiếp không qua LLM, dùng `MCPClient` là đủ, không cần cấu hình LLM.
- Là dự án cộng đồng còn khá mới, tài liệu tập trung ở repo chính (`mcp-use/mcp-use`) — kiểm tra lại API có đổi không trước khi copy code mẫu từ bài viết cũ.

## Đánh giá cá nhân
- **Điểm mạnh:** Gói đủ 3 vai (Client/Agent/Server) trong 1 thư viện, tiết kiệm thời gian so với tự ghép `mcp` SDK gốc + LangChain adapter bằng tay. Config nhiều MCP server qua 1 file duy nhất khá tiện khi hệ thống có nhiều nguồn dữ liệu.
- **Điểm yếu:** Là layer cộng đồng trên nền MCP SDK gốc, không phải chính chủ Anthropic — độ ổn định/tốc độ cập nhật phụ thuộc 1 maintainer chính. Cần hiểu rõ MCP cơ bản trước, không hợp để học MCP từ số 0.
- **Có nên dùng không:** 7/10 cho ai đã quen MCP và cần build agent nối nhiều MCP server nhanh bằng Python — nếu chỉ cần 1 MCP client đơn giản, dùng `mcp` SDK gốc trực tiếp có thể gọn hơn.

## Link
- Repo: https://github.com/mcp-use/mcp-use
- Docs/Demo: https://pypi.org/project/mcp-use/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Cài: pip install mcp-use
from mcp_use import MCPClient, MCPAgent

client = MCPClient.from_config_file("mcp_config.json")
agent = MCPAgent(llm=your_llm, client=client)
result = await agent.run("Tổng hợp giá vé rẻ nhất tuần này")
```
> ⚠️ File `mcp_config.json` cần khai đúng địa chỉ/transport của từng MCP server Hermes muốn nối — sai transport (stdio vs HTTP) là lỗi hay gặp nhất.

### OpenClaw
Không áp dụng trực tiếp (thư viện Python) — nếu OpenClaw (Node.js) cần logic tương tự, dùng SDK JS song song trong hệ sinh thái `mcp-use`, hoặc gọi qua 1 API endpoint Python nhỏ bọc quanh `MCPAgent`.

### Antigravity
```bash
# Cài môi trường cho service Python dùng mcp-use trên VPS
python3 -m venv .venv && source .venv/bin/activate
pip install mcp-use
```
> ⚠️ Đảm bảo mọi MCP server trong `mcp_config.json` đã chạy sẵn (hoặc mcp-use tự khởi động được qua stdio) trước khi service Python start, không thì `list_tools()` trả về rỗng mà không báo lỗi rõ ràng.
