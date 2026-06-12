from database.db import get_connection

def init_db():

    conn = get_connection()
    cur = conn.cursor()

    # ---------------- PATIENTS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        age INTEGER,
        gender TEXT,
        phone TEXT,
        address TEXT,
        blood_group TEXT
    )
    """)

    # ---------------- DOCTORS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        specialization TEXT,
        experience INTEGER,
        phone TEXT
    )
    """)

    # ---------------- APPOINTMENTS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date TEXT,
        status TEXT,
        notes TEXT
    )
    """)

    # ---------------- DISEASE PREDICTIONS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS disease_predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        disease_type TEXT,
        result TEXT,
        confidence REAL,
        created_at TEXT
    )
    """)

    # ---------------- MEDICAL HISTORY ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS medical_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        disease TEXT,
        medications TEXT,
        allergies TEXT,
        record_date TEXT
    )
    """)

    # ---------------- PRESCRIPTIONS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doctor_id INTEGER,
        patient_id INTEGER,
        prescription TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully")


if __name__ == "__main__":
    init_db()
