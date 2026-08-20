---
name: research-independent-review-gate
description: >
  Cấu hình santa-method (dual independent adversarial review có sẵn trong kho)
  riêng cho Research Analytics Pro — 2 reviewer độc lập, không thấy nhau,
  không thấy lý luận của agent đã viết báo cáo, mỗi người bắt loại lỗi khác
  nhau (Domain Expert bắt lỗi sự kiện/thuật ngữ, Red-team Analyst chủ động
  cãi lại verdict). Cả 2 phải pass mới được trình Nobitano. Dùng SAU
  `ceo-stress-test-and-roadmap` — 2 lớp bổ sung nhau, không thay thế nhau.
---

# Research Independent Review Gate — Dual review cho báo cáo research

## TL;DR
`ceo-stress-test-and-roadmap` là 1 checklist chạy tuần tự bởi cùng 1 "bộ não" đã viết báo cáo — vẫn có thể bỏ sót lỗi mà chính agent đó không tự thấy được (santa-method gọi đây là "chia sẻ bias với chính mình"). Skill này thêm lớp thứ 2: 2 reviewer ĐỘC LẬP, không nhìn thấy nhau, không thấy context của agent gốc, dùng đúng cơ chế `santa-method` đã có trong kho — cả 2 phải pass mới cho báo cáo qua.

## Khi nào dùng
- Sau khi báo cáo đã qua `ceo-stress-test-and-roadmap` (Phần A+B), TRƯỚC KHI trình Nobitano duyệt đầu tư thật
- Báo cáo dùng để quyết định số tiền/nguồn lực lớn — không cần cho báo cáo nội bộ tham khảo nhanh
- Khi nghi ngờ chính agent viết báo cáo có thể đã "tự tin thái quá" vào 1 hướng ngay từ đầu (confirmation bias xuyên suốt cả báo cáo, không phải lỗi cục bộ dò được bằng checklist)

## Nội dung skill / prompt

### Áp dụng kiến trúc santa-method (xem `skills/santa-method` để hiểu đầy đủ cơ chế gốc)

```
GENERATOR: Research Analytics Pro (đã viết báo cáo + qua ceo-stress-test)
        ↓ output = báo cáo đã stress-test
DUAL INDEPENDENT REVIEW (2 agent, CÙNG báo cáo, KHÔNG thấy nhau, KHÔNG thấy
                          lý luận gốc — chỉ nhận báo cáo cuối + rubric riêng)
        ↓
   Reviewer B                    Reviewer C
   "Domain Expert"                "Red-team Analyst"
        ↓                              ↓
VERDICT GATE: B pass VÀ C pass → NICE (trình Nobitano)
              Ngược lại → NAUGHTY → Fix cycle → chạy lại từ đầu
```

### Rubric Reviewer B — "Domain Expert" (bắt lỗi sự kiện/thuật ngữ)

```
Bạn là chuyên gia ngành [lĩnh vực báo cáo], KHÔNG biết ai viết báo cáo này
hay họ đã lý luận thế nào. Đọc báo cáo, chấm theo rubric:

1. Thuật ngữ ngành dùng đúng không? (vd nhầm TAM với SAM, nhầm đại lý cấp 1
   với cấp 2, hiểu sai khái niệm ngành)
2. Số liệu trích dẫn có khớp nguồn thật không? (không tự verify lại từng
   link, nhưng flag nếu số liệu "nghe không hợp lý" so với hiểu biết ngành)
3. Có bỏ sót yếu tố ngành quan trọng nào mà 1 chuyên gia thật sẽ hỏi ngay
   không? (vd báo cáo hàng không quên nhắc quy định IATA liên quan)
4. Đối thủ/bối cảnh cạnh tranh có mô tả đúng thực tế ngành không?

Trả về: PASS hoặc FAIL + danh sách lỗi cụ thể (không chung chung "có vẻ ổn").
```

### Rubric Reviewer C — "Red-team Analyst" (chủ động cãi lại verdict)

```
Bạn là nhà phân tích phản biện, nhiệm vụ DUY NHẤT là tìm cách chứng minh
verdict của báo cáo SAI. Không cần khách quan — hãy cố hết sức argue cho
kết luận NGƯỢC LẠI, xem lý lẽ đó mạnh tới đâu:

1. Nếu verdict là "nên làm X" — viết lý lẽ mạnh nhất cho "KHÔNG nên làm X"
2. Giả định nào trong báo cáo, nếu SAI, sẽ làm sụp cả kết luận? (khác với
   sensitivity analysis đã có — ở đây chủ động TẤN CÔNG giả định đó bằng lý
   lẽ, không chỉ show số liệu thay đổi)
3. Có kịch bản nào báo cáo hoàn toàn bỏ qua không? (vd đối thủ lớn phản ứng
   ra sao nếu ABTRIP thành công — báo cáo có tính tới đối thủ COPY lại
   không?)
4. Nếu là nhà đầu tư khó tính, câu hỏi đầu tiên khiến báo cáo bị bác là gì?

Trả về: PASS (không tìm ra lý lẽ đủ mạnh để bác verdict) hoặc FAIL + lý lẽ
phản biện mạnh nhất tìm được.
```

