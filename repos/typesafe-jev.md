# TypeSafe Jev — GitHub Repo

## TL;DR
Model AI rất mới (ra mắt gần đây, TypeSafe AI tự gọi là "System One Model" đầu tiên) — không sinh văn bản như LLM thường, mà nhận state (text/JSON) + câu hỏi đã định kiểu sẵn, trả về quyết định có cấu trúc (Choice/Score/Boolean) kèm xác suất/độ tin cậy. TypeSafe tự công bố nhanh hơn LLM tới 193.6 lần và rẻ hơn 444.6 lần cho việc ra quyết định nhỏ.

## Repo này dùng để làm gì
Khác hẳn ChatGPT/Claude — Jev không "trò chuyện", nó trả lời đúng loại câu hỏi đã khai trước: `Choice` (chọn 1 trong nhiều option), `Score` (chấm điểm theo thang có sẵn), `Noul`/Boolean (xác suất đúng/sai). Hợp cho những chỗ code cần "if hiểu ngữ nghĩa" mà không cần cả 1 LLM tốn token: chọn tool/subagent tiếp theo trong vòng lặp agent, quyết định tiếp tục/dừng/hỏi lại, chấm độ ưu tiên/rủi ro trước khi hành động, kiểm tra output của model khác (guardrail).

## Setup từng bước
1. Cài SDK chính chủ:
   ```bash
   pip install typesafe-sdk          # Python
   # hoặc
   npm install @typesafe-ai/sdk      # JavaScript/TypeScript
   ```
2. Set API key (hiện có waitlist truy cập sớm, cần đăng ký):
   ```bash
   export TYPESAFE_API_KEY="your-key"
   ```
3. Gọi 1 quyết định kiểu Boolean (ví dụ qua AI SDK của Vercel, cách phổ biến nhất hiện có):
   ```ts
   import { experimental_evaluate as evaluate } from 'ai';

   const result = await evaluate({
     model: 'typesafe-ai/jev',
     state: 'Nhân viên hỗ trợ đã hoàn tiền đầy đủ cho khách.',
     questions: {
       refunded: { type: 'boolean', instructions: 'Có phải đã hoàn tiền không?' },
     },
   });
   console.log(result.answers.refunded);   // trả về xác suất, không phải văn bản
   ```
4. Không muốn chờ waitlist — gọi qua Vercel AI Gateway (đã bật sẵn `typesafe-ai/jev`, không cần chờ TypeSafe cấp quyền riêng) hoặc qua LiteLLM pass-through endpoint.
5. Muốn dùng như 1 tool MCP cho agent — có "Jev MCP" (Python MCP server expose sẵn tool `classify`/`score`/`check`/`match`/`screen`), nhưng đây là **dự án cộng đồng**, không phải bản chính chủ TypeSafe.

## Ví dụ thực tế
Cho hệ thống agent kiểu Hermes/OpenClaw: trước khi để 1 agent tốn token gọi LLM đầy đủ để "đọc hiểu rồi quyết định", dùng Jev làm lớp lọc rẻ — vd chấm điểm mức độ khẩn cấp của 1 ticket khách ABTRIP gửi vào (Score 1-10), hoặc kiểm tra nhanh "output của agent A có đúng định dạng yêu cầu không" (Boolean) trước khi cho agent B xử lý tiếp, tránh phải gọi cả 1 LLM to chỉ để trả lời có/không.

