---
name: ghi-so
description: >
  Ghi sổ kho: dòng GAP-LOG khi tra không có ứng viên đủ tốt, dòng USAGE-LOG khi một mục được dùng thật trong dự án.
  Dùng ở cuối mỗi lần tra thất bại hoặc cuối mỗi dự án. Chỉ nối cuối bảng; kết quả chỉ nhận dùng được / phải sửa / bỏ.
---

# Ghi sổ (GAP-LOG và USAGE-LOG)

## Khi nào dùng
- Tra xong mà không có ứng viên đủ tốt cho một khả năng → **GAP-LOG**
- Người dùng báo một mục đã dùng trong dự án thật (hoặc thử rồi bỏ) → **USAGE-LOG**
- Hết dự án: hỏi "đã dùng mục nào trong kho?" để đóng vòng (PLAYBOOK mục 3)

## Khi nào KHÔNG dùng
- Chỉ đọc, hoặc chạy thử cho biết → không ghi USAGE-LOG (log ghi "dùng trong dự án thật")
- Chưa tra đủ (chưa thử `--ca-chua-nhan`, chưa đổi cách diễn đạt) → tra tiếp rồi mới ghi GAP

## Quy trình
**Trước mọi dòng ghi:** truy vấn và ghi chú phải ĐÃ che dữ liệu nhạy cảm của khách (thẻ, CVV, OTP, mật khẩu, giấy tờ, số tài khoản thành `[ĐÃ ẨN: loại dữ liệu]`) và không chứa khoá/token. Dòng sổ lưu lâu và nhiều người đọc.

### GAP-LOG
1. Đảm bảo đã: thử ≥ 2 cách diễn đạt, thử `--ca-chua-nhan`, bỏ ràng buộc mềm xem có ứng viên không.
2. Tạo dòng: `python tools/thu_kho.py ghi-gap "<khả năng cần>" --du-an "<khách/dự án>" --ghi-chu "<vì sao chưa đủ>"`
3. Cho người dùng xem dòng. Được đồng ý thì thêm `--ghi` (nối cuối `catalog/GAP-LOG.md`).
4. Không đi sưu tầm entry mới ngay; entry mới (nếu có) phải trỏ lại dòng GAP này.

### USAGE-LOG
1. Hỏi đủ: mục (id), dự án/khách thật, kết quả (`dùng được` / `phải sửa` / `bỏ`), tiết kiệm được gì (giờ hoặc việc cụ thể, không ghi cảm giác), ghi chú (sửa gì, vì sao bỏ).
2. `python tools/thu_kho.py ghi-usage <id> --du-an "<...>" --ket-qua "dung duoc" --tiet-kiem "2 giờ lên lịch tuần" --ghi-chu "..."`
3. Công cụ từ chối kết quả ngoài ba giá trị trên, từ chối "dùng được" mà thiếu cột tiết kiệm, từ chối thiếu tên dự án. Đừng lách.
4. Được đồng ý → thêm `--ghi`.
5. Sau 2 dòng "dùng được" cho cùng một mục, báo người duy trì kho để nâng nhãn từ "điểm đọc" sang "điểm dùng".

## Dòng sai hoặc ghi dở
- Dòng nhập sai: nối thêm một dòng đính chính ở cuối bảng, cột ghi chú ghi `đính chính dòng ngày X`. Không sửa, không xoá dòng cũ.
- Dòng ghi dở do lỗi file: người duy trì kho xử lý; Thủ Kho không sửa.

## Ví dụ
```
$ python tools/thu_kho.py ghi-gap "viết email lạnh tiếng Việt" --du-an "Khách sạn A" --ghi-chu "mục gắn nhãn chỉ có billionmail (máy chủ gửi mail), không có công cụ soạn"
| 2026-10-17 | viết email lạnh tiếng Việt | Khách sạn A | thu_kho tim; capability: email-outreach; ... | mục gắn nhãn chỉ có billionmail... | mở |

$ python tools/thu_kho.py ghi-usage mcps/buffer-mcp --du-an "Fanpage Khách B" --ket-qua "phai sua" --tiet-kiem "1 giờ/tuần lên lịch" --ghi-chu "phải đổi base URL"
| 2026-10-17 | mcps/buffer-mcp.md | Fanpage Khách B | phải sửa | 1 giờ/tuần lên lịch | phải đổi base URL |
```

## PASS / FAIL
- **PASS:** dòng đúng 6 cột như bảng gốc; chỉ nối cuối; kết quả hợp lệ; GAP có đủ "đã tra" và "vì sao chưa đủ"
- **FAIL:** ghi USAGE cho thứ chưa dùng thật; bịa số giờ tiết kiệm; xoá/sửa dòng cũ; ghi khi người dùng chưa đồng ý; dòng chứa dữ liệu nhạy cảm của khách hoặc khoá chưa che
