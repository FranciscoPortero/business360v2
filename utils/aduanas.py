import streamlit as st
import pandas as pd
def mostrar_importaciones():
    df = pd.DataFrame({
        "País Origen": ["China", "EEUU"],
        "Valor FOB": [15000, 22000],
        "Año": [2022, 2023]
    })
    st.dataframe(df)
