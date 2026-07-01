# DeepSeek-Reasonix — GitHub Repo

## TL;DR
AI coding agent chạy trên terminal, được build đặc biệt để tận dụng prefix cache của DeepSeek. Session dài mà chỉ tốn 1/5 chi phí input token so với các agent thông thường — vì loop append-only, cache hit 90%+.

## Repo này dùng để làm gì
Nói thẳng: đây là Claude Code nhưng dùng DeepSeek thay vì Anthropic.

Mày gõ lệnh trong terminal, nó đọc code, sửa file, chạy test, commit — tất cả trong 1 vòng lặp. Điểm khác biệt chính so với các coding agent khác là nó được thiết kế từ đầu để giữ prefix cache của DeepSeek ổn định. Nghĩa là:

- Session 18 phút, cache hit 95%, tốn $0.043 — thay vì ~$0.20 nếu không có cache
- Càng làm việc lâu trong cùng session thì càng rẻ, không phải ngược lại

Phù hợp với mày nếu:
- Dùng DeepSeek API thường xuyên (đặc biệt OmniRoute proxy)
- Cần coding agent terminal chạy trên VPS (Antigravity) không cần GUI
- Muốn alternative rẻ hơn Claude Code cho các task lặp đi lặp lại

## Setup từng bước

### Cài nhanh (npm)
```bash
npm install -g reasonix@next
# hoặc alias ngắn hơn:
npm install -g dsnix
```

### Cài qua Homebrew (macOS)
```bash
brew install esengine/reasonix/reasonix
```

### Config tối thiểu
Tạo file `reasonix.toml` trong thư mục project:
```toml
default_model = "deepseek-flash"

[[providers]]
name = "deepseek-flash"
kind = "openai"
base_url = "https://api.deepseek.com"
model = "deepseek-v4-flash"
api_key_env = "DEEPSEEK_API_KEY"
```

### Set API key
```bash
export DEEPSEEK_API_KEY="sk-..."
# hoặc dùng OmniRoute endpoint thay base_url
```

### Chạy
```bash
reasonix          # launch coding agent trong thư mục hiện tại
reasonix code     # tương đương
reasonix chat     # chat thuần, không có file/shell tools
reasonix run "thêm retry với backoff vào http client"  # one-shot
```

## Ví dụ thực tế

**Tao dùng cho Wonder Mart:** Gõ `reasonix` trong thư mục backend, rồi:
```
> thêm rate limiting vào tất cả API endpoints
```
Nó tự đọc codebase, tìm đúng files, viết middleware, update routes, chạy test — xong báo kết quả. Không cần copy paste gì cả.

**Kết quả thực tế từ README của repo:**
- 435M input tokens trong 1 ngày → cache hit 99.82% → tốn $12 thay vì $61

## Lưu ý / Lỗi thường gặp

- **Cần DeepSeek API key trả phí** — không có free tier. Nhưng rẻ hơn Claude Code nhiều vì cache
- **Windows có bug** — repo đang có nhiều issue Windows-specific (xem issues trang). Linux/macOS ổn
- **Đang trong giai đoạn Go rewrite (v2)** — v0.x bị deprecated, phải cài `@next` không phải `latest`
- **OmniRoute tương thích**: đổi `base_url` thành endpoint OmniRoute của mày, `kind = "openai"` giữ nguyên
- **Node ≥ 22** required cho npm package (binary Go nhưng wrapper vẫn cần Node)

## Đánh giá cá nhân

- **Điểm mạnh:** Cache optimization thật sự hoạt động — session dài mà cost không tăng tuyến tính. Single binary, không deps lằng nhằng. MCP-compatible nên cắm thêm tools được. Đang develop rất active (25k stars, v2 Go rewrite)
- **Điểm yếu:** Buộc phải dùng DeepSeek (hoặc OpenAI-compatible endpoint). Windows support kém. Docs hơi lộn xộn vì đang chuyển từ v0 sang v2
- **Có nên dùng không:** 8/10 nếu mày đã dùng DeepSeek API và cần coding agent terminal. 4/10 nếu mày chỉ muốn thử cho vui vì cần setup API key trả phí

## Link
- Repo: https://github.com/esengine/DeepSeek-Reasonix
- Docs/Website: https://esengine.github.io/DeepSeek-Reasonix/
- Stars: ~25.6k ⭐

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import subprocess

# Chạy Reasonix one-shot từ Hermes
result = subprocess.run(
    ["reasonix", "run", "task description here"],
    cwd="/path/to/project",
    capture_output=True,
    text=True,
    env={**os.environ, "DEEPSEEK_API_KEY": "[DEEPSEEK_API_KEY]"}
)
print(result.stdout)
```

### OpenClaw
```bash
# Cài global, dùng trong browser automation pipeline
npm install -g reasonix@next

# Chạy trong project directory
cd /path/to/project && reasonix run "your task"
```

### Antigravity (VPS Tencent Cloud)
```bash
# Cài trên VPS
npm install -g reasonix@next

# Config với OmniRoute endpoint
cat > ~/reasonix.toml << 'TOML'
default_model = "deepseek-flash"

[[providers]]
name = "deepseek-flash"
kind = "openai"
base_url = "http://localhost:PORT"  # OmniRoute local endpoint
model = "deepseek-v4-flash"
api_key_env = "OMNIROUTE_KEY"
TOML
```

> ⚠️ Đổi `base_url` thành OmniRoute endpoint của mày để tiết kiệm cost thêm nữa — OmniRoute đã free ~1.6B tokens/month từ 231 providers
