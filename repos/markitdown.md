# MarkItDown — Convert Mọi File Thành Markdown (153k⭐, Microsoft)

**GitHub:** https://github.com/microsoft/markitdown
**Stars:** 153k⭐ | **License:** MIT | **By:** Microsoft AutoGen Team
**#1 GitHub Trending Tuần 23** | +15,015 stars — quán quân
**Install:** `pip install markitdown`

---

## Đây Là Gì

Python tool của Microsoft — **convert hầu hết file formats sang Markdown**. Dùng để feed documents vào LLM mà không cần xử lý phức tạp.

---

## Formats Hỗ Trợ

| Format | Chi tiết |
|--------|---------|
| **PDF** | Text extraction, basic layout |
| **Word (.docx)** | Text, headers, tables, lists |
| **Excel (.xlsx)** | Sheets → markdown tables |
| **PowerPoint (.pptx)** | Slides → markdown |
| **HTML** | Clean text, links |
| **Images** | OCR + AI description (cần API key) |
| **Audio** | Transcription (Whisper) |
| **CSV/JSON/XML** | Structured → markdown |
| **ZIP/tar** | Extract + convert nội dung |
| **YouTube** | Transcript extraction |
| **Wikipedia** | Clean article |
| **Bing Search** | Results → markdown |

---

## Cài & Dùng

```bash
pip install markitdown[all]  # tất cả features

# CLI
markitdown document.pdf > output.md
markitdown presentation.pptx > slides.md
markitdown spreadsheet.xlsx > data.md

# Python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("report.pdf")
print(result.text_content)

# Với LLM (cho image description)
from anthropic import Anthropic
client = Anthropic()
md = MarkItDown(llm_client=client, llm_model="claude-haiku-4-5")
result = md.convert("chart.png")  # AI mô tả chart
```

---

## MCP Server

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "uvx",
      "args": ["markitdown-mcp"]
    }
  }
}
```

```bash
# Trong Claude Code
"Convert file PDF này sang markdown để tôi đọc"
"Extract text từ presentation.pptx"
"Convert Excel report sang markdown table"
"Transcribe audio file này"
```

---

## Workflow Kế Toán + AI

```python
from markitdown import MarkItDown
md = MarkItDown()

# Convert báo cáo PDF sang markdown → feed vào Claude
result = md.convert("bao-cao-tai-chinh-q2.pdf")
# → Claude analyze markdown text (rẻ hơn nhiều so với PDF vision)

# Convert Excel sao kê → markdown table
result = md.convert("sao-ke-ngan-hang.xlsx")
# → Feed vào ke-toan-automation prompt
```

---

## Đánh Giá Cá Nhân

153k stars — số 1 trending tuần này, và xứng đáng. Microsoft build, chất lượng cao.

Vấn đề trước đây: muốn cho LLM đọc PDF/Word/Excel phải dùng nhiều library khác nhau. MarkItDown giải quyết bằng 1 tool duy nhất, output chuẩn markdown.

**Rating: 9.5/10** — Cài ngay, dùng cho mọi workflow cần đọc documents.

---
*Nguồn: github.com/microsoft/markitdown | 153k⭐ | MIT | Microsoft | tháng 6/2026*

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity.

### Hermes (Python)
```python
# Antigravity phải cài trước: pip install markitdown
from markitdown import MarkItDown

md = MarkItDown()

def read_file(path_or_url):
    """Đọc PDF/DOCX/XLSX/PPTX/HTML → markdown"""
    result = md.convert(path_or_url)
    return result.text_content

# Examples:
# text = read_file("/path/to/report.pdf")
# text = read_file("https://example.com/document.pdf")
# text = read_file("/path/to/data.xlsx")
# text = read_file("/path/to/slides.pptx")
#
# Sau đó pass text vào LLM để phân tích
```

### OpenClaw
```bash
npx -y markitdown-mcp
```

### Antigravity
```bash
pip install markitdown
# Test: python3 -c "from markitdown import MarkItDown; print('OK')"
```
> ⚠️ No API key. Đọc được PDF scanned nếu cài thêm: pip install markitdown[all]
