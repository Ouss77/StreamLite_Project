import streamlit as st
# Create an empty container
placeholder = st.empty()

actual_user = "admin"
actual_password = "admin"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    admin = st.text_input("Name")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and admin == actual_user and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
elif submit and admin != actual_user and password != actual_password:
    st.error("Login failed")
else:
    pass