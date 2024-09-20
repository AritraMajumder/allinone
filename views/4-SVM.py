import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

st.title("Support Vector Machines",anchor=False)

with open(r'C:\Users\HP\Desktop\projects\z_app\models\model4', 'rb') as f:
    loaded_model = pickle.load(f)

@st.dialog("Predicted result ")
def predict(arr):
    arr = np.array([arr])

    res = loaded_model.predict(arr)
    if res==1:
        st.write("Diabetes highly likely")
    else:
        st.write("Diabetes highly unlilkely")
      


data = st.text_input("Enter details")
if st.button("Analyse data"):
    data_values =[float(i) for i in data.split(",")]
    categories = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    
    predict(data_values)

    view = dict(zip(categories,data_values))
    df = pd.DataFrame([view])
    st.write(df)


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

add_bg_from_local_image('assets/bg6.png')