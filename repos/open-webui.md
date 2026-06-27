# Open WebUI — GitHub Repo

## TL;DR
Giao diện web đẹp, self-hosted để chạy Ollama và mọi LLM local — thay thế ChatGPT UI hoàn toàn. 143K stars. Cài một lần, dùng mãi, không tốn subscription.

## Repo này dùng để làm gì
Nếu mày đang chạy Ollama (LLM local) mà chỉ có terminal — Open WebUI cho mày giao diện như ChatGPT nhưng:
- Chạy 100% local, không gửi data ra ngoài
- Support Ollama + OpenAI API + bất kỳ OpenAI-compatible endpoint
- Multi-user: tạo account cho cả team, mỗi người có history riêng
- RAG built-in: upload tài liệu → chat với nó ngay
- Image generation, voice input, web search tích hợp
- Model management: pull/delete model Ollama từ UI

## Setup từng bước
```bash
# Cần có Ollama trước
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.2  # hoặc model mày muốn

# Cài Open WebUI bằng Docker
docker run -d -p 3000:8080   --add-host=host.docker.internal:host-gateway   -v open-webui:/app/backend/data   --name open-webui   --restart always   ghcr.io/open-webui/open-webui:main

# Truy cập: http://localhost:3000
# Lần đầu: tạo admin account
```

**Kết nối OpenAI API song song:**
Vào Settings → Connections → thêm OpenAI API key → dùng cả GPT-4 lẫn Ollama local trong cùng một UI.

## Ví dụ thực tế
**Setup team AI internal cho doanh nghiệp:**
1. Deploy Open WebUI trên VPS nội bộ
2. Kết nối Ollama chạy Llama 3.2 local (không tốn API)
3. Upload tài liệu công ty → RAG index tự động
4. Cả team chat với AI biết về quy trình nội bộ, không lo data leak ra OpenAI

Chi phí: $0/tháng API (dùng local model), chỉ tốn VPS.

## Lưu ý / Lỗi thường gặp
- Cần GPU để chạy local model nhanh — CPU chạy được nhưng chậm
- Docker volume quan trọng — không có `-v` thì mất data khi restart container
- Update thường xuyên: `docker pull ghcr.io/open-webui/open-webui:main` rồi restart
- Port 3000 hay conflict với app khác — đổi sang 3001 nếu cần

## Đánh giá cá nhân
- Điểm mạnh: UI đẹp ngang ChatGPT; multi-user; RAG built-in; support mọi LLM; active development cực mạnh
- Điểm yếu: Nặng nếu chạy full stack local; cần Docker; một số feature beta còn bug
- Có nên dùng không: **9/10** — Must-have nếu mày dùng Ollama. Thay ChatGPT hoàn toàn cho use case không cần internet.

## Link
- Repo: https://github.com/open-webui/open-webui
- Docs: https://docs.openwebui.com
