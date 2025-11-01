# Heart_Disease Prediction System
🩺 A machine learning project for predicting heart disease risk using patient medical data, with model explainability (SHAP) and deployment via Streamlit.
---

## 📊 Project Overview

Heart disease is one of the leading causes of death globally. This project aims to build a predictive model that assists healthcare professionals by identifying individuals at high risk early, using clinical and lifestyle attributes.

The system integrates:
- Exploratory Data Analysis (EDA)
- Machine Learning model development
- SHAP model explainability
- Streamlit web app deployment
---

## 🧩 Features
✅ Data preprocessing and transformation  
✅ Machine learning model training and evaluation 
✅ Feature importance visualization using SHAP  
✅ Interactive prediction interface with Streamlit  
✅ Easy-to-understand results for non-technical users  
---

## 🧠 Dataset
The dataset used is the **Heart Disease UCI Dataset**, containing several patient health attributes such as:

| Feature | Description |
|----------|--------------|
| age | Age of the patient |
| sex | Gender (1 = male, 0 = female) |
| cp | Chest pain type (4 values) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Serum cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 mg/dl (1 = true, 0 = false) |
| restecg | Resting electrocardiographic results |
| thalach | Maximum heart rate achieved |
| exang | Exercise-induced angina (1 = yes, 0 = no) |
| oldpeak | ST depression induced by exercise relative to rest |
| slope | The slope of the peak exercise ST segment |
| ca | Number of major vessels (0–3) colored by fluoroscopy |
| thal | Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect) |
| target | 1 = heart disease, 0 = no heart disease |
---

## 📦 Project Structure

heart-disease-prediction/
│
├── data/
│   └── heart.csv
│
├── notebooks/
│   └── Heart Disease.ipynb
│
├── models/
│   ├── heart_disease_model.pkl
│   └── scaler.pkl
│
├── app/
│   └── heart_app.py
│
├── requirements.txt
├── README.md
└── LICENSE
