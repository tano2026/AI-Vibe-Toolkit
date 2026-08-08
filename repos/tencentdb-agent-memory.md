# TencentDB Agent Memory (Tencent) — GitHub Repo

## TL;DR
Hệ thống bộ nhớ dài hạn 4 tầng cho AI agent, chạy local hoàn toàn (SQLite + sqlite-vec, zero dependency ngoài), có sẵn plugin npm cho **OpenClaw** và Docker image cho **Hermes** — 2 cái tên xuất hiện y hệt tên 2 runtime đang dùng trong hệ thống Tano Agency. 17.9K sao (tăng rất nhanh), Tencent chính chủ.

## ⚠️ Cần xác minh trước khi dùng: đây có phải cùng "Hermes"/"OpenClaw" đang dùng không?
Repo này liệt kê hỗ trợ trực tiếp: "**OpenClaw, Hermes, Claude Code, CodeBuddy**" như các framework/runtime đã có tên riêng trong hệ sinh thái — không phải Tencent tự đặt tên trùng tình cờ. Có 2 khả năng:
1. "OpenClaw"/"Hermes" là tên **framework mã nguồn mở phổ biến** đã tồn tại trong cộng đồng agent, và hệ thống Tano Agency đang dùng đúng 2 framework đó (đặt tên theo chuẩn chung).
2. Chỉ là trùng tên ngẫu nhiên với 2 cái tên tự đặt riêng cho `agent-core`/orchestrator của Tano Agency.

**Cần Nobitano/Antigravity xác minh trực tiếp** — nếu là (1), đáng cân nhắc dùng lại/tích hợp
framework gốc thay vì tiếp tục tự viết `agent-core` từ đầu; nếu là (2), bỏ qua phần tích hợp
sẵn, chỉ dùng như 1 memory backend độc lập.

## Repo này dùng để làm gì
Khác cách lưu trữ "băm nhỏ mọi thứ vào 1 vector store phẳng rồi search mù" của nhiều memory
system khác, TencentDB Agent Memory dùng **memory layering** (4 tầng, từ raw conversation tới
persona tổng hợp) + **symbolic memory** (không phải embedding thuần, có cấu trúc đọc được):
- **L2 Scenario** — file Markdown thuần, mở ra đọc được trực tiếp
- **L3 Persona** — `persona.md`, truy ngược lại đúng Scenario nào sinh ra nó
- **Task canvas ngắn hạn** — dạng Mermaid diagram, người và agent đều đọc được
- Mọi thứ nối bằng `result_ref`/`node_id` — khi recall sai, debug được bằng cách đi ngược chuỗi
  "Persona → Scenario → Atom → Conversation" tới tận gốc, KHÔNG phải dò mù qua điểm vector score
  như đa số memory system khác (đây là điểm khác biệt lớn nhất, giải quyết đúng vấn đề "recall
  sai không biết sai ở đâu").

4 loại tài sản bộ nhớ tái sử dụng: **Chat Memory** (hội thoại), **Skill** (kỹ năng đã học),
**LLM-Wiki** (tài liệu tự sinh có link graph), **Code-Graph** (index symbol/file/call
relationship của codebase — tự động khi import repo).

Retrieval: hybrid BM25 + vector + RRF (Reciprocal Rank Fusion) — không chỉ dựa thuần vector
similarity.

## Setup từng bước
```bash
git clone https://github.com/Tencent/TencentDB-Agent-Memory
# Cài theo hướng dẫn "Full Installation Guide" trong repo — có bản one-click deploy
# Memory Core + Hub + Proxy
```
Mặc định local (SQLite + sqlite-vec), có backend optional Tencent Cloud Vector Database
(TCVDB) nếu cần scale lớn hơn. Toàn bộ artifact bộ nhớ nằm ở `~/.openclaw/memory-tdai/` — mở
thư mục ra xem trực tiếp được, không phải hộp đen.

## Ví dụ thực tế
Nếu xác minh đúng là framework OpenClaw thật đang dùng — import toàn bộ conversation lịch sử
+ codebase kho AI-Vibe-Toolkit vào, CodeGraph tự index symbol/file/call relationship, LLM-Wiki
tự sinh tài liệu có link graph từ các file `.md` đã có — agent mới không phải "học lại từ đầu"
project mỗi lần, tiết kiệm đúng chi phí "mỗi agent đều mất công học lại" đã ghi nhận trong
`UNIFIED-ARCHITECTURE.md`.

## Lưu ý / Lỗi thường gặp
- **License "Other" (NOASSERTION)** — KHÔNG phải MIT/Apache rõ ràng như phần lớn repo khác
  trong kho. Đọc kỹ điều khoản trước khi dùng thương mại, khác hẳn `supermemory` (MIT) đã có.
- CodeGraph hiện ưu tiên repo public HTTPS — hỗ trợ private repo/SSH credential "đang hoàn
  thiện", chưa chắc dùng ngay được với repo private của Tano Agency.
- Memory routing (tự động chọn tầng nào để lưu/lấy) "vẫn đang lặp lại" theo chính README —
  chưa hoàn toàn tự động, có thể cần gán tay 1 số tác vụ.
- **Trùng phạm vi với `repos/supermemory.md` đã có trong kho** — cả 2 đều là memory engine hỗ
  trợ sẵn Hermes + OpenClaw. Không nên cài cả 2 cùng lúc cho cùng 1 mục đích — chọn 1, test thử
  trước khi cam kết.

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc debug-được (không phải hộp đen vector), Tencent chính chủ nên bảo trì
  dài hạn đáng tin hơn dự án cá nhân, CodeGraph tự index codebase là tính năng độc đáo
  `supermemory` không có.
- Điểm yếu: license không rõ ràng bằng MIT; còn vài phần "đang hoàn thiện" (private repo,
  auto-routing); trùng lặp chức năng với supermemory đã chọn trước đó.
- Có nên dùng không: 7/10 — **việc đầu tiên cần làm không phải cài, mà là xác minh câu hỏi
  "OpenClaw/Hermes ở đây có phải framework đang dùng không"** — câu trả lời đó quyết định toàn
  bộ giá trị của repo này với Tano Agency.

## Link
- Repo: https://github.com/Tencent/TencentDB-Agent-Memory (mirror: TencentCloud/TencentDB-Agent-Memory)
- So sánh: `repos/supermemory.md` (memory engine khác đã có, MIT license, cũng hỗ trợ Hermes+OpenClaw)
