import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_used_cars.csv")

# Create vehicle age
df["vehicle_age"] = 2026 - df["model_year"]

# Extract engine size
df["engine_size"] = (
    df["engine"]
      .astype(str)
      .str.extract(r'(\d+\.\d+)')
      .astype(float)
)

df["engine_size"] = df["engine_size"].fillna(df["engine_size"].median())

# Binary encoding
df["accident"] = df["accident"].map({
    "None reported": 0,
    "At least 1 accident or damage reported": 1
})

df["clean_title"] = df["clean_title"].map({
    "Yes": 1,
    "No": 0
})

# Features
X = df.drop(columns=["price", "engine", "model_year"])
y = df["price"]

categorical_features = [
    "brand",
    "model",
    "fuel_type",
    "transmission",
    "ext_col",
    "int_col"
]

numeric_features = [
    "milage",
    "vehicle_age",
    "engine_size",
    "accident",
    "clean_title"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numeric_features
        )
    ]
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=300,
        random_state=42
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "models/vehicle_price_model.pkl")

print("Model Saved Successfully")