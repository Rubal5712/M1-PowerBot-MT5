import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time

# =============================================================================
# 🔧 CONFIGURATION – change these values (no coding needed)
# =============================================================================
SYMBOLS = ["XAUUSD"]
SIGNAL_TIMEFRAME = mt5.TIMEFRAME_M1
HIGHER_TF = mt5.TIMEFRAME_H4

ACCOUNT_BALANCE = 1805                  # reference balance (for info)
RISK_PERCENT_PER_BATCH = 4.0            # risk per batch = 4% → $80
TARGET_PROFIT_PER_BATCH = 100.0         # profit target
FIXED_SL_POINTS = 5000                  # Stop Loss in points
FIXED_TP_POINTS = 25                   # Take Profit (must be > SL)

ORDERS_PER_BATCH = 3                    # fewer orders to avoid margin fragmentation
MAX_LOT_PER_ORDER = 0.40                 # safety cap
MAX_SPREAD_POINTS = 50
SLEEP_SECONDS = 1

SCALE_IN_POINTS = 80                    # distance to add another batch
MAX_BATCHES = 3                         # max scale‑in batches
MARTINGALE_MULTIPLIER = 1.5

MIN_SCORE_TO_TRADE = 0.5
ALLOW_TRADE_ON_FLAT_TREND = True

USE_OPENAI = False
OPENAI_API_KEY = None
GPT_MODEL = "gpt-3.5-turbo"
GPT_SIGNAL_WEIGHT = 1.0

MT5_LOGIN = 
MT5_PASSWORD = ""
MT5_SERVER = ""

# =============================================================================
# 🛠️ CORE FUNCTIONS
# =============================================================================

def initialize_mt5():
    if not mt5.initialize():
        raise RuntimeError("MT5 initialize failed")
    if mt5.account_info() is not None:
        print(f"Connected to account #{mt5.account_info().login}")
        return
    authorized = mt5.login(MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
    if not authorized:
        raise RuntimeError(f"Login failed: {mt5.last_error()}")
    print(f"Logged in to account #{mt5.account_info().login}")

def get_filling_mode(symbol):
    info = mt5.symbol_info(symbol)
    if info is None:
        return mt5.ORDER_FILLING_IOC
    if hasattr(info, 'filling_mode') and info.filling_mode != 0:
        return info.filling_mode
    return mt5.ORDER_FILLING_RETURN

def fetch_rates(symbol, timeframe, bars=200):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    if rates is None or len(rates) < 10:
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def add_indicators(df):
    df['ema12'] = df['close'].ewm(span=12, adjust=False).mean()
    df['ema26'] = df['close'].ewm(span=26, adjust=False).mean()
    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1/14, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/14, adjust=False).mean()
    rs = avg_gain / avg_loss
    df['rsi'] = 100 - (100 / (1 + rs))
    ema12_macd = df['close'].ewm(span=12, adjust=False).mean()
    ema26_macd = df['close'].ewm(span=26, adjust=False).mean()
    df['macd'] = ema12_macd - ema26_macd
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    df['macd_hist'] = df['macd'] - df['macd_signal']
    df['bb_mid'] = df['close'].rolling(20).mean()
    bb_std = df['close'].rolling(20).std()
    df['bb_upper'] = df['bb_mid'] + 2 * bb_std
    df['bb_lower'] = df['bb_mid'] - 2 * bb_std
    high, low, close = df['high'], df['low'], df['close']
    tr = pd.concat([high - low,
                    (high - close.shift()).abs(),
                    (low - close.shift()).abs()], axis=1).max(axis=1)
    df['atr'] = tr.ewm(alpha=1/14, adjust=False).mean()
    df['volume_sma'] = df['tick_volume'].rolling(20).mean()
    return df

