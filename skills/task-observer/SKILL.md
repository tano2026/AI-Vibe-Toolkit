# Task Observer (a.k.a "One Skill to Rule Them All") — Prompt Template / System Prompt

## TL;DR
Meta-skill theo dõi mọi phiên làm việc của mày với Claude, tự phát hiện lỗ hổng trong bộ skill hiện có và đề xuất skill mới — thay vì để skill "đóng băng" từ lúc viết ra tới lúc quên mất nó tồn tại.

## Skill này dùng để làm gì
Nó không làm task thay mày. Nó **quan sát** trong lúc mày dùng Claude làm việc bình thường, rồi soi ra 3 thứ:

1. **Correction/adjustment** — mày sửa output, chỉnh hướng Claude làm → dấu hiệu 1 skill nào đó viết chưa đủ rõ
2. **Gap chưa skill nào cover** — mày đang làm tay 1 việc lặp lại → nó flag thành "ứng viên skill mới"
3. **Blind spot của chính nó** — task-observer tự theo dõi cả bản thân nó, tự log lại chỗ nó quan sát sai hoặc trigger nhầm ngữ cảnh

Cuối phiên, nó ra 1 **observation log** có cấu trúc: quan sát gì, ảnh hưởng skill nào, đề xuất sửa gì cụ thể. Mày review, duyệt, rồi mới apply — nó **không tự sửa skill của mày**, chỉ đề xuất. Có thêm 1 log riêng cho "cross-cutting principles" — pattern không thuộc riêng skill nào, được check chéo mỗi khi tạo/sửa skill mới.

Tác giả claim 6 tháng dùng đã log + áp dụng hơn 900 cải tiến trên 50 skill của ổng — phần lớn 50 skill đó cũng do chính observer này gợi ý tạo ra ban đầu.

## Setup từng bước
1. Tải repo: `git clone https://github.com/rebelytics/one-skill-to-rule-them-all` (hoặc download ZIP), giữ nguyên `SKILL.md` + folder `references/` đi cùng nhau — nếu chỉ cài mỗi SKILL.md thì skill vẫn chạy nhưng ở chế độ giảm tính năng (nó tự báo file nào thiếu).
2. Cài vào đúng chỗ theo môi trường:
   - **Claude web/app/mobile/Cowork:** zip cả folder (SKILL.md + references/) → Settings → Capabilities → upload
   - **Claude Code:** đặt vào `.claude/skills/task-observer/` (project-level) hoặc user-level skills dir
3. Đảm bảo skill được load ở MỌI session cần dùng — cách chắc nhất là thêm 1 dòng instruction vào CLAUDE.md (hoặc Project Instructions với claude.ai) kiểu: "Đầu mỗi phiên làm việc có dùng tool + tạo deliverable, load skill task-observer trước." Vì skill tự trigger theo mô tả không đủ tin cậy 100%.
4. Cuối mỗi phiên, chủ động hỏi "Any observations logged?" — đôi khi nó tìm thêm được thứ chưa kịp log lúc đang chạy.
5. Đặt lịch review định kỳ để apply các observation đang mở (tác giả chạy T2/T4/T6 sáng — tự điều chỉnh theo nhịp làm việc của mày).

## Ví dụ thực tế
Case của tác giả: dùng skill viết blog post, mỗi lần Claude ra draft mày đều phải sửa tông giọng bớt formal. Task Observer bắt được pattern "correction lặp lại 3 lần trong 2 tuần" → log observation: "skill `blog-writer` thiếu chỉ dẫn về tông giọng casual, đề xuất thêm section Tone Guidelines với 2 ví dụ trước/sau." Mày review, duyệt, skill được update — lần sau Claude ra draft đúng tông ngay từ đầu, không cần sửa nữa.

Với môi trường Claude Cowork/Code (có filesystem): observation ghi thẳng vào `[shared folder]/skill-observations/log.md`, đề xuất update ghi vào `[shared folder]/skill-updates/`. Với claude.ai web/mobile (không có filesystem): nó ra 1 **handoff doc** cuối phiên — mày copy sang phiên/Cowork task khác để apply.

