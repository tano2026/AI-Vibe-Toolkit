# Hermes Agent — MEMORY.md Template

**Copy vào:** `~/.hermes/MEMORY.md`
**Mục đích:** Long-term context — Hermes đọc file này mỗi phiên

---

```markdown
# Long-term Memory

## Kho AI Vibe Toolkit

### Stats hiện tại (cập nhật tự động)
- Repos: 41 | MCPs: 30 | Skills: 126 | Scripts: 51 | Stacks: 3

### Repos đã có (KHÔNG thêm lại):
Xem TRACKER.md trong kho

### Script số tiếp theo:
Fetch content/ folder → đếm files → +1

### Format file .md chuẩn:
- Header: tên, stars, license, tác giả, ngày tạo
- Mô tả ngắn (vấn đề giải quyết)
- Cài đặt (commands cụ thể)
- Use cases thực tế (3-5 cái)
- Đánh giá cá nhân + Rating X/10

## Content Channel

### Videos đã có script (KHÔNG viết lại):
Xem /content/ folder trong kho

### Hook templates hay nhất:
- "[X]k stars — [feature độc đáo nhất]"
- "Tool này làm [Y] mà [tool cũ] không làm được"
- "Tao dùng [X] tháng, đây là kết quả"

## Skills Đã Tích Lũy

### Research workflow:
Khi nhận URL/tên repo:
1. requests.get GitHub API /repos/{owner}/{repo}
2. requests.get README.md raw
3. Extract: stars, license, install command, key features
4. Viết .md + script → push → update TRACKER

### Push GitHub workflow:
```python
# Pattern chuẩn để push file lên kho
import requests, base64
headers = {"Authorization": f"token {TOKEN}"}
url = f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/{path}"
r = requests.get(url, headers=headers)
sha = r.json().get('sha')  # None nếu file chưa tồn tại
payload = {
    "message": f"Add {path}",
    "content": base64.b64encode(content.encode()).decode()
}
if sha: payload["sha"] = sha
requests.put(url, headers=headers, json=payload)
```

## Ecosystem Context

- Antigravity: package manager, deploy tool
- OpenClaw: gateway Telegram/WhatsApp → giao tasks cho tao
- Claude: brainstorm, writing, quick chat
- Hermes (tôi): execute tasks, tích lũy skills, research sâu

## Quy Tắc Quan Trọng

1. KHÔNG bịa số liệu — luôn fetch thật từ GitHub API
2. Luôn update TRACKER.md sau mỗi batch push
3. Script video: hook quan trọng hơn nội dung
4. Khi uncertain → hỏi, không đoán
5. Batch 3+ repos cùng lúc khi có thể (delegate_task)
```
