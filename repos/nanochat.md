# nanochat (Karpathy) — Tự Train AI Của Riêng Mày Với $100

> Andrej Karpathy — cha đẻ "vibe coding" — viết toàn bộ pipeline train LLM từ đầu trong 8k dòng code đọc được. Train ChatGPT của mày với $15-100.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **GitHub** | [karpathy/nanochat](https://github.com/karpathy/nanochat) ⭐ 42,000+ |
| **Tác giả** | Andrej Karpathy (Tesla AI, OpenAI founding member) |
| **Demo** | nanochat.karpathy.ai |
| **Chi phí train** | ~$15-100 (spot instance) |
| **Free** | ✅ Open source |

---

## 🎯 Nanochat là gì

Mày biết GPT-2 cost $43,000 để train năm 2019?

**nanochat làm điều tương tự với $48** — trên 8 GPU H100 thuê 2 tiếng. Spot instance còn rẻ hơn, khoảng $15.

Không phải để dùng thay ChatGPT — mà để **hiểu AI thực sự hoạt động thế nào:**
- Tokenization từ đầu (BPE bằng Rust)
- Pretraining loop
- Finetuning + RLHF
- Evaluation
- Chat UI để nói chuyện với model mày vừa train

---

## ⚡ Bắt đầu nhanh

```bash
# Clone về
git clone https://github.com/karpathy/nanochat.git
cd nanochat

# Cài dependencies
uv sync
source .venv/bin/activate

# Chạy toàn bộ pipeline tự động
bash runs/speedrun.sh

# Nếu không có GPU — chạy CPU (nhỏ hơn, chậm hơn)
bash runs/runcpu.sh
```

---

## 💡 Tại sao hay cho vibe coders

**Không cần chạy thật để học được nhiều:**
- Đọc code → hiểu Transformer hoạt động thế nào
- Hiểu tại sao AI hallucinate
- Hiểu tại sao context window quan trọng
- Biết trade-off giữa model size và quality

→ Sau khi đọc nanochat, mày sẽ prompt AI giỏi hơn hẳn vì hiểu nó đang làm gì.

---

## ⚠️ Lưu ý

- Train full model cần GPU — thuê RunPod hoặc Lambda Labs
- Chạy CPU được nhưng rất chậm và model rất nhỏ
- Code tiếng Anh — nhờ Claude giải thích từng phần
- Đây là để học, không phải dùng production

---

## 🔗 Hay kết hợp với

- **Vibe Coder Assistant skill** — nhờ Claude giải thích từng đoạn code trong nanochat
- **karpathy/autoresearch** — repo mới của Karpathy: AI agent tự nghiên cứu và cải thiện training

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Giá trị học hỏi | ⭐⭐⭐⭐⭐ |
| Dùng thực tế ngay | ⭐⭐☆☆☆ |
| Content potential | ⭐⭐⭐⭐⭐ |
| Wow factor | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Không phải tool dùng hàng ngày — nhưng là goldmine content. "Tao vừa tự train AI của mình với $15" là hook cực mạnh cho video.

---

*Thêm vào kho: 06/2025 | Nguồn: github.com/karpathy/nanochat*
