# Script Video #23 — DiffusionGemma: Google Vừa Thay Đổi Cách LLM Sinh Text

**Format:** TikTok / YouTube Shorts (~85s)
**Hook type:** "Paradigm shift" — cách mới hoàn toàn
**Style:** Không lộ mặt, animation diagram + terminal

---

## 🎬 SCRIPT

**[0s - 8s] HOOK**
> "Từ GPT-1 đến Claude 4 — tất cả LLM đều sinh text theo cùng 1 cách: từng từ một, trái sang phải. Ngày 10 tháng 6 năm 2026, Google thay đổi điều đó."

*[Show: animation token-by-token → contrast với parallel generation]*

**[8s - 28s] AUTOREGRESSIVE VS DIFFUSION**
> "LLM thông thường — mỗi token phải chờ token trước. Sinh 1000 từ = 1000 lần xử lý tuần tự. GPU spend 90% thời gian chờ load weights."

*[Show: diagram autoregressive — token xuất hiện từng cái một]*

> "DiffusionGemma làm ngược lại. Bắt đầu từ 256 ô trống — refine tất cả cùng lúc — hội tụ thành text hoàn chỉnh."

*[Show: 256 masked tokens → dần dần resolve thành text — animation đẹp]*

> "Kết quả: 4 lần nhanh hơn. 1000+ tokens mỗi giây trên H100."

**[28s - 50s] SPECS THỰC TẾ**
> "26 tỷ parameters nhưng chỉ activate 3.8 tỷ mỗi bước — Mixture of Experts. Cần 18GB VRAM ở 4-bit. 256K context. Đọc được cả image và video. 140 ngôn ngữ. Apache 2.0."

*[Show: specs list trên màn hình]*

> "Chạy được với HuggingFace Transformers, vLLM, MLX trên Mac ngay từ ngày đầu."

**[50s - 68s] HONEST REVIEW**
> "Thật thà mà nói — quality thấp hơn Gemma 4 thông thường. Google tự thừa nhận. Đây không phải 'LLM tốt nhất' — đây là 'LLM nhanh nhất ở quality chấp nhận được'."

> "Ngon nhất cho: code infilling, inline editing, task cần response tức thì. Không phải cho reasoning phức tạp."

> "Thêm nữa: nếu mày dùng GPU tầm trung — RTX 3060, 4060 — speed advantage gần như biến mất. Cần GPU xịn mới thấy khác biệt."

**[68s - 85s] TẠI SAO QUAN TRỌNG + CTA**
> "Đây là lần đầu tiên có diffusion LLM open-weight đủ lớn để chạy được. Nếu hướng này tiếp tục — tốc độ sẽ không còn là vấn đề của local AI nữa."

> "Watch repo này trong 6 tháng tới. Link HuggingFace trong bio."

*[Show: google/diffusiongemma-26B-A4B-it]*

---

## 📝 CAPTION
```
Google vừa thay đổi cách LLM hoạt động — không còn từng token một nữa 🚀

DiffusionGemma: 256 tokens song song · 4x nhanh hơn · Apache 2.0

Honest review: quality thấp hơn Gemma 4, GPU tầm trung không thấy khác biệt nhiều

Ra ngày 10/6/2026 — còn rất mới

#llm #googleai #diffusion #localai #vibecoding #ai #machinelearning
```

## 🎯 B-ROLL
1. **Animation quan trọng nhất:** autoregressive (token từng cái) vs diffusion (256 ô → resolve cùng lúc) — có thể dùng Claude tạo HTML animation
2. Benchmark chart: DiffusionGemma vs Gemma 4 speed
3. Terminal: download model từ HuggingFace, chạy inference
4. Quality comparison text output: DiffusionGemma vs Gemma 4 standard

## ⚙️ TẠO ANIMATION DIAGRAM
```
Prompt cho Claude:
"Tạo HTML animation minh họa:
- Bên trái: Autoregressive — token xuất hiện từng cái một, trái sang phải
- Bên phải: Diffusion — 256 ô masked → dần dần reveal cùng lúc
- Dark theme, smooth animation, loop"
→ Record bằng OBS
```

---
*Script v1 — tháng 6/2026*
