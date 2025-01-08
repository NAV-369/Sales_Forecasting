import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path  # To handle paths

# Define the path to the trained model
model_path = Path(__file__).parent / "random_forest_model.pkl"  # Adjust path as needed

# Load the trained model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Model file not found at {model_path}. Please check the file path.")

app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    features: list  # Adjust based on your input features

# Define the prediction endpoint
@app.post("/predict")
async def predict(input_data: InputData):
    # Preprocess input data
    try:
        features = np.array(input_data.features).reshape(1, -1)  # Adjust shape if necessary
        prediction = model.predict(features)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}