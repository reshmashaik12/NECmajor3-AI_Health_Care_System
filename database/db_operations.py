from database.db import get_connection
from datetime import datetime

# ---------------- DISEASE PREDICTIONS ----------------

def save_prediction(patient_id, disease_type, result, confidence):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO disease_predictions
    (patient_id, disease_type, result, confidence, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (
        patient_id,
        disease_type,
        str(result),
        confidence,
        str(datetime.now())
    ))

    conn.commit()
    conn.close()


def get_predictions(patient_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM disease_predictions
    WHERE patient_id=?
    ORDER BY id DESC
    """, (patient_id,))

    data = cur.fetchall()
    conn.close()
    return data

# ---------------- APPOINTMENTS ----------------

def get_all_doctors():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, name, specialization, experience, phone
    FROM doctors
    ORDER BY name
    """)

    data = cur.fetchall()
    conn.close()
    return data


def add_appointment(patient_id, doctor_id, date, notes):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO appointments
    (patient_id, doctor_id, appointment_date, status, notes)
    VALUES (?, ?, ?, ?, ?)
    """, (patient_id, doctor_id, date, "Pending", notes))

    conn.commit()
    conn.close()


def get_booked_appointment_times(doctor_id, appointment_date):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT appointment_date
    FROM appointments
    WHERE doctor_id=?
    AND appointment_date LIKE ?
    AND status != 'Cancelled'
    """, (doctor_id, f"{appointment_date}%"))

    booked_times = []

    for row in cur.fetchall():
        value = row["appointment_date"]
        if " " in value:
            booked_times.append(value.split(" ", 1)[1])

    conn.close()
    return booked_times


def get_doctor_appointments(doctor_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM appointments
    WHERE doctor_id=?
    """, (doctor_id,))

    data = cur.fetchall()
    conn.close()
    return data


def get_patient_appointments(patient_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM appointments
    WHERE patient_id=?
    """, (patient_id,))

    data = cur.fetchall()
    conn.close()
    return data


# ---------------- MEDICAL HISTORY ----------------

def add_medical_history(patient_id, disease, medications, allergies, record_date):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO medical_history
    (patient_id, disease, medications, allergies, record_date)
    VALUES (?, ?, ?, ?, ?)
    """, (
        patient_id,
        disease,
        medications,
        allergies,
        record_date
    ))

    conn.commit()
    conn.close()


def get_medical_history(patient_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT disease, medications, allergies, record_date
    FROM medical_history
    WHERE patient_id=?
    ORDER BY record_date DESC, id DESC
    """, (patient_id,))

    data = cur.fetchall()
    conn.close()
    return data
