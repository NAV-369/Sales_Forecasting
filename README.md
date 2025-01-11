# Customer Behavior and Store Sales Prediction Project

## Overview

### This project explores customer purchasing behavior and uses machine learning and deep learning techniques to predict store sales. The project is divided into three main tasks:
	1.	Exploration of customer purchasing behavior - Analyzing customer data to uncover patterns and trends.
	2.	Prediction of store sales - Using machine learning models to forecast sales for the next 6 weeks.
	3.	Model serving via API - Creating a REST API to serve predictions from the trained models.



### Task 1 - Exploration of Customer Purchasing Behavior

Data Cleaning and Preparation
	•	Clean the dataset by detecting and handling missing data and outliers.
	•	Prepare the data for further analysis by ensuring all columns are in the correct format.

Exploratory Data Analysis (EDA)

Perform EDA to understand the key relationships and trends within the data. Key analysis points include:
	•	Distribution Comparison: Check if promotions are similarly distributed in both training and test datasets.
	•	Holiday Impact: Compare sales behavior before, during, and after holidays.
	•	Seasonality: Investigate how sales are affected by seasons like Christmas, Easter, etc.
	•	Promo Analysis: Analyze how promotions affect sales and customer behavior.
	•	Store Opening Impact: Check how store openings and closings affect sales.
	•	Customer Interaction: Explore how the number of customers influences sales.
	•	Assortment Type Analysis: Study how product assortment impacts sales.

Data Visualization

Visualize the data using various plots to communicate findings effectively. Create plots for:
	•	Correlation matrices
	•	Distribution of sales across different factors (e.g., promos, holidays)
	•	Trends and seasonal effects

Logging

Use the logging library to track steps taken during the analysis for reproducibility and traceability.

### Task 2 - Prediction of Store Sales

Data Preprocessing
	•	Convert non-numeric columns into numeric form.
	•	Handle missing values and generate new features such as:
	•	Weekdays, weekends
	•	Days until holidays and days after holidays
	•	Beginning, mid, and end of the month
	•	Scale the data using StandardScaler to standardize features.

Building Machine Learning Models
	•	Use tree-based algorithms like Random Forest Regressor as a baseline model.
	•	Implement a machine learning pipeline using sklearn to streamline preprocessing and model fitting.

Loss Function Selection
	•	Choose and justify a suitable loss function for regression, such as Mean Squared Error (MSE) or Mean Absolute Error (MAE).
	•	Explain how the chosen loss function aligns with the goal of accurate sales prediction.

Post Prediction Analysis
	•	Explore feature importance to understand what factors most influence sales.
	•	Estimate the confidence interval of predictions to provide a range of uncertainty for sales forecasts.

Serialize Models
	•	Serialize the model to a file format (e.g., .pkl) for each daily prediction to track changes over time.
	•	Store the model with timestamps (e.g., 10-08-2020-16-32-31-00.pkl) to maintain version control.

Deep Learning Model
	•	Build a Long Short-Term Memory (LSTM) model using either TensorFlow or PyTorch for time-series forecasting.
	•	Transform the dataset into time-series data, ensuring the data is stationary before training.
	•	Check for autocorrelation and partial autocorrelation in the data.
	•	Scale the data to the range (-1, 1) and build an LSTM regression model to predict future sales.

### Task 3 - Model Serving API

Framework Selection

Choose a framework for building the REST API:
	•	Flask - Simple and lightweight framework.
	•	FastAPI - High-performance framework, suitable for production-level APIs.
	•	Django REST framework - If more complex web functionalities are needed.

Loading the Model
	•	Load the trained serialized machine learning models from Task 2 using joblib or pickle.

API Endpoints

Define the following API endpoints:
	•	POST /predict: Accept input data (e.g., store info, date) and return sales predictions.
	•	GET /model: Check the model’s status and version.

Handle Requests
	•	Preprocess input data to match the format expected by the trained models.
	•	Use the models to make predictions based on incoming data.

Return Predictions
	•	Format predictions and return them in a user-friendly format (e.g., JSON).

Model Deployment
	•	Deploy the API to a web server or cloud platform (e.g., AWS, Heroku) for real-time prediction requests.

Dependencies

The following Python libraries are required for this project:
	•	Data Analysis and Preprocessing:
	•	pandas
	•	numpy
	•	matplotlib
	•	seaborn
	•	Machine Learning:
	•	scikit-learn
	•	xgboost
	•	Deep Learning:
	•	TensorFlow or PyTorch
	•	API Development:
	•	Flask or FastAPI
	•	pickle or joblib
	•	Logging:
	•	logging

Instructions for Running the Project
	1.	Install dependencies:

pip install -r requirements.txt

	2.	Run the Jupyter Notebook for Task 1:

jupyter notebook Task1_Exploratory_Analysis.ipynb

	3.	Train and save models for Task 2:

python train_models.py

	4.	Run the API for Task 3:

python app.py

	5.	Test the API:

Use a tool like Postman to send POST requests to /predict and receive predictions.

## Conclusion

This project provides valuable insights into customer purchasing behavior and forecasts store sales to aid decision-making. By leveraging both machine learning and deep learning techniques, along with a real-time model serving API, the company can optimize store operations and marketing strategies.
