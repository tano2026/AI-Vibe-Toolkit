# System Design Primer — GitHub Repo

## TL;DR
Kho tài liệu mã nguồn mở lớn nhất về thiết kế hệ thống quy mô lớn — 360k sao, 57.5k fork, hoạt động từ 2017 tới nay vẫn được cập nhật liên tục. Không phải tool code, mà là **tài liệu tham khảo** khi thiết kế kiến trúc — đúng lúc cần cho giai đoạn Tano đang chuẩn bị B2B Travel Platform và mở rộng agent pipeline.

## Repo này dùng để làm gì
Tổng hợp có tổ chức mọi khái niệm thiết kế hệ thống lớn: load balancer, caching, database sharding/replication, message queue, CDN, CAP theorem... mỗi mục đều nói rõ **trade-off** (không có giải pháp nào miễn phí, luôn đánh đổi cái gì lấy cái gì). Kèm theo bộ giải pháp mẫu cho các hệ thống kinh điển (thiết kế Pastebin, thiết kế mạng xã hội, thiết kế hệ thống rút gọn URL...) và bộ Anki flashcard để ôn nhanh.

## Setup từng bước
1. Không cần setup — đọc trực tiếp README trên GitHub hoặc clone về đọc offline: `git clone https://github.com/donnemartin/system-design-primer`
2. Nếu cần ôn nhanh khái niệm: import bộ Anki flashcard có sẵn trong repo, dùng spaced repetition để nhớ lâu.
3. Muốn học có định hướng: repo có gợi ý lộ trình theo thời gian (ngắn/trung/dài hạn) tuỳ mức độ chuẩn bị cần thiết.
4. Với nhu cầu thiết kế thật (không phải luyện phỏng vấn): đọc thẳng phần `solutions/system_design/` — mỗi case study có cấu trúc chuẩn: gom yêu cầu → high-level design → đi sâu từng thành phần → bàn bottleneck và cách xử lý.

## Ví dụ thực tế
Áp trực tiếp cho **B2B Travel Platform** đang trong giai đoạn Phase 0: mục `solutions/system_design/` có case study kiểu hệ thống giao dịch (mint) và hệ thống mạng xã hội (social graph) — cấu trúc bàn luận giống hệt câu hỏi Tano sẽ phải trả lời khi chọn kiến trúc NDC aggregator (Duffel) + consolidator: chỗ nào cần cache, chỗ nào cần queue, chỗ nào chấp nhận eventual consistency thay vì strong consistency.

Cũng áp được để review lại kiến trúc `agents/company/hq.db` hiện tại — phần bàn về SQL vs NoSQL, khi nào cần replication, giúp trả lời câu hỏi đang mở "Observability layer cho agent pipelines — thêm `runtime_stage` field vào hq.db" có nên tách bảng hay không.

## Lưu ý / Lỗi thường gặp
- **Đây là tài liệu học, không phải checklist áp dụng máy móc** — mỗi phần đều nói "everything is a trade-off", đọc xong phải tự cân nhắc theo bối cảnh thật, không copy nguyên kiến trúc mẫu vào production.
- Nội dung hướng nhiều tới chuẩn bị phỏng vấn hệ thống lớn (FAANG-style) — với quy mô Tano hiện tại (1 VPS, agent nhỏ), nhiều phần về "hệ thống hàng triệu người dùng" sẽ overkill nếu áp thẳng, cần lọc lại phần phù hợp quy mô thật.
- Không có code chạy được, không có API — thuần văn bản + sơ đồ, không nhầm với 1 framework hay thư viện.

## Đánh giá cá nhân
- **Điểm mạnh:** Tổ chức tốt nhất trong các tài liệu system design miễn phí hiện có, mỗi khái niệm đều có link đào sâu, không lan man. Case study có cấu trúc rõ ràng, học được cách "nói chuyện kiến trúc" mạch lạc — hữu ích khi phải giải thích quyết định kiến trúc cho client B2B Travel Platform.
- **Điểm yếu:** Không cập nhật theo xu hướng agent/AI-infra hiện đại (repo hướng về hệ thống web truyền thống: load balancer, CDN, SQL/NoSQL) — không có phần nào bàn riêng về kiến trúc multi-agent, LLM gateway, hay vector store, những thứ Tano đang cần cho RIO Bot/OmniRoute.
- **Có nên dùng không:** 8/10 làm nền tảng tư duy kiến trúc chung, nhưng cần bổ sung thêm nguồn riêng cho phần AI-agent-infra vì repo này không cover.

## Link
- Repo: https://github.com/donnemartin/system-design-primer
- Docs/Demo: README trong repo có toàn bộ nội dung, không có site riêng

---

## 🤖 Agent Integration

Không áp dụng — đây là tài liệu học (markdown + Anki flashcard), không có API, không có package cài đặt, không chạy được như 1 tool/service. Hermes/OpenClaw/Antigravity không tương tác trực tiếp với repo này; giá trị nằm ở việc **người** đọc để ra quyết định kiến trúc, không phải agent tự động fetch và dùng.