## Lưu ý / Lỗi thường gặp
- Không tự sửa skill — chỉ đề xuất, review thủ công. Nếu mày kỳ vọng "tự động hoá hoàn toàn" là hiểu sai use case.
- Trigger dựa vào description-matching không đáng tin 100% → nếu không set structural trigger qua CLAUDE.md/Project Instructions, dễ bị bỏ sót ở những phiên cần quan sát nhất.
- Giá trị chỉ thật sự rõ khi bộ skill đã lớn (nhiều skill, nhiều phiên song song, cần review định kỳ). Setup nhỏ vài skill thì tính năng memory built-in của Claude đã đủ, sửa tay trực tiếp còn nhanh hơn — tác giả tự thừa nhận điều này trong README.
- Một số khái niệm trong SKILL.md gốc mang tính Claude-centric (`<available_skills>`, skill-creator reference) — dùng ngoài hệ Claude (OpenClaw, Hermes...) cần tự thích nghi lại, không copy y nguyên được.
- Kỷ luật vận hành quan trọng hơn công cụ: nếu không có nhịp review định kỳ, observation log chất đống mà không ai xử lý — vô dụng.

## Đánh giá cá nhân
- Điểm mạnh: đúng bài toán kho AI-Vibe-Toolkit đang gặp — bộ skill/mcp/repo ngày càng phình (skills đã 400+ entry), không ai audit tay nổi. Cơ chế "tự quan sát cả chính nó" khá thông minh, tránh method bị đóng băng.
- Điểm yếu: cần filesystem + kỷ luật review định kỳ mới phát huy hết giá trị — dùng qua claude.ai web/mobile (chế độ handoff doc) yếu hơn hẳn bản Cowork/Code. Repo còn khá mới (do 1 tác giả cá nhân duy trì), chưa có track record dài hạn ở quy mô lớn.
- Có nên dùng không: 7.5/10 — đáng cài thử ở lớp Claude Project (nơi Nobitano tương tác trực tiếp để research/viết kho), nhưng KHÔNG nên kỳ vọng nó tự vận hành trên Hermes/OpenClaw autonomous mà không có review layer của Nobitano.

## Link
- Repo: https://github.com/rebelytics/one-skill-to-rule-them-all
- Docs (User Guide): https://github.com/rebelytics/one-skill-to-rule-them-all/blob/main/USER-GUIDE.md
- Trang giới thiệu: https://www.rebelytics.com/task-observer/
- License: CC BY 4.0 — dùng/sửa/phân phối kể cả thương mại, chỉ cần credit tác giả Eoghan Henn / rebelytics.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Task Observer bản gốc dựa vào filesystem + Claude skill system — Hermes không có
# 2 thứ đó, nhưng có thể tự triển khai phần lõi: log observation vào file, không cần MCP nào.
import json, os, time
from datetime import datetime

LOG_PATH = "/home/hermes/skill-observations/log.md"

def log_observation(skill_affected: str, pattern: str, suggested_fix: str, kind: str = "correction"):
    """
    kind: 'correction' | 'gap' | 'self-blindspot'
    Gọi hàm này ngay sau khi Hermes nhận correction từ Nobitano qua Telegram,
    hoặc tự phát hiện đang làm tay 1 việc lặp lại không skill nào cover.
    """
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    entry = f"""
### Observation {int(time.time())}
- Kind: {kind}
- Skill affected: {skill_affected}
- Pattern: {pattern}
- Suggested fix: {suggested_fix}
- Status: OPEN
- Logged at: {datetime.now().isoformat()}
"""
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def get_open_observations():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, encoding="utf-8") as f:
        content = f.read()
    return [block for block in content.split("### Observation") if "Status: OPEN" in block]
```
> ⚠️ Hermes chỉ nên LOG, không tự sửa skill file trong kho — quyền ghi kho vẫn thuộc Claude (theo phân công hiện tại). Cuối mỗi ca chạy, Hermes gửi digest `get_open_observations()` qua Telegram để Nobitano quyết có báo Claude update kho không.

### OpenClaw
```bash
# Users đã report tích hợp thành công vào setup OpenClaw. Cài y hệt Claude Code:
git clone https://github.com/rebelytics/one-skill-to-rule-them-all ~/.openclaw/skills/task-observer
```
> Thêm dòng trigger vào OPENCLAW-PLAYBOOK.md: "Đầu mỗi task có dùng tool + tạo deliverable, load skill task-observer trước" — bản chất giống cách CLAUDE.md dùng structural trigger ép skill load.

### Antigravity
```bash
# Tạo shared folder dùng chung giữa Hermes + OpenClaw để 2 agent ghi chung 1 log
# thay vì tách rời (tránh observation bị phân mảnh không ai tổng hợp nổi)
mkdir -p /opt/shared/skill-observations /opt/shared/skill-updates
chmod 775 /opt/shared/skill-observations /opt/shared/skill-updates
```
> ⚠️ Đây là bước hạ tầng nền — chỉ cần làm 1 lần, không phải maintain liên tục.
