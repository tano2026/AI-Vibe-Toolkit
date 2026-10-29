# TENANT-DEFAULTS — Mặc định riêng của chủ (đổi chủ thì chỉ sửa file này)

> Phần còn lại của gói là CORE, không chứa tên thương hiệu. Chỗ nào chưa biết ghi `CHƯA CÓ — hỏi CEO`. Chỉ ghi TÊN biến môi trường, không ghi giá trị khoá.

## Chủ

- Tên: Tân (Nobitano). Giao tiếp tiếng Việt thân mật, xưng tao/mày. Thích **một khuyến nghị dứt khoát**, không thích danh sách lựa chọn dài. Muốn chạy tự động, giao ra file/đoạn dán được ngay, ưu tiên bảng và cấu trúc hơn văn xuôi.
- Vai trò: Phó Giám đốc Sales, Marketing, Brand tại ABTRIP (đại lý vé máy bay/du lịch); Business Director tại An Bình Airport Services; đồng quản lý Tano Cafe và Wonder Mart. Có chứng chỉ IATA, dùng Amadeus GDS, BSP, Timatic.
- Hướng dài hạn: AI Implementation Partner cho doanh nghiệp vừa và nhỏ Việt Nam, bán dịch vụ trước, sản phẩm sau. Vì vậy mọi tool mức B trở lên phải tách cấu hình để nhân bản được.

## Hạ tầng mặc định

| Thứ | Mặc định |
|---|---|
| Hosting | VPS riêng của chủ, tên miền trỏ về VPS. Host cụ thể: `CHƯA CÓ — hỏi CEO` nếu không có trong thư mục task |
| Dữ liệu | Supabase (org của công ty), không phụ thuộc Claude khi chạy |
| AI trong tool | OpenRouter, model free tự động chọn, chỉ cho phần hiểu ngôn ngữ tự nhiên. Logic xác định (parse, tính, định dạng) viết bằng code |
| Giao diện | Web một trang, HTML/CSS/JS thuần khi được, chạy trên điện thoại |
| Đăng nhập | **Công cụ nội bộ không có màn hình đăng nhập** (chủ đã chốt). Không tự thêm xác thực trừ khi tool xử lý dữ liệu khách nhạy cảm hoặc mở ra ngoài; khi đó **hỏi chủ trước** |
| Độc lập AI | Tool chạy không cần gọi Claude, để tiết kiệm token và dễ bàn giao |

## Định dạng riêng

- Lệnh Amadeus **SR DOCS (APIS)** viết bằng dấu gạch ngang giữa các trường: `SR DOCS YY HK1-P-VNM-<số hộ chiếu>-VNM-<ngày sinh>-M-<ngày hết hạn>-<HỌ>/<TÊN>/P<n>` (họ tên vẫn ngăn bằng dấu gạch chéo). Số hộ chiếu trong ví dụ và test luôn là **dữ liệu giả**.
- Báo cáo, mẫu văn bản, thông báo lỗi: tiếng Việt. Thuật ngữ kỹ thuật và lệnh GDS giữ tiếng Anh.

## Quy trình nghiệp vụ đã chốt (công cụ phải tôn trọng)

- **Mua sắm công (e-GP):** bệnh viện, đơn vị công gửi yêu cầu báo giá vé máy bay. Sale admin lấy thông tin gói thầu → chuyển Ticketing kiểm tra, làm báo giá → Sale admin nộp trên e-GP trước hạn chót. Tool liên quan phải có **theo dõi hạn chót và nhắc việc**.
- **Thông tin hay đổi** (visa, nhập cảnh, hành lý, chính sách hãng): tool phải kiểm bằng nguồn mới nhất khi chạy hoặc ghi ngày kiểm và nguồn. Không nhúng cứng.

## Phân biệt thương hiệu (khi tool tạo nội dung hoặc tài liệu)

- ABTRIP (vé/du lịch): giọng ấm, B2C. An Bình (dịch vụ sân bay): giọng trang trọng, B2B/B2G. Không trộn màu: không dùng cam trong thiết kế An Bình, không dùng vàng trong thiết kế ABTRIP. Mã màu và logo lấy từ brand kit trong kho, không tự chế.
