import streamlit as st

def email_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_input("Your Message")
        submit = st.form_submit_button("Submit")

        if submit:
            st.success("Message sent!")