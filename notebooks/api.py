import os
import joblib
import requests
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

# Define the path to save the model
model_path = Path(__file__).parent / "random_forest_model.pkl"
# Update with a direct download link format for Google Drive
model_id = "1squMdWoR_trc1lpxnkx1OJiqzhpaSsl3"
model_url = f"https://drive.google.com/uc?id={model_id}&export=download"

# Function to download the model file
def download_model(url, save_path):
    print("Model file not found locally. Downloading...")
    session = requests.Session()
    response = session.get(url, stream=True)

    # Handle Google Drive large file download warning
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            url += f"&confirm={value}"
            response = session.get(url, stream=True)
            break

    with open(save_path, "wb") as model_file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                model_file.write(chunk)
    print("Model downloaded successfully!")

# Check if the model file exists, otherwise download it
if not model_path.exists():
    try:
        download_model(model_url, model_path)
    except Exception as e:
        print(f"Error downloading model: {e}")
        raise

# Load the trained model
try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    raise

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