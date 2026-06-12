import streamlit as st
from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Profile")

user = st.session_state.user

st.title("👤 Patient Profile")

st.markdown("---")

st.write(f"**Name:** {user['name']}")
st.write(f"**Email:** {user['email']}")
st.write(f"**Age:** {user['age']}")
st.write(f"**Gender:** {user['gender']}")
st.write(f"**Phone:** {user['phone']}")
st.write(f"**Address:** {user['address']}")
st.write(f"**Blood Group:** {user['blood_group']}")
