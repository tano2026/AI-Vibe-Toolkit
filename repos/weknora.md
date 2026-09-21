# WeKnora — GitHub Repo

## TL;DR
Platform quản lý tri thức doanh nghiệp mã nguồn mở từ Tencent — biến tài liệu rời rạc thành RAG tra cứu được + agent tự suy luận + Wiki tự cập nhật. Khác llama_index/graphrag (thư viện, tự code) — đây là platform đầy đủ (Web UI/API/CLI), có multi-tenant RBAC sẵn.

## Repo này dùng để làm gì
3 năng lực lõi: RAG Q&A tra cứu nhanh, agent suy luận tự chủ, Wiki tự bảo trì. Ingest đa nguồn (Feishu/GitLab/Notion/Yuque/RSS...), đọc 10+ định dạng file (PDF/Word/ảnh/Excel/XMind), trả lời qua IM (WeCom/Feishu/Slack/Telegram — không có Zalo trực tiếp). Tương thích 20+ LLM provider (OpenAI/DeepSeek/Qwen/Gemini/Ollama...) qua LiteLLM.

⚠️ Không thấy Claude/Anthropic trong danh sách 20+ provider liệt kê trực tiếp — có LiteLLM (bridge đa provider, có thể route qua đó tới Claude) nhưng chưa xác nhận chắc chắn hoạt động mượt, cần tự test.

## Điểm đáng chú ý — Multi-tenant RBAC có sẵn

Enterprise-ready multi-workspace RBAC (ma trận 4 cấp vai trò + quyền sở hữu theo từng resource + audit log riêng từng workspace) — đây đúng khái niệm CORE/TENANT-CONFIG đã thiết kế trong MASTER-TEMPLATE-MANIFEST.md, nhưng WeKnora có implementation thật, chạy được, không chỉ là thiết kế trên giấy.

## Setup từng bước
1. Self-host qua Docker (kiến trúc modular, tự chọn vector DB/storage backend)
2. Cấu hình LLM provider (qua LiteLLM nếu muốn dùng Claude — cần tự verify)
3. Nạp tài liệu qua Web UI hoặc auto-sync từ nguồn đã kết nối (Notion/GitLab...)
4. Dùng CLI (weknora) hoặc RESTful API (~360 endpoint) để tích hợp vào hệ thống khác
5. Có Chrome Extension + Website Embed Widget nếu muốn nhúng vào trang khác

## Ví dụ thực tế
Toàn bộ kho AI-Vibe-Toolkit (857 skill + 7 Pro agent) có thể nạp vào WeKnora làm knowledge base tra cứu — khác llama_index (phải tự code), WeKnora cho sẵn Web UI để Nobitano tự tra cứu trực tiếp không cần viết code, và multi-workspace RBAC sẵn sàng nếu sau này có nhân viên khác cần quyền truy cập giới hạn (đúng nhu cầu khi Tano Agency có thêm người).

## Lưu ý / Lỗi thường gặp
- Nhiều fork trùng mô tả y hệt (649111698, xzho2604, geversite, jjj-n, jacentsao, zlh123123...) — dùng đúng Tencent/WeKnora (tổ chức chính thức, đáng tin hơn cá nhân fork)
- Docs vừa được thêm đầy đủ (PR #2350, 6/8/2026) — còn khá mới, có thể còn thiếu sót
- Gốc từ hệ sinh thái Trung Quốc (Feishu/DingTalk/Tencent IMA là nguồn ingest chính) — phần tích hợp phù hợp VN (Zalo, Gmail workspace VN) chưa có sẵn, cần tự dựng nếu cần

## Đánh giá cá nhân
- Điểm mạnh: platform đầy đủ (không phải chỉ thư viện), multi-tenant RBAC thật — đúng nhu cầu MASTER-TEMPLATE-MANIFEST đang thiết kế; từ Tencent nên có support/bảo trì nghiêm túc
- Điểm yếu: chưa xác nhận rõ tương thích Claude; hệ sinh thái ingest thiên về công cụ Trung Quốc, cần tự nối cho công cụ VN
- Có nên dùng: 7/10 — đáng thử nghiệm cho việc biến kho thành tra cứu qua UI thật, nhưng cần verify LiteLLM→Claude hoạt động tốt trước khi tin dùng chính

## Link
- Repo: https://github.com/Tencent/WeKnora
- Docs: mới thêm, VitePress site — xem trong repo
