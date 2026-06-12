import streamlit as st
from utils.helpers import check_doctor, show_doctor_sidebar

check_doctor()
show_doctor_sidebar("Dashboard")

user = st.session_state.user

st.title("🩺 Doctor Dashboard")

st.success(
    f"Welcome Dr. {user['name']}"
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Patients",
        "0"
    )

with col2:
    st.metric(
        "Appointments",
        "0"
    )

with col3:
    st.metric(
        "Emergency Alerts",
        "0"
    )

st.markdown("---")

st.info("""
Doctor Features

• Patient Records

• Prescriptions

• Appointments

• Treatment Recommendations

• Outcome Prediction

• Analytics

• Reports

• Emergency Alerts
""")