def detect_candlestick_patterns(df):
    if len(df) < 3:
        return 0
    o1, c1, h1, l1 = df.iloc[-2][['open','close','high','low']]
    o2, c2, h2, l2 = df.iloc[-1][['open','close','high','low']]
    if c1 < o1 and c2 > o2 and o2 <= c1 and c2 >= o1:
        return 1
    if c1 > o1 and c2 < o2 and o2 >= c1 and c2 <= o1:
        return -1
    body = abs(c2 - o2)
    lower_wick = min(o2, c2) - l2
    upper_wick = h2 - max(o2, c2)
    if lower_wick > 2 * body and upper_wick < body and l2 < l1:
        return 1
    if upper_wick > 2 * body and lower_wick < body and h2 > h1:
        return -1
    return 0

def find_support_resistance(df, window=20):
    highs = df['high'].rolling(window).max()
    lows = df['low'].rolling(window).min()
    price = df['close'].iloc[-1]
    dist_res = (highs.iloc[-1] - price) / price * 100
    dist_sup = (price - lows.iloc[-1]) / price * 100
    return dist_res, dist_sup

def get_trend_strength(symbol, tf):
    df = fetch_rates(symbol, tf, bars=100)
    if df is None:
        return 0
    df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()
    close = df['close'].iloc[-1]
    ema50 = df['ema50'].iloc[-1]
    if close > ema50 * 1.002:
        return 1
    elif close < ema50 * 0.998:
        return -1
    return 0

def ask_gpt(symbol, df):
    if not USE_OPENAI or not OPENAI_API_KEY:
        return 0
    try:
        import openai
        last_candles = df.tail(5)[['time','open','high','low','close','tick_volume']].to_string(index=False)
        prompt = (f"Expert financial trader. Based on the last 5 candles of {symbol} (15-min chart), "
                  f"respond with exactly one word: BUY, SELL, or HOLD.\n\n{last_candles}")
        if hasattr(openai, "OpenAI"):
            client = openai.OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=GPT_MODEL,
                messages=[{"role": "system", "content": prompt}],
                temperature=0.0,
                max_tokens=10
            )
            verdict = response.choices[0].message.content.strip().upper()
        else:
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model=GPT_MODEL,
                messages=[{"role": "system", "content": prompt}],
                temperature=0.0,
                max_tokens=10
            )
            verdict = response.choices[0].message['content'].strip().upper()
        if verdict == "BUY":
            return 1
        elif verdict == "SELL":
            return -1
        else:
            return 0
    except Exception as e:
        print(f"[GPT Error] {e}")
        return 0

def calculate_composite_score(symbol):
    breakdown = {}
    score = 0.0
    h4_trend = get_trend_strength(symbol, HIGHER_TF)
    if h4_trend == 1:
        score += 0.5
        breakdown['H4'] = 0.5
    elif h4_trend == -1:
        score -= 0.5
        breakdown['H4'] = -0.5
    else:
        breakdown['H4'] = 0.0

    df = fetch_rates(symbol, SIGNAL_TIMEFRAME, bars=200)
    if df is None:
        return 0, h4_trend, ""
    df = add_indicators(df)

    if df['ema12'].iloc[-1] > df['ema26'].iloc[-1]:
        score += 0.3
        breakdown['EMA'] = 0.3
    else:
        score -= 0.3
        breakdown['EMA'] = -0.3

    rsi = df['rsi'].iloc[-1]
    if rsi < 30:
        score += 0.4
        breakdown['RSI'] = 0.4
    elif rsi > 70:
        score -= 0.4
        breakdown['RSI'] = -0.4
    else:
        breakdown['RSI'] = 0.0

    if df['macd_hist'].iloc[-1] > 0 and df['macd_hist'].iloc[-1] > df['macd_hist'].iloc[-2]:
        score += 0.2
        breakdown['MACD'] = 0.2
    elif df['macd_hist'].iloc[-1] < 0 and df['macd_hist'].iloc[-1] < df['macd_hist'].iloc[-2]:
        score -= 0.2
        breakdown['MACD'] = -0.2
    else:
        breakdown['MACD'] = 0.0

    close = df['close'].iloc[-1]
    if close <= df['bb_lower'].iloc[-1]:
        score += 0.3
        breakdown['BB'] = 0.3
    elif close >= df['bb_upper'].iloc[-1]:
        score -= 0.3
        breakdown['BB'] = -0.3
    else:
        breakdown['BB'] = 0.0

    if df['tick_volume'].iloc[-1] > df['volume_sma'].iloc[-1] * 1.5:
        if df['close'].iloc[-1] > df['close'].iloc[-2]:
            score += 0.2
            breakdown['Vol'] = 0.2
        else:
            score -= 0.2
            breakdown['Vol'] = -0.2
    else:
        breakdown['Vol'] = 0.0

    pattern = detect_candlestick_patterns(df)
    score += pattern * 0.6
    breakdown['Pat'] = pattern * 0.6

    dist_res, dist_sup = find_support_resistance(df)
    if dist_sup < 0.3:
        score += 0.4
        breakdown['SR'] = 0.4
    elif dist_res < 0.3:
        score -= 0.4
        breakdown['SR'] = -0.4
    else:
        breakdown['SR'] = 0.0

    if USE_OPENAI and OPENAI_API_KEY:
        gpt_signal = ask_gpt(symbol, df)
        score += gpt_signal * GPT_SIGNAL_WEIGHT
        breakdown['GPT'] = gpt_signal * GPT_SIGNAL_WEIGHT
    else:
        breakdown['GPT'] = 0.0

    b_str = " | ".join([f"{k}:{v:+.1f}" for k, v in breakdown.items()])
    return score, h4_trend, b_str

