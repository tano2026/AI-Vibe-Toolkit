# QA-GATE — Cổng kiểm của Claude trước khi xin OK deploy

> Cổng này kiểm **hồ sơ + code + ca kiểm**, không bảo chứng tool "tốt". PASS nghĩa là đủ thứ phải có và không phạm luật cứng. FAIL bất kỳ mục nào thì ghi KHÔNG ĐẠT vào `QA-VERDICT.md`, không sửa mong đợi để cho qua.

## A. Mọi tool (mức A, B, C)

| # | Kiểm | PASS khi | Cách kiểm |
|---|---|---|---|
| A1 | Ca kiểm | Mọi ca kiểm trong `TOOL-SPEC` chạy và ra đúng kết quả mong đợi | Chạy lại, không tin báo cáo của tay |
| A2 | Công thức | Mỗi công thức trong code khớp công thức trong spec, kể cả trọng số | Đọc code, tính tay một ca |
| A3 | Khoá và bí mật | Không có chuỗi giống khoá, token, mật khẩu trong code, log, báo cáo; chỉ dùng TÊN biến môi trường | Quét `ghp_`, `sk-`, `AKIA`, `-----BEGIN`, `password=` |
| A4 | Dữ liệu giả | Dữ liệu mẫu và test không chứa dữ liệu khách thật | Đọc dữ liệu mẫu |
| A5 | Lỗi dễ hiểu | Nhập sai/thiếu thì tool báo tiếng Việt, không treo, không hiện stack trace | Thử 3 đầu vào sai |
| A6 | Phạm vi | Tool không làm điều ghi trong "không làm" của spec | Đọc code, thử |
| A7 | Ra ngoài | Nút đăng/gửi/trả tiền (nếu có) mặc định là nháp, không tự gọi API ghi | Thử |
| A8 | Điện thoại | Giao diện dùng được ở màn hình hẹp, không cuộn ngang | Mở ở khổ hẹp |
| A9 | Cấu hình | Ngưỡng và trọng số nằm trong `config.json`, đổi không cần sửa code | Đổi một ngưỡng, chạy lại |

## B. Tool nội bộ (mức B, C)

| # | Kiểm | PASS khi |
|---|---|---|
| B1 | Nội dung ngoài là dữ liệu | Tool xử lý văn bản từ web/tin nhắn/file dán thì luồng do code quyết; chuỗi "bỏ qua chỉ dẫn" không đổi được hành vi |
| B2 | Lưu dữ liệu | Có chỗ lưu và chỗ xoá rõ ràng; không ghi dữ liệu nhạy cảm vào log |
| B3 | Khởi động lại | Có cách khởi động lại và cách gỡ, ghi trong `BUILD-REPORT-deploy.md` |
| B4 | Nhắc việc | Tool có hạn chót (vd nộp thầu) phải có nhắc việc kiểm được bằng một ca có ngày giả |
| B5 | Đọc được bởi người khác | Nhân viên không rành kỹ thuật làm theo hướng dẫn 5 bước vẫn dùng được |
| B6 | Báo cáo trung thực | `BUILD-REPORT` ghi rõ phần chưa làm, phần chưa chạy; không có "xong" mà thiếu kết quả chạy |

## C. Tool mầm sản phẩm (mức C)

| # | Kiểm | PASS khi |
|---|---|---|
| C1 | Tách cấu hình theo khách | Tên công ty, logo, bảng giá, mẫu văn bản, ngưỡng nằm trong cấu hình riêng; đổi khách không sửa code |
| C2 | Cách ly dữ liệu | Dữ liệu khách A không đọc được từ khách B; có ca kiểm chứng minh |
| C3 | Đầu vào độc hại | Thử chuỗi script, SQL, đường dẫn lên cấp, file quá lớn: tool từ chối hoặc làm sạch |
| C4 | Giới hạn gọi AI | Có trần số lần/chi phí gọi LLM mỗi lần chạy; hết trần thì dừng báo rõ |
| C5 | Giấy phép | Gói bên thứ ba có giấy phép cho phép dùng thương mại; ghi lại tên gói và giấy phép |
| C6 | Soát bảo mật riêng | Nếu xử lý dữ liệu khách thật: chủ thuê/tự soát riêng trước khi mở cho khách. Cổng này không thay thế |

## Kết quả

- **ĐẠT:** A, B (nếu B/C), C (nếu C) đều PASS.
- **KHÔNG ĐẠT:** ghi mục FAIL, tay phải sửa, số vòng. Lỗi lặp 3 vòng: escalation (`TEAM-CHARTER.md` mục 8).
- Claude không tự hạ tiêu chuẩn vì chủ đang vội. Chủ muốn bỏ qua một mục thì chủ nói rõ bằng chữ, Claude ghi vào `QA-VERDICT.md` là "chủ miễn mục X, rủi ro Y".
