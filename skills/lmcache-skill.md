# lmcache — Cache LLM Context, Tăng Tốc + Tiết Kiệm Chi Phí (8.6k⭐)

**Repo:** github.com/LMCache/LMCache | Apache 2.0
**Stars:** 8.6k | Tích hợp với vLLM, SGLang, OpenAI API

---

## Concept

LLM phải recompute KV cache mỗi lần dù context không đổi → **tốn compute + chậm**.

LMCache: **lưu KV cache** → lần sau dùng lại → tiết kiệm 40-70% latency, 50%+ chi phí.

## Khi Nào LMCache Hữu Ích Nhất

✅ **System prompt dài** (dùng đi dùng lại nhiều lần)
✅ **RAG với documents** (same docs, different questions)
✅ **Multi-turn conversations** (context dài)
✅ **Batch inference** (same prefix khác nhau)

## Setup Với vLLM

```bash
pip install lmcache vllm

# Chạy vLLM với LMCache
python -m vllm.entrypoints.openai.api_server     --model meta-llama/Llama-3.1-8B-Instruct     --lmcache-config-file lmcache_config.yaml
```

```yaml
# lmcache_config.yaml
chunk_size: 256
local_cpu:
  enable: true
  max_cache_size: 20  # GB
```

## Tích Hợp OpenAI-Compatible API

```python
from openai import OpenAI

# Point tới local server với LMCache
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="none"
)

# Lần 1: compute + cache
response = client.chat.completions.create(
    model="llama-3.1-8b",
    messages=[
        {"role": "system", "content": LONG_SYSTEM_PROMPT},  # cache này
        {"role": "user", "content": "Question 1"}
    ]
)

# Lần 2: dùng cache → nhanh hơn 40-70%
response = client.chat.completions.create(
    model="llama-3.1-8b", 
    messages=[
        {"role": "system", "content": LONG_SYSTEM_PROMPT},  # từ cache
        {"role": "user", "content": "Question 2"}           # chỉ cần compute cái này
    ]
)
```

## Savings Thực Tế

| Use Case | Latency Reduction | Cost Reduction |
|----------|------------------|----------------|
| System prompt 2k tokens | -50% | -40% |
| RAG 10k context | -65% | -55% |
| Multi-turn 20k | -70% | -60% |

## Khi Nào KHÔNG Cần LMCache

❌ Simple one-shot queries (mỗi câu khác nhau hoàn toàn)
❌ Dùng Claude API (Anthropic tự handle caching)
❌ Context ngắn < 1k tokens

**Note:** Anthropic đã có prompt caching built-in → chỉ cần LMCache khi self-host vLLM.

---
*skills/lmcache-skill.md | AI Vibe Toolkit | tháng 6/2026*
