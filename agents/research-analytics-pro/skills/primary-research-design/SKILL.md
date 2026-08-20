---
name: primary-research-design
description: >
  Thiết kế nghiên cứu sơ cấp (survey, interview guide) khi không có nguồn thứ cấp
  nào trả lời được câu hỏi — tức là khi research-synthesis/source-evaluation đã
  chạy hết mà vẫn thiếu data vì không ai công bố. Dùng cho Research Analytics Pro
  khi cần hỏi trực tiếp khách hàng/thị trường thay vì tổng hợp nguồn có sẵn.
  Bổ sung Capability Map — lỗ hổng đã xác định: agent mạnh research thứ cấp,
  chưa có skill tự thiết kế thu thập data sơ cấp.
---

# Primary Research Design — Thiết kế khảo sát & phỏng vấn

## TL;DR
Khi nguồn công khai không trả lời được câu hỏi (vd "khách ABTRIP thật sự chọn Fast Track vì lý do gì" — không ai công bố cái này), phải tự thu thập data sơ cấp. Skill này thiết kế đúng công cụ (survey hay interview) cho đúng loại câu hỏi, tránh lỗi thiết kế khiến data thu về vô dụng.

## Khi nào dùng
- Đã chạy `research-synthesis` + `source-evaluation` mà vẫn thiếu data quan trọng vì không ai công bố công khai
- Cần hiểu "tại sao" (motivation, lý do quyết định) — thứ nguồn thứ cấp gần như không bao giờ trả lời được
- Trước khi ra quyết định lớn (đổi giá, launch sản phẩm mới) muốn kiểm chứng với chính khách hàng thật, không chỉ suy luận từ data gián tiếp

## Nội dung skill / prompt

### Bước 1 — Chọn đúng công cụ (sai bước này là hỏng cả nghiên cứu)

| Câu hỏi dạng | Công cụ đúng | Vì sao |
|---|---|---|
| "Bao nhiêu % khách...", "có bao nhiêu người..." | Survey (định lượng) | Cần số đông, đo được tỷ lệ |
| "Tại sao khách chọn...", "họ nghĩ gì khi..." | Interview (định tính) | Cần hiểu sâu, không đo được bằng %, hỏi trực tiếp mới ra |
| Chưa biết câu hỏi gì để hỏi | Interview trước (khám phá) → Survey sau (đo lường diện rộng) | Interview giúp tìm ra đúng biến cần đo trước khi survey hàng loạt |

Sai lầm phổ biến nhất: dùng survey để hỏi "tại sao" (câu trả lời tích chọn sẵn ép người trả lời vào khung có sẵn, mất hết insight thật) hoặc dùng interview để đo tỷ lệ (mẫu quá nhỏ, không đại diện).

### Bước 2 — Thiết kế Survey (nếu chọn định lượng)

**Nguyên tắc câu hỏi:**
- Mỗi câu chỉ hỏi 1 thứ — "Bạn có hài lòng về giá và dịch vụ không" là 2 câu hỏi trộn làm 1, không phân tích được
- Tránh câu hỏi dẫn dắt ("Bạn có đồng ý rằng dịch vụ X rất tốt không?" — đã cài sẵn câu trả lời mong muốn)
- Thang đo nhất quán (vd Likert 1-5 xuyên suốt, không đổi thang giữa chừng)
- Câu hỏi nhân khẩu học để CUỐI form, không đầu (đầu form nên là câu dễ trả lời, giữ chân người làm khảo sát)
- Test thử trên 3-5 người trước khi gửi diện rộng — bắt lỗi câu hỏi mơ hồ

**Cấu trúc form chuẩn:**
```
1. Câu hỏi sàng lọc (screening) — xác nhận đúng đối tượng cần khảo sát
2. Câu hỏi hành vi hiện tại (dễ trả lời, khởi động)
3. Câu hỏi thái độ/đánh giá (core của khảo sát)
4. Câu hỏi mở (tối đa 1-2 câu, để không mất động lực trả lời)
5. Nhân khẩu học (cuối cùng)
```

**Sample size tối thiểu** (để kết luận có ý nghĩa thống kê cơ bản):
- Khảo sát thăm dò nhanh: 30+ là chấp nhận được để thấy xu hướng thô
- Khảo sát ra quyết định quan trọng: 100+ tuỳ độ biến thiên của câu trả lời
- Càng nhiều phân khúc muốn so sánh (theo tuổi, theo khu vực...) → cần mẫu lớn hơn để mỗi phân khúc đủ số

