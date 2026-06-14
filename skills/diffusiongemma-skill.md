# DiffusionGemma — LLM Tạo Text 4x Nhanh Hơn (Google, 10/6/2026)

**Nguồn:** google/diffusiongemma-26B-A4B-it | Apache 2.0
**Architecture:** 26B MoE, 3.8B active params | Diffusion-based (không phải autoregressive)

---

## Concept Khác Biệt

```
LLM thường (autoregressive):
token 1 → token 2 → token 3 → ... → token N
(tuần tự, chậm)

DiffusionGemma (diffusion):
[MASK][MASK][MASK]...[MASK] → refine song song → full text
(song song, 4x nhanh)
```

## Load Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "google/diffusiongemma-26B-A4B-it"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Generate
inputs = tokenizer("Giải thích AI agent trong 3 câu:", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))
```

## Dùng Qua HuggingFace Inference API (Không Cần GPU)

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/google/diffusiongemma-26B-A4B-it"
headers = {"Authorization": "Bearer hf_xxx"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({"inputs": "Viết code Python đọc CSV:"})
```

## Khi Nào Dùng DiffusionGemma

✅ Cần generate text **nhanh** (batch inference)
✅ Server phải handle nhiều requests cùng lúc
✅ Budget GPU thấp (3.8B active params)
✅ Tasks không cần ultra-high quality

❌ Tasks cần reasoning phức tạp → dùng Claude
❌ Cần instruction following chính xác → dùng Gemini Pro
❌ Production apps quan trọng → test kỹ trước (experimental)

## So Sánh Nhanh

| | DiffusionGemma | Llama 3.1 8B | Claude Haiku |
|--|----------------|--------------|-------------|
| Speed | 4x nhanh | Baseline | Medium |
| Quality | Good | Good | Excellent |
| Cost | $0 self-host | $0 self-host | Pay per token |
| GPU | ~8GB VRAM | ~8GB VRAM | Cloud |

---
*skills/diffusiongemma-skill.md | AI Vibe Toolkit | tháng 6/2026*
