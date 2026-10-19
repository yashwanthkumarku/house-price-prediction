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

## Model Evaluation

The House Price Prediction model was evaluated on a held-out test set using standard regression metrics.

### Evaluation Results

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | ₹413,608.98 |
| Mean Squared Error (MSE) | 273,860,158,597.18 |
| Root Mean Squared Error (RMSE) | ₹523,316.50 |
| R² Score | 0.5402 |
| Baseline MAE | ₹1,354,166.67 |

### Results Interpretation

- **MAE:** The model's predictions have an average absolute error of approximately ₹4.14 lakh on the test set.
- **MSE:** Measures the average squared prediction error, penalizing larger errors more heavily. Its unit is rupees squared.
- **RMSE:** The RMSE is approximately ₹5.23 lakh, indicating that larger prediction errors have a stronger influence on this metric than on MAE.
- **R² Score:** The model achieved an R² score of 0.5402, indicating that it explains approximately 54.02% of the variation in house prices on the test set relative to a mean-based reference.
- **Baseline Comparison:** The baseline MAE is ₹13.54 lakh, compared with the model's MAE of ₹4.14 lakh. The model's MAE is approximately 69.45% lower than the baseline MAE on this test set.

### Conclusion

The Multiple Linear Regression model outperformed the mean-price baseline on the evaluated test set. The results suggest that area, number of bedrooms, and location provide useful information for estimating house prices.

### Limitations and Future Improvements

- Model performance depends on the dataset and train/test split.
- A small or synthetic dataset may not represent actual housing market conditions.
- Additional features, such as property age, condition, and nearby facilities, could improve predictions.
- Testing with a larger, representative dataset and cross-validation would help assess how well the model generalizes to unseen properties.
- The current evaluation does not guarantee real-world prediction accuracy.

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
