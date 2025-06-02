import streamlit as st
def login_form():
    st.sidebar.subheader("🔐 Iniciar Sesión")
    user = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")
    return user == "admin" and password == "admin"
