# Kiểm thử sử dụng lô skill-a2 (skill-agent, 41 mục cuối theo id)

Phương pháp: mô phỏng bằng văn bản (không chạy mã, không dùng mạng). Ngày 2026-10-19. Đây là mô phỏng bằng mô hình, không phải dùng thật trong dự án.

## Đếm verdict

| verdict | số mục |
|---|---|
| pass | 9 |
| partial | 30 |
| fail | 1 |
| khong-ap-dung | 1 |
| tổng | 41 |

## 10 vấn đề phổ biến nhất

| # | mã | số lần | ví dụ |
|---|---|---|---|
| 1 | MAU_THUAN | 27 | research-synthesis: Ví dụ cluster A nói 'VND 3,500 tỷ vs $450M, convert ra trùng khớp' nhưng 3.500 tỷ VND chỉ khoảng 140 triệu USD; ví dụ minh hoạ sai đúng bước 'resolve conflicts' mà skill dạy, rồi dùng $450M trong narrative. |
| 2 | CAN_CONG_CU_NGOAI | 22 | research-independent-review-gate: Setup bước 2 yêu cầu 'spawn Reviewer B và C' nhưng không nói công cụ/cách tạo 2 agent cô lập ngữ cảnh ở môi trường nào. |
| 3 | KHAC | 21 | research-synthesis: Văn phong xưng 'mày/tao' trong nội dung skill (Bước 4, Lỗi thường gặp) không phù hợp khi skill được dùng cho khách; nên trung tính. |
| 4 | GAN_THUONG_HIEU_CUNG | 19 | primary-research-design: TL;DR và phần 'Ví dụ thực tế' gắn cứng ABTRIP/Fast Track Nội Bài; phần quy trình thì trung lập nên tái dùng được, chỉ cần thay ví dụ. |
| 5 | THIEU_GUARDRAIL | 14 | social-listening-research: Gợi ý lấy nội dung Facebook Groups/bình luận cá nhân mà không dặn về nhóm kín, điều khoản nền tảng, và bỏ tên người viết khi báo cáo. |
| 6 | MO_HO | 12 | research-independent-review-gate: Rubric B/C không có định dạng đầu ra cố định ngoài 'PASS/FAIL + danh sách lỗi', không có ngưỡng thế nào là 'đủ mạnh' cho Reviewer C. |
| 7 | PHAI_BIA_SO_LIEU | 11 | trend-forecasting: Xác suất 60/20/20 và 'gấp 2-3x base' là cố định, không có căn cứ; làm theo thì phải gán xác suất giả cho mọi chủ đề. |
| 8 | REF_THIEU | 7 | social-listening-research: Setup bước 2 trỏ tới 'Tầng Tay bên dưới' nhưng file không có mục đó; đường dẫn 'skills/x-research-skill-skill.md' sai (thực tế là thư mục skills/x-research-skill-skill/SKILL.md). |
| 9 | KHONG_CO_DINH_DANG_RA | 3 | statistical-analysis: Chỉ có ví dụ SAI/ĐÚNG diễn giải từng số, không có mẫu báo cáo tổng hợp; không có mục 'Ví dụ thực tế'. |

## Mục fail

- **agents/trum-san-bay/skills/aviation-knowledge**: Sai sự kiện: Tân Sơn Nhất ghi T1 quốc tế/T2 nội địa (đảo ngược); Đà Nẵng ghi '1 terminal' trong khi có T1 nội địa và T2 quốc tế; 'laptop trong vali ký gửi bị cấm' không đúng (chỉ pin lithium rời/sạc dự phòng bị cấm ký gửi).; Quy trình chuẩn nói drop baggage 2-3 giờ trước nhưng khuyến nghị có mặt nội địa 1.5-2 giờ trước.

## Mục khong-ap-dung

- **agents/trum-san-bay/skills/media-performance-discipline**: File 724 byte chỉ là stub chuyển hướng, vẫn được liệt kê là skill-agent riêng nên có thể gây trùng khi tra kho; thiếu frontmatter.

## Ghi chú về phạm vi

- Catalog hiện có 85 mục loai skill-agent; lô lấy 41 mục CUỐI theo id (từ research-analytics-pro/primary-research-design đến yt-cashcow/trend-scout). Đề bài ghi 'chỉ số 41 đến 81' nhưng với 85 mục không trùng với '41 mục cuối', nên theo '41 mục cuối'.
- 3 mục trong thu-kho đều có trong catalog (kiem_tu_dong để trống). 3 cặp file yt-cashcow và shorts-affiliate-system (compliance-gate, platform-disclosure-adapter, trend-scout) giống hệt từng byte nên kết luận gần như trùng.
- Các nhận xét về sự kiện hàng không (terminal Tân Sơn Nhất/Đà Nẵng, quy định laptop) dựa trên hiểu biết của tester, chưa đối chiếu nguồn chính thức vì không dùng mạng.
- Các dữ kiện ngoài kho (URL RSS, tên nhóm Facebook, giới hạn nền tảng) không kiểm chứng được.
