# founder-skills (ognjengt) — GitHub Repo

## TL;DR
Bộ **15 skill** dạng prompt thuần (MIT, tác giả Ognjen Gatalo) cho founder/marketer: SOP, tối ưu chuyển đổi (CRO), go-to-market, định giá, outreach, viết bài X/LinkedIn, PRD, Product Hunt… Cài bằng 1 lệnh, dùng bằng `/tên-skill`. Không có script hay API — chỉ là các file `SKILL.md` + tài liệu tham chiếu, nên **an toàn để đọc và mượn**, nhưng thiên mạnh về thị trường Mỹ/tiếng Anh và **repo đã 5 tháng không có commit mới**.

> Lưu ý trùng tên: tìm "founder-skills" ra nhiều repo khác nhau (`shawnpang/startup-founder-skills`, `emotixco/claude-skills-founder`, `tenequm/founder-playbook`). Entry này nói về **`ognjengt/founder-skills`** (khớp đúng tên). Nếu ý là repo khác → báo để viết riêng.

## Repo này dùng để làm gì
Mỗi skill là một quy trình hỏi-đáp có khung sẵn: bạn mô tả việc, skill hỏi tối đa 5–10 câu chẩn đoán rồi trả kết quả theo mẫu. Có một file `FOUNDER_CONTEXT.md` (tên công ty, khách hàng mục tiêu, giọng thương hiệu, mục tiêu) để skill tự cá nhân hoá — mỗi dự án/khách một file.

| Nhóm | Skill |
|---|---|
| Chiến lược | `strategic-planning` (3 bước đi tiếp theo), `go-to-market-plan` (3 chiến lược GTM), `pricing-strategist`, `competitor-intel` (bắt buộc tìm web) |
| Chuyển đổi/Copy | `cro-optimization` (13 nguyên tắc), `brand-copywriter` (AIDA/PAS/BAB…), `lead-magnet-generator`, `viral-hook-creator` |
| Mạng xã hội/Outreach | `x-writer` (51+ mẫu), `linkedin-writer`, `outreach-specialist` (cold email/DM) |
| Sản phẩm/Vận hành | `prd-generator`, `sop-creator`, `product-hunt-launch-plan`, `marketing-ideas` (160+ ý tưởng) |

## Số liệu đã kiểm (15/10/2026, đọc từ bản clone nông)
- License: MIT (đã mở LICENSE). Commit mới nhất: 18/05/2026 (`a45931c`)
- Thực tế có **15 skill** trong `skills/` — README ghi "20+" nên không khớp
- Tổng ~180KB SKILL.md, không có file `.py/.sh/.js` nào trong `skills/`; `bin/cli.js` chỉ chép thư mục vào `~/.claude/skills` và chép `FOUNDER_CONTEXT.md` vào thư mục dự án (không thấy gọi mạng)
- Số sao / số người dùng: **chưa đo** (API GitHub bị chặn trong phiên này)
- Chưa cài, chưa chạy skill nào trên Claude Code thật

## Setup
```bash
# Cài tất cả
npx skills add https://github.com/ognjengt/founder-skills
# Cài 1 skill
npx skills add https://github.com/ognjengt/founder-skills --skill competitor-intel
# Hoặc thủ công
git clone https://github.com/ognjengt/founder-skills
cp -r founder-skills/skills/competitor-intel ~/.claude/skills/
```
Sau đó tạo `FOUNDER_CONTEXT.md` ở thư mục gốc dự án (copy mẫu trong repo, điền thật). Gọi: `/go-to-market-plan sản phẩm của tôi là …`.

## Ví dụ thực tế
Bối cảnh: agency cần phân tích đối thủ cho một khách SaaS đặt chỗ.
```text
/competitor-intel [TÊN ĐỐI THỦ] website [URL], ngành [NGÀNH], quan tâm giá và kênh quảng cáo
```
Skill bắt buộc tìm web (theo SKILL.md), đối chiếu số liệu thật và đưa chiến lược khai thác điểm yếu + dự đoán bước tiếp theo của đối thủ. Với `FOUNDER_CONTEXT.md` của khách, phần "khai thác" bám theo định vị của khách. **Chưa chạy thử — chưa biết chất lượng đầu ra.**

