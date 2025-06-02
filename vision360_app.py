import streamlit as st
import pandas as pd
from actividad_loader import obtener_actividades
from empresas_loader import obtener_empresas

st.set_page_config(page_title="Business360", layout="wide")
st.title("📊 Business360 - Análisis Empresarial 360°")

# Filtros
st.sidebar.header("🔎 Filtros")
actividades = obtener_actividades()
actividad_seleccionada = st.sidebar.selectbox("Selecciona una actividad económica:", [a["descripcion"] for a in actividades])

empresas = obtener_empresas()
empresas_filtradas = [e for e in empresas if actividad_seleccionada in e["razon_social"]]
empresa_seleccionada = st.sidebar.selectbox("Selecciona una empresa:", [e["razon_social"] for e in empresas_filtradas])

st.subheader("📌 Información General")
st.write(f"Actividad seleccionada: **{actividad_seleccionada}**")
st.write(f"Empresa seleccionada: **{empresa_seleccionada}**")

# Simulación de análisis
st.subheader("📈 Análisis Financiero")
st.bar_chart(pd.DataFrame({
    "Ventas": [100, 120, 130],
    "Costos": [60, 70, 75]
}, index=["2021", "2022", "2023"]))

st.subheader("📊 Datos Aduaneros (Simulados)")
st.dataframe(pd.DataFrame({
    "País Origen": ["China", "EEUU"],
    "Valor FOB": [15000, 22000],
    "Año": [2022, 2023]
}))

st.subheader("📉 Indicadores Macroeconómicos (Simulados)")
st.line_chart(pd.DataFrame({
    "PIB (mill USD)": [95000, 97000, 99000],
    "Exportaciones": [25000, 26500, 28000]
}, index=["2021", "2022", "2023"]))
