# HERMES-ADAPTER.md — Research Analytics Pro

> Adapter chính thức nối Research Analytics Pro vào Hermes (Python thuần,
> chỉ `urllib` + stdlib, không pip install). Không copy tĩnh nội dung skill
> vào đây — Hermes có `github()` (đã có sẵn trong bộ hàm gốc) nên fetch
> động từ kho khi cần, tránh lỗi thời khi skill trong kho được cập nhật.

## 3 vấn đề đã vá so với bản tĩnh trước đó

### 1. `read_file()` — thêm fallback stdlib, không phụ thuộc hoàn toàn MarkItDown

Bản gốc đã có `try/except ImportError` (không crash), nhưng chỉ trả lỗi thay vì cố đọc được gì đó. Bản vá thêm fallback đọc text/CSV/JSON bằng thư viện chuẩn trước khi báo lỗi:

```python
def read_file(file_path):
    """
    Đọc file: ưu tiên markitdown (PDF/XLSX/DOCX/PPTX) nếu có cài; nếu
    không, fallback đọc trực tiếp cho text/CSV/JSON bằng stdlib — không
    crash, không phụ thuộc hoàn toàn vào 1 thư viện ngoài.
    """
    import os, csv, json as jsonlib

    ext = os.path.splitext(file_path)[1].lower()

    # Fallback stdlib trước cho định dạng đơn giản — nhanh hơn, không cần pip
    if ext in ['.txt', '.md', '.csv', '.json', '.log']:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                if ext == '.csv':
                    reader = csv.reader(f)
                    return '\n'.join([', '.join(row) for row in reader])
                return f.read()
        except Exception as e:
            return f"❌ Lỗi đọc file (stdlib fallback): {e}"

    # Định dạng phức tạp (PDF/XLSX/DOCX/PPTX) — cần markitdown, báo rõ nếu thiếu
    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(file_path)
        return result.text_content
    except ImportError:
        return (f"⚠️ File .{ext} cần thư viện 'markitdown' (chưa cài trên Hermes — "
                f"quy tắc Hermes không pip install). Với PDF/XLSX/DOCX/PPTX, cần "
                f"nhờ Antigravity cài trước trên VPS, hoặc chuyển file sang .txt/.csv "
                f"thủ công trước khi đưa Hermes đọc.")
    except Exception as e:
        return f"❌ Lỗi đọc file: {e}"
```

### 2. Nguồn VN có thể bị chặn từ VPS — resilience pattern (KHÔNG trỏ vào skill chưa xác nhận)

Chưa xác nhận được `vn-web-research` có tồn tại/vị trí nào — không dựng fallback dựa trên claim chưa verify. Thay vào đó, mọi hàm fetch nguồn VN (`vn_news`, `search_wiki`, `vn_cpi`...) cần wrap qua retry pattern chung, tự báo lỗi rõ ràng thay vì im lặng trả rỗng:

```python
def resilient_fetch(fetch_fn, *args, fallback_note="", **kwargs):
    """
    Wrapper chung cho mọi hàm fetch nguồn có thể bị chặn (Cloudflare/WAF)
    từ IP VPS cụ thể. KHÔNG tự đoán nguồn thay thế — chỉ báo rõ trạng thái
    để người/agent gọi tiếp biết mà tự quyết định bước sau (đổi nguồn khác,
    thử qua nguồn free-API như tavily_search/ddg_search, hoặc chấp nhận
    thiếu dữ liệu phần này).
    """
    try:
        result = fetch_fn(*args, **kwargs)
        if not result or (isinstance(result, str) and len(result) < 20):
            return {"status": "empty_or_blocked", "data": None,
                    "note": f"Kết quả rỗng/quá ngắn — có thể bị chặn. {fallback_note}"}
        return {"status": "ok", "data": result, "note": None}
    except Exception as e:
        return {"status": "error", "data": None,
                "note": f"Lỗi khi fetch: {e}. {fallback_note}"}

# Cách dùng — thay vì gọi trực tiếp vn_news(query), gọi:
# result = resilient_fetch(vn_news, query,
#     fallback_note="Nếu bị chặn, thử tavily_search() hoặc ddg_search() thay thế")
# if result["status"] != "ok":
#     # tự quyết định bước tiếp — không giả định luôn có nguồn thay thế cụ thể
```

**Việc cần làm thật (không phải code):** Nobitano/Antigravity tự test trên VPS xem chính xác nguồn nào bị chặn (cafef/vnexpress/wikipedia theo claim, nhưng cần verify từng cái) — cập nhật danh sách nguồn bị chặn thật vào đây sau khi có kết quả test thật, không suy đoán trước.

### 3. API key optional — check rõ trước khi gọi, không im lặng crash

```python
import os

def check_api_key(key_name):
    """Kiểm tra key có sẵn trong biến môi trường chưa, báo rõ nếu thiếu."""
    key = os.environ.get(key_name)
    if not key:
        return None, f"⚠️ Thiếu {key_name} — set qua biến môi trường trước khi dùng hàm này."
    return key, None

# Áp dụng cho tavily_search, exa_search, github (cần TAVILY_API_KEY,
# EXA_API_KEY, GITHUB_TOKEN tương ứng) — mỗi hàm gọi check_api_key() trước,
# trả thông báo rõ thay vì lỗi urllib khó hiểu nếu thiếu key.
```

**Bảng phân loại — hàm nào cần key, hàm nào free hoàn toàn:**

| Cần API key | Free hoàn toàn (dùng ngay không cần setup) |
|---|---|
| `tavily_search()` — TAVILY_API_KEY | `fetch()`, `strip_html()`, `search_hn()`, `search_wiki()`, `search_reddit()`, `ddg_search()` |
| `exa_search()` — EXA_API_KEY | `npm_info()`, `pypi_info()`, `worldbank()`, `exchange_rate()`, `owid()` |
| `github()`, `github_search()`, `github_readme()` — GITHUB_TOKEN (dùng token đã có sẵn trong Project Instructions cho việc push kho) | `semantic_scholar()`, `arxiv_search()`, `pubmed_search()`, `check_domain_age()`, `check_wayback()`, `check_vn_company()` |

Nếu chưa set key nào — vẫn dùng được phần lớn hàm (2/3 danh sách là free), chỉ mất 3 nguồn cần đăng ký riêng.

## Cách dùng thật trên Hermes

```python
# Đầu script Hermes, import module này (hoặc paste trực tiếp nếu Hermes
# không hỗ trợ import file ngoài)
import urllib.request, json, base64, re, time, os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "tano2026/AI-Vibe-Toolkit"

def github(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def fetch_skill_from_kho(skill_path):
    """
    Fetch NỘI DUNG THẬT của 1 skill trong kho theo path — dùng khi cần đọc
    kiến thức 1 skill cụ thể (thay vì nhét tĩnh toàn bộ vào 1 file khổng lồ,
    Hermes tự lấy đúng cái cần, luôn là bản mới nhất trong kho).
    """
    data = github(f"repos/{REPO}/contents/{skill_path}")
    return base64.b64decode(data['content']).decode()

# Ví dụ: cần đọc skill source-evaluation khi đang research
# content = fetch_skill_from_kho("agents/research-analytics-pro/skills/source-evaluation/SKILL.md")
```

Với toàn bộ 34 hàm nghiên cứu (fetch, tavily_search, exa_search, worldbank, arxiv_search, check_vn_company...) — giữ nguyên bản gốc trong `agents/research-analytics-pro/system-prompt.md`, không lặp lại ở đây. Adapter này chỉ vá 3 điểm yếu đã phát hiện.
