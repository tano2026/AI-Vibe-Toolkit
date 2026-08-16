# Overnight Worker — Skill

## TL;DR
Skill "giao việc trước khi ngủ, sáng có kết quả" — autonomous agent làm việc qua đêm, tự phân rã task, tự research web, xong gửi push notification kết quả có cấu trúc. Đúng tên gọi luôn: OpenClaw Skill.

## Skill này dùng để làm gì
Skill này được gắn nhãn "OpenClaw Skill" ngay trong mô tả gốc — tức là thiết kế để chạy trên các agent gateway kiểu OpenClaw (giống hệ thống Nobitano đang có), không chỉ Claude Code thường. Cơ chế: giao 1 task mơ hồ ("chuẩn bị content Trùm Sân Bay tuần sau") trước khi đi ngủ, agent tự phân rã thành việc con, tự research nếu cần, chạy suốt đêm, sáng dậy có kết quả có cấu trúc sẵn (không phải log lộn xộn) + notification báo xong.

## Setup từng bước
1. Clone repo về:
```bash
git clone https://github.com/fullstackcrew-alpha/skill-overnight-worker
```
2. Đọc README của tác giả để cấu hình kênh push notification (Telegram/email/webhook — tùy bản, cần map với Telegram Bot API sẵn có trong kho).
3. Test với 1 task nhỏ, rõ ràng trước, tăng dần độ mơ hồ khi đã tin tưởng agent tự phân rã đúng hướng.

## Ví dụ thực tế
Input tối trước khi ngủ: "Research xu hướng Fast Track dịch vụ sân bay Đông Nam Á 2026, tổng hợp thành brief cho content tuần sau."
→ Overnight Worker tự chia nhỏ: research web, lọc nguồn, viết brief, sáng hôm sau Nobitano nhận Telegram báo "xong, xem file brief tại [path]" thay vì phải tự trigger từng bước.
Khớp thẳng với HEARTBEAT.md của CEO Agent trong Mission Control — có thể ghép logic overnight task queue này vào để CEO Agent tự chạy việc dài hơi ngoài giờ làm việc.

## Lưu ý / Lỗi thường gặp
- Repo nhỏ (4 sao) — cần tự audit code trước khi cho chạy overnight không giám sát trên VPS (đúng nguyên tắc `security-wall`/`kiem-tra-bao-mat-truoc-deploy` đã có trong kho, đặc biệt vì đây là agent chạy autonomous qua đêm, rủi ro cao hơn agent tương tác trực tiếp).
- "Autonomous overnight" dễ tốn token nếu task phân rã sai hướng và tự loop nhiều bước không cần thiết — nên giới hạn budget/thời gian chạy tối đa.
- Cần setup kênh notification đúng — nếu không cấu hình xong sẽ không biết agent đã hoàn thành hay đang bị stuck.

## Đánh giá cá nhân
- Điểm mạnh: đúng use case Nobitano cần — giao việc dài hơi, không cần canh giờ, hợp mô hình agency 1 người làm ban ngày, agent làm đêm.
- Điểm yếu: repo còn quá mới/nhỏ để tin tưởng chạy autonomous không giám sát ngay từ đầu, thiếu track record.
- Có nên dùng không: 6.5/10 — đáng thử nghiệm giới hạn (task nhỏ, có giám sát) trước khi giao việc quan trọng qua đêm.

## Link
- Repo: https://github.com/fullstackcrew-alpha/skill-overnight-worker

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Overnight Worker thiết kế cho OpenClaw gateway — Hermes có thể trigger task
# rồi poll kết quả theo lịch (vd 6h sáng check file kết quả).
import time, os
def check_overnight_result(result_path, max_wait_hours=10):
    waited = 0
    while not os.path.exists(result_path) and waited < max_wait_hours * 3600:
        time.sleep(600)
        waited += 600
    return os.path.exists(result_path)
```

### OpenClaw
```bash
git clone https://github.com/fullstackcrew-alpha/skill-overnight-worker ~/.openclaw/skills/overnight-worker
# Cấu hình notification qua Telegram Bot API đã có sẵn trong hệ thống
```

### Antigravity
```bash
# Deploy trên VPS để chạy 24/7 cùng OpenClaw
git clone https://github.com/fullstackcrew-alpha/skill-overnight-worker /opt/openclaw/skills/overnight-worker
```
> ⚠️ Test kỹ với task nhỏ, giám sát trước — audit bảo mật trước khi cho chạy autonomous không giám sát trên VPS production.
