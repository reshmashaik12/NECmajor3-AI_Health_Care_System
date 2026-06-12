import streamlit as st
import os

from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Lab Reports")

st.title("🧪 Lab Reports")

os.makedirs(
    "uploads/lab_reports",
    exist_ok=True
)

uploaded_file = st.file_uploader(
    "Upload Report",
    type=["pdf","jpg","png"]
)

if uploaded_file:

    filepath = os.path.join(
        "uploads/lab_reports",
        uploaded_file.name
    )

    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Report Uploaded")

files = os.listdir(
    "uploads/lab_reports"
)

if files:

    st.subheader("Uploaded Reports")

    for file in files:

        with open(
            os.path.join(
                "uploads/lab_reports",
                file
            ),
            "rb"
        ) as f:

            st.download_button(
                label=file,
                data=f,
                file_name=file
            )
