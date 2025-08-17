# bot/run.py
import os, time, logging
import ccxt

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(message)s"
)

EXCHANGE_NAME = os.getenv("EXCHANGE", "kraken").lower()   # ex: kraken, binance
SYMBOL        = os.getenv("TICK_SYMBOL", "BTC/USDT")      # paire à suivre
INTERVAL_SEC  = int(os.getenv("TICK_INTERVAL_SEC", "10")) # 10s par défaut

def make_exchange(name: str):
    if name == "binance":
        return ccxt.binance({"enableRateLimit": True})
    # défaut: kraken
    return ccxt.kraken({"enableRateLimit": True})

def tick(ex):
    # fetch_ticker = public (pas besoin de clé)
    t = ex.fetch_ticker(SYMBOL)
    last = t.get("last") or t.get("close")
    logging.info("Ticker %s on %s → last=%.2f", SYMBOL, EXCHANGE_NAME, float(last))

def main():
    logging.info("Starting Crypteum worker… exchange=%s symbol=%s", EXCHANGE_NAME, SYMBOL)
    ex = make_exchange(EXCHANGE_NAME)

    while True:
        try:
            tick(ex)
        except ccxt.BaseError as e:
            logging.warning("Exchange error: %s", e)
        except Exception as e:
            logging.exception("Unexpected error: %s", e)
        time.sleep(INTERVAL_SEC)

if __name__ == "__main__":
    main()
