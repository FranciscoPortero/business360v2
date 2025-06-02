import streamlit as st
import pandas as pd
def mostrar_contratacion_publica():
    df = pd.DataFrame({
        "Entidad": ["Ministerio Salud", "Municipio Quito"],
        "Objeto": ["Equipos médicos", "Obras públicas"],
        "Monto": [50000, 150000]
    })
    st.dataframe(df)
