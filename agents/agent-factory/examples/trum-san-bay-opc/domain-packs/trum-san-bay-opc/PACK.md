# Domain Pack — Trùm Sân Bay (`trum-san-bay-opc`)

> **DEMO dựng từ thiết kế NHÁP chưa duyệt (agents/trum-san-bay/OPC-DESIGN-NOTES.md, dừng sau Phần 2 trên 5 phần). Không phải kế hoạch triển khai, chưa chạy gì.**

> Sinh từ `domain-packs/_TEMPLATE.md` bởi Agent Factory ngày 2026-10-19. Mục nào ghi `CHƯA CÓ — hỏi CEO`
> là thật sự chưa có thông tin; agent không được tự bịa. Đây là file DUY NHẤT agent nạp để hiểu project.

---

## 1. Brand context

- **Sản phẩm/Dịch vụ:** Công ty một người quanh thương hiệu Trùm Sân Bay: xây kênh nội dung hàng không (Facebook chính, kèm Instagram) và thương hiệu, rồi bán dịch vụ sân bay (README của agents/trum-san-bay nêu Fast Track, SIM du lịch, đổi tiền) và làm affiliate. Dịch vụ do đối tác bên thứ ba thực hiện; Trùm Sân Bay thu tiền của khách rồi trả đối tác. Nguồn: agents/trum-san-bay/OPC-DESIGN-NOTES.md (NHÁP chưa duyệt).
- **Khách hàng mục tiêu:** CHƯA CÓ — hỏi CEO
- **Positioning statement:** CHƯA CÓ — hỏi CEO
- **Đối thủ chính:** CHƯA CÓ — hỏi CEO (hoặc giao `research` làm competitive scan nền trước)
- **Brand voice (đúng 3 đặc điểm):** CHƯA CÓ — hỏi CEO
- **Từ CẤM dùng:** CHƯA CÓ — hỏi CEO
- **Ngôn ngữ phục vụ khách:** CHƯA CÓ — hỏi CEO (đề xuất: vi, và ngôn ngữ khác chỉ khi CEO duyệt mẫu câu cho ngôn ngữ đó; câu ngoài mẫu là nháp kèm bản dịch tiếng Việt cho người duyệt)

## 2. Design tokens

- **Màu:** CHƯA CÓ — hỏi CEO
- **Font:** CHƯA CÓ — hỏi CEO
- **Logo rule:** CHƯA CÓ — hỏi CEO
- **Tone hình ảnh:** CHƯA CÓ — hỏi CEO
- Chưa có token thì `media` không được tự chốt bộ nhận diện.

## 3. Constraints (giới hạn cứng)

- **Budget trần:** CHƯA CÓ — hỏi CEO. Không agent nào đề xuất chi vượt khi chưa có trần.
- **Kênh được phép và tần suất tối đa:** facebook, zalo, instagram; tần suất CHƯA CÓ — hỏi CEO
- **Nguồn doanh thu bật:** affiliate, dich-vu
- **Pháp lý/ngành:** CHƯA CÓ — hỏi CEO (xem `RISKS-LEGAL.md`; kho không tư vấn pháp lý)
- **Giá/promotion:** CHƯA CÓ — hỏi CEO. Không agent nào tự báo giá. Bảng giá chuẩn do CEO duyệt trước; giá ngoài bảng là L3. Bot chỉ đọc nguyên dòng giá của bảng chuẩn; tính tổng cho đơn (nhân số người, phụ thu, thuế, ngày lễ) là việc của `sales` qua đơn nháp, mức L2 (trong bảng) hoặc L3 (ngoài bảng).
- **Thông tin hàng không (giờ bay, hành lý, quy định, nhà ga):** bot chỉ trả lời khách bằng mục KB đã duyệt có ngày kiểm. Ngoài KB: skill tra cứu quy định hàng không (`aviation-policy-lookup`) chỉ để soạn NHÁP kèm nguồn và câu miễn trừ cho người duyệt (L2); bot KHÔNG trả thẳng kết quả tra web cho khách (GATES Luật vận hành 13).

## 4. Glossary

| Từ | Nghĩa trong project này |
|---|---|
| CHƯA CÓ — hỏi CEO | CHƯA CÓ — hỏi CEO |

## 5. Nguồn data sẵn có

- CHƯA CÓ — hỏi CEO

## 6. Trạng thái hiện tại

- [2026-10-19] Pack được dựng bởi Agent Factory từ thiết kế NHÁP. Chưa có mục nào được CEO điền hay duyệt.

## 7. Mẫu câu và chính sách với khách (CEO duyệt từng mục; chưa duyệt thì không dùng)

| Mục | Nội dung |
|---|---|
| Câu xác nhận tạm khi chuyển CEO (đề xuất, chưa duyệt) | Cảm ơn bạn đã liên hệ. Mình đã chuyển nội dung này cho người phụ trách xem xét. Hiện mình chưa thể xác nhận giá, thời gian hay khoản hoàn tiền nào; người phụ trách sẽ phản hồi bạn. |
| Ngày CEO duyệt câu trên | CHƯA CÓ — hỏi CEO |
| SLA phản hồi của người duyệt (số giờ, giờ làm việc hay 24/7) | CHƯA CÓ — hỏi CEO |
| Mẫu trả lời khi khách gửi dữ liệu nhạy cảm (đề xuất, chưa duyệt) | Cảm ơn bạn. Vì an toàn, bạn vui lòng không gửi số thẻ, mã CVV, mật khẩu hay mã OTP qua tin nhắn hoặc bình luận. Hãy thanh toán qua kênh thanh toán chính thức của chúng tôi. |
| Kênh thanh toán chính thức | CHƯA CÓ — hỏi CEO |
| Người xoá tin gốc có dữ liệu nhạy cảm (nếu nền tảng cho phép) | CHƯA CÓ — hỏi CEO |

---

> **Quy tắc dùng pack:** mọi delegation phải có header `[PACK: trum-san-bay-opc]`. Agent chỉ đọc đúng pack này trong phiên.
> Output đặt tên file có slug. Chi tiết: `agents/company/COORDINATION-v2.md` mục 7.
