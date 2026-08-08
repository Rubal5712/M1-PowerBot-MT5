# M1-PowerBot-MT5
Python-based MetaTrader 5 XAUUSD M1 algorithmic trading bot with multi-indicator signals, H4 trend confirmation, risk management, batch orders, and optional AI signals.
Yes. For the MT5 bot you uploaded, here is a complete **GitHub branding/package setup** based on the actual features in your code. 




```text
🤖 XAUUSD M1 MT5 trading bot | EMA • RSI • MACD • BB • ATR • H4 Trend • Risk Management • Optional AI Signals
```

---





 Project structure

I recommend:

```text
M1-PowerBot-MT5/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── src/
│   └── m1_power_bot.py
│
├── config/
│   └── config.example.py
│
└── docs/
    └── strategy.md
```



Subtitle

```markdown
### XAUUSD M1 Algorithmic Trading Bot for Educational & Demo Testing
```

---

 introduction

```markdown
M1 Power Bot is a Python-based algorithmic trading project designed for
MetaTrader 5 (MT5). The current strategy focuses on XAUUSD using the M1
signal timeframe with H4 higher-timeframe trend confirmation.

The bot combines multiple technical indicators and market conditions into
a composite trading score before generating a BUY or SELL decision.
```

---

  Features section

```markdown
## 🚀 Features

- 🥇 XAUUSD trading support
- ⏱️ M1 signal timeframe
- 🕐 H4 higher-timeframe trend confirmation
- 📈 EMA 12/26
- 📊 RSI 14
- 📉 MACD
- 🔵 Bollinger Bands
- 📐 ATR volatility calculation
- 📦 Tick-volume analysis
- 🕯️ Candlestick pattern detection
- 📍 Support/resistance analysis
- 🧮 Composite signal scoring
- 💰 Risk-based lot calculation
- 🛡️ Margin-aware position sizing
- 📦 Batch order execution
- 🎯 Configurable take-profit and stop-loss
- 📈 Configurable scale-in system
- 🔄 MT5 reconnection handling
- 🧠 Optional GPT-based signal integration
- ⚙️ Configurable trading parameters
```

These features correspond to the functionality present in your uploaded bot. 

---

 Strategy section

```markdown
## 🧠 Strategy Overview

The bot calculates a composite score using several market signals:

| Component | Purpose |
|---|---|
| H4 Trend | Higher-timeframe direction |
| EMA 12/26 | Short-term trend |
| RSI 14 | Momentum/overbought/oversold condition |
| MACD | Momentum confirmation |
| Bollinger Bands | Price-extreme detection |
| Tick Volume | Activity confirmation |
| Candlestick Patterns | Reversal confirmation |
| Support/Resistance | Price-level context |
| Optional GPT | Additional signal input |

A trade is considered only when the calculated score reaches the configured
minimum threshold and satisfies the higher-timeframe trend filter.
```

---
 Installation

````markdown
## 🛠️ Installation

### Requirements

- Python 3
- MetaTrader 5 desktop terminal
- MT5 trading account
- Windows environment recommended
- Python packages listed in `requirements.txt`

### Install dependencies

```bash
pip install -r requirements.txt
````

### Run

```bash
python m1_power_bot.py
```

````

---

 Configuration

```markdown
## ⚙️ Configuration

The strategy contains configurable parameters for:

- Trading symbols
- Signal timeframe
- Higher timeframe
- Risk percentage
- Profit target
- Stop-loss distance
- Take-profit distance
- Orders per batch
- Maximum lot size
- Maximum spread
- Scale-in distance
- Maximum batches
- Position multiplier
- Minimum signal score
- Optional AI signal integration
````



 Security section

```markdown
## 🔐 Security

Never commit sensitive credentials to GitHub.

Do NOT upload:

- MT5 passwords
- API keys
- OpenAI keys
- Account credentials
- Private configuration files

Use environment variables or a local configuration file that is excluded
from Git with `.gitignore`.
```

---

 Disclaimer

```markdown
## ⚠️ Disclaimer

This project is provided for educational purposes, algorithmic-trading
research, and demo-account testing.

Automated trading involves significant financial risk. Past performance,
backtesting results, or simulated results do not guarantee future results.

Use this software only on accounts and systems you are authorized to use.
The author is not responsible for financial losses or misuse of the software.
```

---

 Author section

```markdown
## 👨‍💻 Author

### Rubal Kumar

Cybersecurity | Python | Algorithmic Trading

GitHub: @Rubal5712
```

---