## Lưu ý / Lỗi thường gặp
- **Thiên Mỹ/EN**: X, LinkedIn, Product Hunt, cold email kiểu Mỹ. Với khách Việt phải viết lại phần kênh và giọng (Zalo, TikTok, Facebook không có sẵn)
- `prd-generator` xuất PDF bằng `npx md-to-pdf` (tải gói từ npm khi chạy) — môi trường chặn mạng sẽ lỗi
- `x-writer` có "voice matching" theo các nhân vật (Hormozi, Naval…) và chính tác giả → cẩn thận khi dùng cho brand/khách thật, đừng để nó bắt chước người cụ thể
- Skill `competitor-intel` nói "không bịa số" nhưng chỉ đúng khi agent thật sự tìm web được — luôn kiểm số liệu lên bài
- README gọi "skills công ty trả hàng triệu đô" là quảng cáo, không có bằng chứng trong repo
- Repo chưa cập nhật từ 05/2026; chưa biết có còn được bảo trì

## Đánh giá cá nhân
- Điểm mạnh: MIT, prompt thuần nên rủi ro bảo mật thấp (không script, đã đọc `cli.js`), cấu trúc chuẩn `SKILL.md` + `references/`, có cơ chế `FOUNDER_CONTEXT.md` dùng lại cho nhiều khách, vòng hỏi chẩn đoán trước khi trả lời tốt hơn kiểu "viết hộ ngay"
- Điểm yếu: chưa chạy thử, thiên thị trường Mỹ, đã 5 tháng không commit, README nói quá (20+ vs 15), trùng ý với `repos/marketingskills.md` (Corey Haines — nhiều skill hơn, 44K sao theo entry đó)
- Có nên dùng: **5/10**. Không cài thành bộ cho agent. Dùng làm **nguồn mượn khung**: lấy cơ chế `FOUNDER_CONTEXT.md` (hồ sơ khách dùng chung) và khung hỏi chẩn đoán của `go-to-market-plan`, `pricing-strategist`, `sop-creator` để viết lại thành skill của Pro Agent Marketing/Sales. Cần marketing ops đầy đủ → dùng `repos/marketingskills.md` trước

## Link
- Repo: https://github.com/ognjengt/founder-skills
- Trang giới thiệu của tác giả: https://saasstrats.com/founder-skills
- Liên quan trong kho: `repos/marketingskills.md`, `repos/ai-marketing-claude.md`, `repos/claude-seo.md`, `agents/digital-marketing-agent/`, `agents/sales-ceo/`

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không có API. Skill là file SKILL.md để nạp làm system prompt/chỉ dẫn.
# Hermes chỉ cần ĐỌC file (đã clone về VPS) và ghép với hồ sơ khách:
import pathlib

def load_skill(repo_dir, name, context_path=None):
    skill = (pathlib.Path(repo_dir) / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
    ctx = ""
    if context_path and pathlib.Path(context_path).exists():
        ctx = "\n\n# FOUNDER_CONTEXT\n" + pathlib.Path(context_path).read_text(encoding="utf-8")
    return skill + ctx   # đưa làm system prompt cho model, rồi gửi yêu cầu của người dùng

# vd: prompt = load_skill("/opt/kho/founder-skills", "go-to-market-plan", "khach-A/FOUNDER_CONTEXT.md")
```
Chưa chạy thử. Skill dùng công cụ `AskUserQuestion` và `Read` của Claude Code — ngoài Claude Code phải đổi thành hỏi thường.

### OpenClaw
```bash
npx skills add https://github.com/ognjengt/founder-skills --skill go-to-market-plan
```

### Antigravity
```bash
# Không cần deploy. Chỉ clone để các agent đọc:
git clone --depth 1 https://github.com/ognjengt/founder-skills /opt/kho/founder-skills
```
> ⚠️ Mỗi khách một `FOUNDER_CONTEXT.md` riêng, không để lẫn dữ liệu giữa các khách và không commit lên kho chung. Skill do người ngoài viết: đọc `SKILL.md` trước khi cài, đi qua `skill-lifecycle-management` nếu muốn đưa vào Pro Agent.
