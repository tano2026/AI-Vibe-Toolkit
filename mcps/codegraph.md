# CodeGraph — Index Code Local Cho AI Agent Đọc Đúng File

> Đồ thị tri thức code chạy 100% local, nối vào Claude Code/Cursor/Codex qua MCP để agent đọc đúng file cần thay vì quét lan man.

---

## 📌 Thông tin cơ bản

| | |
|--|--|
| **Dùng để làm gì** | Cho AI coding agent 1 index sẵn của codebase, đỡ phải tự grep/glob dò file |
| **Độ khó setup** | ⭐⭐☆☆☆ Dễ |
| **Cần biết code không** | Không — chạy lệnh có sẵn |
| **Free hay trả phí** | Free, mã nguồn mở (MIT) |
| **GitHub** | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) ⭐ 43,000+ |

---

## 🎯 Vấn đề nó giải quyết

Khi Claude Code/Cursor cần hiểu 1 codebase, nó tự mò bằng grep/glob/Read — với repo to (VS Code, Django...) việc này tốn rất nhiều tool call và token chỉ để "tìm đường".

**CodeGraph fix cái này:** parse trước toàn bộ code bằng tree-sitter, lưu vào SQLite local (symbol, call graph, file structure), expose ra cho agent qua MCP server. Agent hỏi 1 câu, có thẳng source liên quan, không cần dò file thủ công nữa.

---

## ⚡ Setup trong 3 bước

```bash
# Bước 1: Cài CLI (không cần Node, tự tải bản đúng OS)
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
# Windows (PowerShell): irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex

# Bước 2: Mở terminal MỚI, nối vào agent đang dùng (tự detect Claude Code/Cursor/Codex/Gemini CLI...)
codegraph install

# Bước 3: Vào project, khởi tạo + index lần đầu
cd ten-project-cua-may
codegraph init -i
```

Restart lại agent sau bước 2 để nó load MCP server mới.

---

## 💡 Dùng thế nào

Không cần gõ lệnh gì thêm — sau khi cài, agent tự gọi tool `codegraph_explore`, `codegraph_search`, `codegraph_callers`... mỗi khi cần hiểu code:

```
Prompt mày gõ vào Claude Code:
"Request đi qua hệ thống của tao như thế nào, từ route tới database?"

Claude tự gọi codegraph_explore thay vì gọi 10 lệnh grep/read,
trả lời thẳng kèm source liên quan trong 1 lượt.
```

Benchmark chính chủ trên repo VS Code (~10k file): 4 tool call thay vì 21, 640k token thay vì 1.79M, rẻ hơn 18%, nhanh hơn 11%.

---

## ⚠️ Lưu ý

- Chỉ đáng gắn với codebase đủ lớn (vài trăm file trở lên) — repo nhỏ thì agent tự grep cũng đủ nhanh, gắn thêm chưa chắc lợi.
- Báo "CodeGraph not initialized" → quên chạy `codegraph init` trong project đó.
- Mấy framework convention-heavy (Django, Spring) độ chính xác cross-file thấp hơn (74-83%) so với code thuần OOP.
- Dùng theo kiểu embed thư viện trực tiếp (`import CodeGraph from '@colbymchenry/codegraph'`) thì cần Node 22.5+; còn cài CLI bình thường thì không cần vì nó tự bundle runtime riêng.

---

## 🔗 Hay kết hợp với

- **Context7** — Context7 lo docs thư viện ngoài, CodeGraph lo hiểu code nội bộ của chính project mày

---

## 📊 Đánh giá cá nhân

| Tiêu chí | Điểm |
|----------|------|
| Dễ setup | ⭐⭐⭐⭐☆ |
| Thực sự hữu ích | ⭐⭐⭐⭐☆ |
| Docs rõ ràng | ⭐⭐⭐⭐⭐ |

**Tóm lại:** Repo nhỏ thì bỏ qua cũng được, nhưng codebase lớn thì đây là cách rẻ nhất để agent đỡ tốn token dò file — số liệu benchmark đầy đủ, không nói mồm.

---

*Thêm vào kho: 06/2026 | Nguồn: github.com/colbymchenry/codegraph*
