import streamlit as st
import pandas as pd
from database.db import get_connection
from utils.helpers import check_doctor, show_doctor_sidebar

check_doctor()
show_doctor_sidebar("Emergency Alerts")

st.title("🚨 Emergency Alerts")

conn = get_connection()

query = """
SELECT * FROM disease_predictions
WHERE result='1'
ORDER BY created_at DESC
"""

data = pd.read_sql_query(query, conn)

conn.close()

if len(data) == 0:
    st.success("No Emergency Cases")
else:
    st.error("High Risk Patients Detected")
    st.dataframe(data)
