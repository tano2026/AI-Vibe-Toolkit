# TradingAgents — Phòng Giao Dịch AI Đa-Agent (86k⭐)

**GitHub:** https://github.com/TauricResearch/TradingAgents
**Stars:** 86k⭐ | **License:** MIT | **Paper:** arXiv:2412.20138
**Version:** v0.2.5 | **Launch:** 12/2024
**Stack:** LangGraph + 11 LLMs | **Assets:** Cổ phiếu + Crypto

---

## Đây Là Gì

Framework đa-agent mô phỏng **phòng giao dịch thật** — nhiều AI chuyên trách cùng phân tích và tranh luận trước khi ra lệnh mua/bán.

```
Market Data
    ↓
┌─────────────────────────────────┐
│  Fundamental Analyst Agent      │ ← Phân tích cơ bản
│  Technical Analyst Agent        │ ← Phân tích kỹ thuật
│  Sentiment Analyst Agent        │ ← Phân tích tâm lý thị trường
│  News Analyst Agent             │ ← Phân tích tin tức
│  Social Media Analyst Agent     │ ← Reddit/Twitter signals
│  Risk Manager Agent             │ ← Quản lý rủi ro
│  Portfolio Manager Agent        │ ← Quyết định cuối cùng
└─────────────────────────────────┘
    ↓ Debate + consensus
 Trading Decision (Buy/Sell/Hold)
```

---

## Cài Đặt

```bash
git clone https://github.com/TauricResearch/TradingAgents
cd TradingAgents
pip install -r requirements.txt
cp .env.example .env
# Điền API keys

# Chạy
python main.py --ticker AAPL --date 2026-06-15
```

---

## Config (.env)

```bash
# LLM providers (chọn 1+)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...  # dùng Claude
GROQ_API_KEY=...              # free, fast

# Data sources
FINNHUB_API_KEY=...           # stock data (free tier)
ALPACA_API_KEY=...            # trading execution
ALPACA_SECRET_KEY=...

# Optional
REDDIT_CLIENT_ID=...          # sentiment analysis
```

---

## 11 LLMs Hỗ Trợ

```python
# Trong config.py
SUPPORTED_LLMS = [
    "gpt-4o", "gpt-4-turbo",           # OpenAI
    "claude-opus-4-6", "claude-sonnet-4-6",  # Anthropic
    "gemini-pro", "gemini-flash",       # Google
    "llama-3.1-70b", "mixtral-8x7b",   # Groq (free)
    "deepseek-v3",                      # DeepSeek
    "qwen-72b",                         # Alibaba
    "grok-2",                           # xAI
]

# Cost optimization: dùng Groq cho non-critical agents
config = {
    "fundamental_agent": "claude-opus-4-6",   # quan trọng nhất
    "technical_agent": "claude-sonnet-4-6",
    "sentiment_agent": "llama-3.1-70b",        # Groq free
    "news_agent": "llama-3.1-70b",             # Groq free
    "risk_manager": "claude-opus-4-6",         # critical
}
```

---

## Workflow Thực Tế

```bash
# Analyze 1 cổ phiếu
python main.py --ticker NVDA --date 2026-06-15

# Backtest
python backtest.py --ticker AAPL --start 2025-01-01 --end 2026-01-01

# Paper trading (không dùng tiền thật)
python trade.py --paper --ticker BTC-USD --interval 1h
```

---

## ⚠️ Cảnh Báo

TradingAgents là **research/educational tool** — không phải financial advisor.
- Backtest tốt ≠ future performance
- Không dùng tiền thật mà không hiểu rõ rủi ro
- Past performance không đảm bảo tương lai

---

## Đánh Giá Cá Nhân

86k stars, paper trên arXiv — nghiêm túc về mặt học thuật. Community lớn, active.

Điểm hay nhất: **debate mechanism** — các agents tranh luận với nhau trước khi quyết định. Tránh được single-agent bias.

Điểm cần chú ý: cần nhiều API keys (stock data, LLMs). Chi phí chạy real-time không nhỏ nếu dùng Claude cho tất cả agents.

**Rating: 8.5/10** — Xuất sắc cho research, cẩn thận khi dùng real money.

---
*Nguồn: github.com/TauricResearch/TradingAgents | 86k⭐ | MIT | tháng 6/2026*
