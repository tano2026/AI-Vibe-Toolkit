# Awesome LLM Apps — GitHub Repo

## TL;DR
Kho hơn 100 ứng dụng AI agent/RAG mã nguồn mở, làm sẵn end-to-end, clone về chạy được luôn — từ agent đơn giản tới multi-agent phức tạp, license Apache 2.0 nên clone/sửa/bán lại đều thoải mái. 121k+ star, đang trending top đầu GitHub.

## Repo này dùng để làm gì
Đây không phải 1 tool mà là 1 "chợ template" — mỗi thư mục con là 1 app AI hoàn chỉnh đã test end-to-end: agent đơn (single_agent_apps), multi-agent (multi_agent_apps), agent luôn chạy nền (always_on_agents), agent skills (agent_skills, kiểu tương tự Claude Skills nhưng cho nhiều LLM khác), voice AI agent, RAG app. Cái hay là mỗi app đều có ví dụ cụ thể, không phải code mẫu chung chung — vd "Project Graveyard" (agent tự mổ xẻ vì sao side-project cũ chết), "Insurance Claim Live Agent Team" (xử lý claim bảo hiểm real-time bằng voice), "AI Fraud Investigation Agent". Hỗ trợ nhiều model: Claude, Gemini, GPT, DeepSeek, Llama, Qwen.

## Setup từng bước
1. Clone repo:
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
   ```
2. Duyệt cấu trúc thư mục để tìm app phù hợp nhu cầu — mỗi thư mục con có README riêng với hướng dẫn chạy cụ thể (thường là `pip install -r requirements.txt` + set API key).
3. Đa số app cần `.env` với API key của model tương ứng (Claude/OpenAI/Gemini...).
4. Chạy thử theo README của app cụ thể (khác nhau tuỳ app, không có 1 lệnh chung cho cả repo).
5. Tham khảo tutorial chi tiết hơn tại theunwindai.com (kênh của tác giả) nếu README chưa đủ rõ.

## Ví dụ thực tế
Cần dựng nhanh 1 agent auto-brief tin tức mỗi sáng (tương tự pattern `morning-briefing` đã có
trong kho) → tìm trong `always_on_agents/always_on_hn_briefing_agent/` — có sẵn code đọc Hacker
News tự động và tóm tắt, chỉ cần chỉnh nguồn tin + brand voice thay vì viết từ đầu.

## Lưu ý / Lỗi thường gặp
- Kho quá rộng (100+ app) — không có 1 điểm entry chung, dễ mất thời gian nếu không biết chính
  xác cần loại app nào, nên search theo tên thư mục con thay vì đọc lướt cả repo.
- Chất lượng code giữa các app không đồng đều — 1 số app là proof-of-concept đơn giản, không
  production-ready, cần review kỹ trước khi dùng thật cho khách hàng.
- Một số app cần API trả phí (OpenAI, các dịch vụ voice) mới chạy được đầy đủ tính năng demo.

## Đánh giá cá nhân
- Điểm mạnh: kho tham khảo pattern agent cực rộng, tiết kiệm thời gian research kiến trúc — thay
  vì tự nghĩ cách build 1 loại agent mới, có thể tìm ví dụ tương tự trong đây trước rồi customize.
- Điểm yếu: là "chợ ý tưởng" hơn là sản phẩm hoàn thiện — không nên clone nguyên xi bán cho khách
  mà chưa review/test kỹ, dễ dính bug hoặc thiếu guardrail so với agent tự build theo pattern
  Harness Engineering đã áp dụng trong kho.
- Có nên dùng không: 7/10 — dùng tốt cho việc research nhanh "đã có ai làm agent kiểu này chưa"
  trước khi tự build, không nên coi là nguồn code production trực tiếp.

## Link
- Repo: https://github.com/Shubhamsaboo/awesome-llm-apps
- Docs/Tutorials: https://www.theunwindai.com
