import streamlit as st
from forms.contact import email_form

@st.dialog("Contact Me")
def email_display():
    email_form()

#_______________BIO_______________
c1,c2 = st.columns(2, gap = "medium", vertical_alignment= "center")

with c1:
    st.image("assets/headshot1.png",width=230)

with c2:
    st.title("Aritra Majumder", anchor=False)
    st.write(
        " Passionate data science enthusiast, driven by curiosity and committed to exploring the wide-ranging applications of Artificial Intelligence and Machine Learning. Excited to see where these technologies can take us!"
    )

    if st.button(" Contact Me 📧"):
        email_display()
    
#_________ACADEMIC DETAILS_________

st.write("\n")
st.subheader("Academic Qualifications", anchor=False)
st.write(
    """
    -10th CBSE: 89.6% \n
    -12th CBSE: 95.5% \n
    -CGPA(7th sem): 8.88 \n
    -VELLORE INSTITUTE OF TECHNOLOGY | B.Tech CSE (2021-2025) \n
    """
)

#______________SKILLS______________

st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """ 
    -Programming Language: Python \n
    -Machine Learning Tools: Tensorflow, Scikit Learn, Python Streamlit library, Open CV \n
    -Vizualization Tools - Power BI, Tableau, Seaborn, Matplotlib \n
    """
)

#_____________PROJECTS_____________

st.write("\n")
st.subheader("Projects", anchor=False)
st.write(
    """
    -Machine Learning: Regression, Classification, Clustering tasks\n
    -Deep Learning: Neural Networks, Natural Language Processing\n
    -Large Language Models\n
    -Recommender Systems\n
    -Data Visualization Dashboards
    """
)

import base64


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

add_bg_from_local_image('assets/bg2.jpg')
