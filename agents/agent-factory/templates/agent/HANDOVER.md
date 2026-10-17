# HANDOVER — `{{slug}}`

> File này là KHUNG. Lệnh `tools/agent_factory.py ban-giao` điền phần giữa hai dấu `BAN-GIAO` và đóng gói
> kèm checksum. Phần ngoài hai dấu do con người viết. Trạng thái trung thực nằm ở mục "Việc còn nợ".

## Tóm tắt

- **Agent:** {{ten_agent}} (`{{slug}}`)
- **Việc:** {{job_mot_cau}}
- **Vessel:** {{vessel_ten}}
- **Mức tự chủ:** {{tu_chu}}; chế độ khởi động `draft_only` 2 tuần
- **Chủ sở hữu:** {{chu_so_huu}}
- **Ngày dựng:** {{ngay}}

## Cách chạy

1. Làm theo `deploy-checklist.md` từ Pha 0 đến Pha 2.
2. Chạy dưới vessel: {{vessel_ten}}, hướng dẫn `{{vessel_doc}}`.
3. Lệnh khởi chạy cụ thể: CHƯA CÓ — hỏi CEO (công cụ chưa biết môi trường cài của bạn).

## Biến môi trường cần có (chỉ TÊN)

Tên đề xuất, phải khớp lại với mã thật khi dựng. Giá trị nằm ngoài kho.

{{ENV_VARS_TABLE}}

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
