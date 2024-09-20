import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

st.title("Spam Detection",anchor=False)

loaded_model = load_model(r'C:\Users\HP\Desktop\projects\z_app\models\model10.keras')        #get the model
with open(r'C:\Users\HP\Desktop\projects\z_app\models\model10_tokenizer.pkl','rb') as f:        #get the scaler object
    tokenizer = pickle.load(f)



@st.dialog("Predicted result ")
def predict(arr):
    sequence = tokenizer.texts_to_sequences([arr])
    T = 189
    padded_sequence = pad_sequences(sequence, maxlen=T)  # Ensure the sequence has the correct length

    # Make a prediction using the trained model
    prediction = loaded_model.predict(padded_sequence)

    # Print the prediction (it will be a probability between 0 and 1)
    print("Prediction (probability):", prediction)

    # Determine if it's spam (1) or ham (0)
    threshold = 0.5  # You can adjust this threshold based on performance
    if prediction >= threshold:
        st.write("This is spam.❌")
    else:
        st.write("Smells like ham.✔")



data = st.text_input("Enter text")

if st.button("Analyse data"):
    predict(data)


#Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def add_bg_from_local_image(image_path):
    encoded_image = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_image});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local_image('assets/bg10.jpg')