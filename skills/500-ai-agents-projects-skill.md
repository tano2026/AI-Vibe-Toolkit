# 500-AI-Agents-Projects — Skill Tìm Use Case + Code Mẫu (32.4k⭐)

**Repo:** github.com/ashishpatel26/500-AI-Agents-Projects | MIT
**Dùng cho:** Tìm idea + code mẫu AI agent theo ngành

---

## Cài & Dùng Ngay

```bash
git clone https://github.com/ashishpatel26/500-AI-Agents-Projects
cd 500-AI-Agents-Projects

# Chọn agent theo ngành
ls agents/  # xem danh sách

# Chạy agent cụ thể
cd agents/01-web-research-agent
pip install -r requirements.txt
cp .env.example .env  # điền API key
python agent.py
```

## Decision Tree — Chọn Framework

```
Task đơn giản, 1 agent?
→ Agno (dễ nhất, học nhanh)

Team agent theo vai trò?
→ CrewAI (Manager → Worker pattern)

Cần RAG + document Q&A?
→ LlamaIndex hoặc LangGraph

Cần agent tự viết code?
→ AutoGen

Cần production-grade, phức tạp?
→ LangGraph (stateful graph)
```

## 5 Agents Hay Nhất Để Bắt Đầu

```bash
# 1. Web Research Agent (Agno)
cd agents/web-research-agent
# → Nhập query → agent search + synthesize

# 2. Document Q&A (LlamaIndex)
cd agents/document-qa-agent
# → Upload PDF → hỏi bất kỳ

# 3. Code Review Agent (AutoGen)
cd agents/code-review-agent
# → Paste code → agent review + suggest

# 4. Market Research (CrewAI)
cd agents/market-research-crew
# → Nhập industry → team agent research + report

# 5. SQL Agent (LangChain)
cd agents/sql-agent
# → Hỏi bằng tiếng thường → agent viết SQL + query
```

## Workflow Dùng Kho Này

```
Mày cần build AI agent cho ngành X
→ ls agents/ | grep [keyword]
→ Clone agent gần nhất
→ Đọc agent.py (~100-200 dòng)
→ Adapt theo use case cụ thể
→ Không cần bắt đầu từ trang trắng
```

---
*skills/500-ai-agents-projects-skill.md | AI Vibe Toolkit | tháng 6/2026*
