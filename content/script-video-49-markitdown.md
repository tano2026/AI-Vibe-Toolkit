# Script Video #49 — MarkItDown: Mọi File → Markdown, Microsoft Build

**Repo:** https://github.com/microsoft/markitdown | 153k⭐
**Hook:** "#1 trending GitHub tuần này — Microsoft convert PDF/Word/Excel/Audio → Markdown"

## 🎬 SCRIPT

**[HOOK 0:00-0:08]**
Số 1 GitHub trending tuần này.
153 nghìn stars.
Microsoft build.

**[PROBLEM 0:08-0:18]**
Muốn LLM đọc PDF → dùng pdfplumber.
Muốn đọc Word → python-docx.
Excel → pandas.
Audio → Whisper.
4 library. 4 cách setup khác nhau.

**[SOLUTION 0:18-0:40]**
MarkItDown. 1 tool. Tất cả formats.

```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("report.pdf")
# → clean markdown, ready to feed LLM
```

PDF, Word, Excel, PowerPoint, HTML, ảnh (OCR), audio (transcribe), YouTube transcript, Wikipedia...

**[USE CASE 0:40-0:55]**
Cho kế toán: convert báo cáo PDF → markdown → feed Claude phân tích.
Cho content: convert slide deck → markdown → script video.
Cho research: convert tài liệu dài → markdown → RAG.

**[CTA 0:55-1:05]**
pip install markitdown[all]
MIT. Microsoft. Link bio.

*Script #49 | AI Vibe Toolkit*
