---
name: deal-scoring-forecast-discipline
description: >
  Operationalize luật scoring/cadence/objection/pricing/forecast/CRM đã có
  sẵn trong agents/company/EXPERT-CORE.md section ③ SALES — biến từ "1 dòng
  nhắc tên file" thành skill thật dùng được. Dùng khi cần chấm điểm lead
  mới, lên lịch touch, xử lý objection, forecast pipeline, hoặc audit CRM.
  KHÔNG dùng MEDDIC/framework enterprise ngoài — luật này may đo riêng cho
  SMB Việt Nam (deal nhỏ, chu kỳ ngắn, người quyết = chủ doanh nghiệp).
---

# Deal Scoring & Forecast Discipline (SMB Việt Nam)

## TL;DR
`EXPERT-CORE.md` section ③ đã có đủ luật số cụ thể (scoring, cadence, objection, pricing, forecast, CRM) nhưng trước giờ chỉ được `sales-ceo` nhắc tên 1 dòng, chưa ai thực sự dùng có hệ thống. Skill này là bản vận hành thật — copy-paste áp được ngay, không phải đọc lại cả EXPERT-CORE mỗi lần cần 1 luật.

## ⚠️ Vì sao không dùng MEDDIC
Research xác nhận: MEDDIC hợp deal **$500K+, chu kỳ 9 tháng, 6-10 stakeholder** (enterprise). Nobitano bán giải pháp AI cho **SMB VN — chủ doanh nghiệp nhỏ quyết trực tiếp, chu kỳ ngắn, deal nhỏ** — đúng nhóm mà chính nguồn MEDDIC khuyên "BANT/CHAMP hợp hơn". Luật trong EXPERT-CORE ③ vốn đã được thiết kế đúng tầm SMB VN (không phải BANT/CHAMP nguyên bản, mà là bản tự chế phù hợp thực tế) — không cần nhập framework ngoài.

## Khi nào dùng
- Có lead mới cần quyết định outreach ngay hay nurture hay bỏ
- Đang follow-up 1 deal, cần biết touch tiếp theo là gì/khi nào
- Khách đưa ra objection (giá, tính năng, thời gian)
- Cần forecast doanh thu quý/tháng cho pipeline hiện tại
- Audit CRM định kỳ xem deal nào đang "chết" mà không ai để ý

## Nội dung skill / prompt

### 1. Scoring & ưu tiên lead

```
2 trục, mỗi trục chấm 0-5:
  FIT (đúng ICP không): ngành / quy mô nhân sự / doanh thu ước / mức độ
       số hoá hiện tại / ai là người quyết (owner trực tiếp = tốt, chu kỳ ngắn)
  INTENT (tín hiệu mua): đã hỏi giá? đã xem demo? referral từ khách cũ?
       chủ động inbound hay bị outbound tiếp cận?

Tổng điểm:
  ≥7  → outreach trong 24h
  5-6 → nurture (đưa vào cadence dài hơn, chưa ưu tiên ngay)
  <5  → KHÔNG đụng — đừng đốt thời gian "biết đâu"

Lead không rõ ≥3/5 tiêu chí FIT → xếp nurture, CHƯA outreach (theo đúng
nguyên tắc ICP firmographics đã có trong system-prompt sales-ceo).

Inbound lead: phản hồi trong giờ làm việc ≤2h — tốc độ phản hồi là biến số
mạnh nhất của conversion inbound, quan trọng hơn cả nội dung phản hồi.
```

### 2. Cadence — nhịp theo dõi

```
Touch theo nhịp: ngày 1 → 3 → 7 → 14
Tối đa 4 touch không phản hồi → nghỉ 30 ngày → 1 touch "break-up"
  ("Có vẻ chưa đúng thời điểm, mình dừng đây, khi nào cần cứ nhắn lại")

Mỗi touch PHẢI thêm giá trị mới (insight, case study, tài liệu) —
lặp lại "anh chị xem chưa ạ" = spam, không phải follow-up.
```

### 3. Xử lý objection

```
Trình tự bắt buộc: Ack → Isolate → Answer → Confirm

Ack:     Thừa nhận mối lo của khách trước, không vội bào chữa
Isolate: "Ngoài giá ra còn điểm nào khiến anh/chị chưa quyết không?"
         (tìm objection THẬT trước khi trả lời — objection nêu ra đầu
         tiên thường không phải objection thật)
Answer:  Trả lời đúng objection đã isolate được (không trả lời cái chưa hỏi)
Confirm: "Vậy nếu giải quyết được [X], mình tiến hành được chứ?"

KHÔNG answer trước khi isolate — trả lời objection giả (khách nói cho có)
là đốt đạn vào chỗ không cần thiết.
```

### 4. Luật giá

