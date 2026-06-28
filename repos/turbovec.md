# TurboVec — Vector Search Nhanh Hơn FAISS, 31GB → 4GB, Không Cần Training

**GitHub:** https://github.com/RyanCodrai/turbovec
**Stars:** ~6k | **License:** MIT
**Tác giả:** RyanCodrai (implement Google Research's TurboQuant)
**Language:** Rust (core SIMD) + Python bindings
**Based on:** TurboQuant paper — ICLR 2026, Google Research

---

## Vấn Đề Nó Giải Quyết

Mày build RAG pipeline — 10 triệu documents, mỗi vector 1536 dimensions (text-embedding-3-small), lưu float32 → **31GB RAM** chỉ cho vector index. Chưa tính embedding server, API, cache, LLM inference.

Pinecone, Weaviate Cloud giải quyết bằng cách charge mày theo usage. TurboVec giải quyết bằng cách compress:

**10 triệu vectors: 31GB → 4GB. Tìm kiếm nhanh hơn FAISS.**

---

## Cơ Chế — TurboQuant

Thay vì lưu float32 đầy đủ, TurboVec dùng **data-oblivious quantization**:

```
Vector gốc (float32 × 1536 dims) → 31GB/10M vectors
        ↓ TurboQuant compress
Vector nén (2-4 bit) → 4GB/10M vectors
        ↓ SIMD search (ARM NEON / x86 AVX-512)
Kết quả nearest neighbor
```

**Điểm khác biệt với FAISS (Product Quantization):**

| | FAISS PQ | TurboVec |
|--|---------|---------|
| Training phase | Cần train codebook trước | Không cần — online ingest |
| Thêm vector mới | Có thể cần rebuild | Add trực tiếp, không rebuild |
| Đổi embedding model | Rebuild toàn bộ | Rebuild nhưng nhanh hơn |
| Speed (ARM) | Baseline | Nhanh hơn 10-19% |

---

## Cài & Dùng

```bash
pip install turbovec
```

**RAG pipeline cơ bản:**
```python
import numpy as np
from turbovec import IdMapIndex

# Tạo index
index = IdMapIndex(dims=1536, bits=4)  # 4-bit compression

# Add vectors
embeddings = embed(documents)  # numpy array (N, 1536)
doc_ids = list(range(len(documents)))
index.add(embeddings, doc_ids)

# Search
query_vec = embed(["câu hỏi của user"])[0]
scores, ids = index.search(query_vec, k=5)
results = [documents[i] for i in ids]
```

**Save/Load index:**
```python
index.save("my_index.tvim")
index = IdMapIndex.load("my_index.tvim")
```

**Filter khi search (tenant isolation):**
```python
# Chỉ search trong subset documents
allowlist = [0, 1, 5, 10, ...]  # doc_ids được phép
scores, ids = index.search(query_vec, k=5, allowlist=allowlist)
```

---

## Tích Hợp Với RAG Frameworks

TurboVec swap được vào LangChain, LlamaIndex, Haystack, Agno:

```python
# LangChain
from langchain_turbovec import TurboVecVectorStore
vectorstore = TurboVecVectorStore.from_documents(docs, embeddings)

# LlamaIndex
from llama_index.vector_stores.turbovec import TurboVecVectorStore
vector_store = TurboVecVectorStore(index=index)
```

---

## RAG Pipeline Local Hoàn Toàn ($0 API)

```python
from turbovec import IdMapIndex
import ollama  # local LLM + embeddings

# Embed documents locally
def embed(texts):
    return [ollama.embed(model="bge-m3", input=t)["embeddings"][0] for t in texts]

# Build index
index = IdMapIndex(dims=1024, bits=4)
embeddings = embed(documents)
index.add(np.array(embeddings), list(range(len(documents))))

# Query
def rag_query(question):
    q_vec = embed([question])[0]
    _, ids = index.search(np.array(q_vec), k=3)
    context = "\n".join([documents[i] for i in ids])
    return ollama.chat(model="llama3", messages=[{
        "role": "user",
        "content": f"Context: {context}\n\nQuestion: {question}"
    }])
```

**Toàn bộ pipeline: $0/tháng, không data rời khỏi máy mày.**

---

## Benchmark Thực Tế

| Metric | Giá trị |
|--------|---------|
| Compression ratio | 16x (float32 → 2-bit) |
| 10M vectors RAM | 31GB → 4GB |
| Speed vs FAISS (ARM) | +10-19% faster |
| Speed vs FAISS (x86) | Tương đương ở 4-bit |
| Recall quality | Gần với full-precision (ICLR 2026 proof) |

---

## Điểm Trừ Thẳng Thắn

**"Faster than FAISS" không phải lúc nào cũng đúng:** Win trên ARM (Apple Silicon), tie hoặc sát nhau trên x86. Không phải luôn nhanh hơn.

**10M vectors chưa được reproduce rộng rãi:** Con số 31GB → 4GB là từ README, chưa có independent benchmark lớn xác nhận.

**Không phải vector database đầy đủ:** Không có dashboard, không có query language, không có distributed mode. Chỉ là library — mày phải tự build API layer nếu cần.

**Dynamic corpus có giới hạn:** Đổi embedding model vẫn cần rebuild. Corpus thay đổi liên tục thì có thể cần re-index.

---

## Khi Nào Dùng TurboVec

**✅ Phù hợp:**
- RAG pipeline local, privacy-first
- Dataset lớn, RAM hạn chế
- Apple Silicon (ARM — performance peak)
- Cần embedded library, không cần managed service

**❌ Không phù hợp:**
- Cần distributed vector search (nhiều nodes)
- Team không có Rust/Python expertise để debug
- Corpus cực dynamic (thêm/xóa liên tục hàng triệu vectors)
- Cần SLA và support

---

## Đánh Giá Cá Nhân

TurboVec giải quyết đúng pain point của vibe coders build RAG: Pinecone tốn tiền, FAISS tốn RAM. TurboQuant paper có basis toán học vững (ICLR 2026, Google Research) nên không phải hype trống rỗng.

Điểm tao thích nhất: **không cần training phase**. FAISS cần bạn train codebook trên data trước mới index được — mỗi lần đổi corpus là headache. TurboVec add vectors online, không cần prepare trước.

Cho local RAG pipeline dưới 10M documents — đây là lựa chọn tốt nhất hiện tại nếu mày muốn $0 managed service. Nếu mày cần scale lên distributed hoặc cần dashboard — vẫn phải dùng Pinecone/Weaviate.

**Rating: 8/10** — trừ điểm vì chưa có independent benchmark lớn và thiếu managed features.

---

*Nguồn: github.com/RyanCodrai/turbovec*
*TurboQuant paper: arXiv:2504.19874 — ICLR 2026*
*Cập nhật: tháng 6/2026*

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

QDRANT_URL = "http://localhost:6333"  # TurboVec dùng Qdrant backend

def vec_upsert(collection, id, vector, payload=None):
    data = json.dumps({"points": [{"id": id, "vector": vector, "payload": payload or {}}]}).encode()
    req = urllib.request.Request(
        f"{QDRANT_URL}/collections/{collection}/points",
        data=data, headers={"Content-Type": "application/json"}, method="PUT"
    )
    return json.loads(urllib.request.urlopen(req).read())

def vec_search(collection, query_vector, top_k=5, filters=None):
    payload = {"vector": query_vector, "limit": top_k, "with_payload": True}
    if filters:
        payload["filter"] = filters
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{QDRANT_URL}/collections/{collection}/points/search",
        data=data, headers={"Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())["result"]

# Use case: lưu embeddings của content kho, search semantic
```

### OpenClaw
```bash
# REST API — không cần npm
```

### Antigravity
```bash
docker run -d -p 6333:6333 -p 6334:6334 \
  -v qdrant_storage:/qdrant/storage \
  --name qdrant qdrant/qdrant
```
> ⚠️ Vector DB cho semantic search. Hermes tìm content tương tự trong kho.
