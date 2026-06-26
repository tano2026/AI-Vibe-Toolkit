# Page Agent — GitHub Repo

## TL;DR
JavaScript in-page GUI agent của Alibaba — control bất kỳ web interface nào bằng ngôn ngữ tự nhiên, chạy thẳng trong browser mà không cần backend. 19.8K stars, đang trending mạnh.

## Repo này dùng để làm gì
Khác với browser automation truyền thống (Playwright, Selenium phải chạy server riêng), Page Agent là một JavaScript library nhúng thẳng vào trang web. Mày có thể:
- Điều khiển UI bằng tiếng tự nhiên: "Click nút Submit", "Fill form với email này"
- Build chatbot điều khiển app của chính mình
- Tạo automation flows mà end user có thể dùng bằng ngôn ngữ tự nhiên
- Tích hợp MCP để AI agent control web app

Không cần cài thêm extension, không cần Puppeteer server — chỉ cần `<script>` tag.

## Setup từng bước
```bash
# Cài via npm
npm install page-agent
```

```javascript
// Import vào project
import { PageAgent } from 'page-agent';

// Init với LLM provider
const agent = new PageAgent({
  llm: {
    provider: 'anthropic',
    apiKey: process.env.ANTHROPIC_API_KEY,
    model: 'claude-sonnet-4-6'
  }
});

// Control trang bằng ngôn ngữ tự nhiên
await agent.act("Click vào nút 'Thêm vào giỏ hàng'");
await agent.act("Fill form email với test@example.com");
await agent.act("Scroll xuống và screenshot section pricing");

// Hoặc query UI
const result = await agent.query("Giá sản phẩm này là bao nhiêu?");
console.log(result); // "299,000 VNĐ"
```

**Tích hợp MCP (cho AI agent điều khiển):**
```json
{
  "mcpServers": {
    "page-agent": {
      "command": "npx",
      "args": ["page-agent-mcp"]
    }
  }
}
```

## Ví dụ thực tế
**Use case:** Auto-fill form đăng ký trên site khách hàng khi chạy campaign

**Code:**
```javascript
const agent = new PageAgent({ llm: { provider: 'anthropic', apiKey: '...' } });
await agent.navigate('https://landing-page.com/register');
await agent.act(`Fill form với:
  - Tên: Nguyễn Văn A
  - Email: test@gmail.com  
  - Phone: 0901234567`);
await agent.act("Click Submit và chờ confirmation");
```

Chạy 100 lần với data khác nhau → automation testing hoàn chỉnh.

## Lưu ý / Lỗi thường gặp
- Tốn token LLM mỗi action — với flow dài cần estimate cost trước
- Trang có captcha → agent bị block (vẫn chưa solve được)
- CORS có thể chặn nếu integrate sai domain
- Chỉ control được element visible — popup ẩn sau CSS sẽ bị miss

## Đánh giá cá nhân
- Điểm mạnh: In-page approach độc đáo; không cần server riêng; MCP integration cho AI agent; API đơn giản
- Điểm yếu: Tốn API token; captcha là blocker lớn; performance chậm hơn Playwright thuần
- Có nên dùng không: **8/10** — Rất phù hợp nếu mày build web app muốn add natural language control. Không thay thế Playwright cho scraping heavy-duty.

## Link
- Repo: https://github.com/alibaba/page-agent
- Docs: https://page-agent.github.io
- Topics: browser-automation, mcp, javascript, ai-agents
