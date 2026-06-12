import streamlit as st

from database.models import create_tables
from utils.helpers import initialize_session, logout

create_tables()
initialize_session()

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide"
)

# ================= SIDEBAR =================

with st.sidebar:

    st.title("🏥 AI Healthcare System")

    if st.session_state.logged_in:

        st.success(f"{st.session_state.role} Logged In")

        st.write("👤", st.session_state.user["name"])

        if st.button("Logout"):
            logout()
            st.rerun()

        st.markdown("---")

        role = st.session_state.role

        # ---------------- PATIENT MENU ----------------
        if role == "Patient":

            page = st.radio(
                "Patient Menu",
                [
                    "Dashboard",
                    "Profile",
                    "Appointments",
                    "Disease Prediction",
                    "Treatment Recommendation",
                    "Outcome Prediction",
                    "Medical History",
                    "Lab Reports",
                    "Chatbot"
                ]
            )

        # ---------------- DOCTOR MENU ----------------
        else:

            page = st.radio(
                "Doctor Menu",
                [
                    "Dashboard",
                    "Appointments",
                    "Patient Records",
                    "Prescriptions",
                    "Analytics",
                    "Emergency Alerts",
                    "Reports"
                ]
            )

    else:

        page = st.radio(
            "Menu",
            ["Login", "Register"]
        )

# ================= PAGE ROUTING =================

# ---------------- HOME ----------------
if page == "Home":
    st.title("🏥 AI Healthcare System")
    st.info("Please Login or Register to continue")

# ---------------- LOGIN ----------------
if page == "Login":
    st.switch_page("pages/1_Login.py")

# ---------------- REGISTER ----------------
elif page == "Register":
    st.switch_page("pages/2_Register.py")

# ================= PATIENT PAGES =================

elif page == "Dashboard":
    if st.session_state.role == "Patient":
        st.switch_page("pages/Patient_Dashboard.py")
    else:
        st.switch_page("pages/Doctor_Dashboard.py")

elif page == "Profile":
    st.switch_page("pages/Patient_Profile.py")

elif page == "Appointments":
    if st.session_state.role == "Patient":
        st.switch_page("pages/Patient_Appointments.py")
    else:
        st.switch_page("pages/Doctor_Appointments.py")

elif page == "Disease Prediction":
    st.switch_page("pages/Patient_Disease_Prediction.py")

elif page == "Treatment Recommendation":
    st.switch_page("pages/Patient_Treatment_Recommendation.py")

elif page == "Outcome Prediction":
    st.switch_page("pages/Patient_Outcome_Prediction.py")

elif page == "Medical History":
    st.switch_page("pages/Patient_Medical_History.py")

elif page == "Lab Reports":
    st.switch_page("pages/Patient_Lab_Reports.py")

elif page == "Chatbot":
    st.switch_page("pages/Patient_Chatbot.py")

# ================= DOCTOR PAGES =================

elif page == "Patient Records":
    st.switch_page("pages/Doctor_Patient_Records.py")

elif page == "Prescriptions":
    st.switch_page("pages/Doctor_Prescriptions.py")

elif page == "Analytics":
    st.switch_page("pages/Doctor_Analytics.py")

elif page == "Emergency Alerts":
    st.switch_page("pages/Doctor_Emergency_Alerts.py")

elif page == "Reports":
    st.switch_page("pages/Doctor_Reports.py")
