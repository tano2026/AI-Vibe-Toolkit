# AI Content Stack — Workflow Viết Content Hoàn Chỉnh Cho Người Việt

**Use case:** Tạo content marketing chuyên nghiệp với AI — từ ý tưởng đến đăng bài
**Target:** Founder, marketer, creator không có team content
**Thời gian setup:** 30 phút
**Chi phí:** Từ $0 (free tier) đến ~$20/tháng

---

## Vấn đề Stack Này Giải Quyết

Mày có sản phẩm/dịch vụ cần content đều đặn nhưng:
- Không có thời gian viết từ đầu
- Thuê copywriter đắt ($50-200/bài)
- Tự viết thì AI output ra bài generic, đọc là biết robot viết

Stack này giải quyết cả 3 vấn đề — output chất lượng, nhanh, và đọc như người thật viết.

---

## Stack Overview

```
[IDEATION] → [RESEARCH] → [WRITING] → [EDITING] → [PUBLISH]
   Perplexity     Perplexity    Claude/GPT    Claude      Buffer/Later
   ChatGPT        Firecrawl     6 Prompts     Prompt #06
```

---

## Các Tool Trong Stack

### 1. Ideation & Research
**Tool:** Perplexity AI (free) hoặc ChatGPT

**Dùng để:**
- Tìm topic ideas theo niche
- Research competitor content
- Tìm pain points của target audience

**Prompt tìm ý tưởng:**
```
Tìm 10 chủ đề content hot nhất cho [niche của mày] trong tháng này.
Ưu tiên những chủ đề:
- Có nhiều người đang tìm kiếm
- Chưa có quá nhiều bài viết tốt
- Phù hợp với người [mô tả target audience]
```

---

### 2. Scrape & Thu Thập Thông Tin
**Tool:** Firecrawl MCP hoặc Brave Search MCP

**Dùng để:**
- Đọc bài của competitor
- Lấy thông tin từ URL cụ thể
- Thu thập dữ liệu làm dẫn chứng

**Cách dùng với Claude:**
```
Đọc bài viết tại [URL] và tóm tắt:
- Ý chính là gì
- Điểm mạnh/yếu của bài
- Góc nhìn nào chưa được đề cập
```

---

### 3. Writing — 6 Prompt Core
**Tool:** Claude hoặc ChatGPT

Đây là core của stack. Dùng **6 prompts từ skills/ai-content-writing.md** theo workflow:

```
Ý tưởng → Prompt #05 (draft) → Prompt #01 (humanize)
→ Prompt #02 (persuasion) → Prompt #06 (proofread)
→ Prompt #04 (social version) hoặc Prompt #03 (long-form version)
```

**Thời gian:** 15-20 phút/bài thay vì 2-3 giờ

---

### 4. Hình Ảnh & Visual
**Tool:** Canva (free) + ChatGPT Image

**Workflow:**
```
ChatGPT Image → Tạo ảnh minh họa từ prompt
Canva → Thêm text, brand colors, resize theo platform
```

**Prompt tạo ảnh:**
```
Tạo ảnh infographic minh họa cho chủ đề [X]:
- Style: clean, professional, màu chủ đạo [màu brand]
- Không có text (sẽ thêm sau trong Canva)
- Tỷ lệ 9:16 cho TikTok/Reels
```

---

### 5. Scheduling & Distribution
**Tool:** Buffer (free 3 kênh) hoặc Later

**Workflow:**
- Viết content batch 1 lần/tuần (5-7 bài)
- Schedule tự động cho cả tuần
- Track performance trong dashboard

---

## Workflow Chi Tiết — Từng Bước

### Bước 1: Ideation (5 phút)
```
Perplexity: "Top 5 câu hỏi mà [target audience] đang hỏi về [topic] tuần này"
→ Chọn 1 topic → Note 3-5 ý chính muốn cover
```

### Bước 2: Draft Nhanh (3 phút)
```
Gạch đầu dòng 5-7 ý chính ra notepad
→ Dán vào Prompt #05
→ Claude xuất ra draft 400-500 từ
```

### Bước 3: Humanize (2 phút)
```
Copy draft → Dán vào Prompt #01
→ Bài đọc tự nhiên hơn, bớt AI hơn
```

### Bước 4: Tăng Persuasion (2 phút)
```
Copy kết quả → Dán vào Prompt #02
→ Thêm CTA, nhấn mạnh value
```

### Bước 5: Proofread (2 phút)
```
Copy toàn bài → Dán vào Prompt #06
→ Sửa lỗi, tối ưu flow, bản final
```

### Bước 6: Repurpose (5 phút)
```
Bài hoàn chỉnh → Prompt #04 → Post social media
Bài hoàn chỉnh → Prompt #03 → Bài blog 700 từ
```

**Tổng thời gian: ~20 phút/bài**

---

## Content Calendar Gợi Ý

| Ngày | Content Type | Prompt chính |
|------|-------------|--------------|
| Thứ 2 | Educational post | #05 → #01 → #06 |
| Thứ 3 | Story/case study | #05 → #01 → #02 |
| Thứ 4 | Tips/list | #05 → #04 |
| Thứ 5 | Blog dài | #05 → #01 → #03 |
| Thứ 6 | CTA/offer | #02 → #06 |

---

## Chi Phí Ước Tính

| Tool | Free Tier | Paid |
|------|-----------|------|
| Claude | Claude.ai free | $20/tháng (Pro) |
| ChatGPT | GPT-3.5 free | $20/tháng (Plus) |
| Perplexity | 5 searches/ngày | $20/tháng |
| Canva | Miễn phí | $13/tháng (Pro) |
| Buffer | 3 kênh, 10 posts | $15/tháng |
| Firecrawl | 500 pages/tháng | $16/tháng |

**Tổng tối thiểu (free):** $0 — dùng được ngay
**Tổng đề xuất:** ~$20-40/tháng (Claude Pro + Canva)

---

## Nâng Cấp Stack

Khi mày đã quen workflow cơ bản, thêm:

**Level 2 — Tự động hóa một phần:**
- **n8n** — tự động lấy topic từ RSS → tạo draft → lưu vào Notion
- **Make.com** — schedule post tự động từ Google Sheets

**Level 3 — Scale:**
- **marketingskills** (xem `/repos/marketingskills.md`) — thêm framework CRO, SEO vào workflow
- **ElevenLabs** — convert bài viết thành voiceover cho video

---

## Đánh Giá Stack

Stack này phù hợp nhất cho **solo founder hoặc team nhỏ 1-3 người** cần content đều đặn mà không muốn thuê content writer.

Điểm mạnh: Toàn bộ flow từ ý tưởng đến đăng bài trong ~30 phút. 6 prompts cover đủ các trường hợp viết phổ biến nhất.

Điểm yếu: Cần chỉnh tay thêm nếu mày có brand voice rất đặc thù — AI vẫn cần một vài vòng chỉnh để match đúng tone.

Tao estimate stack này tiết kiệm được 10-15 giờ/tuần so với viết thủ công hoặc brief cho copywriter.

**Rating: 8.5/10**

---

## Related
- `skills/ai-content-writing.md` — 6 prompts chi tiết
- `repos/marketingskills.md` — framework marketing nâng cao
- `mcps/firecrawl.md` — setup Firecrawl để research content

---

*Cập nhật: tháng 6/2026*
