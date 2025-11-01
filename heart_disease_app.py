import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import time

# ---------------------------------------------------------------------
# HOW TO RUN:
# 1️⃣ cd <directory where this file is saved
# 2️⃣ streamlit run heart_app.py
# Example:
# cd C:\Users\DELL\Jupyter\capstone\Heart_disease
# streamlit run heart_app.py
# ---------------------------------------------------------------------

# Streamlit App
st.set_page_config(page_title="Heart Disease Prediction", page_icon="🩺", layout="centered")
st.title("🥼🩺 Heart Disease Prediction App")
st.info("This app predicts whether a patient is likely to have heart disease based on medical attributes.")

# Load trained model
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load("scaler.pkl")  # 🔹 Use the same scaler from training

# Sidebar Inputs
with st.sidebar:
    st.header("Input Patient Details")
    age = st.slider("Age", 28, 78, 40)
    sex = st.selectbox("Gender", ["Male", "Female"])
    cp = st.selectbox("Chest pain type - cp", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
    trestbps = st.slider("Resting blood pressure -trestbps (mm Hg)", 94, 200, 120)
    chol = st.slider("Serum cholesterol - chol (mg/dl)", 125, 565, 295)
    fbs = st.selectbox("Fasting blood sugar - fbs > 120 (mg/dl)", ["Yes", "No"])
    restecg = st.selectbox("Resting electrocardiographic results - restecg", [
        "Normal", 
        "Having ST-T wave abnormality",
        "Showing probable or definite left ventricular hypertrophy"])
    thalach = st.slider("Maximum heart rate achieved - thalach", 71, 202, 150)
    exang = st.selectbox("Exercise induced angina - exang", ["Yes", "No"])
    oldpeak = st.slider("ST depression induced by exercise relative to rest - oldpeak", 0.0, 6.2, 2.9)
    slope = st.selectbox("Slope of peak exercise ST segment - slope", ["Upsloping", "Flat", "Downsloping"])
    ca = st.slider("Number of major vessels colored by fluoroscopy - ca", 0, 3, 1)
    thal = st.selectbox("Thalassemia type - thal", ["Normal", "Fixed defect", "Reversible defect"])

# Encode categorical values into numeric codes
data = {
    'age': age,
    'sex': 1 if sex == "Male" else 0,
    'cp': {"Typical angina": 0, "Atypical angina": 1, "Non-anginal pain": 2, "Asymptomatic": 3}[cp],
    'fbs' : 1 if fbs == "Yes" else 0, 
    'restecg' : {"Normal": 0, "Having ST-T wave abnormality": 1, 
                "Showing probable or definite left ventricular hypertrophy": 2}[restecg], 
    'thalach' : thalach, 
    'exang' : 1 if exang == "Yes" else 0, 
    'slope' : {"Upsloping": 0, "Flat": 1, "Downsloping": 2}[slope], 
    'ca' : ca, 
    'thal' : {"Normal": 0, "Fixed defect": 1, "Reversible defect": 2}[thal], 
    'trestbps_log' : np.log1p(trestbps), 
    'chol_log' : np.log1p(chol), 
    'oldpeak_log' : np.log1p(oldpeak + 1) 
}

# Convert to DataFrame
input_df = pd.DataFrame(data, index=[0])

st.write("### Patient Input Summary")
st.dataframe(input_df)

# Scale using pre-fitted scaler
scaled_input = scaler.transform(input_df)

# Prediction
if st.button("🩺 Check Result"):
    progress_text = "Analyzing patient's heart condition..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.015)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()

    prediction = model.predict(input_df)
    if prediction == 1:
        st.error("😥 Sorry, this result indicates that the patient **may have heart disease.**")
        st.warning("Please consult a medical professional for further diagnosis.")
    else:
        st.success("😊 Good news! The model predicts **no sign of heart disease.**")
        st.balloons()

st.caption("Developed by Group 12 — Insight Innovators 💡")
