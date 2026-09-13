---
name: swe-agent
description: >
  Stars: 19k+ Tác giả: princeton-nlp (Princeton University) Domain: Agent tự động sửa lỗi GitHub issue
---

# SWE-agent — quăng cho nó 1 GitHub issue, nó tự sửa và tạo PR

**GitHub:** https://github.com/princeton-nlp/SWE-agent (hay `SWE-agent/SWE-agent`)
**Tác giả:** Princeton NLP Group (John Yang, Carlos E. Jimenez) — công bố tại NeurIPS 2024
**Stars:** 19k+ | MIT License | swe-agent.com

---

## TL;DR

Đưa 1 GitHub issue cho SWE-agent, nó tự đọc codebase, tìm nguyên nhân, sửa code, chạy test, và tạo pull request — dùng LM bất kỳ (GPT-4o, Claude Sonnet...), không khoá vào 1 hãng.

## Tool này dùng để làm gì

Điểm khác biệt so với coding agent thường (Claude Code, Cursor) là SWE-agent thiết kế riêng 1 "Agent-Computer Interface" (ACI) — bộ lệnh và định dạng phản hồi tối ưu cho LM thao tác code, thay vì chỉ nối LM với terminal bash thông thường. Nhóm nghiên cứu chứng minh cách thiết kế interface này ảnh hưởng lớn tới độ chính xác — tương tự việc UI tốt giúp con người làm việc hiệu quả hơn.

Ngoài sửa bug GitHub, còn dùng được cho: tìm lỗ hổng bảo mật (bản EnIGMA cho offensive cybersecurity), và giải bài toán lập trình thi đấu.

## Setup từng bước

1. Cách nhanh nhất — thử ngay trên trình duyệt không cần cài gì:
```
Mở GitHub Codespaces từ nút "Open in GitHub Codespaces" trong repo
```
2. Cài local:
```bash
git clone https://github.com/princeton-nlp/SWE-agent.git
cd SWE-agent
pip install -e .
```
3. Chạy trên 1 issue cụ thể:
```bash
sweagent run --agent.model.name=claude-sonnet-4-5 \
  --env.repo.github_url=https://github.com/user/repo \
  --problem_statement.github_url=https://github.com/user/repo/issues/123
```

## Ví dụ thực tế

Repo `web-abtrip` (TypeScript) có issue báo lỗi form đặt vé không validate email đúng — quăng link issue cho SWE-agent chạy với Claude Sonnet, nó tự đọc code, sửa hàm validate, chạy test có sẵn xác nhận pass, rồi tạo PR để review thay vì tự ngồi debug từ đầu.

## Lưu ý / Lỗi thường gặp

- Tỷ lệ giải đúng trên benchmark SWE-bench khoảng 12-15% với model cũ hơn — chất lượng fix phụ thuộc rất nhiều vào LM chọn dùng, không phải lúc nào cũng đúng, luôn cần review PR trước khi merge
- Chạy trong môi trường Docker cô lập để test — cần cấu hình repo có test suite sẵn thì SWE-agent mới verify được fix đúng hay sai; repo không có test tốt thì độ tin cậy giảm
- Hướng nghiên cứu học thuật (Princeton) nên trải nghiệm không mượt bằng sản phẩm thương mại như Cursor/Devin, cần biết dùng CLI

## Đánh giá cá nhân

- **Điểm mạnh:** mã nguồn mở hoàn toàn, không khoá vào 1 LM provider; ý tưởng ACI khá hay, đáng học hỏi cách thiết kế agent-tool interface; benchmark rõ ràng, có paper NeurIPS đứng sau
- **Điểm yếu:** tỷ lệ tự sửa đúng không cao bằng công cụ thương mại mới nhất, luôn cần người review; setup phức tạp hơn Cursor/Claude Code vốn plug-and-play
- **Có nên dùng không:** 6.5/10 — thú vị để thử nghiệm/học cách xây agent riêng, nhưng cho công việc thật (sửa bug web-abtrip) vẫn nên ưu tiên Claude Code trước, SWE-agent hợp cho task tự động hoá quy mô lớn (chạy hàng loạt issue) hơn là việc lẻ tẻ

## Link
- Repo: https://github.com/princeton-nlp/SWE-agent
- Docs: https://princeton-nlp.github.io/SWE-agent/
- Website: https://swe-agent.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# SWE-agent có CLI, Hermes gọi qua subprocess để tự động hoá chạy hàng loạt issue
import subprocess

def fix_github_issue(repo_url, issue_url, model="claude-sonnet-4-5"):
    result = subprocess.run([
        "sweagent", "run",
        f"--agent.model.name={model}",
        f"--env.repo.github_url={repo_url}",
        f"--problem_statement.github_url={issue_url}",
    ], capture_output=True, text=True)
    return result.stdout
```

### OpenClaw
```bash
git clone https://github.com/princeton-nlp/SWE-agent.git
cd SWE-agent && pip install -e .
```

### Antigravity
```bash
# Cần Docker để chạy môi trường cô lập test
docker --version
git clone https://github.com/princeton-nlp/SWE-agent.git /opt/swe-agent
cd /opt/swe-agent && pip install -e .
```
> ⚠️ Luôn review PR do SWE-agent tạo trước khi merge — tỷ lệ tự sửa đúng chưa đủ cao để tin tưởng auto-merge.
