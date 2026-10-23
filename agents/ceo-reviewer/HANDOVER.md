# HANDOVER — `ceo-reviewer`

> File này là KHUNG. Lệnh `tools/agent_factory.py ban-giao` điền phần giữa hai dấu `BAN-GIAO` và đóng gói
> kèm checksum. Phần ngoài hai dấu do con người viết. Trạng thái trung thực nằm ở mục "Việc còn nợ".

## Tóm tắt

- **Agent:** CEO Reviewer (`ceo-reviewer`)
- **Việc:** đọc plan/feature/ý tưởng sản phẩm và review theo góc nhìn CEO-founder (thách thức premise, ROI, rủi ro, nên mở rộng hay cắt scope) → bản review có verdict + phản biện + 3 việc làm tiếp → CEO chủ sở hữu
- **Vessel:** Claude Code
- **Mức tự chủ:** L0; chế độ khởi động `draft_only` 2 tuần
- **Chủ sở hữu:** CHƯA CÓ — hỏi CEO
- **Ngày dựng:** 2026-10-23

## Cách chạy

1. Làm theo `deploy-checklist.md` từ Pha 0 đến Pha 2.
2. Chạy dưới vessel: Claude Code, hướng dẫn `agents/CLAUDE-CODE-BRIDGE.md`.
3. Lệnh khởi chạy cụ thể: CHƯA CÓ — hỏi CEO (công cụ chưa biết môi trường cài của bạn).

## Biến môi trường cần có (chỉ TÊN)

Tên đề xuất, phải khớp lại với mã thật khi dựng. Giá trị nằm ngoài kho.

| Tên biến | Dùng cho | Nguồn của tên | Ai tạo / ai đổi |
|---|---|---|---|
| `LLM_API_KEY` | Khoá LLM/OmniRoute cho agent (tên chung; khớp lại theo router thật) | đề xuất của công cụ | Con người; đổi/xoay là L3 |
| `WEB_RESEARCH_MCP_SKILL_API_KEY` | Mục kho `kho:skills/web-research-mcp-skill` cần khoá API (theo trường needs) | đề xuất của công cụ từ trường needs | Con người; đổi/xoay là L3 |

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
| Khách gửi thẻ, CVV, OTP, giấy tờ vào chat | Có mẫu số thẻ hoặc mã trong tin | Kiểm log và Telegram có giá trị thô không; che; người duyệt xoá tin gốc nếu nền tảng cho phép | Bổ sung bộ lọc ở lớp nhận tin; chạy lại test `T11` |
| Hệ thống lưu hàng đợi hoặc cờ `paused` hỏng | Không đọc được cờ, hàng đợi hoặc bản ghi duyệt | Fail-closed: không đăng, không trả lời tự động; báo Telegram trực tiếp | Khi khôi phục, đối chiếu nhật ký tạm, không phát lại hành động đã thực thi |
| Khách chờ lâu sau khi bị chuyển CEO | Quá SLA của người duyệt | Nhắc người duyệt một lần; khách vẫn chỉ nhận câu xác nhận tạm | Rà SLA ở `JD-KPI-SOP-ESCALATION.md` mục 5.1 |

## KPI và cách đo

Xem bảng KPI trong `JD-KPI-SOP-ESCALATION.md`. Cách ghi: mỗi tuần một dòng với số thật. Chưa có số nền thì để trống, không điền số đoán.

<!-- BAN-GIAO:BEGIN -->
(Phần này do `ban-giao` điền: kết quả kiểm, danh sách mục kho, HỔNG, các chỗ còn `CHƯA CÓ — hỏi CEO`.)
<!-- BAN-GIAO:END -->

## Việc còn nợ (nói thẳng)

- Chưa có mục kho nào được dùng thật; mức kiểm duy nhất là đọc nguồn.
- Chưa chạy agent với credential thật; chưa có bằng chứng nào về chất lượng đầu ra.
- Nút dừng khẩn, hàng đợi duyệt, ghi log: thiết kế trên giấy, chưa nối mã.
- Bộ lọc che dữ liệu nhạy cảm, nhật ký tạm cục bộ, chống đăng đôi (fail-closed): thiết kế trên giấy, chưa nối mã.
- Không bật `launch_mode` khác `draft_only` trước khi test `T02`, `T05`, `T11`, `T13` PASS bằng bằng chứng chạy.
- Câu xác nhận tạm, mẫu trả lời khi khách gửi dữ liệu thẻ, SLA người duyệt, kênh thanh toán chính thức: CEO chưa duyệt.
- Các mục ghi `CHƯA CÓ — hỏi CEO` chưa có người điền (xem danh sách tự động ở trên).
- Tiêu chí gỡ: 6 tháng không có job nào thì đề xuất gỡ.
