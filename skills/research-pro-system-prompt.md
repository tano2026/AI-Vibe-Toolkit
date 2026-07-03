# Research Pro System Prompt — Prompt Template / System Prompt

## TL;DR
System prompt cho 1 agent nghiên cứu đa lĩnh vực (market/competitive/tech research) — bắt buộc gắn nhãn độ tin cậy từng câu, không bịa số, lộ công thức tính, nhớ research cũ qua Mem0, khung báo cáo 8 khối dùng lại được cho mọi domain.

## Khi nào dùng
Trigger khi cần: research thị trường, phân tích đối thủ, đánh giá tool/công nghệ (bao gồm research MCP/repo mới cho chính kho AI-Vibe-Toolkit), due diligence đối tác/nhà cung cấp. Dùng khi câu hỏi cần độ sâu — không dùng cho lookup nhanh 1 fact đơn giản.

## Nội dung skill / prompt
```
[Toàn bộ nội dung: xem file research-pro-v3-system-prompt.md đính kèm — paste thẳng vào
Project Instructions của Research Pro. Gồm: vai trò, 9 kỷ luật viết báo cáo (gắn nhãn
FACT/ƯỚC TÍNH/GIẢ THUYẾT từng câu, không có dữ liệu thì ghi rõ, lộ công thức tính, version
diff qua Mem0, ma trận định vị 2 trục, SWOT backlink bằng chứng, mục "không nên bắt chước",
bảng tin cậy theo từng phần, validate list ưu tiên theo chi phí/giá trị), khung 3 lớp
phương pháp luận (Thu thập → Đa chiều → Hành động) gắn với toolset thật (Tavily/Firecrawl/
Mem0/Opik/MarkItDown/Brave Search), khung báo cáo chuẩn 8 khối áp dụng đa domain.]
```

## Setup từng bước
1. Tạo 1 Claude Project riêng tên "Research Pro" (tách khỏi project AI-Vibe-Toolkit để tránh lẫn context)
2. Copy toàn bộ nội dung system prompt vào Project Instructions
3. Bật các MCP/tool cần: web_search, Tavily MCP, Firecrawl MCP, Mem0, Opik (nếu đã setup), MarkItDown
4. Test 1 câu hỏi research thật, kiểm tra output có đủ tag `[FACT]/[ƯỚC TÍNH]/[GIẢ THUYẾT]` và bảng tin cậy cuối bài không

## Ví dụ thực tế
Trước khi áp skill: hỏi "thị trường tool AI content automation VN thế nào" → agent trả đoạn văn chung chung, số liệu không rõ nguồn, confidence là 1 câu mơ hồ cuối bài.

Sau khi áp skill: agent trả báo cáo 8 phần, TAM tính ra công thức `1,5-3 triệu đơn vị × 2-4 triệu VNĐ/năm`, mỗi claim có tag nguồn, kết thúc bằng bảng tin cậy riêng từng phần + verdict rõ ràng "Tham gia/Không tham gia".

## Lưu ý / Lỗi thường gặp
- Agent có xu hướng bỏ tag khi báo cáo dài — cần nhắc lại trong prompt nếu thấy tái phát
- Ma trận định vị 2 trục chỉ nên dùng khi có ≥3 đối tượng so sánh, ép dùng với <3 đối tượng sẽ trông gượng
- Khung 8 khối không bắt buộc đủ cho mọi domain — domain nhỏ (vd đánh giá 1 tool đơn lẻ) chỉ cần 3-4 khối, ép đủ 8 sẽ lan man

## Đánh giá cá nhân
- Điểm mạnh: kỷ luật "không bịa, ghi rõ không có dữ liệu" là thứ hiếm — hầu hết AI report có xu hướng lấp đầy mọi mục dù không có info thật
- Điểm yếu: chưa test độ ổn định qua nhiều lần chạy (agent có tuân thủ đúng format 8 khối liên tục không, hay trôi dần theo hội thoại dài) — cần theo dõi thêm
- Có nên dùng không: 8/10 — đáng dùng ngay cho mọi research task nghiêm túc, chưa 10 vì thiếu benchmark thực tế qua nhiều batch

## Link
- Nguồn gốc: đúc kết từ pattern viết thật của 2 báo cáo mẫu (thị trường AI content automation VN H1/2026, phân tích cạnh tranh 100xtourism.com) — không lấy từ nguồn ngoài
