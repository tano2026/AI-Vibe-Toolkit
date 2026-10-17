# HANDOVER — OPC `{{slug}}`

> File này là KHUNG. `tools/agent_factory.py ban-giao` điền phần giữa hai dấu `BAN-GIAO` và đóng gói kèm checksum.
> Phần ngoài hai dấu do con người viết.

## Tóm tắt

- **OPC:** {{ten_thuong_hieu}} (`{{slug}}`)
- **Nguồn doanh thu / kênh:** {{doanh_thu_list}} / {{kenh_list}}
- **Gói mở rộng:** {{goi_list}}
- **Chủ sở hữu (CEO):** {{chu_so_huu}}
- **Ngày dựng:** {{ngay}}

## Cách chạy

1. Điền các mục còn trống (danh sách tự động ở phần `BAN-GIAO`).
2. Dựng Airtable `company-hq` theo `airtable-schema.json`.
3. Dựng kênh lệnh CEO (Telegram CEO Bot) và nối với Hermes (agent `ceo`). Chi tiết vessel: `agents/HERMES-GUIDE.md`, `agents/OPENCLAW-GUIDE.md`.
4. Bật theo `PHASES.md`, từng pha một, mỗi bộ phận hai tuần `draft_only` đầu.
5. Lệnh khởi chạy cụ thể: CHƯA CÓ — hỏi CEO (phụ thuộc môi trường cài).

## Biến môi trường cần có (chỉ TÊN)

Tên đề xuất, khớp lại với mã thật khi dựng. Giá trị nằm ngoài kho. Mỗi khách/OPC dùng khoá và tài khoản riêng.

{{ENV_VARS_TABLE}}

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
