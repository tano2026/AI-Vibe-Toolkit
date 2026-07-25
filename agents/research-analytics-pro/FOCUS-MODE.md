---
name: focus-mode
description: >
  Cơ chế khoá research-analytics-pro vào 1 domain/pack duy nhất trong 1 khoảng thời gian,
  tích luỹ state qua các tuần thay vì research rời rạc mỗi lần từ đầu. Dùng khi cần theo dõi
  liên tục 1 ngành/1 domain (đặc biệt local business) thay vì trả lời 1 câu hỏi rời.
version: 1.0
updated: 2026-07-25
---

# Focus Mode — Nghiên cứu tập trung 1 ngành

> Đọc kèm: `ARCHITECTURE.md`, `domain-playbooks.md`, `skills/local-gap-finder/SKILL.md`,
> `agents/company/OPERATING-RHYTHM.md` (lịch xoay vòng daily scan đã có sẵn — Focus Mode
> KHÔNG tạo lịch song song, chỉ định nghĩa research chạy sâu hơn thế nào trong slot đã có).

---

## Vấn đề Focus Mode giải quyết

Research mặc định (Scout→Validator→Analyst→Synthesizer) trả lời 1 câu hỏi rồi xong — không
nhớ đã research domain này tuần trước ra sao, không so sánh được thay đổi theo thời gian.
Với domain cần theo dõi liên tục (local business cạnh tranh theo địa lý, hoặc bất kỳ domain
nào Nobitano muốn "khoá" trong 1 giai đoạn) — cần tích luỹ, không phải research lại từ đầu
mỗi lần.

## Cách kích hoạt

**Cách 1 — Tự động qua lịch xoay vòng đã có (`OPERATING-RHYTHM.md` mục 1):**
```
T2 abtrip+an-binh · T3 trum-san-bay · T4 airfare-decoded · T5 gmsp · T6 ai-review · T7 tổng hợp đối thủ
```
Khi domain trong ngày là **local business** (abtrip/an-binh, tano-cafe) → daily scan tự động
chạy pipeline `local-gap-finder` thay vì scan chung chung. Domain không phải local business
→ giữ nguyên research scan bình thường như hiện tại, không đổi.

**Cách 2 — Thủ công:** Nobitano gõ `/focus <pack>` → khoá research vào đúng pack đó cho tới
khi có lệnh `/unfocus` hoặc hết 1 tuần (mặc định).

## Cơ chế tích luỹ state

```
Mỗi Chủ nhật 20:00 (khớp "Weekly report" đã có trong OPERATING-RHYTHM.md mục 2):
  1. Hermes chạy local-gap-finder cho pack đang Focus
  2. Trước khi viết report mới → fetch report tuần trước tại /reports/<pack>/YYYY-WW.md
  3. So sánh:
     - Gap nào tuần trước rank cao, tuần này đối thủ đã fill → đánh dấu ĐÃ ĐÓNG
     - Gap nào mới xuất hiện tuần này → đánh dấu MỚI
     - Gap Score đổi >2 điểm → note "biến động mạnh", nêu lý do nếu xác định được
  4. Report mới = Ranked Opportunity List hiện tại + mục "Thay đổi so với tuần trước"
  5. Push /reports/<pack>/YYYY-WW.md (không ghi đè tuần cũ — mỗi tuần 1 file, giữ lịch sử)
```

## Định dạng lưu trữ

```
/reports/
├── README.md                    ← quy ước đặt tên, không phải report
├── abtrip/
│   ├── 2026-W30.md
│   ├── 2026-W31.md
│   └── ...
├── an-binh/
├── tano-cafe/
└── <pack khác nếu bật Focus Mode>/
```
Tên file: `YYYY-Wnn.md` (ISO week). Mỗi file là 1 snapshot đầy đủ, không phải diff — diff nằm
trong mục "Thay đổi so với tuần trước" bên trong file mới nhất.

## Khi nào escalate lên Morning Brief (thứ 2, theo OPERATING-RHYTHM.md mục 2)

- Gap mới xuất hiện với Gap Score ≥8/10 → đưa vào Morning Brief, không đợi Nobitano hỏi
- Gap đã đóng mà mình chưa kịp fill → đưa vào Morning Brief kèm cảnh báo "đối thủ đi trước"
- Biến động Gap Score bất thường không giải thích được bằng data hiện có → escalate lên
  Senior Advisor (`agents/company/SENIOR-ADVISOR.md`) nếu cần thiết kế lại tiêu chí đo

## Domain nào bật Focus Mode mặc định

| Pack | Focus Mode | Vì sao |
|---|---|---|
| abtrip, an-binh | ✅ Mặc định bật | Local business, cạnh tranh theo địa lý rõ |
| tano-cafe | ✅ Mặc định bật | Local business, F&B gần sân bay |
| trum-san-bay, airfare-decoded, gmsp, ai-review | ❌ Không bật | Content/media channel, không cạnh tranh theo địa lý — dùng research scan thường |

Muốn bật Focus Mode cho pack khác → Nobitano tự `/focus <pack>`, không cần sửa file này.
