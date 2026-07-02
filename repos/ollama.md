# Ollama — GitHub Repo

## TL;DR
Ollama là runtime chạy LLM local trên máy/VPS của mày bằng 1 lệnh duy nhất — không cần API, không tốn token, không lộ data ra ngoài. 172K+ stars, MIT license, đã trở thành chuẩn de facto cho local LLM.

## Repo này dùng để làm gì
Nói đơn giản: Ollama là "Docker cho LLM". Mày gõ `ollama run llama3.1` là nó tự tải model, tự setup context window, tự quản lý GPU/CPU, xong cho mày chat luôn. Nó expose ra 1 REST API OpenAI-compatible tại `localhost:11434` — nghĩa là bất cứ code nào đang gọi OpenAI API, chỉ cần đổi URL là chạy được với model local.

Dùng để làm gì trong bối cảnh của tao:
- **Backup khi OmniRoute/DeepSeek down** — vẫn có model chạy được, không phụ thuộc 100% vào API ngoài
- **Test prompt không tốn token** — dev/test pipeline Research Pro trên model local trước khi chạy thật qua DeepSeek
- **Data nhạy cảm** — nếu sau này xử lý data khách ABTRIP không muốn gửi ra ngoài, chạy local

## Setup từng bước
1. Cài trên VPS (Linux):
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```
2. Kiểm tra service (tự chạy dưới dạng systemd trên Linux):
```bash
systemctl status ollama
```
3. Tải và chạy model:
```bash
ollama run qwen2.5-coder:7b   # nhẹ, hợp VPS RAM vừa
```
4. Gọi qua REST API:
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "qwen2.5-coder:7b",
  "messages": [{"role": "user", "content": "tóm tắt file README này"}],
  "stream": false
}'
```
5. Muốn truy cập từ máy khác (ví dụ OpenClaw chạy container riêng gọi vào):
```bash
sudo systemctl edit ollama
# thêm: Environment="OLLAMA_HOST=0.0.0.0"
```

## Ví dụ thực tế
Hermes đang phụ thuộc hoàn toàn vào OmniRoute (231 provider free) để gọi LLM. Nếu OmniRoute rate-limit hoặc down đột ngột, task đang chạy (ví dụ research pipeline) bị đứng. Cài Ollama trên VPS Tencent Cloud, set fallback trong code Hermes: gọi OmniRoute trước, nếu lỗi/timeout thì fallback qua `localhost:11434` chạy model nhẹ như `qwen2.5-coder:7b` để task không bị treo hoàn toàn, dù chất lượng thấp hơn.

## Lưu ý / Lỗi thường gặp
- **`OLLAMA_HOST=0.0.0.0` không có firewall = ai trong network cũng gọi được model** — nhớ set firewall/reverse proxy nếu expose ra ngoài localhost.
- **VPS RAM phải đủ cho model chọn** — model 7B cần ~5-8GB RAM, VPS Tencent Cloud hiện đang tight RAM (đang chờ giải quyết Chatwoot) nên chỉ nên chạy model nhỏ (3B-7B), không chạy model to.
- **Không tối ưu cho nhiều user đồng thời** — quá 2-3 request cùng lúc là nghẽn, nếu cần serve nhiều request song song thì phải nhảy qua vLLM (đã note trong danh sách 16 repo, có thể làm tiếp).
- **GGUF only** — nếu sau này cần format GPTQ/AWQ thì Ollama không hỗ trợ, phải dùng llama.cpp trực tiếp.

## Đánh giá cá nhân
- **Điểm mạnh:** Setup nhanh nhất trong mọi lựa chọn self-host LLM hiện có, API OpenAI-compatible nên gần như không cần sửa code khi fallback. Đã có tích hợp chính thức với OpenClaw ("turn Ollama into a personal AI assistant qua WhatsApp/Telegram/Slack") — khớp thẳng vào stack Hermes/OpenClaw hiện tại.
- **Điểm yếu:** Chất lượng model local vẫn thua model cloud (DeepSeek R1/V3) cho task reasoning phức tạp — chỉ hợp làm fallback hoặc test, không thay được production. Multi-user/multi-GPU không phải điểm mạnh.
- **Có nên dùng không:** 8/10 — không phải để thay OmniRoute mà để làm lớp fallback an toàn, chi phí gần như 0 (chỉ tốn RAM VPS sẵn có).

## Link
- Repo: https://github.com/ollama/ollama
- Docs: https://ollama.com (chạy `curl https://ollama.com/docs`)
- Model library: https://ollama.com/library

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

def ollama_fallback(prompt, model="qwen2.5-coder:7b"):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }).encode()
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())["message"]["content"]

def call_llm_with_fallback(prompt):
    try:
        return call_omniroute(prompt)  # hàm gọi OmniRoute có sẵn
    except Exception:
        return ollama_fallback(prompt)  # fallback local khi OmniRoute lỗi
```

### OpenClaw
```bash
# OpenClaw có tích hợp chính thức với Ollama — biến model local thành
# personal assistant qua WhatsApp/Telegram/Slack/Discord
# Cấu hình trong OpenClaw: chọn Ollama làm 1 trong các model provider
npx openclaw config add-provider ollama --url http://localhost:11434
```

### Antigravity
```bash
# Cài trên VPS Tencent Cloud
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull qwen2.5-coder:7b
systemctl enable ollama  # tự start khi VPS reboot
```
> ⚠️ Chỉ pull model nhỏ (3B-7B) trên VPS hiện tại vì đang tight RAM — không pull model 20B+ trước khi mở rộng RAM hoặc có VPS riêng.
