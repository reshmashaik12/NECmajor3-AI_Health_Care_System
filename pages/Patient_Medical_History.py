import streamlit as st
import pandas as pd

from utils.helpers import check_patient, show_patient_sidebar

from database.db_operations import (
    add_medical_history,
    get_medical_history
)

check_patient()
show_patient_sidebar("Medical History")

st.title("📋 Medical History")

patient_id = st.session_state.user["id"]

disease = st.text_input(
    "Disease"
)

medications = st.text_area(
    "Medications"
)

allergies = st.text_area(
    "Allergies"
)

record_date = st.date_input(
    "Date"
)

if st.button("Save History"):

    add_medical_history(
        patient_id,
        disease,
        medications,
        allergies,
        str(record_date)
    )

    st.success(
        "History Saved"
    )

history = get_medical_history(
    patient_id
)

if history:

    st.subheader(
        "Previous Records"
    )

    st.dataframe(
        pd.DataFrame(history)
    )
