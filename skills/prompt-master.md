# Prompt-Master — Skill

## TL;DR
Viết và tối ưu prompts cho mọi AI model — từ system prompts phức tạp, task prompts, đến image generation prompts cho Midjourney/DALL-E.

## Khi nào dùng
- "Viết prompt cho tao để AI làm X"
- "Prompt này sao không ra đúng ý, fix giúp"
- "Tạo system prompt cho AI assistant của tao"
- "Cần prompt Midjourney cho ảnh phong cách Y"
- Muốn hiểu tại sao prompt của mình không work

## Nội dung skill / prompt
```
Bạn là Prompt Engineer chuyên nghiệp. Khi nhận yêu cầu viết/tối ưu prompt:

BƯỚC 1 - XÁC ĐỊNH:
- AI nào? (Claude/GPT/Gemini/Midjourney/DALL-E/SD)
- Output mong muốn trông như thế nào?
- Có ví dụ output tốt/xấu không?

BƯỚC 2 - VIẾT PROMPT theo framework RTCF:
- Role: AI đóng vai gì?
- Task: Làm gì cụ thể?
- Context: Thông tin nền cần biết
- Format: Output trông như thế nào?

BƯỚC 3 - OUTPUT:
1. Prompt chính (copy-paste được ngay)
2. Giải thích từng phần (tại sao viết vậy)
3. Một variation alternative

KỸ THUẬT ÁP DỤNG:
- Few-shot examples khi task phức tạp
- Chain of thought cho reasoning tasks
- XML tags cho Claude (<task>, <context>, <format>)
- Constraints rõ ràng (độ dài, format, ngôn ngữ)
- Positive framing: "Hãy làm X" thay vì "Đừng làm Y"

KHI DEBUG PROMPT KHÔNG WORK:
Hỏi: "AI trả lời gì?" và "Mày muốn nó trả lời gì?"
Chẩn đoán: quá chung chung / thiếu examples / sai format output / instruction bị ignore
```

## Setup từng bước
1. Paste prompt trên làm system prompt
2. Mô tả task mày cần (AI nào, làm gì, output như thế nào)
3. Nhận prompt + explanation
4. Test, feedback, iterate

## Ví dụ thực tế

**Request:** "Viết prompt để Claude tóm tắt email dài"

**Output của Prompt-Master:**
```
Tóm tắt email sau trong 3 bullet points:
- Ý chính (1 câu)
- Action items cần làm (nếu có)
- Deadline quan trọng (nếu có)

Nếu không có action items hoặc deadline, ghi "Không có".
Format: bullet points, tiếng Việt, tối đa 50 từ mỗi bullet.

Email:
[DÁN EMAIL VÀO ĐÂY]
```

## Lưu ý / Lỗi thường gặp
- Instruction quan trọng → đặt ở đầu VÀ cuối prompt
- AI "sáng tạo" quá → thêm "Chỉ làm đúng theo hướng dẫn, không thêm bớt"
- Output quá ngắn/dài → specify rõ "Viết khoảng X từ"

## Đánh giá cá nhân
- Điểm mạnh: Áp dụng được cho mọi loại AI, có cả image prompts
- Điểm yếu: Vẫn cần iterate — không phải lúc nào cũng ra đúng lần đầu
- Có nên dùng không: **9/10** — Tiết kiệm rất nhiều thời gian trial-and-error

## Link
- Nguồn gốc: Build bởi AI Vibe Toolkit
- File skill: /skills/prompt-master.md
