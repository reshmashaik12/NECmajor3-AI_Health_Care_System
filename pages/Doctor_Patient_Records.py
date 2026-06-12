import streamlit as st
import pandas as pd
from database.db import get_connection
from utils.helpers import check_doctor, show_doctor_sidebar

check_doctor()
show_doctor_sidebar("Patient Records")

st.title("Patient Records")

conn = get_connection()

df = pd.read_sql_query(
    """
    SELECT
        id,
        name,
        email,
        age,
        gender,
        phone,
        address,
        blood_group
    FROM patients
    ORDER BY id
    """,
    conn
)

conn.close()

st.dataframe(df, use_container_width=True)
