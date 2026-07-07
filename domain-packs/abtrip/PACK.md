# Domain Pack — ABTRIP / An Bình Travel (`abtrip`)

> Pack thật đầu tiên, đồng thời là mẫu tham chiếu cách điền `_TEMPLATE.md`.
> Mục nào ghi `CHƯA CÓ — hỏi CEO` là thật sự chưa có thông tin, agent không được tự bịa.

---

## 1. Brand context

- **Sản phẩm/Dịch vụ:** ABTRIP (An Bình) — dịch vụ travel: vé máy bay, tour, dịch vụ du lịch cho
  khách Việt Nam. Thế mạnh nền: chuyên môn ticketing sâu (IATA, GDS Amadeus, Timatic, BSP) — tư vấn
  vé/hành trình phức tạp chính xác hơn đại lý phổ thông.
- **Khách hàng mục tiêu:** khách Việt đặt vé/tour, gồm cả cá nhân và SMB có nhu cầu công tác;
  chân dung chi tiết theo segment — `CHƯA CÓ — hỏi CEO` (Research có thể đề xuất draft để CEO duyệt).
- **Positioning statement (draft, CEO chưa chốt):** Với khách Việt cần vé máy bay và hành trình
  phức tạp, ABTRIP là dịch vụ travel tư vấn chuẩn nghiệp vụ hàng không, khác đại lý phổ thông ở chỗ
  xử lý được các ca khó (đổi/hoàn/nối chuyến/visa-transit) nhanh và đúng quy định.
- **Đối thủ chính:** `CHƯA CÓ — hỏi CEO` (hoặc giao Research làm competitive scan trước).
- **Brand voice (3 đặc điểm):** đáng tin như chuyên gia nghiệp vụ / nói dễ hiểu cho người không
  trong ngành / không hù dọa không giật tít rẻ tiền.
- **Từ CẤM dùng:** không cam kết "rẻ nhất thị trường"; không hứa kết quả visa; không nói thay quy
  định hãng khi chưa trích nguồn (quy định hãng/IATA thay đổi thường xuyên — luôn verify mới).

## 2. Design tokens

- **Màu / Font / Logo rule / Tone hình ảnh:** `CHƯA CÓ — hỏi CEO`.
  Designer tạm dùng: tone tin cậy ngành travel (xanh dương đậm + trắng), ảnh thật hành trình,
  KHÔNG chốt bộ nhận diện chính thức khi CEO chưa cấp token.

## 3. Constraints

- **Budget trần ads:** `CHƯA CÓ — hỏi CEO`. Marketing không đề xuất chi tiêu khi chưa có trần.
- **Kênh được phép:** `CHƯA CÓ — hỏi CEO` (đề xuất baseline được, chạy thật phải duyệt).
- **Pháp lý/ngành:** thông tin visa/nhập cảnh/quy định hãng PHẢI verify nguồn mới nhất (Timatic,
  website hãng, IATA) tại thời điểm viết — không dùng kiến thức cũ. Sai thông tin nhập cảnh = khách
  kẹt ở sân bay = rủi ro lớn nhất của project này.
- **Giá:** không role nào tự báo giá cho khách — báo giá là hành động cần CEO duyệt (Sales guardrail).

## 4. Glossary

| Từ | Nghĩa trong project này |
|----|--------------------------|
| PNR | Passenger Name Record — mã đặt chỗ trên GDS |
| GDS / Amadeus (1A) | Hệ thống phân phối toàn cầu ABTRIP thao tác chính |
| EMD | Electronic Miscellaneous Document — chứng từ dịch vụ bổ sung |
| BSP | Bank Settlement Plan — cơ chế thanh toán đại lý ↔ hãng |
| Timatic | Nguồn tra quy định nhập cảnh/visa/quá cảnh |

## 5. Nguồn data sẵn có

- Skill nền trong kho: `skills/expert-ticketing-aviation.md` — mọi role làm content/tư vấn cho
  ABTRIP nên nạp kèm skill này.

## 6. Trạng thái hiện tại

- [2026-07-07] Tạo pack đầu tiên. Nhiều mục chờ CEO bổ sung — role gặp mục `CHƯA CÓ` thì hỏi đúng mục đó, 1 lần, rồi pack được update dùng mãi.
