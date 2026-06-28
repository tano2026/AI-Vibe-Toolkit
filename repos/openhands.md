# OpenHands — GitHub Repo

## TL;DR
AI Software Engineer agent mã nguồn mở — giao task, nó tự code, test, debug, deploy. 78.4K stars. Thay thế Devin (tool AI coding trả phí $500/tháng) hoàn toàn free và self-hostable.

## Repo này dùng để làm gì
OpenHands (trước gọi là OpenDevin) là AI agent có thể:
- Viết code từ spec mô tả bằng ngôn ngữ tự nhiên
- Chạy và test code trong sandbox
- Debug lỗi tự động
- Browse web để research
- Đọc/write file, chạy terminal commands
- Submit PR lên GitHub

Khác với Claude Code hay Cursor (AI assist trong editor của mày), OpenHands chạy **autonomous** — mày giao task, nó tự làm từ đầu đến cuối trong môi trường sandbox riêng.

## Setup từng bước
```bash
# Cài Docker trước, sau đó:
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.39-nikolaik

docker run -it --rm   -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.39-nikolaik   -v /var/run/docker.sock:/var/run/docker.sock   -p 3000:3000   --add-host host.docker.internal:host-gateway   -e LOG_ALL_EVENTS=true   docker.all-hands.dev/all-hands-ai/openhands:0.39

# Truy cập: http://localhost:3000
# Nhập API key (Claude/OpenAI) → bắt đầu giao task
```

**Khuyến nghị model:** Claude Sonnet 4 (balance giữa capability và cost).

## Ví dụ thực tế
**Task thực tế:**
Prompt: *"Tạo một Python script crawl danh sách tour từ trang web X, lưu vào CSV, schedule chạy hàng ngày lúc 6 giờ sáng, gửi email báo cáo nếu có tour mới."*

OpenHands tự:
1. Research cấu trúc web X (browse)
2. Viết crawler với BeautifulSoup
3. Test chạy thử, fix lỗi
4. Thêm scheduling với cron
5. Thêm email notification với smtplib
6. Tạo README hướng dẫn

Mày review output và deploy.

## Lưu ý / Lỗi thường gặp
- Tốn token nhiều hơn coding tool thông thường — autonomous agent = nhiều LLM calls
- Sandbox bị giới hạn network trong môi trường Docker — cần config nếu cần internet access
- Kết quả phụ thuộc rất nhiều vào model — Claude Sonnet 4 cho kết quả tốt nhất hiện tại
- Review kỹ output trước khi deploy production — đặc biệt với security-sensitive code

## Đánh giá cá nhân
- Điểm mạnh: Autonomous thật sự; sandbox an toàn; mã nguồn mở; support nhiều LLM; community cực active
- Điểm yếu: Tốn token nhiều; đôi khi loop hoặc stuck; chưa ổn định 100% với task phức tạp
- Có nên dùng không: **8/10** — Dùng cho task độc lập, rõ ràng, không quá phức tạp. Thay Devin $500/tháng hoàn toàn được với task vừa phải.

## Link
- Repo: https://github.com/All-Hands-AI/OpenHands
- Docs: https://docs.all-hands.dev
- Website: https://www.all-hands.dev

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

OPENHANDS_URL = "http://localhost:3000"

def openhands_run_task(task, model="claude-3-5-sonnet-20241022", api_key=None):
    """Delegate coding task cho OpenHands agent"""
    payload = json.dumps({
        "task": task,
        "llm_config": {"model": model, "api_key": api_key}
    }).encode()
    req = urllib.request.Request(
        f"{OPENHANDS_URL}/api/conversations",
        data=payload, headers={"Content-Type": "application/json"}
    )
    r = json.loads(urllib.request.urlopen(req).read())
    return r["conversation_id"]

def openhands_get_result(conversation_id):
    req = urllib.request.Request(f"{OPENHANDS_URL}/api/conversations/{conversation_id}")
    return json.loads(urllib.request.urlopen(req).read())

# Hermes delegate coding tasks cho OpenHands, không cần tự code
```

### OpenClaw
```bash
# Docker UI — không cần npm
```

### Antigravity
```bash
docker run -d -p 3000:3000 \
  -e SANDBOX_USER_ID=$(id -u) \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/.openhands-state:/.openhands-state \
  --name openhands ghcr.io/all-hands-ai/openhands:main
```
> ⚠️ Hermes có thể delegate complex coding tasks cho OpenHands agent.
