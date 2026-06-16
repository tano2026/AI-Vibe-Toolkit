# 7B Vượt GPT-5 Trên LiveCodeBench — Sakana AI Research Note

**Paper:** arXiv:2512.04388 | **By:** Sakana AI
**Nguồn:** @ainius.net | tháng 6/2026
**Loại:** Research insight — không phải tool để cài

---

## Core Finding

Model 7B parameters của Sakana AI vượt GPT-5 trên LiveCodeBench — benchmark coding thực tế.

```
7B model → Beat GPT-5 on LiveCodeBench
Chìa khóa: không phải model lớn hơn
→ "Orchestration beats scale"
```

---

## Tại Sao 7B Có Thể Vượt GPT-5?

### 1. Task Decomposition
```
GPT-5 (monolithic):
Problem → Single LLM → Solution

7B Orchestrated:
Problem
  → Decompose thành sub-tasks
  → Assign từng sub-task cho 7B model
  → Verify từng bước
  → Combine
→ Better result, ít tốn hơn
```

### 2. Specialization > Raw Power
```
7B fine-tuned cho coding
> 100B general model
cho coding tasks cụ thể
```

### 3. Multi-attempt + Self-critique
```
7B → solution 1 → self-critique → solution 2 → verify → final
vs
GPT-5 → solution 1 → done
```

---

## Ý Nghĩa Thực Tế

### Cho AI Agent Design
```
Đừng chỉ dùng model lớn nhất
→ Orchestrate nhiều model nhỏ chuyên biệt
→ Thường tốt hơn và rẻ hơn

Ví dụ trong kho:
- Claude Sonnet cho reasoning
- Claude Haiku cho classification tasks
- Local 7B (Ollama) cho repetitive tasks
= Tiết kiệm 80% cost, quality tương đương
```

### Cho SAMS Loop Design
```
Maker agent: 7B specialized model ($0, local)
Checker agent: Claude Sonnet (quality verify)
→ Cost-effective loop
→ Checker không cần lớn bằng maker
```

---

## Model 7B Nào Chạy Được Local (Ollama)

```bash
# Pull models
ollama pull codellama:7b       # coding focused
ollama pull deepseek-coder:7b  # code generation
ollama pull qwen2.5-coder:7b   # coding tasks

# Dùng trong Python
import ollama
response = ollama.generate(
    model='deepseek-coder:7b',
    prompt='Write a Python function to...'
)
```

---

*AI Vibe Toolkit | Sakana AI 7B Research | tháng 6/2026*
