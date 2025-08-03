
import json
from datetime import datetime

def log_predictions(predictions):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "predictions": predictions
    }
    with open("data/history_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
