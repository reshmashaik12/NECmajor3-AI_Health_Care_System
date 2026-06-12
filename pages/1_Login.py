import streamlit as st
from utils.auth import (
    login_patient,
    login_doctor,
    reset_patient_password,
    reset_doctor_password
)

if st.session_state.get("logged_in"):
    if st.session_state.get("role") == "Patient":
        st.switch_page("pages/Patient_Dashboard.py")
    elif st.session_state.get("role") == "Doctor":
        st.switch_page("pages/Doctor_Dashboard.py")

with st.sidebar:
    st.title("AI Healthcare System")
    page = st.radio(
        "Menu",
        ["Login", "Register"],
        index=0
    )

if page == "Register":
    st.switch_page("pages/2_Register.py")

st.title("Login")

login_tab, forgot_tab = st.tabs(["Login", "Forgot Password"])

with login_tab:

    role = st.selectbox(
        "Select Role",
        ["Patient", "Doctor"]
    )

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if not email or not password:
            st.error("Please fill all fields.")
            st.stop()

        if role == "Patient":

            user = login_patient(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.role = "Patient"
                st.session_state.user = user

                st.success(
                    f"Welcome {user['name']}"
                )

                st.switch_page("pages/Patient_Dashboard.py")

            else:
                st.error("Invalid Email or Password")

        else:

            user = login_doctor(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.role = "Doctor"
                st.session_state.user = user

                st.success(
                    f"Welcome Dr. {user['name']}"
                )

                st.switch_page("pages/Doctor_Dashboard.py")

            else:
                st.error("Invalid Email or Password")

with forgot_tab:

    reset_role = st.selectbox(
        "Select Role",
        ["Patient", "Doctor"],
        key="reset_role"
    )

    reset_email = st.text_input(
        "Registered Email",
        key="reset_email"
    )
    new_password = st.text_input(
        "New Password",
        type="password",
        key="new_password"
    )
    confirm_password = st.text_input(
        "Confirm New Password",
        type="password",
        key="confirm_password"
    )

    if st.button("Reset Password"):

        if not reset_email or not new_password or not confirm_password:
            st.error("Please fill all fields.")
            st.stop()

        if new_password != confirm_password:
            st.error("Passwords do not match.")
            st.stop()

        if reset_role == "Patient":
            success = reset_patient_password(reset_email, new_password)
        else:
            success = reset_doctor_password(reset_email, new_password)

        if success:
            st.success("Password reset successful. Please login with your new password.")
        else:
            st.error("No account found with this email and role.")
