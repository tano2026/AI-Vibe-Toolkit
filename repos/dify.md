# Dify — GitHub Repo

## TL;DR
Production-ready platform build AI app và agent workflow — kết hợp RAG, LLM, tool calling, monitoring trong một platform hoàn chỉnh. 146.7K stars, top 5 repo AI trên GitHub. Dùng khi mày cần deploy AI app cho khách hàng thật, không chỉ prototype.

## Repo này dùng để làm gì
Dify khác Langflow ở chỗ: **production-first**. Không chỉ build workflow mà còn có:
- **LLMOps:** Monitor token usage, latency, error rate của từng AI app
- **Prompt versioning:** A/B test prompt, rollback khi cần
- **RAG pipeline:** Upload doc → chunk → embed → retrieve — có UI quản lý
- **Agent:** Tool calling, multi-step reasoning với nhiều LLM
- **API:** Mọi app tạo ra đều có API endpoint ngay
- **Multi-tenant:** Tạo nhiều workspace cho nhiều team/client

Dify = nơi deploy AI app cho production. Langflow = nơi prototype nhanh.

## Setup từng bước
```bash
# Self-host với Docker Compose (khuyến nghị)
git clone https://github.com/langgenius/dify
cd dify/docker

cp .env.example .env
# Edit .env: SECRET_KEY, database config, API keys

docker compose up -d

# Truy cập: http://localhost/install
# Setup admin account → done

# Hoặc dùng Dify Cloud (free 200 message/ngày)
# cloud.dify.ai
```

**Build chatbot RAG cho tài liệu công ty:**
1. Knowledge → Upload PDF/Word/URL
2. Studio → New App → Chatbot
3. Kéo thả: Knowledge Retrieval → LLM → Answer
4. Publish → lấy API endpoint hoặc embed widget

## Ví dụ thực tế
**AI Assistant cho ABTRIP:**
- Knowledge base: upload 200 file PDF về điểm đến, chính sách, giá tour
- Build chatbot answer câu hỏi khách: "Tour Hà Giang 3 ngày bao nhiêu tiền?"
- Deploy widget lên website ABTRIP
- Monitor: xem câu hỏi nào hay bị AI trả lời sai → cải thiện knowledge base

Không cần backend engineer.

## Lưu ý / Lỗi thường gặp
- Self-host cần ít nhất 4GB RAM — 8GB nếu chạy embedding local
- Vector database mặc định là Weaviate — có thể đổi sang pgvector, Qdrant, Pinecone
- Dify Cloud free tier chỉ 200 message/ngày — self-host nếu traffic cao
- Update version hay breaking change — backup data trước khi update

## Đánh giá cá nhân
- Điểm mạnh: Production-ready thật sự; monitoring LLMOps tốt nhất trong class; RAG pipeline mạnh; API sẵn có; community cực lớn (146K stars)
- Điểm yếu: Nặng hơn Langflow; self-host phức tạp hơn; learning curve với LLMOps concept
- Có nên dùng không: **9/10** — Nếu mày build AI app cho khách hàng thật, Dify là platform tốt nhất hiện tại. Kết hợp Supabase + Dify + Coolify = full AI SaaS stack không cần backend engineer.

## Link
- Repo: https://github.com/langgenius/dify
- Docs: https://docs.dify.ai
- Cloud: https://cloud.dify.ai
