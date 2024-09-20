import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pickle

st.title("Convolution Neural Networks",anchor = False)

loaded_model = load_model(r'C:\Users\HP\Desktop\projects\z_app\models\model8.keras')        #get the model

@st.dialog("Predicted result ")
def predict(img):
    test_image = image.load_img(img, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = loaded_model.predict(test_image)

    if result[0][0] == 1:
        prediction = 'High likelihood of pneumonia'
    else:
        prediction = 'Low likelihood of pneumonia'

    st.write(prediction)


uploaded_file = st.file_uploader("Choose a file")

if st.button("Analyse image"):
    predict(uploaded_file)


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

add_bg_from_local_image('assets/bg13.jpg')