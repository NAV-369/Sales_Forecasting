# Task 2 - Prediction of Store Sales

## Objective
Prediction of sales is the central task in this challenge. You want to predict daily sales in various stores up to 6 weeks ahead of time. This will help the company plan ahead of time.

## Steps
### 2.1 Preprocessing
- Process the data into a format suitable for machine learning models.
- Convert non-numeric columns to numeric and handle NaN values.
- Generate new features from existing datetime columns:
  - Weekdays
  - Weekends
  - Number of days to holidays
  - Number of days after a holiday
  - Beginning, mid-month, and end of the month
  - (Consider additional features for extra marks)
- Scale the data using Standard Scaler from sklearn.

### 2.2 Building Models with sklearn Pipelines
- Use tree-based algorithms, starting with Random Forest Regressor.
- Implement sklearn pipelines for modular and reproducible modeling.

### 2.3 Choose a Loss Function
- Select an appropriate loss function that reflects model performance and justifies your choice creatively.

### 2.4 Post Prediction Analysis
- Explore feature importance and estimate confidence intervals for predictions.

### 2.5 Serialize Models
- Serialize models with timestamps (e.g., 10-08-2020-16-32-31-00.pkl) for tracking predictions.

### 2.6 Building Model with Deep Learning
- Create a Long Short Term Memory (LSTM) model using TensorFlow or PyTorch.
- Ensure the model is not very deep (two layers) to run comfortably in Google Colab.
- Isolate the Rossmann Store Sales dataset into time series data and check for stationarity.
- Transform time series data into supervised learning data and scale it in the (-1, 1) range.
- Build an LSTM Regression model to predict the next sale.