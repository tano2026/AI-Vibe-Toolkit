---
name: unsloth
description: >
  Stars: 68k+ Tác giả: unslothai (Daniel & Michael Han, YC S24) Domain: Fine-tuning LLM nhanh, tiết kiệm VRAM
---

# Unsloth — fine-tune LLM nhanh gấp 2-30 lần, tốn ít VRAM hơn 70-90%

**GitHub:** https://github.com/unslothai/unsloth
**Tác giả:** Daniel Han & Michael Han (anh em người Úc, YC S24, San Francisco)
**Stars:** 68k+ | Dual license Apache 2.0 / AGPL-3.0

---

## TL;DR

Thư viện fine-tune LLM mã nguồn mở — tự viết lại kernel bằng Triton thay vì dùng autograd mặc định của PyTorch, nên train nhanh hơn 2-30 lần và tốn ít VRAM hơn 70-90% mà không mất độ chính xác. Bản 2026 mới thêm training MoE nhanh gấp 12 lần.

## Tool này dùng để làm gì

Bình thường fine-tune 1 LLM (dù chỉ qua LoRA/QLoRA) cần GPU khá mạnh và tốn thời gian. Unsloth viết lại phần lõi tính toán (kernel) để làm việc này rẻ hơn hẳn — chạy được gpt-oss-20b chỉ với 12.8GB VRAM, tức là GPU tầm trung cũng train được model lớn. Hỗ trợ hầu hết model phổ biến: Llama, Qwen3 (kể cả bản 235B), Gemma, DeepSeek R1/V3, GLM, Mistral, Phi-4.

Bản 2026 mới bổ sung: train MoE nhanh 12x, fine-tune embedding model nhanh 2x (tốt cho RAG/retrieval), và Reinforcement Learning với context cực dài (380K token trên 1 GPU B200).

## Setup từng bước

1. Cài qua pip (khuyến nghị dùng Colab/Kaggle notebook có sẵn GPU miễn phí để thử trước):
```bash
pip install unsloth
```
2. Load model + áp LoRA:
```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3-8B-bnb-4bit",
    max_seq_length=2048,
    load_in_4bit=True,
)
model = FastLanguageModel.get_peft_model(model, r=16, lora_alpha=16)
```
3. Train bằng `SFTTrainer` của Hugging Face TRL như bình thường — Unsloth tự động patch kernel bên dưới

## Ví dụ thực tế

Muốn fine-tune 1 model chuyên trả lời câu hỏi về quy định hàng không/Timatic bằng dữ liệu nội bộ ABTRIP — dùng Unsloth train Qwen3-8B trên GPU thuê rẻ (RTX 4090 24GB) thay vì phải thuê A100 đắt đỏ, nhờ VRAM tiết kiệm 70%.

## Lưu ý / Lỗi thường gặp

- License kép: bản Apache 2.0 dùng thoải mái cho sản phẩm riêng; nhưng nếu build "fine-tuning-as-a-service" lộ API Unsloth ra ngoài thì dính AGPL-3.0, buộc phải mở nguồn dịch vụ đó
- Unsloth tối ưu cho single-GPU — nếu cần train multi-GPU quy mô production, cộng đồng khuyên chuyển sang Axolotl (Unsloth hợp giai đoạn thử nghiệm/prototype hơn)
- Một số model rất mới ra có thể chưa được hỗ trợ ngay, cần đợi bản cập nhật

## Đánh giá cá nhân

- **Điểm mạnh:** rào cản kỹ thuật thấp hẳn — GPU tầm trung vẫn fine-tune được model lớn; tài liệu và Colab mẫu rất đầy đủ, dev mới cũng làm theo được
- **Điểm yếu:** giới hạn ở single-GPU nên không hợp nếu cần scale production lớn; license AGPL cần đọc kỹ nếu định build sản phẩm bán ra ngoài
- **Có nên dùng không:** 8.5/10 — rất đáng thử nếu Tano Agency có nhu cầu fine-tune model riêng cho ABTRIP/An Bình mà không muốn tốn tiền GPU khủng

## Link
- Repo: https://github.com/unslothai/unsloth
- Docs: https://docs.unsloth.ai

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Unsloth là thư viện Python, Hermes dùng trực tiếp trong pipeline training
from unsloth import FastLanguageModel

def load_finetune_model(model_name="unsloth/Qwen3-8B-bnb-4bit"):
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=model_name, max_seq_length=2048, load_in_4bit=True
    )
    return FastLanguageModel.get_peft_model(model, r=16, lora_alpha=16), tokenizer
```

### OpenClaw
```bash
pip install unsloth
# hoặc cài bản đủ extras cho training + inference
pip install "unsloth[all]"
```

### Antigravity
```bash
# Deploy trên VPS có GPU — kiểm tra driver CUDA trước khi cài
nvidia-smi   # xác nhận GPU + CUDA version
pip install unsloth
```
> ⚠️ Cần GPU thật (không chạy được thuần CPU) — nếu VPS hiện tại không có GPU, phải thuê thêm GPU instance riêng cho việc fine-tune.
