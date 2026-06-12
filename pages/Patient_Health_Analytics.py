import streamlit as st
import pandas as pd

from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Health Analytics")

st.title("📊 Health Analytics")

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],
    "Health Score": [
        60,
        65,
        70,
        75,
        82
    ]
}

df = pd.DataFrame(data)

st.line_chart(
    df.set_index("Month")
)

st.dataframe(df)
