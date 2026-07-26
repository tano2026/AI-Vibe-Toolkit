---
name: ai-chatbot-react-starter
description: >
  Build chatbot AI nhúng vào website (React + Express) — dùng OmniRoute thay vì gọi thẳng
  OpenAI API để tiết kiệm chi phí. Hợp cho FAQ bot nhúng landing page ABTRIP/Wonder Mart —
  KHÁC Chatwoot (đã có trong kho): cái này là AI-only widget, Chatwoot là nền tảng CSKH đầy
  đủ có ticketing + human handoff. Nguồn cảm hứng: carousel TikTok @aicareersuite.
---

# AI Chatbot React Starter (điều chỉnh cho Tano Agency)

## TL;DR
Kiến trúc: React (frontend widget) → Express (backend, giữ API key an toàn) → **OmniRoute**
(thay vì OpenAI trực tiếp) → trả JSON → React cập nhật hội thoại. Đúng chuẩn kỹ thuật, đã kiểm
tra kỹ — không có lỗi trong nguồn gốc. Bài viết gốc dùng OpenAI thẳng, bản này đổi sang
OmniRoute để route qua model rẻ (DeepSeek V3/Gemini Flash) thay vì luôn trả phí OpenAI.

## Khi nào dùng
- Cần 1 chat widget AI đơn giản nhúng vào landing page (trả lời FAQ Fast Track, hỏi giá Wonder
  Mart) — KHÔNG cần ticketing/human handoff.
- Muốn tự chủ hoàn toàn UI (không bị giới hạn theo giao diện Chatwoot).
- KHÔNG dùng khi cần: hàng đợi hỗ trợ, nhiều agent người thật xử lý cùng lúc, lịch sử ticket đa
  kênh (Zalo/Facebook/email) — những việc đó nên dùng Chatwoot (`repos/chatwoot.md`).

## Nội dung skill / hướng dẫn build

### Bước 1 — Setup project (React + Vite)
```bash
npx create-vite@latest ai-chatbot -- --template react
cd ai-chatbot
npm install
npm install axios
```
Cấu trúc: `src/components/ChatBot.jsx`, `App.jsx`, `App.css`, `main.jsx`.

### Bước 2 — Build Chat UI (React)
```jsx
const [message, setMessage] = useState("");
const [messages, setMessages] = useState([]);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);
```
UI cần đủ: message list (render bằng `.map()`), input box (controlled input), send button,
loading state, error fallback. Input rỗng phải validate trước khi gửi.

### Bước 3 — Backend (Express) — ĐIỀU CHỈNH dùng OmniRoute
```bash
npm install express cors dotenv
```
```javascript
// server.js
require("dotenv").config();
const express = require("express");
const cors = require("cors");
const app = express();
app.use(cors());
app.use(express.json());

app.post("/chat", async (req, res) => {
  try {
    const { message } = req.body;
    if (!message?.trim()) return res.status(400).json({ error: "Tin nhắn rỗng" });

    // Gọi OmniRoute thay vì OpenAI trực tiếp — route sang model rẻ, không luôn trả phí cao
    const response = await fetch(process.env.OMNIROUTE_URL + "/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message,
        task_type: "cheap",  // FAQ đơn giản không cần model đắt
        system: "Bạn là trợ lý AI của [tên brand]. Chỉ trả lời trong phạm vi dịch vụ công ty.",
      }),
    });
    const data = await response.json();
    res.json({ reply: data.reply });
  } catch (err) {
    res.status(500).json({ error: "Có lỗi xảy ra, thử lại sau." });
  }
});

app.listen(5000, () => console.log("Chatbot backend chạy port 5000"));
```
`.env`:
```
OMNIROUTE_URL=http://localhost:PORT_OMNIROUTE
```
**Bắt buộc thêm `.env` vào `.gitignore`** — không bao giờ commit key/URL nội bộ lên git.

### Bước 4 — Nối frontend-backend
```javascript
const res = await axios.post("http://localhost:5000/chat", { message });
```
Luồng: User gõ → React POST → Express nhận `/chat` → OmniRoute route model → trả JSON → React
cập nhật hội thoại.

### Bước 5 — Nâng cấp lên production-ready
- Chat history (lưu lại session), typing animation, markdown support, streaming response
- Dark/light mode
- Trước khi deploy: chạy qua **`skills/kiem-tra-bao-mat-truoc-deploy.md`** — đặc biệt mục #1
  (secret trong code) và #6 (nếu sau này có tính năng thanh toán qua chat)
- Rate limiting — chống spam request tốn token OmniRoute

## Ví dụ thực tế
Nhúng chatbot FAQ vào `fasttracknoibai.com` trả lời câu hỏi thường gặp (giờ hoạt động, giá dịch
vụ, quy trình đặt) — dùng `task_type: "cheap"` (DeepSeek V3) cho câu hỏi đơn giản, không cần
route Claude Sonnet đắt tiền cho mỗi câu FAQ.

## Lưu ý / Lỗi thường gặp
- Đây là chatbot AI THUẦN — không có bộ nhớ về khách hàng cụ thể, không biết đơn hàng của ai
  (khác Chatwoot có CRM khách hàng đi kèm).
- System prompt PHẢI giới hạn phạm vi trả lời (chỉ nói về dịch vụ công ty) — tránh chatbot trả
  lời lạc đề hoặc bịa thông tin không có trong phạm vi kinh doanh.
- Nếu cần chatbot biết context thật (giá vé hiện tại, tình trạng đơn hàng) — cần nối thêm
  database/API thật vào backend, bản cơ bản này chưa có.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc chuẩn, đúng kỹ thuật, dễ tuỳ biến UI hoàn toàn theo brand (khác Chatwoot
  bị giới hạn theo giao diện có sẵn); đổi sang OmniRoute tiết kiệm chi phí đáng kể so với bản
  gốc gọi thẳng OpenAI.
- Điểm yếu: phải tự xây mọi thứ từ đầu (ticketing, human handoff, đa kênh) nếu sau này cần —
  Chatwoot có sẵn những thứ đó.
- Có nên dùng không: 7.5/10 cho use case cụ thể "FAQ bot đơn giản nhúng landing page" — không
  thay thế Chatwoot cho nhu cầu CSKH đầy đủ.

## Link
- Nguồn cảm hứng: TikTok @aicareersuite — "Build an AI Chatbot in React" (7-slide guide)
- So sánh: `repos/chatwoot.md` (nền tảng CSKH đầy đủ, khác use case)
