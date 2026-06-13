# Script Video #28 — TurboVec: RAG Pipeline 10 Triệu Docs Từ 31GB Xuống 4GB

**Format:** TikTok / YouTube Shorts (~80s)
**Hook type:** Cost/infrastructure shock
**Style:** Không lộ mặt, diagram + terminal demo

---

## 🎬 SCRIPT

**[0s - 8s] HOOK**
> "Mày build RAG chatbot với 10 triệu documents. Chỉ riêng vector index đã cần 31GB RAM — chưa tính LLM, API, cache. TurboVec nén cái đó xuống còn 4GB và tìm kiếm nhanh hơn FAISS."

*[Show: 31GB RAM bill → 4GB]*

**[8s - 22s] VẤN ĐỀ VỚI VECTOR DB HIỆN TẠI**
> "Pinecone, Weaviate Cloud — charge theo usage, data lên cloud. FAISS local thì tốn RAM và cần train codebook trước khi index được."

> "TurboVec khác: implement Google's TurboQuant algorithm — nén vector 16 lần, không cần training phase, add documents trực tiếp."

**[22s - 50s] DEMO**
> "Cài:"
```bash
pip install turbovec
```

```python
from turbovec import IdMapIndex
import numpy as np

# Tạo index — 1536 dims, 4-bit compression
index = IdMapIndex(dims=1536, bits=4)

# Add 10M documents — không cần train trước
index.add(embeddings, doc_ids)

# Search — nhanh hơn FAISS trên Apple Silicon
scores, ids = index.search(query_vec, k=5)
```

*[Show: search time comparison bar chart]*

> "Kết quả: 4GB thay vì 31GB. Search trên Apple Silicon nhanh hơn FAISS 10-19%."

**[50s - 65s] LOCAL RAG $0**
> "Combine với Ollama — toàn bộ RAG pipeline chạy local, $0/tháng, không data lên cloud:"

```
Documents → Ollama embed → TurboVec index
Query → Ollama embed → TurboVec search → top docs → Ollama LLM → Answer
```

> "Không Pinecone, không OpenAI, không gì hết."

**[65s - 80s] HONEST + CTA**
> "Thật thà: nhanh hơn FAISS chủ yếu trên ARM — Apple Silicon. x86 thì sát nhau. Và đây là library, không phải database đầy đủ — không có dashboard hay distributed mode."

> "Nhưng cho local RAG dưới 10 triệu docs — đây là lựa chọn tốt nhất hiện tại. MIT license, link trong bio."

*[Show: github.com/RyanCodrai/turbovec]*

---

## 📝 CAPTION
```
RAG pipeline cần 31GB RAM? TurboVec nén xuống 4GB, search nhanh hơn FAISS 🔥

Implement Google's TurboQuant (ICLR 2026) · Không cần training phase · MIT license

Combine với Ollama = RAG local $0/tháng, không data lên cloud

~6k ⭐ · github.com/RyanCodrai/turbovec

#rag #vectordatabase #python #vibecoding #ai #llm #localai #rust
```

## 🎯 B-ROLL
1. RAM usage comparison: 31GB vs 4GB — visual bar
2. Terminal: `pip install turbovec` → index build → search query
3. Speed benchmark chart: TurboVec vs FAISS
4. Local RAG flow diagram: Documents → TurboVec → Ollama → Answer

---
*Script v1 — tháng 6/2026*
