import streamlit as st
import numpy as np
import pandas as pd
import joblib
from datetime import datetime

from utils.helpers import check_patient, show_patient_sidebar
from database.db import get_connection

check_patient()
show_patient_sidebar("Disease Prediction")

st.title("🧠 AI Disease Prediction System")

# ---------------- LOAD MODELS ----------------

diabetes_model = joblib.load("models/disease_prediction/diabetes_model.pkl")
heart_model = joblib.load("models/disease_prediction/heart_model.pkl")
kidney_model = joblib.load("models/disease_prediction/kidney_model.pkl")

DIABETES_COLUMNS = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

HEART_COLUMNS = [
    "Age", "Sex", "ChestPainType", "RestingBP",
    "Cholesterol", "FastingBS", "MaxHR", "ExerciseAngina"
]

KIDNEY_COLUMNS = [
    "Age", "BloodPressure", "SpecificGravity", "Albumin",
    "Sugar", "BloodGlucose", "BloodUrea", "SerumCreatinine",
    "Hemoglobin"
]


def predict_with_confidence(model, values, columns):
    data = pd.DataFrame([values], columns=columns)
    result = int(model.predict(data)[0])
    confidence = 0.0

    if hasattr(model, "predict_proba"):
        confidence = float(model.predict_proba(data)[0][result] * 100)

    return result, confidence

patient_id = st.session_state.user["id"]

# ---------------- SELECT DISEASE ----------------

disease = st.selectbox(
    "Select Disease",
    ["Diabetes", "Heart Disease", "Kidney Disease"]
)

# =================================================
# DIABETES
# =================================================

if disease == "Diabetes":

    st.subheader("Diabetes Prediction")

    pregnancies = st.number_input("Pregnancies", 0)
    glucose = st.number_input("Glucose", 0)
    bp = st.number_input("Blood Pressure", 0)
    skin = st.number_input("Skin Thickness", 0)
    insulin = st.number_input("Insulin", 0)
    bmi = st.number_input("BMI", 0.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0)
    age = st.number_input("Age", 1)

    if st.button("Predict Diabetes"):

        data = [
            pregnancies, glucose, bp, skin,
            insulin, bmi, dpf, age
        ]

        result, confidence = predict_with_confidence(
            diabetes_model,
            data,
            DIABETES_COLUMNS
        )

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO disease_predictions
        (patient_id, disease_type, result, confidence, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            "Diabetes",
            str(result),
            confidence,
            str(datetime.now())
        ))

        conn.commit()
        conn.close()

        if result == 1:
            st.error("⚠️ High Risk of Diabetes")
        else:
            st.success("✅ No Diabetes Risk")

# =================================================
# HEART
# =================================================

elif disease == "Heart Disease":

    st.subheader("Heart Disease Prediction")

    age = st.number_input("Age", 1)
    sex = st.selectbox("Sex (1=Male, 0=Female)", [0, 1])
    cp = st.number_input("Chest Pain Type", 0)
    bp = st.number_input("Resting BP", 0)
    chol = st.number_input("Cholesterol", 0)
    fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
    maxhr = st.number_input("Max Heart Rate", 0)
    exang = st.selectbox("Exercise Angina", [0, 1])

    if st.button("Predict Heart Disease"):

        data = [
            age, sex, cp, bp, chol, fbs, maxhr, exang
        ]

        result, confidence = predict_with_confidence(
            heart_model,
            data,
            HEART_COLUMNS
        )

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO disease_predictions
        (patient_id, disease_type, result, confidence, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            "Heart Disease",
            str(result),
            confidence,
            str(datetime.now())
        ))

        conn.commit()
        conn.close()

        if result == 1:
            st.error("⚠️ Heart Disease Risk Detected")
        else:
            st.success("✅ No Heart Disease Risk")

# =================================================
# KIDNEY
# =================================================

elif disease == "Kidney Disease":

    st.subheader("Kidney Disease Prediction")

    age = st.number_input("Age", 1)
    bp = st.number_input("Blood Pressure", 0)
    sg = st.number_input("Specific Gravity", 0.0)
    albumin = st.number_input("Albumin", 0)
    sugar = st.number_input("Sugar", 0)
    glucose = st.number_input("Blood Glucose", 0)
    urea = st.number_input("Blood Urea", 0)
    creatinine = st.number_input("Serum Creatinine", 0.0)
    hb = st.number_input("Hemoglobin", 0.0)

    if st.button("Predict Kidney Disease"):

        data = [
            age, bp, sg, albumin,
            sugar, glucose, urea,
            creatinine, hb
        ]

        result, confidence = predict_with_confidence(
            kidney_model,
            data,
            KIDNEY_COLUMNS
        )

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO disease_predictions
        (patient_id, disease_type, result, confidence, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            "Kidney Disease",
            str(result),
            confidence,
            str(datetime.now())
        ))

        conn.commit()
        conn.close()

        if result == 1:
            st.error("⚠️ Kidney Disease Risk Detected")
        else:
            st.success("✅ No Kidney Disease Risk")
