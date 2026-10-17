# HANDOVER — OPC `trum-san-bay-opc`

> **DEMO dựng từ thiết kế NHÁP chưa duyệt (agents/trum-san-bay/OPC-DESIGN-NOTES.md, dừng sau Phần 2 trên 5 phần). Không phải kế hoạch triển khai, chưa chạy gì.**

> File này là KHUNG. `tools/agent_factory.py ban-giao` điền phần giữa hai dấu `BAN-GIAO` và đóng gói kèm checksum.
> Phần ngoài hai dấu do con người viết.

## Tóm tắt

- **OPC:** Trùm Sân Bay (`trum-san-bay-opc`)
- **Nguồn doanh thu / kênh:** affiliate, dich-vu / facebook, zalo, instagram
- **Gói mở rộng:** tai-chinh, doi-tac
- **Chủ sở hữu (CEO):** CHƯA CÓ — hỏi CEO
- **Ngày dựng:** 2026-10-17

## Cách chạy

1. Điền các mục còn trống (danh sách tự động ở phần `BAN-GIAO`).
2. Dựng Airtable `company-hq` theo `airtable-schema.json`.
3. Dựng kênh lệnh CEO (Telegram CEO Bot) và nối với Hermes (agent `ceo`). Chi tiết vessel: `agents/HERMES-GUIDE.md`, `agents/OPENCLAW-GUIDE.md`.
4. Bật theo `PHASES.md`, từng pha một, mỗi bộ phận hai tuần `draft_only` đầu.
5. Lệnh khởi chạy cụ thể: CHƯA CÓ — hỏi CEO (phụ thuộc môi trường cài).

## Biến môi trường cần có (chỉ TÊN)

Tên đề xuất, khớp lại với mã thật khi dựng. Giá trị nằm ngoài kho. Mỗi khách/OPC dùng khoá và tài khoản riêng.

| Tên biến | Dùng cho | Nguồn của tên | Ai tạo / ai đổi |
|---|---|---|---|
| `AIRTABLE_TOKEN` | Truy cập Airtable company-hq | agents/company/COORDINATION-v2.md | Con người; đổi/xoay là L3 |
| `AIRTABLE_BASE_HQ` | Định danh base company-hq (cấu hình) | agents/company/COORDINATION-v2.md | Con người; đổi/xoay là L3 |
| `LLM_API_KEY` | Khoá LLM/OmniRoute cho agent (tên chung; khớp lại theo router thật) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `TELEGRAM_BOT_TOKEN` | CEO Bot: kênh lệnh và duyệt | đề xuất của công cụ; kênh Telegram theo agents/README.md | Con người; đổi/xoay là L3 |
| `TELEGRAM_CHAT_ID_CEO` | Chỉ nhận lệnh từ chat của CEO (cấu hình, không bí mật) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `FB_PAGE_ACCESS_TOKEN` | Đăng bài và đọc bình luận Facebook Page | đề xuất của công cụ; agents/trum-san-bay/deploy-checklist.md ghi cần Page Access Token | Con người; đổi/xoay là L3 |
| `ZALO_APP_ID` | Zalo OA | agents/company/SECURITY-WALL.md | Con người; đổi/xoay là L3 |
| `ZALO_SECRET_KEY` | Zalo OA | agents/company/SECURITY-WALL.md | Con người; đổi/xoay là L3 |
| `ZALO_ACCESS_TOKEN` | Zalo OA | agents/company/SECURITY-WALL.md | Con người; đổi/xoay là L3 |
| `IG_USER_ID` | Định danh tài khoản Instagram Business (không phải bí mật nhưng là cấu hình) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `PAYMENT_GATEWAY_API_KEY` | Cổng thanh toán (chưa chọn cổng; tên chung) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `WEB_RESEARCH_MCP_API_KEY` | Mục kho `kho:repos/web-research-mcp` cần khoá API (theo trường needs) | đề xuất của công cụ từ trường needs | Con người; đổi/xoay là L3 |
| `CLOUD_ACCOUNTING_MCPS_API_KEY` | Mục kho `kho:mcps/cloud-accounting-mcps` cần khoá API (theo trường needs) | đề xuất của công cụ từ trường needs | Con người; đổi/xoay là L3 |

## Cách dừng

- Dừng khẩn: `/stop` trên kênh CEO, hoặc đặt `agents.status = paused` (toàn OPC hoặc từng agent).
- Dừng một kênh: thu hồi token nền tảng của kênh đó (việc L3, con người làm).
- Dừng hẳn: tắt tiến trình Hermes/OpenClaw, xoay toàn bộ khoá ở bảng trên.
- Nút dừng mới ở mức thiết kế; kiểm bằng test `OT05` khi dựng.

## Runbook sự cố

| Sự cố | Dấu hiệu | Làm ngay | Sau đó |
|---|---|---|---|
| Đăng/gửi ngoài lô đã duyệt | Hành động ra ngoài không có bản ghi `approved` | `/stop`, thu hồi token kênh | Escalation, rà `activity_log`, quay về đầu pha |
| Token nền tảng hết hạn | Lỗi xác thực từ API | Tự khoá kênh đó; CEO xoay token | Ghi escalation; kiểm ngưỡng cảnh báo sớm |
| Khách phàn nàn, đòi hoàn tiền | Tin nhắn có từ khoá/cảm xúc tiêu cực | Chuyển nguyên văn cho CEO (L3), bot không tự trả lời | Cập nhật KB nếu là lỗi lặp |
| Tiền sai lệch khi đối soát | Thu và chi không khớp | Dừng chi trả (G4), báo CEO | Đối soát lại từng giao dịch; ghi escalation |
| Nội dung ngoài cố điều khiển agent | Câu kiểu "bỏ qua chỉ dẫn" trong dữ liệu | Không làm theo; ghi nguyên văn | Báo CEO; rà quy tắc nội dung ngoài trong `GATES.md` |
| Thông tin sai sự thật đã đăng | Có người báo | Gỡ bài theo G6; ghi lại | Thêm bước kiểm nguồn vào SOP của `research` |

## KPI và cách đo

KPI từng agent: `OPC-ROSTER.md`. Cách ghi: bảng `kpis`, mỗi tuần một dòng, số thật. Chưa có số nền thì để trống.

## Trạng thái pha

Mỗi lần qua pha, CEO ghi một dòng: ngày, pha, ai xác nhận, mốc đã đạt.

| Ngày | Pha | CEO xác nhận | Mốc đã đạt |
|---|---|---|---|
| CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |

<!-- BAN-GIAO:BEGIN -->
(Phần này do `ban-giao` điền: kết quả kiểm, danh sách mục kho, HỔNG, các chỗ còn `CHƯA CÓ — hỏi CEO`.)
<!-- BAN-GIAO:END -->

## Việc còn nợ (nói thẳng)

- Chưa mục kho nào được dùng thật; mức kiểm duy nhất là đọc nguồn.
- Chưa chạy gì với credential thật. Chưa có workflow n8n hay mã Hermes dựng từ bộ khung này.
- `PACK.md`, `RISKS-LEGAL.md`, bảng giá, danh sách đối tác, pháp nhân, cổng thanh toán, bộ nhận diện: CEO chưa điền.
- Các gói mở rộng đề xuất mới (Tài chính và thanh toán, Quản lý đối tác) CHƯA có role pack trong kho; xem mục gói mở rộng ở `OPC-ROSTER.md` và `catalog/GAP-LOG.md`.
- Tiêu chí gỡ: 6 tháng không có job nào chạy ở một bộ phận thì đề xuất gỡ bộ phận đó.
