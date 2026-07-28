for col in feature_columns:

    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[feature_columns]