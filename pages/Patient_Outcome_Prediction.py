import streamlit as st
from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Outcome Prediction")

st.title("📊 Outcome Prediction")

age = st.number_input("Age", 1, 100)
severity = st.slider("Severity (1-10)", 1, 10)

if st.button("Predict Outcome"):

    score = (10 - severity) * 10 - (age * 0.3)

    if score > 60:
        st.success("High Recovery Chance")
    elif score > 30:
        st.warning("Moderate Recovery Chance")
    else:
        st.error("Low Recovery Chance")
