import joblib
from fastapi import FastAPI
from pydantic import BaseModel

class PredictHouseRequest(BaseModel):
    size: int
    rooms: int
    park_spaces: int

class PredictHouseResponse(BaseModel):
    estimated_price: float

app = FastAPI()

modelo = joblib.load("best_regression_model.pkl")

@app.post("/predict/", response_model=PredictHouseResponse)
def prever_preco(casa: PredictHouseRequest):
    
    entry_data = [[casa.size, 
                       casa.rooms, 
                       casa.park_spaces]]
    estimated_price = modelo.predict(entry_data)[0]
    return {
        "estimated_price": round(float(estimated_price), 2)
    }