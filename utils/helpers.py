import streamlit as st

def initialize_session():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    if "role" not in st.session_state:
        st.session_state.role = None


def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None


def show_patient_sidebar(current_page="Dashboard"):

    with st.sidebar:
        st.title("AI Healthcare System")
        st.success("Patient Logged In")

        if st.session_state.user:
            st.write(st.session_state.user["name"])

        if st.button("Logout"):
            logout()
            st.switch_page("pages/1_Login.py")

        st.markdown("---")

        pages = {
            "Dashboard": "pages/Patient_Dashboard.py",
            "Profile": "pages/Patient_Profile.py",
            "Appointments": "pages/Patient_Appointments.py",
            "Disease Prediction": "pages/Patient_Disease_Prediction.py",
            "Treatment Recommendation": "pages/Patient_Treatment_Recommendation.py",
            "Outcome Prediction": "pages/Patient_Outcome_Prediction.py",
            "Medical History": "pages/Patient_Medical_History.py",
            "Lab Reports": "pages/Patient_Lab_Reports.py",
            "Health Analytics": "pages/Patient_Health_Analytics.py",
            "Chatbot": "pages/Patient_Chatbot.py",
        }

        selected_page = st.radio(
            "Patient Menu",
            list(pages.keys()),
            index=list(pages.keys()).index(current_page)
        )

    if selected_page != current_page:
        st.switch_page(pages[selected_page])


def show_doctor_sidebar(current_page="Dashboard"):

    with st.sidebar:
        st.title("AI Healthcare System")
        st.success("Doctor Logged In")

        if st.session_state.user:
            st.write(f"Dr. {st.session_state.user['name']}")

        if st.button("Logout"):
            logout()
            st.switch_page("pages/1_Login.py")

        st.markdown("---")

        pages = {
            "Dashboard": "pages/Doctor_Dashboard.py",
            "Appointments": "pages/Doctor_Appointments.py",
            "Patient Records": "pages/Doctor_Patient_Records.py",
            "Prescriptions": "pages/Doctor_Prescriptions.py",
            "Analytics": "pages/Doctor_Analytics.py",
            "Emergency Alerts": "pages/Doctor_Emergency_Alerts.py",
            "Reports": "pages/Doctor_Reports.py",
        }

        selected_page = st.radio(
            "Doctor Menu",
            list(pages.keys()),
            index=list(pages.keys()).index(current_page)
        )

    if selected_page != current_page:
        st.switch_page(pages[selected_page])


def check_patient():

    if not st.session_state.logged_in or st.session_state.role != "Patient":
        st.warning("Please login as Patient")
        st.stop()


def check_doctor():

    if not st.session_state.logged_in or st.session_state.role != "Doctor":
        st.warning("Please login as Doctor")
        st.stop()

