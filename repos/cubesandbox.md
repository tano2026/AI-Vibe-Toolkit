---
name: cubesandbox
description: >
  CubeSandbox (TencentCloud) là sandbox siêu nhẹ, siêu nhanh (khởi động
  <60ms, chỉ tốn <5MB RAM/instance) để agent chạy code do AI sinh ra một cách
  an toàn — mỗi agent có kernel riêng, không share kernel như Docker nên
  không lo container escape. Đã chạy production thật ở Tencent Cloud trước
  khi mở nguồn, tương thích ngược với E2B SDK.
---

# CubeSandbox — GitHub Repo

## TL;DR
CubeSandbox (TencentCloud) là sandbox siêu nhẹ, siêu nhanh (khởi động <60ms, chỉ tốn <5MB RAM/instance) để agent chạy code do AI sinh ra một cách an toàn — mỗi agent có kernel riêng, không share kernel như Docker nên không lo container escape. Đã chạy production thật ở Tencent Cloud trước khi mở nguồn, tương thích ngược với E2B SDK.

## Repo này dùng để làm gì
Vấn đề: Hermes đang chạy code Python trực tiếp trong OpenClaw runtime — nếu code do AI sinh ra (từ task tự động) có lỗi hoặc bug lạ, nó chạy chung môi trường với mọi thứ khác, rủi ro cao. CubeSandbox tạo ra 1 "hộp" riêng biệt (MicroVM, không phải container Docker thường) cho mỗi lần chạy code, xong thì hủy — mỗi hộp có kernel OS riêng thật sự, không chỉ namespace giả lập như Docker.

Điểm đặc biệt: **tương thích 100% với E2B SDK** — nghĩa là nếu code nào đang gọi E2B Cloud (dịch vụ sandbox trả phí phổ biến cho AI agent), chỉ cần đổi 1 biến môi trường (`E2B_API_URL`) là chuyển sang CubeSandbox tự host, miễn phí, không sửa code.

3 lớp kiến trúc chính:
- **CubeAPI** — cổng REST API tương thích E2B
- **CubeMaster** — điều phối, nhận request rồi giao cho node phù hợp
- **Cubelet + CubeHypervisor** — quản lý lifecycle từng sandbox trên 1 node, dùng KVM MicroVM thật

## Setup từng bước
1. Yêu cầu: Linux x86_64 có hỗ trợ KVM (kiểm tra trước — nhiều VPS share host tắt nested virtualization, cần bare-metal hoặc VPS có KVM passthrough)
```bash
lsmod | grep kvm   # kiểm tra KVM có sẵn chưa
```
2. Cài one-click:
```bash
curl -sL https://github.com/tencentcloud/CubeSandbox/raw/master/deploy/one-click/online-install.sh | bash
```
3. Tạo template từ image có sẵn:
```bash
cubemastercli tpl create-from-image \
  --image cube-sandbox-int.tencentcloudcr.com/cube-sandbox/sandbox-code:latest \
  --expose-port 49999 --probe 49999
```
4. Set biến môi trường để SDK trỏ vào CubeSandbox thay vì E2B Cloud:
```bash
export E2B_API_URL="http://<vps-ip>:<port>"
export E2B_API_KEY="bất-kỳ-giá-trị"  # không check nếu tự host
```

## Ví dụ thực tế
Hermes cần chạy code Python do OmniRoute/DeepSeek sinh ra để xử lý task tự động (ví dụ: tự viết script tính giá tour ABTRIP theo công thức phức tạp). Nếu code có bug vô hạn loop hoặc side-effect lạ, chạy trực tiếp trên VPS sẽ ảnh hưởng cả OpenClaw. Deploy CubeSandbox trên VPS, đổi endpoint E2B trong Hermes, mỗi lần chạy code là 1 sandbox mới tạo trong <60ms, chạy xong huỷ, không đụng gì tới hệ thống chính.

