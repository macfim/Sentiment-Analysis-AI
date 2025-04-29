import streamlit as st
import altair as alt
import plotly.express as px
import pandas as pd
import numpy as np
import requests
import json

# API endpoint
API_URL = "https://sentiment-analysis-ai-f8je.onrender.com"

# Function to predict emotions using API
def predict_emotions(docx):
    response = requests.post(f"{API_URL}/predict", json={"text": docx})
    if response.status_code == 200:
        result = response.json()
        return result["prediction"]
    return "Error"

def get_prediction_proba(docx):
    response = requests.post(f"{API_URL}/predict", json={"text": docx})
    if response.status_code == 200:
        result = response.json()
        return [list(result["probabilities"].values())]
    return [[]]

def get_emotions_with_emoji():
    response = requests.get(f"{API_URL}/emotions")
    if response.status_code == 200:
        result = response.json()
        return result["emotions_with_emoji"]
    return {"anger": "😠", "disgust": "🤮", "fear": "😨😱", "happy": "🤗", "joy": "😂", "neutral": "😐", "sad": "😔", "sadness": "😔", "shame": "😳", "surprise": "😮"}

# Main Application
def main():
    st.title("Emotion Classifier App")
    menu = ["Home"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    # Check if API is available
    try:
        response = requests.get(f"{API_URL}/")
        api_status = "API Connected" if response.status_code == 200 else "API Unavailable"
        st.sidebar.success(api_status)
    except:
        st.sidebar.error("API Unavailable")
    
    # Get emotions dictionary from API
    emotions_emoji_dict = get_emotions_with_emoji()
    
    if choice == "Home":
        st.subheader("Emotion Detection in Text")

        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label='Submit')

        if submit_text:
            col1, col2 = st.columns(2)

            prediction = predict_emotions(raw_text)
            probability = get_prediction_proba(raw_text)

            with col1:
                st.success("Original Text")
                st.write(raw_text)

                st.success("Prediction")
                emoji_icon = emotions_emoji_dict.get(prediction, "")
                st.write("{}:{}".format(prediction, emoji_icon))
                st.write("Confidence:{}".format(np.max(probability) if probability[0] else "N/A"))

            with col2:
                st.success("Prediction Probability")
                
                # Get emotion classes from API
                response = requests.get(f"{API_URL}/emotions")
                if response.status_code == 200:
                    emotions = response.json()["emotions"]
                    
                    # Create DataFrame for visualization
                    proba_df = pd.DataFrame(probability, columns=emotions)
                    proba_df_clean = proba_df.T.reset_index()
                    proba_df_clean.columns = ["emotions", "probability"]

                    fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions', y='probability', color='emotions')
                    st.altair_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()