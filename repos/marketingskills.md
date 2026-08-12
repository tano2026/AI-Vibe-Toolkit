---
name: marketingskills
description: >
  Stars: 44k Forks: 6.9k License: MIT Tác giả: Corey Haines Version: v2.10.0
  (27/07/2026)
---

# marketingskills — 49 skill marketing biến AI agent thành CMO thực thụ

**GitHub:** https://github.com/coreyhaines31/marketingskills
**Stars:** 44k | **Forks:** 6.9k | **Watching:** 385 | **License:** MIT
**Tác giả:** Corey Haines (founder Conversion Factory, newsletter Swipe Files) | **Version:** v2.10.0 (27/07/2026)
**Commits:** 389 | **Releases:** 39 | **Branches:** 33 | **Tags:** 39

---

## Vấn đề nó giải quyết

Mày đang dùng Claude Code hoặc Cursor để build sản phẩm. Đến lúc cần làm marketing, mày hỏi agent:

> "Optimize landing page này giúp tôi"

Agent trả ra một đống text chung chung. Câu nào cũng đúng, không cái nào dùng được.

Lý do: agent không có context về sản phẩm của mày, không biết framework CRO là gì, không biết khi nào cần A/B test trước khi rewrite copy.

marketingskills giải quyết đúng vấn đề đó — bằng cách cho agent **chuyên môn hóa**.

---

## Cơ chế hoạt động

Repo này là **49 file markdown** (tính tới v2.10.0), mỗi file = một "skill" định nghĩa cho agent biết:
- Khi nào activate skill này
- Làm theo framework nào
- Tham chiếu skill nào khác khi cần

**Flow:**
```
Mày hỏi → agent nhận diện intent → load đúng skill → thực thi theo framework
```

**Điểm thiết kế thông minh nhất:** Skill `product-marketing` là foundation. Trước khi làm bất cứ thứ gì, tất cả skill còn lại đều đọc file context sản phẩm của mày trước. Setup một lần, dùng mãi.

---

## 49 Skills — Phân loại theo nhóm

| Nhóm | Skills |
|------|--------|
| **SEO & Content** | seo-audit, ai-seo, site-architecture, programmatic-seo, schema, content-strategy, aso |
| **CRO** | cro, signup, onboarding, offers, popups, paywalls |
| **Copy & Content** | copywriting, copy-editing, cold-email, emails, social, video, image, sms, ad-creative |
| **Paid & Measurement** | ads, analytics, ab-testing, **attribution** (mới v2.10.0) |
| **Growth & Retention** | referrals, free-tools, churn-prevention, community-marketing, lead-magnets, co-marketing, marketing-loops |
| **Sales & GTM** | revops, sales-enablement, launch, pricing, competitors, competitor-profiling, directory-submissions, prospecting, public-relations, influencer-marketing |
| **Strategy** | marketing-ideas, marketing-psychology, customer-research, marketing-plan, **marketing-council** |

**Skill mới đáng chú ý nhất — `attribution` (v1.1.0, thêm trong v2.10.0):** trả lời câu hỏi khó nhất marketing — kênh nào thực sự tạo ra conversion/revenue. Trước đây phần này bị rải rác trong analytics (UTM), ads (pixel), revops (pipeline), ai-seo (AI blind spot) — giờ gom thành 1 skill riêng, có 2 trụ: (A) Interpretation — 6 mô hình attribution và khi nào mỗi mô hình "nói dối"; (B) Own your attribution — tự dựng first-party attribution khi mày kiểm soát được site/app.

**Skill độc đáo — `marketing-council`:** mô phỏng một "ban cố vấn" gồm các marketer huyền thoại (Seth Godin, David Ogilvy, Eugene Schwartz, April Dunford, Rory Sutherland, Alex Hormozi, Byron Sharp...) — mỗi người đưa ý kiến theo đúng framework họ từng công bố, cố tình để họ **bất đồng** với nhau để lộ ra trade-off thật, rồi tổng hợp khuyến nghị. Skill tự ghi rõ đây là "persona simulation", không phải người thật.

**Skill nền tảng cho người mới — `marketing-ideas`:** thư viện 139 ý tưởng marketing đã kiểm chứng cho SaaS (không phải 140 như một số bài review — số thật lấy trực tiếp từ SKILL.md là 139), gợi ý 3-5 ý tưởng phù hợp nhất theo giai đoạn/ngân sách/team size.

**`ai-seo`** vẫn là skill hiếm có framework marketing nào làm — optimize content để được ChatGPT, Claude, Perplexity trích dẫn.

---

