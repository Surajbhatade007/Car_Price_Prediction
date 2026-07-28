if st.button("Predict Price"):

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Price: £{prediction:,.2f}")


    prediction = np.expm1(model.predict(input_data)[0])