```
KHÔNG BAO GIỜ giảm giá đơn thuần — đổi scope/điều kiện thay vào:
  - Thanh toán trước (toàn bộ hoặc phần lớn)
  - Cam kết dài hạn hơn (6 tháng thay vì 1 tháng)
  - Bớt hạng mục (giảm scope tương ứng giảm giá, không giảm giá giữ nguyên scope)

Trần giảm giá theo PACK (nếu deal có brief/PACK riêng, dùng ngưỡng đó).
PACK không ghi → MỌI nhượng giá cần Nobitano duyệt, không tự quyết.
```

### 5. Forecast — không cộng "cảm giác sắp chốt"

```
commit    = xác suất ≥90% (khách đã đồng ý điều khoản, chỉ chờ ký/thanh toán)
best-case = xác suất ≥60% (đàm phán tích cực, chưa chốt điều khoản)
còn lại   = pipeline, weighted theo stage (không đưa vào commit/best-case)

KHÔNG cộng "cảm giác sắp chốt" vào commit — commit chỉ tính khi có bằng
chứng cụ thể (khách đã đồng ý điều khoản bằng văn bản/lời nói rõ ràng),
không phải vì rep "cảm thấy" deal sắp xong.
```

### 6. Vệ sinh CRM

```
Deal không có activity 14 ngày = stale flag — tự động cờ đỏ, không đợi
  ai nhớ ra mới kiểm tra
Mọi cuộc trao đổi log trong ngày (không để dồn qua hôm sau, dễ quên/sai)
Next-step + ngày cụ thể trên MỌI deal đang mở — deal không có next-step
  cụ thể = deal đang chết, dù chưa ai đánh dấu "lost"
```

### Anti-pattern (tự kiểm tra không mắc phải)

```
❌ Gửi cùng 1 template cho 50 lead — cá nhân hoá ít nhất dòng đầu là tối thiểu
❌ Hứa tính năng/giá chưa được duyệt — chỉ nói những gì đã confirm được
❌ Đàm phán qua email khi deal vượt ngưỡng — đẩy sang call (email dễ hiểu
   lầm, khó điều chỉnh linh hoạt khi deal lớn/phức tạp)
❌ Quên deal cũ đã "lost" — 90 ngày sau deal lost là nguồn lead ẤM NHẤT
   (hoàn cảnh khách có thể đã đổi, đáng touch lại, không phải bỏ hẳn)
```

## Setup từng bước
1. Lead mới vào → chấm FIT×INTENT ngay, quyết outreach/nurture/bỏ theo bảng điểm
2. Outreach → thiết lập cadence 1→3→7→14, note lại ngày touch tiếp theo trong CRM
3. Gặp objection → chạy đúng trình tự Ack→Isolate→Answer→Confirm, không nhảy bước
4. Khách đòi giảm giá → đổi scope/điều kiện, không giảm giá đơn thuần; vượt trần PACK → xin duyệt
5. Cuối tuần/tháng → forecast theo đúng ngưỡng commit ≥90%/best-case ≥60%, không thêm deal "cảm thấy ổn" vào commit
6. Định kỳ → audit CRM tìm deal stale ≥14 ngày, deal thiếu next-step

## Ví dụ thực tế
Lead mới hỏi về gói AI automation qua Zalo OA ABTRIP: FIT — chủ shop nhỏ, ngành travel liên quan, doanh thu ước trung bình, người nhắn trực tiếp là chủ (5/5 rõ ràng) = 4/5. INTENT — chủ động hỏi giá ngay từ tin đầu = 4/5. Tổng 8 → outreach trong 24h. Phản hồi trong 2h vì là inbound. Nếu sau đó khách nói "để suy nghĩ thêm" mà không nói rõ lý do → Isolate hỏi "ngoài giá ra còn điều gì khiến anh/chị chưa quyết không" trước khi vội giảm giá.

## Lưu ý / Lỗi thường gặp
- Isolate objection là bước hay bị bỏ qua nhất — reply thẳng vào "giá cao quá" bằng cách giảm giá ngay, trong khi objection thật có thể là lo ngại triển khai/thời gian, không phải giá
- Forecast commit dựa "cảm giác" là lỗi phổ biến nhất phá vỡ độ tin cậy forecast — luôn hỏi "bằng chứng cụ thể nào cho thấy khách đã đồng ý điều khoản?"
- Quên re-engage deal lost sau 90 ngày — đây là nguồn lead rẻ nhất bị bỏ qua thường xuyên nhất

## Đánh giá cá nhân
- Điểm mạnh: không phát minh gì mới — chỉ vận hành hoá luật đã có sẵn trong EXPERT-CORE, đúng tầm SMB VN thay vì nhập framework enterprise không hợp
- Điểm yếu: cần CRM thực tế đang dùng hỗ trợ track được stale flag/next-step tự động — nếu chưa có, phải làm thủ công, dễ bị bỏ sót
- Có nên dùng: 9/10 — đây là luật "không thương lượng" theo EXPERT-CORE, không phải optional

## Link
- Nguồn gốc luật: `agents/company/EXPERT-CORE.md` section ③ SALES
- Research đối chiếu: MEDDIC (Rework, Fullcast, Uplift GTM 2026) — xác nhận MEDDIC không hợp SMB, không áp dụng
