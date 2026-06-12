import streamlit as st
import pandas as pd

from utils.helpers import check_doctor, show_doctor_sidebar
from database.db import get_connection

check_doctor()
show_doctor_sidebar("Appointments")

st.title("📅 Doctor Appointments")

doctor_id = st.session_state.user["id"]

conn = get_connection()

query = """
SELECT
    appointments.id,
    patients.name AS patient_name,
    patients.email AS patient_email,
    patients.phone AS patient_phone,
    appointments.appointment_date,
    appointments.status,
    appointments.notes
FROM appointments
JOIN patients ON patients.id = appointments.patient_id
WHERE appointments.doctor_id=?
ORDER BY appointments.appointment_date DESC, appointments.id DESC
"""

appointments = pd.read_sql_query(
    query,
    conn,
    params=(doctor_id,)
)

conn.close()

if appointments.empty:
    st.info("No appointments booked yet.")
else:
    st.dataframe(appointments)
