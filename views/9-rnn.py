import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
from tensorflow.keras.models import load_model
import pickle
import matplotlib.pyplot as plt

#st.title("Recurrent Neural Networks",anchor = False)

loaded_model = load_model(r'C:\Users\HP\Desktop\projects\z_app\models\model9.keras')

with open(r'C:\Users\HP\Desktop\projects\z_app\models\model9_scaler.pkl','rb') as f:
    sc = pickle.load(f)



def predict(stats):
    dataset_train = pd.read_csv(stats)

    dataset_test = pd.read_csv(r'C:\Users\HP\Desktop\projects\z_app\data\Google_Stock_Price_Test.csv')
    real_stock_price = dataset_test.iloc[:, 1:2].values
    dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)
    inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values   
    inputs = inputs.reshape(-1,1)
    inputs = sc.transform(inputs)
    X_test = []
    for i in range(60, 80):
        X_test.append(inputs[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_stock_price = loaded_model.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    fig, ax = plt.subplots()
    #ax.plot(real_stock_price, color='red', label='Real Google Stock Price')
    ax.plot(predicted_stock_price, color='blue', label='Predicted Google Stock Price')
    ax.set_title('Google Stock Price Prediction')
    ax.set_xlabel('Time')
    ax.set_ylabel('Google Stock Price')
    ax.legend()
    st.pyplot(fig)



stonks = st.file_uploader("Choose a file")
if stonks:
    if st.button("Analyse data"):
        predict(stonks)


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

add_bg_from_local_image('assets/bg14.jpg')