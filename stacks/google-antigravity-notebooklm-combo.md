# Google Antigravity + NotebookLM — Combo Tools theo Use Case

> ⚠️ **PHÂN BIỆT TÊN GỌI — ĐỌC TRƯỚC:** "Antigravity" trong file này là **Google
> Antigravity** (antigravity.google — agentic IDE/browser environment của
> Google), **KHÔNG PHẢI** agent "Antigravity" đang chạy trên VPS của Tano
> (Shell/infra manager, xem `agents/ANTIGRAVITY-PLAYBOOK.md`). Hai cái trùng
> tên hoàn toàn ngẫu nhiên. Hermes/OpenClaw đọc file này cần hiểu đây là 1 sản
> phẩm bên thứ 3 của Google, không liên quan tới agent nội bộ cùng tên.

## TL;DR
Combo đang được cộng đồng AI builder gọi là "invisible developer stack": NotebookLM đóng vai chiến lược gia — đọc/tổ chức nguồn tài liệu, ra bản kế hoạch kỹ thuật (PRD) có căn cứ nguồn rõ ràng; Google Antigravity đóng vai người thực thi — nhận PRD đó, tự viết code, chạy lệnh, dựng app thật. Kết nối qua MCP.

## Các tool trong stack
1. **NotebookLM** (notebooklm.google.com) → nghiên cứu có căn cứ nguồn (grounded RAG) — chỉ trả lời dựa trên tài liệu/PDF/URL người dùng nạp vào, có trích dẫn rõ ràng, không bịa từ training data. Vai trò: biến research thô thành PRD/spec kỹ thuật có cấu trúc.
2. **Google Antigravity** (antigravity.google) → agentic IDE chạy trên trình duyệt của Google, có Agent Manager để chạy nhiều task song song, hỗ trợ native MCP server connection. Vai trò: nhận PRD, tự scaffold app, viết code, chạy lệnh, ship ra sản phẩm chạy được.

## Workflow ghép nối
```
Nạp nguồn (tài liệu, note, research) → NotebookLM
        ↓ (hỏi/trò chuyện để làm rõ ý tưởng)
NotebookLM tổng hợp thành PRD/spec kỹ thuật có cấu trúc
        ↓ (kết nối qua MCP — Antigravity chưa có connector NotebookLM
        ↓  cắm sẵn, phải tự cấu hình MCP server thủ công)
Dán/feed PRD vào Google Antigravity
        ↓
Antigravity tự lên kế hoạch, scaffold code, chạy lệnh, verify
        ↓
Sản phẩm chạy được (app/tool/website) — quay lại NotebookLM nếu cần
research thêm cho vòng lặp tiếp theo
```

Điểm quan trọng: **không có connector NotebookLM cắm sẵn trong Antigravity** — đây là điều nhiều bài viral bỏ qua. Phải tự bootstrap MCP server nối 2 bên, không phải bật 1 switch là xong.

## Ví dụ thực tế
Dùng thử cho ý tưởng landing page **Wonder Mart ngành hàng mới**: nạp research thị trường + brief sản phẩm vào NotebookLM, hỏi nó tổng hợp thành PRD (đối tượng, tính năng cần, tone thương hiệu). NotebookLM ra 1 bản spec có trích dẫn rõ nguồn nào nói gì — khác hẳn việc tự gõ thẳng "làm landing page cho tao" vào 1 công cụ code (dễ ra sản phẩm chung chung). Đưa PRD đó qua Antigravity, nó tự dựng landing page có cấu trúc/tone khớp đúng research ban đầu, không cần lặp lại ngữ cảnh nhiều lần.

## Lưu ý / Lỗi thường gặp
- **Không có nút "connect" 1 chạm** — bài viral nói "Google vừa update kết nối 2 tool" nhưng thực chất là qua MCP, người dùng phải tự cấu hình server, xác thực, và tự giới hạn phạm vi quyền — không đơn giản như quảng cáo.
- **NotebookLM chỉ trả lời từ nguồn đã nạp** — nếu không nạp đủ tài liệu, PRD ra sẽ thiếu context, Antigravity build ra sản phẩm generic dù có PRD.
- **Antigravity hiện là sản phẩm free/beta của Google** — chính sách, giới hạn dùng có thể thay đổi, không nên xây quy trình cốt lõi phụ thuộc hoàn toàn vào tool đang trong giai đoạn thử nghiệm.
- **Đừng nhầm với Antigravity agent nội bộ** — nếu ghi note/doc về combo này trong kho hoặc brief cho Hermes, luôn ghi rõ "Google Antigravity" để tránh lẫn với agent VPS.

## Đánh giá cá nhân
- **Điểm mạnh:** Ý tưởng tách vai trò rõ ràng (NotebookLM = nghiên cứu có căn cứ, Antigravity = thực thi) là mô hình hay — giống đúng pattern Collector→Synthesizer mà `SKILL_AGENTIC_FACTORY.md` khuyến nghị cho mọi agent. Free, không cần trả phí để thử.
- **Điểm yếu:** Setup MCP thủ công, không "cắm là chạy" như marketing nói. Cả 2 tool đều của Google, phụ thuộc hệ sinh thái 1 hãng — không tự chủ hạ tầng như cách Tano đang làm với OmniRoute (231 provider độc lập).
- **Có nên dùng không:** 6/10 — hợp để thử nghiệm nhanh 1 ý tưởng cá nhân (landing page, prototype), không nên đưa vào pipeline chính thức của Tano vì phụ thuộc quá nhiều vào 2 sản phẩm cùng 1 hãng đang ở giai đoạn beta.

## Link
- Link tới từng file .md tool liên quan trong /mcps, /repos, /skills:
  - `/mcps/notebooklm-mcp-2026.md` (và các bản NotebookLM MCP khác đã có trong kho)
  - Google Antigravity: chưa có entry riêng trong kho — cân nhắc research thêm nếu cần dùng độc lập, không chỉ trong combo này.
