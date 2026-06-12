import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import get_connection
from utils.helpers import check_doctor, show_doctor_sidebar

check_doctor()
show_doctor_sidebar("Analytics")

st.title("📊 Analytics Dashboard")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT disease_type, result FROM disease_predictions",
    conn
)

conn.close()

if not df.empty:

    fig = px.histogram(
        df,
        x="disease_type",
        color="result"
    )

    st.plotly_chart(fig)

    st.dataframe(df)

else:
    st.info("No Data Available")
