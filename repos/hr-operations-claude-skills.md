# hr-operations (borghei/Claude-Skills) — GitHub Repo

## TL;DR
Cụm skill hành chính nhân sự trong bộ 343 skill của `borghei/Claude-Skills` (388 stars) — quản lý con người thật (tuyển dụng, onboarding, quan hệ lao động, đánh giá hiệu suất, org design), khác hẳn 8 role AI hiện có trong kho vốn chỉ điều phối công việc số.

## Repo này dùng để làm gì
`borghei/Claude-Skills` là kho tổng hợp skill cho mọi phòng ban (engineering, PM, marketing, C-level, compliance...), trong đó cụm `hr-operations/` gồm nhiều skill con, đáng chú ý nhất:
- **`hr-business-partner`** — đóng vai HRBP chiến lược: lập kế hoạch nhân sự, thiết kế quy trình đánh giá hiệu suất, xử lý case quan hệ lao động (khiếu nại, tranh chấp) theo quy trình chuẩn **Listen → Investigate → Analyze → quyết định**, tư vấn thay đổi tổ chức cho lãnh đạo.
- Các skill khác trong cụm HR (theo router `SKILL.md` gốc): mô tả công việc (JD), bộ câu hỏi phỏng vấn, checklist onboarding, benchmark lương thưởng, DEI strategy.

Điểm khác biệt quan trọng với 8 role AI đã có trong `agents/company/`: những role đó (Research, Marketing, Sales, Content, Dev, Designer, Media, Ops&Finance) đều là AI phối hợp AI, xử lý công việc số. Cụm skill này quản lý **người thật** — nhân viên ca trực Fast Track, nhân sự Tano Cafe, cộng tác viên/freelancer thuê ngoài — có hợp đồng thật, có tranh chấp thật, có nghĩa vụ pháp lý thật.

## Setup từng bước
1. Clone repo, copy đúng cụm cần dùng:
```bash
git clone https://github.com/borghei/Claude-Skills.git
cp -r Claude-Skills/hr-operations ~/.claude/skills/
```
2. Hoặc copy lẻ 1 skill nếu chỉ cần 1 việc cụ thể:
```bash
cp -r Claude-Skills/hr-operations/hr-business-partner ~/.claude/skills/
```
3. Trigger tự nhiên: mô tả tình huống (vd "nhân viên ca trực Fast Track khiếu nại về lịch làm") → skill tự áp quy trình Listen/Investigate/Analyze.

## Ví dụ thực tế
Tano Cafe cần tuyển thêm 1 nhân viên pha chế ca sáng — dùng skill để soạn JD chuẩn, bộ câu hỏi phỏng vấn theo năng lực (competency-based), và checklist onboarding tuần đầu (giới thiệu quy trình, ca trực, brand guideline quán). Khi có tranh chấp (vd nhân viên ca trực Fast Track phàn nàn về phân ca không công bằng) → dùng `hr-business-partner` để đi đúng quy trình: nghe đầy đủ, thu thập fact từ các bên, đối chiếu chính sách công ty, rồi mới đề xuất phương án cho CEO quyết — tránh xử lý cảm tính hoặc hứa hẹn vượt thẩm quyền.

## Lưu ý / Lỗi thường gặp
- Skill không có sẵn context luật lao động Việt Nam (BHXH, BHYT, hợp đồng lao động theo Bộ luật Lao động VN, thuế TNCN) — chỉ đưa khung quy trình chuẩn quốc tế, phần tuân thủ pháp lý VN vẫn phải tự bổ sung hoặc hỏi luật sư/kế toán khi có vấn đề thật.
- Case quan hệ lao động (khiếu nại, tranh chấp, sa thải) luôn có rủi ro pháp lý — AI chỉ hỗ trợ quy trình và soạn thảo, quyết định cuối cùng bắt buộc qua CEO (Nobitano), không được tự động hoá.
- License repo gốc là "Other/NOASSERTION" (không phải MIT/Apache chuẩn) — đọc kỹ điều khoản trước khi dùng thương mại, khác với hầu hết skill khác trong kho.

## Đánh giá cá nhân
- Điểm mạnh: quy trình HRBP rõ ràng, có sẵn khung xử lý case nhạy cảm (quan hệ lao động) thay vì chỉ có mẫu JD/checklist hời hợt; nằm trong kho lớn 343 skill nên dễ mở rộng thêm cụm khác (vd compliance, procurement) nếu cần sau này.
- Điểm yếu: không có context luật VN — phần compliance vẫn phải tự làm; license không rõ ràng bằng MIT nên cẩn trọng khi dùng cho mục đích thương mại; đây không phải skill chuyên biệt 100% cho HR (nằm trong kho tổng hợp đa ngành).
- Có nên dùng không: 7/10 — đủ dùng làm khung quy trình cho role HR&Admin mới, miễn là luôn nhớ tự bổ sung phần tuân thủ pháp lý VN và giữ nguyên tắc "AI không tự quyết định sa thải/kỷ luật".

## Link
- Repo: https://github.com/borghei/Claude-Skills
- Skill path: https://github.com/borghei/Claude-Skills/tree/main/hr-operations/hr-business-partner

---

## 🤖 Agent Integration

### Hermes (Python)
```python
def fetch_hr_business_partner_skill():
    url = "https://raw.githubusercontent.com/borghei/Claude-Skills/main/hr-operations/hr-business-partner/SKILL.md"
    return http_get(url)

def hr_case_review(case_summary):
    """case_summary: mô tả tình huống nhân sự cần xử lý (khiếu nại, tranh chấp, tuyển dụng...)"""
    system = fetch_hr_business_partner_skill()
    return call_llm(case_summary, task_type="reasoning", system=system, max_tokens=3000)
```

### OpenClaw
```bash
git clone https://github.com/borghei/Claude-Skills.git /tmp/claude-skills-borghei
cp -r /tmp/claude-skills-borghei/hr-operations ~/.claude/skills/
```

### Antigravity
```bash
mkdir -p /opt/skills && git clone https://github.com/borghei/Claude-Skills.git /opt/skills/claude-skills-hr
```
> ⚠️ Mọi case liên quan quyết định thật với nhân viên (sa thải, kỷ luật, thay đổi lương) luôn trả về `needs_confirmation: true` cho CEO — AI chỉ soạn thảo và đề xuất, không tự quyết.
