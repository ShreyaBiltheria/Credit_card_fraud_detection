import streamlit as st

def run():
    st.markdown("<h1 style='text-align: center;'>📜 Security Guidelines</h1>", unsafe_allow_html=True)
    st.markdown("""
        - Use strong passwords 🔑  
        - Never share your OTP or CVV 🛡️  
        - Monitor transactions regularly 📊  
        - Report suspicious activity immediately 🚨  
    """)

if __name__ == "__main__":
    run()
