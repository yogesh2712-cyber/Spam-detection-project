import streamlit as st
import pickle

st.title("📩 SMS Spam Detection")

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

msg = st.text_area("Enter SMS message")

if st.button("Predict"):
    data = vectorizer.transform([msg])
    result = model.predict(data)[0]
    if result == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")
