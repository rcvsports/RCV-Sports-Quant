from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RCV Backend Running"}

@app.get("/parlays")
def get_parlays():
    return [
        {
            "type": "3-Leg",
            "ev": 1.12,
            "probability": 0.42,
            "legs": ["Thunder - Spread", "Under 224", "Magic ML"]
        }
    ]
