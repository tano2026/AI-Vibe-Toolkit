# DiffusionGemma — LLM tạo text 4x nhanh hơn, Google vừa thả 10/6/2026

**GitHub / HuggingFace:** google/diffusiongemma-26B-A4B-it
**License:** Apache 2.0 | **Ra mắt:** 10/6/2026
**Tác giả:** Google DeepMind
**Architecture:** 26B MoE (Mixture of Experts), 3.8B active params
**Status:** Experimental — không phải production model

---

## Tại Sao Đây Là Bước Ngoặt

Từ trước đến nay, tất cả LLM lớn (GPT, Claude, Gemma...) đều dùng **autoregressive** — sinh từng token một, trái qua phải, tuần tự. Muốn sinh 1000 tokens phải chờ 1000 lần forward pass.

DiffusionGemma dùng cách khác hoàn toàn — **text diffusion**:

```
Autoregressive:  Token1 → Token2 → Token3 → ... → Token1000
                 (tuần tự, phải chờ từng bước)

DiffusionGemma:  [MASK][MASK][MASK]...[MASK]  (256 tokens cùng lúc)
                      ↓ refine nhiều lần
                 Token1 Token2 Token3... Token256
                 (song song, nhiều token cùng một forward pass)
```

Kết quả: **4x nhanh hơn** Gemma 4 cùng size trên GPU dedicated.

---

## Specs Thực Tế

| Thông số | Giá trị |
|----------|---------|
| Total params | 26B (MoE) |
| Active params per step | 3.8B |
| Block size | 256 tokens parallel |
| Tốc độ H100 | 1,000+ tokens/s |
| Tốc độ RTX 5090 | 700+ tokens/s |
| VRAM cần (4-bit) | ~18GB |
| Context window | 256K tokens |
| Ngôn ngữ | 140+ |
| Multimodal | Có — image + video 60s |

---

## Cài & Chạy

**Cách 1: HuggingFace Transformers (ổn định nhất)**
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "google/diffusiongemma-26B-A4B-it"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    load_in_4bit=True  # cần ~18GB VRAM
)

inputs = tokenizer("Viết code Python đọc file CSV:", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0]))
```

**Cách 2: vLLM (production serving)**
```bash
pip install vllm
vllm serve google/diffusiongemma-26B-A4B-it --tensor-parallel-size 1
```

**Cách 3: MLX (Apple Silicon)**
```bash
pip install mlx-lm
mlx_lm.generate --model google/diffusiongemma-26B-A4B-it \
    --prompt "Explain diffusion models:"
```

**Cách 4: Unsloth (fine-tuning)**
```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    "google/diffusiongemma-26B-A4B-it",
    load_in_4bit=True,
)
```

---

## Tại Sao Diffusion Nhanh Hơn

**Autoregressive bị bottleneck bởi memory bandwidth:**
- Mỗi token = load toàn bộ weights từ VRAM → compute → output 1 token
- GPU spend 90% thời gian chờ load weights, không phải tính toán

**Diffusion exploit compute:**
- Draft 256 tokens cùng lúc → GPU tensor cores luôn bận
- Refine nhiều lần nhưng mỗi lần = 256 tokens → throughput cao hơn rất nhiều

**Thêm lợi ích của bi-directional attention:**
- Mỗi token attend đến tất cả tokens khác (cả trái lẫn phải)
- Tốt hơn cho: code infilling, inline editing, bài toán không tuyến tính

---

## Điểm Trừ — Google Tự Thừa Nhận

**Quality thấp hơn Gemma 4 standard trên benchmark:**
- DiffusionGemma thua Gemma 4 26B ở hầu hết benchmark quality
- Google nói thẳng: đây là tradeoff tốc độ vs chất lượng, không phải "tốt hơn"

**Hardware requirements cao:**
- 700-1000+ tokens/s chỉ đạt được trên H100 / RTX 5090
- GPU thường (RTX 3060, 4060, laptop GPU) — speed advantage gần như biến mất
- Apple Silicon — MLX support nhưng không đạt tốc độ peak

**Ecosystem chưa chín:**
- llama.cpp: unmerged PR, chưa stable
- Ollama: không support
- Community GGUF quantizations: chất lượng không đảm bảo
- Chưa có LoRA/QLoRA recipes

---

## Dùng Khi Nào, Không Dùng Khi Nào

**✅ Phù hợp:**
- Code infilling (điền code giữa chừng)
- Inline editing (sửa đoạn văn cụ thể)
- Rapid iteration — cần response nhanh, chấp nhận quality vừa phải
- Research về diffusion LLM
- App cần throughput cao, không cần accuracy tuyệt đối

**❌ Không phù hợp:**
- Production AI assistant cần quality cao
- Người dùng GPU tầm trung (RTX 3060/4060)
- Cần ecosystem ổn định (LoRA, quantization phong phú)
- Task cần reasoning sâu hoặc accuracy cao

---

## Đây Có Phải Tương Lai Không?

Diffusion LLM không phải ý tưởng mới — Inception Labs (Mercury), Google nội bộ (Gemini Diffusion) đã nghiên cứu từ trước. DiffusionGemma là lần đầu tiên có **open-weight diffusion LLM đủ lớn** để người dùng thực sự chạy được.

Nếu hướng đi này đúng và ecosystem mature thêm 6-12 tháng nữa — tốc độ sẽ không còn là nút thắt lớn nhất của local AI nữa. Đó là tuyên bố lớn.

Hiện tại (6/2026): thú vị để theo dõi và thử nghiệm, chưa phải thay thế autoregressive models cho production.

---

## Đánh Giá Cá Nhân

DiffusionGemma là release đáng chú ý nhất của Google trong tháng 6/2026 — không phải vì nó tốt nhất, mà vì nó **khác nhất**.

4x speed với cùng size là con số thực, không phải marketing. Nhưng quality tradeoff là thật. Google honest về điều này — đây là experimental, không phải Gemma 5.

Điểm tao thấy hứa hẹn nhất: **bi-directional attention cho code infilling**. Autoregressive models viết code từ trái sang phải — không "nhìn" được context phía sau. DiffusionGemma nhìn được cả 2 chiều → tiềm năng cho coding assistant rất lớn nếu quality cải thiện.

Watch repo này trong 3-6 tháng tới. Nếu llama.cpp và Ollama support mature, đây sẽ là topic hot.

**Rating: 7.5/10** — tiềm năng cao, ecosystem chưa ready cho vibe coders thông thường.

---

*Nguồn: blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation*
*HuggingFace: google/diffusiongemma-26B-A4B-it*
*Cập nhật: tháng 6/2026*
