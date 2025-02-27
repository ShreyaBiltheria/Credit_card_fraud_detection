import streamlit as st

def login_page():
    """Login Page for User Authentication"""
    st.title("🔐 Login Page")

    # Login form
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("✅ Login successful! Redirecting...")
        else:
            st.error("❌ Invalid credentials, please try again.")

# ✅ Ensure this function runs only if the file is executed directly
if __name__ == "__main__":
    login_page()
