import streamlit as st
import numpy as np
import pandas as pd
import pickle
import base64

st.title("Linear Regression",anchor=False)
st.write("Using information about location, area in square feet, number of bathrooms, and bhk we leverage a Linear Regression model to calculate price of real estate in Bangalore.")
st.write('\n')
st.write('\n')
st.write('\n')
         
#load model
with open(r'C:\Users\HP\Desktop\projects\z_app\models\model1', 'rb') as f:
    loaded_model = pickle.load(f)

#need the modified file
X = pd.read_csv(r'C:\Users\HP\Desktop\projects\z_app\data\Bengaluru_final.csv')

@st.dialog("Estimated Price ")
def predict_price(location,sqft,bath,bhk):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    price = str(round(loaded_model.predict([x])[0],2))
    price = "Rs "+price+" lacs"
    st.write(price)

locations = (X.columns[3:])
#print(predict_price('Indira Nagar',1000,3,3))
location = st.selectbox('Enter Location', locations)

sqft = st.number_input('Enter area')

bath = st.number_input('Enter baths')

bhk = st.number_input('Enter bhk')

if st.button("Calculate price"):
    predict_price(location,sqft,bath,bhk)

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

add_bg_from_local_image('assets/bg3.jpg')
