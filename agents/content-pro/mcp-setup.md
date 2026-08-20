# MCP Setup — Content Pro

Danh sách MCP/tool cần thiết + lý do + cách bật.

## Bắt buộc

| Tool | Lý do | Cách bật |
|---|---|---|
| `web_search` | Research chủ đề/trend khi xây Pillar/Cluster cho brand mới | Có sẵn mặc định trong Claude.ai |
| `vidIQ MCP` | Phân tích kênh YouTube/TikTok/Instagram thật (view/CTR/retention) khi audit content cũ hoặc nghiên cứu đối thủ | Đã kết nối sẵn trong hệ thống hiện tại (dùng chung với Research Analytics Pro) |

## Khuyến nghị (tăng chất lượng, không bắt buộc)

| Tool | Lý do | Cách bật |
|---|---|---|
| `Airtable MCP` | Dựng tracker Pillar/Cluster + checklist phân phối + trạng thái editorial workflow | Cần base `company-hq` (đã có trong roadmap hạ tầng chung, chưa setup xong) |
| `x-research-skill` | Pulse chủ đề đang hot trên X/Twitter khi research trend cho pillar mới | Có sẵn trong Capability Map Research Analytics Pro, dùng chung được |
| `Postiz MCP` | Nếu muốn tự động hoá 1 phần khâu lên lịch đăng (hiện `content-distribution-system` mới dừng ở checklist thủ công) | Xem `skills/postiz/postiz` trong kho nếu cần tích hợp sâu hơn |

## Không cần cho Content Pro (khác Research Analytics Pro)

- Không cần Firecrawl/Brave Search MCP chuyên sâu — Content Pro không tự nghiên cứu thị trường sâu như Research Pro, chỉ cần web_search cơ bản cho trend/chủ đề
- Không cần MarkItDown — trừ khi cần đọc tài liệu brand cũ (PDF brand guideline...) để rút insight

## Lưu ý khi thiếu tool

- Thiếu Airtable → dùng Google Sheets tạm, hoặc theo dõi thủ công qua checklist trong chat — không dừng vận hành chỉ vì thiếu tracker tự động
- Thiếu vidIQ (nếu OMC/nền tảng khác không có sẵn) → `content-distribution-system` audit refresh vẫn chạy được bằng đánh giá định tính (đọc lại content, nhận xét bằng mắt), chỉ là không có số liệu chính xác để so sánh