## Lưu ý / Lỗi thường gặp
- **Cần KVM support** — đây là điều kiện chặn nhiều nhất. VPS Tencent Cloud hiện tại (CentOS/RHEL) cần kiểm tra kỹ có hỗ trợ nested virtualization/KVM hay không trước khi thử deploy, nếu không có sẽ không chạy được (khác PVM mode — có support riêng cho non-KVM nhưng phức tạp hơn).
- **Image sandbox khá nặng** — README cảnh báo "the image is large", tải + build template lần đầu tốn thời gian, cần kiên nhẫn.
- **Registry khác nhau theo vùng** — dùng `cube-sandbox-int.tencentcloudcr.com` (quốc tế) hoặc `cube-sandbox-cn.tencentcloudcr.com` (nếu server đặt tại Trung Quốc đại lục) — chọn sai registry sẽ chậm hoặc lỗi pull image.
- **AgentHub feature có sẵn tích hợp OpenClaw** — "Spin up OpenClaw assistants in one click" là tính năng dựng sẵn, không cần tự viết integration.

## Đánh giá cá nhân
- **Điểm mạnh:** Đã chạy production thật ở Tencent Cloud (không phải demo), an toàn thật (kernel riêng, không chỉ giả lập), tương thích E2B nên nếu sau này có code dùng E2B SDK sẵn thì chuyển qua gần như miễn phí công sức. Docs có sẵn ví dụ wire với OpenAI Agents SDK, SWE-bench.
- **Điểm yếu:** Rào cản kỹ thuật đầu vào (cần KVM, Linux x86_64, không chạy được trên mọi VPS) cao hơn hẳn Docker thường. Setup one-click nhưng debug khi lỗi (kernel PVM, network CubeVS) đòi hiểu sâu về virtualization, không phải "cắm là chạy" như Ollama.
- **Có nên dùng không:** 7/10 — rất đáng nếu VPS Tencent Cloud hiện tại support KVM (khả năng cao vì cùng nhà Tencent), giải quyết đúng bài toán "chạy code AI sinh ra an toàn" cho Hermes. Nhưng nên test KVM support trước khi cam kết deploy, tránh mất công như một số trường hợp thiếu RAM trước đây.

## Link
- Repo: https://github.com/TencentCloud/CubeSandbox
- Docs: https://github.com/TencentCloud/CubeSandbox/blob/master/docs/index.md
- Quick Start: https://github.com/TencentCloud/CubeSandbox/blob/master/docs/guide/quickstart.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request, json

CUBE_URL = "http://<vps-ip>:<port>"

def run_code_in_sandbox(code: str):
    # Tương thích E2B SDK — nếu có sẵn e2b-code-interpreter, chỉ cần set
    # E2B_API_URL trước khi import, không cần code riêng cho CubeSandbox
    payload = json.dumps({"code": code}).encode()
    req = urllib.request.Request(
        f"{CUBE_URL}/execute",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    return json.loads(urllib.request.urlopen(req).read())

result = run_code_in_sandbox("print('tính giá tour ABTRIP')")
```

### OpenClaw
```bash
# CubeSandbox có tính năng AgentHub — spin up OpenClaw assistant 1 click
# Cấu hình theo docs/guide/tutorials/examples.md — mục OpenClaw skill
```

### Antigravity
```bash
# Kiểm tra KVM trước, sau đó one-click install
lsmod | grep kvm
curl -sL https://github.com/tencentcloud/CubeSandbox/raw/master/deploy/one-click/online-install.sh | bash
```
> ⚠️ BẮT BUỘC kiểm tra `lsmod | grep kvm` trước khi deploy — nếu VPS không hỗ trợ KVM (nhiều VPS share-host tắt tính năng này), toàn bộ setup sẽ fail. Hỏi Tencent Cloud support xem instance hiện tại có bật KVM/nested virtualization chưa trước khi thử.
