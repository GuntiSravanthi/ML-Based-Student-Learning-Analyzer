import streamlit as st
import pickle
import numpy as np

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Student Risk Prediction",
    page_icon="🎓",
    layout="centered"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            height: 3em;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
        }
        .stNumberInput>div>div>input {
            border-radius: 10px;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: gray;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- LOAD MODEL -------------------
model = pickle.load(open("student_risk_model.pkl", "rb"))

# ------------------- TITLE -------------------
st.markdown('<div class="title">🎓 Student Risk Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered Academic Risk Detection</div>', unsafe_allow_html=True)

st.write("")

# ------------------- INPUT SECTION -------------------
col1, col2 = st.columns(2)

with col1:
    study_hours = st.number_input("📚 Study Hours", min_value=0.0, max_value=15.0, step=0.5)

with col2:
    attendance = st.number_input("📅 Attendance (%)", min_value=0.0, max_value=100.0, step=1.0)

previous_marks = st.number_input("📝 Previous Marks", min_value=0.0, max_value=100.0, step=1.0)

st.write("")

# ------------------- PREDICT BUTTON -------------------
if st.button("Predict Risk Level"):

    input_data = np.array([[study_hours, attendance, previous_marks]])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.write("")
    st.write("### Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ High Risk Student")
    else:
        st.success("✅ Low Risk Student")

    st.info(f"Risk Probability: {probability:.2f}")
