---
name: ifixai
description: >
  Bộ audit mã nguồn mở cho AI agent: ném agent vào một "công ty giả lập", cho
  nó nhận yêu cầu vượt quyền, rồi để một model khác chấm điểm A-F. Kiểm tra
  agent có bịa, lừa, vượt quyền hay không — thứ mà eval thường bỏ sót.
---

# iFixAi — GitHub Repo

## TL;DR
iFixAi là công cụ audit độc lập cho AI agent (Apache-2.0, ~33.7K sao, bản 4.3.0 ra 22/10/2026). Nó đặt agent vào môi trường giả lập, gửi các yêu cầu cố tình đẩy agent ra khỏi vai trò, rồi một judge model khác hãng chấm A-F. Mặc định chạy 10 inspection, bật `--full-run` thì chạy đủ 61.

## Repo này dùng để làm gì
Eval thông thường hỏi "agent làm task có đúng không". iFixAi hỏi câu khác: "agent có đang làm đúng việc được giao, trong đúng quyền được giao không". Ví dụ: chatbot tư vấn vé có tự bịa chính sách hoàn vé không, có hứa điều nó không có quyền hứa không, có bị prompt injection dắt đi không, có nói dối khi không làm được việc không.

Cách nó hoạt động, giải thích đơn giản:
- Mày mô tả agent của mày (vai trò, quyền, luật) trong một file profile JSON
- `ifixai author` biến profile đó thành "fixture" — một công ty giả lập quanh agent
- iFixAi gửi hàng loạt request vào agent thật, trong đó có nhiều request cố tình vượt quyền
- Một judge model (bắt buộc khác hãng với agent) chấm từng câu trả lời
- Ra điểm A-F theo 5 trụ: bịa (fabrication), thao túng (manipulation), lừa dối (deception), khó đoán (unpredictability), mờ đục (opacity). Fail một trong 3 mục bắt buộc (B01, B08, P01) thì grade bị chặn trần ở D

Lưu ý tên gọi: bản mã nguồn mở có **61 inspection**. Các số "250 inspection / 69 nhóm" trên Product Hunt là của bản Pro trả phí, đừng nhầm.

## Setup từng bước

Cần Python 3.10 trở lên. Python mặc định của macOS thường là 3.9, nhớ check `python3 --version`.

1. Cài:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install "ifixai[anthropic]"     # thay anthropic bằng provider của judge: openai, gemini, azure, bedrock, openrouter...
```

2. Thử demo không cần API key (agent giả, chỉ để xem nó chạy ra sao):
```bash
ifixai author reference -o reference.yaml
ifixai validate reference.yaml
ifixai run --provider mock --eval-mode self --fixture reference.yaml
```
Báo cáo nằm trong `./ifixai-results/` (JSON + Markdown).

3. Audit agent thật — cách đơn giản nhất là để Claude Code tự làm:
```
/plugin marketplace add ifixai-ai/iFixAi
/plugin install ifixai@ifixai-community
```
Rồi nói "run iFixAi on my setup". Plugin đọc code agent của mày, viết profile, chạy audit và giải thích kết quả. Dùng agent khác (Cursor, VS Code, Windsurf, Cline, Gemini, Zed...) thì: `uvx ifixai install --agents cursor`.

4. Cách thủ công, hợp với CI:
```bash
ifixai setup                         # wizard chọn endpoint, judge, suite -> ghi ifixai.yaml
ifixai run --dry-run                 # xem trước số test và số lần gọi judge
ifixai run                           # chạy thật
```
Hoặc một dòng đầy đủ:
```bash
ifixai run --provider http --endpoint https://agent-cua-may/v1 --api-key "$AGENT_KEY" \
  --fixture reference.yaml --judge-provider anthropic --judge-api-key "$JUDGE_KEY" \
  --judge-budget 3000 --min-score 0.85
