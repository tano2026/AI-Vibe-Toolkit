# Deep Agents — GitHub Repo

## TL;DR
Thư viện Python (kèm bản JS) của LangChain — đóng gói sẵn "bộ giáp" cho agent: lập kế hoạch, đọc/ghi file, gọi shell, đẻ sub-agent, tự tóm gọn context khi hội thoại dài — thay vì tự viết tay từng phần như khi dùng LangGraph trần. 27.5k star, lấy cảm hứng trực tiếp từ Claude Code.

## Repo này dùng để làm gì
Bình thường muốn agent làm được việc phức tạp nhiều bước (research dài, code nhiều file, task cần nhớ lâu) thì phải tự ghép planning + filesystem + sub-agent + quản lý context bằng tay trên LangGraph. Deep Agents gói sẵn hết 4 thứ đó thành 1 hàm `create_deep_agent()`, gọi là có agent chạy được ngay, mọi phần đều override được nếu không thích default. Không kén model — chạy được với OpenAI, Anthropic, Google, hoặc model local qua Ollama/vLLM/llama.cpp, miễn model hỗ trợ tool calling.

## Setup từng bước
1. Cài package (khuyến nghị dùng `uv`, hoặc pip bình thường cũng được):
   ```bash
   uv add deepagents
   # hoặc: pip install deepagents
   ```
2. Viết agent tối thiểu:
   ```python
   from deepagents import create_deep_agent

   agent = create_deep_agent(
       model="openai:gpt-5.5",
       tools=[my_custom_tool],
       system_prompt="You are a research assistant.",
   )
   result = agent.invoke({"messages": "Research LangGraph and write a summary"})
   ```
3. Agent tự lập kế hoạch (`write_todos`), đọc/ghi file (`read_file`/`write_file`/`edit_file`), chạy shell (`execute`, có sandbox), và đẻ sub-agent (`task`) khi cần tách context riêng cho từng việc con.
4. Muốn trace/debug/đánh giá production → nối với LangSmith (khuyến nghị chính chủ LangChain).
5. Muốn 1 agent code sẵn kiểu Claude Code chạy trong terminal (không phải tự build) → cài riêng "Deep Agents Code":
   ```bash
   curl -LsSf https://langch.in/dcode | bash
   ```

## Ví dụ thực tế
Dùng cho task research/report kiểu ABTRIP cần tổng hợp thị trường: `create_deep_agent` với system prompt "bạn là trợ lý research du lịch hàng không", cấp thêm tool web search — agent tự lập todo list các bước cần điều tra, ghi kết quả tạm ra file thay vì nhồi hết vào context (tránh tràn context khi research dài), đẻ sub-agent riêng để đào sâu 1 nhánh (vd đối thủ cạnh tranh) trong khi agent chính tiếp tục phần khác, cuối cùng tổng hợp thành báo cáo.

## Lưu ý / Lỗi thường gặp
- Model string dùng format `"openai:gpt-5.5"` (có tiền tố provider) — quen code LangChain cũ dễ quên phần tiền tố này.
- Model demo trong README dùng `gpt-5.5`/`gpt-6-astra` — đây là ví dụ minh hoạ của repo tại thời điểm viết tài liệu, luôn kiểm tra lại model string thật đang hỗ trợ trước khi chạy, vì tên model đổi theo thời gian.
- **Bảo mật quan trọng nhất cần nhớ:** Deep Agents theo triết lý "trust the LLM" — nghĩa là agent làm được BẤT CỨ GÌ tool của nó cho phép, không có cơ chế tự kiểm duyệt hành vi ở tầng model. Muốn an toàn phải chặn ở tầng tool/sandbox (như ví dụ OpenShell sandbox trong hệ sinh thái deepagents), không phải trông chờ agent "tự biết dừng".
- Có 3 lớp trong hệ sinh thái LangChain dễ nhầm: LangGraph (runtime graph) → LangChain `create_agent` (harness nhẹ) → Deep Agents (harness đầy đủ tính năng trên cùng). Chọn nhầm lớp dễ dẫn tới over-engineer (dùng Deep Agents cho task đơn giản) hoặc thiếu tính năng (tự viết lại filesystem/sub-agent bằng LangGraph trần trong khi Deep Agents có sẵn).

## Đánh giá cá nhân
- **Điểm mạnh:** Không phải xây agent harness từ đầu — planning, filesystem, sub-agent, context management đều có sẵn và chỉnh được từng phần, không bị khoá cứng. Model-agnostic thật sự (kể cả model local), đứng sau là LangChain nên hệ sinh thái docs/ví dụ/community rất dày (27.5k star, forum riêng, LangChain Academy miễn phí).
- **Điểm yếu:** Cảnh báo bảo mật "trust the LLM" là điểm phải cân nhắc kỹ trước khi cho agent chạy shell/file thật trong môi trường sản xuất — không có guardrail sẵn ở tầng model, tự lo phần đó. Là thư viện framework nên vẫn cần biết code Python/LangChain để dùng, không phải no-code.
- **Có nên dùng không:** 8/10 cho ai đang build agent research/coding phức tạp bằng Python và đã quen LangChain — không hợp nếu chỉ cần 1 agent hỏi-đáp đơn giản (dùng LangChain `create_agent` nhẹ hơn là đủ).

## Link
- Repo: https://github.com/langchain-ai/deepagents
- Docs/Demo: https://docs.langchain.com/oss/python/deepagents/overview · https://reference.langchain.com/python/deepagents/
- Bản JS/TS: https://github.com/langchain-ai/deepagentsjs

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Cài: uv add deepagents (hoặc pip install deepagents)
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="openai:gpt-5.5",   # đổi sang model đang dùng thật
    tools=[],                 # gắn tool riêng của Hermes vào đây
    system_prompt="Bạn là trợ lý research cho ABTRIP.",
)
result = agent.invoke({"messages": "Research đối thủ cạnh tranh mảng fast track sân bay"})
```
> ⚠️ Nhớ nguyên tắc "trust the LLM": Hermes phải tự chặn ở tầng tool (vd giới hạn agent chỉ đọc/ghi trong thư mục cho phép), không dựa vào system prompt để agent "tự biết không phá".

### OpenClaw
Không có MCP/connector sẵn — nếu OpenClaw cần trigger 1 Deep Agent Python đã viết, gọi qua subprocess hoặc dựng 1 API endpoint nhỏ bọc quanh `agent.invoke()` rồi gọi HTTP như bình thường.

### Antigravity
```bash
# Cài Deep Agents Code — bản agent code sẵn kiểu Claude Code, chạy terminal, dùng model bất kỳ
curl -LsSf https://langch.in/dcode | bash
```
> ⚠️ Đây là công cụ khác với thư viện `deepagents` (dùng để build agent tuỳ chỉnh) — "Deep Agents Code" là sản phẩm dựng sẵn để code trực tiếp trong terminal, chọn đúng cái cần trước khi cài trên VPS.
