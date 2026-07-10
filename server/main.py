from fastapi import FastAPI
from pydantic import BaseModel
import util

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

util.load_saved_artifacts()


class HouseRequest(BaseModel):
    location: str
    sqft: float
    bath: int
    bhk: int


@app.get("/")
def home():
    return {"message": "Bangalore House Price Prediction API"}


@app.get("/locations")
def locations():
    return util.get_location_names()


@app.post("/predict")
def predict(data: HouseRequest):
    price = util.predict_price(
        data.location,
        data.sqft,
        data.bath,
        data.bhk
    )

    return {
        "estimated_price": price,
        "unit": "Lakh INR"
    }