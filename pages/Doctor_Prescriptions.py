import streamlit as st
from database.db import get_connection
from utils.helpers import check_doctor, show_doctor_sidebar

check_doctor()
show_doctor_sidebar("Prescriptions")

st.title("💊 Prescriptions")

patient_id = st.number_input(
    "Patient ID",
    1
)

prescription = st.text_area(
    "Prescription"
)

if st.button("Save Prescription"):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO prescriptions
    (
        doctor_id,
        patient_id,
        prescription,
        created_at
    )
    VALUES (?,?,?,datetime('now'))
    """,
    (
        st.session_state.user["id"],
        patient_id,
        prescription
    ))

    conn.commit()
    conn.close()

    st.success(
        "Prescription Saved"
    )
