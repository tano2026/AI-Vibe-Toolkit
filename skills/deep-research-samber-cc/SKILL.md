# Deep Research (samber/cc-skills) — Skill

## TL;DR
Skill nghiên cứu sâu kiểu "senior research analyst": search web song song nhiều nhánh, bắt buộc trích nguồn cho mọi claim, tự chấm confidence, ra báo cáo Markdown có citation. Có 11 loại nghiên cứu dựng sẵn (market, competitive, technical, academic, financial, legal, trend, community...).

## Tool này dùng để làm gì
Đây là 1 trong ~17 skill nằm trong repo `samber/cc-skills` (153 sao GitHub, tác giả Samuel Berthe). Khác với skill `deep-research` cũ trong kho (dùng MCP firecrawl/exa), skill này KHÔNG cần MCP — chỉ cần WebSearch/WebFetch có sẵn, và tự fan-out 3-20 sub-agent song song theo từng bước nghiên cứu.

Cơ chế hay nhất: bắt persona "nhà phân tích nghi ngờ nguồn đơn lẻ" — mọi claim quan trọng (market size, growth rate, positioning...) phải có ≥2 nguồn độc lập, nếu không sẽ tự gắn nhãn `confidence: Low`. Không được để trống mục nào — thiếu nguồn thì viết thẳng "không tìm thấy nguồn cho X" thay vì bịa hoặc lờ đi.

Có 3 mode theo độ sâu: Quick (câu hỏi hẹp, cần nhanh), Standard (mặc định), Deep (khi user nói "thorough/exhaustive/comprehensive" — thêm bước outline refinement + critique pass).

## Setup từng bước
1. Cài qua CLI `skills` (chuẩn, dùng được với mọi tool support Agent Skills):
```
npx skills add https://github.com/samber/cc-skills --skill deep-research
```
2. Với Claude Code: `/plugin marketplace add samber/cc` rồi `/plugin install cc-skills@samber`
3. Với OpenClaw (agent của Nobitano dùng): clone thẳng vào thư mục discovery
```
git clone https://github.com/samber/cc-skills.git ~/.openclaw/skills/cc-skills
```
4. Không cần config gì thêm — agent tự detect qua `SKILL.md` frontmatter, cần WebSearch/WebFetch bật sẵn.

## Ví dụ thực tế
Input: "Research thị trường Fast Track dịch vụ sân bay ở Đông Nam Á, so ABTRIP với đối thủ."
→ Skill tự chọn research type "competitive" + "market", chạy Standard mode (5 bước): Step 1 scope (hỏi lại nếu prompt mơ hồ, còn prompt cụ thể thì tự suy ra assumption rồi ghi đầu báo cáo) → Step 2-4 fan-out sub-agent tìm data thị trường, đối thủ, giá → Step 5 dùng `ultrathink` để tổng hợp, đối chiếu nguồn mâu thuẫn.
Output: file Markdown, mỗi câu quan trọng có `[Source]`, phần nào thiếu dữ liệu ghi rõ "No sources found for X" thay vì đoán bừa.

## Lưu ý / Lỗi thường gặp
- Không có WebSearch → skill dừng ngay, báo lỗi thẳng chứ không cố research bằng trí nhớ (tránh bịa số).
- Cài chung với `deep-research` cũ trong kho (bản ECC dùng firecrawl/exa) sẽ **trùng tên slug** — đặt tên riêng khi cài local (`skills/deep-research-samber-cc/`) để tránh đè lên nhau, 2 skill này cơ chế khác nhau (1 cái dùng MCP, 1 cái dùng WebSearch thuần).
- Deep mode tốn token nhiều (báo cáo full có thể lên hơn 14k token nội dung skill + report dài) — chỉ bật khi thật sự cần báo cáo kỹ, đừng dùng default cho câu hỏi đơn giản.

## Đánh giá cá nhân
- Điểm mạnh: nguyên tắc "2+ nguồn độc lập mới tin" + "prose-first, không dump bullet" ra báo cáo đọc như research analyst thật viết, không giống AI liệt kê gạch đầu dòng vô hồn. Repo có bảng benchmark hẳn hoi: dùng skill giảm error rate 51% so với không dùng.
- Điểm yếu: không tích hợp MCP nào (Similarweb, Tavily...) nên chất lượng phụ thuộc hoàn toàn vào WebSearch built-in — nếu công cụ search yếu thì research cũng yếu theo. Cũng chưa có sẵn export ra file .docx/.pptx, phải tự nối thêm skill khác.
- Có nên dùng không: 8/10 — dùng thay hoặc dùng song song với deep-research cũ, hợp cho research-analytics-pro agent package trong kho.

## Link
- Repo: https://github.com/samber/cc-skills
- SKILL.md gốc: https://github.com/samber/cc-skills/blob/main/skills/deep-research/SKILL.md
- Directory tổng hợp: https://mcpservers.org/vi/agent-skills

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Skill này chạy trong agent harness (Claude Code/OpenClaw), không có REST API riêng.
# Hermes không gọi trực tiếp được — chỉ có thể clone repo về máy để OpenClaw dùng.
import urllib.request
url = "https://raw.githubusercontent.com/samber/cc-skills/main/skills/deep-research/SKILL.md"
content = urllib.request.urlopen(url).read().decode()
# Lưu về local để OpenClaw discover
with open("skills_local/deep-research-samber-cc/SKILL.md", "w") as f:
    f.write(content)
```

### OpenClaw
```bash
git clone https://github.com/samber/cc-skills.git ~/.openclaw/skills/cc-skills-deep-research
```

### Antigravity
```bash
git clone https://github.com/samber/cc-skills.git ~/.antigravity/skills/cc-skills
```
> ⚠️ Đặt tên thư mục khác skill `deep-research` cũ đang có trong kho — 2 skill trùng tên nhưng cơ chế khác nhau, tránh Antigravity nhầm lẫn khi tự match trigger.
