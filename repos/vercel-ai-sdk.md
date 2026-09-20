# vercel/ai (AI SDK) — GitHub Repo

## TL;DR
AI SDK TypeScript từ đội Next.js — ship streaming và tool calls chỉ với vài dòng code. 26,5k sao, 5,0k fork.

## Repo này dùng để làm gì
Bộ SDK thống nhất để gọi nhiều model AI khác nhau (OpenAI, Claude, Gemini...) ngay trong app React/Next.js — không phải viết riêng code cho từng provider. Hỗ trợ sẵn streaming response và tool/function calling.

## Setup từng bước
1. Cài: `npm install ai @ai-sdk/anthropic`
2. Code cơ bản (Next.js API route):
```typescript
import { anthropic } from '@ai-sdk/anthropic';
import { streamText } from 'ai';

const result = streamText({
  model: anthropic('claude-sonnet-4-6'),
  prompt: 'Câu hỏi ở đây',
});
```
3. Frontend dùng hook `useChat` để tự động xử lý streaming UI

## Ví dụ thực tế
Zalo Mini App bán vé ABTRIP dùng React — nếu muốn thêm chatbot hỏi đáp ngay trong app (vd "Fast Track khác gì thường"), dùng vercel/ai để gọi Claude API kèm streaming response mượt trong giao diện React, không phải tự viết code xử lý stream từ đầu.

## Lưu ý / Lỗi thường gặp
- Chỉ hợp môi trường JavaScript/TypeScript (React/Next.js/Node) — không dùng được cho Python (Hermes)
- Đổi provider (OpenAI sang Claude) chỉ cần đổi import, không cần viết lại logic — đây là lợi thế chính
- Cần API key riêng cho từng provider dùng

## Đánh giá cá nhân
- Điểm mạnh: từ đội Next.js nên tối ưu tốt cho hệ sinh thái React, streaming/tool-calling dễ dùng, docs tốt
- Điểm yếu: chỉ hợp JS/TS, không dùng được cho Hermes (Python) hay Antigravity script
- Có nên dùng: 8/10 — đúng công cụ nếu build thêm tính năng AI vào Zalo Mini App hoặc bất kỳ app React/Next.js nào

## Link
- Repo: https://github.com/vercel/ai
