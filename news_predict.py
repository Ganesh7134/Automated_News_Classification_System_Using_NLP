import streamlit as st
import numpy as np
import pickle
from streamlit_lottie import st_lottie
import json

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        gif = json.load(f)
    return gif

def load_lottie_files():
    col1, col2 , col3 = st.columns(3)
    try:
        gif1 = load_lottie_file("sports.json")
        gif2 = load_lottie_file("science.json")
        gif3 = load_lottie_file("business.json")
        with col1:
            st_lottie(gif1, speed=1, width=250, height=300)
        with col2:
            st_lottie(gif2, speed=1, width=250, height=300)
        with col3:
            st_lottie(gif3, speed=1, width=250, height=300)
            
    except:
        print("Error loading Lottie files")

# Load Lottie files initially
load_lottie_files()

st.title("Automated_News_Classification_System_Using_NLP")



x_new = [st.text_input("Enter news description to predict: ")]


def result():
    classifier = pickle.load(open("news_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer_1.pkl", "rb"))

    new_features = vectorizer.transform(x_new)

    # Get the predicted topic label
    proba = classifier.predict_proba(new_features)

    categories = ["Business", "Science","Sports"]
    # Print the predicted category and its probability
    predicted_category = categories[np.argmax(proba)]

    if predicted_category == "Business":
        st.write("## :green[Business]💼")
    elif predicted_category == "Science":
        st.write("## :red[Science]🚀")
    else:
        st.write("## :blue[Sports]🏏")

button = st.button("Click here to predict news type [🏏,💼,🚀]",type="primary")

if button:
    if x_new != [""]:
        result()
    else:
        st.warning("enter any text blank spaces not allowed")