def get_max_lot_from_margin(symbol, free_margin, margin_usage=0.5):
    """Return the maximum total lot allowed given free margin (using margin_usage fraction)."""
    info = mt5.symbol_info(symbol)
    if info is None:
        return 0.0
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        return 0.0
    price = tick.ask
    # Use order_calc_margin (correct method)
    margin_req = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, 1.0, price)
    if margin_req is None or margin_req <= 0:
        # fallback: use margin_initial from symbol info
        margin_req = info.margin_initial
        if margin_req <= 0:
            print(f"[{symbol}] Cannot determine margin – skipping margin cap")
            return float('inf')  # no cap
    max_lot = (free_margin * margin_usage) / margin_req
    return max_lot

def calculate_lot_per_order(symbol, balance, risk_pct, sl_points, num_orders, multiplier, free_margin):
    """
    Compute lot per order, capped by margin.
    Returns (lot_per_order, total_lot_capped_flag).
    """
    info = mt5.symbol_info(symbol)
    if info is None or sl_points <= 0:
        return 0.01, False
    risk_money = balance * risk_pct / 100.0
    tick_val = info.trade_tick_value
    tick_sz = info.trade_tick_size
    point = info.point
    point_val = tick_val * (point / tick_sz) if tick_sz > 0 else 0
    if point_val == 0:
        return 0.01, False
    loss_per_lot = sl_points * point_val
    total_lot = risk_money / loss_per_lot
    total_lot *= multiplier
    # Margin cap
    max_total_lot = get_max_lot_from_margin(symbol, free_margin, 0.5)
    capped = False
    if max_total_lot > 0 and total_lot > max_total_lot:
        total_lot = max_total_lot
        capped = True
    lot_per_order = total_lot / num_orders
    step = info.volume_step
    lot_per_order = round(lot_per_order / step) * step
    lot_per_order = max(info.volume_min, min(info.volume_max, lot_per_order))
    lot_per_order = min(lot_per_order, MAX_LOT_PER_ORDER)
    return lot_per_order, capped

