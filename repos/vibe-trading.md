# Vibe-Trading — GitHub Repo

## TL;DR
Personal AI trading agent — "one command empowers your agent with comprehensive trading capabilities." 15.9K stars, HKUDS (Hong Kong University), Python+FastAPI+React, MIT license. Multi-agent: ban phan tich, ban quant, ban quan tri rui ro. MCP server co san. Dang trending manh (3 thang dat 14.9K stars).

## Repo nay dung de lam gi
Trading thuong doi hoi: theo doi gia lien tuc, phan tich tin tuc, backtest chien luoc, quan tri rui ro — rat nhieu viec vua phai lam vua phai de y gia. Vibe-Trading bung thanh doi AI agent:

**Kien truc multi-agent:**
- **Research Agent:** Phan tich tin tuc, sentiment thi truong, macro data
- **Quant Agent:** Backtest chien luoc, tinh toan signal ky thuat (RSI, MACD, Bollinger...)
- **Risk Agent:** Quan tri rui ro, tinh position size, stop loss
- **Execution Agent:** (simulate hoac live) ra lenh mua/ban theo signal
- **Portfolio Agent:** Theo doi danh muc, P&L, rebalance

**Shadow Account (diem doc dao):** Chay simulate song song voi tai khoan that — thu nghiem chien luoc tren live data ma khong mat tien that truoc khi dung that.

**Ket noi du lieu:**
- Crypto: Binance, Coinbase, OKX
- Stock US: Alpaca, Interactive Brokers
- Stock VN: VNSTOCK (co ho tro rieng)
- Forex: (dang phat trien)
- News: NewsAPI, RSS feeds

## Setup tung buoc

```bash
# Cach 1: pip (nhanh nhat)
pip install vibe-trading-ai

# Khoi dong
vibe-trading init
vibe-trading start

# Cach 2: tu source
git clone https://github.com/HKUDS/Vibe-Trading
cd Vibe-Trading
pip install -r requirements.txt
python main.py
```

**Config agent trong `config.yaml`:**
```yaml
agents:
  research:
    enabled: true
    model: deepseek-v3  # hoac claude-sonnet, gpt-4o
    sources: [newsapi, rss, reddit]

  quant:
    enabled: true
    indicators: [RSI, MACD, BB, EMA]
    timeframes: [1h, 4h, 1d]

  risk:
    max_position_size: 0.1  # 10% portfolio
    max_drawdown: 0.05      # stop neu mat 5%
    stop_loss: 0.02         # 2% per trade

market:
  exchange: binance  # hoac alpaca, vnstock
  mode: shadow       # "shadow" de test, "live" de that

llm:
  provider: openrouter  # hoac openai, anthropic, omniroute
  model: deepseek/deepseek-chat
```

**Ket noi MCP voi Claude Code:**
```json
{
  "mcpServers": {
    "vibe-trading": {
      "command": "python",
      "args": ["-m", "vibe_trading_ai.mcp_server"]
    }
  }
}
```

## Vi du thuc te

**Scenario: Phan tich co phieu VN + signal trading**
```
Claude Code voi Vibe-Trading MCP:
"Phan tich VNM (Vinamilk) trong 30 ngay qua, cho tao tin hieu
 mua/ban dua tren RSI va MACD, kem quan tri rui ro"

→ Research Agent: lay lich su gia VNM tu VNSTOCK
→ Quant Agent: tinh RSI, MACD → RSI = 32 (oversold), MACD crossover
→ Risk Agent: position size 8% portfolio, stop loss -2%
→ Output: "BUY signal, entry 78,500, stop 76,930, target 83,000"

Shadow mode: thu nghiem 30 ngay khong mat tien
```

**Backtest chien luoc:**
```python
from vibe_trading_ai import VibeTradingAgent

agent = VibeTradingAgent(config="config.yaml")
results = agent.backtest(
    strategy="RSI_MACD_combo",
    symbol="VNM",
    start="2025-01-01",
    end="2026-01-01"
)
print(f"Return: {results.total_return:.1%}")
print(f"Sharpe: {results.sharpe_ratio:.2f}")
print(f"Max Drawdown: {results.max_drawdown:.1%}")
```

## Luu y / Loi thuong gap
- **KHONG PHAI tu van dau tu** — AI agent co the sai, luon co human oversight truoc khi trade that
- Shadow mode bat buoc truoc khi dung live — chay it nhat 1 thang simulate
- VNSTOCK data: free nhung co rate limit — them delay giua cac request
- Live trading (Binance, Alpaca) can API key co quyen trading — luu tru an toan, khong de trong code
- Risk management la quan trong nhat — max_drawdown va stop_loss phai set truoc

## Danh gia ca nhan
- Diem manh: Multi-agent thuat su hieu qua cho trading phuc tap; Shadow Account de test an toan; MCP server tich hop Claude Code muot; VNSTOCK ho tro; community active (Discord)
- Diem yeu: AI trading co the sai — khong bao gio bot 100%; can kien thuc co ban ve trading de dung hieu qua; live trading co rui ro that
- Co nen dung khong: **8/10** — Cho ai quan tam dau tu/trading va muon dung AI de ho tro phan tich. Dung Shadow mode de hoc va test, dung Live khi da hieu ro chien luoc. Khong dung de "de AI tu quyet dinh het".

## Agent Integration

### Hermes (Python)
```python
# Hermes goi Vibe-Trading API
import urllib.request, json

def get_trading_signal(symbol, timeframe="1d"):
    req = urllib.request.Request(
        "http://localhost:8080/api/v1/signal",
        data=json.dumps({"symbol": symbol, "timeframe": timeframe}).encode(),
        headers={"Content-Type": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req).read())

# signal = get_trading_signal("VNM")
# → {"action": "BUY", "confidence": 0.78, "entry": 78500, "stop": 76930}
```

### Antigravity (Deploy)
```bash
pip install vibe-trading-ai --break-system-packages
pm2 start "python -m vibe_trading_ai.server" --name vibe-trading
pm2 save
```

> ⚠️ LUON bat Shadow mode truoc, chi chuyen Live sau khi test ky. Khong de API key trading trong code.

## Link
- Repo: https://github.com/HKUDS/Vibe-Trading
- Website: https://vibetrading.wiki
- Docs: https://vibetrading.wiki/docs/
- PyPI: vibe-trading-ai
- License: MIT
- Stack: Python 3.11+, FastAPI, React 19
