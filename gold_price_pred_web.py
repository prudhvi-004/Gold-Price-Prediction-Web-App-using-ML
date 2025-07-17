import streamlit as st
import numpy as np
import pickle

# Load model
with open("C:/Users/prudh/OneDrive/Desktop/Machine Learning/Projects/Gold Price Prediction/gold.sav", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Gold Price Predictor", layout="centered")
st.title("Gold Price Prediction")

# Input fields
spx = st.number_input("SPX", value=1200.0)
us_oil = st.number_input("USO", value=90.0)
slv = st.number_input("SLV", value=20.0)
eur_usd = st.number_input("EUR/USD", value=1.2)

# Predict
if st.button("Predict"):
    input_data = np.array([[spx, us_oil, slv, eur_usd]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Gold Price: ${prediction[0]:.2f}")