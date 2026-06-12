import streamlit as st
from fpdf import FPDF
import os
from database.db import get_connection
from utils.helpers import check_doctor, show_doctor_sidebar

check_doctor()
show_doctor_sidebar("Reports")

st.title("📄 Generate Patient Report")

patient_id = st.number_input("Patient ID", 1)

if st.button("Generate Report"):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    patient = cur.fetchone()

    cur.execute("""
        SELECT * FROM disease_predictions
        WHERE patient_id=?
        ORDER BY id DESC LIMIT 1
    """, (patient_id,))

    prediction = cur.fetchone()
    conn.close()

    if patient and prediction:

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, "AI Healthcare Report", ln=True)

        pdf.cell(200, 10, f"Name: {patient['name']}", ln=True)
        pdf.cell(200, 10, f"Disease: {prediction['disease_type']}", ln=True)
        pdf.cell(200, 10, f"Result: {prediction['result']}", ln=True)
        pdf.cell(200, 10, f"Date: {prediction['created_at']}", ln=True)

        os.makedirs("reports/generated_reports", exist_ok=True)

        file_path = f"reports/generated_reports/report_{patient_id}.pdf"
        pdf.output(file_path)

        st.success("Report Generated")
        st.download_button(
            "Download Report",
            open(file_path, "rb"),
            file_name="patient_report.pdf"
        )

    else:
        st.error("No data found")
