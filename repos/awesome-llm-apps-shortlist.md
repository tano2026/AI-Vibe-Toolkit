# Shortlist Thực Dùng Được — awesome-llm-apps (175K sao)

## TL;DR
Đã clone toàn bộ repo, lọc qua 13 category / 100+ app. Đây KHÔNG phải liệt kê hết — chỉ giữ
lại app khớp trực tiếp domain thật của Tano Agency (ABTRIP, Wonder Mart, Tano Cafe, GMSP, vận
hành nội bộ). Mỗi app đều là DEMO/TEMPLATE học kiến trúc, không phải sản phẩm production —
dùng để tham khảo cách chia agent + luồng dữ liệu, luôn cần thay data source thật + bảo mật
trước khi đưa vào production.

## Shortlist theo domain

### CSKH (ABTRIP + Wonder Mart)
- **`voice_ai_agents/customer_support_voice_agent`** — voice agent trả lời CSKH real-time.
  Tham khảo cho ý tưởng "voice FAQ" tại quầy Fast Track (khách hỏi trực tiếp bằng giọng nói
  thay vì gõ chat) — khác `ai-chatbot-react-starter.md` đã có (chỉ text).
- **`advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent`** — phát hiện giao dịch
  bất thường. Liên quan trực tiếp mục #6 (Payment) trong `kiem-tra-bao-mat-truoc-deploy.md` —
  tham khảo cách 1 agent tự động soi giao dịch lạ cho Wonder Mart.

### Sales & Outreach
- **`advanced_ai_agents/multi_agent_apps/ai_email_gtm_outreach_agent`** — multi-agent viết +
  gửi email outreach theo GTM. Áp dụng cho Sales role tìm đối tác B2B mới cho ABTRIP.
- **`advanced_ai_agents/single_agent_apps/ai_meeting_agent`** — agent chuẩn bị brief trước
  meeting (research đối tác, tóm tắt lịch sử trao đổi). Hữu ích cho CEO trước khi gặp đối tác
  ground handling B2B mới — nối với `sales:call-prep` skill đã có sẵn trong hệ thống.

### Nghiên cứu & Vận hành nội bộ
- **`advanced_ai_agents/multi_agent_apps/product_launch_intelligence_agent`** — multi-agent
  phân tích trước khi launch sản phẩm/tính năng mới. Dùng khi ABTRIP ra tính năng mới hoặc
  Wonder Mart launch sản phẩm mới — kiểm tra thị trường/đối thủ tự động trước khi công bố.
- **`mcp_ai_agents/multi_mcp_agent_router`** — code mẫu THẬT cho pattern "1 agent điều phối,
  nhiều specialist agent mỗi cái nối 1 MCP riêng". Đây là ví dụ code cụ thể cho đúng mô hình
  đã thiết kế trong bảng "Phân luồng theo ROLE" ở `OPENCLAW-PLAYBOOK.md` — đáng đọc code thật
  để đối chiếu cách implement.
- **`always_on_agents/always_on_hn_briefing_agent`** — pattern agent chạy nền định kỳ, lọc tin
  tức thành brief hàng ngày. Tham khảo kiến trúc cho việc mở rộng RIO Bot thành research luôn
  chạy nền theo lịch, không chỉ chờ lệnh Telegram.
- **`agent_skills/project-graveyard`** — agent skill đọc git history, tìm hiểu vì sao side
  project cũ bị bỏ dở. Vui nhưng thực dụng — có thể chạy thử soi lại các domain/thử nghiệm cũ
  của Tano Agency đã ngừng (nếu có) để rút bài học trước khi bắt đầu domain mới.

### HR & Tài chính (bổ sung cái đã có)
- **`advanced_llm_apps/resume_job_matcher`** — matching CV với JD tự động. Bổ sung cho
  `roles/hr-admin.md` khi tuyển nhiều vị trí cùng lúc (ca trực Fast Track, nhân viên Tano Cafe).
- **`advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent`** +
  **`generative_ui_agents/ai-financial-coach-agent`** (bản có UI dashboard) — góc nhìn khác so
  với `tu-duy-tai-chinh-phat-trien-ban-than.md` đã có, bản này có UI trực quan hơn, có thể tham
  khảo cách hiển thị dashboard tài chính cá nhân nếu muốn làm giao diện thay vì chỉ chat.

### RAG (nếu cần build knowledge base thật cho ABTRIP FAQ)
- **`rag_tutorials/`** — 18 tutorial RAG khác nhau (agentic RAG, hybrid search, corrective RAG,
  local RAG chạy Ollama...). Nếu sau này `ai-chatbot-react-starter.md` cần nâng cấp từ "chatbot
  không biết gì" lên "chatbot biết data thật của ABTRIP" (giá dịch vụ, FAQ đầy đủ) — đây là nơi
  tham khảo kiến trúc RAG phù hợp, không phải tự nghĩ từ đầu.

## Những gì KHÔNG liên quan (bỏ qua, không cần xem)
Game-playing agents (chess/tic-tac-toe), LLM fine-tuning tutorials, Cursor AI experiments,
chat-with-tarots, health/fitness/medical imaging agents, resume các domain hoàn toàn không
khớp business Tano Agency (aviation/F&B/e-commerce/content) — bỏ qua để đỡ tốn thời gian đọc.

## Đánh giá cá nhân
- Điểm mạnh: kho khổng lồ nên gần như domain nào cũng có ít nhất 1 template tham khảo kiến
  trúc; code thật, chạy được, không phải chỉ lý thuyết.
- Điểm yếu: MỌI app đều là demo — khoảng cách tới production luôn cần: thay API key demo bằng
  data source thật, thêm bảo mật, thêm rate limiting, test kỹ.
- Có nên dùng không: 8/10 làm "thư viện tham khảo kiến trúc" — tra cứu khi cần ý tưởng cho 1
  bài toán cụ thể, không phải để deploy nguyên xi bất kỳ app nào trong này.

## Link
- Repo tổng: `repos/awesome-llm-apps.md`
- Deep-dive travel agent riêng: `repos/ai-travel-agent-templates.md`
