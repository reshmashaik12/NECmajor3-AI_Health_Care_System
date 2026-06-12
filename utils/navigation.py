import streamlit as st

def show_patient_menu():

    st.sidebar.title("Patient Menu")

    return st.sidebar.radio(
        "Navigate",
        [
            "Dashboard",
            "Profile",
            "Appointments",
            "Disease Prediction",
            "Treatment",
            "Outcome",
            "Reports",
            "Chatbot"
        ]
    )


def show_doctor_menu():

    st.sidebar.title("Doctor Menu")

    return st.sidebar.radio(
        "Navigate",
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