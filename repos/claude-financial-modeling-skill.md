# Financial Modeling Suite (anthropics/claude-cookbooks) — GitHub Repo

## TL;DR
Skill tài chính CHÍNH THỨC của Anthropic — dạy Claude làm DCF valuation, sensitivity analysis, Monte Carlo simulation, scenario planning đúng chuẩn ngành tài chính, xuất ra file Excel công thức sống (không phải số cứng). Nằm trong repo `claude-cookbooks` (37.6K stars), path `skills/custom_skills/creating-financial-models`.

## Repo này dùng để làm gì
Đây là "tư duy CFO" đóng gói thành skill — 4 năng lực lõi:
1. **DCF (Discounted Cash Flow)** — build model định giá đầy đủ, nhiều kịch bản tăng trưởng, tính terminal value (cả 2 cách: perpetuity growth và exit multiple), tự tính WACC, ra enterprise value → equity value.
2. **Sensitivity Analysis** — test biến nào ảnh hưởng định giá nhiều nhất (vd WACC vs terminal growth), ra bảng data table + tornado chart xếp hạng biến quan trọng.
3. **Monte Carlo Simulation** — chạy hàng nghìn kịch bản với phân phối xác suất, ra khoảng tin cậy cho định giá, tính xác suất đạt mục tiêu.
4. **Scenario Planning** — dựng nhiều kịch bản (best/base/worst) có trọng số xác suất cho quyết định đầu tư/mở rộng.

Điểm khác biệt với việc tự hỏi Claude làm Excel tay: skill này ép mọi ô là **công thức sống** (không hardcode số), verify từng phần với người dùng trước khi làm tiếp, và cố tình dùng số chiều lẻ cho sensitivity table để ô trung tâm luôn là base case — tránh kiểu Excel "nhìn đẹp nhưng số chết".

## Setup từng bước
1. Clone repo (chỉ cần đúng path này, không cần cả repo nếu muốn tối giản):
```bash
git clone https://github.com/anthropics/claude-cookbooks.git
ln -s ~/claude-cookbooks/skills/custom_skills/creating-financial-models ~/.claude/skills/
```
2. Trigger tự động khi hỏi kiểu "Build a DCF model for..." hoặc ép dùng thẳng: thêm câu *"please use DCF skill"* vào cuối prompt để chắc chắn Claude kích hoạt.
3. Cần input tối thiểu: doanh thu lịch sử, biên EBITDA, capex, working capital, tỷ lệ tăng trưởng dự phóng, WACC giả định, thuế suất, nợ ròng, số cổ phần (nếu định giá công ty cổ phần) — hoặc tương đương cho case không phải công ty cổ phần (freelance/agency thì thay bằng doanh thu domain, chi phí biến đổi, chi phí cố định).

## Ví dụ thực tế
Áp cho quyết định thực tế của Tano Agency: đang cân nhắc có nên đầu tư mở rộng Tano Cafe (mua thêm thiết bị, thuê thêm 1 người) hay dồn vốn vào phát triển YouTube "Airfare Decoded". Thay vì đoán mò, đưa Claude data 2 domain (doanh thu, chi phí hiện tại, dự phóng tăng trưởng kỳ vọng) → yêu cầu scenario planning 3 kịch bản (best/base/worst) cho mỗi domain, kèm sensitivity xem biến nào (giá vé máy bay/traffic YouTube vs lượng khách Cafe) ảnh hưởng lớn nhất tới kết quả — ra quyết định có số liệu chống lưng thay vì cảm tính.

## Lưu ý / Lỗi thường gặp
- Model phức tạp (DCF full + sensitivity) có thể mất 1-2 phút để Claude sinh xong — không phải lỗi, là do độ phức tạp thật.
- Skill được thiết kế cho công ty/dự án có dòng tiền dự đoán được — với agency nhỏ/freelance doanh thu bất định, cần điều chỉnh input cho hợp lý (không nên áp máy móc WACC kiểu công ty niêm yết).
- Đây là skill xử lý số liệu tài chính — theo khuyến cáo bảo mật, nên cân nhắc tách riêng session/profile khi làm việc với data tài chính thật nhạy cảm, không trộn chung với các task khác.
- Không thay thế được tư vấn tài chính/kế toán chuyên nghiệp cho quyết định lớn (vay vốn, gọi đầu tư) — dùng để có góc nhìn số liệu trước, không phải quyết định cuối.

## Đánh giá cá nhân
- Điểm mạnh: chính thức từ Anthropic nên độ tin cậy phương pháp luận cao (đúng chuẩn ngành: DCF, WACC, Monte Carlo không phải hàng tự chế); xuất Excel công thức sống dùng lại được, không phải bảng chết; miễn phí, chỉ cần clone.
- Điểm yếu: thiết kế gốc cho định giá công ty/dự án đầu tư kiểu truyền thống — cần "dịch" input cho phù hợp mô hình agency nhỏ nhiều domain như Tano; không có sẵn context Việt Nam (thuế, lãi suất tham chiếu) nên vẫn phải tự điền đúng số.
- Có nên dùng không: 8/10 — nên tích hợp vào role Ops & Finance Agent để nâng từ "ghi sổ thu chi" lên "tư duy quyết định đầu tư/mở rộng có số liệu", đúng thứ đang thiếu trong role pack hiện tại.

## Link
- Repo: https://github.com/anthropics/claude-cookbooks
- Skill path: https://github.com/anthropics/claude-cookbooks/tree/main/skills/custom_skills/creating-financial-models

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Skill là file .md + .py (dcf_model.py, sensitivity_analysis.py) — không phải REST API.
# Hermes dùng gián tiếp: fetch nội dung SKILL.md làm system prompt cho call_llm()
def fetch_financial_modeling_skill():
    url = ("https://raw.githubusercontent.com/anthropics/claude-cookbooks/"
           "main/skills/custom_skills/creating-financial-models/SKILL.md")
    return http_get(url)

def run_dcf_analysis(financial_data_summary):
    system = fetch_financial_modeling_skill()
    return call_llm(financial_data_summary, task_type="reasoning",
                    system=system, max_tokens=4000)
```

### OpenClaw
```bash
# Cài trực tiếp vào project trước khi giao task định giá/scenario planning cho Claude Code
git clone https://github.com/anthropics/claude-cookbooks.git /tmp/cookbooks
cp -r /tmp/cookbooks/skills/custom_skills/creating-financial-models ~/.claude/skills/
```

### Antigravity
```bash
# Không cần deploy service — chỉ cần đảm bảo skill có mặt nếu Ops&Finance Agent
# chạy trên VPS cũng cần dựng model
mkdir -p /opt/skills && git clone https://github.com/anthropics/claude-cookbooks.git /opt/skills/claude-cookbooks
```
> ⚠️ Data tài chính thật (doanh thu, chi phí từng domain) không nên trộn chung session với task khác — tách riêng để tránh rò rỉ số liệu nhạy cảm vào context không liên quan.
