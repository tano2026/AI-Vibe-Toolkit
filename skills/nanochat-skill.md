# nanochat (Karpathy) — Tự Train LLM Với $15-100

**Repo:** github.com/karpathy/nanochat | MIT
**Tác giả:** Andrej Karpathy — cha đẻ "vibe coding"
**Code:** 8,000 dòng, readable từ đầu đến cuối

---

## Concept

Karpathy viết lại toàn bộ pipeline train LLM từ đầu — tokenizer, transformer, training loop, inference. Đọc được, học được, modify được.

## Cài & Run

```bash
git clone https://github.com/karpathy/nanochat
cd nanochat
pip install -r requirements.txt

# Train với data của mày
python train.py   --data_path ./data/my_texts.txt   --model_size small \  # ~10M params
  --epochs 10   --batch_size 32

# Generate text
python generate.py --model ./checkpoints/model.pt   --prompt "AI Vibe Toolkit là"
```

## Chi Phí Thực Tế

| Model Size | GPU | Thời gian | Chi phí |
|-----------|-----|-----------|---------|
| 10M params | T4 (Colab free) | 2-4h | $0 |
| 50M params | A100 (Colab Pro) | 4-8h | $15-30 |
| 200M params | A100 80GB | 8-24h | $50-100 |

## Dùng Để Học Gì

```
Đọc train.py → hiểu attention mechanism
Đọc model.py → hiểu transformer architecture
Đọc tokenizer.py → hiểu BPE tokenization
Modify → experiment với kiến trúc khác
```

## Fine-tune Với Data Của Mày

```bash
# Chuẩn bị data
python prepare_data.py --input my_docs/ --output data/train.txt

# Fine-tune từ checkpoint
python train.py   --resume_from ./checkpoints/base.pt   --data_path ./data/train.txt   --lr 1e-4   --epochs 3
```

## Khi Nào Dùng nanochat

✅ Muốn hiểu LLM từ bên trong
✅ Cần domain-specific small model ($0 inference sau khi train)
✅ Privacy: data không ra ngoài
✅ Học AI research từ đầu

❌ Production app cần quality cao → dùng Claude/GPT
❌ Không có thời gian học sâu → dùng HuggingFace fine-tune

---
*skills/nanochat-skill.md | AI Vibe Toolkit | tháng 6/2026*
