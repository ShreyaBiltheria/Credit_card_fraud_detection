import streamlit as st

def run():
    st.markdown("<h1 style='text-align: center;'>📝 Create an Account</h1>", unsafe_allow_html=True)
    
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email Address")
    password = st.text_input("🔑 Password", type="password")

    if st.button("📝 Register"):
        st.success("✅ Registration Successful! You can now login.")

if __name__ == "__main__":
    run()
