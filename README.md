# House Price Prediction Using Machine Learning

## Project Overview

This project predicts the estimated price of a house based on its area, number of bedrooms, and location using a Linear Regression model.

The project uses Python, Pandas, NumPy, and Scikit-learn to build a machine learning pipeline that preprocesses data, trains the model, evaluates its performance, and predicts prices for new house details.

## Features

- Loads housing data from a CSV file.
- Inspects missing values and removes duplicate rows.
- Handles missing numerical and categorical values.
- Encodes categorical locations using One-Hot Encoding.
- Trains a Linear Regression model.
- Evaluates predictions using MAE, MSE, RMSE, and R².
- Accepts user input to estimate a house price.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Linear Regression
- VS Code

## Project Structure

```text
house-price-prediction/
├── house_price_prediction.py
├── house_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command from the project folder:

```bash
python house_price_prediction.py
```

Enter the requested house details when prompted:

- Area in square feet
- Number of bedrooms
- Location

The program displays the estimated house price.

## Model Evaluation

The model reports the following evaluation metrics:

- **MAE:** Mean Absolute Error
- **MSE:** Mean Squared Error
- **RMSE:** Root Mean Squared Error
- **R²:** Coefficient of Determination

Actual evaluation results depend on the dataset and the train/test split.

## Dataset

The CSV dataset contains the following columns:

| Column | Description |
|---|---|
| `area` | House area in square feet |
| `bedrooms` | Number of bedrooms |
| `location` | House location |
| `price` | Target house price |

## Limitations

The model's predictions depend on the quality, size, and representativeness of the training data. A small or synthetic dataset will not reliably represent actual housing market prices.

The predicted price is an estimate, not a guaranteed market value.

## Future Improvements

- Use a larger, reliable housing dataset.
- Add more useful features, such as property age and bathrooms.
- Compare Linear Regression with other regression models.
- Improve validation and model evaluation.
- Build a simple web interface for predictions.

## Learning Outcomes

This project demonstrates practical experience with data preprocessing, categorical encoding, machine learning pipelines, regression, model evaluation, and user-input-based prediction.
