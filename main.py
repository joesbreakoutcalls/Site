
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import requests
import asyncio
import time
from typing import List, Dict

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def fetch_yahoo_assets(symbols: List[str]) -> List[Dict]:
    results = []
    for symbol in symbols:
        try:
            data = yf.Ticker(symbol)
            hist = data.history(period="2d")
            if len(hist) >= 2:
                prev_close = hist["Close"].iloc[-2]
                latest_close = hist["Close"].iloc[-1]
                change_pct = ((latest_close - prev_close) / prev_close) * 100
                volume = hist["Volume"].iloc[-1]
                results.append({
                    "symbol": symbol,
                    "type": "stock",
                    "latest_close": latest_close,
                    "change_pct": change_pct,
                    "volume": volume,
                    "score": change_pct * (volume ** 0.5)
                })
        except Exception:
            continue
    return results

def fetch_coingecko_assets(limit=100) -> List[Dict]:
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    resp = requests.get(url, params=params)
    results = []
    if resp.status_code == 200:
        for coin in resp.json():
            try:
                change_pct = coin["price_change_percentage_24h"]
                volume = coin["total_volume"]
                score = change_pct * (volume ** 0.5)
                results.append({
                    "symbol": coin["symbol"].upper(),
                    "type": "crypto",
                    "latest_close": coin["current_price"],
                    "change_pct": change_pct,
                    "volume": volume,
                    "score": score
                })
            except Exception:
                continue
    return results

@app.get("/api/breakouts")
async def get_breakouts():
    start = time.time()
    
    # Example stock symbols - will be replaced with full scan later
    stock_symbols = ["AAPL", "TSLA", "AMD", "NVDA", "GOOG", "META", "MSFT", "GME", "AMC", "PLTR"]
    stock_data = fetch_yahoo_assets(stock_symbols)
    crypto_data = fetch_coingecko_assets(limit=100)

    combined = stock_data + crypto_data
    top_10 = sorted(combined, key=lambda x: x["score"], reverse=True)[:10]

    for item in top_10:
        item["reason"] = f"Strong {item['type']} price movement: {item['change_pct']:.2f}% with high volume."

    return {
        "status": "ok",
        "top_10_predictions": top_10,
        "processing_time_sec": round(time.time() - start, 2)
    }
