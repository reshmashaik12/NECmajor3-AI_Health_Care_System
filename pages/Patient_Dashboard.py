import streamlit as st
from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Dashboard")

st.title("👨‍⚕️ Patient Dashboard")

user = st.session_state.user

st.success(
    f"Welcome {user['name']}"
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Predictions",
        "0"
    )

with col2:
    st.metric(
        "Appointments",
        "0"
    )

with col3:
    st.metric(
        "Reports",
        "0"
    )

st.markdown("---")

st.info("""
Use the sidebar to access:

• Profile

• Appointments

• Medical History

• Disease Prediction

• Treatment Recommendation

• Outcome Prediction

• Lab Reports

• Health Analytics

• Chatbot
""")
