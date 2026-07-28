import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/vehicle_price_model.pkl")
df = pd.read_csv("data/processed/cleaned_used_cars.csv")

st.title("🚗 Used Vehicle Price Prediction")

brand = st.selectbox("Brand", sorted(df["brand"].unique()))

models = sorted(df[df["brand"] == brand]["model"].unique())

model_name = st.selectbox("Model", models)

fuel = st.selectbox(
    "Fuel Type",
    sorted(df["fuel_type"].dropna().unique())
)

transmission = st.selectbox(
    "Transmission",
    sorted(df["transmission"].dropna().unique())
)

ext_col = st.selectbox(
    "Exterior Color",
    sorted(df["ext_col"].dropna().unique())
)

int_col = st.selectbox(
    "Interior Color",
    sorted(df["int_col"].dropna().unique())
)

year = st.number_input(
    "Model Year",
    1990,
    2026,
    2020
)

milage = st.number_input(
    "Mileage",
    0,
    300000,
    40000
)

engine = st.text_input(
    "Engine",
    "2.0L"
)

accident = st.selectbox(
    "Accident",
    [
        "None reported",
        "At least 1 accident or damage reported"
    ]
)

clean_title = st.selectbox(
    "Clean Title",
    [
        "Yes",
        "No"
    ]
)

if st.button("Predict Price"):

    input_df = pd.DataFrame({

        "brand":[brand],

        "model":[model_name],

        "model_year":[year],

        "milage":[milage],

        "fuel_type":[fuel],

        "engine":[engine],

        "transmission":[transmission],

        "ext_col":[ext_col],

        "int_col":[int_col],

        "accident":[accident],

        "clean_title":[clean_title]

    })

    input_df["vehicle_age"] = 2026 - input_df["model_year"]

    input_df["engine_size"] = (
        input_df["engine"]
        .str.extract(r'(\d+\.\d+)')
        .astype(float)
    )

    input_df["engine_size"] = input_df["engine_size"].fillna(2.0)

    input_df["accident"] = input_df["accident"].map({
        "None reported":0,
        "At least 1 accident or damage reported":1
    })

    input_df["clean_title"] = input_df["clean_title"].map({
        "Yes":1,
        "No":0
    })

    input_df = input_df.drop(columns=["engine", "model_year"])

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Price: ${prediction:,.2f}")