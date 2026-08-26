# Prime Agent — GitHub Repo

## TL;DR
Coding agent open-source của PrimeIntellect-ai, khác biệt ở chỗ nó tự cải thiện bản thân qua session — nhớ style code, quy tắc dự án, và sub-agent đã tạo, không "quên sạch" mỗi lần đóng terminal như hầu hết coding agent khác.

## Repo này dùng để làm gì
Prime Agent chạy trong 1 IPython kernel bền vững thay vì gọi hàng chục tool JSON rời rạc (grep, edit, bash...) — model viết Python code sống chạy trực tiếp trong console persistent. Context, data, biến số giữ nguyên qua các bước xử lý, không làm phình context window.

Điểm đặc biệt nhất là **Continual Harness**: agent lưu instruction, skill, và sub-agent definition ra đĩa như state bền vững. Chạy `/refine` là agent tự phân tích công việc đã làm, rút ra bài học, và cập nhật rule cho khớp coding style của mình — tức là agent "học" theo thời gian, không static từ lúc setup.

Có daemon chạy nền — đóng terminal, ngắt SSH, hay restart UI thì agent vẫn tiếp tục chạy task, reconnect lại session bất cứ lúc nào. Sub-agent (`rlm("subtask")`) giao tiếp trực tiếp với nhau (Agent-to-Agent), chạy song song, report ngược về kernel chính.

## Setup từng bước

1. Cài đặt (theo docs chính thức tại repo PrimeIntellect-ai/prime-agent)
2. Cấu hình provider (Opus, các model khác qua API key)
3. Khởi chạy interactive mode, dùng slash commands (`/goal`, `/heartbeat`, `/autonomous`, `/refine`)
4. Set goal bền vững bằng `/goal` — agent giữ mục tiêu này xuyên nhiều turn tới khi hoàn thành/pause/clear
5. Với task dài hạn: dùng `/autonomous` — chạy trong giới hạn turn/token/time đã set, có quality gate tự định nghĩa

## Ví dụ thực tế

Tình huống: refactor một module lớn trong `tano.agency` repo, cần agent tự quyết định thứ tự sửa file, chạy test giữa chừng, và tiếp tục làm dù mất kết nối SSH.

- Set `/goal`: "Refactor server/kho-client.ts theo kiến trúc mới, giữ cache 1h intact"
- Chạy `/autonomous` với budget token giới hạn
- Agent tự spawn sub-agent kiểm tra test suite song song với việc sửa code chính
- Ngắt SSH giữa chừng → reconnect sau → agent vẫn đang chạy, daemon giữ state
- Sau khi xong, `/refine` — agent tự ghi lại pattern coding vừa học được cho lần sau

## Lưu ý / Lỗi thường gặp

- IPython kernel chạy Python với quyền OS của worker process — **không phải sandbox bảo mật**. Review kỹ skill của bên thứ 3 trước khi chạy, đặc biệt với repo không tin cậy.
- Có nhiều repo trùng tên "prime-agent" trên GitHub (kể cả clone/fork không chính chủ) — chỉ dùng `PrimeIntellect-ai/prime-agent`, tránh nhầm với `ThePrimeagen/prime-agent` (repo cá nhân khác, không liên quan) hay `prime-RLM-agent/prime-agent` (có vẻ là mirror/rebrand).
- "Passed quality gate" chỉ verify đúng cái gate đó check — không có nghĩa task đã hoàn thành đúng ý, cần review lại output.

## Đánh giá cá nhân

- **Điểm mạnh:** Continual Harness là ý tưởng hay — agent thực sự "học" qua session thay vì static config. Daemon-backed continuity giải quyết đúng pain point của coding agent chạy dài (mất session khi disconnect).
- **Điểm yếu:** Còn khá mới, docs vẫn đang hoàn thiện. Không phải sandbox an toàn — rủi ro cao hơn nếu chạy code không kiểm soát. Cần Opus-tier model để phát huy hết khả năng (báo cáo 95.5% ARC-AGI-3 dùng Opus 5).
- **Có nên dùng không:** 7/10 — Hợp cho ai cần agent chạy task dài hạn tự chủ (giống hướng Hermes đang làm), nhưng cần tự đánh giá rủi ro sandbox trước khi cho chạy trên production.

## Link
- Repo: https://github.com/PrimeIntellect-ai/prime-agent
- Docs: https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/index.md
- Blog giới thiệu: https://www.primeintellect.ai/blog/prime-agent

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Prime Agent chạy như 1 process riêng, Hermes có thể gọi qua subprocess
# hoặc dùng daemon socket nếu cần điều khiển từ xa (xem docs RPC mode)
import subprocess

def run_prime_agent_task(goal: str, workdir: str):
    """Gọi Prime Agent chạy 1 goal cụ thể trong thư mục chỉ định."""
    result = subprocess.run(
        ["prime-agent", "run", "--goal", goal, "--workdir", workdir],
        capture_output=True, text=True, timeout=3600
    )
    return result.stdout, result.stderr
```

### OpenClaw
```bash
# Nếu cần tích hợp làm sub-orchestrator cho task coding dài hạn
npx prime-agent --version  # kiểm tra cài đặt trước
```

### Antigravity
```bash
# Deploy Prime Agent daemon trên VPS nếu muốn chạy 24/7 độc lập với Hermes
# Xem "Long-running and background agents" trong docs chính thức trước khi setup
```
> ⚠️ Kernel không phải sandbox — nếu deploy trên VPS chung với Hermes/OpenClaw, cân nhắc isolate bằng container riêng để tránh rủi ro chéo.
