# marketingskills — 43 skill marketing biến AI agent thành CMO thực thụ

**GitHub:** https://github.com/coreyhaines31/marketingskills
**Stars:** 31.9k | **Forks:** 5.3k | **License:** MIT
**Tác giả:** Corey Haines | **Version:** v2.3.0 (tháng 5/2026)
**Commits:** 309 | **Releases:** 16

---

## Vấn đề nó giải quyết

Mày đang dùng Claude Code hoặc Cursor để build sản phẩm. Đến lúc cần làm marketing, mày hỏi agent:

> "Optimize landing page này giúp tôi"

Agent trả ra một đống text chung chung. Câu nào cũng đúng, không cái nào dùng được.

Lý do: agent không có context về sản phẩm của mày, không biết framework CRO là gì, không biết khi nào cần A/B test trước khi rewrite copy.

marketingskills giải quyết đúng vấn đề đó — bằng cách cho agent **chuyên môn hóa**.

---

## Cơ chế hoạt động

Repo này là **43 file markdown**, mỗi file = một "skill" định nghĩa cho agent biết:
- Khi nào activate skill này
- Làm theo framework nào
- Tham chiếu skill nào khác khi cần

**Flow:**
```
Mày hỏi → agent nhận diện intent → load đúng skill → thực thi theo framework
```

**Điểm thiết kế thông minh nhất:** Skill `product-marketing` là foundation. Trước khi làm bất cứ thứ gì, tất cả 42 skill còn lại đều đọc file context sản phẩm của mày trước. Setup một lần, dùng mãi.

---

## 43 Skills — Phân loại theo nhóm

| Nhóm | Skills |
|------|--------|
| **SEO & Content** | seo-audit, ai-seo, site-arch, programmatic-seo, schema-markup, content-strategy, aso-audit |
| **CRO** | cro, signup, onboarding, form-cro, popups, paywall |
| **Copy & Content** | copywriting, copy-editing, cold-email, email-sequence, social, video, image, sms, ad-creative |
| **Paid & Analytics** | paid-ads, analytics-tracking, ab-testing |
| **Growth & Retention** | referral-program, free-tool-strategy, churn-prevention, community-marketing, lead-magnets, co-marketing |
| **Sales & GTM** | revops, sales-enablement, launch-strategy, pricing-strategy, competitor-alternatives, competitor-profiling, directory-submissions, prospecting |
| **Strategy** | marketing-ideas, marketing-psychology, customer-research, marketing-plan |

**Skill đáng chú ý nhất:** `ai-seo` — optimize content để được ChatGPT, Claude, Perplexity cite. Đây là thứ rất ít framework marketing nào có ở thời điểm này.

**Skill mới nhất (tháng 5/2026):** `marketing-plan` — tạo bản kế hoạch marketing theo AARRR, ~13 mục, ~10,000 từ, điều chỉnh theo budget/team size/giai đoạn sản phẩm.

---

## Setup — 3 cách cài

**Cách 1: npx (nhanh nhất)**
```bash
npx skills add coreyhaines31/marketingskills
```
Tự động cài vào `.agents/skills/` và symlink vào `.claude/skills/`.

**Cách 2: Claude Code plugin**
```
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

**Cách 3: Thủ công (không có Claude Code)**
```bash
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

---

## Setup quan trọng nhất — product-marketing context

Trước khi dùng bất kỳ skill nào, phải tạo file context sản phẩm:

```bash
# Trong project của mày, chạy:
mkdir -p .agents
```

Sau đó tạo file `.agents/product-marketing.md` với 12 sections:

```
Product Overview → Target Audience → Personas → Problems & Pain Points
→ Competitive Landscape → Differentiation → Objections → Switching Dynamics
→ Customer Language → Brand Voice → Proof Points → Goals
```

Điền xong file này → mọi skill khác biết sản phẩm của mày là gì, không cần giải thích lại.

---

## Dùng với claude.ai (không có Claude Code)

Fork [mysticaltech/marketingskills](https://github.com/mysticaltech/marketingskills) — bản này có sẵn `.skill` files để upload lên Claude Settings.

Hoặc thủ công:
1. Vào GitHub, mở skill cần dùng, click **Raw**
2. Copy toàn bộ nội dung
3. Paste vào đầu chat trong thẻ:

```
<skill>
[nội dung SKILL.md]
</skill>

Task của mày ở đây
```

---

## Ví dụ thực tế

```
"Help me optimize this landing page for conversions"
→ Agent load skill cro → phân tích theo 7-dimension framework
→ Output: Quick Wins / High-Impact / Test Ideas / Copy Alternatives

"Write homepage copy for my SaaS"
→ Agent load skill copywriting → áp dụng PAS/BAB/FAB framework
→ Output: 3 headline options + rationale + body copy draft

"Set up GA4 tracking for signups"
→ Agent load skill analytics-tracking
→ Output: implementation guide step-by-step
```

---

## Cross-reference quan trọng

Skills tự biết khi nào cần gọi skill khác:
- `copywriting` ↔ `cro` ↔ `ab-testing`
- `revops` ↔ `sales-enablement` ↔ `cold-email`
- `seo-audit` ↔ `schema-markup` ↔ `ai-seo`
- `customer-research` → `copywriting`, `cro`, `competitor-alternatives`

---

## Điểm trừ thẳng thắn

**Cần biết dùng CLI:** Cài qua `npx` hoặc copy thủ công — không có GUI.

**Phụ thuộc vào context file:** Nếu `.agents/product-marketing.md` bỏ trống hoặc điền qua loa, output vẫn generic như không có skill.

**Không phải cho người dùng web interface:** Lợi ích giảm đáng kể nếu chỉ chat trực tiếp trên claude.ai — phải paste thủ công từng skill.

---

## Đánh giá cá nhân

marketingskills là thứ **technical founder nên cài trước khi mua thêm bất kỳ AI marketing tool SaaS nào**.

31.9k stars không phải ngẫu nhiên — đây là một trong số ít repo giải quyết đúng vấn đề: AI agent giỏi code nhưng không biết marketing. Bộ skill này vá đúng lỗ hổng đó.

Điểm tao đánh giá cao nhất là `ai-seo` và `marketing-plan`. Hai skill này cover những thứ mà ngay cả fractional CMO chuyên nghiệp cũng hay bỏ sót khi làm với startup giai đoạn đầu.

Phù hợp nhất: technical founder, indie hacker, hoặc marketer đang dùng Claude Code / Cursor. Không phù hợp: người chưa biết terminal là gì.

**Rating: 9/10** — trừ 1 điểm vì barrier to entry với non-technical users còn cao.

---

*Nguồn: github.com/coreyhaines31/marketingskills*
*Cập nhật: tháng 6/2026*
