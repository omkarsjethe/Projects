import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import Ridge, Lasso

# Load and clean data
df = pd.read_csv("car_data.csv")
df.drop(columns=["name", "torque"], inplace=True)

# Extract numeric parts
df['mileage'] = df['mileage'].str.extract(r'(\d+\.\d+|\d+)').astype(float)
df['engine'] = df['engine'].str.extract(r'(\d+)').astype(float)
df['max_power'] = df['max_power'].str.extract(r'(\d+\.\d+|\d+)').astype(float)

# Feature engineering
df['car_age'] = 2025 - df['year']
df.drop(columns=["year"], inplace=True)

# Drop rows with missing target
df.dropna(subset=['selling_price'], inplace=True)

# Features and target
X = df.drop(columns='selling_price')
y = df['selling_price']

# Define feature types
num_cols = ['km_driven', 'mileage', 'engine', 'max_power', 'seats', 'car_age']
cat_cols = ['fuel', 'seller_type', 'transmission', 'owner']

# Pipelines
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, num_cols),
    ("cat", categorical_pipeline, cat_cols)
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge model
ridge_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", Ridge(alpha=1.0, random_state=42))
])

ridge_pipeline.fit(X_train, y_train)

# Lasso model
lasso_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", Lasso(alpha=1.0, max_iter=10000, random_state=42))
])

lasso_pipeline.fit(X_train, y_train)

# Save models
with open("ridge_model_fixed.pkl", "wb") as f:
    pickle.dump(ridge_pipeline, f)

with open("lasso_model_fixed.pkl", "wb") as f:
    pickle.dump(lasso_pipeline, f)

print("✅ Models trained and saved as 'ridge_model_fixed.pkl' and 'lasso_model_fixed.pkl'")
