# Fact-Checker — Skill

## TL;DR
Kiểm tra độ chính xác của thông tin, số liệu, claims và nguồn dẫn. Có hệ thống rating rõ ràng, luôn web search để verify thay vì dựa vào training data.

## Khi nào dùng
- "Thông tin này có đúng không?"
- "Fact-check bài báo/post này cho tao"
- "Verify số liệu này"
- "Nguồn này đáng tin không?"
- Trước khi share tin tức quan trọng

## Nội dung skill / prompt
```
Bạn là fact-checker chuyên nghiệp. Khi nhận nội dung cần kiểm tra:

BƯỚC 1 - EXTRACT CLAIMS:
Liệt kê các claims cần verify (số liệu, ngày tháng, tên người/sự kiện, thống kê, trích dẫn)

BƯỚC 2 - WEB SEARCH:
Với mỗi claim quan trọng: search ít nhất 2-3 nguồn độc lập
Ưu tiên: nguồn gốc > báo uy tín > website thông thường

BƯỚC 3 - RATING & OUTPUT:
✅ Đúng — được xác nhận bởi nguồn đáng tin
🟡 Phần lớn đúng — đúng nhưng thiếu context
🔄 Có tranh cãi — nguồn tin cậy bất đồng  
🟠 Phần lớn sai — sai hoặc gây hiểu nhầm
❌ Sai — bị bác bỏ bởi bằng chứng
❓ Không verify được — thiếu bằng chứng

FORMAT OUTPUT:
### Claim: "[trích dẫn]"
Verdict: [rating]
Phân tích: [2-4 câu]
Nguồn: [link]

## Tổng kết: [đánh giá tổng thể]

QUAN TRỌNG:
- Luôn acknowledge khi không verify được
- Phân biệt opinion và fact
- Với tin gần đây: search kỹ hơn
```

## Setup từng bước
1. Paste prompt làm system prompt
2. Paste nội dung cần fact-check
3. Nhận report với rating cho từng claim
4. Click vào links để verify thêm nếu cần

## Ví dụ thực tế

**Input:** "Việt Nam có 100 triệu dân, là nước đông dân nhất Đông Nam Á"

**Output:**
```
### Claim 1: "Việt Nam có 100 triệu dân"
Verdict: ✅ Đúng
Phân tích: Dân số Việt Nam vượt 100 triệu người từ năm 2023.
Nguồn: Tổng cục Thống kê Việt Nam

### Claim 2: "đông dân nhất Đông Nam Á"  
Verdict: ❌ Sai
Phân tích: Indonesia mới là nước đông dân nhất ĐNA (~280 triệu). Việt Nam đứng thứ 3 sau Philippines.
Nguồn: Worldometers, UN Population Data
```

## Lưu ý / Lỗi thường gặp
- Không fact-check quan điểm cá nhân — chỉ fact/claim có thể verify
- Thông tin thay đổi theo thời gian → ghi rõ "đúng tính đến [năm]"
- Red flags: không có ngày đăng, headline sensational, ảnh dùng sai context

## Đánh giá cá nhân
- Điểm mạnh: Có hệ thống rating rõ ràng, minh bạch về giới hạn
- Điểm yếu: Phụ thuộc vào chất lượng search results, không phải lúc nào cũng tìm được nguồn
- Có nên dùng không: **8/10** — Cần thiết trong thời đại fake news

## Link
- Nguồn gốc: Build bởi AI Vibe Toolkit
- File skill: /skills/fact-checker.md

---

## 🤖 Hermes — Cách dùng skill này

**Use case:** verify thông tin trước khi báo cáo chủ

```python
import urllib.request, json, base64

def fetch_skill(skill_file, token="[GITHUB_TOKEN]"):
    req = urllib.request.Request(
        f"https://api.github.com/repos/tano2026/AI-Vibe-Toolkit/contents/skills/{skill_file}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    )
    data = json.loads(urllib.request.urlopen(req).read())
    return base64.b64decode(data["content"]).decode()

# Bước 1: Fetch skill này về
skill_prompt = fetch_skill("fact-checker.md")

# Bước 2: Extract phần "Prompt Template" hoặc "Nội dung skill"
# (tìm block code đầu tiên sau header ## Prompt)
import re
match = re.search(r'```\n([\s\S]+?)\n```', skill_prompt)
prompt = match.group(1) if match else skill_prompt

# Bước 3: Nhúng vào LLM call
def call_with_skill(user_input, system_prompt):
    # Gọi Claude/DeepSeek với skill làm system prompt
    payload = json.dumps({
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 2000,
        "system": system_prompt,
        "messages": [{"role": "user", "content": user_input}]
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=payload,
        headers={"x-api-key": "[ANTHROPIC_KEY]",
                 "anthropic-version": "2023-06-01",
                 "Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["content"][0]["text"]

# Dùng:
# result = call_with_skill("Phân tích thị trường AI tools VN 2026", prompt)
```

> Skills không cần cài gì — fetch về, nhúng làm system prompt, gọi LLM.
