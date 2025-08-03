
def compute_score(asset):
    score = 0
    if asset.get("momentum", 0) > 70:
        score += 30
    if asset.get("volume_change", 0) > 100:
        score += 20
    if asset.get("volatility", 0) > 50:
        score += 10
    if asset.get("insider_activity", False):
        score += 20
    if asset.get("politician_investment", False):
        score += 20
    if asset.get("sentiment", "") == "bullish":
        score += 10
    return score
