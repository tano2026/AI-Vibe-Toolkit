# TurboVec — Vector Search 8x Nhỏ Hơn, Nhanh Hơn FAISS (~6k⭐)

**Repo:** github.com/RyanCodrai/turbovec | MIT
**Tech:** Rust SIMD + Python bindings | Based on Google TurboQuant research
**Benchmark:** 31GB → 4GB, nhanh hơn FAISS 2-8x

---

## Cài Nhanh

```bash
pip install turbovec
```

## Drop-in Replacement Cho FAISS

```python
import turbovec
import numpy as np

# Tạo index
index = turbovec.Index(dim=1536)  # OpenAI embedding size

# Add vectors (giống FAISS hoàn toàn)
vectors = np.random.rand(100000, 1536).astype('float32')
index.add(vectors)

# Search
query = np.random.rand(1, 1536).astype('float32')
distances, indices = index.search(query, k=10)

# Save/load
index.save("my_index.turbo")
index_loaded = turbovec.Index.load("my_index.turbo")
```

## So Sánh Với FAISS

```python
# FAISS (trước)
import faiss
index = faiss.IndexFlatL2(1536)
index.add(vectors)  # 31GB cho 10M vectors

# TurboVec (sau)
import turbovec
index = turbovec.Index(dim=1536, quantization="int8")
index.add(vectors)  # 4GB cho 10M vectors — 8x nhỏ hơn
```

## RAG Pipeline Với TurboVec

```python
from turbovec import Index
from anthropic import Anthropic

# Setup
embedder = ... # OpenAI / Cohere / local model
index = Index(dim=1536)
claude = Anthropic()

# Index documents
docs = load_documents("./knowledge_base/")
for doc in docs:
    embedding = embedder.embed(doc.content)
    index.add(embedding, metadata={"text": doc.content})

# Query
def rag_query(question):
    # Search relevant docs
    q_embedding = embedder.embed(question)
    distances, doc_ids = index.search(q_embedding, k=5)
    
    # Build context
    context = "
".join([docs[i].content for i in doc_ids[0]])
    
    # Ask Claude
    response = claude.messages.create(
        model="claude-sonnet-4-5",
        messages=[{
            "role": "user",
            "content": f"Context:
{context}

Question: {question}"
        }],
        max_tokens=1000
    )
    return response.content[0].text
```

## Khi Nào Dùng TurboVec

✅ RAG với > 100k documents
✅ Memory bị hạn chế (VPS nhỏ)
✅ Cần search nhanh, latency thấp
✅ Đang dùng FAISS muốn drop-in replace

❌ < 10k documents → FAISS hoặc simple list search đủ rồi
❌ Cần full-featured vector DB → Qdrant, Weaviate, Pinecone

---
*skills/turbovec-skill.md | AI Vibe Toolkit | tháng 6/2026*