## Lưu ý / Lỗi thường gặp
- **Đây là model rất mới, chưa được kiểm chứng độc lập rộng** — mọi số liệu benchmark (193.6x nhanh hơn, 444.6x rẻ hơn) là do chính TypeSafe công bố trên "workflow evaluations" của họ, chưa thấy bên thứ ba đối chiếu lại. Xem là tín hiệu đáng để test thử, không phải con số chốt.
- Community đã tự thừa nhận rõ: "schema-valid output không đồng nghĩa quyết định đúng" — Jev trả về đúng định dạng luôn (Choice/Score/Boolean hợp lệ) nhưng không có nghĩa quyết định đó chính xác, vẫn phải tự validate trên dữ liệu thật và giữ hành động quan trọng ở lớp kiểm tra deterministic riêng, không giao thẳng cho Jev quyết định.
- Hiện đang **early access + waitlist** — không phải ai cũng gọi được API chính chủ ngay, cách dễ nhất để test không cần chờ là qua Vercel AI Gateway hoặc adapter drop-in (`system-one-adapter-python`, TypeSafe cung cấp chính chủ) giả lập bằng OpenAI/Anthropic để so sánh trước khi có quyền dùng Jev thật.
- Rất nhiều SDK/tool "unofficial" mọc lên rất nhanh (PHP, Ruby, Rust, Elixir...) — chỉ 2 SDK chính chủ là Python (`typesafe-ai/typesafe-sdk-python`) và JS/TS (`typesafe-ai/typesafe-sdk-js`), còn lại đều là cộng đồng tự làm, không có gì đảm bảo tương thích lâu dài.
- Không hỗ trợ streaming (khác LLM thường) — vì bản chất trả về 1 quyết định có cấu trúc, không phải sinh văn bản dần dần.

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng đúng vào 1 lỗ hổng thật của hệ agent hiện tại — dùng cả 1 LLM to chỉ để trả lời "có/không" hay "chọn A hay B" là lãng phí token; nếu số liệu tốc độ/chi phí đúng như công bố, đây là lớp quyết định rẻ rất đáng chèn vào vòng lặp agent (routing, guardrail).
- **Điểm yếu:** Quá mới để đánh giá chắc chắn — chưa có kiểm chứng độc lập, còn early access/waitlist nên chưa thể tích hợp ngay lập tức vào production. Ecosystem SDK cộng đồng mọc nhanh nhưng thiếu chuẩn hoá, dễ chọn nhầm bản không chính chủ.
- **Có nên dùng không:** 6/10 tại thời điểm này — đáng theo dõi và thử nghiệm ở mức nhỏ (qua Vercel AI Gateway, không cần chờ waitlist) cho các quyết định phụ (routing, chấm điểm) trong hệ agent, chưa nên giao việc quan trọng/nhạy cảm cho tới khi có thêm bên thứ ba kiểm chứng.

## Link
- Repo/Org chính chủ: https://github.com/typesafe-ai
- SDK Python: https://github.com/typesafe-ai/typesafe-sdk-python
- SDK JS/TS: https://github.com/typesafe-ai/typesafe-sdk-js
- Docs: https://docs.typesafe.ai
- Qua Vercel AI Gateway (không cần waitlist): https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Cài: pip install typesafe-sdk
import os
os.environ["TYPESAFE_API_KEY"] = "your-key"

from typesafe import TypeSafeClient   # tên class có thể đổi theo version SDK, kiểm tra docs

client = TypeSafeClient()
result = client.evaluate(
    model="jev-latest",
    state="Khách đã yêu cầu hoàn tiền vé máy bay 2 lần trong tháng.",
    questions={"is_high_risk": {"type": "boolean", "instructions": "Đây có phải khách rủi ro cao không?"}},
)
```
> ⚠️ Model còn early access/waitlist — nếu chưa có quyền dùng API chính chủ, test tạm qua Vercel AI Gateway hoặc `system-one-adapter-python` (giả lập bằng LLM khác) trước.

### OpenClaw
```ts
// npm install @typesafe-ai/sdk (hoặc dùng qua AI SDK evaluate API nếu OpenClaw đã dùng Vercel AI SDK)
import { experimental_evaluate as evaluate } from 'ai';

const result = await evaluate({
  model: 'typesafe-ai/jev',
  state: inputText,
  questions: { nextAction: { type: 'choice', options: ['reply', 'escalate', 'ignore'] } },
});
```
> ⚠️ Đây là quyết định phụ trợ (routing/guardrail) — không nên dùng Jev làm lớp quyết định cuối cùng cho hành động quan trọng khi chưa validate kỹ trên dữ liệu thật của OpenClaw.

### Antigravity
Không áp dụng dạng deploy hạ tầng — đây là API bên thứ ba (TypeSafe), không tự host được. Antigravity chỉ cần đảm bảo biến môi trường `TYPESAFE_API_KEY` được set đúng cho service nào cần gọi Jev trên VPS, không có bước cài đặt server riêng.
