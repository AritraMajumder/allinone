import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
from tensorflow.keras.models import load_model
import pickle

st.title("Artificial Neural Networks",anchor = False)
loaded_model = load_model(r'C:\Users\HP\Desktop\projects\z_app\models\model7.keras')        #get the model
with open(r'C:\Users\HP\Desktop\projects\z_app\models\model7_scaler.pkl','rb') as f:        #get the scaler object
    sc = pickle.load(f)

@st.dialog("Predicted result ")
def predict(arr):
    res = loaded_model.predict(sc.transform([arr]))>0.5
    st.write(res[0][0])

#input gender
genders = ['Male','Female']
gender = st.selectbox('Gender', genders)
if gender=='Female':
    gender = 0 
else:
    gender = 1

#input location
locations = ['France','Germany','Spain']
location = st.selectbox('Location', locations)
dummy = [0, 0, 0]
dummy[locations.index(location)] = 1

#input credit score
cred = int(st.number_input("Credit Score"))
data = st.text_input("Enter details")
if st.button("Analyse data"):
    dummy.append(cred)
    dummy.append(gender)
    data = [float(i) for i in data.split(",")]
    params = dummy+data
    predict(params)
    

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

add_bg_from_local_image('assets/bg9.jpeg')

#619,France,Female,42,2,0,1,1,1,101348.88,0         false


#502,France,Female,42,8,159660.8,3,1,0,113931.57,1   true

