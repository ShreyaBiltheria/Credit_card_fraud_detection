import streamlit as st
from streamlit_option_menu import option_menu


import Home,Login,Register, app, Help, Guidelines
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")


# Custom CSS
st.markdown("""
    <style>
    .stApp { background-color: #f5f7fa; }
    .css-1d391kg { background-color: #001f3f !important; }
    .css-1d391kg h1 { color: white !important; }
    h1 { color: #002f5f; font-size: 2.5rem; }
    .stButton>button { background-color: #002f5f; color: white; border-radius: 10px; font-size: 18px; padding: 10px; }
    .stButton>button:hover { background-color: #004080; }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("bank_logo.png", use_container_width=True)
    
    selected = option_menu(
        menu_title="🏦 Banking Services",
        options=["Home", "Login", "Register", "Verify Transaction", "Help", "Guidelines"],
        icons=["house", "key", "person-plus", "credit-card", "question-circle", "file-earmark-text"],
        menu_icon="cast",
        default_index=0,
    )

# Load the selected page
if selected == "Home":
    Home.run()
elif selected == "Login":
    Login
elif selected == "Register":
    Register.run()
elif selected == "Verify Transaction":
    app.run()
elif selected == "Help":
    Help.run()
elif selected == "Guidelines":
    Guidelines.run()
