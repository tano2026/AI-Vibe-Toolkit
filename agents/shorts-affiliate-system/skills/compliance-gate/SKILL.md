---
name: compliance-gate
description: >
  Dùng skill này NGAY SAU khi Script Variation Engine viết xong script, TRƯỚC khi
  đưa vào MoneyPrinterTurbo render. Bắt buộc cho mọi video trong pipeline yt-cashcow,
  không optional. Chặn video có nguy cơ bị YouTube gắn "Inauthentic Content" —
  policy áp dụng ở cấp CẢ KÊNH, không phải từng video, nên 1 video lọt lưới vẫn
  có thể kéo cả kênh mất monetize.
---

# Compliance Gate — Chặn Inauthentic Content trước khi render

## TL;DR
Node bắt buộc trong pipeline, đứng giữa Script Variation Engine và MoneyPrinterTurbo.
So structural fingerprint script mới với 15 video gần nhất trong Airtable
`fingerprint_history`. Fail → bounce lại yêu cầu sửa. Pass → cho render.

## Căn cứ chính sách (research thật, không suy đoán)

YouTube đổi tên policy "Repetitious Content" → "Inauthentic Content" (7/2025), mở rộng
phạm vi. Tháng 1/2026 xóa 16 kênh / 35 triệu subscriber / 4.7 tỷ view trong 1 đợt.
Policy áp dụng cấp **toàn kênh** — nếu đủ video vi phạm, mất monetize cả kênh chứ
không phải chỉ video đó.

3 nhóm bị cấm cụ thể (theo YouTube Help chính thức):
1. Đọc lại nguyên văn nguồn khác (text từ website/newsfeed) không thêm gì
2. Template lặp lại y hệt cấu trúc qua nhiều video, chỉ đổi chủ đề
3. Slideshow ảnh + giọng đọc AI, không có narrative/commentary/giá trị giáo dục

Được phép: cùng intro/outro, nhưng **nội dung phần thân phải khác biệt rõ** — có
commentary, góc nhìn, hoặc structure khác nhau giữa các video.

## Thuật toán chấm điểm (áp code, không chỉ dặn prompt)

### Bước 1 — Trích fingerprint từ script mới
Từ script text, trích ra 4 trường:
```
structure_type   : intro-list-outro | narrative | comparison | tutorial | case-study
hook_type        : question | shock-stat | story-open | controversy | how-to
unique_claims    : list các fact/số liệu/ví dụ cụ thể xuất hiện trong script
commentary_ratio : % câu trong script là góc nhìn/phân tích riêng (không phải liệt kê fact thô)
```

### Bước 2 — So với 15 video gần nhất (Airtable `fingerprint_history`)
```python
def check_compliance(new_fp, history):
    same_structure = sum(1 for h in history if h['structure_type'] == new_fp['structure_type'])
    same_hook = sum(1 for h in history if h['hook_type'] == new_fp['hook_type'])
    claim_overlap = jaccard_similarity(new_fp['unique_claims'],
                                        flatten([h['unique_claims'] for h in history[-5:]]))

    # Ngưỡng chặn — điều chỉnh được, mặc định bảo thủ
    if same_structure >= 8:  # quá 8/15 video cùng structure_type
        return "FAIL", "structure_type lặp lại quá nhiều, đổi format"
    if same_hook >= 6:
        return "FAIL", "hook_type lặp lại, dùng viral-hooks skill chọn trigger khác"
    if claim_overlap > 0.4:
        return "FAIL", "nội dung trùng lặp với video gần đây, thêm góc nhìn/data mới"
    if new_fp['commentary_ratio'] < 0.15:
        return "FAIL", "quá ít commentary/góc nhìn riêng — giống đọc lại nguồn thô"

    return "PASS", None
```

Không cần vector DB/embedding phức tạp — Jaccard similarity trên list claims đủ
dùng ở quy mô vài chục video/tháng, chạy nhẹ trên VPS hiện tại, không cần thêm hạ tầng.

