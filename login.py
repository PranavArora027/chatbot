import streamlit as st
from dotenv import load_dotenv
import pyrebase
from st_pages import hide_pages
import os

st.session_state.sbstate = 'collapsed'
st.set_page_config(page_title='LOGIN', page_icon='👤', initial_sidebar_state=st.session_state.sbstate)


# Load environment variables
load_dotenv()

# Initialize Firebase
firebaseConfig = {
  'apiKey': os.getenv('apiKey'),
  'authDomain': os.getenv('authDomain'),
  'projectId': os.getenv('projectId'),
  'databaseURL': os.getenv('databaseURL'),
  'storageBucket': os.getenv('storageBucket'),
  'messagingSenderId': os.getenv('messagingSenderId'),
  'appId': os.getenv('appId'),
  'measurementId': os.getenv('measurementId')
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

hide_pages("bot.py")

# Streamlit app title
st.title("ChatGPT-like clone")

# Dropdown for action selection
action = st.selectbox("Select Action", ["Login", "Sign Up"])

# Email and password input fields
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Perform action based on selection
if action == "Sign Up":
    if st.button("Sign Up"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Successfully signed up! Please log in.")
        except Exception as e:
            st.error(f"Error signing up: {e}")
elif action == "Login":
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Logged in successfully!")
            st.switch_page("pages/bot.py")
        except Exception as e:
            st.error(f"Error logging in: {e}")
