import streamlit as st
import pickle
import numpy as np
import base64

st.title("Logistic Regression",anchor=False)
st.write("Using medical data like age, resting blood pressure, cholesterol etc we leverage a Logistic Regression model to predic the chances of a heart disease.")
st.write('\n')
st.write('\n')
st.write('\n')
#load model
with open(r'C:\Users\HP\Desktop\projects\z_app\models\model2', 'rb') as f:
    loaded_model = pickle.load(f)

@st.dialog("Chances of a heart disease ")
def predict(arr):
    res = str(round(loaded_model.predict(arr)[0]*100,2))
    res = res+"%"
    st.write(res)

#ip = (42,1,2,120,240,1,1,194,0,0.8,0,0,3)
#ip_data = np.asarray(ip)

age	= st.number_input('Age')
sex	= st.number_input('Sex')
cp	= st.number_input('Chest Pain Type')
trestbps	= st.number_input('Resting Blood Pressure (in mm Hg)')
chol	= st.number_input('Serum Cholesterol')
fbs	= st.number_input('Fasting Blood Sugar')
restecg	= st.number_input('Resting Electrocardiographic Results')
thalach	= st.number_input('Maximum Heart Rate Achieved')
exang	= st.number_input('Exercise Induced Angina')
oldpeak	= st.number_input('Depression of ST Segment')
slope	= st.number_input('Slope of the Peak Exercise ST Segment')
ca	 = st.number_input('Number of Major Vessels Colored by Fluoroscopy')
thal = st.number_input('Thalassemia')

ip = (age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
ip_data = np.asarray(ip)

#getting probability
if st.button("Analyse data"):
    predict(ip_data)

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

add_bg_from_local_image('assets/bg4.jpg')