def place_market_order(symbol, order_type, lot, sl_points, tp_points, magic):
    info = mt5.symbol_info(symbol)
    if info is None:
        return None
    tick = mt5.symbol_info_tick(symbol)
    point = info.point

    if order_type == mt5.ORDER_TYPE_BUY:
        price = tick.ask
        sl = price - sl_points * point
        tp = price + tp_points * point
    else:
        price = tick.bid
        sl = price + sl_points * point
        tp = price - tp_points * point

    fillings_to_try = [
        get_filling_mode(symbol),
        mt5.ORDER_FILLING_RETURN,
        mt5.ORDER_FILLING_IOC,
        mt5.ORDER_FILLING_FOK
    ]
    tried = set()
    for fill in fillings_to_try:
        if fill in tried:
            continue
        tried.add(fill)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 20,
            "magic": magic,
            "comment": "M1_PowerBot",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": fill,
        }
        result = mt5.order_send(request)
        if result.retcode == mt5.TRADE_RETCODE_DONE:
            return result.order
        elif result.retcode == 10030:
            continue
        else:
            print(f"[{symbol}] Order failed, retcode={result.retcode}, error={result.comment}")
            return None
    print(f"[{symbol}] All filling modes failed.")
    return None

def close_all_positions(symbol, magic):
    positions = mt5.positions_get(symbol=symbol)
    if positions is None:
        return
    for pos in positions:
        if pos.magic == magic:
            tick = mt5.symbol_info_tick(symbol)
            order_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price = tick.bid if pos.type == mt5.POSITION_TYPE_BUY else tick.ask
            fill = get_filling_mode(symbol)
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": pos.volume,
                "type": order_type,
                "position": pos.ticket,
                "price": price,
                "deviation": 20,
                "magic": magic,
                "comment": "ClosePower",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": fill,
            }
            mt5.order_send(request)

def total_profit(symbol, magic):
    positions = mt5.positions_get(symbol=symbol)
    if positions is None:
        return 0
    return sum(p.profit for p in positions if p.magic == magic)

def get_direction_from_positions(symbol, magic):
    positions = mt5.positions_get(symbol=symbol)
    if positions is None:
        return 0
    for p in positions:
        if p.magic == magic:
            return 1 if p.type == mt5.POSITION_TYPE_BUY else -1
    return 0

