# MCP/Tools Setup — An Bình / ABTRIP Ops Analyst

## Nguyên tắc chọn
Agent này chỉ ở mức **Tra cứu + Phân tích** — không bật bất kỳ connector nào có khả năng
ghi/gửi (Gmail, Slack, HubSpot-write, booking system). Nếu sau này nâng cấp agent lên mức
hành động, xem lại `ARCHITECTURE.md` phần "Vì sao KHÔNG có tầng Action" trước khi bật thêm.

## Danh sách bật

| Tool | Lý do | Bắt buộc? | Cách bật |
|---|---|---|---|
| **web_search / web_fetch** | Tra cứu chính sách hàng không, giá đối thủ — luôn cần mới nhất | Có, mặc định sẵn | Không cần cấu hình, có sẵn trong Claude |
| **Similarweb** | Ước lượng traffic/định vị đối thủ online (ABTRIP booking, OTA đối thủ) | Nên có | Connect qua Claude connector directory nếu chưa bật |
| **Google Drive/Sheets** | Đọc data booking/complaint export nếu Nobitano lưu ở đây | Tuỳ có data hay không | Connect qua Claude connector directory, chỉ cấp quyền ĐỌC |
| **Code execution (pandas/matplotlib)** | Phân tích pattern thật, ra chart | Có, mặc định sẵn trong Claude | Không cần cấu hình |
| **docx/pdf skill** | Xuất report cuối cho Nobitano | Có, mặc định sẵn | Không cần cấu hình |

## KHÔNG bật (có chủ đích)

| Tool | Vì sao không bật |
|---|---|
| Gmail (gửi) | Agent không được phép tự gửi email cho khách |
| Slack (gửi) | Agent không được phép tự gửi tin nhắn nội bộ thay Nobitano |
| HubSpot/CRM-write | Agent không được phép tự ghi log CRM — chỉ đọc nếu cần context, không ghi |
| Booking/OTA-write API | Agent không được phép tự đăng/sửa listing thật |

Nếu một ngày cần nâng cấp: bật thêm connector tương ứng CHỈ SAU KHI đã thêm sub-agent
Executor + tầng Confirm riêng theo `ARCHITECTURE.md`.
