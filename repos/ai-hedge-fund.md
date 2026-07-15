# AI Hedge Fund — GitHub Repo

## TL;DR
Proof-of-concept 1 "quỹ đầu tư ảo" chạy bằng nhiều AI agent, mỗi agent mô phỏng phong cách đầu tư của 1 nhà đầu tư nổi tiếng (Warren Buffett, Cathie Wood, Michael Burry...) rồi tổng hợp lại thành quyết định giao dịch. 61k+ star, MIT license. Tác giả ghi rõ: chỉ để **học/nghiên cứu**, không dùng để giao dịch/đầu tư thật.

## Repo này dùng để làm gì
Đây là 1 hệ multi-agent minh hoạ cách kết hợp nhiều "góc nhìn" đầu tư khác nhau vào 1 quyết định cuối. Có khoảng 13 agent theo phong cách nhà đầu tư nổi tiếng (mỗi agent áp 1 triết lý riêng: Ben Graham = value investing an toàn, Cathie Wood = growth/disruption, Michael Burry = contrarian deep value...), cộng thêm các agent chuyên môn: Valuation Agent (định giá nội tại), Sentiment Agent (tâm lý thị trường), Fundamentals/Technicals Agent (phân tích cơ bản/kỹ thuật), Risk Manager (giới hạn rủi ro), và Portfolio Manager (ra quyết định cuối, tạo lệnh). Dự án đang được viết lại để trở thành 1 "fund" persistent — backtest được, paper-trade được, và tuỳ chọn chạy live.

## Setup từng bước
1. Clone repo:
   ```bash
   git clone https://github.com/virattt/ai-hedge-fund.git
   cd ai-hedge-fund
   ```
2. Cần API key cho LLM (OpenAI/Anthropic/tuỳ chọn) và nguồn dữ liệu tài chính (project dùng data provider riêng, xem README phần setup key cụ thể).
3. Cấu hình `.env` theo mẫu `.env.example` trong repo.
4. Chạy theo hướng dẫn cụ thể trong README (thường qua Python/Poetry) để backtest trên dữ liệu lịch sử — KHÔNG kết nối tài khoản giao dịch thật khi mới thử.
5. Đọc thêm `VISION.md` và `ROADMAP.md` trong repo để hiểu hướng phát triển thành "fund" persistent.

## Ví dụ thực tế
Muốn học cách thiết kế 1 hệ multi-agent có "nhiều chuyên gia tranh luận rồi 1 người ra quyết định
cuối" (đúng pattern Orchestrator + Sub-agents đã dùng cho `research-analytics-pro` trong kho) →
đọc cách repo này tách Valuation/Sentiment/Risk/Portfolio Manager thành các vai trò riêng biệt,
áp dụng ý tưởng kiến trúc này sang domain khác (không nhất thiết phải là tài chính).

## Lưu ý / Lỗi thường gặp
- Tác giả ghi rất rõ: dự án **chỉ cho mục đích học tập**, không phải công cụ đầu tư thật — không
  nên kết nối vốn thật hay coi khuyến nghị của agent là lời khuyên tài chính.
- Dự án đang trong giai đoạn "rebuilding" sang mô hình fund persistent — code hiện tại có thể
  thay đổi cấu trúc lớn trong thời gian tới, không nên build phụ thuộc sâu vào API hiện tại.
- Cần data tài chính thật (giá cổ phiếu, báo cáo tài chính) để chạy đầy đủ — không tự có sẵn,
  phải tự kết nối nguồn dữ liệu.

## Đánh giá cá nhân
- Điểm mạnh: ví dụ rất trực quan cho pattern "multi-agent với nhiều persona chuyên môn tranh
  luận, có 1 agent tổng hợp quyết định cuối" — dễ học, dễ mượn kiến trúc áp cho domain khác.
- Điểm yếu: đây là proof-of-concept giáo dục, không phải sản phẩm production — nếu tính đến
  chuyện tự động hoá quyết định tài chính thật thì rủi ro rất cao và không phù hợp mục đích
  ban đầu của tác giả.
- Có nên dùng không: 7/10 cho mục đích học kiến trúc multi-agent; không khuyến khích dùng để ra
  quyết định đầu tư thật dưới bất kỳ hình thức nào — kể cả tao (Claude) cũng không đưa lời
  khuyên đầu tư cụ thể, chỉ mô tả kiến trúc repo một cách khách quan.

## Link
- Repo: https://github.com/virattt/ai-hedge-fund
- Vision/Roadmap: file `VISION.md` và `ROADMAP.md` trong repo
