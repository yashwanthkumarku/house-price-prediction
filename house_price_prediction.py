
from pathlib import Path

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from pathlib import Path


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


# 1. Load the dataset



# Load dataset from the script's folder
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "house_data.csv"

print("Python script location:", Path(__file__).resolve())
print("CSV path:", csv_path)
print("CSV file exists:", csv_path.exists())

df = pd.read_csv(csv_path)

print("\nDataset loaded successfully!")
print(df.head())

# 2. Basic data preprocessing
print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where the target price is missing
df = df.dropna(subset=["price"])

# Separate input features (X) and target (y)
X = df[["area", "bedrooms", "location"]]
y = df["price"]

# 3. Identify numerical and categorical columns
numeric_features = ["area", "bedrooms"]
categorical_features = ["location"]

# 4. Preprocessing
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# 5. Create the machine learning pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# 6. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 7. Train the model
model.fit(X_train, y_train)

print("\nModel training completed successfully!")

# 8. Make predictions on test data
y_pred = model.predict(X_test)

# 9. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"Mean Absolute Error (MAE): ₹{mae:,.2f}")
print(f"Mean Squared Error (MSE): {mse:,.2f}")
print(f"Root Mean Squared Error (RMSE): ₹{rmse:,.2f}")
print(f"R² Score: {r2:.4f}")

# 10. Predict the price of a new house

print("\n--- Predict House Price ---")

area = float(input("Enter house area in square feet: "))
bedrooms = int(input("Enter number of bedrooms: "))

location = input(
    "Enter location (Bangalore, Mysore, Tumkur): "
).strip().title()

valid_locations = ["Bangalore", "Mysore", "Tumkur"]

if location not in valid_locations:
    print("Invalid location. Please choose Bangalore, Mysore, or Tumkur.")
else:
    new_house = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "location": [location]
    })

    predicted_price = model.predict(new_house)[0]

    print(f"\nEstimated house price: ₹{predicted_price:,.2f}")
    print("Note: This is a model estimate, not a guaranteed market price.")
