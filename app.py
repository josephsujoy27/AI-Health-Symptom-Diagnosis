import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# App title
st.title("🩺 Symptom-Based Disease Predictor")

# Input sliders
st.subheader("Enter your symptoms (0 = No, 1 = Severe)")

fever = st.slider("Fever Level", 0.0, 1.0, 0.5)
cough = st.slider("Cough Level", 0.0, 1.0, 0.5)
fatigue = st.slider("Fatigue Level", 0.0, 1.0, 0.5)
headache = st.slider("Headache Level", 0.0, 1.0, 0.5)

# Create input array
input_data = np.array([[fever, cough, fatigue, headache]])

# Predict
if st.button("Predict Disease"):
    prediction = model.predict(input_data)
    st.success(f"🧾 Predicted Diagnosis: **{prediction[0]}**")
