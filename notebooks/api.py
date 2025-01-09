import os
import joblib
import requests
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

# Define the path to save the model
model_path = Path(__file__).parent / "random_forest_model.pkl"
model_url = "https://drive.google.com/file/d/1squMdWoR_trc1lpxnkx1OJiqzhpaSsl3/view?usp=sharing"  # Replace with the actual URL

# Check if the model file exists, otherwise download it
if not model_path.exists():
    print("Model file not found locally. Downloading...")
    response = requests.get(model_url, stream=True)
    with open(model_path, "wb") as model_file:
        for chunk in response.iter_content(chunk_size=8192):
            model_file.write(chunk)
    print("Model downloaded successfully!")

# Load the trained model
model = joblib.load(model_path)

app = FastAPI()

class InputData(BaseModel):
    features: list

@app.post("/predict")
async def predict(input_data: InputData):
    try:
        features = np.array(input_data.features).reshape(1, -1)
        prediction = model.predict(features)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}