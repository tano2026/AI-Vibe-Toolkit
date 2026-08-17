# DeepSeek Harness — GitHub Repo

## TL;DR
Đối thủ mã nguồn mở của Claude Code, do chính DeepSeek AI làm — ra mắt developer preview 13/8/2026, cùng ngày với DeepSeek-V4-Pro GA. Triết lý "mọi thứ đều là plugin" — model, tool, session, sandbox, cả UI đều thay được. MIT license.

## Repo này dùng để làm gì
DeepSeek lập hẳn 1 team riêng từ tháng 3/2026 với mục tiêu nội bộ ghi rõ: "đối chuẩn Claude Code, làm DeepSeek Code Harness". Câu slogan họ dùng: "Model + Harness = Agent" — có model mạnh chưa đủ, thứ còn thiếu là lớp trung gian giữa model và hành động thật (quản lý context, gọi tool, xác minh, workflow). Kiến trúc dựng trên hệ dependency-injection nội bộ tên **Cordis**, cho phép thay từng lớp riêng lẻ: inference, tool registry, session state, agent control loop, execution sandbox, kể cả web UI — không phải 1 pipeline cố định như hầu hết agent framework khác.

Điểm khác biệt lớn nhất: **không giới hạn chạy model DeepSeek** — theo MindStudio, harness còn gọi được cả Claude Code hoặc Codex làm sub-agent bên trong. Đây là điểm nhiều nguồn nhấn mạnh là khác hẳn LangChain-style wrapper thông thường.

## Setup từng bước
1. Cài Node.js
2. Chạy nhanh không cần clone:
```bash
npx @deepseek-ai/dsh web
```
Web UI tự mở ở `http://127.0.0.1:3080`

3. Hoặc clone full để dev/tuỳ biến:
```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```
4. Cài thêm plugin bên ngoài:
```bash
dsh plugin --profile <tên-profile> add <package-hoặc-git-spec>
```
5. Cần DeepSeek API key để chạy các demo Web/headless/ACP automation và test e2e thật

## Ví dụ thực tế
Test thực tế từ MindStudio: dựng 1 tracker theo dõi vị trí trạm ISS real-time, harness tiêu tốn ~20 triệu token qua 2 turn, mất khoảng 35 phút, cache hit rate đạt 100% ở cuối run — cho thấy cơ chế cache của Cordis hoạt động hiệu quả cho task nhiều bước lặp lại. Với Tano Agency: đáng thử làm backend cho Automation & Ops Lead vì đã có OmniRoute route sẵn DeepSeek models, kết hợp harness này có thể thay thế 1 phần vai trò OpenClaw cho các task thuần code — nhưng nhớ đây mới developer preview, đừng thay hẳn OpenClaw production ngay.

## Lưu ý / Lỗi thường gặp
- Đang ở bản `0.1.0-rc.5`, chính README cảnh báo rõ: "THERE WILL BE COMPATIBILITY-BREAKING CHANGES" — đổi API bất cứ lúc nào, không hợp gắn cứng vào production
- DeepSeek-V4-Pro (model đi kèm harness) đổi cơ chế giá **peak/off-peak** — theo AIToolsReview, đây thực chất là tăng giá so với mức giá phẳng cũ dù được truyền thông là cải tiến
- Chỉ `deepseek-v4-flash` hỗ trợ tích hợp Codex hiện tại (qua Responses API), các model khác chưa
- Cộng đồng plugin phát triển rất nhanh (`awesome-deepseek-harness` đã liệt kê hàng chục plugin: remote SSH, browser panel, desktop companion...) — nhưng plugin bên thứ 3 chưa được DeepSeek chính thức kiểm định, cân nhắc trước khi cài plugin lạ vào máy có dữ liệu nhạy cảm

## Đánh giá cá nhân
- Điểm mạnh: MIT license thật sự mở, kiến trúc plugin triệt để hiếm thấy (thay được cả sandbox/UI, không riêng gì tool), khả năng gọi chéo Claude Code/Codex làm sub-agent là ý tưởng thú vị không phải harness nào cũng làm được, hệ sinh thái plugin cộng đồng phát triển cực nhanh trong vài ngày đầu
- Điểm yếu: mới developer preview, breaking changes liên tục, tài liệu phần lớn hướng dev nội bộ (nhiều thuật ngữ riêng như Cordis, "Host/Client aggregates") — đường học khá dốc so với Claude Code; giá model đi kèm (V4-Pro) đổi cấu trúc theo giờ cao điểm, cần tính toán lại chi phí thật kỹ trước khi rely vào
- Có nên dùng không: 6/10 cho production ngay bây giờ — đáng theo dõi sát và thử nghiệm nhỏ, nhưng đợi qua giai đoạn breaking-changes rồi mới cân nhắc thay OpenClaw/Claude Code cho việc quan trọng

## Link
- Repo: https://github.com/deepseek-ai/deepseek-harness
- Docs/Demo: https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/development.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# DeepSeek Harness expose theo JSON-RPC qua stdio (không phải REST đơn giản).
# Có SDK Python chính thức tương tự SDK TypeScript -- nhưng Hermes chỉ dùng
# urllib.request thuần (no pip install), nên KHÔNG cài SDK trực tiếp được.
# Cách khả thi: gọi qua subprocess tới dsh CLI đã cài sẵn trên máy, giao tiếp
# qua JSON-RPC newline-delimited.
import subprocess, json

def dsh_run_turn(prompt, profile="headless"):
    proc = subprocess.Popen(
        ["dsh", "--profile", profile],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    request = json.dumps({"jsonrpc": "2.0", "method": "turn", "params": {"prompt": prompt}, "id": 1})
    out, _ = proc.communicate(input=request + "\n", timeout=120)
    return out
```
> ⚠️ Đây mới là bản phác thảo dựa trên tài liệu công khai — chưa verify thật trên máy Hermes. Test kỹ trước khi gắn vào pipeline thật, vì API còn đang breaking changes liên tục (`0.1.0-rc.5`).

### OpenClaw
```bash
# Chạy Web UI làm dịch vụ nền, để OpenClaw gọi qua HTTP tới localhost:3080
npx @deepseek-ai/dsh web &
```
Có thể dùng PM2 quản lý tiến trình này song song OpenClaw hiện tại, thử nghiệm route 1 phần task code-heavy sang DeepSeek Harness trước khi quyết định thay thế.

### Antigravity
```bash
# Deploy trên VPS để share cho team
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install && pnpm run build
pnpm dsh web --port 3080
```
> ⚠️ Set `DSH_TOOLS_MODE` đúng (native/code/both) theo nhu cầu, và đảm bảo DeepSeek API key không lộ plaintext trong config — theo đúng nguyên tắc bảo mật đã áp cho các agent khác trong TANO AGENCY.
