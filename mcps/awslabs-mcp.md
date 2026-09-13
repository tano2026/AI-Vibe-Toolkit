# awslabs/mcp — MCP Server

## TL;DR
Bộ MCP server chính chủ AWS Labs, cho phép Claude/Cursor/Cline gọi thẳng dịch vụ AWS (EC2, S3, Lambda, CloudFormation, RDS...) bằng ngôn ngữ tự nhiên thay vì gõ AWS CLI.

## Tool này dùng để làm gì
Thay vì tự nhớ cú pháp AWS CLI hoặc mở AWS Console click từng bước, cắm MCP server này vào Claude Desktop/Code, gõ thẳng "tạo 1 EC2 instance loại t3.micro ở us-east-1" là agent tự gọi đúng API AWS làm giúp. Bộ này không phải 1 server duy nhất mà là 1 SUITE nhiều server con, mỗi server phụ trách 1 nhóm dịch vụ AWS (compute, networking, database, cost management, serverless...) — cắm server nào tuỳ nhu cầu, không phải cài hết 1 lần.

Dùng transport `stdio` là chính, không còn hỗ trợ Server-Sent Events (SSE) từ tháng 5/2025 — nếu thấy hướng dẫn cũ dùng SSE thì đã lỗi thời.

## Setup từng bước
1. Clone repo về xem danh sách server con có sẵn:
```bash
git clone https://github.com/awslabs/mcp.git
```
2. Chọn server cần (vd `core-mcp-server`, `cost-analysis-mcp-server`), thêm vào config Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "aws-core": {
      "command": "uvx",
      "args": ["awslabs.core-mcp-server@latest"],
      "env": { "AWS_PROFILE": "default", "AWS_REGION": "us-east-1" }
    }
  }
}
```
3. Đảm bảo đã cấu hình AWS credentials cục bộ (`aws configure`) — MCP server chạy local, dùng credentials có sẵn trên máy, không gửi ra ngoài

## Ví dụ thực tế
Nếu An Bình hoặc ABTRIP có hạ tầng chạy trên AWS (S3 lưu trữ, Lambda xử lý), gắn MCP này vào Claude Code để hỏi thẳng "S3 bucket nào đang tốn chi phí nhiều nhất tháng này" — agent gọi Cost Analysis MCP server trả lời trực tiếp, không cần mở AWS Console.

## Lưu ý / Lỗi thường gặp
- Đây là suite nhiều server, không phải 1 server đơn — đọc kỹ README để biết server nào phù hợp nhu cầu, cài hết tất cả sẽ dư thừa và chậm
- SSE đã bị gỡ bỏ khỏi mọi server bản mới — nếu copy config mẫu cũ dùng SSE sẽ lỗi, phải chuyển qua stdio hoặc Streamable HTTP
- Cần AWS credentials hợp lệ cấu hình sẵn trên máy chạy MCP server — không tự tạo credentials

## Đánh giá cá nhân
- **Điểm mạnh:** chính chủ AWS Labs nên bám sát API thật, cập nhật đều (release gần nhất theo lịch hàng tháng); phủ rất rộng dịch vụ AWS trong 1 nơi
- **Điểm yếu:** chỉ có giá trị nếu hạ tầng đang dùng AWS thật — nếu Tano Agency dùng VPS thường (không phải AWS) thì bộ này không áp dụng được; cấu hình nhiều server con hơi rối lúc đầu
- **Có nên dùng không:** 7/10 nếu có hạ tầng AWS thật, 0/10 nếu không dùng AWS — kiểm tra trước khi định cài

## Link
- Repo: https://github.com/awslabs/mcp
- MCP registry: có trên MCP Registry chính thức
