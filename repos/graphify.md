# Graphify — GitHub Repo

## TL;DR
Graphify biến cả folder code/SQL schema/docs/ảnh/video thành 1 knowledge graph truy vấn được — agent (Claude Code, Hermes, OpenClaw...) hỏi 1 câu là ra đúng chỗ liên quan, không cần đọc hết file hay grep mò. Từ 50K lên 76K+ stars chỉ trong vài tháng, viral sau khi Andrej Karpathy nhắc tới.

## Repo này dùng để làm gì
Vấn đề: agent như Hermes khi cần hiểu 1 codebase/kho lớn (như AI-Vibe-Toolkit đang có 113 repos, 84 skills...) phải đọc từng file hoặc grep, tốn context + dễ bỏ sót liên kết giữa các phần. Graphify quét cả folder — code (31 ngôn ngữ qua tree-sitter AST), SQL schema, docs, PDF, ảnh, video — rồi build ra 1 graph nối các khái niệm/entity với nhau.

Sau khi build graph, gõ `/graphify` trong Claude Code (hoặc lệnh tương ứng trong Hermes/OpenClaw), agent query graph thay vì đọc file thô. README claim giảm tới 71.5x số token cần dùng mỗi lần query so với đọc raw context — với corpus nhỏ (~6 file) thì graph không lời bằng do đã fit context window sẵn, giá trị thật hiện ra rõ khi corpus lớn (50+ file).

Output sau khi build: `graph.html` (graph tương tác click được), `GRAPH_REPORT.md` (tóm tắt kiến trúc, câu hỏi gợi ý), `graph.json` (data thô để query lại không cần đọc lại file).

## Setup từng bước
1. Cài CLI (tên PyPI là `graphifyy`, 2 chữ y — CLI vẫn gọi là `graphify`):
```bash
uv tool install graphifyy && graphify install
# hoặc: pipx install graphifyy && graphify install
```
2. Cài skill cho agent (ghi file config để agent biết ưu tiên query graph thay vì grep):
```bash
graphify install --project   # cài scoped vào đúng repo hiện tại
```
3. Trong Claude Code/Cursor/OpenClaw, gõ:
```
/graphify .
```
(Codex dùng `$graphify .` vì `/` bị coi là path separator)
4. Query lại graph mà không cần đọc file thô:
```bash
graphify query "kho AI-Vibe-Toolkit tổ chức skill theo cấu trúc nào?"
```

## Ví dụ thực tế
Kho AI-Vibe-Toolkit đang có 113 repos + 84 skills + 37 MCPs rời rạc theo file .md. Khi Hermes cần trả lời "tool nào trong kho liên quan tới web scraping", nó phải đọc/grep từng file. Chạy `/graphify .` trên toàn bộ kho 1 lần, build ra graph nối các entry theo chủ đề (scraping, agent framework, local LLM...), sau đó Hermes chỉ cần `graphify query "tool scraping trong kho"` là ra đúng danh sách (Firecrawl, và các tool liên quan) kèm quan hệ giữa chúng, không cần đọc hết 113 file.

## Lưu ý / Lỗi thường gặp
- **Tên package PyPI khác tên CLI** — cài `graphifyy` (2 chữ y), lệnh gọi vẫn là `graphify`. Nhầm cái này là lỗi "package not found" phổ biến nhất.
- **Code được xử lý local (AST), không gửi ra ngoài** — nhưng docs/PDF/ảnh cần semantic extraction thì gửi qua model API (Anthropic/OpenAI tùy platform), không phải 100% on-device như quảng cáo ban đầu nghe qua.
- **Cần API key cho phần semantic extraction** (docs/ảnh) — nếu chỉ có code thuần thì graphify tự skip bước này, không cần key, đừng để agent loop hỏi key không cần thiết.
- **71.5x giảm token chỉ đúng khi corpus lớn** — thử trên kho nhỏ (vài chục file) như 1 vài repo con thì lợi ích không rõ, hợp nhất khi áp cho toàn bộ kho AI-Vibe-Toolkit.

## Đánh giá cá nhân
- **Điểm mạnh:** Tích hợp sẵn với Hermes, OpenClaw, Antigravity (README liệt kê thẳng tên 3 agent này trong list platform hỗ trợ) — nghĩa là gần như build ra để dùng cho đúng stack hiện tại. Multimodal thật (video transcribe bằng Whisper, ảnh/diagram đọc được), không chỉ code.
- **Điểm yếu:** Setup ban đầu (build graph lần đầu cho corpus lớn) tốn thời gian + credit API cho phần semantic extraction. Một vài ngôn ngữ (PHP/SQL/Nim) còn bug fold sai theo changelog gần nhất — không phải hoàn hảo 100%.
- **Có nên dùng không:** 8/10 — rất khớp việc tổ chức lại kho AI-Vibe-Toolkit thành 1 graph truy vấn được thay vì chỉ file .md rời, đặc biệt khi kho ngày càng phình to (113 repos rồi).

## Link
- Repo: https://github.com/safishamsi/graphify
- PyPI: https://pypi.org/project/graphifyy/

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess, json

def graphify_build(path="."):
    subprocess.run(["graphify", path], check=True)

def graphify_query(question):
    result = subprocess.run(
        ["graphify", "query", question],
        capture_output=True, text=True, check=True
    )
    return result.stdout

# Build graph 1 lần cho toàn bộ kho, sau đó query nhiều lần không cần đọc lại file
graphify_build("/path/to/AI-Vibe-Toolkit")
answer = graphify_query("tool nào trong kho liên quan web scraping?")
print(answer)
```

### OpenClaw
```bash
# Graphify hỗ trợ OpenClaw native (sequential extraction, chưa parallel)
graphify install --project --platform openclaw
# Gõ trong OpenClaw: /graphify .
```

### Antigravity
```bash
# Graphify hỗ trợ Google Antigravity native trong danh sách platform
uv tool install graphifyy
graphify install --project --platform antigravity
```
> ⚠️ Semantic extraction cho docs/ảnh cần gọi model API (tốn token OmniRoute) — nếu chỉ cần build graph cho code thuần (Python/JS), graphify tự dùng AST local, không tốn API call nào.
