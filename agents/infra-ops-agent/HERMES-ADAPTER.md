# HERMES-ADAPTER.md — Infra Ops Agent

> Khác Research Pro/Content Pro (Hermes tự thực thi việc thật), Infra Ops
> Agent trên Hermes CHỈ được dùng để **đọc/báo cáo/phân tích** — tuyệt đối
> không tự chạy lệnh thay đổi hệ thống. Đây là ranh giới cứng, không phải
> tuỳ chọn.

## Việc Hermes ĐƯỢC làm cho Infra Ops Agent

```python
import urllib.request, json, os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "tano2026/AI-Vibe-Toolkit"

def github(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def fetch_doc(path):
    import base64
    data = github(f"repos/{REPO}/contents/{path}")
    return base64.b64decode(data['content']).decode()

# Ví dụ: đọc destructive-command-guardrail trước khi soạn plan
guardrail = fetch_doc("agents/infra-ops-agent/skills/destructive-command-guardrail/SKILL.md")
```

**Việc đọc-only hợp lệ trên Hermes:**
- Đọc log/metric hệ thống (nếu Hermes có quyền đọc file log trên chính máy nó chạy)
- Đọc kho (playbook, skill) để tra quy trình
- Phân tích dữ liệu cost/capacity đã có sẵn (không tự pull thêm từ Tencent Cloud API nếu chưa được cấp quyền rõ ràng)
- Soạn plan/script dạng TEXT để người/Antigravity đọc và tự quyết định chạy

## Việc Hermes TUYỆT ĐỐI KHÔNG được làm

```
❌ Tự chạy bất kỳ lệnh nào trong danh sách destructive-command-guardrail
❌ Tự SSH vào VPS khác (Hermes chạy trên chính máy nó, không leo qua máy khác)
❌ Tự sửa file config production
❌ Tự restart/stop service đang chạy
❌ Đưa ra plan rồi TỰ THỰC THI LUÔN không đợi confirm — luôn dừng ở bước
   "đây là plan, cần Antigravity/Nobitano xác nhận trước khi chạy"
```

## Luật no-fabrication áp dụng nghiêm ngặt hơn cho Infra Ops trên Hermes

Đúng tinh thần `dev-automation-discipline` — với Infra Ops đặc biệt nghiêm
trọng hơn vì output của nó (plan/script) có thể dẫn tới hành động thật gây
hại nếu Hermes tự tin báo sai trạng thái hệ thống:

```python
def report_system_state(claim, evidence_command=None, evidence_output=None):
    """
    Bắt buộc đi kèm bằng chứng khi báo cáo trạng thái hệ thống — không có
    evidence_command/evidence_output = KHÔNG được đưa claim này vào output
    cuối cùng gửi Nobitano/Antigravity.
    """
    if not evidence_command or not evidence_output:
        return {
            "status": "UNVERIFIED",
            "claim": claim,
            "warning": "⚠️ Claim này CHƯA có bằng chứng lệnh/API cụ thể — "
                       "không được trình bày như fact, cần chạy lệnh xác "
                       "nhận trước."
        }
    return {"status": "VERIFIED", "claim": claim, "evidence": evidence_output}
```

## Cách dùng thật trên Hermes

```python
# Khi Nobitano hỏi "VPS đang tốn bao nhiêu chi phí" qua Telegram:
# 1. Hermes đọc skill tencent-vps-capacity-cost để biết cách tính
capacity_skill = fetch_doc("agents/infra-ops-agent/skills/tencent-vps-capacity-cost/SKILL.md")
# 2. Hermes CHỈ báo cáo dựa trên data đã có sẵn (report cũ, log đã lưu) —
#    KHÔNG tự gọi Tencent Cloud API mới nếu chưa được cấp quyền rõ ràng
# 3. Nếu không đủ data → báo "chưa đủ data để tính chính xác, cần
#    Antigravity chạy lệnh X để lấy số liệu thật" — không suy đoán con số
```

## Vì sao Adapter này khác hẳn Research Pro/Content Pro

| | Research Pro/Content Pro trên Hermes | Infra Ops Agent trên Hermes |
|---|---|---|
| Mức tự chủ | Tự thực thi việc thật (research, viết content) | CHỈ đọc/phân tích/soạn plan |
| Rủi ro sai | Sai insight, sửa được | Sai lệnh có thể sập hệ thống thật, khó hoàn tác |
| Ai chạy hành động cuối | Chính Hermes | Antigravity (con người/agent khác), không phải Hermes |
