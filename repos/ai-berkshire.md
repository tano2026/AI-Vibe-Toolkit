# AI Berkshire — GitHub Repo

## TL;DR
Framework đầu tư giá trị dựa trên Claude Code — tổng hợp phương pháp của 4 nhà đầu tư huyền thoại (Buffett, Munger, Duan Yongping, Li Lu) thành agent chạy phân tích cổ phiếu. Thực chiến: +69% năm 2024, +66% năm 2025 YTD.

## Repo này dùng để làm gì
Thay vì đọc báo cáo tài chính hàng giờ, mày deploy agent AI phân tích theo đúng framework của các nhà đầu tư nổi tiếng:
- **Buffett:** Economic moat, earnings power, management quality
- **Munger:** Mental models, invert thinking, business quality
- **Duan Yongping:** Business model gốc rễ, consumer psychology
- **Li Lu:** Emerging market edge, contrarian value

Multi-agent parallel research: nhiều agent chạy cùng lúc từ nhiều góc độ, tổng hợp thành báo cáo đầu tư đầy đủ.

## Setup từng bước
```bash
# 1. Clone
git clone https://github.com/xbtlin/ai-berkshire
cd ai-berkshire

# 2. Cài dependencies
pip install -r requirements.txt

# 3. Setup Claude Code (bắt buộc — không chạy với ChatGPT)
# Cài Claude Code CLI: npm install -g @anthropic-ai/claude-code

# 4. Set API key
export ANTHROPIC_API_KEY=your_key

# 5. Chạy phân tích một công ty
claude code --skill skills/buffett-analysis.md --target "AAPL"

# 6. Full multi-agent research
python run_research.py --ticker AAPL --frameworks all
```

## Ví dụ thực tế
**Input:** Phân tích Apple (AAPL) theo framework Buffett + Munger

**Output:**
- Moat analysis: Brand + Ecosystem lock-in → Wide Moat
- Earnings power: $120B+ FCF/năm, tăng trưởng ổn định
- Management: Tim Cook = capital allocator xuất sắc (buyback kỷ lục)
- Khuyến nghị: Hold/Buy nếu P/E < 28x
- Red flags: China revenue risk, antitrust

## Lưu ý / Lỗi thường gặp
- **Chỉ chạy với Claude Code** — không compatible với GPT-4/Gemini
- Cần data tài chính (Yahoo Finance API hoặc Financial Modeling Prep) để phân tích số thực
- Framework phân tích của người Trung Quốc (Duan/Li Lu) thiên về market Trung Quốc — điều chỉnh nếu phân tích stock VN/US
- Không phải tư vấn đầu tư — dùng để research, quyết định cuối là của mày

## Đánh giá cá nhân
- Điểm mạnh: Track record thực (không phải backtest); phương pháp rõ ràng, có thể học được; multi-agent cho góc nhìn đa chiều
- Điểm yếu: Chỉ dùng được Claude Code; thiên về value investing (không phù hợp growth/momentum trading); market VN thiếu data tốt
- Có nên dùng không: **7/10** — Rất hay cho ai học value investing + muốn dùng AI để research. Không phải tool get-rich-quick.

## Link
- Repo: https://github.com/xbtlin/ai-berkshire
- Topics: warren-buffett, claude-code, value-investing, multi-agent, stock-analysis
