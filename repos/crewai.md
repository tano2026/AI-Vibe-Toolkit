# CrewAI — GitHub Repo

## TL;DR
Framework Python đa-agent viết từ đầu, không dựa trên LangChain — 54k+ star, cho phép ghép nhiều AI agent có vai trò riêng (Researcher, Writer, Reviewer...) làm việc chung như 1 đội (Crew), hoặc dựng luồng sự kiện có kiểm soát chặt (Flow) khi cần độ chính xác cao hơn tính tự chủ.

## Repo này dùng để làm gì
2 cách build chính: **Crews** — mỗi agent có role/goal/backstory riêng, tự thảo luận & chia việc theo vai (hợp cho task cần sáng tạo/tự chủ như research, viết nội dung); **Flows** — kiểm soát luồng chạy theo event, gọi model đơn lẻ hoặc nhúng cả Crew vào giữa (hợp cho pipeline cần đúng thứ tự, ít "lang thang"). Hỗ trợ sẵn MCP và A2A (Agent-to-Agent) để nối với hệ agent khác.

## Setup từng bước
1. Cài:
   ```bash
   pip install crewai
   pip install duckduckgo-search   # optional, nếu agent cần search web
   ```
2. Định nghĩa agent + task + crew (ví dụ tối thiểu):
   ```python
   from crewai import Agent, Task, Crew

   researcher = Agent(role="Researcher", goal="Tìm thông tin thị trường",
                       backstory="Chuyên gia phân tích ngành du lịch")
   task = Task(description="Research đối thủ fast track sân bay tại VN",
               agent=researcher)
   crew = Crew(agents=[researcher], tasks=[task])
   result = crew.kickoff()
   ```
3. Muốn kiểm soát chặt luồng chạy (Flow) thay vì để agent tự do thảo luận — dùng `@start`, `@listen` decorator của CrewAI Flows, có thể nhúng cả Crew vào 1 bước trong Flow.
4. Học nhanh miễn phí tại learn.crewai.com (đã có 100k+ dev được cấp chứng nhận qua khoá học này).

## Ví dụ thực tế
Dựng 1 crew nghiên cứu thị trường cho ABTRIP: Agent "Researcher" thu thập tin đối thủ, Agent "Analyst" phân tích số liệu, Agent "Writer" tổng hợp báo cáo — 3 agent tự thảo luận, chia việc theo role đã định nghĩa, `crew.kickoff()` một lần là chạy hết pipeline, trả về báo cáo cuối.

## Lưu ý / Lỗi thường gặp
- Số liệu "5K+ star", "45.9K+ star", "54.2K+ star" xuất hiện ở các bài khác thời điểm khác nhau — kiểm tra lại số star thật trên GitHub trước khi trích dẫn, vì repo tăng rất nhanh.
- Dễ nhầm nên dùng Crews hay Flows: Crews hợp khi muốn agent tự chủ quyết định (rủi ro là kết quả có thể "lang thang" ngoài mong đợi), Flows hợp khi cần chắc chắn thứ tự chạy đúng — chọn nhầm dễ gây khó debug về sau.
- Được build độc lập với LangChain nhưng vẫn nối được (dùng LangChain cho phần tool/RAG, CrewAI cho phần điều phối agent) — không phải chọn 1 trong 2, có thể dùng chung.
- Production reliability không tự động có sẵn — framework chỉ là lớp điều phối, độ ổn định thật phụ thuộc model + tool cấu hình bên trong, cần tự thêm retry/cost ceiling/observability khi đưa vào chạy thật.

## Đánh giá cá nhân
- **Điểm mạnh:** Mô hình "vai trò + đội" (Crews) rất trực quan, dễ tưởng tượng khi thiết kế agent mới — không cần hiểu LangGraph. Có cả 2 chế độ tự chủ (Crews) và kiểm soát chặt (Flows) trong cùng 1 framework, community/docs rất lớn (100k+ dev đã học qua khoá miễn phí).
- **Điểm yếu:** Đúng như mọi multi-agent framework khác, "demo chạy tốt" không đồng nghĩa "production ổn định" — cần tự lo phần retry/cost/observability. Documentation focus/gọn nhưng đôi khi thiếu chi tiết so với LangChain (theo nhận xét từ nhiều bài so sánh).
- **Có nên dùng không:** 8/10 cho ai cần dựng nhanh 1 hệ đa-agent theo vai trò (research, content, sale) mà không muốn học LangGraph — 7/10 nếu cần kiểm soát cực chặt từng bước (khi đó Flow của CrewAI vẫn ổn nhưng LangGraph trần có thể linh hoạt hơn).

## Link
- Repo: https://github.com/crewAIInc/crewAI
- Docs/Demo: https://docs.crewai.com · https://learn.crewai.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Cài: pip install crewai
from crewai import Agent, Task, Crew

def run_crew(role, goal, backstory, task_description):
    agent = Agent(role=role, goal=goal, backstory=backstory)
    task = Task(description=task_description, agent=agent)
    crew = Crew(agents=[agent], tasks=[task])
    return crew.kickoff()
```
> ⚠️ Cần cấu hình API key model (OpenAI/Anthropic/...) qua biến môi trường trước khi `kickoff()`, không truyền trực tiếp trong code.

### OpenClaw
Không có MCP/connector sẵn cho riêng CrewAI — nếu OpenClaw (Node.js) cần trigger 1 crew Python đã viết, gọi qua subprocess hoặc bọc quanh 1 API endpoint nhỏ (FastAPI/Flask) rồi gọi HTTP bình thường.

### Antigravity
```bash
# Cài môi trường Python cho crew chạy trên VPS
python3 -m venv .venv && source .venv/bin/activate
pip install crewai
```
> ⚠️ Nếu crew cần search web, nhớ cài thêm tool tương ứng (`duckduckgo-search` hoặc tool khác) và whitelist domain cần thiết trong network policy của VPS.
