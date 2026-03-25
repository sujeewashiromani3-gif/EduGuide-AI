import streamlit as st
from model import predict_student
from advisor import generate_full_advice

# Page config
st.set_page_config(page_title="EduGuide AI", layout="centered")

# Custom UI styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        text-align: center;
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🎓 EduGuide AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Smart Academic Advisor for Students</p>", unsafe_allow_html=True)

st.write("---")

# Input section
st.subheader("📥 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    math = st.slider("Math Marks", 0, 100, 50)
    science = st.slider("Science Marks", 0, 100, 50)

with col2:
    english = st.slider("English Marks", 0, 100, 50)
    attendance = st.slider("Attendance (%)", 0, 100, 75)

interest = st.selectbox(
    "Interest",
    ["Technology", "Arts", "Business"]
)

st.write("")

# Button
if st.button("🚀 Analyze Student"):

    # Prediction
    level = predict_student(math, science, english, attendance)

    # Advice
    advice = generate_full_advice(level, interest, math, science, english)

    st.success("✅ Analysis Complete!")

    st.write("---")

    # Results
    st.markdown("### 📊 Performance Level")
    st.info(level)

    st.markdown("### 📚 Study Plan")
    st.write(advice["study_plan"])

    st.markdown("### 📖 Subjects")
    st.write(", ".join(advice["subjects"]))

    st.markdown("### 💼 Career Advice")
    st.write(advice["career"])

    st.markdown("### 🎓 Recommended A/L Stream")
    st.write(advice["stream"])

    st.markdown("### 🤖 AI Explanation")
    st.write(advice["explanation"])