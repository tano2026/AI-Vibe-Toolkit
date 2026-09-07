# Project Starter Rules — Skill / System Prompt

## TL;DR
Bộ 5 trụ cột quy tắc chuẩn tự động đóng gói vào MỌI dự án mới của Tano Agency (Hermes, OpenClaw, VPS bots, web apps) — chặn code rác, giữ chi phí token thấp, chặn vòng lặp vô tận, bảo mật secret, và cấm báo cáo "xong" khi chưa test thật.

## Khi nào dùng
Ngay khi khởi tạo bất kỳ project/repo mới nào (Hermes agent mới, OpenClaw sub-project, VPS bot mới, web app mới). Trigger câu lệnh: "Áp dụng quy tắc dự án mới", "hermes skill project-starter-rules", hoặc đơn giản là copy file `AGENTS.md` vào thư mục gốc project mới.

## Nội dung skill / prompt
```
# AGENTS.md — Standard Project Starter Ruleset (Tano Agency)

## 1. Chất Lượng Code & Kiến Trúc
- Không nuốt ngoại lệ (except: pass), không comment out test hỏng, không trả dữ liệu giả 0-byte
- Trace lỗi tận gốc: đọc log đầy đủ trước khi chẩn đoán
- Sửa hàm/interface → cập nhật 100% nơi gọi tương ứng (giữ nguyên API contract)
- Giữ nguyên comment/docstring hiện có

## 2. Tối Ưu Chi Phí & Token
- model.default: openrouter/free hoặc deepseek/deepseek-chat — không cài model Pro làm mặc định
- Context compression: threshold 0.85
- Idle reset: 180 phút không nhắn tin → reset phiên
- Turn cap: tối đa 20 lượt gọi/yêu cầu

## 3. Chống Vòng Lặp Vô Tận
- Cảnh báo nếu 1 tool lỗi 3 lần liên tiếp
- Hard stop nếu 1 tool lỗi 8 lần liên tiếp

## 4. Bảo Mật & Kết Nối
- Redact API key/password trong log & chat tự động
- Local bridge qua Tailscale IP (100.90.212.62:8083) cho scrape web + thao tác file ổ D:\

## 5. Kiểm Thử Thực Tế
- Không tuyên bố "xong" khi chưa chạy build/test thật
- Bắt buộc có log/output terminal làm bằng chứng
```

## Setup từng bước
1. **Cách 1 (tự động):** Skill đã nạp vào Local PC + VPS Cloud của Hermes. Gõ trong chat: `"Áp dụng quy tắc dự án mới"` hoặc `"hermes skill project-starter-rules"` → Hermes tự tuân thủ.
2. **Cách 2 (thủ công):** Copy nguyên khối `AGENTS.md` ở trên vào thư mục gốc của project mới. Bot đọc và tuân thủ 100% ngay từ lần chạy đầu.
3. Với Claude (kho): trước khi sinh code cho bất kỳ agent/project nào trong `agents/`, đối chiếu output với 5 trụ cột này trước khi push.

## Ví dụ thực tế
Trước khi có rule: 1 sub-agent mới của OpenClaw viết `except: pass` để nuốt lỗi gọi API, treo vòng lặp retry vô hạn khi endpoint down 8 lần liên tiếp, đốt token vì không có turn cap → hoá đơn API tăng đột biến.

Sau khi có rule: agent hard-stop ở lần lỗi thứ 8, cảnh báo Nobitano ở lần lỗi thứ 3, turn cap 20 chặn vòng lặp leo thang, model mặc định free/deepseek giữ chi phí thấp.

## Lưu ý / Lỗi thường gặp
- Quên set `idle_minutes: 180` → phiên treo vô thời hạn, tốn context không cần thiết
- Local bridge Tailscale IP là IP nội bộ — đổi máy/VPN khác sẽ mất kết nối, cần cập nhật lại IP trong AGENTS.md
- "Verification First" chỉ có giá trị nếu agent thực sự chạy lệnh test — nếu agent tự bịa log thì rule này vô nghĩa, cần double-check thủ công định kỳ

## Đánh giá cá nhân
- Điểm mạnh: 5 trụ cột cover đủ 3 lớp rủi ro thực tế (code rác, đốt tiền, bảo mật) mà một solo agency dễ dính phải khi scale nhiều agent cùng lúc
- Điểm yếu: rule 4 (Local Bridge Tailscale IP) hardcode cứng — không portable nếu đổi hạ tầng; rule 5 (Verification First) dựa vào agent tự giác báo cáo trung thực, không có cơ chế enforce độc lập
- Có nên dùng không: 8/10 — nên dùng cho mọi project mới, nhưng cần audit định kỳ xem agent có thực sự tuân thủ rule 5 hay không

## Link
- Nguồn gốc skill: Nobitano tự soạn, đóng gói lại từ kinh nghiệm vận hành Hermes/OpenClaw/VPS thực tế

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes tự nhận diện trigger "project-starter-rules" đã nạp sẵn ở Local PC + VPS
# Không cần gọi API rời — chỉ cần đảm bảo AGENTS.md có mặt ở project root
import os

def ensure_starter_rules(project_dir: str, agents_md_content: str):
    path = os.path.join(project_dir, "AGENTS.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(agents_md_content)
    return path
```

### OpenClaw
```bash
# Khi OpenClaw khởi tạo sub-project mới, tự copy AGENTS.md chuẩn vào root
cp /path/to/kho/skills/project-starter-rules/AGENTS-template.md ./AGENTS.md
```

### Antigravity
```bash
# Khi bootstrap VPS project mới, seed AGENTS.md ngay bước đầu deploy
scp AGENTS-template.md user@vps:/opt/projects/<ten-du-an>/AGENTS.md
```
> ⚠️ Rule 4 (Local Bridge) chỉ áp dụng khi agent chạy trên máy có Tailscale nối tới `100.90.212.62:8083` — VPS thuần không có bridge này thì bỏ qua, đừng hardcode.
