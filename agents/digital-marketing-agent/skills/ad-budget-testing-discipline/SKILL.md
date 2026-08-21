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
`digital-marketing-orchestrator` hiện chưa có bất kỳ ngưỡng số cụ thể nào cho ngân sách/kill rule/A/B test — mọi quyết định đang dựa cảm tính. Skill này vận hành hoá luật đã có sẵn trong EXPERT-CORE ②, áp trực tiếp cho mọi campaign chạy thật.

## Khi nào dùng
- Bắt đầu campaign mới, chưa có data lịch sử để chia ngân sách
- Đang chạy campaign, cần quyết định tắt/giữ 1 ad set hay creative
- Thiết kế A/B test cho content/landing page/ads
- Viết report có claim tăng trưởng liên quan tới đổi attribution model
- Chạy retargeting, cần biết tần suất hợp lý

## Nội dung skill / prompt

### 1. Luật budget

```
Chưa có data lịch sử → split khởi điểm 70/20/10:
  70% kênh đã proven (hoặc kênh an toàn nhất theo ngành nếu chưa proven)
  20% kênh test có giả thuyết cụ thể
  10% moonshot (thử nghiệm mạo hiểm, chấp nhận mất)

Có data rồi → shift dần theo CPA thật, mỗi lần dịch ngân sách ≤15% tổng
budget (không đảo 180 độ 1 lần)

Chạy dài hạn (>3 tháng) → tối thiểu 20% dành cho brand/content nền,
KHÔNG dồn 100% vào performance — CAC sẽ leo dần khi audience lạnh cạn
(hiệu ứng đã biết trước, không phải rủi ro bất ngờ).
```

### 2. Kill rule mặc định

```
Ad set: TẮT khi
  - Spend ≥ 3× CPA target mà 0 conversion, HOẶC
  - CPA thực > 1.5× target SAU KHI đã qua learning phase (không tắt
    trong lúc đang learning — chưa đủ data để đánh giá)

Creative: THAY khi CTR < 1/2 median của campaign sau 3 ngày chạy

KHÔNG "để thêm vài ngày xem sao" quá 1 LẦN cho cùng 1 ad set — cho thêm
cơ hội 1 lần là hợp lý, lần thứ 2 là trì hoãn quyết định đã rõ.
```

### 3. Luật A/B test

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
- Bổ sung cho: `agents/digital-marketing-agent/skills/digital-marketing-orchestrator/SKILL.md`
