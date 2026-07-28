import pandas as pd
import numpy as np
from pathlib import Path


def load_data(path):
    """Load dataset"""
    return pd.read_csv(path)


def clean_price(df):
    """Convert price to numeric"""

    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    return df


def clean_milage(df):
    """Convert mileage to numeric"""

    df["milage"] = (
        df["milage"]
        .astype(str)
        .str.replace(r"[^\d]", "", regex=True)
    )

    df["milage"] = pd.to_numeric(df["milage"], errors="coerce")

    return df


def create_vehicle_age(df):

    current_year = 2026

    df["vehicle_age"] = current_year - df["model_year"]

    return df


def clean_missing(df):

    cat_cols = df.select_dtypes(exclude=["number"]).columns

    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    num_cols = df.select_dtypes(include=["number"]).columns

    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    return df


def remove_duplicates(df):

    return df.drop_duplicates()


def preprocess(df):

    df = remove_duplicates(df)

    df = clean_price(df)

    df = clean_milage(df)

    df = create_vehicle_age(df)

    df = clean_missing(df)

    return df


if __name__ == "__main__":

    df = load_data(r"D:\MACHINE LEARNING\Car_price_Prediction\data\used_cars.csv")

    df = preprocess(df)

    print(df.head())

    print(df.info())

    #from pathlib import Path

    # Create output directory if it doesn't exist
    output_dir = Path(__file__).resolve().parent.parent / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    df.to_csv(output_dir / "cleaned_used_cars.csv", index=False)

    print("✅ Dataset saved successfully!")