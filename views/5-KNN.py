import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

st.title("K Nearest Neighbours",anchor=False)

with open(r'C:\Users\HP\Desktop\projects\z_app\models\model5', 'rb') as f:
    loaded_model = pickle.load(f)

@st.dialog("Predicted result ")
def predict(arr):
    arr = [float(i) for i in arr]
    arr = np.array([arr])

    res = loaded_model.predict(arr)[0]
    st.write(res)
      


SepalLengthCm = st.number_input("SepalLengthCm")
SepalWidthCm = st.number_input("SepalWidthCm")
PetalLengthCm = st.number_input("PetalLengthCm")
PetalWidthCm = st.number_input("PetalWidthCm")

features = [SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]
if st.button("Get results"):
    predict(features)


# Function to encode image to base64
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

add_bg_from_local_image('assets/bg7.jpg')