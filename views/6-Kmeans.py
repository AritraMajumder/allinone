import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.title("K Means Clustering",anchor=False)

file = st.file_uploader('Choose a file')
if file:
    df = pd.read_csv(file)
    x = df.iloc[:,[3,4]].values

    wcss=[]
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i,init="k-means++",random_state=42)
        kmeans.fit(x)

        wcss.append(kmeans.inertia_)

    fig, ax = plt.subplots()
    ax.plot(range(1, 11), wcss, marker='o')  # Adding markers for clarity
    ax.set_title("Elbow Graph")
    ax.set_xlabel("Number of Clusters")
    ax.set_ylabel("WCSS")

    # Display the plot in Streamlit
    st.pyplot(fig)

    k = int(st.number_input("Number of clusters"))

    if st.button("Plot clusters:"):
        km = KMeans(n_clusters=k,init="k-means++",random_state=42)
        y = km.fit_predict(x)

        fig, ax = plt.subplots(figsize=(10, 10))

        # Plot cluster points
        ax.scatter(x[y == 0, 0], x[y == 0, 1], s=50, c='green', label='Cluster 1')
        ax.scatter(x[y == 1, 0], x[y == 1, 1], s=50, c='red', label='Cluster 2')
        ax.scatter(x[y == 2, 0], x[y == 2, 1], s=50, c='yellow', label='Cluster 3')
        ax.scatter(x[y == 3, 0], x[y == 3, 1], s=50, c='blue', label='Cluster 4')
        ax.scatter(x[y == 4, 0], x[y == 4, 1], s=50, c='orange', label='Cluster 5')

        # Plot centroids
        ax.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=100, c='cyan', label='Centroids')

        # Axis labels
        ax.set_title("Customer Groups")
        ax.set_xlabel("Annual Income")
        ax.set_ylabel("Spending Score")
        ax.legend()

        st.pyplot(fig)

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

add_bg_from_local_image('assets/bg8.png')