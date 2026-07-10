import json
import pickle
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

__locations = None
__data_columns = None
__model = None


def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    with open(ARTIFACTS_DIR / "columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open(ARTIFACTS_DIR / "bangalore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)


def get_location_names():
    return __locations


def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)