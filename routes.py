
from fastapi import APIRouter
from ai.predictor import get_top_breakouts
from data.history import log_predictions

router = APIRouter()

@router.get("/top-breakouts")
async def top_breakouts():
    predictions = get_top_breakouts()
    log_predictions(predictions)
    return {"predictions": predictions}
