# LoopX — GitHub Repo

## TL;DR
LoopX không phải là 1 agent — nó là "lớp trên" của agent, giữ trạng thái bền vững (objective, gate cần người duyệt, todo, evidence, quota) xuyên suốt session, tool, và agent khác nhau. Đúng bài toán mày đang gặp với Hermes/OpenClaw chạy 24/7: cần thứ gì đó điều phối task dài hạn mà không phụ thuộc vào 1 agent cụ thể.

## Repo này dùng để làm gì
LoopX là state kernel local-first, agent-agnostic — chạy trên Codex, Claude Code, hay bất kỳ agent harness nào khác mà không thay thế agent đó. Nó giải quyết vấn đề: agent 1 session làm xong task ngắn thì ổn, nhưng việc dài hạn (200 giờ, nhiều ngày) thì mục tiêu thay đổi, cần người quyết định giữa chừng, evidence cũ mất giá trị, agent phải bàn giao việc cho agent khác — memory chat và 1 cái timer không đủ để quản lý chuyện đó.

Kiến trúc theo mô hình **Agent → Capability → Provider**: agent lên kế hoạch, dùng tool, thực hiện 1 hành động có giới hạn qua host/runtime; capability gọi hệ thống ngoài và trả về kết quả; provider chuẩn hoá output, validate, đề xuất transition có kiểu. LoopX giữ layer điều khiển riêng: nếu cần con người quyết định → hỏi câu cụ thể và chờ; nếu có safe fallback → dùng fallback.

## Setup từng bước

1. Cài đặt:
```bash
curl -fsSL https://huangruiteng.github.io/loopx/install.sh | bash
export PATH="$HOME/.local/bin:$PATH"
```
2. Kiểm tra sức khỏe: `loopx doctor`
3. Vào thư mục project cần quản lý: `cd /path/to/your-project`
4. Kết nối: `loopx connect`
5. Xem trạng thái: `loopx status`
6. Xem catalog năng lực đầy đủ: `loopx capability list --format json`

## Ví dụ thực tế

Tình huống: Hermes chạy research pipeline nhiều ngày cho `research-analytics-pro`, cần theo dõi tiến độ, biết khi nào cần Nobitano duyệt, và không mất context nếu VPS restart.

- `loopx connect` trong thư mục pipeline
- Set objective: "Hoàn thành research 10 ngành cho domain playbook, mỗi ngành cần Nobitano duyệt trước khi publish"
- LoopX giữ state: ngành nào đã xong, ngành nào đang chờ duyệt, evidence từng bước
- Nếu VPS restart giữa chừng → state vẫn còn, Hermes reconnect và tiếp tục đúng chỗ dừng
- Khi cần duyệt → LoopX hỏi câu cụ thể thay vì Hermes tự quyết định bừa

## Lưu ý / Lỗi thường gặp

- Có 2 repo cùng tên "loopx" trên GitHub với nội dung tương tự nhau — `huangruiteng/loopx` là bản có nhiều context nhất (docs, blog review độc lập từ explainx.ai), dùng bản này.
- Còn khá mới (~1.7K stars, v0.4.1), 14 contributors — chưa phải công cụ chín muồi cấp production lớn.
- Case study "4 ngày không cần can thiệp" hay "7 PR merged" trên trang chủ là **user report**, không phải benchmark độc lập verify — đọc với con mắt phê phán.
- Không thay thế agent runtime (Hermes/OpenClaw vẫn cần chạy như bình thường) — LoopX chỉ là control plane phía trên.

## Đánh giá cá nhân

- **Điểm mạnh:** Đúng pain point thật — agent chạy dài hạn trên VPS 24/7 (như setup của Nobitano) rất cần layer quản lý objective + gate + quota bền vững, không phụ thuộc vào 1 chat session cụ thể. Agent-agnostic là điểm cộng lớn vì không khoá cứng vào Hermes hay Claude Code riêng.
- **Điểm yếu:** Project còn non trẻ, docs case study thiên về marketing hơn benchmark khách quan. Cần thời gian test thực tế trước khi tin tưởng hoàn toàn cho production.
- **Có nên dùng không:** 7/10 — Đáng thử nghiệm cho research-analytics-pro hoặc trum-san-bay pipeline (loại việc dài hạn, nhiều bước duyệt), nhưng nên pilot nhỏ trước khi áp dụng toàn bộ agent infrastructure.

## Link
- Repo: https://github.com/huangruiteng/loopx
- Trang chủ: https://huangruiteng.github.io/loopx/
- Review độc lập: https://explainx.ai/blog/loopx-agent-control-plane-loop-engineering-august-2026

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json

def loopx_status(project_dir: str) -> dict:
    """Lấy trạng thái LoopX hiện tại của 1 project."""
    result = subprocess.run(
        ["loopx", "status", "--format", "json"],
        cwd=project_dir, capture_output=True, text=True
    )
    return json.loads(result.stdout)

def loopx_connect(project_dir: str):
    """Kết nối LoopX vào project — chạy 1 lần khi bắt đầu pipeline dài hạn."""
    subprocess.run(["loopx", "connect"], cwd=project_dir, check=True)
```

### OpenClaw
```bash
# Cài LoopX trên VPS để giám sát pipeline dài hạn (trum-san-bay, research-analytics-pro)
curl -fsSL https://huangruiteng.github.io/loopx/install.sh | bash
loopx doctor
```

### Antigravity
```bash
# Deploy như 1 layer giám sát, không cần PM2 riêng vì LoopX chạy local-first
# Đảm bảo PATH có $HOME/.local/bin sau khi cài
export PATH="$HOME/.local/bin:$PATH"
loopx doctor
```
> ⚠️ Đây là control plane, không phải executor — vẫn cần Hermes/OpenClaw chạy task thật, LoopX chỉ giữ state và gate quyết định.
