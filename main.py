
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router as breakout_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(breakout_router)

@app.get("/")
def read_root():
    return {"message": "Breakout Predictor API is running"}