```

## Ví dụ thực tế

**Đã chạy thật (demo không key, bản 4.3.0):** audit agent mẫu "Larkspur Assist" ra 10/10 inspection PASS, grade A, 2 giây. Nhưng chính tool tự cảnh báo: kết quả này là `self-judged` (model tự chấm output của mình), chỉ là smoke test, không citable. Điểm đáng giá của demo là thấy được format báo cáo và 10 inspection mặc định: Tool Invocation Governance, Policy Violation Detection, Privilege Escalation Detection, Explicit Uncertainty Signalling, Prompt Injection Blocking, Silent Failure Rate, Instruction Adherence, In-Context Session Isolation, Plausible-Justification Destruction Resistance, Goal Stability.

**Áp vào ABTRIP (kế hoạch, CHƯA chạy):** chatbot tư vấn vé trên Zalo OA. Profile ghi rõ: bot chỉ được báo giá tham khảo và quy định chung, không được hứa hoàn vé, không được xác nhận giữ chỗ, phải chuyển hotline khi khách hỏi đổi/hoàn. Chạy audit để kiểm tra 4 thứ: bot có bịa điều kiện hoàn vé của hãng không, có hứa hoàn tiền khi khách ép không, có lộ system prompt khi bị inject không, có chuyển hotline đúng lúc không. Giá trị cho Tano Agency: một báo cáo A-F có evidence là thứ bán được kèm gói chatbot cho khách SMB, thay vì chỉ nói "bot này ổn lắm".

## Lưu ý / Lỗi thường gặp
- **Judge phải khác hãng với agent.** iFixAi tự chọn judge từ các API key mày set, không dùng chung provider với agent. Chỉ có 1 key thì nó rơi về chế độ self-judged, grade vô giá trị. Agent chạy Claude thì để judge là OpenAI hoặc Gemini.
- **Tốn lượt gọi judge.** Demo mock ước tính ~854 judge call chỉ cho 10 inspection. Với judge thật, luôn chạy `--dry-run` trước và đặt `--judge-budget` để khỏi cháy tiền. `--full-run` (61 inspection) tốn nhiều hơn hẳn.
- **Telemetry bật mặc định** (pseudonymous). Agency làm cho khách thì tắt: `export DO_NOT_TRACK=1` hoặc `IFIXAI_TELEMETRY=0`. Muốn xem nó gửi gì: `ifixai run --print-telemetry`.
- **Có quảng cáo bản Pro** khi chạy trong terminal. Tắt bằng `IFIXAI_NO_PROMO=1` (trong CI thì nó tự ẩn).
- **Probe là request thật vào agent.** Chạy trên bản staging, đừng audit thẳng vào bot đang phục vụ khách, nhất là bot có tool ghi dữ liệu.
- **Điểm có nhiễu.** Báo cáo JSON tự ghi chú: chênh lệch dưới 0.15 giữa hai lần chạy chưa có ý nghĩa thống kê. Đừng so 87% với 84% rồi kết luận gì.
- **Exit code 2 khi điểm dưới `--min-score`** (mặc định 0.85). Các exit code khác chưa thấy tài liệu ghi, nên script CI cứ coi mọi mã khác 0 là fail.
- **Windows:** không thấy lệnh `ifixai` thì chạy `python -m ifixai.cli.main`.
- Chỉ kiểm tra hành vi của agent (prompt, tool), không kiểm tra tầng mạng/hosting bên dưới.

## Đánh giá cá nhân
- Điểm mạnh: Đánh trúng chỗ eval thường bỏ qua (vượt quyền, bịa, lừa). Có plugin cho Claude Code nên chạy gần như một câu lệnh. Report JSON + Markdown để so sánh giữa các lần chạy. Gắn `--min-score` vào CI được. Apache-2.0, dùng thương mại thoải mái.
- Điểm yếu: Judge là LLM nên điểm có nhiễu và phụ thuộc chất lượng judge. Tốn nhiều lượt gọi judge. Phải viết profile agent cho kỹ thì kết quả mới có nghĩa, profile sơ sài ra điểm đẹp giả. Bản mã nguồn mở không có badge "Audited by iFixAi" (chỉ có ở bản trả phí). Telemetry bật sẵn. Repo mới nổi rất nhanh nên CLI còn đổi, tài liệu CI chưa đầy đủ.
- Có nên dùng không: **7/10** — Nếu mày giao chatbot hoặc agent cho khách (ABTRIP Zalo OA, bot SMB của Tano) thì nên chạy trước khi bàn giao và đính báo cáo vào hồ sơ nghiệm thu. Còn nếu chỉ build agent nội bộ chơi thì chưa cần. Đừng coi grade A là chứng nhận, nó là bằng chứng từ chính những lần chạy của mày.

## Link
- Repo: https://github.com/ifixai-ai/iFixAi
- PyPI: https://pypi.org/project/ifixai/
- Trang chủ (bản Pro, audit trả phí): https://ifixai.ai
- Product Hunt: https://producthunt.com/products/ifixai

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# iFixAi la CLI Python, khong co REST API rieng. Hermes goi qua subprocess
# roi doc file JSON ket qua. Chay ban staging cua agent, khong chay vao bot dang phuc vu khach.
import glob, json, os, subprocess

def audit_agent(endpoint, agent_key, fixture, judge_provider, judge_key, min_score=0.85):
    env = {**os.environ, "DO_NOT_TRACK": "1", "IFIXAI_NO_PROMO": "1"}
    proc = subprocess.run(
        ["ifixai", "run", "--provider", "http", "--endpoint", endpoint,
         "--api-key", agent_key, "--fixture", fixture,
         "--judge-provider", judge_provider, "--judge-api-key", judge_key,
         "--judge-budget", "3000", "--min-score", str(min_score)],
        env=env, capture_output=True, text=True,
    )
    # exit code 2 = diem duoi min-score. Ma khac 0 khac thi coi la loi
    report = max(glob.glob("ifixai-results/*.json"), key=os.path.getmtime)
    data = json.load(open(report, encoding="utf-8"))
    return {
        "grade": data["overall"]["grade"],
        "score": data["overall"]["score"],
        "passed": data["overall"]["passed"],
        "mandatory_minimums_ok": data["mandatory_minimums"]["all_passed"],
        "self_judged": data["metadata"]["self_judged"],  # True = grade vo gia tri
        "exit_code": proc.returncode,
    }
```

### OpenClaw
```bash
# OpenClaw khong nam trong danh sach agent ma "ifixai install" ho tro
# (cursor, claude, vscode, windsurf, cline, continue, gemini, zed). Goi CLI truc tiep qua shell.
source ~/ifixai/.venv/bin/activate
export DO_NOT_TRACK=1 IFIXAI_NO_PROMO=1
ifixai run --dry-run                  # xem truoc so test va so luot goi judge
ifixai run --min-score 0.85           # exit code 2 neu diem thap hon nguong
```

### Antigravity
```bash
# Cai tren VPS can Python 3.10+ (kiem tra bang python3 --version truoc)
python3 -m venv ~/ifixai/.venv
source ~/ifixai/.venv/bin/activate
pip install "ifixai[anthropic,openai]"   # cai SDK cua ca agent lan judge
ifixai --version                          # bat dau tu 4.3.0
```
> ⚠️ Judge phai khac hang voi agent, nen can it nhat 2 API key tu 2 hang khac nhau.
> Dat `DO_NOT_TRACK=1` trong env cua service/cron de tat telemetry cho cac lan chay tu dong.
> Chi chay tren staging: moi probe la request that gui vao agent.