# =============================================================================
# 🧠 BOT CLASS
# =============================================================================
class AISymbolBot:
    def __init__(self, symbol, magic_base):
        self.symbol = symbol
        self.magic = magic_base
        self.cooldown = 0
        self.batch_count = 0
        self.last_entry_price = None
        self.batch_placed_fully = False

    def update(self, balance):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        info = mt5.symbol_info(self.symbol)
        if info is None or info.trade_mode != mt5.SYMBOL_TRADE_MODE_FULL:
            return

        tick = mt5.symbol_info_tick(self.symbol)
        spread = (tick.ask - tick.bid) / info.point
        if spread > MAX_SPREAD_POINTS:
            return

        open_positions = mt5.positions_get(symbol=self.symbol)
        own = [p for p in open_positions if p.magic == self.magic] if open_positions else []

        if own:
            profit = total_profit(self.symbol, self.magic)
            if profit >= TARGET_PROFIT_PER_BATCH:
                print(f"[{self.symbol}] Profit ${profit:.2f} reached target – closing all")
                close_all_positions(self.symbol, self.magic)
                self.batch_count = 0
                self.last_entry_price = None
                self.batch_placed_fully = False
                return

            if self.batch_placed_fully and self.batch_count < MAX_BATCHES:
                direction = get_direction_from_positions(self.symbol, self.magic)
                if direction != 0:
                    current_price = tick.ask if direction == 1 else tick.bid
                    if self.last_entry_price is not None:
                        dist = abs(current_price - self.last_entry_price) / info.point
                        if dist >= SCALE_IN_POINTS:
                            self._open_batch(balance, direction, tick, info)
            return

        self.batch_count = 0
        self.last_entry_price = None
        self.batch_placed_fully = False
        score, h4_trend, b_str = calculate_composite_score(self.symbol)
        print(f"[{self.symbol}] Score: {score:+.2f} (H4: {h4_trend}) [{b_str}]")

        if abs(score) < MIN_SCORE_TO_TRADE:
            return
        if h4_trend != 0 and np.sign(score) != np.sign(h4_trend) and abs(score) < 0.8:
            return

        direction = 1 if score > 0 else -1
        self._open_batch(balance, direction, tick, info)

    def _open_batch(self, balance, direction, tick, info):
        order_type = mt5.ORDER_TYPE_BUY if direction == 1 else mt5.ORDER_TYPE_SELL

        sl_points = FIXED_SL_POINTS
        tp_points = FIXED_TP_POINTS

        account = mt5.account_info()
        if account is None:
            return
        free_margin = account.margin_free

        multiplier = MARTINGALE_MULTIPLIER ** self.batch_count
        lot_per_order, capped = calculate_lot_per_order(
            self.symbol, balance, RISK_PERCENT_PER_BATCH,
            sl_points, ORDERS_PER_BATCH, multiplier, free_margin
        )
        if lot_per_order <= 0:
            print(f"[{self.symbol}] Lot too small or margin insufficient – skipping")
            return

        if capped:
            print(f"[{self.symbol}] ⚠️ Lot capped by margin – risk may be lower than intended")

        dir_str = "BUY" if direction == 1 else "SELL"
        print(f"🤖 [{self.symbol}] {dir_str} | Batch #{self.batch_count+1} | Lot: {lot_per_order:.2f} | SL: {sl_points} | TP: {tp_points}")

        placed = 0
        for i in range(ORDERS_PER_BATCH):
            order = place_market_order(self.symbol, order_type, lot_per_order, sl_points, tp_points, self.magic)
            if order:
                placed += 1
                print(f"  [{self.symbol}] {placed}/{ORDERS_PER_BATCH} ticket={order}")
            time.sleep(0.15)

        if placed == ORDERS_PER_BATCH:
            self.last_entry_price = tick.ask if direction == 1 else tick.bid
            self.batch_count += 1
            self.batch_placed_fully = True
        elif placed > 0:
            print(f"[{self.symbol}] Only {placed}/{ORDERS_PER_BATCH} placed – closing them")
            close_all_positions(self.symbol, self.magic)
            self.batch_count = 0
            self.last_entry_price = None
            self.batch_placed_fully = False
            self.cooldown = 10
        else:
            self.cooldown = 10
            self.batch_placed_fully = False

# =============================================================================
# 🏁 MAIN
# =============================================================================
def main():
    print("🚀 M1 Power Bot – Target $100 per batch (Margin‑Aware)")
    initialize_mt5()
    for sym in SYMBOLS:
        mt5.symbol_select(sym, True)

    bots = {}
    for i, sym in enumerate(SYMBOLS):
        bots[sym] = AISymbolBot(sym, 700000 + i)

    print(f"Trading {len(SYMBOLS)} symbols, {ORDERS_PER_BATCH} orders per batch")
    print(f"Risk: {RISK_PERCENT_PER_BATCH}% per batch → ${ACCOUNT_BALANCE * RISK_PERCENT_PER_BATCH / 100:.2f}")
    print(f"Reward target: ${TARGET_PROFIT_PER_BATCH:.2f} (SL={FIXED_SL_POINTS}, TP={FIXED_TP_POINTS})")
    print(f"Scale‑in: {SCALE_IN_POINTS} points, max {MAX_BATCHES} batches, multiplier {MARTINGALE_MULTIPLIER}")
    print("Waiting for signals...\n")

    while True:
        try:
            if mt5.terminal_info() is None:
                print("Reconnecting...")
                mt5.shutdown()
                time.sleep(2)
                initialize_mt5()
                for sym in SYMBOLS:
                    mt5.symbol_select(sym, True)

            account = mt5.account_info()
            if account is None:
                time.sleep(5)
                continue
            balance = account.balance

            for sym in SYMBOLS:
                bots[sym].update(balance)

            time.sleep(SLEEP_SECONDS)

        except KeyboardInterrupt:
            print("Shutting down...")
            mt5.shutdown()
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            time.sleep(5)

if __name__ == "__main__":
    main()
