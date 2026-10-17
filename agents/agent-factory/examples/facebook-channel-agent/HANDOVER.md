# HANDOVER — `facebook-channel-agent`

> **DEMO dựng từ chính CLI để minh hoạ Agent Factory. Chưa duyệt, chưa spike, chưa chạy với credential thật.**

> File này là KHUNG. Lệnh `tools/agent_factory.py ban-giao` điền phần giữa hai dấu `BAN-GIAO` và đóng gói
> kèm checksum. Phần ngoài hai dấu do con người viết. Trạng thái trung thực nằm ở mục "Việc còn nợ".

## Tóm tắt

- **Agent:** Facebook Channel Agent (`facebook-channel-agent`)
- **Việc:** đăng bài và trả lời bình luận trên một Facebook Page → bản nháp bài đăng và bản nháp trả lời bình luận, chỉ đăng sau khi duyệt → chủ Page (CEO) duyệt
- **Vessel:** Hermes
- **Mức tự chủ:** L1; chế độ khởi động `draft_only` 2 tuần
- **Chủ sở hữu:** CHƯA CÓ — hỏi CEO
- **Ngày dựng:** 2026-10-17

## Cách chạy

1. Làm theo `deploy-checklist.md` từ Pha 0 đến Pha 2.
2. Chạy dưới vessel: Hermes, hướng dẫn `agents/HERMES-GUIDE.md -> agents/HERMES-PLAYBOOK.md`.
3. Lệnh khởi chạy cụ thể: CHƯA CÓ — hỏi CEO (công cụ chưa biết môi trường cài của bạn).

## Biến môi trường cần có (chỉ TÊN)

Tên đề xuất, phải khớp lại với mã thật khi dựng. Giá trị nằm ngoài kho.

| Tên biến | Dùng cho | Nguồn của tên | Ai tạo / ai đổi |
|---|---|---|---|
| `LLM_API_KEY` | Khoá LLM/OmniRoute cho agent (tên chung; khớp lại theo router thật) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `TELEGRAM_BOT_TOKEN` | CEO Bot: kênh lệnh và duyệt | đề xuất của công cụ; kênh Telegram theo agents/README.md | Con người; đổi/xoay là L3 |
| `TELEGRAM_CHAT_ID_CEO` | Chỉ nhận lệnh từ chat của CEO (cấu hình, không bí mật) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `FB_PAGE_ACCESS_TOKEN` | Đăng bài và đọc bình luận Facebook Page | đề xuất của công cụ; agents/trum-san-bay/deploy-checklist.md ghi cần Page Access Token | Con người; đổi/xoay là L3 |

## Cách dừng

- Dừng khẩn: lệnh `/stop` trên kênh duyệt; hoặc đặt `status = paused` trong `tenant-config.json`.
- Dừng hẳn: tắt tiến trình trên vessel, thu hồi (xoay) các khoá liệt kê ở trên (việc L3, con người làm).
- Nút dừng mới ở mức thiết kế. Phải kiểm bằng test `T05` sau khi nối vào vessel.

## Runbook sự cố

| Sự cố | Dấu hiệu | Làm ngay | Sau đó |
|---|---|---|---|
| Agent đăng/gửi ngoài lô đã duyệt | Có hành động ra ngoài không có bản ghi `approved` | `/stop`, thu hồi khoá liên quan | Escalation, xem lại log, quay lại Pha 2 |
| Khoá/token bị lộ hoặc bị từ chối | Lỗi xác thực, hoặc khoá xuất hiện trong log/đầu ra | `/stop`, xoay khoá (con người) | Rà log đọc khoá; ghi escalation |
| Đầu ra sai sự thật | Người dùng/khách báo | Gỡ nội dung (cần duyệt theo GA6), ghi lại | Thêm bước kiểm nguồn vào SOP |
| Nội dung ngoài cố điều khiển agent | Câu kiểu "bỏ qua chỉ dẫn" trong dữ liệu | Không làm theo; ghi nguyên văn | Báo CEO; rà SOP-03 |
| Agent kẹt/lặp lỗi | Hơn 24 giờ hoặc 3 lần | Dừng thử | Escalation |

## KPI và cách đo

Xem bảng KPI trong `JD-KPI-SOP-ESCALATION.md`. Cách ghi: mỗi tuần một dòng với số thật. Chưa có số nền thì để trống, không điền số đoán.

<!-- BAN-GIAO:BEGIN -->
(Phần này do `ban-giao` điền: kết quả kiểm, danh sách mục kho, HỔNG, các chỗ còn `CHƯA CÓ — hỏi CEO`.)
<!-- BAN-GIAO:END -->

## Việc còn nợ (nói thẳng)

- Chưa có mục kho nào được dùng thật; mức kiểm duy nhất là đọc nguồn.
- Chưa chạy agent với credential thật; chưa có bằng chứng nào về chất lượng đầu ra.
- Nút dừng khẩn, hàng đợi duyệt, ghi log: thiết kế trên giấy, chưa nối mã.
- Các mục ghi `CHƯA CÓ — hỏi CEO` chưa có người điền (xem danh sách tự động ở trên).
- Tiêu chí gỡ: 6 tháng không có job nào thì đề xuất gỡ.
