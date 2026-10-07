# Twenty CRM — Tuỳ biến cho ABTRIP (dùng nội bộ)

## TL;DR
Spec thiết kế dùng Twenty CRM làm CRM nội bộ ABTRIP (object Bookings, Fast Track & Meet Assist, GDS Reference; pipeline 5 stage theo chu kỳ bán thật). CHƯA triển khai, CHƯA chạy thử — việc đầu tiên là quyết định giữ hay bỏ ABTrip CRM tự xây, rồi test PASS/FAIL ở mục 7.

> Trạng thái: **spec thiết kế, CHƯA triển khai, CHƯA chạy thử.**
> Phạm vi: CHỈ nhân viên ABTRIP dùng, đặt sau VPN, không mở cho khách truy cập trực tiếp.
> Đọc trước: `repos/twenty-crm.md` (license + bảo mật). Tao không phải luật sư; phần license cần xác nhận nếu tính bán.

## 0. Quyết định cần Nobitano chốt TRƯỚC khi làm bất kỳ bước nào
**Dừng ABTrip CRM tự xây tay (React/TS/Vite, 9 module) và chuyển sang Twenty, hay giữ nguyên?**
Spec này giả định chuyển hẳn. Không chạy song song 2 hệ thống — dữ liệu sẽ phân mảnh. Nếu giữ CRM tay, bỏ qua file này.

## 1. Object gốc Twenty — giữ nguyên, không sửa cấu trúc
```
Companies     → đối tác B2B (PVN, cơ quan/doanh nghiệp đặt vé số lượng lớn), KHÔNG dùng cho khách lẻ
People        → người liên hệ tại từng Company + khách cá nhân
Opportunities → deal đang đàm phán (hợp đồng mới, gia hạn phụ lục)
Notes/Tasks   → dùng chuẩn
```

## 2. Object MỚI — đúng nghiệp vụ ABTRIP

### `Bookings` (Đặt chỗ/Vé)
```
- PNR (record locator GDS)                 text
- Hãng bay                                  select
- Hành trình                                text, vd "HAN-SGN-HAN"
- Ngày bay / Ngày xuất vé                   date
- Giá vé                                    currency (VND)
- Hạng vé                                   select
- Liên kết: Company (đặt theo hợp đồng B2B) hoặc People (khách lẻ)
- Trạng thái: Đã đặt / Đã xuất / Đã bay / Huỷ
```
> Chỉ lưu MÃ PNR. Không lưu số hộ chiếu, ngày sinh, thẻ thanh toán (dữ liệu nhạy cảm).

### `Fast Track & Meet Assist` (dịch vụ sân bay)
```
- Loại dịch vụ: Fast Track / Meet & Assist / cả hai    select
- Sân bay áp dụng                                       select
- Ngày dùng dịch vụ                                     date
- Số lượng người                                        number
- Liên kết: Company (PVN hoặc đối tác khác)
- Trạng thái duyệt: Chờ duyệt / Đã duyệt / Đã dùng
```

### `GDS Reference` (tra cứu nhanh)
Lưu sẵn mẫu cú pháp (vd. định dạng SR DOCS/APIS đã chuẩn hoá, KHÔNG chứa dữ liệu hành khách thật) để nhân viên copy đúng cú pháp.

## 3. Pipeline Opportunities — đổi stage mặc định
```
Mặc định Twenty: New → Screening → Meeting → Proposal → Customer
Đổi thành:       Tiếp cận → Báo giá → Đàm phán hợp đồng → Ký/Gia hạn → Đang phục vụ
```

## 4. Phân quyền nội bộ (gợi ý, chỉnh theo team thật)
| Vai trò | Thấy gì |
|---|---|
| Tan (quản lý) | Toàn quyền |
| Sales | Bookings + Opportunities + Companies/People |
| Kế toán (nếu có) | Bookings (giá vé) + Fast Track (chi phí) |

> Phân quyền theo vai trò chi tiết có thể nằm trong nhóm tính năng Enterprise (thương mại). Kiểm tra bản Community có đủ không trước khi hứa với team.

## 5. Nối agent (làm SAU khi Twenty chạy ổn)
- Hermes gọi REST API (mẫu code ở `repos/twenty-crm.md`) để: liệt kê Booking chưa xuất vé quá 3 ngày, tổng hợp Fast Track của PVN theo tháng, soạn nháp follow-up cho Company chưa phản hồi báo giá sau 1 tuần
- MCP của Twenty (nếu bản đang chạy có): chưa kiểm tra, không dựa vào cho tới khi test thật
- Claude Code hiện chưa chạy được trên máy Windows — đừng đặt Claude Code làm điều kiện, dùng Hermes trước

## 6. Việc BẮT BUỘC trước khi tự host
1. Đọc GitHub Security Advisories của `twentyhq/twenty`, dùng bản release mới nhất. 2026 có nhiều lỗ hổng nặng riêng của Twenty (RCE/command execution, SQL injection, lộ mật khẩu qua GraphQL ngày 05/10/2026 — chi tiết ở `repos/twenty-crm.md`). Chưa xác nhận được bản vá cụ thể cho từng lỗi.
2. Chạy sau VPN/Tailscale hoặc whitelist IP văn phòng. Không publish cổng ra internet.
3. Backup Postgres hằng ngày, thử khôi phục 1 lần.
4. API key riêng từng agent, quyền tối thiểu, không ghi vào file trong kho.
5. Không dùng các file/tính năng đánh dấu `@license Enterprise` (billing, SSO, record-share…) khi chưa có license thương mại.

> Lưu ý đính chính: CVE-2026-44492/44494/44495 là lỗi của thư viện **axios**, không phải của Twenty, và `twenty-server` main đã ghim axios ≥ 1.16.0. Đừng viết lại thành "Twenty dính CVE-44492".

## 7. Cách kiểm chứng (đây là việc đầu tiên, trước mọi thiết kế thêm)
```
PASS khi: docker compose lên được trên VPS thử, tạo 1 Company + 1 People + 1 Opportunity
          bằng tay, rồi Hermes đọc lại đúng record đó qua REST API.
FAIL/dừng: không lên được trong 2 giờ, hoặc API không đọc được → quay lại quyết định mục 0.
```
Chưa PASS bước này thì không làm object riêng, không nối agent, không nhập dữ liệu thật.