### Nguyên tắc bất biến (kế thừa từ santa-method)

- **Context isolation tuyệt đối** — Reviewer B và C không thấy nhau, không thấy báo cáo đã qua ceo-stress-test như thế nào, chỉ nhận bản báo cáo cuối cùng + rubric riêng của mình
- **Không tự nới lỏng tiêu chuẩn** — nếu 1 trong 2 FAIL, chạy Fix cycle (sửa báo cáo theo lỗi đã chỉ ra) → chạy lại CẢ HAI reviewer từ đầu, không chỉ sửa rồi tự cho pass
- **Giới hạn vòng lặp** — tối đa 3 vòng fix-and-recheck, quá đó → escalate cho Nobitano tự quyết thay vì lặp vô hạn tốn token

### Khác biệt với ceo-stress-test-and-roadmap (bổ sung, không thay thế)

| | ceo-stress-test-and-roadmap | research-independent-review-gate |
|---|---|---|
| Ai chạy | Cùng agent đã viết báo cáo, tự phản biện | 2 reviewer độc lập, không thấy context gốc |
| Cơ chế | Checklist tuần tự 5 câu hỏi | Dual-review song song + convergence loop |
| Bắt lỗi loại gì | Cấu trúc lập luận (hypothesis-vs-conclusion, sensitivity, cost, baseline) | Sai sót ngành + verdict có đứng vững trước phản biện chủ động không |
| Chạy khi nào | Ngay sau khi có Full Report | Sau ceo-stress-test, trước khi trình Nobitano |

## Setup từng bước
1. Báo cáo đã qua `ceo-stress-test-and-roadmap` (Phần A+B) → đây là input, không chạy skill này trên báo cáo thô
2. Spawn Reviewer B và C với PROMPT RIÊNG BIỆT — chỉ đưa báo cáo cuối cùng, không đưa lịch sử hội thoại đã dẫn tới báo cáo đó
3. Thu kết quả 2 reviewer, không cho reviewer nào thấy kết quả người kia
4. Cả 2 PASS → trình Nobitano kèm ghi chú "đã qua dual-review"
5. 1 trong 2 FAIL → sửa báo cáo theo đúng lỗi cụ thể đã chỉ ra → quay lại bước 2, tối đa 3 vòng

## Ví dụ thực tế
Áp cho báo cáo Fast Track Nội Bài đã qua ceo-stress-test (v2): Reviewer C (Red-team) có thể bắt ra điều mà chính CEO-stress-test bỏ sót — "báo cáo giả định đối thủ (VISANA, Hong Ngọc Hà...) sẽ không phản ứng gì nếu ABTRIP ra mắt bundle thành công — thực tế đối thủ có thể copy ngay trong vài tháng, làm mất lợi thế người đi đầu nhanh hơn cửa sổ 12-24 tháng đã ước tính". Đây là loại lỗi checklist tuần tự khó bắt được vì nó không nằm trong 5 câu hỏi cố định, chỉ lộ ra khi có 1 "bộ não khác" chủ động tấn công verdict.

## Lưu ý / Lỗi thường gặp
- Đừng để Reviewer B/C thấy báo cáo ĐÃ qua ceo-stress-test ra sao (tức thấy version trước/sau) — chỉ đưa bản cuối, tránh anchor theo sửa đổi đã có
- Reviewer C dễ bị nhầm là "phá đám vô cớ" — nhắc rõ nhiệm vụ CHỈ là tìm lý lẽ mạnh nhất, không phải chê bai ngẫu nhiên; nếu không tìm ra lý lẽ đủ mạnh, PASS thẳng, không ép phải tìm lỗi cho có
- Vòng lặp fix-and-recheck tốn token thật — giới hạn 3 vòng là bắt buộc, không phải gợi ý, tránh lặp vô hạn vì 2 reviewer không bao giờ đồng thuận 100%
- Không dùng skill này cho báo cáo nhỏ/không dẫn tới quyết định đầu tư lớn — santa-method chính chủ đã ghi rõ "không dùng cho draft nội bộ/research thăm dò"

## Đánh giá cá nhân
- Điểm mạnh: tận dụng đúng cơ chế đã kiểm chứng có sẵn trong kho (santa-method) thay vì phát minh lại; context isolation thật sự giải quyết được điểm mù mà checklist tự chạy không giải quyết nổi (cùng não viết + cùng não tự sửa vẫn mang chung bias)
- Điểm yếu: tốn thêm thời gian/token đáng kể (2 reviewer + có thể nhiều vòng lặp) — chỉ nên dùng cho quyết định thật sự lớn, không phải mọi báo cáo
- Có nên dùng: 8/10 — bắt buộc cho báo cáo dẫn tới quyết định đầu tư/rót nguồn lực lớn (như case ABTRIP bundle), không cần cho báo cáo nội bộ tham khảo nhanh

## Link
- Cơ chế gốc: `skills/santa-method/SKILL.md` — đọc để hiểu đầy đủ Phase 1-4 (Generate → Dual Review → Verdict Gate → Fix Cycle)
- Chạy trước: `agents/research-analytics-pro/skills/ceo-stress-test-and-roadmap/SKILL.md`