## Setup — 3 cách cài

**Cách 1: npx (nhanh nhất)**
```bash
npx skills add coreyhaines31/marketingskills
```
Tự động cài vào `.agents/skills/` và symlink vào `.claude/skills/`.

**Cách 2: Claude Code plugin marketplace**
```
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

**Cách 3: Thủ công (không có Claude Code)**
```bash
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

Ngoài ra còn git submodule, fork tùy chỉnh, và SkillKit đa agent — hợp Claude Code, OpenAI Codex, Cursor, Windsurf.

---

## Setup quan trọng nhất — product-marketing context

Trước khi dùng bất kỳ skill nào, phải tạo file context sản phẩm:

```bash
mkdir -p .agents
```

Sau đó tạo file `.agents/product-marketing.md` với 12 sections:

```
Product Overview → Target Audience → Personas → Problems & Pain Points
→ Competitive Landscape → Differentiation → Objections → Switching Dynamics
→ Customer Language → Brand Voice → Proof Points → Goals
```

Điền xong file này → mọi skill khác (kể cả `marketing-council` và `attribution` mới) đều tự đọc, không cần giải thích lại.

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

"Google nói kênh A tốt nhất, GA4 nói kênh B tốt nhất, số nào đúng?"
→ Agent load skill attribution → giải thích vì sao 2 dashboard "nói dối"
theo cách khác nhau, đề xuất mô hình attribution phù hợp

"Seth Godin với Hormozi sẽ nghĩ gì về chiến lược launch này?"
→ Agent load skill marketing-council → mô phỏng debate giữa các advisor,
tổng hợp khuyến nghị + chỗ họ bất đồng
```

---

## Cross-reference quan trọng

Skills tự biết khi nào cần gọi skill khác:
- `copywriting` ↔ `cro` ↔ `ab-testing`
- `revops` ↔ `sales-enablement` ↔ `cold-email`
- `seo-audit` ↔ `schema` ↔ `ai-seo`
- `customer-research` → `copywriting`, `cro`, `competitors`
- `attribution` → không ôm việc của `analytics` (UTM/event tracking) hay `ads` (pixel) — chỉ lo phần "join touch → conversion → revenue"

---

## Điểm trừ thẳng thắn

**Cần biết dùng CLI:** Cài qua `npx` hoặc copy thủ công — không có GUI.

**Phụ thuộc vào context file:** Nếu `.agents/product-marketing.md` bỏ trống hoặc điền qua loa, output vẫn generic như không có skill — kể cả skill mới `marketing-council`/`attribution` cũng dựa vào file này.

**Không phải cho người dùng web interface:** Lợi ích giảm đáng kể nếu chỉ chat trực tiếp trên claude.ai — phải paste thủ công từng skill.

**`marketing-council` là persona simulation:** không phải Seth Godin/Hormozi thật trả lời — chỉ là mô phỏng dựa trên framework họ đã công bố công khai, cần hiểu rõ giới hạn này trước khi tin tưởng tuyệt đối vào output.

---

## Đánh giá cá nhân

marketingskills là thứ **technical founder nên cài trước khi mua thêm bất kỳ AI marketing tool SaaS nào**.

44k stars không phải ngẫu nhiên — đây là một trong số ít repo giải quyết đúng vấn đề: AI agent giỏi code nhưng không biết marketing. Bộ skill này vá đúng lỗ hổng đó, và vẫn đang active phát triển đều (39 release, update gần nhất tháng 7/2026).

Skill mới `attribution` là bổ sung hợp lý nhất trong bản v2.10.0 — trước đây đúng là bị thiếu 1 chỗ "chốt" câu hỏi kênh nào thực sự ăn tiền, giờ có hẳn 1 skill riêng xử lý reconciliation giữa các dashboard mâu thuẫn nhau. `marketing-council` thì vui nhưng giá trị thực tế phụ thuộc nhiều vào việc người dùng có hiểu đây là simulation hay không.

Phù hợp nhất: technical founder, indie hacker, hoặc marketer đang dùng Claude Code / Cursor. Không phù hợp: người chưa biết terminal là gì.

**Rating: 9/10** — trừ 1 điểm vì barrier to entry với non-technical users còn cao, và `marketing-council` dễ bị hiểu nhầm là "ý kiến thật" nếu không đọc kỹ disclaimer.

---

*Nguồn: github.com/coreyhaines31/marketingskills*
*Cập nhật: 12/08/2026 — nâng từ v2.3.0 (31.9k sao, 43 skill) lên v2.10.0 (44k sao, 49 skill, thêm attribution + marketing-council)*
