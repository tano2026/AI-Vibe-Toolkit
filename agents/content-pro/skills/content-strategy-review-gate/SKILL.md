---
name: content-strategy-review-gate
description: >
  Stress-test khung Pillar/Cluster + kế hoạch content TRƯỚC KHI bắt đầu sản
  xuất — tương đương ceo-stress-test-and-roadmap nhưng cho chiến lược
  content thay vì báo cáo thị trường. Dùng ngay sau khi
  content-pillar-cluster-architecture ra khung, trước khi giao viết.
---

# Content Strategy Review Gate

## TL;DR
Khung Pillar/Cluster nghe hợp lý không có nghĩa là đúng — pillar có thể dựa trên suy đoán thay vì insight thật, cluster có thể trùng lặp, nhịp đăng có thể không bền vững. 5 câu hỏi bắt buộc trước khi bắt đầu sản xuất, tránh đổ công sức vào khung sai từ đầu.

## Khi nào dùng
- Ngay sau khi có khung Pillar/Cluster mới (từ `content-pillar-cluster-architecture`), trước khi giao viết hàng loạt
- Định kỳ review lại khung cũ (mỗi 3-6 tháng) — xem còn đúng không hay cần điều chỉnh
- Khi content sản xuất ra đều đặn nhưng hiệu quả không như kỳ vọng — nghi ngờ khung gốc có vấn đề

## Nội dung skill / prompt

### 5 câu hỏi bắt buộc (chạy trước khi giao sản xuất)

**1. Insight-vs-Assumption check**
Pillar có bắt nguồn từ insight khách hàng THẬT (interview, social listening, dữ liệu bán hàng) không, hay chỉ là "nghe hợp lý"? Nếu là suy đoán → dừng lại, chạy `primary-research-design` hoặc `social-listening-research` trước.

**2. Authority check**
Brand có thẩm quyền THẬT để nói về pillar này không? (Không phải "chủ đề đang hot" mà brand chưa từng có kinh nghiệm/dữ liệu thật về nó). Thiếu thẩm quyền → content generic, mất niềm tin dài hạn dù ngắn hạn có thể viral.

**3. Cadence Sustainability check**
**[FACT, nguồn Digital Applied 2026]** "Cadence beats volume — 2 bài/tuần bền vững thắng 5 bài/tuần không bền vững." Lịch đăng đề xuất có duy trì được liên tục 12 tháng với nguồn lực hiện tại không, hay chỉ làm nổi vài tuần đầu rồi đuối?

**4. Cluster Overlap check**
Các cluster topic trong cùng 1 pillar có bị trùng ý quá 70% không? (Kiểm bằng cách tự hỏi: nếu đọc 2 cluster topic cạnh nhau, người đọc có thấy dư thừa không). Trùng nhiều → gộp lại hoặc tách góc nhìn rõ hơn.

**5. Distribution Feasibility check**
Kế hoạch phân phối (`content-distribution-system`) có thực tế với nguồn lực hiện có không, hay chỉ là danh sách task lý tưởng không ai làm nổi? Đối chiếu số task phân phối với số người/giờ thực tế có.

### Verdict Gate

```
Cả 5 câu PASS → duyệt khung, giao sản xuất
≥1 câu FAIL → không giao sản xuất ngay, quay lại sửa đúng chỗ fail,
              chạy lại cả 5 câu (không chỉ câu vừa sửa — sửa 1 chỗ có
              thể ảnh hưởng chỗ khác)
```

## Setup từng bước
1. Có khung Pillar/Cluster mới từ `content-pillar-cluster-architecture` → chạy 5 câu hỏi trên
2. Bất kỳ câu nào FAIL → note cụ thể lý do, không chung chung "có vẻ chưa ổn"
3. Sửa khung theo đúng lỗi đã chỉ ra
4. Chạy lại đủ 5 câu (không skip câu đã pass trước đó — thay đổi 1 phần có thể phá phần khác)
5. Cả 5 PASS → duyệt, giao `editorial-workflow-quality-gates` bắt đầu sản xuất

## Ví dụ thực tế
Khung Trùm Sân Bay đề xuất pillar "Kinh nghiệm bay quốc tế lần đầu" — check Authority: Trùm Sân Bay có thẩm quyền thật (đã làm dịch vụ Fast Track/SIM/đổi tiền cho khách quốc tế) → PASS. Check Cadence: đề xuất ban đầu 5 video/tuần cho pillar mới trong khi kênh hiện chỉ có 1 người sản xuất → FAIL, cần hạ xuống 2-3 video/tuần bền vững hơn theo đúng nguyên tắc "cadence beats volume".

## Lưu ý / Lỗi thường gặp
- Đừng chạy skill này SAU KHI đã sản xuất hàng loạt — phải chạy TRƯỚC, phát hiện muộn tốn công sức đã bỏ ra
- Câu hỏi Cadence hay bị bỏ qua nhất vì lịch đăng "trông đẹp trên giấy" — luôn đối chiếu với nguồn lực thật, không lý tưởng hoá
- Không tự nới lỏng cả 5 câu chỉ vì đang gấp deadline — nếu thực sự cần content gấp, đó là content one-off, không phải content theo khung Pillar/Cluster dài hạn

## Đánh giá cá nhân
- Điểm mạnh: bắt lỗi khung chiến lược sớm, trước khi tốn công sản xuất theo khung sai; câu hỏi Cadence là insight thực tế hay bị bỏ qua
- Điểm yếu: thêm 1 bước trước khi sản xuất — không hợp cho content one-off/thời sự cần gấp
- Có nên dùng: 9/10 cho mọi khung Pillar/Cluster mới hoặc review định kỳ; không cần cho content thử nghiệm nhỏ

## Link
- Tham chiếu: `agents/research-analytics-pro/skills/ceo-stress-test-and-roadmap` (cùng triết lý, khác domain)
- Digital Applied — Content Calendar Template 2026 (nguồn nguyên tắc Cadence)
