# Natural Writing — Chống văn phong "nghe như AI"

## TL;DR
Checklist cụ thể để sửa mọi đoạn text (script video, bài .md trong kho, caption, email) khỏi bị "mùi AI" — thay vì mấy lời khuyên chung chung kiểu "viết tự nhiên hơn", skill này chỉ thẳng từng pattern cụ thể + ví dụ Bad/Good.

## Skill này dùng để làm gì
LLM viết bị "lộ" vì nó luôn kéo về câu chữ trung bình — thay chi tiết cụ thể bằng ngôn ngữ chung chung nghe có vẻ quan trọng. Skill này liệt kê 15 pattern cụ thể gây ra chuyện đó và cách sửa từng cái. Không phải lý thuyết — mỗi mục có ví dụ Bad → Good rõ ràng, áp dụng được ngay vào bất kỳ đoạn text nào Hermes/Claude generate ra.

15 pattern chính (rút gọn):
1. **Cắt "significance inflation"** — bỏ "marking a pivotal moment", "reflecting the transformative power of" → nói thẳng sự việc
2. **Giết "trailing analysis"** — câu kết thúc bằng "...showcasing/underscoring/demonstrating X" → cắt, hoặc tách thành câu riêng có số liệu cụ thể
3. **Né từ vựng AI** — delve, tapestry, multifaceted, nuanced, leverage, pivotal, robust, seamless, nestled, renowned... → dùng từ ngắn, phổ thông hơn
4. **Dùng "is/are" thay vì "serves as/stands as/represents"**
5. **Bỏ "not only X but also Y"** kiểu văn hoa
6. **Phá "rule of three"** máy móc — không phải lúc nào cũng liệt kê đúng 3 cái
7. **Ngưng "elegant variation"** — lặp lại đúng từ thay vì đổi synonym liên tục (VD: cứ gọi "cây cầu" là "cây cầu", đừng đổi thành "công trình", "kết cấu")
8. **Đừng bịa "range" giả** — "from X to Y" chỉ dùng khi X-Y thực sự là 1 dải liên tục
9. **Hạn chế em-dash** — tối đa 1 cái/đoạn
10. **Cắt "it's important to note"** — nói thẳng luôn, không rào trước
11. **Đừng tóm tắt lại cái vừa nói** — kết thúc khi hết ý, không cần "In summary..."
12. **Tránh attribution mơ hồ** — "experts agree", "many have praised" → nêu tên cụ thể hoặc bỏ
13. **Đừng thổi phồng ngôn ngữ quảng cáo** — "nestled within breathtaking region" → mô tả sự thật, để người đọc tự cảm nhận
14. **Bỏ mục "Challenges and Future Prospects"** rập khuôn cuối bài nếu không có nội dung thật
15. **Đa dạng cấu trúc câu** — trộn câu ngắn/dài, không đều đều

## Setup từng bước
1. Copy toàn bộ nội dung checklist (file gốc, xem link bên dưới) vào system prompt/project instruction của Claude hoặc Hermes khi làm task viết
2. Sau khi Hermes/Claude generate xong 1 đoạn text — chạy lại qua "Quick Self-Check" cuối skill (7 câu hỏi tự kiểm) trước khi publish
3. Với script video Trùm Sân Bay/GMSP — áp dụng đặc biệt kỹ mục 1, 2, 3, 4 (đây là chỗ dễ lộ "mùi AI" nhất trong voiceover)

## Ví dụ thực tế
**Trước (script cho video ABTRIP về Fast Track):**
> "Fast Track không chỉ là một dịch vụ, mà còn là biểu tượng cho sự tận tâm của ABTRIP trong việc mang đến trải nghiệm sân bay liền mạch và đẳng cấp cho hành khách, phản ánh cam kết không ngừng nghỉ về chất lượng dịch vụ."

**Sau khi áp skill:**
> "Fast Track của ABTRIP đưa mày qua an ninh trong 5 phút, không phải xếp hàng 40 phút như bình thường."

Ngắn hơn, cụ thể hơn (5 phút vs 40 phút), không có từ "biểu tượng/đẳng cấp/liền mạch/cam kết" nào cả.

## Lưu ý / Lỗi thường gặp
- Áp dụng quá tay có thể làm câu văn cụt lủn, mất chất giọng thương hiệu — vẫn cần đọc lại bằng tai người, không chỉ chạy checklist máy móc
- Mục "bỏ elegant variation" đôi khi mâu thuẫn với yêu cầu SEO (cần đa dạng từ khóa) — với content SEO-driven thì cân nhắc linh hoạt
- Không thay thế được việc đọc to script trước khi thu voiceover ElevenLabs — checklist chỉ bắt được lỗi văn bản, không bắt được lỗi nhịp điệu khi đọc

## Đánh giá cá nhân
- Điểm mạnh: cụ thể, có ví dụ Bad/Good rõ ràng cho từng mục, áp dụng được ngay không cần setup gì, miễn phí 100%
- Điểm yếu: chỉ là 1 checklist tĩnh, không tự động hoá — vẫn phải người (hoặc Claude) tự rà lại bằng tay; không phân biệt được ngữ cảnh nào nên giữ văn phong "trang trọng" có chủ đích
- Có nên dùng không: 9/10 — impact cao, chi phí áp dụng gần như bằng 0, nên nhét thẳng vào system prompt content pipeline luôn

## Link
- Nguồn gốc skill: adapted từ [blader/humanizer](https://github.com/blader/humanizer) (MIT), qua bundle [Rylaispirit/rylai-codex-hermes-skills](https://github.com/Rylaispirit/rylai-codex-hermes-skills)
- Lưu ý: repo trung gian (Rylai bundle) có dấu hiệu sao/fork bất thường (39 sao/33 fork sau 3 ngày, push 1 lần) — nhưng nội dung skill này copy từ upstream `blader/humanizer` (đã ghi nguồn gốc trong PROVENANCE.yml của họ), nên đáng tin về mặt nội dung

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Không cần API — đây là system prompt text thuần, nhét thẳng vào
# request tới OmniRoute khi task có generate content

NATURAL_WRITING_CHECKLIST = """
[Dán toàn bộ nội dung 15 pattern ở trên vào đây]
"""

def build_content_prompt(task_prompt: str) -> str:
    return f"{NATURAL_WRITING_CHECKLIST}\n\n---\n\nTask: {task_prompt}"
```

### OpenClaw
```bash
# Thêm vào system prompt của content agent (marketing/media trong 9-agent pipeline)
# File: agents/marketing/system-prompt.md hoặc agents/media/system-prompt.md
# Append nội dung checklist vào cuối file, không cần MCP/tool riêng
```

### Antigravity
> Không cần deploy gì — đây là prompt-only skill, không có runtime dependency.
