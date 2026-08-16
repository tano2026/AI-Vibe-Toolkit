# Prism Scanner — Skill/Tool

## TL;DR
Scanner bảo mật mã nguồn mở cho skill/plugin/MCP server của AI agent — 39+ rule detection, AST taint tracking, chấm điểm A-F. Cài qua `pip install prism-scanner`, Apache-2.0, 13 sao.

## Tool này dùng để làm gì
Vấn đề: kho AI Vibe Toolkit liên tục thêm skill/MCP mới từ nguồn ngoài (như đợt vừa lọc từ `rohitg00/awesome-claude-code-toolkit`) — mỗi skill là code/instruction từ tác giả lạ, review bằng mắt tốn thời gian và dễ bỏ sót. Prism Scanner tự động hóa việc này: quét file skill/plugin/MCP config, dùng AST taint tracking (theo dõi luồng dữ liệu từ input tới chỗ nguy hiểm như exec/eval/network call) để phát hiện pattern độc hại, rồi chấm điểm A-F cho tổng thể.

Đúng nguyên tắc `security-wall`/`canary-watch` đã ghi trong kho là "mandatory inline skill cho deploy workflow" — Prism Scanner có thể là công cụ thực thi cụ thể cho nguyên tắc đó thay vì chỉ là quy định suông.

## Setup từng bước
1. Cài qua pip:
```bash
pip install prism-scanner
```
2. Chạy quét 1 skill/plugin cụ thể trước khi thêm vào kho:
```bash
prism-scanner scan <đường-dẫn-skill-hoặc-repo>
```
3. Đọc report điểm A-F + danh sách rule vi phạm (nếu có) trước khi quyết định push vào kho GitHub.

## Ví dụ thực tế
Trước khi thêm 1 skill mới tìm được (như Overnight Worker vừa research — autonomous agent chạy qua đêm, rủi ro cao hơn skill thường vì không giám sát) → chạy `prism-scanner scan` trước, xem có rule nào bị flag (network call lạ, exec động, đọc file ngoài phạm vi...) rồi mới quyết định đưa vào `security-wall` review tiếp hay bỏ qua luôn.

## Lưu ý / Lỗi thường gặp
- Repo nhỏ, 39 rule không thể bắt hết mọi kiểu tấn công — coi đây là lớp lọc đầu (fast filter), không thay thế hoàn toàn việc đọc code kỹ với skill sắp chạy production/autonomous.
- Cần Python environment sạch để cài — dùng `pip install prism-scanner --break-system-packages` nếu chạy trên môi trường có restriction giống container hiện tại.
- Chấm điểm A-F mang tính tương đối, không phải chuẩn tuyệt đối — 1 skill điểm B vẫn nên tự đọc phần bị trừ điểm trước khi tin dùng.

## Đánh giá cá nhân
- Điểm mạnh: đúng khoảng trống đang thiếu trong quy trình kho — hiện `security-wall` là nguyên tắc, chưa có tool thực thi cụ thể; Prism Scanner lấp vào đó, đặc biệt hữu ích khi tốc độ thêm skill mới vào kho khá nhanh (474 skill và tăng).
- Điểm yếu: còn non trẻ (13 sao), cần tự verify thêm không nên tin 100% score.
- Có nên dùng không: 7.5/10 — nên tích hợp vào Bước 2 "Research" của quy trình kho intake, chạy scan trước khi viết .md cho bất kỳ skill/MCP nào có code thực thi (không cần cho loại chỉ là markdown chỉ dẫn thuần).

## Link
- Repo: https://github.com/aidongise-cell/prism-scanner
- PyPI: `pip install prism-scanner`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess
def scan_skill(path):
    result = subprocess.run(["prism-scanner", "scan", path], capture_output=True, text=True)
    return result.stdout
# Gắn vào Bước 2 (Research) của quy trình kho intake — scan trước khi viết .md
```

### OpenClaw
```bash
pip install prism-scanner --break-system-packages
```

### Antigravity
```bash
pip install prism-scanner --break-system-packages
# Chạy định kỳ quét lại toàn bộ skill/plugin đang cài trên VPS
```
> ⚠️ Nên thêm bước `prism-scanner scan` vào quy trình kho intake (Bước 2 — Research) cho mọi skill/MCP có code thực thi thật, trước khi Claude viết file .md và push.
