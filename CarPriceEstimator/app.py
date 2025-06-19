import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Car Price Estimator", layout="centered")
st.title("🚘 Used Car Price Estimator")

# Load model dynamically
model_choice = st.selectbox("Choose Prediction Model", ["Ridge", "Lasso"])
model_path = "ridge_model_fixed.pkl" if model_choice == "Ridge" else "lasso_model_fixed.pkl"

@st.cache_resource
def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)

model = load_model(model_path)

# Input fields
st.subheader("Enter Car Details:")

km_driven = st.number_input("Kilometers Driven", 0, 1000000, step=1000)
mileage = st.number_input("Mileage (kmpl)", 0.0, 100.0, step=0.5)
engine = st.number_input("Engine Capacity (CC)", 500, 5000, step=100)
max_power = st.number_input("Max Power (BHP)", 10.0, 400.0, step=1.0)
seats = st.selectbox("Seats", [2, 4, 5, 6, 7])
car_age = st.slider("Car Age (Years)", 0, 30, 5)

fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual', 'Trustmark Dealer'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
owner = st.selectbox("Ownership", ['First Owner', 'Second Owner', 'Third Owner',
                                   'Fourth & Above Owner', 'Test Drive Car'])

# Convert to DataFrame
input_df = pd.DataFrame({
    'km_driven': [km_driven],
    'mileage': [mileage],
    'engine': [engine],
    'max_power': [max_power],
    'seats': [seats],
    'car_age': [car_age],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'transmission': [transmission],
    'owner': [owner]
})

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {round(prediction, 2)} Lakhs")
