# M1 PowerBot – AI‑Enhanced MetaTrader 5 Scalping Bot

**M1 PowerBot** is an automated trading bot for MetaTrader 5 that combines technical indicators, candlestick patterns, support/resistance levels, and optional GPT‑powered sentiment analysis. It uses a **scaling‑in** (martingale) strategy with dynamic lot sizing based on risk and available margin.

## ⚠️ Disclaimer
> This software is for **educational purposes only**. Trading financial markets involves substantial risk. Past performance does not guarantee future results. Use this bot **at your own risk**.

## Features
- **Multi‑timeframe analysis** (M1 signal, H4 trend filter)
- **Composite scoring** – EMA, RSI, MACD, Bollinger Bands, volume, patterns, S/R
- **Optional GPT‑3.5/4 integration** for additional trade signals
- **Batch order placement** with configurable number of orders per batch
- **Scale‑in** with automatic batch triggering at defined price intervals
- **Martingale lot multiplier** (configurable)
- **Margin‑aware lot sizing** – never exceeds available free margin
- **Automatic profit target** & stop‑loss management

## Configuration
Edit the `# 🔧 CONFIGURATION` :

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

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rubal5712/M1PowerBot.git
   cd M1PowerBot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure** – fill in your MT5 login and other settings.

4. **Run the bot**
   ```bash
   python main.py
   ```

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

