# Deploy Checklist — `facebook-channel-agent`

> Đánh dấu `[x]` chỉ khi người thật đã làm và thấy kết quả. Công cụ không tự đánh dấu.
> Trạng thái mặc định: chưa làm gì. Chưa có credential thật nào được dùng.

## Pha 0 — Điền thông tin còn trống

- [ ] Mọi mục `CHƯA CÓ — hỏi CEO` trong `tenant-config.json`, `JD-KPI-SOP-ESCALATION.md`, `HANDOVER.md` đã được điền hoặc CEO xác nhận để trống có chủ đích
- [ ] Chủ sở hữu agent đã được ghi tên trong `HANDOVER.md`
- [ ] `python tools/agent_factory.py kiem <thư mục này>` cho kết quả PASS

## Pha 1 — Môi trường (Hermes)

- [ ] Đã đọc `agents/HERMES-GUIDE.md -> agents/HERMES-PLAYBOOK.md` và làm theo phần chuẩn bị của vessel
- [ ] Đã đọc `INSTALL-PLAN.md`; người duyệt đã đồng ý từng mục sẽ cài
- [ ] Đã cài các mục được duyệt (công cụ không tự cài)
- [ ] Đã tạo các biến môi trường theo danh sách TÊN ở `HANDOVER.md`; file chứa giá trị nằm ngoài kho và không có trong git
- [ ] Đã dán `system-prompt.md` làm instruction của agent

## Pha 2 — Kiểm trước khi bật

- [ ] `tests/TEST-PLAN.md`: mọi test mang nhãn `lan-ranh-do` đã chạy và ghi PASS thật
- [ ] Test nút dừng khẩn (`T05`) PASS: sau `/stop` không còn hành động ra ngoài
- [ ] Spike 30 phút trên MỘT việc thật cho từng khả năng ở `capability-map.json`; ghi `catalog/USAGE-LOG.md` (dùng được / phải sửa / bỏ)
- [ ] Mục nào spike FAIL thì bỏ, ghi lý do, dùng mục dự phòng hoặc ghi `catalog/GAP-LOG.md`

## Pha 3 — Hai tuần đầu: chỉ soạn nháp (`launch_mode = draft_only`)

- [ ] Agent chỉ ghi nháp vào hàng đợi; người thực thi tay mọi hành động ra ngoài
- [ ] Mỗi tuần ghi KPI thật vào bảng KPI (số nền cho ô `CHƯA CÓ — hỏi CEO`)
- [ ] Không có vi phạm lằn ranh đỏ nào (một vi phạm = quay lại Pha 2, ghi escalation)

## Pha 4 — Sang mức tự chủ đã khai báo (L1)

Điều kiện tối thiểu (CEO có thể đặt chặt hơn):
- [ ] Hai tuần Pha 3 không có vi phạm lằn ranh đỏ
- [ ] CEO đã xem lại các nháp và đồng ý chuyển
- [ ] `launch_mode` đổi trong `tenant-config.json` bởi con người, có ghi ngày và người đổi

## Gỡ khi không dùng

- Sáu tháng liền không có job nào chạy thì đề xuất gỡ: tắt agent, lưu package, ghi lý do vào `HANDOVER.md`, ghi `catalog/USAGE-LOG.md` kết quả `bỏ`.
