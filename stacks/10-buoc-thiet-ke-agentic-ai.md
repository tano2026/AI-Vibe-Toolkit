# 10 Bước Thiết Kế Hệ Thống Agentic AI — Combo Tools theo Use Case

## TL;DR
Khung 10 bước đi từ ý tưởng tới triển khai an toàn cho 1 hệ thống Agentic AI, mỗi bước gắn sẵn nhóm công cụ cụ thể nên vừa là quy trình tư duy vừa là danh sách tool để chọn khi build agent thật (không riêng cho Claude, áp được cho bất kỳ stack agent nào).

## Các tool trong stack
1. **Bước 1-2 (Xác định use case + chọn model)** → Notion/Jira/Miro/Lucidchart để làm rõ mục tiêu, OpenAI GPT/Claude/Gemini/Llama/Mistral để chọn model theo khả năng suy luận, context window, chi phí
2. **Bước 3-4 (Hướng dẫn Agent + RAG)** → OpenAI Agents SDK, LangGraph, PydanticAI, Microsoft Agent Framework để định vai/luật nghiệp vụ; Pinecone/Qdrant/Weaviate/Azure AI Search/Elasticsearch để nạp kiến thức ngoài
5. **Bước 5 (Bộ nhớ & trạng thái)** → thiết kế lưu bộ nhớ làm việc, lịch sử hội thoại, trạng thái workflow (không gắn 1 tool cụ thể, tuỳ hạ tầng)
6. **Bước 6 (Công cụ & hành động)** → MCP, REST API, Function Calling, Webhooks, Custom APIs để Agent chạm được hệ thống ngoài
7. **Bước 7 (Lập kế hoạch & điều phối)** → LangGraph, Microsoft Agent Framework, Temporal, CrewAI, n8n để Agent tự phân rã việc và định tuyến task
8. **Bước 8 (Multi-agent chuyên biệt + con người kiểm soát)** → CrewAI, LangGraph, AutoGen (A2A), Microsoft Agent Framework, OPA để phân quyền giữa các sub-agent và chốt phê duyệt của người
9. **Bước 9 (Giám sát hành vi)** → LangSmith, Arize Phoenix, OpenTelemetry, Datadog, Grafana để theo dõi tỷ lệ hoàn thành, hallucination, chi phí
10. **Bước 10 (Triển khai an toàn & mở rộng)** → Docker, Kubernetes, Terraform, HashiCorp Vault, AWS/Azure/GCP cho xác thực, quản lý secret, scaling, audit logging

## Workflow ghép nối
```
B1 Xác định use case → B2 Chọn model → B3 Viết hướng dẫn cho Agent → B4 Nối RAG
→ B5 Thiết kế bộ nhớ/trạng thái → B6 Nối tool & hành động → B7 Xây planner/điều phối
→ B8 Thêm sub-agent chuyên biệt + checkpoint con người → B9 Đánh giá & giám sát hành vi
→ B10 Triển khai an toàn & mở rộng production
```
Nguyên tắc xuyên suốt: mỗi bước sau phụ thuộc dữ liệu bước trước (model đã chọn quyết định cách viết hướng dẫn, RAG đã nối quyết định bộ nhớ cần lưu gì, planner đã có mới nói tới multi-agent). Bỏ bước nào giữa chừng thì các bước sau dễ vỡ.

## Ví dụ thực tế
Áp cho 1 agent nghiên cứu đầu tư (ví dụ trong ảnh gốc): B1 xác định agent cần thu thập dữ liệu, phân tích công ty, tạo báo cáo có cấu trúc → B2 chọn model mạnh cho lập kế hoạch, model nhẹ hơn cho phân loại → B3 viết rule "phải liệt kê nguồn khi báo cáo" → B4 nối RAG để agent truy xuất báo cáo nội bộ trước khi phân tích công ty mục tiêu → B6 cấp quyền gọi API để truy xuất dữ liệu thị trường và lưu kết quả vào DB → B7-B8 dựng vòng lặp Nghiên cứu → Phân tích → Đánh giá → Chuyển cho chuyên gia duyệt nếu phát hiện rủi ro → B9 theo dõi tỷ lệ gọi công cụ thất bại → B10 deploy sau tường xác thực, giới hạn quyền API, bật audit log.

## Lưu ý / Lỗi thường gặp
- Khung này liệt kê rất nhiều tool ở mỗi bước nhưng không phải dùng hết — nó là menu để chọn theo nhu cầu thật, không phải checklist bắt buộc đủ cả 5-6 tool/bước.
- Bước 5 (bộ nhớ & trạng thái) trong ảnh gốc không gắn tool cụ thể nào — dễ hiểu lầm là "chưa cần làm gì", thực ra đây là bước dễ bị bỏ qua nhất khi build agent thật, cần tự thiết kế lưu trữ (Redis, DB, session store...) chứ không có sẵn công cụ đề xuất.
- B8 (multi-agent + kiểm soát con người) và B9 (giám sát) hay bị gộp làm 1 hoặc bỏ qua khi làm nhanh — nhưng đây chính là 2 bước quyết định agent có "chạy được sản phẩm" hay chỉ dừng ở demo.
- Đây là framework tổng quát, không phải 1 tool tải về cài đặt — không có bước "setup" theo nghĩa thông thường, giá trị nằm ở việc dùng làm checklist khi thiết kế agent mới.

## Đánh giá cá nhân
- **Điểm mạnh:** Đủ 10 bước bao trọn vòng đời agent từ ý tưởng tới production, mỗi bước có tool gợi ý cụ thể nên không bị nói suông — rất hợp để dùng làm checklist khi brainstorm 1 agent mới trước khi nhảy vào code.
- **Điểm yếu:** Không đi sâu HOW cho từng bước (vd không nói rõ cách viết instruction Agent thế nào cho tốt), và liệt kê nhiều tool cùng lúc dễ gây rối cho người mới không biết chọn cái nào trước. Bước 5 (bộ nhớ) bị hời hợt nhất trong cả khung.
- **Có nên dùng không:** 7/10 — dùng làm checklist tư duy khi bắt đầu 1 agent mới thì tốt, nhưng cần kết hợp thêm tài liệu chi tiết hơn (vd skill `agentic-factory` trong kho) để biết cách viết từng phần thực tế.

## Link
- Nguồn: infographic từ tác giả @EroraThanh — không tìm được bài gốc có link/text đi kèm, nội dung lấy lại nguyên vẹn từ ảnh.

---

## 🤖 Agent Integration

### Hermes (Python)
Không áp dụng trực tiếp — đây là framework tư duy, không phải API/package gọi được. Hermes dùng khung này gián tiếp: khi Nobitano giao xây 1 agent Python mới, đi theo đúng 10 bước này để quyết định kiến trúc trước khi viết code.

### OpenClaw
Không áp dụng trực tiếp — dùng làm checklist khi thiết kế orchestrator mới cho OpenClaw (vd thêm 1 nhánh xử lý task mới), tham khảo cùng skill `agentic-factory` sẵn có trong kho.

### Antigravity
Không áp dụng trực tiếp — liên quan nhất ở Bước 10 (Docker, Kubernetes, Terraform, Vault) khi Antigravity cần deploy 1 agent mới lên VPS: checklist xác thực, giới hạn quyền, secret management, audit log trước khi đưa vào chạy thật.
