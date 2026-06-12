import streamlit as st
from utils.helpers import check_patient, show_patient_sidebar

check_patient()
show_patient_sidebar("Chatbot")

st.title("AI Healthcare Chatbot")

st.markdown("Ask any health-related question")

question = st.text_input("Enter your query")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def get_response(q):

    q = q.lower().strip()
    q = (
        q.replace("feaver", "fever")
        .replace("stomack", "stomach")
        .replace("head ache", "headache")
        .replace("bp", "blood pressure")
    )

    greetings = [
        "hi",
        "hii",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if q in greetings:
        return "Hello! How can I help you with your health today?"

    if "thank" in q:
        return "You're welcome. Take care!"

    emergency_keywords = [
        "chest pain",
        "breathing trouble",
        "shortness of breath",
        "unconscious",
        "severe bleeding",
        "stroke",
        "heart attack"
    ]

    if any(keyword in q for keyword in emergency_keywords):
        return "This may be an emergency. Please seek urgent medical help immediately."

    responses = [
        (
            ["fever", "temperature", "high temp", "body heat"],
            "For fever, drink fluids, rest, and monitor temperature. Consult a doctor if fever is above 103°F, lasts more than 2 days, or comes with breathing trouble, rash, severe weakness, or confusion."
        ),
        (
            ["headache", "head pain", "migraine"],
            "Headache may happen due to stress, dehydration, lack of sleep, eye strain, or migraine. Drink water, rest in a quiet place, and consult a doctor if it is severe, sudden, repeated, or with vomiting/vision problems."
        ),
        (
            ["cold", "cough", "sneezing", "runny nose", "sore throat"],
            "For cold or cough, take warm fluids, rest, and avoid cold drinks. Consult a doctor if cough lasts more than a week, fever is high, or you have chest pain or breathing difficulty."
        ),
        (
            ["stomach", "abdominal", "gastric", "acidity", "vomit", "vomiting", "nausea"],
            "Stomach pain, vomiting, or acidity can have many causes. Drink small sips of water, eat light food, and avoid spicy/oily food. See a doctor if pain is severe, repeated, or with blood, fever, or dehydration."
        ),
        (
            ["diarrhea", "loose motion", "motions"],
            "For diarrhea, drink ORS or plenty of fluids to avoid dehydration. Eat light food. Consult a doctor if it lasts more than 24-48 hours, or if there is blood, high fever, or severe weakness."
        ),
        (
            ["diabetes", "sugar", "glucose"],
            "For diabetes care, monitor glucose regularly, reduce sugary foods, exercise, and take medicines as prescribed. Consult a doctor if sugar is very high/low or symptoms like excess thirst, urination, or weakness appear."
        ),
        (
            ["blood pressure", "hypertension", "low pressure", "high pressure"],
            "For blood pressure issues, check BP regularly, reduce salt, avoid stress, and take prescribed medicines. Seek medical help if BP is very high with headache, chest pain, dizziness, or breathing difficulty."
        ),
        (
            ["heart", "cholesterol", "palpitation"],
            "For heart health, avoid smoking, reduce oily foods, exercise regularly, and monitor BP/cholesterol. Chest pain, sweating, or breathing trouble needs urgent care."
        ),
        (
            ["kidney", "urine", "burning urination", "urination"],
            "Kidney or urine problems need proper testing. Drink water unless a doctor restricted fluids. Consult a doctor for burning urine, swelling, reduced urine, severe back pain, or abnormal kidney reports."
        ),
        (
            ["skin", "rash", "itching", "allergy"],
            "For mild itching or rash, avoid scratching and note any new food, medicine, or product used. Consult a doctor if rash spreads, has swelling, fever, pus, or breathing difficulty."
        ),
        (
            ["diet", "food", "weight loss", "healthy eating"],
            "A healthy diet usually includes vegetables, fruits, pulses/protein, whole grains, and enough water. Reduce fried food, excess sugar, and packaged snacks."
        ),
        (
            ["sleep", "insomnia", "not sleeping"],
            "For better sleep, keep a fixed sleep time, avoid phone/caffeine before bed, and keep the room calm. If poor sleep continues, discuss it with a doctor."
        ),
        (
            ["water", "dehydration", "drink"],
            "Drink enough water through the day. Signs of dehydration include dark urine, dizziness, dry mouth, and weakness."
        ),
        (
            ["appointment", "doctor", "consult"],
            "You can book an appointment from the Appointments page by selecting an available doctor, your problem, date, and symptoms."
        ),
        (
            ["medicine", "tablet", "dose"],
            "Please take medicines only as prescribed by a doctor. Do not start, stop, or change dosage without medical advice."
        ),
        (
            ["pregnancy", "pregnant"],
            "During pregnancy, consult a gynecologist for any medicine, pain, bleeding, fever, vomiting, or unusual symptoms."
        )
    ]

    for keywords, answer in responses:
        if any(keyword in q for keyword in keywords):
            return answer

    return "I can answer basic health questions like fever, headache, cough, stomach pain, diabetes, blood pressure, diet, sleep, and appointments. For accurate diagnosis, please consult a medical professional."


if st.button("Ask"):

    if not question.strip():
        st.error("Please enter your query.")
        st.stop()

    answer = get_response(question)

    st.session_state.chat_history.append((question, answer))

for q, a in reversed(st.session_state.chat_history):

    st.markdown(f"**You:** {q}")
    st.markdown(f"**AI:** {a}")
    st.markdown("---")