### Bước 3 — Nếu FAIL
Bounce lại Script Variation Engine kèm lý do cụ thể (không phải "làm lại từ đầu" —
chỉ định rõ phần nào cần đổi: structure, hook, hay thêm commentary).

### Bước 4 — Nếu PASS
- Ghi fingerprint mới vào `fingerprint_history` (giữ rolling 15 record gần nhất).
- Random 1/10 video → set `compliance_status = human-review`, dừng auto-publish,
  gửi Telegram cho Nobitano duyệt trước khi MoneyPrinterTurbo render.
- 9/10 còn lại → cho render bình thường.

## Ví dụ thực tế

**Input:** Script mới về "Top 5 AI tool 2026", structure_type = `intro-list-outro`,
hook_type = `shock-stat`.

**History gần nhất:** 9/15 video trước cũng là `intro-list-outro`, 7/15 cũng `shock-stat`.

**Kết quả:** FAIL cả 2 điều kiện. Compliance Gate trả về: "structure_type lặp lại
quá nhiều, đổi format" + "hook_type lặp lại, dùng viral-hooks skill chọn trigger khác".

**Sửa:** Script Variation Engine đổi sang structure `case-study` (kể chuyện 1 người
dùng thử tool thay vì liệt kê), hook đổi sang `story-open`. Chạy lại Gate → PASS.

## Lưu ý / Lỗi thường gặp

- Đừng set ngưỡng quá lỏng để "cho qua nhanh" — mục đích của Gate là chặn thật,
  không phải formality. Ngưỡng trong code trên đã bảo thủ có chủ đích.
- Nếu kênh mới <15 video, dùng toàn bộ số video hiện có làm history, không chặn
  vì thiếu data.
- commentary_ratio cần LLM chấm (không phải rule-based đếm từ) — dùng OmniRoute
  reasoning tier (DeepSeek R1) để chấm, rẻ và đủ chính xác cho việc này.

## Đánh giá cá nhân
- Điểm mạnh: chặn sớm (trước render tốn compute), có căn cứ chính sách thật, không
  cần hạ tầng nặng (không vector DB).
- Điểm yếu: Jaccard similarity là proxy thô cho "similarity nội dung thật" — không
  bắt được trường hợp diễn đạt khác nhưng ý y hệt (paraphrase). Cần review định kỳ
  ngưỡng dựa trên video nào thực sự bị flag bởi YouTube (nếu có) để tinh chỉnh.
- Có nên dùng: 10/10 — không phải optional, đây là điều kiện sống còn của kênh theo
  đúng case thật đã xảy ra 1/2026.

## Agent Integration

### Hermes (Python, urllib thuần)
```python
import urllib.request, json

def get_fingerprint_history(airtable_base, airtable_token, n=15):
    url = f"https://api.airtable.com/v0/{airtable_base}/fingerprint_history?maxRecords={n}&sort[0][field]=timestamp&sort[0][direction]=desc"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {airtable_token}"})
    data = json.loads(urllib.request.urlopen(req).read())
    return [r['fields'] for r in data['records']]

def jaccard_similarity(list_a, list_b):
    set_a, set_b = set(list_a), set(list_b)
    if not set_a or not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)

# check_compliance() — xem thuật toán Bước 2 ở trên, copy thẳng vào
```

### OpenClaw
```bash
# Gọi compliance-gate như 1 bước bắt buộc trong Domain Agent Router
# trước khi forward sang MoneyPrinterTurbo render step
```

### Antigravity
Không cần — skill này chạy hoàn toàn trong Hermes/OpenClaw, không đụng shell/VPS.

> ⚠️ Không tắt Compliance Gate để "publish nhanh hơn" — đây chính là guardrail
> theo đúng "Rủi ro cao nhất" đã xác định ở Bước 1 của Agentic Factory.
