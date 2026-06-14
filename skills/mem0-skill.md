# mem0 — Skill Thêm Memory Vào AI Agent (48k⭐)

**Repo:** github.com/mem0ai/mem0 | MIT | YC-backed | $24M Series A
**Dùng với:** Python, Node.js, bất kỳ LLM nào

---

## Cài Nhanh

```bash
pip install mem0ai
export OPENAI_API_KEY="..."   # hoặc Anthropic, Groq...
```

## 3 Dòng Code Thêm Memory

```python
from mem0 import Memory

m = Memory()

# Lưu memory
m.add("Tao thích Python hơn JavaScript", user_id="user_1")
m.add("Tao đang làm AI Vibe Toolkit, push lên GitHub", user_id="user_1")

# Search memory
results = m.search("tech stack của tao là gì?", user_id="user_1")
# → trả về: "Python, GitHub workflow, AI tools"

# Get tất cả memories
all_memories = m.get_all(user_id="user_1")
```

## Tích Hợp Với Claude

```python
from mem0 import MemoryClient
from anthropic import Anthropic

mem_client = MemoryClient(api_key="m0-xxx")  # cloud version
claude = Anthropic()

user_id = "user_123"
conversation_history = []

def chat_with_memory(user_msg):
    # Lấy relevant memories
    memories = mem_client.search(user_msg, user_id=user_id, limit=5)
    mem_context = "
".join([m['memory'] for m in memories])
    
    # Build prompt với memory context
    system = f"Memories về user:
{mem_context}

Dùng memories trên để trả lời personalized."
    
    conversation_history.append({"role": "user", "content": user_msg})
    
    response = claude.messages.create(
        model="claude-sonnet-4-5",
        system=system,
        messages=conversation_history,
        max_tokens=1000
    )
    
    assistant_msg = response.content[0].text
    conversation_history.append({"role": "assistant", "content": assistant_msg})
    
    # Lưu conversation vào memory
    mem_client.add(conversation_history, user_id=user_id)
    
    return assistant_msg
```

## Self-hosted (Free, Không Cần API Key)

```python
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333}
    },
    "llm": {
        "provider": "groq",
        "config": {"model": "llama-3.1-8b-instant", "api_key": "..."}
    },
    "embedder": {
        "provider": "huggingface",
        "config": {"model": "BAAI/bge-small-en-v1.5"}
    }
}
m = Memory.from_config(config)
```

## Khi Nào Dùng mem0 vs Claude Projects vs Hermes L5

| | mem0 | Claude Projects | Hermes L5 |
|--|------|----------------|-----------|
| Cross-session | ✅ | ✅ | ✅ |
| Multi-user | ✅ | ❌ | ❌ |
| Semantic search | ✅ | ❌ | Partial |
| Self-hosted | ✅ | ❌ | ✅ |
| Token savings | -72% | Không đo | -73% |
| Setup | 5 phút | 0 phút | 30 phút |

**Rule:** App nhiều users → mem0. Personal agent → Hermes L5.

---
*skills/mem0-skill.md | AI Vibe Toolkit | tháng 6/2026*
