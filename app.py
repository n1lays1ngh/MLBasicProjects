import streamlit as st
import joblib

# Load model
model = joblib.load('spam_classifier.pkl')

# App title and banner
st.title("📩 Spam Classifier App")
st.write("Enter a message and find out if it's spam or not!")

# User input
message = st.text_area("💬 Your Message", "")

# Predict button
if st.button("🔍 Classify"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: {label}")

