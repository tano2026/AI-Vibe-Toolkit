# Site Launch Checklist — Skill

## TL;DR
Checklist trước khi ship 1 website/landing page ra production: analytics (GA4, PostHog, GSC), bảo mật headers, SEO + GEO (kèm robots.txt, sitemap, llms.txt cho AI crawler), copywriting pass, favicon, Lighthouse/Core Web Vitals/accessibility. Chạy tương tác từng bước, không tuôn 1 lần cả đống câu hỏi.

## Tool này dùng để làm gì
Đây là skill "chốt sổ trước khi launch" — cách vận hành đặc biệt ở chỗ nó BẮT BUỘC hỏi từng câu một bằng nút bấm (kiểu `ask_user_input_v0`), không đoán bừa hộ user. Ngay đầu phiên hỏi 6 câu cố định: loại site (doc-site/marketing/SaaS/khóa học/portfolio), có migrate domain không, đa ngôn ngữ không, setup PostHog kiểu gì, chính sách cho AI bot scrape, có browser tool để tự kiểm tra không.

Điểm hay nhất cho Nobitano: có hẳn phần **SEO/GEO** — kiểm tra robots.txt, sitemap, hreflang, schema markup, VÀ cả `llms.txt` (file cho AI crawler như ChatGPT/Perplexity đọc) — đúng hướng GEO/AEO mà kho đã note trước đó ("Google confirm GEO vẫn là SEO cốt lõi").

## Setup từng bước
1. Cài lẻ:
```
npx skills add https://github.com/samber/cc-skills --skill site-launch-checklist
```
2. Cần Claude Code (skill yêu cầu compatibility Claude Code cụ thể, không chạy tốt trên agent thuần).
3. Cần sẵn: `curl`, `npm`, `npx`, `jq` trên máy (skill tự check requires.bins).
4. Chạy skill → trả lời 6 câu hỏi mở đầu → skill tự chạy qua các phase (Phase 3 dành riêng cho site tiếng Pháp thì tự skip nếu chọn site không phải FR).

## Ví dụ thực tế
Input: chuẩn bị launch `fasttracknoibai.com` bản mới (redesign lại, giữ domain cũ).
→ Trả lời: site type = marketing/lead-gen, migration = replacing-existing-on-same-domain, multilingual = single-locale (vi), PostHog = skip, AI scraper policy = customize-per-bot (cho phép GPTBot/ClaudeBot đọc để lên AI Overview, chặn bot spam khác).
→ Skill chạy qua từng phase: check GA4 event, robots.txt/llms.txt, security headers, đồng bộ TONE.md content trước khi lên (đây là chỗ nối được với PROSE.md/TONE.md ở 2 skill kia), rồi Lighthouse + mobile test trước khi bấm nút go-live.

## Lưu ý / Lỗi thường gặp
- Skill này **opinionated cho Cloudflare DNS + Vercel hosting** — nếu ABTRIP/Wonder Mart host chỗ khác (VD cPanel truyền thống), một số bước (cache purge, edge config) sẽ không áp dụng được, phải tự bỏ qua hoặc thay thủ công.
- Không tự làm gì nếu chưa hỏi user — kể cả cài thêm MCP/skill khác (Sentry, BetterStack, Crisp) cũng phải hỏi trước, không được tự ý `npx skills add`.
- Chỉ chạy tốt trên Claude Code — nếu Hermes/OpenClaw cần logic tương tự, phải tự viết lại flow đơn giản hơn (bớt phần hỏi tương tác) chứ không copy nguyên si.

## Đánh giá cá nhân
- Điểm mạnh: gộp đủ mọi thứ hay quên trước khi launch (đặc biệt phần llms.txt/AI bot policy — nhiều landing page VN hiện chưa ai làm), tương tác từng bước tránh launch ẩu.
- Điểm yếu: quá gắn với stack Cloudflare+Vercel+PostHog, VPS Tencent Cloud + domain riêng của Nobitano sẽ phải chỉnh tay khá nhiều đoạn.
- Có nên dùng không: 6.5/10 — dùng được nhưng cần "may đo" lại phần hạ tầng, không plug-and-play 100% cho hệ thống hiện tại của Nobitano.

## Link
- Repo: https://github.com/samber/cc-skills
- SKILL.md gốc: https://github.com/samber/cc-skills/blob/main/skills/site-launch-checklist/SKILL.md

---

## 🤖 Agent Integration

### Hermes (Python)
```python
import urllib.request
url = "https://raw.githubusercontent.com/samber/cc-skills/main/skills/site-launch-checklist/SKILL.md"
content = urllib.request.urlopen(url).read().decode()
with open("skills_local/site-launch-checklist/SKILL.md", "w") as f:
    f.write(content)
```

### OpenClaw
```bash
git clone https://github.com/samber/cc-skills.git ~/.openclaw/skills/cc-skills-launch
```

### Antigravity
```bash
git clone https://github.com/samber/cc-skills.git ~/.antigravity/skills/cc-skills
# Antigravity là bên deploy VPS — có thể dùng checklist này làm base rồi tự sửa phần
# Cloudflare/Vercel-specific thành lệnh tương ứng cho Tencent Cloud VPS.
```
> ⚠️ Yêu cầu Claude Code, không chạy 1:1 trên OpenClaw/Hermes runtime — chỉ dùng làm checklist tham khảo, không gọi trực tiếp qua agent thường.
