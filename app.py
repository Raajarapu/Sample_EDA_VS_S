import streamlit as st

# --- LOGIN PAGE ---
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "1234":  # simple demo
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    st.success("Login Successful!")
    st.switch_page("pages/eda.py")   # we will build EDA in another file
