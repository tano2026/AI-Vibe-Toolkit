# financial-unit-economics + household-cfo (lyndonkl/claude) — GitHub Repo

## TL;DR
Bộ skill "CFO cá nhân/công ty nhỏ" — phân tích CAC, LTV, contribution margin, cohort payback, cộng thêm pipeline đọc sao kê ngân hàng/thẻ tự động phân loại giao dịch, đối soát sổ sách, phát hiện chi phí định kỳ. Đúng dạng "tư duy tài chính" cho công ty 1 người quản nhiều domain cùng lúc.

## Repo này dùng để làm gì
Repo cá nhân `lyndonkl/claude` gom nhiều skill, trong đó cụm liên quan tài chính đáng chú ý nhất:
- **`financial-unit-economics`** — phân tích CAC (chi phí có 1 khách), LTV (giá trị vòng đời khách), contribution margin, cohort payback period. Đây chính là "tư duy tài chính chiến lược" — trả lời câu "domain nào đang thực sự có lãi, domain nào chỉ trông có doanh thu nhưng CAC ăn hết margin".
- **`household-cfo` agent + 8 specialist skill** — pipeline xử lý sao kê PDF tự động, gồm:
  - `pdf-statement-parser` — parse sao kê ngân hàng/brokerage/thẻ ra JSON chuẩn kèm độ tin cậy
  - `transaction-categorizer` — phân loại giao dịch (rule trước, LLM sau khi rule không match) + học rule mới theo tên merchant
  - `transaction-deduplicator` — chống trùng giao dịch khi import nhiều lần
  - `recurring-charge-detector` — tự phát hiện chi phí định kỳ (subscription, thuê bao...), gắn cờ khi có khoản im lặng lâu (dormant)
  - `statement-reconciler` — đối soát số dư đầu kỳ + tổng phát sinh = số dư cuối kỳ, tự tìm chỗ lệch dấu/thiếu dòng/đếm trùng

Có kèm 1 orchestration runtime riêng (inbox nhận file → archive → lưu JSON chuẩn → dashboard HTML tĩnh cập nhật hàng tuần) — đúng mô hình tự động hóa sổ sách cho 1 người quản nhiều tài khoản/domain.

## Setup từng bước
1. Clone repo, các skill nằm độc lập theo thư mục:
```bash
git clone https://github.com/lyndonkl/claude.git
```
2. Copy skill cần dùng vào `.claude/skills/`, vd:
```bash
cp -r claude/skills/financial-unit-economics ~/.claude/skills/
cp -r claude/skills/household-cfo ~/.claude/skills/
```
3. Với pipeline sao kê PDF: cần copy thêm 4 skill phụ trợ (`pdf-statement-parser`, `transaction-categorizer`, `transaction-deduplicator`, `recurring-charge-detector`, `statement-reconciler`) vì chúng chạy nối tiếp nhau trong 1 pipeline, thiếu skill nào thì bước đó phải làm tay.
4. Không có MCP/API cần cấu hình — mọi thứ chạy qua Claude Code đọc file local (PDF sao kê, JSON lưu trữ).

## Ví dụ thực tế
Áp cho đúng vấn đề Tano Agency đang cần: mỗi tháng có giao dịch rải rác qua nhiều domain (ABTRIP, Tano Cafe, Wonder Mart, chi phí VPS/API cho hệ agent). Dùng `financial-unit-economics` để tính: domain Fast Track có CAC bao nhiêu (chi quảng cáo/booking mới), LTV 1 khách lặp lại dùng Fast Track nhiều lần là bao nhiêu, contribution margin sau khi trừ chi phí trực tiếp — so sánh với Tano Cafe xem domain nào đang gánh domain nào. Kết hợp `recurring-charge-detector` để tự động soi ra các API subscription (OmniRoute, Fal.ai, Minimax...) đang chi định kỳ có domain nào không dùng nữa mà vẫn trả tiền hay không.

## Lưu ý / Lỗi thường gặp
- Đây là repo cá nhân (không phải tổ chức lớn như Anthropic), 1 người maintain — độ ổn định/support lâu dài không chắc chắn bằng skill chính thức, nên review kỹ trước khi tin tưởng số liệu output 100%.
- Pipeline sao kê PDF thiết kế gốc cho tài chính cá nhân/hộ gia đình Mỹ (bank/brokerage/401k/HSA/mortgage) — cần chỉnh sửa category mapping cho phù hợp ngữ cảnh Việt Nam (không có 401k/HSA, cần thêm mục thuế GTGT, BHXH...).
- `transaction-categorizer` học rule theo thời gian — batch đầu tiên cần review tay kỹ hơn, càng dùng lâu càng chính xác.
- Data tài chính (sao kê ngân hàng, số dư) là thông tin nhạy cảm nhất — tuyệt đối không để lộ trong log/Mem0 public, đúng nguyên tắc guardrail đã có trong HERMES-PLAYBOOK.

## Đánh giá cá nhân
- Điểm mạnh: đúng bài toán "1 người quản tài chính nhiều domain cùng lúc" — chính là mô hình Tano Agency đang vận hành; `financial-unit-economics` cho tư duy chiến lược (lãi/lỗ thật theo domain) chứ không chỉ ghi sổ; pipeline sao kê tự động hóa được phần tốn thời gian nhất (nhập liệu + đối soát).
- Điểm yếu: repo cá nhân, cần tự chỉnh category cho ngữ cảnh VN; thiếu tầng bảo mật/audit chính thức như skill enterprise; phải ghép nhiều skill phụ trợ mới chạy trọn pipeline, không phải cắm 1 phát dùng ngay như financial-modeling-skill của Anthropic.
- Có nên dùng không: 7.5/10 — hợp để nâng cấp role Ops & Finance Agent từ "ghi sổ thu chi thủ công theo domain" (hiện tại) lên "tự động phân loại + tính unit economics từng domain" — đúng khoảng trống trong `agents/company/roles/ops-finance.md`.

## Link
- Repo: https://github.com/lyndonkl/claude

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Skill là file .md, dùng như system prompt — Hermes fetch trực tiếp từ GitHub raw
def fetch_unit_economics_skill():
    url = "https://raw.githubusercontent.com/lyndonkl/claude/main/skills/financial-unit-economics/SKILL.md"
    return http_get(url)

def analyze_domain_unit_economics(domain_data_summary):
    """domain_data_summary: doanh thu, chi phí trực tiếp, chi CAC, số khách lặp lại theo domain"""
    system = fetch_unit_economics_skill()
    return call_llm(domain_data_summary, task_type="reasoning",
                    system=system, max_tokens=3000)
```

### OpenClaw
```bash
# Cài cả cụm skill sao kê + unit economics vào project
git clone https://github.com/lyndonkl/claude.git /tmp/lyndonkl-claude
for s in financial-unit-economics household-cfo pdf-statement-parser \
         transaction-categorizer transaction-deduplicator \
         recurring-charge-detector statement-reconciler; do
  cp -r /tmp/lyndonkl-claude/skills/$s ~/.claude/skills/ 2>/dev/null
done
```

### Antigravity
```bash
# Không cần deploy service riêng — chỉ đảm bảo skill có mặt nếu Ops & Finance Agent
# chạy trên VPS cần tự động hóa sao kê định kỳ
mkdir -p /opt/skills && git clone https://github.com/lyndonkl/claude.git /opt/skills/lyndonkl-claude
```
> ⚠️ Data sao kê ngân hàng/số dư là thông tin nhạy cảm nhất trong toàn hệ thống — không log ra Telegram/Mem0 public, chỉ lưu trong storage riêng đã được CEO (Nobitano) duyệt.
