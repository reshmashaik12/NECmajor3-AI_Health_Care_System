from database.models import create_tables
from database.db import get_connection
from utils.auth import register_doctor, register_patient


def update_doctor_profile(email, name, specialization, experience, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE doctors
    SET name=?, specialization=?, experience=?, phone=?
    WHERE email=?
    """, (name, specialization, experience, phone, email))

    conn.commit()
    conn.close()


def seed_test_users():
    create_tables()

    patient_created = register_patient(
        "Test Patient",
        "patient@test.com",
        "patient123",
        25,
        "Male",
        "9000000000",
        "Test Address",
        "O+"
    )

    doctors = [
        (
            "Aarav Sharma",
            "doctor@test.com",
            "doctor123",
            "General Medicine",
            5,
            "9000000001"
        ),
        (
            "Priya Reddy",
            "cardio@test.com",
            "doctor123",
            "Cardiology",
            8,
            "9000000002"
        ),
        (
            "Vikram Rao",
            "neuro@test.com",
            "doctor123",
            "Neurology",
            7,
            "9000000003"
        ),
        (
            "Sneha Iyer",
            "derma@test.com",
            "doctor123",
            "Dermatology",
            6,
            "9000000004"
        ),
        (
            "Rahul Mehta",
            "ortho@test.com",
            "doctor123",
            "Orthopedics",
            9,
            "9000000005"
        ),
        (
            "Ananya Nair",
            "pediatric@test.com",
            "doctor123",
            "Pediatrics",
            6,
            "9000000006"
        ),
        (
            "Kiran Das",
            "diabetes@test.com",
            "doctor123",
            "Diabetology",
            10,
            "9000000007"
        )
    ]

    created_doctors = 0

    for doctor in doctors:
        if register_doctor(*doctor):
            created_doctors += 1
        else:
            name, email, _, specialization, experience, phone = doctor
            update_doctor_profile(email, name, specialization, experience, phone)

    print("Patient account:", "created" if patient_created else "already exists")
    print("Doctor accounts created:", created_doctors)
    print("Patient login: patient@test.com / patient123")
    print("Doctor login password for sample doctors: doctor123")


if __name__ == "__main__":
    seed_test_users()
