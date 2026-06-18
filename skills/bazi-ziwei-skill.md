# Bazi-Ziwei Skill — Prompt Template / System Prompt

## TL;DR
Skill chuẩn SKILL.md cho Claude Code/Hermes/OpenClaw luận Bát Tự + Tử Vi — không để LLM tự đoán lá số (hay sai), có engine tính riêng, xuất luôn ra poster HTML phong cách thủy mặc đẹp để đăng content. 317⭐, MIT.

## Khi nào dùng
Khi muốn Claude/Hermes/OpenClaw trả lời câu hỏi kiểu "xem bát tự/tử vi giúp tôi" mà KHÔNG để LLM tự bốc số tính tay (LLM tính bát tự/tử vi rất dễ sai ngày trụ, sai cách cục vì đây là phép tính lịch phức tạp). Skill này tách rõ: phần tính toán giao cho thuật toán xác định (không phải LLM đoán), phần phân tích/luận giải mới giao cho LLM.

## Nội dung skill / prompt
Cấu trúc skill:
```
bazi-ziwei-skill/
├── SKILL.md                       Skill chính (Agent đọc file này)
├── calculator/
│   ├── run-chart.ts               Sinh thời → JSON lá số
│   ├── dump-text.ts               JSON → bản text dễ đọc
│   ├── render.ts                  JSON + phân tích + template → 1 file HTML
│   ├── yiqi-core/                 Lõi thuật toán lập lá số (vendor từ Yiqi, MIT)
│   └── bazi-enrich/               Lớp bổ sung: cách cục/vượng suy/điều hậu/hình xung hợp hại
├── prompts/                       4 prompt cho 4 kiểu phân tích (bát tự riêng / tử vi riêng / song kiểm dạng văn / dạng poster JSON)
├── templates/report-zonghe-poster.html   Template poster
└── examples/                      Lá số mẫu (không phải người thật) để test thử
```
3 chế độ phân tích: Bát Tự độc lập / Tử Vi độc lập / Bát Tự + Tử Vi đối chứng song kiểm (2 hệ độc lập đối chiếu kết quả, xem có khớp trục chính không).

## Setup từng bước
1. `git clone https://github.com/dzcmemory-web/bazi-ziwei-skill.git`
2. `cd bazi-ziwei-skill/calculator && npm install` (chỉ cần Node >=18, phụ thuộc duy nhất là `lunar-typescript`)
3. Copy cả thư mục skill vào đúng folder skills của agent đang dùng:
   - Claude Code/Desktop: `~/.claude/skills/bazi-ziwei/`
   - Hermes Agent: `~/.hermes/skills/bazi-ziwei/`
   - OpenClaw: thư mục skills riêng / cài qua ClawHub local
4. Agent tự đọc `SKILL.md`, không cần config gì thêm
5. Test thử không qua Agent (chạy thẳng CLI):
```bash
cd calculator
node dist/run-chart.js --year=2000 --month=1 --day=1 --hour=12 --minute=0 --gender=male > chart.json
node dist/dump-text.js --input=chart.json --output=chart.txt
node dist/render.js --chart=chart.json --analysis=analysis.json --template=../templates/report-zonghe-poster.html --output=report.html --currentYear=2026
```

## Ví dụ thực tế
Gõ với agent đã gắn skill: "Tôi sinh 12h trưa ngày 1/1/2000, nam, xem giúp tôi"
→ Agent hỏi lại muốn xem kiểu gì (Bát Tự / Tử Vi / song kiểm), nếu chọn song kiểm thì hỏi tiếp muốn bài dài hay poster ảnh
→ Agent gọi engine tính toán ra JSON chuẩn → load đúng prompt → trả bài phân tích hoặc render ra 1 file HTML poster phong cách thủy mặc, có đủ 12 cung tử vi + tứ trụ bát tự + bảng đối chứng 6 chiều, chụp màn hình share thẳng lên TikTok/Threads được luôn.

So sánh trước/sau: trước khi có skill, hỏi Claude trực tiếp "bát tự tôi là gì" → Claude tự bốc lịch, dễ sai trụ ngày vì phép quy đổi âm-dương lịch + tiết khí rất dễ lệch khi LLM tính tay. Có skill → ngày trụ luôn đúng vì máy tính, LLM chỉ lo phần diễn giải.

## Lưu ý / Lỗi thường gặp
- README ghi rõ disclaimer: chỉ phục vụ nghiên cứu văn hoá/giải trí, không phải cơ sở cho quyết định y tế/đầu tư/hôn nhân/pháp lý — nên giữ đúng disclaimer này khi đưa vào bất kỳ content/sản phẩm nào để tránh hiểu nhầm.
- Toàn bộ tính toán chạy local, không cần internet — phù hợp deploy trên VPS không cần lo lộ data sinh nhật người dùng ra ngoài.
- Bản poster yêu cầu LLM trả đúng format JSON nghiêm ngặt để nhồi vào template — nếu đổi sang model yếu hơn dễ bị lỗi parse, nên test kỹ với model đang dùng trước khi đưa vào production.

## Đánh giá cá nhân
- Điểm mạnh: đúng pattern "tách tính toán khỏi LLM" — pattern này rất nên học để áp dụng cho mọi skill cần độ chính xác cao (không chỉ tử vi); compatible thẳng với Hermes + OpenClaw, không cần chuyển đổi gì; ra được poster đẹp luôn, tiết kiệm công đoạn làm thumbnail riêng.
- Điểm yếu: phụ thuộc lõi tính toán từ 1 repo khác (Yiqi) ít người biết, nếu repo gốc đó archive/bỏ maintain thì cần tự fork giữ lại; setup hơi nhiều bước hơn so với 1 MCP gắn thẳng.
- Có nên dùng: 8/10 — pick này nếu mục tiêu chính là content (poster đẹp để đăng), pick taibu-mcp nếu mục tiêu là tra cứu nhanh nhiều hệ thống cùng lúc.

## Link
- Nguồn gốc skill: https://github.com/dzcmemory-web/bazi-ziwei-skill
- Lõi thuật toán gốc: https://github.com/fdxuyq/Yiqi-BaZi-ZiWei (MIT)
