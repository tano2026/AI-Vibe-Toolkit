# KHOJ-ADAPTER.md — Content Pro

> Khác hẳn Chatwoot (phải tự dựng webhook server) — Khoj có sẵn tính năng
> **Custom Agent** đúng nghĩa: Persona + Tools + Knowledge Base + Output,
> tạo trực tiếp qua UI, không cần code/deploy gì. Đây là fit tự nhiên nhất
> trong các nền tảng đã thử (Mission Control/Chatwoot/Khoj) cho việc mang
> Content Pro ra ngoài Claude.ai.

## Khoj là gì (research thật, không suy đoán)

Mã nguồn mở, tự host được, 36.8k⭐ trên GitHub. "AI second brain" — chat với
bất kỳ LLM nào (gpt/claude/gemini/llama/qwen/mistral/deepseek), đọc tài
liệu riêng (PDF/Markdown/Notion/Word/org-mode), truy cập qua Browser/
Obsidian/Emacs/Desktop/Phone/**WhatsApp**. Tự host hoặc dùng cloud
(app.khoj.dev, có bản miễn phí không cần setup).

## Cách tạo Content Pro Agent trên Khoj (đúng quy trình chính thức)

```
1. Vào https://app.khoj.dev/agents (hoặc domain self-host tương ứng)
2. Bấm "+ Create Agent"
3. Điền các trường:

   PERSONA (= system prompt):
     Paste NGUYÊN VĂN nội dung agents/content-pro/system-prompt.md vào đây

   TOOLS (bật đúng cái Content Pro cần):
     ☑ Information retrieval từ notes/knowledge base (để đọc skill đã upload)
     ☑ Web search + page scraping (research chủ đề/trend khi xây Pillar)
     ☐ Internet access real-time (bật nếu cần tin tức mới nhất cho content
        thời sự, tắt nếu chỉ dùng knowledge base cố định)

   OUTPUT CAPABILITIES:
     ☑ Text response (bắt buộc)
     ☐ Image generation (bật nếu muốn Content Pro tự gợi ý visual/thumbnail
        concept — hiện Content Pro gốc không có skill làm việc này, để tắt)
     ☐ Diagram (không cần cho content strategy thuần)

   KNOWLEDGE BASE (đây là phần mạnh nhất của Khoj so với Chatwoot):
     Upload TRỰC TIẾP các file .md sau làm tài liệu tham khảo cho agent:
     - agents/content-pro/content-brand-playbooks.md
     - agents/content-pro/skills/content-pillar-cluster-architecture/SKILL.md
     - agents/content-pro/skills/editorial-workflow-quality-gates/SKILL.md
     - agents/content-pro/skills/content-distribution-system/SKILL.md
     - agents/content-pro/skills/content-strategy-review-gate/SKILL.md
     - (tuỳ chọn) skills/viral-hooks/SKILL.md, skills/brand-voice/SKILL.md,
       skills/content-engine/SKILL.md — các skill chiến thuật hay dùng nhất

   VISIBILITY:
     Private — chỉ Nobitano thấy (mặc định đúng, đừng để Protected/Public
     vì nội dung có brand/chiến lược nội bộ)

4. Chọn Chat Model: Claude (nếu Khoj instance đã cấu hình Anthropic API key)
5. Lưu agent — có link riêng dùng ngay (dạng app.khoj.dev/agents?agent=...)
```

## Vì sao Knowledge Base của Khoj tốt hơn cách "nhét tĩnh" ở Chatwoot/Hermes

Khoj tự làm **semantic search** trên tài liệu đã upload — không cần code
`load_skill()`/`fetch_skill_from_kho()` như Hermes Adapter phải tự viết.
Upload file 1 lần, Khoj tự tìm đúng đoạn liên quan khi cần, không phải nhét
toàn bộ 12 skill vào context mỗi lần hỏi (tiết kiệm token hơn cách Hermes
đang làm).

**Đánh đổi:** Knowledge Base là snapshot tại thời điểm upload — kho GitHub
cập nhật sau đó KHÔNG tự động phản ánh vào Khoj. Cần tái-upload thủ công
khi skill trong kho đổi, khác hẳn Hermes Adapter (luôn fetch bản mới nhất
qua API mỗi lần chạy).

## WhatsApp — điểm đáng chú ý riêng

Khoj access được qua WhatsApp trực tiếp — nếu Nobitano muốn hỏi Content Pro
ngay trên WhatsApp (thay vì mở Claude.ai/Khoj web), đây là kênh có sẵn,
không cần tự dựng như Chatwoot phải viết webhook riêng.

## Tự host hay dùng Cloud

| | Cloud (app.khoj.dev) | Self-host trên VPS |
|---|---|---|
| Setup | Không cần gì, đăng ký là dùng | Cần Antigravity deploy (Docker có sẵn theo `docker-compose.yml` của Khoj) |
| Dữ liệu | Trên server Khoj | Trên VPS riêng, kiểm soát hoàn toàn |
| Chi phí | Có gói free, gói trả phí nếu cần thêm | Chi phí VPS đã có sẵn, không phát sinh thêm |

Khuyến nghị bắt đầu bằng **Cloud** để test nhanh xem Content Pro hoạt động
tốt trên Khoj không, chỉ tự host sau nếu cần kiểm soát dữ liệu chặt hơn.

## Giới hạn thật (không giấu)

- Chưa test thật — đây là hướng dẫn dựa trên tài liệu chính thức Khoj, chưa tự tay tạo agent để xác nhận từng bước khớp UI thật 100%
- Model Claude cần Khoj instance đã cấu hình Anthropic API key riêng (không dùng chung con token Claude.ai hiện tại của Nobitano)
- Knowledge Base là snapshot tĩnh — cần quy trình nhắc tái-upload định kỳ nếu skill kho update thường xuyên

## Việc cần làm trước khi tin dùng thật

1. Nobitano tự vào app.khoj.dev tạo thử agent theo đúng 5 bước trên, xác nhận UI khớp
2. Test 1 câu hỏi thật (vd "xây pillar cho kênh Tano Cafe") xem Content Pro trên Khoj trả lời có đúng tinh thần system-prompt không
3. Nếu ổn — quyết định Cloud hay self-host dựa theo mức độ dùng thật
