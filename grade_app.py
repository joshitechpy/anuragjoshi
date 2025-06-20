import streamlit as st

st.set_page_config(page_title="ग्रेड प्रीडिक्टर", page_icon="📊")

st.title("📚 ग्रेड प्रीडिक्टर App (Anurag Style)")
st.write("नीचे अपने अंक दर्ज करें और जानिए आप क्या ग्रेड पाते! 😄")

marks = st.number_input("अपने अंक दर्ज करें (0-100)", min_value=0, max_value=100, step=1)

if st.button("ग्रेड देखो 🎯"):
    if 90 <= marks <= 100:
        st.success("🎉 Topper निकला रे तू! Grade: Excellent")
    elif 80 <= marks < 90:
        st.info("👏 अच्छा किया रे तूने! Grade: A")
    elif 70 <= marks < 80:
        st.info("👍 थोड़ी और मेहनत की ज़रूरत है! Grade: B")
    elif 60 <= marks < 70:
        st.warning("📚 पढ़ ले रे, क्या कर रहा है तू! Grade: C")
    elif 50 <= marks < 60:
        st.error("😅 तेरी आरती उतारूं क्या! Grade: D")
    else:
        st.error("😐 भाई... पढ़ाई छोड़, कोई और काम देख!")