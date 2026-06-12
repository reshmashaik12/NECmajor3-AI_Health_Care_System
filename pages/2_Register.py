import streamlit as st
from utils.auth import (
    register_patient,
    register_doctor
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
        index=1
    )

if page == "Login":
    st.switch_page("pages/1_Login.py")

st.title("📝 Register")

role = st.selectbox(
    "Register As",
    ["Patient", "Doctor"]
)

st.markdown("---")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input(
    "Password",
    type="password"
)

phone = st.text_input("Phone Number")

# --------------------
# PATIENT
# --------------------

if role == "Patient":

    age = st.number_input(
        "Age",
        1,
        120
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    address = st.text_area(
        "Address"
    )

    blood_group = st.selectbox(
        "Blood Group",
        [
            "A+","A-",
            "B+","B-",
            "AB+","AB-",
            "O+","O-"
        ]
    )

    if st.button("Register Patient"):

        success = register_patient(
            name,
            email,
            password,
            age,
            gender,
            phone,
            address,
            blood_group
        )

        if success:
            st.success(
                "Patient Registration Successful"
            )
            st.info("Please login with your patient account.")
            st.switch_page("pages/1_Login.py")
        else:
            st.error(
                "Email already exists"
            )

# --------------------
# DOCTOR
# --------------------

else:

    specialization = st.text_input(
        "Specialization"
    )

    experience = st.number_input(
        "Experience (Years)",
        0,
        50
    )

    if st.button("Register Doctor"):

        success = register_doctor(
            name,
            email,
            password,
            specialization,
            experience,
            phone
        )

        if success:
            st.success(
                "Doctor Registration Successful"
            )
            st.info("Please login with your doctor account.")
            st.switch_page("pages/1_Login.py")
        else:
            st.error(
                "Email already exists"
            )
