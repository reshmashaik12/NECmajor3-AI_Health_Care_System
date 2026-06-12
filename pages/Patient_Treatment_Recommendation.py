import streamlit as st
from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Treatment Recommendation")

st.title("💊 AI Treatment Recommendation")

risk = st.selectbox(
    "Select Condition",
    ["Low Risk", "Moderate Risk", "High Risk"]
)

if st.button("Generate Recommendation"):

    if risk == "Low Risk":
        st.success("""
        ✔ Maintain healthy diet  
        ✔ Exercise daily  
        ✔ Regular checkups
        """)

    elif risk == "Moderate Risk":
        st.warning("""
        ⚠ Reduce sugar/salt  
        ⚠ Monitor health weekly  
        ⚠ Consult doctor regularly
        """)

    else:
        st.error("""
        🚨 Immediate medical attention required  
        🚨 Strict diet control  
        🚨 Continuous monitoring needed
        """)
