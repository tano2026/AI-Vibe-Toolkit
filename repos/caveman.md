---
name: caveman
description: >
  Claude Code skill (+ Codex/Gemini/Cursor/40+ agent khác) bắt AI trả lời
  kiểu "người tiền sử" — cắt bỏ mạo từ, câu xã giao, rào đón — giữ nguyên
  100% nội dung kỹ thuật. Giảm 65-75% token output thật, đo bằng Claude API
  thật, có benchmark reproducible. 80k+ sao.
---

# Caveman — GitHub Repo

## TL;DR
Claude Code skill (+ Codex/Gemini/Cursor/40+ agent khác) bắt AI trả lời kiểu "người tiền sử" — cắt bỏ mạo từ, câu xã giao, rào đón — giữ nguyên 100% nội dung kỹ thuật. Giảm ~65-75% token output thật, đo bằng Claude API thật, có benchmark reproducible. 80k+ sao.

## Repo này dùng để làm gì
Vấn đề: AI trả lời dài dòng — "Sure! I'd be happy to help you with that. The issue you're experiencing is most likely caused by..." — tốn token, tốn tiền, tốn thời gian đọc. Caveman ép model bỏ hết phần đệm, chỉ giữ chất kỹ thuật: "Bug in auth middleware." Có 6 mức nén (lite → ultra → wenyan-ultra dùng cả văn ngôn Trung Quốc cổ để nén tối đa).

Không chỉ nén câu trả lời — còn có sub-skill `caveman-compress` nén luôn file memory (CLAUDE.md, project notes) để MỌI session sau đọc ít token hơn vĩnh viễn, không chỉ 1 lần.

## Setup từng bước
1. Cài 1 lệnh (macOS/Linux/WSL):
```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```
2. Windows PowerShell:
```powershell
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```
3. Cần Node ≥18, cài xong tự nhận diện agent nào có trên máy (Claude Code, Cursor, Codex, Gemini, Cline, Copilot...) và tự cài cho từng cái
4. Kích hoạt: gõ `/caveman` hoặc nói "talk like caveman"; tắt bằng "stop caveman" / "normal mode"
5. Chỉ scope 1 agent (vd chỉ OpenClaw):
```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash -s -- --only openclaw
```

## Ví dụ thực tế
Trước: *"The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object."* (69 token)

Sau khi bật caveman: *"New object ref each render. Inline object prop = new ref = re-render. Wrap in useMemo."* (19 token) — giảm 72%, nội dung kỹ thuật không mất chữ nào.

## Lưu ý / Lỗi thường gặp
- Tool bị flag "Snyk High Risk" ở sub-skill `caveman-compress` do pattern subprocess/file I/O — repo giải thích đây là false positive trong SECURITY.md, nhưng vẫn nên tự đọc code trước khi chạy trên máy có dữ liệu nhạy cảm
- Auto-clarity rule: caveman tự động tắt nén ở cảnh báo bảo mật, xác nhận hành động không đảo ngược được, chuỗi nhiều bước dễ hiểu nhầm — nên không lo mất an toàn vì nén quá đà
- Chỉ nén file .md/.txt/.typ/.tex — không đụng vào .py/.js/.json/.yaml/code thật, an toàn cho codebase
- Số liệu "65-75%" là trung bình 10 prompt (dao động 22-87%) — không phải con số cố định cho mọi loại task

## Đánh giá cá nhân
- Điểm mạnh: benchmark có script reproducible công khai trong `benchmarks/`, so sánh với baseline "answer concisely" (không phải so với verbose mặc định) — nên số liệu đáng tin hơn tool tự PR; MIT license; hỗ trợ 40+ agent qua 1 installer
- Điểm yếu: văn phong "caveman" có thể gây khó chịu khi đọc lâu (dù kỹ thuật vẫn chính xác); phần "wenyan" (văn ngôn Hán cổ) chỉ có ý nghĩa với model hiểu tiếng Trung cổ, không áp dụng cho pipeline tiếng Việt của kho
- Có nên dùng không: 8/10 — rất đáng thử cho Hermes/OpenClaw khi chạy session dài cần tiết kiệm token, đặc biệt hợp với nguyên tắc "output paste-ready, structured" Nobitano đã yêu cầu — nhưng nên test kỹ trên 1 agent trước khi bật đại trà

## Link
- Repo: https://github.com/JuliusBrussee/caveman
- Docs: https://juliusbrussee.github.io/caveman/
- Stars: ~81.700+ (rất cao so với tuổi repo, nên theo dõi thêm độ ổn định)

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Caveman la skill markdown, khong co REST API rieng.
# Hermes ap dung bang cach doc SKILL.md vao system prompt khi goi Claude API.
import urllib.request

SKILL_URL = "https://raw.githubusercontent.com/JuliusBrussee/caveman/main/skills/caveman/SKILL.md"

def load_caveman_skill():
    req = urllib.request.Request(SKILL_URL)
    return urllib.request.urlopen(req).read().decode()

# Nhet noi dung nay vao dau system prompt cua Hermes khi can tiet kiem token
caveman_skill_text = load_caveman_skill()
```

### OpenClaw
```bash
# Cai truc tiep, chi cho OpenClaw
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash -s -- --only openclaw
# Skill drop tai ~/.openclaw/workspace/skills/caveman/SKILL.md
```

### Antigravity
```bash
# Neu can nen file memory (CLAUDE.md, project notes) tren VPS de tiet kiem token moi session
npx caveman --with-init
# hoac chay sub-skill compress rieng cho 1 file:
cd caveman-compress && python3 -m scripts /path/to/CLAUDE.md
```
> ⚠️ Test trên 1 file backup trước — sub-skill compress OVERWRITE file gốc (có backup .original.md tự động nhưng vẫn nên cẩn thận với file quan trọng như HERMES-PLAYBOOK.md).


## 🧪 Test thực tế trên kho (03/07/2026)

Đã test nén `agents/HERMES-PLAYBOOK.md` (13.647 ký tự, ~70% là code Python) bằng đúng
quy tắc caveman-compress (không đụng code block, chỉ nén prose/mô tả). Kết quả: **chỉ giảm
3.2%**, KHÔNG đạt 65-75% như quảng cáo.

Lý do: con số 65-75% đo trên văn phong dài dòng kiểu "Sure! I'd be happy to help you with
that...". File playbook của kho đã terse sẵn (gạch đầu dòng, ít chữ đệm) + phần lớn là code
không được phép nén → ít chỗ để cắt.

**Kết luận cập nhật:** Caveman hợp với file/chat có nhiều PROSE DÀI DÒNG (trả lời chat, tài
liệu giải thích nhiều chữ) — KHÔNG hợp với file code-reference đã terse như HERMES-PLAYBOOK.
Đừng kỳ vọng con số marketing áp dụng đều cho mọi loại file.
