# Financial Services Plugins (Anthropic) — GitHub Repo

## TL;DR
Bộ plugin chính thức của Anthropic cho Claude Cowork/Claude Code — biến Claude thành chuyên gia tài chính theo từng vertical: investment banking, equity research, private equity, wealth management. Có cả plugin đối tác từ LSEG và S&P Global mang thẳng data tài chính thật vào Claude.

## Repo này dùng để làm gì
Mỗi plugin đóng gói sẵn skill + connector + slash command + sub-agent cho 1 nghiệp vụ tài chính cụ thể — không phải chatbot trả lời chung chung mà là công cụ ra deliverable thật: comps analysis, DCF model, LBO model dạng file Excel có công thức sống, báo cáo earnings, IC memo.

## Setup từng bước
1. Trong Claude Cowork: mở Customize → Add marketplace from GitHub → nhập `anthropics/financial-services`.
2. Cài plugin lõi trước (bắt buộc): `claude plugin install financial-analysis@claude-for-financial-services`
3. Cài thêm plugin theo vertical cần: `investment-banking`, `equity-research`, `private-equity`, `wealth-management`.
4. Slash command có sẵn sau khi cài: `/comps [company]`, `/dcf [company]`, `/earnings [company] [quarter]`, `/ic-memo`.
5. Cân nhắc thêm plugin đối tác (LSEG, S&P Global) nếu cần data tài chính trả phí chất lượng cao hơn nguồn miễn phí.

## Ví dụ thực tế
Nếu B2B Travel Platform sau này cần huy động vốn hoặc làm việc với nhà đầu tư, dùng `/ic-memo` để soạn nhanh bản ghi nhớ đầu tư nháp, hoặc `/comps` để so sánh định giá với các nền tảng travel-tech tương tự trước khi vào buổi pitch — tiết kiệm thời gian dựng model tài chính từ đầu.

## Lưu ý / Lỗi thường gặp
- **Đây là công cụ soạn thảo, không phải tư vấn đầu tư** — tài liệu chính thức ghi rõ: không đưa ra khuyến nghị đầu tư, không thực hiện giao dịch, mọi output cần người có chuyên môn review trước khi dùng thật.
- Phần lớn tính năng hướng tới nghiệp vụ tài chính chuyên sâu (fund admin, KYC, GP/LP accounting) — nếu chỉ cần phân tích cơ bản cho quyết định kinh doanh nhỏ, dùng 4 plugin cốt lõi là đủ, không cần cài hết marketplace.
- Cần Claude Cowork hoặc Claude Code, không chạy trên claude.ai chat thường.

## Đánh giá cá nhân
- Điểm mạnh: chính thức từ Anthropic, chất lượng cao, model Excel có công thức sống chứ không phải bảng tĩnh — tiết kiệm thời gian đáng kể cho ai cần làm việc với số liệu tài chính thường xuyên.
- Điểm yếu: phần lớn nghiệp vụ (IB, PE, fund admin) không khớp trực tiếp với hoạt động chính của Tano (travel, content, AI agency) — giá trị chỉ hiện rõ khi Tano cần gọi vốn hoặc phân tích tài chính sâu cho B2B Travel Platform.
- Có nên dùng không: 5/10 cho hoạt động hiện tại, tăng lên 8/10 nếu bước vào giai đoạn gọi vốn/đàm phán với nhà đầu tư cho B2B Travel Platform.

## Link
- Repo: https://github.com/anthropics/financial-services
- Docs: https://claude.com/docs/office-agents/fsi-plugins
