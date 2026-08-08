# M1 PowerBot – AI‑Enhanced MetaTrader 5 Scalping Bot

**M1 PowerBot** is an automated trading bot for MetaTrader 5 that combines technical indicators, candlestick patterns, support/resistance levels, and optional GPT‑powered sentiment analysis. It uses a **scaling‑in** (martingale) strategy with dynamic lot sizing based on risk and available margin.

## ⚠️ Disclaimer
> This software is for **educational purposes only**. Trading financial markets involves substantial risk. Past performance does not guarantee future results. Use this bot **at your own risk**. Never trade with money you cannot afford to lose.

---

## ❓ Why This Bot Was Made
Manual scalping on the **M1 (1-minute) timeframe** is extremely difficult because prices move too fast for a human to react. This bot was created to:
- **Remove human emotions** (fear and greed) from trading decisions.
- **Combine multiple indicators** into a single "composite score" so you don't have to guess which signal to follow.
- **Automate risk management** by calculating lot sizes based on your exact account balance and free margin.
- **Scale into positions** intelligently. If the market moves against you, it adds new orders at better prices (scaling-in) to lower the average entry price and recover faster when the price reverses.

---

## ⚙️ How It Works (Step-by-Step Logic)

Here is the exact decision-making process the bot follows every second:

1. **Data Collection**  
   The bot fetches the last 200 candles from MetaTrader 5 for your selected symbol (e.g., XAUUSD).

2. **Indicator Calculation**  
   It calculates: EMA (12 & 26), RSI, MACD, Bollinger Bands, ATR, and Volume SMA.

3. **Composite Scoring**  
   Each indicator gives a **positive or negative score** based on market conditions:
   - If EMA12 > EMA26 → `+0.3` (Bullish)
   - If RSI is below 30 (Oversold) → `+0.4` (Bullish)
   - If price touches the lower Bollinger Band → `+0.3` (Bullish)
   - If volume is high and price is rising → `+0.2` (Bullish)  
   *(All scores are added up to get a total score, e.g., +1.2 for BUY or -0.8 for SELL).*

4. **Trend Filter (H4)**  
   The bot checks the **4-hour (H4) trend**. If the H4 trend is strongly down, but the M1 score says "BUY", the bot will **reject** the signal (to avoid trading against the big trend).

5. **Triggering a Trade**  
   If the composite score is higher than `MIN_SCORE_TO_TRADE` (e.g., 0.5), the bot places **3 orders** (or whatever you set in `ORDERS_PER_BATCH`) in the same direction.

6. **Scaling-In (Averaging)**  
   If the price moves against your position by `SCALE_IN_POINTS` (e.g., 80 points), the bot places another batch of orders. This batch uses the `MARTINGALE_MULTIPLIER` (e.g., 1.5x) to increase the lot size, helping you break even faster when the price retraces.

7. **Taking Profit**  
   The bot continuously monitors the **total profit** of all open positions. As soon as the total profit hits `TARGET_PROFIT_PER_BATCH` (e.g., $100), it **immediately closes all orders** and resets the batch counter.

---

## 💡 Important Tips Before You Start

1. **🔴 ALWAYS test on a Demo account first!**  
   Do not run this on a live account until you have tested it for at least **2-4 weeks** on a demo account. Markets behave differently than backtests.

2. **🚨 CRITICAL: Fix your Stop-Loss and Take-Profit!**  
   In your current code, you have:
   - `FIXED_SL_POINTS = 5000` (Stop Loss)
   - `FIXED_TP_POINTS = 25` (Take Profit)  
   **This means you are risking $100 to make only $0.50!** This is a terrible risk-reward ratio. You should **swap these values** (e.g., SL = 250, TP = 500) or adjust them based on your instrument's volatility.

3. **Start with tiny risk.**  
   Change `RISK_PERCENT_PER_BATCH` from `4.0` to `0.5` or `1.0` when you start testing. This protects your balance if the bot hits the Stop Loss.

4. **Keep MetaTrader 5 open and stable.**  
   The bot relies on a constant connection. If your internet disconnects or MT5 crashes, the bot cannot manage your trades. Consider running it on a **VPS (Virtual Private Server)** for 24/7 uptime.

5. **Understand the Spread.**  
   Gold (XAUUSD) can have high spreads during news events. The bot has a `MAX_SPREAD_POINTS` filter. If the spread is too wide, it will refuse to trade to avoid paying too much.

---

## 🛠️ Configuration
Edit the `# 🔧 CONFIGURATION` section in `main.py`:

| Parameter                     | Description |
|-------------------------------|-------------|
| `SYMBOLS`                     | List of instruments to trade (e.g., `["XAUUSD"]`) |
| `SIGNAL_TIMEFRAME`            | Timeframe for signal generation (e.g., `mt5.TIMEFRAME_M1`) |
| `HIGHER_TF`                   | Higher timeframe for trend filter (e.g., `mt5.TIMEFRAME_H4`) |
| `RISK_PERCENT_PER_BATCH`      | % of balance risked per batch |
| `TARGET_PROFIT_PER_BATCH`     | Take‑profit amount in account currency |
| `FIXED_SL_POINTS` / `FIXED_TP_POINTS` | Stop‑loss and take‑profit in points |
| `ORDERS_PER_BATCH`            | Number of orders per scale‑in batch |
| `MAX_LOT_PER_ORDER`           | Hard cap on lot size per order |
| `SCALE_IN_POINTS`             | Minimum price distance to add next batch |
| `MAX_BATCHES`                 | Maximum number of scale‑in batches |
| `MARTINGALE_MULTIPLIER`       | Lot multiplier for each subsequent batch |
| `MIN_SCORE_TO_TRADE`          | Minimum composite score threshold |
| `USE_OPENAI` / `API_KEY`      | Enable GPT signals (optional) |
| `MT5_LOGIN`, `MT5_PASSWORD`, `MT5_SERVER` | Your MetaTrader 5 account credentials |

---

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rubal5712/M1PowerBot.git
   cd M1PowerBot
   nstall dependencies

3. **Configure** – fill in your MT5 login and other settings.

4. **Run the bot**
   ```bash
   python m1powerbotmt5.py
   ```

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.




