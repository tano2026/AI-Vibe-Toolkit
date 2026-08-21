---
name: ad-budget-testing-discipline
description: >
  Vận hành hoá EXPERT-CORE.md section ② MARKETING — luật ngân sách, kill
  rule cho ad set/creative, luật A/B test (sample size, không peeking),
  luật attribution, luật frequency retargeting. Dùng khi chạy/quản lý ads
  (Meta/Google/TikTok Ads), quyết định tắt/scale campaign, hoặc thiết kế
  A/B test.
---

# Ad Budget & Testing Discipline

## TL;DR
Ngân sách/kill rule đã có công cụ mạnh hơn (`claude-ads/ads-budget.md` + `ads-audit.md`) — dùng luôn, đừng tự làm tay. Skill này giờ chỉ giữ đúng phần chưa ai làm: A/B test discipline (sample size, không peeking), luật attribution, luật frequency retargeting.

## Khi nào dùng
- Bắt đầu campaign mới, chưa có data lịch sử để chia ngân sách
- Đang chạy campaign, cần quyết định tắt/giữ 1 ad set hay creative
- Thiết kế A/B test cho content/landing page/ads
- Viết report có claim tăng trưởng liên quan tới đổi attribution model
- Chạy retargeting, cần biết tần suất hợp lý

## Nội dung skill / prompt

## ⚠️ Đã sửa sau khi phát hiện trùng lặp (audit 21/08/2026)

Phát hiện kho đã có `skills/claude-ads/ads-budget.md` + `ads-audit.md` — dùng đúng "70/20/10 rule, 3x Kill Rule, 20% scaling rule" y hệt, nhưng **trưởng thành hơn nhiều** (có hệ thống scoring 0-100, subagent delegation cho 6 platform, đã test `tested_date: 2026-05-17`). Mục 1 và 2 dưới đây ĐÃ ĐƯỢC THAY bằng tham chiếu, không lặp lại nội dung — chỉ giữ mục 3-5 (A/B test, attribution, frequency) vì đây là phần KHÔNG có trong `claude-ads/*`.

### 1-2. Luật budget & Kill rule — dùng `claude-ads/ads-budget.md` + `ads-audit.md`

```
KHÔNG tự tính budget/kill rule bằng tay nữa — gọi skill claude-ads/ads-budget
cho budget allocation + bidding strategy, gọi claude-ads/ads-audit cho full
audit đa nền tảng (Google/Meta/LinkedIn/TikTok/Microsoft) kèm health score
0-100 và kill list tự động.

Vẫn đúng luật gốc EXPERT-CORE (70/20/10, 3x Kill Rule) — chỉ là đã có công
cụ mạnh hơn thực thi, không cần tự làm tay.
```

### 3. Luật A/B test (KHÔNG có trong claude-ads/* — giữ nguyên)

```
1 BIẾN/LẦN — đổi nhiều biến cùng lúc không biết cái nào tạo ra khác biệt.

Tính sample TRƯỚC khi chạy, không chạy xong mới tính:
  Quy tắc thô: cần ~100 conversion/variant mới gọi tên "winner" cho khác
  biệt ~20%. Ít hơn → chỉ được nói "tín hiệu", KHÔNG được nói "kết luận".

KHÔNG dừng test sớm vì "đang thắng" — peeking (nhìn giữa chừng rồi dừng
khi thấy thắng) là lỗi thống kê kinh điển, kết luận từ peeking không đáng
tin dù nhìn có vẻ rõ ràng.
```

### 4. Luật attribution

```
Khai báo model đang dùng trong MỌI report (mặc định last-click vì đơn
giản + nhất quán, trừ khi có lý do đổi).

Đổi model attribution KHÔNG PHẢI = tăng trưởng thật — cấm claim kiểu
"tăng trưởng X%" khi thực chất chỉ là đổi cách đo, không đổi kết quả
thật. Đây là cách "gian lận" báo cáo phổ biến, dù không cố ý.
```

### 5. Luật frequency

```
Retargeting cap: 2-3 LẦN/TUẦN/NGƯỜI.
Tần suất cao hơn = đốt tiền + hại brand (banner blindness, khó chịu).
```

### Anti-pattern (tự kiểm tra không mắc phải)

```
❌ Chọn kênh vì đang trend — chọn theo data/audience fit, không theo
   "ai cũng đang làm X"
❌ KPI là vanity metric (reach, like) cho campaign mục tiêu conversion —
   KPI phải khớp mục tiêu thật của campaign
❌ Scale ad set thắng bằng cách tăng budget >30%/ngày — vỡ learning
   phase, thuật toán phải học lại từ đầu, phản tác dụng
❌ Báo cáo ROAS mà giấu tỷ lệ organic lẫn vào — ROAS tính cả traffic
   organic là con số phóng đại, gây hiểu nhầm hiệu quả ads thật
```

## Setup từng bước
1. Campaign mới, chưa data → áp 70/20/10, không tự nghĩ ra tỷ lệ khác
2. Đang chạy → check kill rule mỗi lần review (3× CPA/0 conversion, hoặc CPA >1.5× target sau learning)
3. Creative CTR thấp → check < 1/2 median 3 ngày, đúng ngưỡng mới thay, không thay theo cảm tính
4. Thiết kế A/B test → tính sample trước, chỉ 1 biến, không peek giữa chừng
5. Viết report → luôn khai báo attribution model đang dùng
6. Retargeting → set cap 2-3 lần/tuần/người, không để mặc định thuật toán tự quyết

## Ví dụ thực tế
Chạy ads cho gói AI automation Tano Agency, ngân sách mới lần đầu (chưa có data lịch sử): 70% vào kênh Facebook Ads (đã proven cho SMB VN theo kinh nghiệm ngành), 20% test TikTok Ads (giả thuyết: đối tượng chủ shop trẻ dùng TikTok nhiều), 10% thử Google Search (moonshot, chưa chắc SMB tìm kiếm "AI automation" trực tiếp). Sau 2 tuần, ad set Facebook có CPA = 1.7× target sau khi đã qua learning phase → tắt theo đúng kill rule, không "chờ thêm vài ngày xem sao" lần 2.

## Lưu ý / Lỗi thường gặp
- Tắt ad set trong lúc đang learning phase là lỗi phổ biến — chưa đủ data để đánh giá công bằng, cần đợi qua learning mới áp kill rule
- Peeking A/B test là lỗi thống kê hay gặp nhất — thấy "đang thắng" giữa chừng rồi dừng ngay, kết luận đó thường không đáng tin
- Đổi attribution model rồi báo "tăng trưởng" — dễ tự lừa dối chính mình nếu không khai báo rõ model đang dùng

## Đánh giá cá nhân
- Điểm mạnh: ngưỡng số rõ ràng (70/20/10, 3×/1.5× CPA, 100 conversion/variant, 2-3 lần/tuần) — loại bỏ quyết định cảm tính, dễ audit lại sau
- Điểm yếu: cần platform ads cung cấp đủ data (CPA thật, CTR median campaign) để áp đúng — nếu thiếu data, khó áp máy móc
- Có nên dùng: 9/10 — luật "không thương lượng" theo EXPERT-CORE, đặc biệt quan trọng khi bắt đầu chạy ads thật (chưa từng chạy trước đó)

## Link
- Nguồn gốc luật: `agents/company/EXPERT-CORE.md` section ② MARKETING
- **Dùng cùng (không lặp lại):** `skills/claude-ads/ads-budget.md`, `skills/claude-ads/ads-audit.md` — budget allocation + kill rule + health scoring đã có sẵn, mạnh hơn
