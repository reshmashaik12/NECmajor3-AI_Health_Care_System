from database.db import get_connection
from database.models import create_tables
import bcrypt

create_tables()

# ---------------- HASH PASSWORD ----------------

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# ---------------- PATIENT REGISTER ----------------

def register_patient(name, email, password, age, gender, phone, address, blood_group):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
        INSERT INTO patients
        (name, email, password, age, gender, phone, address, blood_group)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            email,
            hash_password(password),
            age,
            gender,
            phone,
            address,
            blood_group
        ))

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()

# ---------------- PATIENT LOGIN ----------------

def login_patient(email, password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients WHERE email=?", (email,))
    user = cur.fetchone()
    conn.close()

    if user and check_password(password, user["password"]):
        return dict(user)

    return None


def reset_patient_password(email, new_password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE patients SET password=? WHERE email=?",
        (hash_password(new_password), email)
    )

    conn.commit()
    updated = cur.rowcount > 0
    conn.close()

    return updated

# ---------------- DOCTOR REGISTER ----------------

def register_doctor(name, email, password, specialization, experience, phone):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
        INSERT INTO doctors
        (name, email, password, specialization, experience, phone)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            email,
            hash_password(password),
            specialization,
            experience,
            phone
        ))

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()

# ---------------- DOCTOR LOGIN ----------------

def login_doctor(email, password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM doctors WHERE email=?", (email,))
    user = cur.fetchone()
    conn.close()

    if user and check_password(password, user["password"]):
        return dict(user)

    return None


def reset_doctor_password(email, new_password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE doctors SET password=? WHERE email=?",
        (hash_password(new_password), email)
    )

    conn.commit()
    updated = cur.rowcount > 0
    conn.close()

    return updated
