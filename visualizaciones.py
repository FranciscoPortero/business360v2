import streamlit as st
import pandas as pd
def mostrar_dashboard_financiero():
    df = pd.DataFrame({
        "Año": ["2021", "2022", "2023"],
        "Ventas": [100000, 120000, 140000],
        "Utilidad Neta": [15000, 18000, 22000],
        "ROE": [0.10, 0.12, 0.14]
    }).set_index("Año")
    st.line_chart(df)
    st.dataframe(df)
