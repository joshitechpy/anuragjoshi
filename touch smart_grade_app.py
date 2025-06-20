import streamlit as st

st.title("📊 Smart Grade Analyzer")

st.subheader("Enter Marks for Each Subject")
math = st.number_input("Maths", min_value=0, max_value=100)
science = st.number_input("Science", min_value=0, max_value=100)
english = st.number_input("English", min_value=0, max_value=100)

if st.button("Calculate Grade"):
    avg = (math + science + english) / 3

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"

    st.success(f"🎯 Your Grade: {grade}")

import plotly.express as px

fig = px.pie(
    names=["Math", "Science", "English"],
    values=[math, science, english],
    title="Subject-wise Score Distribution"
)
st.plotly_chart(fig)
    feedback = {
        "A+": "🔥 Outstanding! You nailed it!",
        "A": "🎉 Great job! Keep going strong.",
        "B": "😊 Good! But you’ve got more potential.",
        "C": "📈 Keep practicing — growth ahead.",
        "D": "💪 Don't give up — work hard and bounce back!"
    }
    st.info(feedback[grade])
    if grade in ["A+", "A"]:
        st.balloons()
    elif grade == "D":
        st.warning("Try again with a growth mindset!")
