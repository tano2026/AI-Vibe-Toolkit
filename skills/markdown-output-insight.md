# Markdown Đang Phá Hoại Output AI — Insight Từ Anthropic Engineer

**Nguồn:** Kỹ sư Anthropic (DevAtlas tổng hợp) | tháng 6/2026
**Loại:** Insight/Best Practice — không phải repo

---

## Core Insight

Markdown trong AI output là vấn đề lớn hơn mày nghĩ:

```
AI generate: **Bold text** và `code blocks` và # Headers
→ Trông đẹp trong chat UI
→ Nhưng khi extract ra để dùng thực tế:
  - **text** → raw asterisks trong string
  - # Header → pound sign trong output
  - `code` → backticks literal
→ Cần strip/parse thêm bước
→ Bug tiềm ẩn, processing phức tạp
```

---

## Vấn Đề Thực Tế

### Khi Feed AI Output Vào Pipeline

```python
# AI trả về:
response = "**Tổng doanh thu:** 50,000,000 VND
## Phân tích..."

# Mày cần số thôi:
import re
# Phải strip markdown trước
clean = re.sub(r'\*+|#{1,6}\s|`+', '', response)
# Còn lại: "Tổng doanh thu: 50,000,000 VND
 Phân tích..."
```

### Khi Dùng Output Trong Code

```python
# AI generate function name với markdown:
# "Hãy tạo function **calculate_tax()**"
# → extract ra: **calculate_tax()** 
# → NameError khi chạy
```

---

## Fix — 3 Cách

### Cách 1: Prompt Rõ Ràng

```
"Trả lời bằng plain text. KHÔNG dùng markdown formatting.
 KHÔNG dùng **bold**, # headers, `backticks`, hay bullet points.
 Chỉ text thuần."
```

### Cách 2: Structured Output (Tốt Nhất)

```python
# Thay vì để AI format tự do
# → Yêu cầu JSON output

response = claude.messages.create(
    model="claude-sonnet-4-6",
    messages=[{
        "role": "user",
        "content": "Phân tích doanh thu. Output JSON: {revenue, analysis, recommendation}"
    }]
)
# → Parse JSON, không cần strip markdown
data = json.loads(response.content[0].text)
```

### Cách 3: Strip Function

```python
import re

def strip_markdown(text):
    # Remove headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r'\*{1,2}(.+?)\*{1,2}', r'', text)
    text = re.sub(r'_{1,2}(.+?)_{1,2}', r'', text)
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`(.+?)`', r'', text)
    # Remove bullet points
    text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)
    return text.strip()
```

---

## Khi Nào Dùng Markdown

```
✅ Dùng markdown khi:
- Render trong chat UI (claude.ai, ChatGPT)
- Documentation cho người đọc
- README files
- Content sẽ được render thành HTML

❌ KHÔNG dùng khi:
- Output đưa vào code xử lý
- Pipeline automation
- Database storage
- API response sẽ bị parse
- Telegram/SMS messages
```

---

## Apply Vào AI Vibe Toolkit

```python
# Khi Hermes/OpenClaw generate output để push GitHub
# → Dùng structured output hoặc strip trước khi push

# Ví dụ: generate repo .md file
response = claude.messages.create(
    messages=[{
        "role": "user",
        "content": f"Generate repo docs cho {repo_name}. Output plain markdown (cho file .md) không phải markdown trong markdown."
    }]
)
# File .md là markdown OK — nhưng content bên trong không nên có nested markdown
```

---
*AI Vibe Toolkit | Markdown Output Insight | tháng 6/2026*
