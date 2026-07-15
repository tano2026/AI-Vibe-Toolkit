# Hallmark (Nutlope) — GitHub Repo

## TL;DR
Skill design chống "AI-slop" cho Claude Code, Cursor, Codex — bắt AI phải thiết kế UI/landing page có gu, không rơi vào mấy pattern hero-3-feature-CTA-footer nhàm chán mà LLM nào cũng bị nhồi vào não. 6.5K stars, top trending #4.

## Tool này dùng để làm gì
Bình thường bảo AI code UI, nó sẽ ra đúng 1 công thức: hero to đùng, 3 card feature, gradient tím-xanh, CTA cuối trang — nhìn phát biết AI làm. Hallmark là 1 skill (file SKILL.md + references) nhét vào Claude Code/Cursor/Codex, ép AI phải:
- Chọn 1 trong ~20 theme + macrostructure khác nhau cho mỗi brief (không lặp công thức)
- Chạy qua 57-65 "slop-test gate" trước khi trả kết quả (kiểm tra typography, contrast, spacing, copy có bịa số không...)
- Tự chấm điểm 1-5 trên 6 trục (Philosophy, Hierarchy, Execution, Specificity, Restraint, Variety) trước khi emit — dưới 3 điểm là tự sửa lại
- Có sẵn 4 chế độ: Design (làm mới), Audit (chấm điểm code cũ, ra punch list), Redesign (giữ nội dung, đổi cấu trúc), Study (bóc DNA từ 1 design mẫu mình thích)

Nói cách khác nó là phiên bản "quality gate" tự động cho design skill, giống `taste-skill` hay `frontend-design` skill sẵn có nhưng chuyên trị đúng vấn đề "trông rõ là AI làm" — rất hợp với `ui-component-forge` skill của mày để tránh generic AI slop.

## Setup từng bước
1. Clone repo hoặc copy trực tiếp phần skill:
```bash
git clone https://github.com/Nutlope/hallmark.git
```
2. Copy `skills/hallmark/SKILL.md` + folder `references/` vào thư mục skill của Claude Code/Cursor/Codex (project skill hoặc user skill directory).
3. Trigger bằng cách nói AI làm UI/landing page bình thường — skill tự động áp rule-set, không cần gọi lệnh đặc biệt (trừ khi muốn chỉ định verb: Design/Audit/Redesign/Study).
4. Muốn xem demo trực tiếp trước khi cài: vào `usehallmark.com`, nhấn phím `T` để cycle qua các theme.
5. Nếu muốn chạy site demo local:
```bash
cd site && python3 -m http.server 4173
```

## Ví dụ thực tế
Brief: "làm landing page cho An Bình Airport Services — Fast Track, SIM du lịch, đổi tiền". Không có Hallmark → AI ra đúng công thức hero-navy-gold + 3 feature card + CTA y hệt mọi landing page khác. Có Hallmark → skill tự chọn 1 macrostructure khác (ví dụ dạng "ticket/boarding-pass" thay vì hero chuẩn), áp đúng theme phù hợp tông "The quiet difference" (Deep Navy + Hanoi Gold), và stamp điểm tự chấm ngay đầu file code (`/* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */`) để mày biết nó tự tin chỗ nào, yếu chỗ nào.

## Lưu ý / Lỗi thường gặp
- Đây là **skill**, không phải app chạy độc lập — phải có Claude Code/Cursor/Codex mới dùng được, không dùng trực tiếp trong claude.ai chat UI thường.
- Rule-set khá "cứng" (57-65 gate) → với brief đơn giản/nhanh có thể thấy hơi rườm rà, tốn thêm 1-2 lượt suy nghĩ trước khi AI trả kết quả.
- Made by Together AI, license MIT — an toàn dùng thương mại, nhưng vẫn là skill do bên thứ 3 viết, nên review code UI xuất ra trước khi ship thật (đặc biệt phần copy — skill có rule "honest copy" chống bịa số liệu, nhưng vẫn nên tự kiểm lại).
- Không thay thế được `frontend-design` skill của Anthropic hay `taste-skill`/`ui-component-forge` đã có sẵn trong kho — nên coi là lớp filter bổ sung, không phải thay thế.

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng pain point "AI code UI nhìn generic" mà không cần tự viết rule; có sẵn 4 chế độ dùng linh hoạt (đặc biệt Audit rất hợp để review UI cũ trước khi launch); mở source, nhẹ, chỉ là file .md.
- Điểm yếu: rule-set nặng, không phải lúc nào cũng cần (task nhỏ/nội bộ không cần soi kỹ tới vậy); phụ thuộc hoàn toàn vào việc harness (Claude Code/Cursor) đọc đúng skill, không kiểm soát được nếu model bỏ qua rule.
- Có nên dùng không: 8/10 — dùng cho mọi landing page/UI khách hàng thấy (An Bình, Wonder Mart, Trùm Sân Bay channel page...), không cần cho code nội bộ/dashboard không ai xem ngoài mày.

## Link
- Repo: https://github.com/Nutlope/hallmark
- Docs/Demo: https://usehallmark.com

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hallmark là skill file (.md), không phải REST API — Hermes không gọi trực tiếp được.
# Cách dùng gián tiếp: fetch nội dung SKILL.md làm context nhồi vào prompt trước khi sinh HTML
import urllib.request

def fetch_hallmark_skill():
    url = "https://raw.githubusercontent.com/Nutlope/hallmark/main/skills/hallmark/SKILL.md"
    req = urllib.request.Request(url)
    return urllib.request.urlopen(req).read().decode()

# Nhồi nội dung này vào system prompt của OmniRoute khi request='creative' + có sinh UI
```

### OpenClaw
```bash
# Copy skill vào project trước khi OpenClaw giao task code UI cho Claude Code
git clone https://github.com/Nutlope/hallmark.git /tmp/hallmark
cp -r /tmp/hallmark/skills/hallmark ~/.claude/skills/hallmark
```

### Antigravity
```bash
# Không cần deploy service — chỉ cần đảm bảo folder skill có mặt trên VPS
mkdir -p /opt/skills && git clone https://github.com/Nutlope/hallmark.git /opt/skills/hallmark
```
> ⚠️ Đây là skill "đọc để áp rule", không có API endpoint thật — mọi tích hợp agent chỉ là "nhồi context", không phải gọi service.
