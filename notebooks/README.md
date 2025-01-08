# Sales Forecasting for Rossmann Pharmaceuticals

This project aims to analyze customer purchasing behavior and forecast sales for Rossmann Pharmaceuticals using historical sales data.

## Table of Contents
- [Project Description](#project-description)
- [Data Description](#data-description)
- [Data Processing](#data-processing)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [Analysis](#analysis)
- [Installation](#installation)
- [Usage](#usage)

## Project Description
This project focuses on predicting sales for Rossmann Pharmaceuticals using historical sales data, promotions, and other factors affecting sales. The analysis includes exploratory data analysis, data preprocessing, and model training.

## Data Description
The datasets used in this project include:
- `train.csv`: Contains historical sales data, including features such as store, day of the week, date, sales, customers, and promotional activities.
- `test.csv`: Contains test data for making predictions.

## Data Processing
1. **Loading Data**: The training and test datasets are loaded using pandas.
2. **Handling Missing Values**: Missing values are handled appropriately.
3. **Date Conversion**: The 'Date' column is converted to a datetime format, and new features (Year, Month, Day) are extracted.
4. **One-Hot Encoding**: Categorical variables are one-hot encoded to prepare for model training.
5. **Feature Alignment**: The training and test datasets are aligned to ensure they have the same features.

## Model Training and Evaluation
- A Random Forest Regressor is used for predicting sales.
- The model is trained on the training dataset, and its performance is evaluated using Mean Absolute Error (MAE).
- Predictions are made on the test dataset.

## Results
- Mean Absolute Error: `504.21` (example value, update with actual results)

## Analysis
- Check for distribution in both training and test sets - are the promotions distributed similarly between these two groups?
- Check & compare sales behavior before, during, and after holidays.
- Find out any seasonal (Christmas, Easter, etc.) purchase behaviors.
- What can you say about the correlation between sales and the number of customers?
- How does promo affect sales? Are the promos attracting more customers? How does it affect already existing customers?
- Could the promos be deployed in more effective ways? Which stores should promos be deployed in?
- Trends of customer behavior during store opening and closing times.
- Which stores are open on all weekdays? How does that affect their sales on weekends?
- Check how the assortment type affects sales.
- How does the distance to the next competitor affect sales? What if the store and its competitors all happen to be in city centers, does the distance matter in that case?
- How does the opening or reopening of new competitors affect stores? Check for stores with NA as competitor distance but later on have values for competitor distance.

## Future Work
- Save the trained model for future use.
- Analyze feature importance to understand which factors influence sales the most.
- Experiment with different machine learning models and hyperparameter tuning for improved predictions.
- Create APIs to serve the model for real-time predictions.

## Installation
Ensure you have the following libraries installed:
```bash
pip install pandas scikit-learn joblib
```

## Usage
To run the analysis, execute the Jupyter notebook `exploratory_analysis.ipynb`. Follow the instructions in the notebook to load data, preprocess it, train the model, and evaluate its performance.