### Bước 3 — Thiết kế Interview Guide (nếu chọn định tính)

**Cấu trúc guide chuẩn (semi-structured — có khung nhưng linh hoạt):**
```
1. Mở đầu: giới thiệu mục đích, xin phép ghi âm, trấn an không có câu trả lời sai
2. Câu hỏi khởi động: dễ, về bối cảnh chung (giúp người được hỏi thoải mái)
3. Câu hỏi chính: mở (open-ended), không dẫn dắt
   - "Kể cho tôi nghe về lần gần nhất bạn..." (tốt — mời kể chuyện cụ thể)
   - "Bạn có thích X không?" (kém — dễ trả lời có/không cụt lủn)
4. Follow-up probes chuẩn bị sẵn: "Vì sao lại vậy?", "Cho tôi ví dụ cụ thể được không?"
5. Kết thúc: hỏi có gì muốn bổ sung không, cảm ơn
```

**Nguyên tắc phỏng vấn:**
- Im lặng sau câu hỏi — đừng vội lấp khoảng trống, người được hỏi cần thời gian nghĩ
- Hỏi về hành vi THẬT đã làm ("lần gần nhất bạn...") thay vì ý định giả định ("bạn có sẽ...") — con người dự đoán hành vi tương lai của chính mình rất tệ
- 5-8 người/nhóm đối tượng thường đủ để bắt đầu thấy pattern lặp lại (data saturation) — không cần quá nhiều để bắt đầu có insight

### Bước 4 — Phân tích kết quả

**Survey:** dùng `statistical-analysis` skill đã có trong Capability Map — thống kê mô tả trước, kiểm định nếu so sánh nhóm.

**Interview:** coding theo theme — đọc hết transcript, gắn nhãn theo chủ đề lặp lại, đếm tần suất theme xuất hiện qua các người được phỏng vấn (không phải trích 1 câu nói hay rồi kết luận đại diện cho tất cả).

## Ví dụ thực tế
Áp cho ABTRIP: research-synthesis đã tìm hết nguồn công khai mà không ai nói rõ "khách chọn Fast Track Nội Bài vì lý do gì cụ thể so với đối thủ". Đây đúng dạng câu hỏi "tại sao" → chọn Interview, không Survey. Thiết kế guide 5 câu hỏi mở, phỏng vấn 6-8 khách hàng gần đây, hỏi "kể lại lần gần nhất bạn đặt Fast Track — lúc đó bạn đang lo gì, so sánh với lựa chọn nào khác không". Sau 6-8 phỏng vấn thấy lặp lại theme "sợ trễ giờ bay hơn là sợ tốn tiền" → đây là insight thứ nguồn thứ cấp không bao giờ cho ra được.

## Lưu ý / Lỗi thường gặp
- Đừng trộn định lượng và định tính trong cùng 1 câu hỏi nghiên cứu — chọn rõ 1 cái trước
- Mẫu tự chọn (self-selected, chỉ người rảnh mới trả lời khảo sát) luôn có bias — nói rõ giới hạn này khi báo cáo, đừng khẳng định chắc như mẫu ngẫu nhiên
- Phỏng vấn hỏi "bạn có sẽ mua sản phẩm mới này không" gần như vô giá trị — con người luôn nói có vì lịch sự, hành vi mua thật khác hẳn lời hứa
- Không đủ nguồn lực làm cả survey lẫn interview → ưu tiên interview trước nếu câu hỏi thuộc dạng "tại sao"/còn mơ hồ, vì nó rẻ hơn và giúp thiết kế survey sau tốt hơn nhiều

## Đánh giá cá nhân
- Điểm mạnh: vá đúng lỗ hổng "chỉ giỏi tổng hợp nguồn có sẵn" của agent — nhiều câu hỏi kinh doanh quan trọng nhất (tại sao khách rời bỏ, tại sao chọn mình) không nguồn thứ cấp nào trả lời được
- Điểm yếu: tốn thời gian/công sức hơn nhiều so với research thứ cấp — không phải lúc nào cũng đáng làm, cần cân nhắc chi phí/lợi ích trước khi chọn hướng này
- Có nên dùng: 8/10 — không dùng thường xuyên như research-synthesis, nhưng khi cần thì không có thay thế nào khác cho ra insight thật

## Link
- Không có nguồn bên ngoài cụ thể — tổng hợp từ nguyên tắc UX research/market research cổ điển
