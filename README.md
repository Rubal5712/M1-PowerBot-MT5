🤖 M1 PowerBot – AI-Enhanced MetaTrader 5 Scalping Bot

Automated M1 Technical-Analysis & Risk-Management Trading System

"Python" (https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
"MetaTrader 5" (https://img.shields.io/badge/MetaTrader-5-blue?style=for-the-badge)
"Trading" (https://img.shields.io/badge/Trading-Automated-orange?style=for-the-badge)
"AI" (https://img.shields.io/badge/AI-Optional-purple?style=for-the-badge)
"Risk Management" (https://img.shields.io/badge/Risk-Management-red?style=for-the-badge)
"License" (https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

M1 PowerBot is a Python-based automated trading system designed for MetaTrader 5 (MT5) and short-term M1 market analysis.

The bot combines multiple technical indicators, candlestick and price-action concepts, support/resistance analysis, higher-timeframe trend confirmation, position sizing, spread filtering, and optional AI-assisted market sentiment analysis.

The project is designed primarily as an educational algorithmic-trading and quantitative-research project.

«⚠️ IMPORTANT: Automated trading involves substantial financial risk. This software does not guarantee profits. Always test with a demo account before considering any real-money deployment. Never trade money you cannot afford to lose.»

---

📖 Table of Contents

- "🤖 About the Project" (#-about-the-project)
- "🎯 Project Objectives" (#-project-objectives)
- "❓ Why M1 PowerBot" (#-why-m1-powerbot)
- "⚙️ How the Bot Works" (#️-how-the-bot-works)
- "📊 Technical Indicators" (#-technical-indicators)
- "🧠 Composite Signal Scoring" (#-composite-signal-scoring)
- "📈 Higher-Timeframe Trend Filter" (#-higher-timeframe-trend-filter)
- "📦 Batch Orders" (#-batch-orders)
- "🔄 Scaling-In Strategy" (#-scaling-in-strategy)
- "💰 Position Sizing" (#-position-sizing)
- "🎯 Take-Profit Management" (#-take-profit-management)
- "🛡️ Risk Management" (#️-risk-management)
- "🚨 Important Risk Warning" (#-important-risk-warning)
- "🛠️ Technologies" (#️-technologies)
- "🏗️ Project Architecture" (#️-project-architecture)
- "⚙️ Configuration" (#️-configuration)
- "📥 Installation" (#-installation)
- "🐍 Python Environment" (#-python-environment)
- "▶️ Running the Bot" (#️-running-the-bot)
- "🧪 Testing Methodology" (#-testing-methodology)
- "📸 Five Screenshots" (#-five-screenshots)
- "📊 Example Workflow" (#-example-workflow)
- "🔐 API Key Security" (#-api-key-security)
- "🖥️ MetaTrader 5 Requirements" (#️-metatrader-5-requirements)
- "☁️ VPS Considerations" (#️-vps-considerations)
- "📚 Learning Outcomes" (#-learning-outcomes)
- "🚀 Future Improvements" (#-future-improvements)
- "⚠️ Limitations" (#️-limitations)
- "🏆 Skills Demonstrated" (#-skills-demonstrated)
- "📌 Project Information" (#-project-information)
- "👨‍💻 Author" (#-author)
- "⭐ Support" (#-support)
- "⚠️ Final Disclaimer" (#️-final-disclaimer)
- "📜 License" (#-license)

---

🤖 About the Project

M1 PowerBot is an automated trading bot built with Python and MetaTrader 5.

The project focuses on short-term market analysis using the 1-minute timeframe (M1) while using a higher timeframe to provide additional trend context.

The system can combine several technical-analysis components:

- EMA
- RSI
- MACD
- Bollinger Bands
- ATR
- Volume analysis
- Candlestick/price-action concepts
- Support and resistance
- Higher-timeframe trend confirmation
- Spread filtering
- Position sizing
- Batch order management
- Optional AI-assisted sentiment analysis

Instead of relying on a single indicator, the bot uses a composite scoring approach to evaluate multiple market conditions.

The project is intended for learning about:

- Algorithmic trading
- Quantitative analysis
- Python automation
- MT5 integration
- Technical indicators
- Risk management
- Trading-system design

---

🎯 Project Objectives

The main objectives of M1 PowerBot are:

1. Automate technical-analysis workflows.
2. Reduce emotional decision-making.
3. Combine multiple indicators into a composite signal.
4. Confirm short-term signals using a higher timeframe.
5. Automate position-size calculations.
6. Implement configurable risk controls.
7. Demonstrate automated MT5 order management.
8. Explore scaling-in strategies.
9. Experiment with optional AI-assisted analysis.
10. Provide a foundation for algorithmic-trading research.

The project should be treated as a research and educational system, not as a guaranteed-profit trading solution.

---

❓ Why M1 PowerBot?

Manual M1 scalping can be challenging because market conditions can change very quickly.

A human trader may experience:

- Fear
- Greed
- Hesitation
- Overtrading
- Revenge trading
- Inconsistent position sizing
- Emotional exits

Automation can help make a predefined strategy more consistent.

However, automation does not remove market risk.

A trading bot can execute a bad strategy faster than a human.

Therefore, strategy validation, risk management, testing, and monitoring remain essential.

---

⚙️ How the Bot Works

The general workflow is:

                    ┌──────────────────────┐
                    │   MetaTrader 5       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Market Data / Candles │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Technical Indicators │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
           EMA/RSI          MACD/ATR        BB/Volume
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Composite Score      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ H4 Trend Confirmation │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Risk / Spread Checks │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Order Management     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Position Monitoring  │
                    └──────────────────────┘

---

📊 Technical Indicators

M1 PowerBot can use multiple indicators to evaluate market conditions.

EMA 12 / EMA 26

The Exponential Moving Average is used to identify short-term trend direction.

Example:

EMA12 > EMA26

can represent bullish momentum.

Conversely:

EMA12 < EMA26

can represent bearish momentum.

---

RSI

The Relative Strength Index can be used to identify momentum and potentially overbought/oversold conditions.

Example configuration:

RSI Period: 14
Oversold: 30
Overbought: 70

RSI should not be treated as a standalone buy/sell signal.

---

MACD

MACD can help evaluate momentum and trend changes.

Typical parameters:

Fast EMA: 12
Slow EMA: 26
Signal: 9

---

Bollinger Bands

Bollinger Bands can help evaluate price volatility and relative price position.

Typical configuration:

Period: 20
Standard Deviation: 2

---

ATR

Average True Range measures market volatility.

ATR can be useful for understanding whether current market conditions are relatively quiet or volatile.

---

Volume

Volume information can provide additional market-activity context.

The bot can compare current volume against a moving average to determine whether activity is elevated.

---

🧠 Composite Signal Scoring

One of the main concepts in M1 PowerBot is combining multiple indicators into a single score.

A simplified example:

EMA12 > EMA26                 +0.3
RSI Oversold                  +0.4
Lower Bollinger interaction   +0.3
High volume + rising price    +0.2
------------------------------------
Total                         +1.2

A negative score can represent bearish conditions.

For example:

EMA12 < EMA26                 -0.3
RSI Overbought                -0.4
Upper Bollinger interaction   -0.3
High volume + falling price   -0.2
------------------------------------
Total                         -1.2

The configured threshold determines whether the score is strong enough for further evaluation.

Example:

MIN_SCORE_TO_TRADE = 0.5

The scoring system is a research mechanism and does not guarantee that the resulting signal will be profitable.

---

📈 Higher-Timeframe Trend Filter

The bot can use an H4 trend filter to provide broader market context.

Example:

Signal Timeframe → M1
Trend Timeframe  → H4

A simplified decision process:

M1 Signal = BUY
        │
        ▼
Check H4 Trend
        │
        ├── Bullish → Continue evaluation
        │
        └── Strong Bearish → Reject/avoid BUY

The purpose is to reduce trades that strongly conflict with the broader trend.

---

📦 Batch Orders

When a valid signal is generated, the bot can place multiple orders as a batch.

Example:

ORDERS_PER_BATCH = 3

Conceptually:

BUY
 ├── Order 1
 ├── Order 2
 └── Order 3

Batch size should be configured carefully because multiple orders increase total exposure.

---

🔄 Scaling-In Strategy

M1 PowerBot can support a scaling-in approach.

If the market moves against an existing position by a configured distance, the system can consider adding another batch.

Example:

Initial Batch
     │
     ▼
Price moves against position
     │
     ▼
Scale-in distance reached
     │
     ▼
Next batch considered

The bot can use a configurable multiplier for subsequent batches.

Example:

MARTINGALE_MULTIPLIER = 1.5

⚠️ Important

Scaling-in and martingale-style position increases can significantly increase risk.

A market can continue moving against the position for much longer than expected.

Therefore, maximum batch limits and account-level risk controls are essential.

---

💰 Position Sizing

The bot can calculate position size based on available account information and configured risk parameters.

Example configuration:

RISK_PERCENT_PER_BATCH = 0.5

A lower risk percentage generally reduces exposure compared with aggressive settings.

Position sizing should also respect:

- Broker minimum lot
- Broker maximum lot
- Lot step
- Available margin
- Maximum configured lot
- Existing exposure

---

🎯 Take-Profit Management

The bot can monitor the combined profit of its managed positions.

Example:

TARGET_PROFIT_PER_BATCH = $100

Conceptually:

Position 1   +$30
Position 2   +$35
Position 3   +$40
-------------------
Total        +$105

When the configured basket target is reached, the system can close the managed positions.

The exact behavior depends on the implementation.

---

🛡️ Risk Management

Risk management is one of the most important components of an automated trading system.

Possible controls include:

Risk Percentage

Controls the amount of account balance allocated to a trading batch.

Maximum Lot

Prevents position size from exceeding a configured limit.

Maximum Batches

Limits the number of scale-in stages.

Stop Loss

Provides a predefined loss-exit mechanism.

Take Profit

Defines a profit target.

Spread Filter

Prevents trading when transaction costs become excessive.

Margin Protection

Helps prevent excessive use of available margin.

Higher-Timeframe Filter

Can reduce trades that conflict with broader market direction.

---

🚨 Important Risk Warning

The original configuration may contain aggressive parameters.

For example:

RISK_PERCENT_PER_BATCH = 4.0

can expose a significant portion of an account to a single trading batch.

For initial demo testing, a much smaller experimental value such as:

RISK_PERCENT_PER_BATCH = 0.5

or:

RISK_PERCENT_PER_BATCH = 1.0

may be more appropriate, depending on the research objective.

Do not assume that a low percentage automatically makes a strategy safe.

Scaling-in and martingale-style approaches can create rapidly increasing exposure.

---

🛠️ Technologies

Technology| Purpose
Python| Main programming language
MetaTrader 5| Trading platform and market interface
MetaTrader5 Python API| MT5 communication
pandas| Market-data processing
NumPy| Numerical calculations
Technical indicators| Market analysis
Optional AI API| Sentiment/analysis experimentation

---

🏗️ Project Architecture

M1PowerBot/
│
├── Market Data
│       │
│       ▼
├── Indicator Engine
│       │
│       ├── EMA
│       ├── RSI
│       ├── MACD
│       ├── Bollinger Bands
│       ├── ATR
│       └── Volume
│
├── Signal Engine
│       │
│       ▼
├── Composite Score
│       │
│       ▼
├── H4 Trend Filter
│       │
│       ▼
├── Risk Manager
│       │
│       ├── Lot Size
│       ├── Spread
│       ├── Margin
│       └── Exposure
│
├── Order Manager
│       │
│       ▼
└── Position Monitor

---

⚙️ Configuration

Configuration is typically located in the configuration section of the main Python file.

Parameter| Description
"SYMBOLS"| Instruments monitored/traded
"SIGNAL_TIMEFRAME"| Signal-generation timeframe
"HIGHER_TF"| Higher-timeframe trend filter
"RISK_PERCENT_PER_BATCH"| Risk allocation per batch
"TARGET_PROFIT_PER_BATCH"| Basket profit target
"FIXED_SL_POINTS"| Stop-loss distance
"FIXED_TP_POINTS"| Take-profit distance
"ORDERS_PER_BATCH"| Orders opened per batch
"MAX_LOT_PER_ORDER"| Maximum lot per order
"SCALE_IN_POINTS"| Distance before considering another batch
"MAX_BATCHES"| Maximum number of batches
"MARTINGALE_MULTIPLIER"| Subsequent batch-size multiplier
"MIN_SCORE_TO_TRADE"| Minimum composite score
"USE_OPENAI"| Enables optional AI analysis
"API_KEY"| Optional AI API credential
"MT5_LOGIN"| MT5 account login
"MT5_PASSWORD"| MT5 account password
"MT5_SERVER"| MT5 broker server

---

📥 Installation

1. Clone the Repository

git clone https://github.com/Rubal5712/M1PowerBot.git

Enter the directory:

cd M1PowerBot

---

2. Create a Virtual Environment

python -m venv venv

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

---

3. Install Dependencies

python -m pip install --upgrade pip

Then:

pip install -r requirements.txt

---

🐍 Python Environment

Recommended:

Python 3.10+

Check Python:

python --version

Check installed packages:

pip list

---

🖥️ MetaTrader 5 Requirements

Before running the bot, make sure:

- MetaTrader 5 is installed.
- Your broker account is available.
- The required trading symbol is available.
- Market data is accessible.
- The Python MT5 package is installed.
- The account is configured correctly.
- Automated trading is enabled where required.

For development and testing, use a demo account.

---

▶️ Running the Bot

After configuring the project:

python m1powerbotmt5.py

If your repository uses another entry-point filename, run that file instead.

A typical startup sequence should verify:

Connecting to MetaTrader 5...
Account connected
Symbol available
Market data available
Risk configuration loaded
Bot started

Do not expose account credentials in terminal screenshots, GitHub commits, logs, or documentation.

---

🧪 Testing Methodology

A professional testing process should be completed before considering live deployment.

Test 1 — Connection

Verify that Python successfully communicates with MT5.

---

Test 2 — Market Data

Confirm that the required symbol provides valid M1 and H4 candle data.

---

Test 3 — Indicator Calculation

Verify that EMA, RSI, MACD, Bollinger Bands, ATR, and volume calculations return valid values.

---

Test 4 — Signal Generation

Use historical or demo-market data to verify that composite scores are calculated correctly.

---

Test 5 — Risk Calculation

Confirm:

- Lot-size calculation
- Maximum lot restriction
- Batch limits
- Margin checks
- Spread filtering

---

Test 6 — Order Management

Use a demo account to verify that orders are handled correctly.

---

Test 7 — Position Monitoring

Confirm that open positions are tracked correctly.

---

Test 8 — Shutdown

Stop the bot and verify that the program terminates cleanly.

---

📸 Five Screenshots

Create:

screenshots/
├── 01-project-structure.png
├── 02-mt5-connection.png
├── 03-indicator-analysis.png
├── 04-trading-signal.png
└── 05-demo-results.png

---

📸 Screenshot 1 — Project Structure

Show the complete M1 PowerBot project in VS Code.

Caption:

«Figure 1: M1 PowerBot project structure showing the Python source code, configuration, dependencies, documentation, and screenshots.»

![Project Structure](screenshots/01-project-structure.png)

---

📸 Screenshot 2 — MT5 Connection

Show the terminal demonstrating a successful connection to the MetaTrader 5 demo environment.

Example:

MetaTrader 5 initialized
Connection successful
Symbol: XAUUSD
Timeframe: M1

Never show account passwords or private credentials.

![MT5 Connection](screenshots/02-mt5-connection.png)

---

📸 Screenshot 3 — Indicator Analysis

Show the bot calculating its indicators.

Example:

EMA12: ...
EMA26: ...
RSI: ...
MACD: ...
ATR: ...
Volume: ...

Caption:

«Figure 3: Technical-indicator analysis used by the M1 PowerBot signal engine.»

![Indicator Analysis](screenshots/03-indicator-analysis.png)

---

📸 Screenshot 4 — Trading Signal

Show an educational/demo signal generated by the composite scoring system.

Example:

Signal Analysis
---------------
EMA       +0.30
RSI       +0.40
BB        +0.30
Volume    +0.20
---------------
Score     +1.20

H4 Trend: Bullish
Decision: BUY

![Trading Signal](screenshots/04-trading-signal.png)

---

📸 Screenshot 5 — Demo Results

Show the demo-account results or trading dashboard.

Recommended information:

Demo Account
Trades
Profit/Loss
Open Positions
Batch Number
Risk Status

Do not publish account credentials.

![Demo Results](screenshots/05-demo-results.png)

---

📊 Example Workflow

A simplified example:

1. Fetch M1 candles
       ↓
2. Calculate indicators
       ↓
3. Generate composite score
       ↓
4. Check H4 trend
       ↓
5. Check spread
       ↓
6. Check risk/margin
       ↓
7. Generate trade decision
       ↓
8. Open demo position/batch
       ↓
9. Monitor exposure
       ↓
10. Manage basket
       ↓
11. Close according to configured rules

---

🔐 API Key Security

If optional AI functionality is enabled, never hard-code API credentials into source code.

❌ Avoid

API_KEY = "your-real-api-key"

Do not commit real credentials to GitHub.

✅ Recommended

Use environment variables or a local configuration file excluded through ".gitignore".

Example:

OPENAI_API_KEY=your_key_here

Add sensitive files to:

.gitignore

Example:

.env
config.local.py
secrets.json

If an API key has accidentally been uploaded to GitHub, revoke and replace it immediately.

---

☁️ VPS Considerations

A VPS can be useful for legitimate 24/7 demo testing because automated trading systems depend on stable connectivity.

Potential benefits include:

- Continuous uptime
- Stable internet
- Reduced local-PC interruptions
- Automated monitoring

However, a VPS does not make a trading strategy profitable or safe.

Always monitor:

- CPU usage
- RAM
- MT5 connection
- Network connectivity
- Bot logs
- Account exposure

---

📚 Learning Outcomes

This project provides practical experience with:

- Python programming
- MetaTrader 5 integration
- Algorithmic trading
- Technical analysis
- Market-data processing
- Indicator calculations
- Signal scoring
- Position sizing
- Risk management