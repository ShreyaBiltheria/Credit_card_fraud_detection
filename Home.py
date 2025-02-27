import streamlit as st

def run():
    st.markdown("<h1 style='text-align: center;'>🏦 Welcome to Our Bank</h1>", unsafe_allow_html=True)
    st.image("bank_building.jpg", use_container_width=True)
    st.markdown("""
        <div style='text-align: center; font-size: 18px;'>
        Securely manage your transactions and detect fraud in real-time. <br>
        Use the sidebar to navigate through the platform.
        </div>
    """, unsafe_allow_html=True)
    st.button("🔐 Login")
    st.button("📝 Register")

if __name__ == "__main__":
    run()
