import streamlit as st


#________PAGES_________

about = st.Page(
    page = "views/0-about.py",
    title = "About Me",
    icon = "😎",
    default= True,
)

page1 = st.Page(
    page = "views/1-linear regression.py",
    title = "Real Estate Price Estimation",
    icon = "🏠",
)

page2 = st.Page(
    page = "views/2-logistic regression.py",
    title = "Heart Disease Detection",
    icon = "❤",
)

page3 = st.Page(
    page = "views/3-boosting.py",
    title = "Parkinson's Detection",
    icon = "👴",
)

page4 = st.Page(
    page = "views/4-SVM.py",
    title = "Diabetes Detection",
    icon = "💉",
)

page5 = st.Page(
    page = "views/5-KNN.py",
    title = "Iris Species Classification",
    icon = "🌷",
)

page6 = st.Page(
    page = "views/6-Kmeans.py",
    title = "Customer Segmentation",
    icon = "👱‍♂️",
)

page7 = st.Page(
    page = "views/7-ann.py",
    title = "Credit Card Default Detection",
    icon = "💳",
)

page8 = st.Page(
    page = "views/8-cnn.py",
    title = "Pneumonia Detection",
    icon = "👩‍⚕️",
)

page9 = st.Page(
    page = "views/9-rnn.py",
    title = "Stock Price Prediction",
    icon = "📈",
)

page10 = st.Page(
    page = "views/10-nlp.py",
    title = "Spam Detection",
    icon = "📩",
)

page11 = st.Page(
    page = "views/11-llm.py",
    title = "Chatbot",
    icon = "🤖",
)

page12 = st.Page(
    page = "views/12-recommender.py",
    title = "Movie Recommender",
    icon = "🎬",
)


#______NAVIGATION_______

pg = st.navigation(
    {
        "Info" : [about],
        "Regression" : [page1,page2],
        "Classification" : [page3,page4,page5],
        "Clustering" : [page6],
        "Neural Networks" : [page7,page8,page9],
        "Natural Language Processing" : [page10],
        "Large Language Models" : [page11],
        "Recommender System" : [page12],
    }
)

st.logo("assets/sidebar_top.jpg")
st.sidebar.text("Made with streamlit by Aritra")
pg.run()