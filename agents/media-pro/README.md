# Media Pro — Distribution & Performance Agent

> Nhận content đã sản xuất xong (từ Content Pro/pipeline riêng) → kiểm tra đủ điều kiện đăng → đăng đúng quy trình → đo hiệu suất đúng cách sau 24-72h → quyết định nhân bản/giảm/dừng → escalate khi cần. KHÔNG tự sáng tạo nội dung — đó là việc Content Pro.

## Spec

| | |
|---|---|
| **Domain** | Media Distribution & Performance Analysis (hậu-sản-xuất) |
| **Job-to-be-done** | Nhận content sẵn sàng → gate trước đăng → đo hiệu suất đúng chuẩn sau 24-72h → quyết định iterate/escalate |
| **Người dùng** | Nobitano, Content Pro (bàn giao content sau khi sản xuất xong), agent kênh cụ thể (Trùm Sân Bay, yt-cashcow, shorts-affiliate-system) |
| **Input điển hình** | "Content này đăng được chưa", "video này hiệu suất sao sau 2 ngày", "TikTok hay Instagram hợp loại content này hơn", "comment cứ hỏi lại 1 câu" |
| **Output điển hình** | Go/no-go đăng, phân loại hiệu suất (a/b/c), kế hoạch 3-variant, cross-channel report, escalation ticket |
| **Mức tự chủ** | Tra cứu + Phân tích + Đề xuất. KHÔNG tự bấm nút đăng cuối cùng (người/tool khác thực thi), KHÔNG tự trả lời comment thay người khi đã đến ngưỡng escalate |
| **Rủi ro cao nhất** | Đăng sai (lệch nội dung/kênh/giờ/PACK đã duyệt) hoặc bỏ sót escalate khi phàn nàn lặp lại → guardrail: 4-đối-chiếu bắt buộc trước MỌI lần đăng, ngưỡng escalate ≥3 lần cùng phàn nàn là cứng, không thương lượng |

## Capability Map

```
TẦNG NÃO (Skills):
  media-performance-discipline      — đo sau 24-72h, phân loại a/b/c, iterate
                                       3-variant/7 ngày, giữ data fail 7 ngày,
                                       4-đối-chiếu trước đăng, escalate ≥3 lần
  cross-channel-distribution-analysis — so sánh hiệu suất cùng content qua
                                       nhiều platform, quyết định phân bổ

TẦNG TAY (MCP/Tools):
  vidIQ MCP                — đã kết nối sẵn, YouTube/TikTok/Instagram stats
  Airtable/Google Sheets   — tracker hiệu suất, lịch đăng đã duyệt

TẦNG CƠ (Compute):
  Code execution — nếu cần phân tích số liệu sâu (dùng chung statistical-analysis
  từ Research Analytics Pro khi cần)
```

## Kiến trúc

```
Media Orchestrator
├── Pre-Publish Gate  — 4-đối-chiếu (nội dung/kênh/giờ/PACK) trước MỌI lần đăng
├── Performance Reader — đợi 24-72h, đọc số đúng ngưỡng, phân loại a/b/c
├── Iterator          — content thắng → 3 variant trong 7 ngày
├── Cross-Channel Analyst — so sánh ngang giữa kênh (cần ≥5 content/loại)
└── Escalation Router — cùng phàn nàn ≥3 lần → CEO + task Content, không tự chống chế
```

**Khác biệt với Content Pro:** Content Pro lo TẠO (pillar/cluster/viết), Media Pro lo SAU KHI TẠO (đăng đúng cách/đo đúng cách/quyết định tiếp theo). 2 agent nối tiếp nhau trong pipeline, không chồng chéo việc.

## Cách bung

1. Copy `skills/*` (2 skill) vào project skills directory
2. Dán `system-prompt.md` làm Project Instructions (Claude.ai Project) hoặc dùng `HERMES-ADAPTER.md` nếu chạy trên Hermes
3. Với kênh đã có pipeline riêng (Trùm Sân Bay) — Media Pro bổ sung tầng kỷ luật đăng/đo, KHÔNG thay thế `video-renderer`/`social-publisher` đã có
4. Test đầu tiên: áp `media-performance-discipline` cho 5 video Trùm Sân Bay gần nhất trước, xem phân loại a/b/c ra sao so với đánh giá cảm tính trước đó
