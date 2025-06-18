import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("Heart Disease Prediction App")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200)
chol = st.number_input("Cholesterol", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar > 120 (1 = Yes, 0 = No)", [1, 0])
restecg = st.selectbox("Resting ECG (0, 1, 2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 250)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [1, 0])
oldpeak = st.number_input("ST Depression", 0.0, 10.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible)", [1, 2, 3])

if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)[0]
    st.success("Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected")
