import streamlit as st
from joblib import load

# Load the pre-trained pipeline (ensure correct path with raw string)
pipeline = load(r'C:\DibyaSinha\Codes\AI & ML\Model 1\Main Project 2\news_classifier.joblib')

# Streamlit app setup
st.set_page_config(page_title="News Classifier", layout="centered")
st.title("📰 News Category Classifier")
st.write("Predict the **category** of news headlines using AI!")

# Sidebar information
st.sidebar.title("📌 About")
st.sidebar.info("This app uses a pre-trained machine learning model to classify news headlines into categories like Politics, Sports, Business, Tech, etc.")

# Example display (non-interactive)
st.markdown("### ✨ Example: *'Tech giants release new AI tools'*")

# User input
headline = st.text_input("Enter a news headline:", "")

# Predict button
if st.button("Predict Category"):
    if headline:
        try:
            # Predict category
            prediction = pipeline.predict([headline])[0]

            # Display result
            st.subheader("✅ Prediction Result")
            st.markdown(f"**Category:** `{prediction}`")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("⚠️ Please enter a headline to classify.")
