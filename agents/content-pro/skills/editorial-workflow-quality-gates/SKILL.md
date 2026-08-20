---
name: editorial-workflow-quality-gates
description: >
  Quy trình biên tập từ ý tưởng tới xuất bản, mỗi bước có owner + output rõ
  ràng + gate duyệt trước khi qua bước tiếp. Dùng khi content được sản xuất
  mà không ai rõ ai duyệt gì, hoặc content đăng lên có lỗi/sai lệch voice mà
  lẽ ra phải bắt được trước khi publish.
---

# Editorial Workflow & Quality Gates

## TL;DR
"Viết xong là đăng" không có quy trình kiểm soát chất lượng — dễ đăng nội dung sai fact, lệch voice, hoặc trùng ý đã viết trước đó. Quy trình 5 bước chuẩn, mỗi bước có gate rõ ràng, không bước nào được bỏ qua dù gấp tới đâu.

## Khi nào dùng
- Thiết lập quy trình sản xuất content mới cho kênh/team
- Content hiện tại hay bị lỗi (sai fact, lệch voice, trùng lặp) sau khi đăng — dấu hiệu thiếu gate
- Nhiều người cùng viết cho 1 kênh, cần chuẩn hoá để giọng điệu nhất quán

## Nội dung skill / prompt

### 5 bước, mỗi bước có Owner + Output + Gate

```
BƯỚC 1 — RESEARCH (Owner: người phụ trách chủ đề)
  Output: chủ đề đã map vào đúng Pillar/Cluster (dùng
          content-pillar-cluster-architecture), có nguồn tham khảo nếu có claim
  Gate: chủ đề có trùng bài đã viết trong cùng cluster không? Có claim
        cần fact-check không?

BƯỚC 2 — BRIEF (Owner: người phụ trách chủ đề hoặc editor)
  Output: tài liệu brief đủ chi tiết để người viết KHÔNG cần hỏi lại —
          gồm: góc độ, đối tượng, outline, nguồn cần trích, tone, CTA
  Gate: brief đủ rõ để 1 người khác (không phải người brief) viết được
        không cần hỏi thêm?

BƯỚC 3 — DRAFT (Owner: người viết)
  Output: bản nháp đầy đủ, đúng độ dài/tone theo brief
  Gate: bám đúng brief không? (không tự đổi hướng giữa chừng mà không báo)

BƯỚC 4 — EDIT/REVIEW (Owner: người khác với người viết — không tự review)
  Output: bản đã sửa, có ghi chú thay đổi
  Gate: chạy qua fact-checker (nếu có claim) + anti-ai-tells (nếu cần tự
        nhiên hoá) + brand-voice/personal-voice check (giọng đúng brand
        không, không lệch)

BƯỚC 5 — PUBLISH + DISTRIBUTE (Owner: người vận hành kênh)
  Output: content đã đăng + kế hoạch phân phối đi kèm (xem
          content-distribution-system — không đăng xong là hết việc)
  Gate: đã gắn task phân phối (email/social post/repurpose) trước khi
        tính là "xong" chưa?
```

### Nguyên tắc bất biến
- **Người review KHÔNG PHẢI người viết** — tự review chia sẻ cùng điểm mù với chính mình (đúng nguyên tắc đã áp cho `research-independent-review-gate`)
- **Không bỏ qua bước dù gấp** — content gấp thì rút ngắn THỜI GIAN mỗi bước, không bỏ hẳn bước nào
- **Brief phải đủ để người khác viết được** — nếu chỉ người brief mới hiểu được ý, đó là brief thiếu, không phải người viết kém

## Setup từng bước
1. Xác định ai đảm nhiệm vai trò nào trong 5 bước (có thể 1 người kiêm nhiều vai với content nhỏ, nhưng KHÔNG kiêm cả viết lẫn review)
2. Chuẩn hoá template Brief (dùng chung form, không mỗi lần viết lại từ đầu)
3. Gắn checklist Gate vào từng bước — có thể làm dạng Airtable status (Research → Brief → Draft → Review → Published)
4. Review định kỳ: content nào hay bị lỗi ở gate nào — đó là chỗ quy trình yếu, cần củng cố

## Ví dụ thực tế
Trùm Sân Bay hiện có pipeline 9-agent nhưng caption/thumbnail/publish vẫn thao tác thủ công — áp workflow này: Bước 1-2 (Research+Brief) do Content Research skill làm tự động, Bước 3 (Draft) do script-writer skill, Bước 4 (Edit) BẮT BUỘC qua fact-checker trước khi Bước 5 — hiện tại bước 4 có thể đang bị bỏ qua (theo ghi nhận "chưa fully automated"), đây chính là điểm cần vá trước tiên.

## Lưu ý / Lỗi thường gặp
- Content gấp thường bị bỏ hẳn Bước 4 (Review) — đây là lỗi phổ biến nhất, chính lúc gấp mới dễ sai nhất
- Brief sơ sài khiến người viết phải tự đoán ý — dẫn tới draft lệch hướng, tốn công sửa nhiều hơn là brief kỹ từ đầu
- Đừng để 1 người vừa viết vừa tự duyệt cho chính mình trừ khi thực sự không có ai khác — nếu vậy, ít nhất cách 1 khoảng thời gian rồi tự đọc lại (không review ngay sau khi viết xong)

## Đánh giá cá nhân
- Điểm mạnh: đơn giản, áp được ngay vào pipeline hiện có mà không cần đổi tool, chỉ cần rõ ai làm gì và gate ở đâu
- Điểm yếu: thêm bước = thêm thời gian — với content khối lượng lớn/tần suất cao có thể cần rút gọn (gộp bước 1-2 hoặc 3-4) tuỳ độ rủi ro nội dung
- Có nên dùng: 9/10 — bất kỳ kênh nào có từ 2 người trở lên làm content nên có quy trình này; kênh 1 người vẫn nên tự áp gate (dù không tách được người khác review)

## Link
- Digital Applied — Content Calendar Template 2026 (nguồn quy trình 7 bước gốc, đã rút gọn còn 5 cho thực tế Tano Agency)
