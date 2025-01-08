import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model
model = joblib.load('/Users/zelalemtegene/Desktop/week-4/notebooks/sales_forecasting_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Convert the JSON data to a DataFrame
    input_data = pd.DataFrame(data)

    # Make predictions using the loaded model
    predictions = model.predict(input_data)

    # Return the predictions as a JSON response
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)