
import random
from utils.scoring import compute_score
from data.sources import get_all_assets

def get_top_breakouts():
    assets = get_all_assets()
    scored_assets = []
    for asset in assets:
        score = compute_score(asset)
        if score > 80:
            scored_assets.append({
                "symbol": asset["symbol"],
                "name": asset["name"],
                "score": score,
                "reason": asset.get("reason", "High momentum, insider trading, and bullish sentiment.")
            })
    scored_assets.sort(key=lambda x: x["score"], reverse=True)
    return scored_assets[:10]
