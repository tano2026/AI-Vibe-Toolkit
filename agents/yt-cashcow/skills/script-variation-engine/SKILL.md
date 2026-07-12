---
name: script-variation-engine
description: >
  Dùng để viết script từ topic brief (do Trend Scout đưa ra), TRƯỚC khi qua
  Compliance Gate. Khác Script Writer thường ở chỗ: bắt buộc tự kiểm tra
  variation so với lịch sử trước khi giao script, không chỉ viết theo template cố định.
---

# Script Variation Engine

## TL;DR
Viết script có "editorial fingerprint" riêng — không phải đổi từ khóa vào cùng
1 khung. Đọc `fingerprint_history` (Airtable) TRƯỚC khi viết, chủ động né
structure_type/hook_type đã dùng nhiều, không đợi Compliance Gate bounce lại.

## Khi nào dùng
Ngay sau Trend Scout, trước Compliance Gate.

## Quy trình

1. **Đọc lịch sử trước khi viết** — pull 15 record gần nhất từ `fingerprint_history`.
   Xem structure_type/hook_type nào đã dùng nhiều → chủ động chọn loại khác.
2. **Chọn hook** — dùng viral-hooks skill (có sẵn kho, 100 formula/10 trigger),
   ưu tiên trigger chưa dùng gần đây.
3. **Chọn structure** — 1 trong 5: `intro-list-outro | narrative | comparison |
   tutorial | case-study`. Không lặp lại structure đã dùng >50% trong 15 video gần nhất.
4. **Viết script với tỷ lệ commentary tối thiểu 15%** — nghĩa là ít nhất 15% câu
   trong script phải là góc nhìn/phân tích/kết nối riêng, không phải liệt kê
   fact thô đọc từ nguồn. Đây là điều kiện để pass Compliance Gate
   (`commentary_ratio < 0.15` → FAIL).
5. **Gắn ít nhất 1 unique claim gốc** — 1 data point, ví dụ, hoặc góc so sánh
   chưa xuất hiện trong 5 video gần nhất (check qua `unique_claims` list).
6. **Xuất fingerprint kèm script** — trả về object có đủ 4 field
   (`structure_type`, `hook_type`, `unique_claims`, `commentary_ratio`) để
   Compliance Gate chấm ngay, không phải tự trích lại.

## Ví dụ thực tế

**Brief từ Trend Scout:** "AI tools that are overhyped vs actually worth the price"

**Lịch sử 15 video gần nhất:** 9 video dạng `intro-list-outro`, 3 dạng `narrative`,
3 dạng `comparison`. Hook: 7 lần `shock-stat`, còn lại rải rác.

**Quyết định của engine:** chọn structure `case-study` (chưa dùng lần nào gần đây)
— kể chuyện theo dõi chi phí thật của 1 người dùng 3 tool AI trong 1 tháng, so
với con số marketing quảng cáo. Hook chọn `story-open` thay vì `shock-stat`.

**Commentary:** thêm đoạn phân tích riêng "vì sao pricing page thường ẩn phí ẩn"
— đây là góc nhìn, không phải liệt kê giá.

**Output:** script + fingerprint `{structure_type: case-study, hook_type: story-open,
unique_claims: [...], commentary_ratio: 0.22}` → gửi thẳng Compliance Gate,
xác suất pass cao vì đã tự né trùng lặp từ đầu.

## Lưu ý / Lỗi thường gặp
- Đừng để LLM tự "nghĩ mình đã đủ variation" — luôn tính commentary_ratio bằng
  cách đếm câu thật (LLM chấm qua prompt riêng, không tự khai báo trong lúc viết).
- Nếu topic quá hẹp, khó tạo unique claim mới → báo lại Trend Scout đổi topic,
  đừng cố viết script yếu rồi để Compliance Gate chặn (tốn 1 vòng lặp vô ích).

## Đánh giá cá nhân
- Điểm mạnh: chủ động né lỗi thay vì đợi bị chặn — giảm số lần bounce qua lại
  giữa Engine và Gate.
- Điểm yếu: phụ thuộc LLM chấm commentary_ratio chính xác — cần audit định kỳ
  bằng cách đọc thủ công vài script xem chấm điểm có hợp lý không.
- Có nên dùng: 9/10.

## Agent Integration

### Hermes (Python, urllib thuần)
```python
def write_script_with_fingerprint(brief, history, omniroute_url, omniroute_key):
    used_structures = [h['structure_type'] for h in history]
    used_hooks = [h['hook_type'] for h in history]
    prompt = f"""Viết script YouTube từ brief: {brief}
Lịch sử structure đã dùng nhiều: {used_structures} — TRÁNH lặp lại loại chiếm >50%.
Lịch sử hook đã dùng nhiều: {used_hooks} — TRÁNH lặp lại loại chiếm >40%.
Bắt buộc: ít nhất 15% câu là commentary/góc nhìn riêng, không liệt kê fact thô.
Trả về JSON: {{script, structure_type, hook_type, unique_claims, commentary_ratio}}"""
    payload = {"model": "claude-sonnet-5", "messages": [{"role": "user", "content": prompt}]}
    import json, urllib.request
    req = urllib.request.Request(omniroute_url, data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {omniroute_key}", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())
```

### OpenClaw
```bash
# Nhận brief từ Trend Scout → gọi Hermes write_script_with_fingerprint()
# → forward output sang Compliance Gate
```
