# Script Video 152 — Agentic Loop Optimizer

## Thông tin
- Tool/Skill liên quan: [skills/agentic-loop-optimizer.md](../skills/agentic-loop-optimizer.md)
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

---

## Hook (3 giây đầu)

"Agent của mày đang chạy vòng lặp — nhưng mày có biết nó đang đốt token vô ích không?"

---

## Script voiceover (ElevenLabs-ready)

[Đoạn 1 — vấn đề]
Hầu hết người build AI agent đều mắc 1 lỗi giống nhau: thiết kế tool xong nhưng quên thiết kế vòng lặp. Kết quả là agent cứ gọi tool rồi gọi lại, không ra kết quả, bill token tăng không kiểm soát.

[Đoạn 2 — giải pháp]
Loop engineering không phải về LLM mạnh hay yếu. Nó về kiến trúc. Mày cần 3 thứ: exit condition rõ ràng, model routing theo task, và context pruning sau mỗi vòng.

[Đoạn 3 — cụ thể]
Exit condition có 4 loại: max iterations, confidence gate, diminishing returns check, và cost cap. Thiếu 1 trong 4 là loop có thể spin mãi. Model routing đơn giản hơn mày nghĩ: task lookup dùng Haiku, task synthesis dùng Sonnet — tiết kiệm được 3 đến 4 lần chi phí. Context pruning: sau mỗi tool call, summarize kết quả rồi drop raw — đừng carry 2000 token qua vòng tiếp theo.

[Đoạn 4 — kết + CTA]
Tao đã tổng hợp toàn bộ patterns này thành 1 skill file trong kho AI Vibe Toolkit. Link trong bio. Follow để xem tiếp series build agent thật trên VPS.

---

## Ghi chú quay (OBS)

- Cảnh 1 (0-5s): Screen terminal — hiển thị vòng lặp agent đang chạy, token counter tăng dần
- Cảnh 2 (5-15s): Slide diagram — 3 pattern loop: Sequential → Reactive → Autonomous, animate từng bước
- Cảnh 3 (15-30s): Code split-screen — bên trái loop không có exit condition, bên phải có đủ 4 exit condition
- Cảnh 4 (30-42s): Terminal — chạy model routing thật, show Haiku vs Sonnet cost so sánh
- Cảnh 5 (42-50s): GitHub repo — zoom vào file agentic-loop-optimizer.md, highlight checklist 10 điểm

---

## Caption/Sub note (CapCut)

- "AGENT ĐANG ĐỐT TOKEN" → highlight đỏ, 0-3s
- "EXIT CONDITION" → highlight vàng, timing khi nói đến 4 loại
- "3-4x RẺ HƠN" → highlight xanh lá, khi nói model routing
- "CONTEXT PRUNING" → highlight cam, khi demo drop raw
- Cắt cảnh nhanh mỗi 3-4 giây để giữ attention

---

## Thumbnail idea (Canva)

- Nền tối (dark mode terminal aesthetic)
- Text lớn bên trái: **"Agent của mày đang lãng phí token?"**
- Bên phải: icon vòng lặp ♻️ với số "4 exit conditions"
- Góc dưới: badge "AI Vibe Toolkit #152"
- Font: monospace cho vibe coding

---

## CTA cuối video

"Skill file này trong kho AI Vibe Toolkit — link bio. Comment 'LOOP' nếu mày muốn tao làm video deep-dive về từng exit condition."
