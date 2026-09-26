# Langfuse — GitHub Repo

## TL;DR
Nền tảng quan sát/trace LLM mã nguồn mở (MIT), tự host miễn phí hoàn toàn — có tích hợp CHÍNH THỨC riêng cho TypeSafe Jev (trace từng quyết định Choice/Score/Noul), không phải tool quan sát chung chung phải tự nối.

## Repo này dùng để làm gì
Mỗi lệnh gọi LLM/Jev = 1 span, chuỗi lệnh gọi = 1 trace — thấy được bước nào chậm, tốn bao nhiêu tiền, model nào đang được chọn. Tự host bằng Docker Compose, dashboard Next.js. 100+ tích hợp sẵn (Anthropic, LangChain, LiteLLM... và TypeSafe Jev).

## Điểm quan trọng nhất — tích hợp chính thức với Jev

```
docs chính thức: langfuse.com/integrations/model-providers/typesafe-js
Bọc systemOne() (lệnh gọi Jev) trong observe() → mọi quyết định Jev
(Choice/Score/Noul + confidence) tự động hiện trong dashboard Langfuse
```

Kết hợp với `hermes-jev-skills` (shadow mode) — dùng Langfuse để XEM Jev quyết định gì trong lúc chạy shadow, trước khi tin dùng thật. Đây chính là công cụ còn thiếu để "shadow mode" có ý nghĩa thực sự (không chỉ ghi log thô, mà thấy được dashboard trực quan).

## Setup từng bước (self-host, Docker Compose)
1. `mkdir langfuse-local && cd langfuse-local`
2. Tải `docker-compose.yml` từ repo chính thức Langfuse
3. Set `DATABASE_URL` (Postgres) — v4 tách trace storage sang ClickHouse
4. `docker compose up -d`
5. Cài SDK: `pip install langfuse` (Python, bắt buộc **v4 trở lên**, bản cũ v2/v3 không nhận trace mới sau 16/11/2026)
6. Set `LANGFUSE_HOST=http://localhost:3000` (hoặc IP VPS nếu deploy trên Antigravity)
7. Dùng decorator `@observe` bọc quanh function cần trace

## Ví dụ thực tế
Deploy Langfuse trên cùng VPS đã chạy Postiz (Antigravity quản lý) — Hermes gọi Jev qua `hermes-jev-skills`, mọi quyết định tự động hiện trong Langfuse dashboard. Nobitano xem trực tiếp "Jev vừa chọn model nào, confidence bao nhiêu, tốn bao nhiêu tiền" mà không cần đọc log thô.

## Lưu ý / Lỗi thường gặp
- **Deadline quan trọng: 16/11/2026** — API ingestion cũ (v2/v3 SDK) ngừng nhận trace mới trên Langfuse Cloud sau ngày này. Self-host thì tự quyết định thời điểm, nhưng nên cài thẳng v4 ngay từ đầu, tránh phải nâng cấp gấp
- Self-host full-stack (Postgres + ClickHouse + MinIO) là cách DUY NHẤT được hỗ trợ chính thức tính tới 5/2026 — chưa có bản nhẹ hơn
- Không cần Kubernetes cho quy mô nhỏ — Docker Compose đủ dùng, Kubernetes/Helm chỉ cần khi lên production quy mô lớn

## Đánh giá cá nhân
- Điểm mạnh: mã nguồn mở thật (MIT), tự host free hoàn toàn không giới hạn, tích hợp Jev chính thức — đúng công cụ còn thiếu để shadow mode có ý nghĩa
- Điểm yếu: setup self-host cần Docker Compose + Postgres + ClickHouse — không đơn giản như 1 dòng lệnh, cần thời gian dựng
- Có nên dùng: 8/10 — đáng dựng cùng đợt với `hermes-jev-skills`, không tách rời 2 việc

## Link
- Repo: https://github.com/langfuse/langfuse
- Docs tích hợp Jev: langfuse.com/integrations/model-providers/typesafe-js
- Self-hosting guide: langfuse.com/self-hosting

---

## 🤖 Agent Integration

### Hermes (Python)
```python
from langfuse import observe

@observe()
def call_jev_via_hermes(task):
    # Logic gọi hermes-jev-skills ở đây — tự động được trace
    pass
```

### Antigravity
```bash
# Deploy cùng VPS đã chạy Postiz
git clone https://github.com/langfuse/langfuse /opt/langfuse
cd /opt/langfuse && docker compose up -d
```
