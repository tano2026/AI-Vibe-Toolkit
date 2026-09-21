# Swarms (kyegomez/swarms) — GitHub Repo

## TL;DR
Framework điều phối đa agent trưởng thành nhất đã research trong phiên này (từ 2023, vẫn active 2026, version 5.3.7) — và có 1 điểm kết nối trực tiếp: **đọc được thẳng thư mục `skills/<name>/SKILL.md` với đúng format frontmatter (`name`/`description`) đang dùng trong kho AI-Vibe-Toolkit, không cần chuyển đổi gì cả.**

## Repo này dùng để làm gì
Cho phép nhiều agent (mỗi agent = LLM + Tools + Memory) phối hợp theo nhiều kiểu kiến trúc dựng sẵn: Sequential (chuỗi tuần tự), Concurrent (chạy song song), Hierarchical (phân cấp), Graph-based, Mixture-of-Agents, Agent Council... Đây chính xác là các mẫu hình đã tự dựng tay trong Agentic Factory (Collector→Validator→Processor→Synthesizer) — Swarms có sẵn implementation đã test, không phải tự viết từ đầu mỗi lần.

## Điểm kết nối quan trọng nhất — Agent Skills tương thích thẳng với kho

Xác nhận từ docs chính thức (docs.swarms.world/agents/agent-skills), cấu trúc thư mục Swarms yêu cầu giống hệt cấu trúc kho đang dùng:
```
skills/
├── ten-skill/
│   └── SKILL.md   (frontmatter: name, description — đúng format kho)
```

Code load skill thật:
```python
from swarms import Agent

agent = Agent(
    agent_name="Research-Analyst",
    model_name="claude-sonnet-4-6",   # xác nhận hỗ trợ Claude, không khoá 1 model như Codex/OpenCreator
    skills_dir="./skills",             # trỏ thẳng vào bản sync của kho
    max_loops=1,
)
response = agent.run("Chấm điểm deal theo fit x intent")
# Swarms tự đọc metadata (name/description) từng SKILL.md, so khớp độ
# liên quan với task, CHỈ nạp đúng skill cần — không nhét hết 857 skill
# vào context mỗi lần
```

Đây giải quyết đúng vấn đề đã tự viết tay cho Content Pro/Sales-CEO (load_skill() fetch từng skill qua GitHub API, phải tự chỉ định tên) — Swarms có dynamic loading theo độ liên quan tác vụ, tự động, không cần code fetch riêng.

## Setup từng bước
1. Cài: `pip install -U swarms` (hoặc `uv pip install swarms`, khuyến nghị theo docs)
2. Cấu hình `.env`: `ANTHROPIC_API_KEY=...` (xác nhận có support thẳng, không chỉ OpenAI)
3. Clone/sync thư mục `skills/` từ kho AI-Vibe-Toolkit về máy chạy Swarms
4. Tạo Agent với `skills_dir` trỏ vào đó, chọn kiến trúc phù hợp (SequentialWorkflow/ConcurrentWorkflow/HierarchicalSwarm...)
5. Repo có sẵn CLAUDE.md ở gốc — thả vào project, Claude Code/Cursor tự biết cách viết code Swarms đúng chuẩn ngay lần đầu, không cần prompt thêm

## Ví dụ thực tế
Thay vì Hermes tự viết SALES_SKILLS = {...} cứng từng tên skill rồi fetch tay (cách đang làm), dựng 1 Agent Swarms với skills_dir trỏ vào agents/sales-ceo/skills/ — hỏi "chấm điểm deal X" thì Swarms tự nạp đúng deal-scoring-forecast-discipline, không cần biết trước tên skill.

## Lưu ý / Lỗi thường gặp
- Cần đồng bộ thư mục skills/ local với kho GitHub (không tự fetch qua API như Hermes Adapter đã viết) — cần cơ chế sync riêng (git pull định kỳ hoặc mount)
- Nhiều fork trùng mô tả y hệt (TheRWX, xizhuomengcontin, rksharma-owg, tokenaissance, praxstack...) — dùng đúng kyegomez/swarms (gốc, có nhiều sao/issue/release nhất, swarms.ai là site chính thức)
- Framework rất rộng (enterprise-grade, có cả x402 crypto payment, Agent2Agent, Marketplace) — không cần dùng hết, chỉ cần phần Agent + skills_dir + 1 kiến trúc phù hợp là đủ cho nhu cầu hiện tại

## Đánh giá cá nhân
- Điểm mạnh: trưởng thành nhất trong các tool research phiên này (3 năm phát triển, không phải fork hỗn loạn vài tuần tuổi); tương thích TRỰC TIẾP với format skill đã dùng; đa model (Claude/OpenAI/Groq...), không lock-in như OpenCreator (Codex)
- Điểm yếu: framework lớn, cần thời gian học các loại kiến trúc (Sequential/Concurrent/Hierarchical/Graph...) để chọn đúng; cần tự dựng cơ chế đồng bộ skills_dir với kho GitHub
- Có nên dùng: 9/10 — đáng đầu tư thời gian tìm hiểu, có thể trở thành ENGINE THẬT chạy phía sau Agentic Factory thay vì chỉ là khung lý thuyết

## Link
- Repo: https://github.com/kyegomez/swarms
- Docs: https://docs.swarms.world
- Docs Agent Skills (đã verify): https://docs.swarms.world/agents/agent-skills
- Awesome list: https://github.com/The-Swarm-Corporation/Awesome-Swarms-List

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Swarms cần pip install — VI PHẠM luật urllib-only của Hermes.
# KHÔNG cài trực tiếp trên Hermes. Đúng cách: Antigravity deploy Swarms
# như 1 service riêng (giống pattern Jev Bridge đã làm), Hermes gọi qua
# HTTP nội bộ, không tự chạy Swarms.
import urllib.request, json

def call_swarms_agent(task, agent_endpoint="http://localhost:8020/run"):
    payload = json.dumps({"task": task}).encode()
    req = urllib.request.Request(agent_endpoint, data=payload,
                                   headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())
```
> ⚠️ Endpoint /run là giả định minh hoạ — cần tự viết 1 FastAPI wrapper nhỏ bọc quanh Agent.run() của Swarms (giống mẫu Jev Bridge), không có sẵn REST endpoint chính thức từ Swarms.

### OpenClaw / Claude Code
```bash
pip install -U swarms
# Thả CLAUDE.md từ repo Swarms vào project — Claude Code tự viết code
# Swarms đúng chuẩn không cần hướng dẫn thêm
```

### Antigravity
```bash
# Deploy Swarms như service nội bộ, đồng bộ skills_dir với kho
python3 -m venv swarms-env && source swarms-env/bin/activate
pip install -U swarms fastapi uvicorn
git clone https://github.com/tano2026/AI-Vibe-Toolkit /opt/kho-sync --depth 1
# Cron định kỳ git pull để đồng bộ skills_dir mới nhất
```
