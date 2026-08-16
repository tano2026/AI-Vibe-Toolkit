# TokenWise — Skill

## TL;DR
Router tự động chọn Haiku/Sonnet/Opus theo độ khó task trong Claude Code, log ra số $ tiết kiệm được thật (không phải ước lượng mơ hồ) vào file NDJSON local. Miễn phí, MIT, không gửi data đi đâu.

## Skill này dùng để làm gì
Vấn đề TokenWise giải quyết: đa số người cứ để mặc định 1 model cho mọi task — việc đơn giản (đổi tên biến, format code) vẫn dùng Opus đắt tiền như việc phức tạp. TokenWise phân loại task theo độ khó, tự route xuống Haiku/Sonnet khi việc đơn giản, chỉ giữ Opus cho việc thật sự cần suy luận sâu, đồng thời A/B test model rẻ hơn trước khi "tin tưởng" hoàn toàn (không đổi ngay, thử dần rồi mới route mặc định).

Điểm khác biệt với skill cùng dạng: có log NDJSON ghi lại mỗi lần route — task nào, model nào, tiết kiệm bao nhiêu $ — xem lại được lịch sử thay vì chỉ tin số liệu marketing.

## Setup từng bước
1. Cài qua plugin marketplace:
```
/plugin marketplace add CodeShuX/tokenwise
```
2. Không cần config API key riêng — hoạt động ngay trong Claude Code, đọc theo session hiện tại.
3. Chạy vài task đầu để TokenWise thu thập baseline, sau đó xem log NDJSON để đánh giá độ chính xác route trước khi tin tưởng hoàn toàn.

## Ví dụ thực tế
Input: chạy 20 task trong 1 buổi sửa code cho landing page ABTRIP — có việc đổi màu CSS (đơn giản) xen với việc viết lại logic booking form (phức tạp).
→ TokenWise tự route việc đổi CSS xuống Haiku, giữ Opus cho phần logic form, cuối phiên xuất log cho biết đã tiết kiệm bao nhiêu $ so với chạy toàn bộ bằng Opus.
Với OmniRoute gateway đang có (route thủ công theo tag cheap/reasoning/balanced/creative), TokenWise cho thấy cách route tự động theo độ khó thay vì gán tag cứng theo loại việc — có thể tham khảo logic phân loại này để nâng cấp OmniRoute.

## Lưu ý / Lỗi thường gặp
- Repo còn nhỏ (3 sao, mới) — chưa có track record dài hạn, kiểm tra kỹ log trước khi tin route quyết định cho việc quan trọng.
- Chỉ hoạt động trong Claude Code, không phải universal router cho mọi agent — muốn dùng logic tương tự cho OmniRoute (đang serve cả DeepSeek, Gemini) phải tự viết lại phần route rule.
- MIT + "zero telemetry" theo mô tả tác giả — nhưng vẫn nên tự kiểm tra code trước khi chạy trên môi trường có dữ liệu nhạy cảm (đúng nguyên tắc security-wall đã có trong kho).

## Đánh giá cá nhân
- Điểm mạnh: đo lường thật bằng số ($ tiết kiệm) chứ không chỉ nói suông, đúng vấn đề cost-optimization đang cần cho hệ thống nhiều agent chạy 24/7.
- Điểm yếu: repo mới, ít người dùng kiểm chứng, chỉ giới hạn trong Claude Code.
- Có nên dùng không: 7/10 — đáng thử nghiệm 1-2 tuần trước khi quyết định có tích hợp ý tưởng vào OmniRoute hay không.

## Link
- Repo: https://github.com/CodeShuX/tokenwise
- Cài qua repo tổng: repos/awesome-claude-code-toolkit.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# TokenWise chạy trong Claude Code, không có REST API riêng để Hermes gọi trực tiếp.
# Hermes có thể đọc log NDJSON do TokenWise xuất ra để tổng hợp báo cáo chi phí định kỳ.
import json
def parse_tokenwise_log(path):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    total_saved = sum(r.get("saved_usd", 0) for r in rows)
    return total_saved, rows
```

### OpenClaw
```bash
# Không áp dụng trực tiếp — TokenWise là plugin Claude Code, OpenClaw dùng OmniRoute riêng.
# Có thể tham khảo logic route theo độ khó task để nâng cấp OmniRoute.
```

### Antigravity
```bash
/plugin marketplace add CodeShuX/tokenwise
```
> ⚠️ Chỉ cài thử trên máy dev cá nhân trước, chưa nên gắn vào VPS production khi repo còn mới.
