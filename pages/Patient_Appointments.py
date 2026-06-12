import streamlit as st
import pandas as pd

from utils.helpers import check_patient, show_patient_sidebar

from database.db_operations import (
    add_appointment,
    get_patient_appointments,
    get_all_doctors,
    get_booked_appointment_times
)

check_patient()
show_patient_sidebar("Appointments")

st.title("Patient Appointments")

patient_id = st.session_state.user["id"]

TIME_SLOTS = [
    "09:00 AM",
    "09:30 AM",
    "10:00 AM",
    "10:30 AM",
    "11:00 AM",
    "11:30 AM",
    "02:00 PM",
    "02:30 PM",
    "03:00 PM",
    "03:30 PM",
    "04:00 PM",
    "04:30 PM"
]

doctors = get_all_doctors()

if not doctors:
    st.info("No doctors are registered yet. Please try again later.")
    st.stop()

doctor_names = {
    f"Dr. {doc['name']} - {doc['specialization']}": doc["id"]
    for doc in doctors
}

doctor = st.selectbox(
    "Available Doctors",
    list(doctor_names.keys())
)

selected_doctor_id = doctor_names[doctor]

problem = st.selectbox(
    "What problem do you have?",
    [
        "Fever",
        "Headache",
        "Cold / Cough",
        "Stomach Pain",
        "Chest Pain",
        "Diabetes",
        "Blood Pressure",
        "Skin Problem",
        "Other"
    ]
)

if problem == "Other":
    problem = st.text_input("Enter your problem")

appointment_date = st.date_input(
    "Appointment Date"
)

booked_times = get_booked_appointment_times(
    selected_doctor_id,
    str(appointment_date)
)

available_times = [
    slot for slot in TIME_SLOTS
    if slot not in booked_times
]

if available_times:
    appointment_time = st.selectbox(
        "Available Time",
        available_times
    )
else:
    st.warning("No time slots available for this doctor on the selected date.")
    st.stop()

notes = st.text_area(
    "Describe symptoms"
)

if st.button("Book Appointment"):

    if not problem:
        st.error("Please enter your problem.")
        st.stop()

    appointment_notes = f"Problem: {problem}\nSymptoms: {notes}"

    add_appointment(
        patient_id,
        selected_doctor_id,
        f"{appointment_date} {appointment_time}",
        appointment_notes
    )

    st.success(f"Appointment booked with {doctor} at {appointment_time}")

st.subheader("My Appointments")

appointments = get_patient_appointments(
    patient_id
)

if appointments:
    st.dataframe(
        pd.DataFrame(appointments),
        use_container_width=True
    )
else:
    st.info("No appointments booked yet.")
