import streamlit as st
import pandas as pd
def mostrar_macro():
    st.write("Indicadores macroeconómicos simulados")
    df = pd.DataFrame({
        "PIB": [95, 98, 101],
        "Exportaciones": [25, 26.5, 28]
    }, index=["2021", "2022", "2023"])
    st.bar_chart(df)
