categorical = pd.DataFrame({
    "brand":[brand],
    "model":[model_name],
    "fuel_type":[fuel_type],
    "transmission":[transmission]
})

categorical = pd.get_dummies(categorical)

input_data = pd.concat(
    [input_data, categorical],
    axis=1
)