# hermes-jev-skills — GitHub Repo

## TL;DR
Bridge làm sẵn giữa Hermes/Claude Code/Codex với Jev (TypeSafe) — đúng việc đã tự thiết kế trong `production-signal-feedback-loop` (Antigravity Bridge tự viết), nhưng có sẵn: installer tự dò agent trên máy, 5 tool dùng ngay, lưu API key an toàn hơn thiết kế tự nghĩ.

## Repo này dùng để làm gì
Cài vào Hermes/Claude Code/Codex có sẵn trên máy, thêm 5 khả năng dùng Jev làm quyết định nhanh: `jev_memory_filter` (lọc bớt context), `jev_compact_select` (chọn gì giữ khi nén hội thoại — ⚠️ tác giả tự đo thấy KÉM HƠN không dùng gì), `jev_choose_action` (chọn hành động), `jev_supervise` (giám sát), `jev_escalate` (đẩy lên khi không chắc — đúng khái niệm confidence <50% đã thiết kế).

## Điểm hay nhất — Shadow Mode, an toàn hơn cách đã tự nghĩ
```
/jev routing shadow   → Jev tự quyết NGẦM, chỉ ghi log, KHÔNG thật sự
                         đổi hành vi — xem log 1 thời gian trước khi tin
/jev routing on        → mới thật sự để Jev quyết định thay
```
Khác thiết kế cũ (tự đặt ngưỡng confidence 80%/50% mà chưa có data thật để biết ngưỡng đó đúng hay không) — shadow mode để CHÍNH Jev tự chứng minh qua log trước khi trao quyền.

## Bảo mật API key — tốt hơn hẳn cách tự làm
```
jev setup-key → mở URL local dùng 1 LẦN DUY NHẤT (chặn DNS rebinding,
không log, tự tắt sau 10 phút) → lưu thẳng vào OS Keychain/secret-tool
→ Hermes KHÔNG BAO GIỜ thấy key thật, kể cả 1 phần
```

## Setup từng bước
1. `pip install hermes-jev` (hoặc theo README repo cụ thể — có nhiều fork giống hệt, xem phần Lưu ý)
2. `python3 install.py --check` — xem trước sẽ làm gì, KHÔNG đổi gì
3. `jev setup-key` — dán TypeSafe key vào URL local 1 lần
4. `/jev routing shadow` — BẮT ĐẦU Ở ĐÂY, không bật `on` ngay
5. Theo dõi `/jev status` + dashboard 1 thời gian, đủ tin mới `/jev routing on`

## Lưu ý / Lỗi thường gặp
- **Nhiều fork trùng mô tả y hệt** (maxkilla, Cossackx, dajiaohuang, kerpopule, ucalyptus, Long0308...) — dùng bản nào có hoạt động gần nhất/nhiều sao nhất, chưa xác định rõ bản "gốc" trong nhóm này
- `jev_compact_select` (nén bộ nhớ) — tác giả TỰ ĐO thấy kết quả nhớ TỆ HƠN giữ nguyên transcript thô — đừng bật tính năng này ngay, để mặc định tắt
- Chỉ đổi được MODEL, không đổi được provider connection — không thay thế được việc cấu hình provider (Anthropic/OpenRouter) đã làm riêng

## Đánh giá cá nhân
- Điểm mạnh: giải đúng bài toán đã tự thiết kế (Jev Bridge cho Hermes) nhưng nhanh hơn, an toàn hơn (shadow mode, key không lộ); tác giả trung thực về tính năng không hiệu quả (đáng tin hơn marketing suông)
- Điểm yếu: hệ sinh thái mới (không rõ tuổi đời/độ ổn định), nhiều fork gây khó chọn bản đúng
- Có nên dùng: 8/10 — đáng thay thế thiết kế tự viết trong `production-signal-feedback-loop`, BẮT ĐẦU BẰNG shadow mode

## Link
- Ví dụ repo: https://github.com/maxkilla/hermes-jev-skills (1 trong nhiều fork giống nhau)
- Nguồn tổng hợp: awesome-jev (onmyway133/AbdelStark/AnotiaWang/fatwang2)

---

## 🤖 Agent Integration

### Hermes
Cài trực tiếp — đây CHÍNH LÀ tool dành cho Hermes, không cần code riêng.

### Antigravity
```bash
# Nếu cần cài cho Hermes chạy trên VPS
pip install hermes-jev  # hoặc theo đúng tên package của fork đã chọn
```
